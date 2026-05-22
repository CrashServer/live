#!/usr/bin/env python3
"""Tiny HTTP server for the grid cell editor.

Serves editor.html and exposes /api/cells for read/write.
Independent of webTroop — runs in its own process on port 1235.

Start with:    python3 grid/serve.py
Then open:     http://localhost:1235

After editing, run `compo.cell_reload()` in your FoxDot session
to pick up changes (or it auto-reloads on next call by mtime).
"""
import json
import os
import sys
import tempfile
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

GRID_DIR = Path(__file__).resolve().parent
CELLS_FILE = GRID_DIR / "cells.json"
EDITOR_HTML = GRID_DIR / "editor.html"
PORT = 1235


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # quieter logs
        sys.stderr.write(f"[grid-editor] {self.address_string()} - {fmt % args}\n")

    def _send_json(self, obj, status=200):
        body = json.dumps(obj, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path, content_type="text/html; charset=utf-8"):
        try:
            body = path.read_bytes()
        except FileNotFoundError:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/" or p == "/index.html":
            self._send_file(EDITOR_HTML)
        elif p == "/api/cells":
            try:
                data = json.loads(CELLS_FILE.read_text())
            except Exception:
                data = {}
            self._send_json(data)
        else:
            self.send_error(404)

    def do_POST(self):
        p = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")

        if p == "/api/generate":
            try:
                payload = json.loads(body) if body.strip() else {}
            except Exception as e:
                self._send_json({"error": f"bad json: {e}"}, status=400)
                return
            try:
                import sys as _sys
                if str(GRID_DIR) not in _sys.path:
                    _sys.path.insert(0, str(GRID_DIR))
                from generate import generate as _gen
                try:
                    cells = json.loads(CELLS_FILE.read_text())
                except Exception:
                    cells = {}
                code, meta = _gen(
                    cells,
                    seed_coord=payload.get("seed"),
                    bars=payload.get("bars"),
                    rng_seed=payload.get("rng_seed"),
                )
                self._send_json({"ok": True, "code": code, "meta": meta})
            except Exception as e:
                import traceback
                self._send_json({"error": str(e), "trace": traceback.format_exc()}, status=500)
            return

        if p != "/api/cells":
            self.send_error(404)
            return
        try:
            payload = json.loads(body)
        except Exception as e:
            self._send_json({"error": f"bad json: {e}"}, status=400)
            return

        # Expected payload: {"coord": "B32", "code": "...", "label": "..."}
        # Or for delete: {"coord": "B32", "delete": true}
        coord = payload.get("coord")
        if not coord:
            self._send_json({"error": "missing coord"}, status=400)
            return

        try:
            cells = json.loads(CELLS_FILE.read_text())
        except Exception:
            cells = {}

        if payload.get("delete"):
            cells.pop(coord, None)
            action = "deleted"
        else:
            # Merge: preserve existing metadata, overlay any sent fields.
            # Empty-string values from the UI are treated as "keep existing"
            # for metadata fields; code and label are always written.
            existing = cells.get(coord, {})
            updated = dict(existing)
            updated["code"]  = payload.get("code", "")
            updated["label"] = payload.get("label", "")
            for field in ("tempo", "key", "type", "instrument", "source",
                          "scale", "root"):
                v = payload.get(field)
                if v is not None and v != "":
                    updated[field] = v
            cells[coord] = updated
            action = "saved"

        # Atomic write
        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(cells, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)

        self._send_json({"ok": True, "coord": coord, "action": action})

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def main():
    httpd = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"grid-editor serving on http://localhost:{PORT}")
    print(f"cells file:  {CELLS_FILE}")
    print("Ctrl-C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()

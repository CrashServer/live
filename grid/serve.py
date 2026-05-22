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

GRID_DIR    = Path(__file__).resolve().parent
CELLS_FILE  = GRID_DIR / "cells.json"
EDITOR_HTML = GRID_DIR / "editor.html"
CODEBANK_DIR = Path.home() / "live" / "codeBank"
PORT = 1235

_BPM_RE   = __import__("re").compile(r'Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)')
_SCALE_RE = __import__("re").compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
_ROOT_RE  = __import__("re").compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')


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

        if p == "/api/codebank/sync":
            self._handle_codebank_sync()
            return

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
                    max_players=payload.get("max_players", 5),
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
                          "scale", "root", "source_file", "attack_category"):
                v = payload.get(field)
                if v is not None and v != "":
                    updated[field] = v
            # is_attack is boolean — explicit False is meaningful
            if "is_attack" in payload:
                updated["is_attack"] = bool(payload["is_attack"])
            cells[coord] = updated
            action = "saved"

        # Atomic write
        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(cells, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)

        # Two-way sync: if this cell mirrors a codeBank file, write it back
        if action == "saved":
            src = cells[coord].get("source_file")
            if src:
                cb_path = CODEBANK_DIR / src
                try:
                    cb_path.write_text(cells[coord].get("code", ""), encoding="utf-8")
                    sys.stderr.write(f"[grid-editor] wrote back → codeBank/{src}\n")
                except Exception as e:
                    sys.stderr.write(f"[grid-editor] writeback failed {src}: {e}\n")

        self._send_json({"ok": True, "coord": coord, "action": action})

    def _handle_codebank_sync(self):
        try:
            cells = json.loads(CELLS_FILE.read_text())
        except Exception:
            cells = {}

        # Build index: source_file → coord
        file_to_coord = {
            v["source_file"]: k
            for k, v in cells.items()
            if isinstance(v, dict) and v.get("source_file")
        }

        def _next_free_q():
            for i in range(400):
                coord = f"Q{i}"
                if coord not in cells:
                    return coord
            return None

        def _extract_meta(code):
            bpms   = _BPM_RE.findall(code)
            scales = _SCALE_RE.findall(code)
            roots  = _ROOT_RE.findall(code)
            tempo  = int(bpms[0]) if bpms else None
            scale  = scales[0] if scales else None
            root   = roots[0].strip("\"'") if roots else None
            key    = None
            if root and scale: key = f"{root} {scale}"
            elif root:         key = root
            elif scale:        key = scale
            return tempo, scale, root, key

        updated_count = 0
        created_count = 0
        errors = []

        if not CODEBANK_DIR.exists():
            self._send_json({"error": f"codeBank not found at {CODEBANK_DIR}"}, status=500)
            return

        for py_file in sorted(CODEBANK_DIR.glob("*.py")):
            filename = py_file.name
            try:
                code = py_file.read_text(errors="replace")
            except Exception as e:
                errors.append(f"{filename}: {e}")
                continue
            if len(code.strip().splitlines()) < 2:
                continue  # skip blank files

            if filename in file_to_coord:
                coord = file_to_coord[filename]
                cells[coord]["code"] = code
                updated_count += 1
            else:
                coord = _next_free_q()
                if coord is None:
                    errors.append(f"{filename}: no free Q slot (grid full)")
                    continue
                tempo, scale, root, key = _extract_meta(code)
                cells[coord] = {
                    "code": code,
                    "label": py_file.stem,
                    "type": "track",
                    "source": "codeBank",
                    "source_file": filename,
                    "tempo": tempo,
                    "key": key,
                    "scale": scale,
                    "root": root,
                }
                file_to_coord[filename] = coord
                created_count += 1

        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(cells, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)

        sys.stderr.write(
            f"[grid-editor] codebank sync: {updated_count} updated, "
            f"{created_count} created, {len(errors)} errors\n"
        )
        self._send_json({
            "ok": True,
            "updated": updated_count,
            "created": created_count,
            "errors": errors,
            "total": updated_count + created_count,
        })

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

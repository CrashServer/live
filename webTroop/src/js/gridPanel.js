/* Grid Panel — embeds the standalone grid editor (served by
 * /home/svdk/live/grid/serve.py on port 1235) inside webTroop
 * as a toggleable side panel.
 *
 * Toggle via:
 *   - the "Toggle Grid Panel" switch in the config panel
 *   - keyboard shortcut Ctrl+G (Cmd+G on macOS)
 *
 * The iframe runs the editor isolated; it talks to its own
 * Python HTTP server for read/write on cells.json. The Test
 * button in the editor copies a `compo.cell_run('...')` command
 * to the clipboard for pasting into webTroop's CodeMirror.
 *
 * Requirements: `python3 /home/svdk/live/grid/serve.py` running
 * on port 1235 (separate process). If it's not up, the iframe
 * shows the browser's connection-refused page.
 */

import "../css/gridPanel.css";
import { EventEmitter } from "./eventBus.js";

const EDITOR_URL = "http://localhost:1235";

// ===== Listen for test-fire requests from the iframe editor =====
// The iframe (origin http://localhost:1235) posts a message of the form
//   { type: 'gridTest', code: '...', coord: 'B32' }
// and waits ~400ms for an ack. We forward `code` to FoxDot via the existing
// EventEmitter('send_foxdot') bridge that main.js wires to wsServer.

window.addEventListener("message", (e) => {
    if (!e.data) return;
    // Origin check — accept only the editor server we know
    try {
        const url = new URL(e.origin);
        if (url.hostname !== "localhost" || url.port !== "1235") return;
    } catch (_) {
        return;
    }

    if (e.data.type === "gridTest") {
        const { code, coord } = e.data;
        if (!code) return;
        EventEmitter.emit("send_foxdot", code);
        console.log(`[gridPanel] fired ${coord} via send_foxdot`);
        try {
            e.source.postMessage({ type: "gridTestAck", coord }, e.origin);
        } catch (err) {
            console.warn("[gridPanel] ack failed:", err);
        }
    } else if (e.data.type === "gridPaste") {
        const { code, coord } = e.data;
        if (!code) return;
        // Insert into webTroop's main CodeMirror editor without evaluating
        EventEmitter.emit("paste_to_editor", code);
        console.log(`[gridPanel] pasted ${coord} into editor`);
        try {
            e.source.postMessage({ type: "gridPasteAck", coord }, e.origin);
        } catch (err) {
            console.warn("[gridPanel] ack failed:", err);
        }
    } else if (e.data.type === "gridReload") {
        // Cell was saved/deleted in the iframe — pull the new cells.json
        // into FoxDot's in-memory grid so the next cell_run() sees it.
        const { coord, kind } = e.data;
        EventEmitter.emit("send_foxdot", "compo.cell_reload()");
        console.log(`[gridPanel] auto-reload after ${kind} ${coord}`);
    }
});

function createGridPanel() {
    if (document.getElementById("gridPanel")) return; // idempotent

    const panel = document.createElement("aside");
    panel.id = "gridPanel";
    panel.className = "grid-panel";

    const header = document.createElement("div");
    header.className = "grid-panel-header";
    header.innerHTML = `
        <h2>cell grid</h2>
        <span class="spacer"></span>
        <button id="gridPanelReload" title="reload iframe">reload</button>
        <button id="gridPanelExternal" title="open in new tab">↗</button>
        <button class="close-btn" id="gridPanelClose" title="close (Ctrl+Shift+Y)">×</button>
    `;

    const iframe = document.createElement("iframe");
    iframe.id = "gridPanelFrame";
    // Lazy-loaded on first open — don't load editor until panel is actually used

    const status = document.createElement("div");
    status.className = "grid-panel-status";
    status.id = "gridPanelStatus";
    status.textContent = `editor @ ${EDITOR_URL}`;

    // Resize handle on the left edge
    const resizeHandle = document.createElement("div");
    resizeHandle.className = "grid-panel-resize";
    panel.appendChild(resizeHandle);

    panel.appendChild(header);
    panel.appendChild(iframe);
    panel.appendChild(status);
    document.body.appendChild(panel);

    // Restore saved width (persisted across sessions)
    const savedWidth = localStorage.getItem("gridPanelWidth");
    if (savedWidth) panel.style.width = savedWidth;

    // Drag-to-resize.
    // Key: disable pointer-events on the iframe while dragging so it doesn't
    // swallow mousemove events when the cursor moves over it (which broke
    // dragging inward / making the panel smaller).
    let resizing = false;
    resizeHandle.addEventListener("mousedown", (e) => {
        resizing = true;
        resizeHandle.classList.add("dragging");
        document.body.style.cursor = "ew-resize";
        document.body.style.userSelect = "none";
        iframe.style.pointerEvents = "none";
        e.preventDefault();
    });
    document.addEventListener("mousemove", (e) => {
        if (!resizing) return;
        const w = window.innerWidth - e.clientX;
        const clamped = Math.max(320, Math.min(window.innerWidth - 200, w));
        panel.style.width = clamped + "px";
        _syncMainMargin(clamped);
    }, { passive: true });
    document.addEventListener("mouseup", () => {
        if (!resizing) return;
        resizing = false;
        resizeHandle.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
        iframe.style.pointerEvents = "";
        localStorage.setItem("gridPanelWidth", panel.style.width);
    });

    // Wire up close button
    document.getElementById("gridPanelClose").addEventListener("click", () => {
        toggleGridPanel(false);
    });

    // Wire up reload
    document.getElementById("gridPanelReload").addEventListener("click", () => {
        iframe.src = iframe.src;
    });

    // Open in new tab
    document.getElementById("gridPanelExternal").addEventListener("click", () => {
        window.open(EDITOR_URL, "_blank");
    });

    // Forward current webTroop theme to iframe on load, and on every theme change.
    function sendTheme() {
        const cls = document.documentElement.className || "";
        const match = cls.match(/(\S+-theme)/);
        const theme = match ? match[1] : "dark";
        try { iframe.contentWindow.postMessage({ type: "setTheme", theme }, "*"); } catch (_) {}
    }
    iframe.addEventListener("load", sendTheme);
    new MutationObserver(sendTheme).observe(document.documentElement, {
        attributes: true, attributeFilter: ["class"]
    });

}

function toggleGridPanel(force) {
    const panel = document.getElementById("gridPanel");
    if (!panel) return;
    if (force === undefined) {
        panel.classList.toggle("visible");
    } else {
        panel.classList.toggle("visible", force);
    }
    const open = panel.classList.contains("visible");

    // Lazy-load: only fetch the editor on first open
    if (open) {
        const iframe = document.getElementById("gridPanelFrame");
        const status = document.getElementById("gridPanelStatus");
        if (iframe && !iframe.src) {
            // Probe the grid server before loading the iframe — gives a clear
            // error instead of a blank browser "connection refused" page.
            fetch(EDITOR_URL + "/api/cells", { method: "HEAD", mode: "no-cors" })
                .then(() => {
                    iframe.src = EDITOR_URL;
                    if (status) {
                        status.className = "grid-panel-status";
                        status.textContent = `editor @ ${EDITOR_URL}`;
                    }
                })
                .catch(() => {
                    if (status) {
                        status.className = "grid-panel-status err";
                        status.textContent = `grid server not running — start it with:  python3 grid/serve.py`;
                    }
                    // Show a helpful placeholder instead of a blank iframe
                    iframe.srcdoc = `<body style="margin:0;background:#111;color:#666;font-family:monospace;font-size:12px;display:flex;align-items:center;justify-content:center;height:100vh;text-align:center">
                        <div><div style="font-size:22px;margin-bottom:12px">grid server offline</div>
                        <div style="color:#444">python3 grid/serve.py</div></div></body>`;
                });
        }
    }

    _syncMainMargin(open ? (parseInt(panel.style.width) || 920) : 0);
}

function _syncMainMargin(width) {
    const mc = document.getElementById("main-container");
    if (mc) mc.style.marginRight = width ? width + "px" : "";
}

// ===== Toggle button injection into the config panel =====

function injectToggle() {
    // Find the existing toggle-group (in the config panel)
    const groups = document.querySelectorAll(".toggle-group");
    if (!groups.length) return;
    const group = groups[0];

    // Avoid double-injection
    if (document.getElementById("gridPanelToggle")) return;

    const item = document.createElement("div");
    item.className = "toggle-item";
    item.innerHTML = `
        <label>Toggle Grid Panel</label>
        <label class="toggle-switch">
            <input type="checkbox" id="gridPanelToggle"/>
            <span class="slider"></span>
        </label>
    `;
    group.appendChild(item);

    document.getElementById("gridPanelToggle").addEventListener("change", (e) => {
        toggleGridPanel(e.target.checked);
    });
}

// ===== Keyboard shortcut =====

document.addEventListener("keydown", (e) => {
    // Ctrl+Shift+Y toggles the panel — Ctrl+G is taken by CodeMirror findNext
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "y" || e.key === "Y")) {
        e.preventDefault();
        const wasVisible = document
            .getElementById("gridPanel")
            ?.classList.contains("visible");
        toggleGridPanel(!wasVisible);
        const tog = document.getElementById("gridPanelToggle");
        if (tog) tog.checked = !wasVisible;
    }
});

// ===== Rec Code + Rec Stems buttons (wired to compo.* via send_foxdot) =====

function wireRecButtons() {
    const codeBtn = document.getElementById("recordCode");
    const stemsBtn = document.getElementById("recStems");
    if (!codeBtn || !stemsBtn) return;

    // Local state mirrors the FoxDot-side recording state. We toggle on
    // click optimistically but always defer to the authoritative __REC_*
    // markers when they arrive from server.js via EventBus.
    let codeRecording = false;
    let stemsRecording = false;

    const setCodeUi = (on, label) => {
        codeRecording = on;
        codeBtn.classList.toggle("recording-active", on);
        codeBtn.textContent = on ? (label || "Recording…") : "Start";
    };
    const setStemsUi = (on, label) => {
        stemsRecording = on;
        stemsBtn.classList.toggle("recording-active", on);
        stemsBtn.textContent = on ? (label || "Recording…") : "Start";
    };

    codeBtn.addEventListener("click", () => {
        if (!codeRecording) {
            setCodeUi(true, "Recording…");
            EventEmitter.emit("send_foxdot", "compo.rec()");
        } else {
            setCodeUi(false);
            EventEmitter.emit("send_foxdot", "compo.rec_stop()");
        }
    });

    stemsBtn.addEventListener("click", () => {
        if (!stemsRecording) {
            const bars = parseInt(document.getElementById("recStemsBars").value, 10) || 16;
            const session = document.getElementById("recStemsSession").value.trim() || "scene";
            const variation = document.getElementById("recStemsVariation").value.trim() || "v1";
            const cmd = `compo.rec_stems(bars=${bars}, session="${session}", variation="${variation}")`;
            setStemsUi(true, `Recording ${bars}b…`);
            EventEmitter.emit("send_foxdot", cmd);
        } else {
            setStemsUi(false);
            EventEmitter.emit("send_foxdot", "compo.stem_stop()");
        }
    });

    // Auto-sync with authoritative state from server.js (which parses
    // __REC_START__ / __REC_STOP__ / __STEMS_START__ / __STEMS_STOP__
    // out of FoxDot's stdout). This means:
    //   - the code-rec button auto-reverts when compo.rec_stop() is called
    //     from anywhere (script eval, keyboard shortcut, etc.)
    //   - the stems button auto-reverts when the scheduled stop fires
    //     after `bars` beats (no need to click again)
    EventEmitter.on("rec_state", (msg) => {
        if (msg.recording) {
            setCodeUi(true, msg.bpm ? `Recording @${msg.bpm}` : "Recording…");
        } else {
            setCodeUi(false);
        }
    });
    EventEmitter.on("stems_state", (msg) => {
        if (msg.recording) {
            setStemsUi(true, `Recording ${msg.bars}b (${msg.players}p)`);
        } else {
            setStemsUi(false);
        }
    });
}

// ===== Bootstrap on DOM ready =====

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
        createGridPanel();
        injectToggle();
        wireRecButtons();
    });
} else {
    createGridPanel();
    injectToggle();
    wireRecButtons();
}

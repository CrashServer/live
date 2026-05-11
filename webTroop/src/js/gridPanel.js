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
    if (!e.data || e.data.type !== "gridTest") return;
    // Origin check — accept only the editor server we know
    try {
        const url = new URL(e.origin);
        if (url.hostname !== "localhost" || url.port !== "1235") return;
    } catch (_) {
        return;
    }
    const { code, coord } = e.data;
    if (!code) return;

    // Forward to FoxDot via the shared send_foxdot bus
    EventEmitter.emit("send_foxdot", code);
    console.log(`[gridPanel] fired ${coord} via send_foxdot`);

    // Ack back to the iframe so it can update its status
    try {
        e.source.postMessage({ type: "gridTestAck", coord }, e.origin);
    } catch (err) {
        console.warn("[gridPanel] ack failed:", err);
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
        <button class="close-btn" id="gridPanelClose" title="close (Ctrl+G)">×</button>
    `;

    const iframe = document.createElement("iframe");
    iframe.id = "gridPanelFrame";
    iframe.src = EDITOR_URL;

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

    // Drag-to-resize
    let resizing = false;
    resizeHandle.addEventListener("mousedown", (e) => {
        resizing = true;
        resizeHandle.classList.add("dragging");
        document.body.style.cursor = "ew-resize";
        document.body.style.userSelect = "none";
        e.preventDefault();
    });
    document.addEventListener("mousemove", (e) => {
        if (!resizing) return;
        const w = window.innerWidth - e.clientX;
        const clamped = Math.max(400, Math.min(window.innerWidth - 200, w));
        panel.style.width = clamped + "px";
    });
    document.addEventListener("mouseup", () => {
        if (!resizing) return;
        resizing = false;
        resizeHandle.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
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

    // Probe the server: if unreachable, hint at how to start it
    fetch(EDITOR_URL + "/api/cells", { method: "HEAD", mode: "no-cors" })
        .catch(() => {
            status.className = "grid-panel-status err";
            status.textContent = `editor server unreachable — run: python3 /home/svdk/live/grid/serve.py`;
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
    // Ctrl+G (or Cmd+G) toggles the panel
    if ((e.ctrlKey || e.metaKey) && (e.key === "g" || e.key === "G") && !e.shiftKey) {
        e.preventDefault();
        const wasVisible = document
            .getElementById("gridPanel")
            ?.classList.contains("visible");
        toggleGridPanel(!wasVisible);
        const tog = document.getElementById("gridPanelToggle");
        if (tog) tog.checked = !wasVisible;
    }
});

// ===== Bootstrap on DOM ready =====

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
        createGridPanel();
        injectToggle();
    });
} else {
    createGridPanel();
    injectToggle();
}

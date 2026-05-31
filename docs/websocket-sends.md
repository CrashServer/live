# WebSocket Message Types

There are two WebSocket connections in webTroop:

```
wsServer   →  ws://HOST_IP:1234   Node server.js  →  FoxDot Python
foxdotWs   →  ws://HOST_IP:PORT   Node server.js  →  CrashOS visuals
```

wsServer is the execution path. foxdotWs is visual-only (CrashOS) — guarded with
readyState check, safe to be disconnected.

---

## wsServer — messages TO server (client → server.js)

### evaluate_code
Sends code to FoxDot for execution.
```javascript
wsServer.send(JSON.stringify({
    type:      "evaluate_code",
    code:      "p1 >> dbass([0,4], oct=4)",
    userColor: "#3af",
    userName:  "svdk"
}));
```

### serverToggle
Toggle the FoxDot Python process on/off.
```javascript
wsServer.send(JSON.stringify({ type: "serverToggle" }));
```

### get_autocomplete
Request the full autocomplete list from FoxDot.
```javascript
wsServer.send(JSON.stringify({ type: "get_autocomplete" }));
```

---

## wsServer — messages FROM server (server.js → client)

Received in `wsServer.onmessage`:

```
type: "output"          FoxDot stdout line (text display)
type: "autocomplete"    autocomplete payload { loops, synthList, fxList, attackList }
type: "rec_state"       { recording: bool, bpm }
type: "stems_state"     { recording: bool, bars, players }
type: "__REC_START__"   recording started marker
type: "__REC_STOP__"    recording stopped marker
```

---

## foxdotWs — messages TO CrashOS

All guarded: only sent when `foxdotWs?.readyState === WebSocket.OPEN`.

### userCode
Notifies CrashOS of code being executed (for live display).
```javascript
foxdotWs.send(JSON.stringify({
    type: `${userName}Code`,
    code: blockCode
}));
```

### sceneName
Switches the active CrashOS scene.
```javascript
foxdotWs.send(JSON.stringify({
    type: "sceneName",
    sceneName: "matrix"
}));
```

---

## Adding a new message type

### 1. Client → server (new command)

In `webTroop/src/js/main.js`, send via wsServer:
```javascript
wsServer.send(JSON.stringify({
    type: "my_command",
    payload: value
}));
```

In `webTroop/server.js`, handle it in the `ws.on('message')` handler:
```javascript
case 'my_command':
    // do something, optionally write to FoxDot stdin:
    foxdot.stdin.write(msg.payload + '\n');
    break;
```

### 2. Server → client (new notification)

In `webTroop/server.js`, broadcast to all clients:
```javascript
broadcast({ type: "my_event", data: value });
```

In `webTroop/src/js/main.js`, handle in `wsServer.onmessage`:
```javascript
case 'my_event':
    // update UI
    break;
```

### 3. EventBus bridge (internal, between JS modules)

Components communicate via EventEmitter without touching WebSocket:
```javascript
// emit from anywhere
EventEmitter.emit("my_internal_event", payload);

// listen in any module
EventEmitter.on("my_internal_event", (payload) => { ... });
```

Current EventBus events:
```
send_foxdot          evaluate code string via wsServer
paste_to_editor      insert text at cursor without evaluating
rec_state            recording state changed
stems_state          stems recording state changed
```

---

## server.js — FoxDot process bridge

```
FoxDot Python process stdin  ← server.js writes code lines
FoxDot Python process stdout → server.js parses + broadcasts to WS clients
```

stdout markers parsed by server.js:
```
__REC_START__        → broadcast rec_state { recording: true }
__REC_STOP__         → broadcast rec_state { recording: false }
__STEMS_START__...   → broadcast stems_state
__STEMS_STOP__       → broadcast stems_state { recording: false }
```

---

## WebFoxDot (supersonic-proto) — separate WS

WebFoxDot does NOT use wsServer or foxdotWs. It has its own eval loop:
the browser's scsynth WASM speaks OSC directly. No WebSocket needed for audio.
See: `supersonic-proto/README.md`

---

## Paths

```
Client WS logic:    webTroop/src/js/main.js  (lines ~780-900)
Server WS handler:  webTroop/server.js
EventBus:           webTroop/src/js/eventBus.js
```

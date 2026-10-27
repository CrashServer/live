# WebTroop YouTube Video Control - Full Implementation Guide

Complete step-by-step guide to implement real-time YouTube video control from FoxDot.

## Overview

```
┌─────────────────────┐     WebSocket      ┌──────────────────────┐
│   FoxDot (Python)   │───────────────────►│   WebTroop Server    │
│   VidCtrl.stut()    │                    │   (server.js:1234)   │
└─────────────────────┘                    └──────────┬───────────┘
                                                      │
                                                      ▼
┌─────────────────────┐                    ┌──────────────────────┐
│   WebTroop Main     │◄───────────────────│   Detached Video     │
│   (opens popup)     │     WebSocket      │   (video.html)       │
└─────────────────────┘                    └──────────────────────┘
```

---

## Step 1: Install Python Dependency

```bash
# Arch Linux
sudo pacman -S python-websocket-client

# Or with pip
pip install websocket-client
```

---

## Step 2: Create Video Player HTML

Create file: `webTroop/video.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>WebTroop Video Control</title>
    <link rel="icon" href="/src/images/favicon-32x32.png" type="image/png" sizes="32x32" />
    <link rel="stylesheet" href="/src/css/video.css" />
  </head>
  <body>
    <div id="video-container">
      <!-- Header with controls -->
      <header id="video-header">
        <div class="url-input-group">
          <input type="text" id="youtube-url" placeholder="YouTube URL or Video ID" />
          <button id="load-video" class="control-btn">Load</button>
        </div>
        <div class="header-controls">
          <button id="sync-btn" class="control-btn" title="Sync with beat">Sync</button>
          <button id="always-top-btn" class="control-btn" title="Request always on top">Pin</button>
          <button id="minimize-header-btn" class="control-btn" title="Minimize header">_</button>
        </div>
      </header>

      <!-- YouTube Player -->
      <div id="player-wrapper">
        <div id="player"></div>
        <div id="player-overlay" class="hidden">
          <span id="overlay-text"></span>
        </div>
      </div>

      <!-- Status bar -->
      <footer id="video-footer">
        <div class="status-group">
          <span id="status-position">00:00.0</span>
          <span class="separator">|</span>
          <span id="status-duration">00:00</span>
        </div>
        <div class="status-group">
          <span id="status-rate">1.0x</span>
          <span class="separator">|</span>
          <span id="status-state">Idle</span>
        </div>
        <div class="status-group">
          <span id="ws-status" class="ws-disconnected">WS: --</span>
        </div>
      </footer>

      <!-- Loop region indicator -->
      <div id="loop-indicator" class="hidden">
        <span id="loop-start">0.0</span>
        <span> - </span>
        <span id="loop-end">0.0</span>
        <button id="clear-loop" class="control-btn small">Clear</button>
      </div>
    </div>

    <script src="https://www.youtube.com/iframe_api"></script>
    <script type="module" src="/src/js/video.js"></script>
  </body>
</html>
```

---

## Step 3: Create Video Player JavaScript

Create file: `webTroop/src/js/video.js`

```javascript
/**
 * WebTroop Video Control - YouTube IFrame API + WebSocket
 */

let config = null;
let ws = null;
let player = null;
let isPlayerReady = false;
let loopRegion = null;
let loopCheckInterval = null;
let stutterBaseTime = null;

// DOM elements
const urlInput = document.getElementById('youtube-url');
const loadBtn = document.getElementById('load-video');
const syncBtn = document.getElementById('sync-btn');
const alwaysTopBtn = document.getElementById('always-top-btn');
const minimizeHeaderBtn = document.getElementById('minimize-header-btn');
const statusPosition = document.getElementById('status-position');
const statusDuration = document.getElementById('status-duration');
const statusRate = document.getElementById('status-rate');
const statusState = document.getElementById('status-state');
const wsStatus = document.getElementById('ws-status');
const loopIndicator = document.getElementById('loop-indicator');
const loopStartSpan = document.getElementById('loop-start');
const loopEndSpan = document.getElementById('loop-end');
const clearLoopBtn = document.getElementById('clear-loop');
const playerOverlay = document.getElementById('player-overlay');
const overlayText = document.getElementById('overlay-text');
const videoHeader = document.getElementById('video-header');

// Initialize
async function init() {
  try {
    const configRequest = await fetch('/crash_config.json');
    config = await configRequest.json();
    connectWebSocket();
    setupEventListeners();
    startPositionUpdater();
  } catch (error) {
    console.error('Init failed:', error);
  }
}

// WebSocket connection
function connectWebSocket() {
  const wsUrl = `ws://${config.HOST_IP}:1234`;
  ws = new WebSocket(wsUrl);

  ws.onopen = () => {
    wsStatus.textContent = 'WS: OK';
    wsStatus.className = 'ws-connected';
  };

  ws.onclose = () => {
    wsStatus.textContent = 'WS: --';
    wsStatus.className = 'ws-disconnected';
    setTimeout(connectWebSocket, 2000);
  };

  ws.onerror = () => {
    wsStatus.textContent = 'WS: ERR';
    wsStatus.className = 'ws-error';
  };

  ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      handleCommand(data);
    } catch (e) {}
  };
}

// Handle incoming commands
function handleCommand(data) {
  if (!data.type || !data.type.startsWith('yt_')) return;

  switch (data.type) {
    case 'yt_load':
      loadVideo(data.url || data.videoId);
      break;
    case 'yt_seek':
      seekTo(data.time);
      break;
    case 'yt_stutter':
      stutter(data.amount || 0.5);
      break;
    case 'yt_rate':
      setPlaybackRate(data.rate || 1.0);
      break;
    case 'yt_play':
      playVideo();
      break;
    case 'yt_pause':
      pauseVideo();
      break;
    case 'yt_loop':
      setLoopRegion(data.start, data.end);
      break;
    case 'yt_clear_loop':
      clearLoopRegion();
      break;
    case 'yt_jump':
      jumpTo(data.time);
      break;
    case 'yt_scrub':
      scrub(data.offset);
      break;
  }
}

// Video control functions
function loadVideo(urlOrId) {
  if (!urlOrId) return;
  const videoId = extractVideoId(urlOrId);
  if (!videoId) return;
  if (player && isPlayerReady) {
    player.loadVideoById(videoId);
  }
}

function extractVideoId(urlOrId) {
  if (/^[a-zA-Z0-9_-]{11}$/.test(urlOrId)) return urlOrId;
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/,
    /youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})/
  ];
  for (const pattern of patterns) {
    const match = urlOrId.match(pattern);
    if (match) return match[1];
  }
  return null;
}

function seekTo(time) {
  if (!player || !isPlayerReady) return;
  const seekTime = Math.max(0, parseFloat(time) || 0);
  player.seekTo(seekTime, true);
  stutterBaseTime = seekTime;
}

function stutter(amount) {
  if (!player || !isPlayerReady) return;
  const currentTime = player.getCurrentTime();
  const newTime = Math.max(0, currentTime - (parseFloat(amount) || 0.5));
  player.seekTo(newTime, true);
}

function jumpTo(time) {
  if (!player || !isPlayerReady) return;
  const jumpTime = Math.max(0, parseFloat(time) || 0);
  player.seekTo(jumpTime, true);
  stutterBaseTime = jumpTime;
}

function scrub(offset) {
  if (!player || !isPlayerReady || stutterBaseTime === null) return;
  const newTime = Math.max(0, stutterBaseTime + (parseFloat(offset) || 0));
  player.seekTo(newTime, true);
}

function setPlaybackRate(rate) {
  if (!player || !isPlayerReady) return;
  const validRates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2];
  const clampedRate = Math.max(0.25, Math.min(2, parseFloat(rate) || 1));
  const closestRate = validRates.reduce((prev, curr) =>
    Math.abs(curr - clampedRate) < Math.abs(prev - clampedRate) ? curr : prev
  );
  player.setPlaybackRate(closestRate);
  statusRate.textContent = `${closestRate}x`;
}

function playVideo() {
  if (player && isPlayerReady) player.playVideo();
}

function pauseVideo() {
  if (player && isPlayerReady) player.pauseVideo();
}

function setLoopRegion(start, end) {
  if (!player || !isPlayerReady) return;
  const startTime = parseFloat(start) || 0;
  const endTime = parseFloat(end) || player.getDuration();
  if (startTime >= endTime) return;

  loopRegion = { start: startTime, end: endTime };
  loopIndicator.classList.remove('hidden');
  loopStartSpan.textContent = formatTime(startTime);
  loopEndSpan.textContent = formatTime(endTime);

  if (!loopCheckInterval) {
    loopCheckInterval = setInterval(checkLoopRegion, 50);
  }
  player.seekTo(startTime, true);
  stutterBaseTime = startTime;
}

function clearLoopRegion() {
  loopRegion = null;
  loopIndicator.classList.add('hidden');
  if (loopCheckInterval) {
    clearInterval(loopCheckInterval);
    loopCheckInterval = null;
  }
}

function checkLoopRegion() {
  if (!loopRegion || !player || !isPlayerReady) return;
  if (player.getCurrentTime() >= loopRegion.end) {
    player.seekTo(loopRegion.start, true);
  }
}

// YouTube IFrame API
window.onYouTubeIframeAPIReady = function() {
  player = new YT.Player('player', {
    height: '100%',
    width: '100%',
    playerVars: {
      autoplay: 0, controls: 1, disablekb: 0, enablejsapi: 1,
      modestbranding: 1, rel: 0, origin: window.location.origin
    },
    events: {
      onReady: onPlayerReady,
      onStateChange: onPlayerStateChange,
      onError: onPlayerError
    }
  });
};

function onPlayerReady() {
  isPlayerReady = true;
  statusState.textContent = 'Ready';
  const urlValue = urlInput.value.trim();
  if (urlValue) loadVideo(urlValue);
}

function onPlayerStateChange(event) {
  const states = { [-1]: 'Unstarted', 0: 'Ended', 1: 'Playing', 2: 'Paused', 3: 'Buffering', 5: 'Cued' };
  statusState.textContent = states[event.data] || 'Unknown';
  if (event.data === 1 && player) {
    statusDuration.textContent = formatTime(player.getDuration());
  }
}

function onPlayerError(event) {
  statusState.textContent = 'Error';
}

// Helpers
function formatTime(seconds) {
  if (!seconds || isNaN(seconds)) return '00:00.0';
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  const ms = Math.floor((seconds % 1) * 10);
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}.${ms}`;
}

function showOverlay(text, duration = 1000) {
  // Disabled
  return;
}

function startPositionUpdater() {
  setInterval(() => {
    if (player && isPlayerReady && player.getCurrentTime) {
      try {
        statusPosition.textContent = formatTime(player.getCurrentTime());
      } catch (e) {}
    }
  }, 100);
}

function setupEventListeners() {
  loadBtn.addEventListener('click', () => {
    const url = urlInput.value.trim();
    if (url) loadVideo(url);
  });

  urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      const url = urlInput.value.trim();
      if (url) loadVideo(url);
    }
  });

  syncBtn.addEventListener('click', () => {
    if (player && isPlayerReady) {
      stutterBaseTime = player.getCurrentTime();
    }
  });

  let headerMinimized = false;
  minimizeHeaderBtn.addEventListener('click', () => {
    headerMinimized = !headerMinimized;
    videoHeader.classList.toggle('minimized', headerMinimized);
    minimizeHeaderBtn.textContent = headerMinimized ? '+' : '_';
  });

  clearLoopBtn.addEventListener('click', clearLoopRegion);

  document.addEventListener('keydown', (e) => {
    if (e.target === urlInput) return;
    switch (e.key) {
      case ' ':
        e.preventDefault();
        if (player && isPlayerReady) {
          player.getPlayerState() === 1 ? pauseVideo() : playVideo();
        }
        break;
      case 'ArrowLeft':
        e.preventDefault();
        if (player && isPlayerReady) player.seekTo(player.getCurrentTime() - 5, true);
        break;
      case 'ArrowRight':
        e.preventDefault();
        if (player && isPlayerReady) player.seekTo(player.getCurrentTime() + 5, true);
        break;
      case 's':
        if (player && isPlayerReady) stutterBaseTime = player.getCurrentTime();
        break;
      case 'Escape':
        clearLoopRegion();
        break;
    }
  });
}

init();
```

---

## Step 4: Create Video Player CSS

Create file: `webTroop/src/css/video.css`

```css
@import 'interfaceThemes.css';

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  width: 100%; height: 100%; overflow: hidden;
  background: var(--bg-col-1, #1a1a1a);
  color: var(--text-col-1, #e0e0e0);
  font-family: 'Fira Code', monospace;
  font-size: 12px;
}

#video-container {
  display: flex; flex-direction: column;
  width: 100%; height: 100%;
}

#video-header {
  display: flex; flex-wrap: wrap;
  justify-content: space-between; align-items: center;
  gap: 0.5rem; padding: 0.5rem;
  background: var(--bg-col-2, #252525);
  border-bottom: 1px solid var(--border-col-1, #333);
}

#video-header.minimized {
  padding: 0.2rem 0.5rem;
}

#video-header.minimized .url-input-group { display: none; }

.url-input-group {
  display: flex; flex: 1; min-width: 200px; gap: 0.5rem;
}

#youtube-url {
  flex: 1; padding: 0.4rem 0.6rem;
  background: var(--bg-col-1); border: 1px solid var(--border-col-2);
  border-radius: 3px; color: var(--text-col-2);
  font-family: inherit; outline: none;
}

.control-btn {
  padding: 0.4rem 0.8rem;
  background: var(--bg-col-2); border: 1px solid var(--border-col-2);
  border-radius: 3px; color: var(--text-col-2);
  cursor: pointer;
}

.control-btn:hover { background: var(--border-col-2); }

#player-wrapper { flex: 1; position: relative; background: #000; }
#player { width: 100%; height: 100%; }
#player iframe { width: 100%; height: 100%; border: none; }

#video-footer {
  display: flex; justify-content: space-between;
  padding: 0.4rem 0.8rem;
  background: var(--bg-col-2);
  border-top: 1px solid var(--border-col-1);
  font-size: 11px;
}

.status-group { display: flex; align-items: center; gap: 0.5rem; }
.ws-connected { color: var(--col-green, #4caf50); }
.ws-disconnected { color: var(--col-red, #f44336); }

#loop-indicator {
  position: absolute; bottom: 40px; left: 50%;
  transform: translateX(-50%);
  padding: 0.4rem 0.8rem;
  background: rgba(0,0,0,0.8);
  border: 1px solid var(--col-blue, #2196f3);
  border-radius: 4px; font-size: 11px;
}

#loop-indicator.hidden { display: none; }
```

---

## Step 5: Modify Server to Relay Messages

Edit: `webTroop/server.js`

Add inside the `ws.on('message', ...)` handler, after the `save_file` block:

```javascript
} else if (data.type && data.type.startsWith('yt_')) {
  // Relay YouTube control messages to all clients
  console.log('YouTube command:', data.type, data);
  broadcastYouTubeCommand(data);
}
```

Add this function after `broadcastLog`:

```javascript
function broadcastYouTubeCommand(data) {
  wss.clients.forEach(client => {
    if (client.readyState === 1) {
      client.send(JSON.stringify(data));
    }
  });
}
```

---

## Step 6: Add Pop-out Button to CrashPanel

Edit: `webTroop/index.html`

Add after the Record section:

```html
<section class="video-control">
    <fieldset class="info-row">
        <legend>Video</legend>
        <button id="popoutVideo" class="configButton">Pop Video</button>
    </fieldset>
</section>
```

---

## Step 7: Add Button Handler to CrashPanel JS

Edit: `webTroop/src/js/crashpanel.js`

Add near the top with other element declarations:

```javascript
const popoutVideoButton = document.getElementById('popoutVideo');
```

Add after the record button handler:

```javascript
// Video popout button
let videoWindow = null;
popoutVideoButton.addEventListener('click', () => {
  if (videoWindow && !videoWindow.closed) {
    videoWindow.focus();
    return;
  }

  const width = 640;
  const height = 400;
  const left = window.screenX + window.outerWidth - width - 50;
  const top = window.screenY + 50;

  videoWindow = window.open(
    '/video.html',
    'WebTroop Video',
    `width=${width},height=${height},left=${left},top=${top},resizable=yes`
  );

  if (videoWindow) {
    popoutVideoButton.textContent = 'Video Open';
    popoutVideoButton.classList.add('video-active');

    const checkClosed = setInterval(() => {
      if (videoWindow.closed) {
        clearInterval(checkClosed);
        popoutVideoButton.textContent = 'Pop Video';
        popoutVideoButton.classList.remove('video-active');
        videoWindow = null;
      }
    }, 500);
  }
});
```

Add after `wsServer.onopen`:

```javascript
// Listen for yt_open_window command from FoxDot
wsServer.onmessage = function(event) {
    try {
        const data = JSON.parse(event.data);
        if (data.type === 'yt_open_window') {
            if (!videoWindow || videoWindow.closed) {
                popoutVideoButton.click();
            }
        }
    } catch (e) {}
};
```

---

## Step 8: Add Button Styling

Edit: `webTroop/src/css/crashpanel.css`

Add at the end:

```css
.video-active {
  background-color: var(--col-blue) !important;
  color: var(--bg-col-1) !important;
  font-weight: bold;
}

#popoutVideo { width: 100%; }
```

---

## Step 9: Create FoxDot VideoControl Module

Create file: `FoxDot/FoxDot/lib/VideoControl.py`

```python
"""
WebTroop YouTube Video Control
Usage: VidCtrl.load(), VidCtrl.stutter(), VidCtrl.pos([10,20,30])
"""

from __future__ import absolute_import, division, print_function
import json
import os
import threading
import time

try:
    import websocket
    HAS_WEBSOCKET = True
except ImportError:
    HAS_WEBSOCKET = False
    print("Warning: websocket-client not installed")


def _load_config():
    """Load HOST_IP from crash_config.json"""
    paths = [
        os.path.expanduser('~/live/webTroop/crash_config.json'),
        './crash_config.json',
    ]
    for path in paths:
        try:
            with open(path, 'r') as f:
                return json.load(f).get('HOST_IP', 'localhost')
        except:
            continue
    return 'localhost'


class YouTubeController:
    def __init__(self, host=None, port=1234):
        self.host = host or _load_config()
        self.port = port
        self.ws = None
        self.connected = False
        self._connect_thread = None

    def connect(self, host=None, port=None):
        if not HAS_WEBSOCKET:
            return self
        if host: self.host = host
        if port: self.port = port

        def _connect():
            try:
                self.ws = websocket.create_connection(
                    f"ws://{self.host}:{self.port}", timeout=5
                )
                self.connected = True
                print(f"VidCtrl connected to {self.host}:{self.port}")
            except Exception as e:
                self.connected = False
                print(f"VidCtrl connection failed: {e}")

        self._connect_thread = threading.Thread(target=_connect, daemon=True)
        self._connect_thread.start()
        return self

    def disconnect(self):
        if self.ws:
            try: self.ws.close()
            except: pass
        self.connected = False
        self.ws = None
        return self

    def _send(self, msg_type, **kwargs):
        if not HAS_WEBSOCKET:
            return self

        if not self.connected or self.ws is None:
            self.connect()
            for _ in range(10):
                if self.connected: break
                time.sleep(0.05)

        if not self.connected:
            print(f"VidCtrl: Not connected")
            return self

        try:
            self.ws.send(json.dumps({"type": msg_type, **kwargs}))
        except Exception as e:
            print(f"VidCtrl error: {e}")
            self.connected = False
            self.connect()
        return self

    # Basic commands
    def load(self, url):
        self._send("yt_open_window")
        time.sleep(0.1)
        return self._send("yt_load", url=str(url))

    def seek(self, t): return self._send("yt_seek", time=float(t))
    def stutter(self, amt=0.5): return self._send("yt_stutter", amount=float(amt))
    def jump(self, t): return self._send("yt_jump", time=float(t))
    def scrub(self, offset): return self._send("yt_scrub", offset=float(offset))
    def rate(self, r=1.0): return self._send("yt_rate", rate=float(r))
    def play(self): return self._send("yt_play")
    def pause(self): return self._send("yt_pause")
    def loop(self, start, end): return self._send("yt_loop", start=float(start), end=float(end))
    def clear_loop(self): return self._send("yt_clear_loop")

    # Pattern methods
    def pos(self, positions, dur=1):
        """Cycle positions: VidCtrl.pos([10, 40, 120])"""
        self._pos_running = False
        self._pos_pattern = list(positions) if isinstance(positions, (list,tuple)) else [positions]
        self._pos_dur = dur
        self._pos_index = 0
        self._pos_running = True
        self._run_pos()
        return self

    def _run_pos(self):
        if not self._pos_running: return
        self.seek(self._pos_pattern[self._pos_index % len(self._pos_pattern)])
        self._pos_index += 1
        try:
            from . import Clock
            Clock.future(self._pos_dur, self._run_pos)
        except: pass

    def stut(self, amounts, dur=1):
        """Cycle stutters: VidCtrl.stut([0, 0.1, 0, 0.2])"""
        self._stut_running = False
        self._stut_pattern = list(amounts) if isinstance(amounts, (list,tuple)) else [amounts]
        self._stut_dur = dur
        self._stut_index = 0
        self._stut_running = True
        self._run_stut()
        return self

    def _run_stut(self):
        if not self._stut_running: return
        amt = self._stut_pattern[self._stut_index % len(self._stut_pattern)]
        if amt > 0: self.stutter(amt)
        self._stut_index += 1
        try:
            from . import Clock
            Clock.future(self._stut_dur, self._run_stut)
        except: pass

    def rates(self, rates, dur=4):
        """Cycle rates: VidCtrl.rates([1, 0.5, 2])"""
        self._rate_running = False
        self._rate_pattern = list(rates) if isinstance(rates, (list,tuple)) else [rates]
        self._rate_dur = dur
        self._rate_index = 0
        self._rate_running = True
        self._run_rates()
        return self

    def _run_rates(self):
        if not self._rate_running: return
        self.rate(self._rate_pattern[self._rate_index % len(self._rate_pattern)])
        self._rate_index += 1
        try:
            from . import Clock
            Clock.future(self._rate_dur, self._run_rates)
        except: pass

    def stop_patterns(self):
        self._pos_running = False
        self._stut_running = False
        self._rate_running = False
        return self

    def stop(self):
        self.stop_patterns()
        return self.pause()


VidCtrl = YouTubeController()
__all__ = ['VidCtrl', 'YouTubeController']
```

---

## Step 10: Import in FoxDot

Edit: `FoxDot/FoxDot/lib/__init__.py`

Add after other imports:

```python
from .VideoControl import VidCtrl, YouTubeController
```

---

## Usage

```python
# Load and play
VidCtrl.load("https://youtube.com/watch?v=...")

# Basic control
VidCtrl.seek(30)
VidCtrl.stutter(0.2)
VidCtrl.rate(0.5)
VidCtrl.play()
VidCtrl.pause()
VidCtrl.loop(10, 20)

# Pattern-based (FoxDot style)
VidCtrl.pos([10, 40, 120])           # cycle positions every beat
VidCtrl.pos([0, 30, 60], dur=4)      # every 4 beats
VidCtrl.stut([0, 0.1, 0, 0.2])       # stutter pattern
VidCtrl.stut([0.1, 0.2], dur=0.5)    # fast stutter
VidCtrl.rates([1, 0.5, 1, 2], dur=4) # rate changes

# Stop patterns
VidCtrl.stop_patterns()
VidCtrl.stop()
```

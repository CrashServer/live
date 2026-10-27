# WebTroop YouTube Video Control

Real-time YouTube video control from FoxDot code via WebSocket.

## Architecture

```
┌─────────────────────┐                    ┌──────────────────────┐
│   FoxDot (Python)   │                    │   WebTroop Server    │
│                     │     WebSocket      │   (server.js:1234)   │
│   yt.stutter(0.5)  ─┼───────────────────►│                      │
│                     │                    │   Relays yt_* msgs   │
└─────────────────────┘                    └──────────┬───────────┘
                                                      │
┌─────────────────────┐                               │ WebSocket
│   WebTroop Main     │                               │
│   (Code Editor)     │                               │
│                     │                               │
│  [Pop Video] button │                               │
└─────────────────────┘                               │
         │                                            │
         │ window.open()                              │
         ▼                                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Detached Video Window                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [YouTube URL input] [Load]           [Sync] [Pin] [_]  │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                         │   │
│  │              YouTube IFrame Player                      │   │
│  │                                                         │   │
│  │         Receives yt_* commands via WebSocket            │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│  Position: 00:42.3  |  Rate: 1.0x  |  Status: Playing          │
└─────────────────────────────────────────────────────────────────┘
```

## Files Created/Modified

### New Files

| File | Description |
|------|-------------|
| `webTroop/video.html` | Detachable video player HTML page |
| `webTroop/src/js/video.js` | YouTube IFrame API + WebSocket control |
| `webTroop/src/css/video.css` | Video player styling |
| `FoxDot/FoxDot/lib/VideoControl.py` | Python module for `yt` commands |

### Modified Files

| File | Changes |
|------|---------|
| `webTroop/server.js` | Added `yt_*` message relay via `broadcastYouTubeCommand()` |
| `webTroop/index.html` | Added "Pop Video" button section |
| `webTroop/src/js/crashpanel.js` | Added pop-out window handler |
| `webTroop/src/css/crashpanel.css` | Added `.video-active` button style |
| `FoxDot/FoxDot/lib/__init__.py` | Added `yt` import |

## Installation

### Prerequisites

Install the websocket-client Python package:

```bash
pip install websocket-client
```

### Configuration

The video controller connects to WebTroop server at the configured `HOST_IP` in `crash_config.json`.

To use from FoxDot, the `yt` object auto-connects on first use.

## Usage

### Opening the Video Window

1. In WebTroop, click **"Pop Video"** in the CrashPanel
2. A detachable window opens with the YouTube player
3. Drag to second monitor if desired

### Loading a Video

**From the video window:**
- Paste YouTube URL in the input field
- Click "Load" or press Enter

**From FoxDot code:**
```python
Video.load("https://youtube.com/watch?v=dQw4w9WgXcQ")
Video.load("dQw4w9WgXcQ")  # Just the video ID
# Or use the alias:
YT.load("dQw4w9WgXcQ")
```

> **Note:** Use `Video` or `YT`, not `yt` - FoxDot reserves two-letter names for players.

### Control Commands

| Command | Description | Example |
|---------|-------------|---------|
| `Video.load(url)` | Load a video | `Video.load("dQw4w9WgXcQ")` |
| `Video.seek(time)` | Seek to position (seconds) | `Video.seek(30)` |
| `Video.stutter(amount)` | Jump back N seconds | `Video.stutter(0.2)` |
| `Video.rate(speed)` | Set playback rate (0.25-2.0) | `Video.rate(0.5)` |
| `Video.play()` | Play video | `Video.play()` |
| `Video.pause()` | Pause video | `Video.pause()` |
| `Video.loop(start, end)` | Set loop region | `Video.loop(10, 20)` |
| `Video.clear_loop()` | Clear loop | `Video.clear_loop()` |
| `Video.jump(time)` | Jump and set as scrub base | `Video.jump(15)` |
| `Video.scrub(offset)` | Scrub from base position | `Video.scrub(0.5)` |

### Convenience Aliases

| Alias | Equivalent |
|-------|------------|
| `Video(30)` | `Video.seek(30)` |
| `Video.go(30)` | `Video.seek(30)` |
| `Video.stop()` | `Video.pause()` |
| `Video.speed(0.5)` | `Video.rate(0.5)` |
| `Video.slow()` | `Video.rate(0.5)` |
| `Video.fast()` | `Video.rate(2)` |
| `Video.normal()` | `Video.rate(1)` |

## Live Performance Examples

### Basic Stutter Effect

```python
# Stutter every beat
@nextBar
def stutter_loop():
    Video.stutter(0.2)
    Clock.future(1, stutter_loop)
```

### Pattern-Based Stutter

```python
# Different stutter amounts per beat
# (Requires scheduling in player)
def video_stutter():
    amounts = [0, 0.1, 0, 0.3, 0, 0.1, 0.2, 0]
    i = int(Clock.beat) % len(amounts)
    if amounts[i] > 0:
        Video.stutter(amounts[i])
```

### Speed Changes

```python
# Slow down for breakdown
Video.rate(0.5)

# Back to normal
Video.rate(1)

# Speed up for build
Video.rate(1.5)
```

### Loop Section

```python
# Loop a 4-second section starting at 10 seconds
Video.loop(10, 14)

# Clear when done
Video.clear_loop()
```

### Scrub with TimeVar

```python
# Set base position
Video.jump(20)

# Scrub back and forth (requires custom scheduling)
# The scrub offset oscillates between 0 and 2 seconds
@nextBar
def scrub_lfo():
    offset = (Clock.beat % 4) * 0.5  # 0, 0.5, 1, 1.5, 0, ...
    Video.scrub(offset)
    Clock.future(0.25, scrub_lfo)
```

## WebSocket Message Format

Messages sent from FoxDot to WebTroop server:

```json
{"type": "yt_load", "url": "https://youtube.com/watch?v=..."}
{"type": "yt_seek", "time": 30.5}
{"type": "yt_stutter", "amount": 0.2}
{"type": "yt_rate", "rate": 0.5}
{"type": "yt_play"}
{"type": "yt_pause"}
{"type": "yt_loop", "start": 10, "end": 20}
{"type": "yt_clear_loop"}
{"type": "yt_jump", "time": 15}
{"type": "yt_scrub", "offset": 0.5}
```

## Keyboard Shortcuts (Video Window)

| Key | Action |
|-----|--------|
| Space | Toggle play/pause |
| Left Arrow | Seek back 5 seconds |
| Right Arrow | Seek forward 5 seconds |
| S | Set current position as scrub base |
| L | Toggle loop indicator visibility |
| Escape | Clear loop region |

## Troubleshooting

### "websocket-client not installed"

```bash
pip install websocket-client
```

### Video window not receiving commands

1. Check WebTroop server is running
2. Check `crash_config.json` has correct `HOST_IP`
3. Check browser console for WebSocket errors

### YouTube player errors

- **"Invalid video ID"**: Check URL format
- **"Embedding disabled"**: Some videos block embedding
- **"Video not found"**: Video may be private or deleted

## Limitations

- YouTube playback rate limited to: 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2
- Cannot access frame-accurate position (YouTube API limitation)
- Some videos disable embedding
- Picture-in-Picture not supported for iframes

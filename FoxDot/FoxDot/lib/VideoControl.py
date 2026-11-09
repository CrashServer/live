"""
VideoControl — YouTube video controller for FoxDot live coding.
Sends commands over WebSocket to the webTroop video popup.
Lazy connection: zero overhead until first command is used.
"""

import json
import os
import re
import asyncio
import websocket  # websocket-client (sync)

_YT_ID = re.compile(r'^[a-zA-Z0-9_-]{11}$')
_YT_URL = re.compile(r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/shorts/)([a-zA-Z0-9_-]{11})')


def _video_id(url_or_id):
    """Accept a bare 11-char video ID or any common YouTube URL form."""
    s = str(url_or_id).strip()
    if _YT_ID.match(s):
        return s
    m = _YT_URL.search(s)
    return m.group(1) if m else s

# Lazy import — Clock is only available after FoxDot init
_clock = None

def _get_clock():
    global _clock
    if _clock is None:
        from FoxDot.lib import Clock as _c
        _clock = _c
    return _clock


class YouTubeController:
    def __init__(self):
        self._ws = None
        self._host = None
        self._port = 1234
        self._patterns_running = False
        self._pattern_id = 0
        self._load_config()

    def _load_config(self):
        """Load host IP from crash_config.json"""
        try:
            config_path = os.path.abspath(
                os.path.join(os.getcwd(), '../webTroop/crash_config.json')
            )
            with open(config_path, 'r') as f:
                config = json.load(f)
            self._host = config.get('HOST_IP', '127.0.0.1')
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"VideoControl: config load failed ({e}), using localhost")
            self._host = '127.0.0.1'

    def _connect(self):
        """Lazy WebSocket connection — only connects on first command."""
        if self._ws is not None:
            try:
                self._ws.ping()
                return
            except Exception:
                self._ws = None
        try:
            self._ws = websocket.create_connection(
                f"ws://{self._host}:{self._port}",
                timeout=3
            )
        except (ConnectionRefusedError, OSError, websocket.WebSocketException) as e:
            print(f"VideoControl: connection failed ({e})")
            self._ws = None

    def _send(self, msg_type, **kwargs):
        """Send a JSON message to the server."""
        self._connect()
        if self._ws is None:
            return
        payload = {"type": msg_type, **kwargs}
        try:
            self._ws.send(json.dumps(payload))
        except (BrokenPipeError, OSError, websocket.WebSocketException) as e:
            print(f"VideoControl: send failed ({e})")
            self._ws = None

    # ─── Transport ────────────────────────────────────────────────

    def load(self, video_id):
        """Open video popup window and load a YouTube video by ID or URL."""
        video_id = _video_id(video_id)
        self._send('yt_open_window', videoId=video_id)
        self._send('yt_load', videoId=video_id)

    def play(self):
        """Resume playback."""
        self._send('yt_play')

    def pause(self):
        """Pause playback."""
        self._send('yt_pause')

    def seek(self, seconds):
        """Seek to position in seconds."""
        self._send('yt_seek', position=float(seconds))

    def stop(self):
        """Stop all beat-synced patterns and pause the video."""
        self.stop_patterns()
        self.pause()

    # ─── Effects ──────────────────────────────────────────────────

    def stutter(self, duration=0.25):
        """Quick seek-back stutter effect."""
        self._send('yt_stutter', duration=float(duration))

    def rate(self, speed=1.0):
        """Set playback rate."""
        self._send('yt_rate', rate=float(speed))

    def loop(self, start, end):
        """Set a loop region (in seconds)."""
        self._send('yt_loop', start=float(start), end=float(end))

    def unloop(self):
        """Remove loop region."""
        self._send('yt_unloop')

    clear_loop = unloop

    def jump(self, seconds):
        """Seek and set the position as the base for scrub()."""
        self._send('yt_jump', time=float(seconds))

    def scrub(self, offset):
        """Seek relative to the last jump()/seek() base, e.g. scrub(linvar([0, 2], 8))."""
        self._send('yt_scrub', offset=float(offset))

    def beat_loop(self, bars=1, start=0):
        """Loop N bars (4/4 at the current Clock.bpm) starting at `start` seconds."""
        length = bars * 4 * 60.0 / float(_get_clock().get_bpm())
        self.loop(start, float(start) + length)

    bloop = beat_loop

    def unfreeze(self):
        """Stop freeze/grain (and any beat-synced pattern) and resume playback."""
        self.stop_patterns()
        self.play()

    def stop_patterns(self):
        """Stop beat-synced patterns without pausing the video."""
        self._patterns_running = False
        self._pattern_id += 1

    # ─── Shortcuts ────────────────────────────────────────────────

    def go(self, seconds):
        """Alias of seek(). e.g. VidCtrl.go(30)"""
        self.seek(seconds)

    def speed(self, rate):
        """Alias of rate(). e.g. VidCtrl.speed(0.75)"""
        self.rate(rate)

    def slow(self):
        """Half-speed playback (rate 0.5)."""
        self.rate(0.5)

    def fast(self):
        """Double-speed playback (rate 2)."""
        self.rate(2)

    def normal(self):
        """Back to normal speed (rate 1)."""
        self.rate(1)

    def __call__(self, seconds):
        """VidCtrl(30) is VidCtrl.seek(30)."""
        self.seek(seconds)

    # ─── Beat-synced patterns ─────────────────────────────────────

    def pos(self, positions, dur=1):
        """Cycle through seek positions on each beat."""
        self._start_pattern('_pos_step', positions, dur)

    def stut(self, durations, dur=1):
        """Cycle through stutter durations on each beat."""
        self._start_pattern('_stut_step', durations, dur)

    def rates(self, speeds, dur=1):
        """Cycle through playback rates on each beat."""
        self._start_pattern('_rates_step', speeds, dur)

    def grain(self, positions=None, size=0.25, dur=0.5):
        """Granular-style: seek to positions with short playback windows."""
        if positions is None:
            positions = [0]
        self._start_pattern('_grain_step', positions, dur, extra={'size': size})

    def freeze(self, position=None, dur=0.5):
        """Repeatedly seek to the same position, creating a freeze frame."""
        if position is None:
            # Will use current position — send special marker
            positions = ['current']
        else:
            positions = [position]
        self._start_pattern('_freeze_step', positions, dur)

    def _start_pattern(self, method_name, values, dur, extra=None):
        """Start a beat-synced pattern using Clock.future."""
        self._patterns_running = True
        self._pattern_id += 1
        pid = self._pattern_id
        clock = _get_clock()
        step_fn = getattr(self, method_name)
        step_fn(values, 0, dur, pid, extra)

    def _pos_step(self, values, idx, dur, pid, _extra):
        if not self._patterns_running or pid != self._pattern_id:
            return
        pos = values[idx % len(values)]
        self.seek(pos)
        clock = _get_clock()
        clock.future(dur, self._pos_step, args=(values, idx + 1, dur, pid, _extra))

    def _stut_step(self, values, idx, dur, pid, _extra):
        if not self._patterns_running or pid != self._pattern_id:
            return
        d = values[idx % len(values)]
        self.stutter(d)
        clock = _get_clock()
        clock.future(dur, self._stut_step, args=(values, idx + 1, dur, pid, _extra))

    def _rates_step(self, values, idx, dur, pid, _extra):
        if not self._patterns_running or pid != self._pattern_id:
            return
        r = values[idx % len(values)]
        self.rate(r)
        clock = _get_clock()
        clock.future(dur, self._rates_step, args=(values, idx + 1, dur, pid, _extra))

    def _grain_step(self, values, idx, dur, pid, extra):
        if not self._patterns_running or pid != self._pattern_id:
            return
        pos = values[idx % len(values)]
        size = extra.get('size', 0.25) if extra else 0.25
        self.seek(pos)
        self.play()
        clock = _get_clock()
        clock.future(size, self.pause)
        clock.future(dur, self._grain_step, args=(values, idx + 1, dur, pid, extra))

    def _freeze_step(self, values, idx, dur, pid, _extra):
        if not self._patterns_running or pid != self._pattern_id:
            return
        pos = values[idx % len(values)]
        if pos != 'current':
            self.seek(pos)
        clock = _get_clock()
        clock.future(dur, self._freeze_step, args=(values, idx + 1, dur, pid, _extra))


# Singleton instance
VidCtrl = YouTubeController()

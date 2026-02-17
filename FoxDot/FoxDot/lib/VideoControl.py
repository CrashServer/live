"""
WebTroop YouTube Video Control

Control a detachable YouTube video player via WebSocket.

Usage in FoxDot:
    VidCtrl.load("https://youtube.com/watch?v=...")  # Load a video
    VidCtrl.seek(30)                                  # Seek to 30 seconds
    VidCtrl.stutter(0.5)                              # Jump back 0.5 seconds
    VidCtrl.rate(0.5)                                 # Half speed playback
    VidCtrl.play() / .pause()                         # Transport
    VidCtrl.loop(10, 20)                              # Loop region
    VidCtrl.pos([10, 40, 120])                        # Cycle positions on beat
    VidCtrl.stut([0, 0.1, 0, 0.2])                    # Cycle stutters on beat
    VidCtrl.grain(30, spread=2)                       # Granular video
    VidCtrl.freeze(30)                                # Freeze frame
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
    print("Warning: websocket-client not installed. YouTube control disabled.")
    print("Install with: pip install websocket-client")


def _load_config():
    """Try to load crash_config.json to get HOST_IP."""
    config_paths = [
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'webTroop', 'crash_config.json'),
        os.path.expanduser('~/live/webTroop/crash_config.json'),
        './crash_config.json',
    ]
    for path in config_paths:
        try:
            with open(path, 'r') as f:
                config = json.load(f)
                return config.get('HOST_IP', 'localhost')
        except:
            continue
    return 'localhost'


class YouTubeController:
    """
    Controls a YouTube video player via WebSocket connection to WebTroop server.
    """

    def __init__(self, host=None, port=1234):
        self.host = host or _load_config()
        self.port = port
        self.ws = None
        self.connected = False
        self._connect_thread = None
        self._reconnect_delay = 2
        self._video_window_opened = False

    def _get_ws_url(self):
        return f"ws://{self.host}:{self.port}"

    def connect(self, host=None, port=None):
        """Connect to WebTroop server WebSocket."""
        if not HAS_WEBSOCKET:
            print("Cannot connect: websocket-client not installed")
            return self

        if host:
            self.host = host
        if port:
            self.port = port

        def _connect():
            try:
                self.ws = websocket.create_connection(
                    self._get_ws_url(),
                    timeout=5
                )
                self.connected = True
                print(f"YouTube control connected to {self._get_ws_url()}")
            except Exception as e:
                self.connected = False
                print(f"YouTube control connection failed: {e}")

        self._connect_thread = threading.Thread(target=_connect, daemon=True)
        self._connect_thread.start()
        return self

    def disconnect(self):
        """Disconnect from WebTroop server."""
        if self.ws:
            try:
                self.ws.close()
            except:
                pass
        self.connected = False
        self.ws = None
        return self

    def _send(self, msg_type, **kwargs):
        """Send a message to the WebTroop server."""
        if not HAS_WEBSOCKET:
            print("VidCtrl: websocket-client not installed")
            return self

        # Auto-connect if not connected
        if not self.connected or self.ws is None:
            self.connect()
            # Wait for connection
            for _ in range(10):
                if self.connected:
                    break
                time.sleep(0.05)

        if not self.connected or self.ws is None:
            print(f"VidCtrl: Not connected to {self.host}:{self.port}")
            return self

        try:
            message = {"type": msg_type, **kwargs}
            self.ws.send(json.dumps(message))
        except Exception as e:
            print(f"VidCtrl send error: {e}")
            self.connected = False
            self.connect()

        return self

    # =========================================================================
    # VIDEO CONTROL METHODS
    # =========================================================================

    def load(self, url_or_id):
        """
        Load a YouTube video by URL or video ID.
        Opens the video window if not already open.

        Args:
            url_or_id: YouTube URL or 11-character video ID

        Example:
            VidCtrl.load("https://youtube.com/watch?v=...")
            VidCtrl.load("dQw4w9WgXcQ")  # Video ID
        """
        # Send URL with open_window command - video.js will load it when ready
        return self._send("yt_open_window", url=str(url_or_id))

    def seek(self, time_seconds):
        """
        Seek to a specific position in the video.

        Args:
            time_seconds: Position in seconds

        Example:
            yt.seek(30)      # Jump to 30 seconds
            yt.seek(2.5)     # Jump to 2.5 seconds
        """
        return self._send("yt_seek", time=float(time_seconds))

    def stutter(self, amount=0.5):
        """
        Jump back by a specified amount (stutter effect).

        Args:
            amount: Seconds to jump back (default 0.5)

        Example:
            yt.stutter(0.2)  # Jump back 0.2 seconds
            yt.stutter(1)    # Jump back 1 second

        Pattern usage:
            p1 >> yt.stutter([0, 0.1, 0, 0.2])
        """
        return self._send("yt_stutter", amount=float(amount))

    def jump(self, time_seconds):
        """
        Jump to a specific time and set it as the stutter base.

        Args:
            time_seconds: Position in seconds

        Example:
            yt.jump(10)  # Jump to 10s and set as base for scrub
        """
        return self._send("yt_jump", time=float(time_seconds))

    def scrub(self, offset):
        """
        Scrub relative to the stutter base position.
        Useful for LFO-style effects.

        Args:
            offset: Offset from base position in seconds

        Example:
            yt.scrub(linvar([0, 2], 8))  # Oscillate over 2 seconds
        """
        return self._send("yt_scrub", offset=float(offset))

    def rate(self, playback_rate=1.0):
        """
        Set playback rate.

        Args:
            playback_rate: Speed multiplier (0.25 to 2.0)
                          YouTube supports: 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2

        Example:
            yt.rate(0.5)   # Half speed
            yt.rate(2)     # Double speed
            yt.rate(0.25)  # Quarter speed
        """
        return self._send("yt_rate", rate=float(playback_rate))

    def play(self):
        """
        Play the video.

        Example:
            yt.play()
        """
        return self._send("yt_play")

    def pause(self):
        """
        Pause the video.

        Example:
            yt.pause()
        """
        return self._send("yt_pause")

    def loop(self, start, end):
        """
        Set a loop region.

        Args:
            start: Loop start position in seconds
            end: Loop end position in seconds

        Example:
            yt.loop(10, 20)  # Loop between 10 and 20 seconds
            yt.loop(0, 5)    # Loop first 5 seconds
        """
        return self._send("yt_loop", start=float(start), end=float(end))

    def clear_loop(self):
        """
        Clear the loop region.

        Example:
            yt.clear_loop()
        """
        return self._send("yt_clear_loop")

    # =========================================================================
    # PATTERN-BASED METHODS (FoxDot style)
    # =========================================================================

    def pos(self, positions, dur=1):
        """
        Cycle through positions on each beat.

        Args:
            positions: List of positions in seconds [10, 40, 120]
            dur: Duration between changes in beats (default 1)

        Example:
            VidCtrl.pos([10, 40, 120])        # cycle every beat
            VidCtrl.pos([0, 30, 60], dur=4)   # cycle every 4 beats
        """
        if not hasattr(self, '_pos_running'):
            self._pos_running = False

        # Stop any existing pattern
        self._pos_running = False

        if not isinstance(positions, (list, tuple)):
            positions = [positions]

        self._pos_pattern = list(positions)
        self._pos_dur = dur
        self._pos_index = 0
        self._pos_running = True

        self._run_pos_pattern()
        return self

    def _run_pos_pattern(self):
        if not self._pos_running or not self._pos_pattern:
            return

        # Get current position from pattern
        pos = self._pos_pattern[self._pos_index % len(self._pos_pattern)]
        self.seek(pos)

        # Advance index
        self._pos_index += 1

        # Schedule next using FoxDot clock
        try:
            from . import Clock
            Clock.future(self._pos_dur, self._run_pos_pattern)
        except:
            pass

    def stut(self, amounts, dur=1):
        """
        Cycle through stutter amounts on each beat.

        Args:
            amounts: List of stutter amounts [0, 0.1, 0, 0.2]
            dur: Duration between stutters in beats (default 1)

        Example:
            VidCtrl.stut([0, 0.1, 0, 0.2])         # stutter pattern every beat
            VidCtrl.stut([0.1, 0.2, 0.3], dur=0.5) # faster stuttering
        """
        if not hasattr(self, '_stut_running'):
            self._stut_running = False

        self._stut_running = False

        if not isinstance(amounts, (list, tuple)):
            amounts = [amounts]

        self._stut_pattern = list(amounts)
        self._stut_dur = dur
        self._stut_index = 0
        self._stut_running = True

        self._run_stut_pattern()
        return self

    def _run_stut_pattern(self):
        if not self._stut_running or not self._stut_pattern:
            return

        # Get current amount from pattern
        amount = self._stut_pattern[self._stut_index % len(self._stut_pattern)]
        if amount > 0:
            self.stutter(amount)

        self._stut_index += 1

        try:
            from . import Clock
            Clock.future(self._stut_dur, self._run_stut_pattern)
        except:
            pass

    def rates(self, rates, dur=4):
        """
        Cycle through playback rates.

        Args:
            rates: List of rates [1, 0.5, 2, 0.25]
            dur: Duration between changes in beats (default 4)

        Example:
            VidCtrl.rates([1, 0.5, 1, 2])
        """
        if not hasattr(self, '_rate_running'):
            self._rate_running = False

        self._rate_running = False

        if not isinstance(rates, (list, tuple)):
            rates = [rates]

        self._rate_pattern = list(rates)
        self._rate_dur = dur
        self._rate_index = 0
        self._rate_running = True

        self._run_rate_pattern()
        return self

    def _run_rate_pattern(self):
        if not self._rate_running or not self._rate_pattern:
            return

        r = self._rate_pattern[self._rate_index % len(self._rate_pattern)]
        self.rate(r)

        self._rate_index += 1

        try:
            from . import Clock
            Clock.future(self._rate_dur, self._run_rate_pattern)
        except:
            pass

    def stop_patterns(self):
        """Stop all running patterns."""
        self._pos_running = False
        self._stut_running = False
        self._rate_running = False
        self._grain_running = False
        return self

    # =========================================================================
    # BEAT-SYNCED FEATURES
    # =========================================================================

    def beat_loop(self, bars=1, start=None):
        """
        Create a loop that matches the duration of N bars at current BPM.

        Args:
            bars: Number of bars for the loop (default 1)
            start: Start position in seconds (default: current position)

        Example:
            VidCtrl.beat_loop(2)        # 2-bar loop from current position
            VidCtrl.beat_loop(4, start=10)  # 4-bar loop starting at 10s
        """
        try:
            from . import Clock
            # Calculate duration of N bars in seconds
            beats_per_bar = 4  # Assume 4/4 time
            total_beats = bars * beats_per_bar
            seconds_per_beat = 60.0 / Clock.bpm
            loop_duration = total_beats * seconds_per_beat

            # Get start position
            start_pos = float(start) if start is not None else 0
            end_pos = start_pos + loop_duration

            return self.loop(start_pos, end_pos)
        except Exception as e:
            print(f"beat_loop error: {e}")
            return self

    def bloop(self, bars=1, start=None):
        """Alias for beat_loop()"""
        return self.beat_loop(bars, start)

    # =========================================================================
    # GRANULAR VIDEO
    # =========================================================================

    def grain(self, position=None, size=0.1, density=4, spread=1.0, dur=None):
        """
        Granular video - rapid tiny loops around a position with random offsets.
        Like audio granular synthesis but for video.

        Args:
            position: Center position in seconds (None = current)
            size: Grain size - how far back to stutter (default 0.1s)
            density: Grains per beat (default 4)
            spread: Random spread in seconds around position (default 1.0)
            dur: Duration in beats before stopping (None = infinite)

        Example:
            VidCtrl.grain(30)                    # Granular around 30s
            VidCtrl.grain(30, size=0.05, density=8)  # Faster, smaller grains
            VidCtrl.grain(30, spread=3, dur=16)  # 3s spread, stop after 16 beats
        """
        import random

        if not hasattr(self, '_grain_running'):
            self._grain_running = False

        self._grain_running = False  # Stop existing grain

        self._grain_position = float(position) if position is not None else 0
        self._grain_size = float(size)
        self._grain_density = float(density)
        self._grain_spread = float(spread)
        self._grain_dur = dur
        self._grain_beats_elapsed = 0
        self._grain_running = True

        self._run_grain()
        return self

    def _run_grain(self):
        if not self._grain_running:
            return

        import random

        # Check if duration exceeded
        if self._grain_dur is not None:
            self._grain_beats_elapsed += 1.0 / self._grain_density
            if self._grain_beats_elapsed >= self._grain_dur:
                self._grain_running = False
                return

        # Random offset within spread
        offset = random.uniform(-self._grain_spread, self._grain_spread)
        target = max(0, self._grain_position + offset)

        # Seek to position then stutter back
        self.seek(target)

        # Schedule next grain
        try:
            from . import Clock
            grain_interval = 1.0 / self._grain_density
            Clock.future(grain_interval, self._run_grain)
        except:
            pass

    def freeze(self, position=None, intensity=0.5):
        """
        Freeze frame effect - rapid micro-stutters at a position.

        Args:
            position: Position to freeze at (None = current)
            intensity: How aggressive (0.1 to 1.0)

        Example:
            VidCtrl.freeze(30)           # Freeze at 30s
            VidCtrl.freeze(30, intensity=0.8)  # More aggressive
        """
        size = 0.02 + (0.08 * (1 - intensity))
        density = 4 + int(12 * intensity)
        return self.grain(position, size=size, density=density, spread=0.05)

    def unfreeze(self):
        """Stop freeze/grain effect and resume playback."""
        self._grain_running = False
        return self.play()

    # =========================================================================
    # CONVENIENCE METHODS
    # =========================================================================

    def stop(self):
        """Alias for pause() and stops patterns."""
        self.stop_patterns()
        return self.pause()

    def go(self, time_seconds):
        """Alias for seek()."""
        return self.seek(time_seconds)

    def speed(self, rate):
        """Alias for rate()."""
        return self.rate(rate)

    def slow(self):
        """Set half speed."""
        return self.rate(0.5)

    def fast(self):
        """Set double speed."""
        return self.rate(2)

    def normal(self):
        """Set normal speed."""
        return self.rate(1)

    # =========================================================================
    # PATTERN SUPPORT
    # =========================================================================

    def __call__(self, time_seconds):
        """
        Calling yt(30) is equivalent to yt.seek(30).

        Example:
            yt(30)  # Seek to 30 seconds
        """
        return self.seek(time_seconds)

    def __repr__(self):
        status = "connected" if self.connected else "disconnected"
        return f"YouTubeController({self.host}:{self.port}) [{status}]"


# Create singleton instance
# Note: Cannot use 'yt' (player variable) or 'Video' (existing SynthDef)
VidCtrl = YouTubeController()

# Export for use in FoxDot
__all__ = ['VidCtrl', 'YouTubeController']

"""

Audio-Reactive System for FoxDot

Provides SC->Python audio analysis feedback, enabling patterns that react
to live audio (amplitude following, onset detection).

Usage:
    reactive(d1)                        # start analyzing d1's output
    d2 >> pluck(amp=PAmp(d1, scale=2))  # d2 amplitude follows d1
    d3 >> bass(dur=POnset(d1))          # d3 triggers on d1 onsets
    unreactive(d1)                      # stop analyzing d1

"""

from __future__ import absolute_import, division, print_function

import threading
import time

from .Patterns.Main import GeneratorPattern
from .ServerManager import Server
from .Settings import FOXDOT_ANALYZER_FILE

try:
    from .OSC3 import OSCMessage
except ImportError:
    from .OSC import OSCMessage


class _AudioReactive:
    """Manages audio analysis state and SC<->Python communication."""

    def __init__(self):
        self._lock = threading.Lock()
        self._state = {}       # {player_name: {amp, onset, timestamp}}
        self._analyzers = {}   # {player_name: reply_id}
        self._next_id = 0
        self._loaded = False
        self._handler_registered = False

    def _ensure_loaded(self):
        """Load the AudioAnalyzer SynthDef into SC if not already done."""
        if not self._loaded:
            try:
                Server.loadSynthDef(FOXDOT_ANALYZER_FILE)
                self._loaded = True
            except Exception as e:
                print("AudioReactive: Could not load analyzer - {}".format(e))

    def _ensure_handler(self):
        """Register the OSC handler for analysis data if not done."""
        if not self._handler_registered:
            try:
                Server.sclang.addHandler('/foxdot/analysis', self._on_analysis)
                self._handler_registered = True
            except Exception as e:
                print("AudioReactive: Could not register handler - {}".format(e))

    def _on_analysis(self, data):
        """Called by OSC handler when analysis data arrives from SC."""
        if len(data) < 3:
            return
        reply_id = int(data[0])
        amp = float(data[1])
        onset = float(data[2])

        with self._lock:
            # Find player name by reply_id
            for name, rid in self._analyzers.items():
                if rid == reply_id:
                    self._state[name] = {
                        'amp': amp,
                        'onset': onset,
                        'timestamp': time.time()
                    }
                    break

    def follow(self, player):
        """Start audio analysis on a player's output bus."""
        self._ensure_loaded()
        self._ensure_handler()

        name = str(player)
        if name in self._analyzers:
            return  # Already following

        reply_id = self._next_id
        self._next_id += 1

        with self._lock:
            self._analyzers[name] = reply_id
            self._state[name] = {'amp': 0.0, 'onset': 0.0, 'timestamp': 0.0}

        # Send OSC message to SC to start the analyzer
        try:
            bus = player.bus
            msg = OSCMessage()
            msg.setAddress('/foxdot/analyzer_ctl')
            msg.append("start")
            msg.append(int(bus))
            msg.append(reply_id)
            msg.append(10)  # analysis rate Hz
            msg.append(0)   # node placeholder
            Server.sclang.send(msg)
        except Exception as e:
            print("AudioReactive: Could not start analyzer for {} - {}".format(name, e))

    def unfollow(self, player):
        """Stop audio analysis on a player."""
        name = str(player)
        if name not in self._analyzers:
            return

        reply_id = self._analyzers[name]

        # Send stop message to SC
        try:
            msg = OSCMessage()
            msg.setAddress('/foxdot/analyzer_ctl')
            msg.append("stop")
            msg.append(reply_id)
            Server.sclang.send(msg)
        except Exception as e:
            print("AudioReactive: Could not stop analyzer for {} - {}".format(name, e))

        with self._lock:
            del self._analyzers[name]
            if name in self._state:
                del self._state[name]

    def get(self, player, param='amp'):
        """Read the latest analysis value for a player."""
        name = str(player)
        with self._lock:
            state = self._state.get(name, {})
            return state.get(param, 0.0)

    def is_following(self, player):
        """Check if a player is being analyzed."""
        return str(player) in self._analyzers


# Singleton instance
AudioReactive = _AudioReactive()


class PAmp(GeneratorPattern):
    """Pattern that follows another player's amplitude.

    Usage: d2 >> pluck(amp=PAmp(d1, scale=2))
    """
    def __init__(self, player, scale=1, smooth=0.5, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.player = player
        self.scale = scale
        self.smooth = smooth
        self._last = 0.0
        self.name = "PAmp"
        self.data = "PAmp({})".format(player)

    def func(self, index):
        raw = AudioReactive.get(self.player, 'amp')
        # Simple exponential smoothing
        self._last = self._last * self.smooth + raw * (1 - self.smooth)
        return self._last * self.scale


class POnset(GeneratorPattern):
    """Pattern that triggers on onset detection from another player.

    Returns 1 on detected onset, 0 otherwise.
    Usage: d3 >> play("x", dur=POnset(d1))
    """
    def __init__(self, player, threshold=0.5, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.player = player
        self.threshold = threshold
        self.name = "POnset"
        self.data = "POnset({})".format(player)

    def func(self, index):
        onset = AudioReactive.get(self.player, 'onset')
        return 1 if onset >= self.threshold else 0


class PReact(GeneratorPattern):
    """Generic audio-reactive pattern with custom mapping function.

    Usage: d2 >> pluck(amp=PReact(d1, 'amp', lambda x: x * 2 + 0.1))
    """
    def __init__(self, player, param='amp', func=None, **kwargs):
        GeneratorPattern.__init__(self, **kwargs)
        self.player = player
        self.param = param
        self._map_func = func if func is not None else lambda x: x
        self.name = "PReact"
        self.data = "PReact({}, {})".format(player, param)

    def func(self, index):
        raw = AudioReactive.get(self.player, self.param)
        return self._map_func(raw)


# Convenience functions
def reactive(player):
    """Start audio analysis on a player's output."""
    AudioReactive.follow(player)

def unreactive(player):
    """Stop audio analysis on a player."""
    AudioReactive.unfollow(player)

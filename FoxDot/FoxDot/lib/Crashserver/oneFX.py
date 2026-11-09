"""
One in FoxDot: One's units, presets and effects as FoxDot words, so a song exported from One reads as FoxDot, and the
same lines typed from scratch sound the same. Installed by soundDesign/one/foxdot/install.sh (with onePresets.py,
generated from One's own patches).

Sounds: One's presets, called like any synth; your own with sound(...).
    b1 >> sub_acid([0, 0, 7, 0], dur=1/4)            # Sub's "acid bass"
    p1 >> fm_glass([(0, 2, 4)], dur=8)               # Bell's "glass pad"
    snd_bass = sound(sub_acid, cutoff=300, res=0.8)  # a sound of your own (from a preset, or a synth: one_sub)
    b1 >> snd_bass([0, 3], dur=1/2, cutoff=linvar([300, 2000], 16))   # what you pass still wins

Drums: a synth per voice of each One kit (kit, kit_tight, kit_boom, kit_dirty, berlin, iron_floor, roll_call, bunker,
berlin_tight) and voice (kick, snare, clap, chat, ohat, tom, rim, bell; Berlin's: kick, clap, chat, ohat, rim, tom, stab, ride),
played as any FoxDot synth; velo is One's velocity (an accent: louder and brighter), amp FoxDot's own volume:
    d1 >> iron_floor_kick(dur=1, velo=[1, 0.75, 0.75, 0.75], every=1)   # every: the rumble ducks each kick (beats)
    d2 >> iron_floor_clap(dur=2, delay=1, tohall=0.2)
    d3 >> iron_floor_chat(dur=1/4, velo=[1, 0.75, 0.75, 0.75])
Or as One's drum machines show them (a sixteenth a step; X accented):  d1 >> iron_floor.kick.steps("X...x...x...x...")

Effects: running all the time, each on its own bus; sounds reach them by name.
    fx_hall("cathedral", decay=9)          # a One preset, and what you change
    fx_echo(div=7, fb=0.6, into="hall")    # the echo feeding the hall (send= how much; out= how much to the speakers)
    fx_duck("pump (side)")                 # a compressor listening to what is sent to `side`
    fx_drive("valve crunch", into="duck", out=0)
    p1 >> fm_glass(..., tohall=0.5)        # a send;  dry=0: only through the effects
    b1 >> sub_bass(..., toduck=1, dry=0)   # through the ducker
    d1 >> iron_floor_kick(dur=1, side=1)   # what the ducker listens to
    fx_echo(fb=linvar([0.3, 0.85], [14, 2]))   # a setting can be a var: it keeps moving
    fx_stop()                              # one (fx_stop("hall")) or all
A sound sent only to effects (dry=0) plays dry while none of them runs, so nothing goes silent when an effect is
stopped or not started yet; an effect sent only into another (out=0, into=…) plays out while that one is stopped.

Effects run in signal order (drive, echo, aux, duck, hall), whatever order they are started in.
"""
import re
from ..ServerManager import Server
from ..OSC3 import OSCMessage
from ..SCLang.SynthDef import SynthDefProxy
from .onePresets import SOUNDS, KITS, FX_DEFAULTS, FX_PRESETS


# ---- sounds ----

class OneSound(object):
    """ A synth with settings: called like one. What the call passes wins over the sound's own settings. """
    def __init__(self, synth, info="", **settings):
        self.synth, self.info, self.settings = synth, info, settings

    def __call__(self, degree=None, **kwargs):
        a = dict(self.settings)
        a.update(kwargs)
        return SynthDefProxy(self.synth, degree, a)

    def steps(self, pattern, swing=0.5, soft=0.75, **kwargs):
        """ A drum line from steps: a sixteenth each, 'X' accented (velo 1), 'x' a hit (velo `soft`), '.' nothing;
            swing moves the odd sixteenths (0.5 straight). Gives dur, delay and velo, as One's drum machines play. """
        hits = [(k / 4.0 + ((swing - 0.5) * 0.5 if k % 2 else 0), 1 if ch == "X" else soft) for k, ch in enumerate(pattern) if ch in "xX"]
        if not hits:
            return self(dur=len(pattern) / 4.0, amp=0, **kwargs)
        L = len(pattern) / 4.0
        dur = [(hits[i + 1][0] if i + 1 < len(hits) else L + hits[0][0]) - t for i, (t, _) in enumerate(hits)]
        a = dict(dur=dur if len(set(dur)) > 1 else dur[0], velo=[v for _, v in hits])
        if hits[0][0] > 0:
            a["delay"] = hits[0][0]
        a.update(kwargs)
        return self(**a)

    def __repr__(self):
        return "<{} {}: {}>".format(self.synth, self.info, ", ".join("{}={}".format(k, v) for k, v in self.settings.items()))


def sound(base, **settings):
    """ A new sound: from a synth (one_sub, kit_kick…) or a sound (sub_acid, iron_floor.kick), with these settings. """
    if isinstance(base, OneSound):
        a = dict(base.settings)
        a.update(settings)
        return OneSound(base.synth, base.info, **a)
    return OneSound(base if isinstance(base, str) else base.name, "", **settings)


class OneKit(object):
    """ A drum kit: a sound per voice (kick, snare, clap, c_hat, o_hat, tom, rim, bell; Berlin: … stab, ride). """
    def __init__(self, info, voices):
        self.info = info
        for name, s in voices.items():
            setattr(self, name, s)
        self.voices = list(voices)

    def __repr__(self):
        return "<kit {}: {}>".format(self.info, ", ".join(self.voices))


for _n, (_s, _a, _w) in SOUNDS.items():
    globals()[_n] = OneSound(_s, _w, **_a)
for _n, (_vs, _w) in KITS.items():
    globals()[_n] = OneKit(_w, dict((_v, OneSound(_s, "{} {}".format(_w, _v), **_a)) for _v, _s, _a in _vs))
    # and each voice as a synth of its own: iron_floor_kick, kit_tight_chat… (the plain kits' are the SynthDefs' names,
    # kit_kick, berlin_kick: the same synths, with One's own settings)
    for _v, _s, _a in _vs:
        globals()["{}_{}".format(_n, _s.split("_", 1)[1])] = OneSound(_s, "{} {}".format(_w, _v), **_a)


# ---- effects, each on its bus (the instruments' sends: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14) ----

ONE_BUS = {"drive": 2, "duck": 6, "hall": 8, "echo": 10, "aux": 12}
ONE_SIDE = 14
ONE_ORDER = ["drive", "echo", "aux", "duck", "hall"]
ONE_SYNTH = {"drive": "one_fx_drive", "duck": "one_fx_squash", "hall": "one_fx_hall", "echo": "one_fx_echo"}
_fx = {}          # name: [node, kind, params]
_group = [None]
ONE_ON = 15360    # control bus ONE_ON + an effect's bus: 1 while it runs (One's synths read it: a sound sent only to an
                  # effect that is not running plays dry instead of not at all; an effect into one not running, to the speakers)


def _send(addr, args):
    m = OSCMessage(addr)
    m.append(args)
    Server.client.send(m)


def _running(name, on):
    if name in ONE_BUS:
        _send("/c_set", [ONE_ON + ONE_BUS[name], 1 if on else 0])


try:   # none runs yet (a FoxDot restarted with the server still up may have left them set)
    for _b in ONE_BUS.values():
        _send("/c_set", [ONE_ON + _b, 0])
except Exception:
    pass


_moving = {}      # effect name: {param: a FoxDot var}, sent again every eighth of a beat


def _args(kw):
    out = []
    for k, v in kw.items():
        out += [k, float(v.now()) if hasattr(v, "now") else float(v)]
    return out


def _keep_moving():
    """ Every eighth of a beat: the effects' settings given as vars (linvar…), at their value now. """
    from .. import Clock
    for name, ps in list(_moving.items()):
        if name in _fx and ps:
            _send("/n_set", [_fx[name][0]] + _args(ps))
    if any(_moving.values()):
        Clock.schedule(_keep_moving, Clock.now() + 0.125)
    else:
        _moving.clear()


def _track(name, params):
    """ Settings given as vars keep moving; a plain value given later stops that one. """
    m = _moving.setdefault(name, {})
    idle = not any(_moving.values())
    for k, v in params.items():
        if hasattr(v, "now"):
            m[k] = v
        else:
            m.pop(k, None)
    if idle and any(_moving.values()):
        _keep_moving()


def _fx_start(name, kind, preset, into, send, out, params):
    """ Start effect `name` (a kind: hall, echo, duck, drive) on its bus; if it runs, change only what is given. """
    if preset:
        preset = re.sub(r"[^a-z0-9]+", "_", preset.lower()).strip("_")     # One's names: "pump (side)" = pump_side
        if preset not in FX_PRESETS[kind]:
            raise ValueError("{} has no preset '{}' (it has: {})".format(kind, preset, ", ".join(FX_PRESETS[kind])))
    route = {}
    if out is not None:
        route["outamt"] = out
    if into is not None:
        route.update(out2b=ONE_BUS[into], out2amt=1 if send is None else send)
    elif send is not None:
        route["out2amt"] = send
    if name in _fx and _fx[name][1] == kind:
        p = dict(FX_PRESETS[kind][preset]) if preset else {}
        p.update(params)
        p.update(route)
        _fx[name][2].update(p)
        _send("/n_set", [_fx[name][0]] + _args(p))
        _track(name, p)
        return
    if name in _fx:
        fx_stop(name)
    p = dict(FX_DEFAULTS[kind])
    if kind in ("hall", "echo"):
        p["mix"] = 1                                  # an effect on a send: only the effect
    if preset:
        p.update(FX_PRESETS[kind][preset])
    p.update(params)
    if kind == "echo":
        from .. import Clock
        p.setdefault("beat_dur", 60.0 / float(Clock.bpm))
    if kind == "duck":
        p["sideb"] = ONE_SIDE
        p["key"] = params.get("key", 2)     # listens to `side` (key=1: to itself, a glue compressor)
    p.update(inb=ONE_BUS[name], outb=0, outamt=1, out2b=-1, out2amt=0)
    p.update(route)
    if _group[0] is None:
        _group[0] = Server.nextnodeID()
        _send("/g_new", [_group[0], 3, 1])     # just after the notes' group
    node = Server.nextnodeID()
    later = [_fx[n][0] for n in ONE_ORDER[ONE_ORDER.index(name) + 1:] if n in _fx]
    _send("/s_new", [ONE_SYNTH[kind], node] + ([2, later[0]] if later else [1, _group[0]]) + _args(p))
    _fx[name] = [node, kind, p]
    _running(name, True)
    _track(name, p)


def fx_hall(preset=None, into=None, send=None, out=None, **params):
    """ One's Hall: pre, size, decay, damp, width (mix 1: only the reverb; it is fed by tohall). Presets: room, plate, cathedral. """
    _fx_start("hall", "hall", preset, into, send, out, params)


def fx_echo(preset=None, into=None, send=None, out=None, **params):
    """ One's Echo: sync (1: div of the beat), div, ms, fb, tone, mode (1 ping-pong). Presets: dub throw, slapback, ping 1/4. """
    _fx_start("echo", "echo", preset, into, send, out, params)


def fx_duck(preset=None, into=None, send=None, out=None, **params):
    """ One's Squash, listening to `side`: thr, ratio, att, rel, knee, gain. Presets: glue, pump (side), drum smash, vocal level. """
    _fx_start("duck", "duck", preset, into, send, out, params)


def fx_drive(preset=None, into=None, send=None, out=None, **params):
    """ One's Drive, fed by todrive: type (0 tape … 4 fuzz), drive, tone, level, mix. Presets: warm tape, valve crunch, broken speaker, wavefolder. """
    _fx_start("drive", "drive", preset, into, send, out, params)


def fx_aux(kind, preset=None, into=None, send=None, out=None, **params):
    """ A second effect of any kind on the aux bus (fed by toaux): fx_aux("hall", "cathedral"). """
    _fx_start("aux", kind, preset, into, send, out, params)


def fx_stop(name=None):
    """ Stop one effect, or all of them. """
    for n in ([name] if name else list(_fx)):
        if n in _fx:
            _send("/n_free", [_fx.pop(n)[0]])
            _running(n, False)
        _moving.pop(n, None)
    if name is None and _group[0] is not None:
        _send("/n_free", [_group[0]])
        _group[0] = None


# ---- what earlier exports use ----

def one_fx(name, synthdef=None, **params):
    """ An effect on explicit buses (exports before the named effects). """
    kind = {v: k for k, v in ONE_SYNTH.items()}.get(synthdef, name)
    if name in _fx and synthdef in (None, ONE_SYNTH.get(_fx[name][1])):
        _send("/n_set", [_fx[name][0]] + _args(params))
        return
    if _group[0] is None:
        _group[0] = Server.nextnodeID()
        _send("/g_new", [_group[0], 3, 1])
    node = Server.nextnodeID()
    _send("/s_new", [synthdef, node, 1, _group[0]] + _args(params))
    _fx[name] = [node, kind, params]
    _running(name, True)


def one_fx_stop(name=None):
    fx_stop(name)


def one_chunks(files, size):
    """ A rendered part, for loop(one_chunks([...], size), dur=size): FoxDot picks a looping player's file by its event's
    place on the clock (beat // size), so the list is turned to start with the section's first chunk at the next
    multiple of `size` (the section's start: the song was fired on such a beat). """
    from .. import Clock
    n0 = int(-(-(Clock.now() + 1e-6) // size))
    k = len(files)
    r = n0 % k
    return files[-r:] + files[:-r] if r else list(files)

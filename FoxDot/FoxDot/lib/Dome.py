"""
Dome — spatial output for multi-speaker domes (25 speakers, 4 rings).

When the dome is active, every note's exit node becomes `makeSoundDome`
instead of `makeSound`: the player's stereo signal is panned onto a
25-channel private bus by direction (az / elev / dspread). From that bus:

  * a monitor synth renders the dome to stereo from a virtual listener
    position (driven by the browser page dome/dome_listener.html via
    dome/bridge.mjs), so you can rehearse the dome on 2 speakers;
  * a direct synth copies the 25 channels to hardware outputs (gig mode,
    e.g. into Inferno / Dante).

Player attributes:
    az       azimuth in degrees, 0 = front, + = right (-180..180)
    elev     elevation in degrees, 0 = bottom ring / ear height, 90 = zenith
    dspread  angular width of the source in degrees (0 = default 30)

    p1 >> pluck([0, 2, 4], az=linvar([-180, 180], 16), elev=15)
    d1 >> play("x-o-", dspread=80)

Usage:
    dome.start()             # dome on, stereo monitor on outs 0/1
    dome.layout("real")      # pan with the measured speaker positions
    dome.direct(2)           # also send the 25 speakers to hardware outs 2..26
    dome.direct(None)        # stop direct outs
    dome.monitor(False)      # mute the stereo monitor (gig)
    dome.stop()              # back to plain stereo makeSound
"""

import os
import tempfile

N_SPEAKERS = 25

# azimuth, elevation, distance (m) — Spat convention, from dome/dome.txt
LAYOUTS = {
    "real": [
        (0, 90, 3.5),
        (-51.454, 46.375, 4.559), (51.454, 46.375, 4.559), (128.546, 46.375, 4.559), (-128.546, 46.375, 4.559),
        (-48.152, 24.141, 5.355), (0, 33.892, 3.927), (48.152, 24.141, 5.355), (90, 31.033, 4.248),
        (131.848, 24.141, 5.355), (-180, 33.892, 3.927), (-131.848, 24.141, 5.355), (-90, 31.033, 4.248),
        (-41.717, 8.017, 5.736), (-8.187, 10.578, 4.358), (8.187, 10.578, 4.358), (41.717, 8.017, 5.736),
        (76.149, 6.742, 6.814), (103.851, 6.742, 6.814), (138.283, 8.017, 5.736), (171.813, 10.578, 4.358),
        (-171.813, 10.578, 4.358), (-138.283, 8.017, 5.736), (-103.851, 6.742, 6.814), (-76.149, 6.742, 6.814),
    ],
    "ideal": (
        [(0, 90, 3.5)]
        + [(a, 60, 3.5) for a in (-45, 45, 135, -135)]
        + [(a, 30, 3.5) for a in (-45, 0, 45, 90, 135, 180, -135, -90)]
        + [(a, 0, 3.5) for a in (-45, -15, 15, 45, 75, 105, 135, 165, -165, -135, -105, -75)]
    ),
}

RINGS = {"top": [1], "quad": [2, 3, 4, 5], "mid": list(range(6, 14)), "low": list(range(14, 26))}


def _xyz(az, el, d=1.0):
    """ Spat coordinates: x right, y front, z up """
    import math
    a, e = math.radians(az), math.radians(el)
    return (d * math.cos(e) * math.sin(a), d * math.cos(e) * math.cos(a), d * math.sin(e))


def _sc_array(values):
    return "[" + ", ".join("{:.5f}".format(v) for v in values) + "]"


class Dome(object):

    def __init__(self, server):
        self.server = server
        self.active = False
        self.bus = None
        self.layout_name = "ideal"
        self.direct_offset = None
        self.monitor_on = True
        self.bridge_port = 57140
        self._file = os.path.join(tempfile.gettempdir(), "foxdot_dome.scd")

    def __repr__(self):
        if not self.active:
            return "<Dome off>"
        direct = "outs {}..{}".format(self.direct_offset, self.direct_offset + N_SPEAKERS - 1) if self.direct_offset is not None else "off"
        return "<Dome on · layout {} · bus {} · monitor {} · direct {}>".format(
            self.layout_name, self.bus, "on" if self.monitor_on else "off", direct)

    # -- SC code -----------------------------------------------------------

    def _send_code(self, code):
        with open(self._file, "w") as f:
            f.write(code)
        self.server.loadSynthDef(self._file)

    def _reserve_bus(self):
        """ Takes the top 32 audio busses away from FoxDot's rotating bus allocator """
        if self.bus is None:
            self.bus = int(self.server.max_busses) - 32
            self.server.max_busses = self.bus
            if self.server.bus + 1 >= self.server.max_busses:
                self.server.bus = self.server.num_input_busses + self.server.num_output_busses
        return self.bus

    def _defs(self):
        spk = LAYOUTS[self.layout_name]
        dirs = [c for (az, el, _) in spk for c in _xyz(az, el)]
        pos = [c for (az, el, d) in spk for c in _xyz(az, el, d)]
        return """
SynthDef(\\makeSoundDome, { |bus, sus, domebus, az=0, elev=0, dspread=0|
    var osc, s, w, dirs, gains;
    osc = In.ar(bus, 2);
    osc = EnvGen.ar(Env([1, 1, 0], [sus * 8, 0.1]), doneAction: 14) * osc;
    DetectSilence.ar(osc, amp: 0.0001, time: 0.1, doneAction: 14);
    s = (dspread <= 0).if(30, dspread);
    w = s * 0.4;  // L and R channels sit either side of az
    dirs = %(dirs)s.clump(3);
    gains = { |a, e|
        var v, g;
        a = a * (pi / 180); e = e * (pi / 180);
        v = [e.cos * a.sin, e.cos * a.cos, e.sin];
        g = dirs.collect { |d|
            var ang = ((v[0] * d[0]) + (v[1] * d[1]) + (v[2] * d[2])).clip(-1, 1).acos;
            (ang.squared.neg / (2 * (s * (pi / 180)).squared)).exp
        };
        g / (g.squared.sum.sqrt.max(0.0001))
    };
    Out.ar(domebus, (gains.(az - w, elev) * osc[0]) + (gains.(az + w, elev) * osc[1]));
    SendReply.kr(Impulse.kr(0), '/dome/note', [az, elev, s]);
}).add;

SynthDef(\\domeMonitor, { |inbus, out=0, amp=1, lx=0, ly=0, lz=0, yaw=0, pitch=0|
    var spk, sig, cy, sy, cp, sp, x, y, z, mix;
    spk = NamedControl.kr(\\spk, %(pos)s);
    sig = InFeedback.ar(inbus, %(n)d);
    SendPeakRMS.kr(sig, 20, 3, '/dome/levels');
    #x, y, z = [lx, ly, lz].lag(0.05);
    yaw = (yaw * (pi / 180)).lag(0.05); pitch = (pitch * (pi / 180)).lag(0.05);
    cy = yaw.cos; sy = yaw.sin; cp = pitch.cos; sp = pitch.sin;
    mix = %(n)d.collect { |i|
        var px = spk[i * 3], py = spk[i * 3 + 1], pz = spk[i * 3 + 2];
        var dx = px - x, dy = py - y, dz = pz - z;
        var dist = (dx.squared + dy.squared + dz.squared).sqrt.max(0.3);
        var right = (dx * cy) - (dy * sy);
        var front = (dx * sy) + (dy * cy);
        var front2 = (front * cp) + (dz * sp);
        var plen = (px.squared + py.squared + pz.squared).sqrt.max(0.001);
        // speakers aim at the centre: quieter when you are behind them
        var cosA = ((px * dx) + (py * dy) + (pz * dz)) / (plen * dist);
        var cone = (cosA.clip(-1, 1).acos * (180 / pi)).linlin(70, 150, 1, 0.35);
        var gain = (3.5 / dist).min(3) * cone;
        var s = DelayL.ar(sig[i], 0.06, (dist / 343).lag(0.1));
        s = LPF.ar(s, (front2 / dist).linexp(-1, 0, 3500, 20000));  // behind you = duller
        Pan2.ar(s, (right / dist).clip(-1, 1), gain)
    }.sum;
    Out.ar(out, mix * amp);
}).add;

SynthDef(\\domeDirect, { |inbus, out=2, amp=1|
    Out.ar(out, InFeedback.ar(inbus, %(n)d) * amp);
}).add;
""" % {"dirs": _sc_array(dirs), "pos": _sc_array(pos), "n": N_SPEAKERS}

    def _setup(self):
        return """
~domeBridge = NetAddr("127.0.0.1", %(port)d);
OSCdef(\\domeNote, { |msg| ~domeBridge.sendMsg('/dome/note', msg[3], msg[4], msg[5]) }, '/dome/note');
OSCdef(\\domeLevels, { |msg| ~domeBridge.sendMsg('/dome/levels', *msg[3..].clump(2).collect(_[1])) }, '/dome/levels');
OSCdef(\\domeListener, { |msg|
    ~domeMon !? { ~domeMon.set(\\lx, msg[1], \\ly, msg[2], \\lz, msg[3], \\yaw, msg[4], \\pitch, msg[5]) }
}, '/dome/listener');
OSCdef(\\domeSpeakers, { |msg| ~domeMon !? { ~domeMon.setn(\\spk, msg[1..]) } }, '/dome/speakers');
OSCdef(\\domeMonAmp, { |msg| ~domeMon !? { ~domeMon.set(\\amp, msg[1]) } }, '/dome/monitor');
""" % {"port": self.bridge_port}

    def _free_synths(self):
        return """
~domeMon !? { ~domeMon.free }; ~domeMon = nil;
~domeDirect !? { ~domeDirect.free }; ~domeDirect = nil;
"""

    def _start_synths(self):
        code = """
~domeGroup.isNil.if { ~domeGroup = Group.head(RootNode(Server.default)) };
"""
        if self.monitor_on:
            code += "~domeMon = Synth.head(~domeGroup, \\domeMonitor, [\\inbus, %d, \\out, 0]);\n" % self.bus
        if self.direct_offset is not None:
            code += "~domeDirect = Synth.tail(~domeGroup, \\domeDirect, [\\inbus, %d, \\out, %d]);\n" % (self.bus, self.direct_offset)
        return code

    def _reload(self, with_defs=True):
        code = "fork {\n"
        if with_defs:
            code += self._defs() + "\nServer.default.sync;\n"
        code += self._setup() + self._free_synths() + "Server.default.sync;\n" + self._start_synths()
        code += '"Dome: %s".postln;\n}\n' % repr(self).replace('"', "'")
        self._send_code(code)

    # -- Public API --------------------------------------------------------

    def start(self, layout=None, monitor=None, direct=None):
        if layout is not None:
            self._check_layout(layout)
            self.layout_name = layout
        if monitor is not None:
            self.monitor_on = bool(monitor)
        if direct is not None:
            self.direct_offset = direct
        self._reserve_bus()
        self._reload()
        self.active = True
        return self

    def stop(self):
        self.active = False
        if self.bus is not None:
            self._send_code("fork {\n" + self._free_synths() + '"Dome: off".postln;\n}\n')
        return self

    def layout(self, name):
        """ 'ideal' or 'real' — speaker directions used for panning (and monitor positions) """
        self._check_layout(name)
        self.layout_name = name
        if self.active:
            self._reload()
        return self

    def monitor(self, on=True):
        """ Stereo monitor (virtual listener) on hardware outs 0/1 """
        self.monitor_on = bool(on)
        if self.active:
            self._reload(with_defs=False)
        return self

    def direct(self, offset=2):
        """ Copy the 25 dome channels to hardware outs offset..offset+24 (None = off).
            Needs numOutputBusChannels >= offset + 25 in FoxDot.sc """
        self.direct_offset = offset
        if self.active:
            self._reload(with_defs=False)
        return self

    @staticmethod
    def _check_layout(name):
        if name not in LAYOUTS:
            raise ValueError("Dome layout must be one of {}".format(list(LAYOUTS)))

    # -- Used by ServerManager.get_exit_node -------------------------------

    def exit_args(self, packet):
        def num(key):
            try:
                return float(packet.get(key, 0) or 0)
            except (TypeError, ValueError):
                return 0.0
        return ['domebus', self.bus, 'az', num('az'), 'elev', num('elev'), 'dspread', num('dspread')]

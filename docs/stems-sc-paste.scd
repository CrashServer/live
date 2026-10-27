// stems-sc-paste.scd — paste this whole block into SC IDE and evaluate
// (Cmd+Enter on the block, or Cmd+A then Cmd+Enter). Reusable: re-evaluating
// just refreshes the handlers since OSCdef is named/replaceable.
//
// This sidesteps needing to recompile the FoxDot class library — useful for
// testing the stem-recording system right now without restarting webTroop.

(
    ~stemSynths = Dictionary.new;
    ~stemBufs   = Dictionary.new;

    SynthDef(\stemDiskOut, { | bus = 32, buf = 0 |
        DiskOut.ar(buf, In.ar(bus, 2));
    }).add;

    SynthDef(\stemTap, { | bus = 32, gain = 1.0 |
        Out.ar(0, In.ar(bus, 2) * gain);
    }).add;

    // /foxdot_stems_start [bus, path, bus, path, ...]
    OSCdef(\stemsStart, { | msg |
        var i, bus, path, buf;
        ("[stems] starting" + ((msg.size - 1) / 2) + "stem recordings").postln;
        i = 1;
        while ({ i < msg.size }, {
            bus = msg[i].asInteger;
            path = msg[i + 1].asString;
            buf = Buffer.alloc(Server.default, 65536, 2);
            buf.write(path, "wav", "int16", 0, 0, true);
            ~stemBufs[bus] = buf;
            ~stemSynths[bus] = [
                Synth.tail(nil, \stemDiskOut, [\bus, bus, \buf, buf.bufnum]),
                Synth.tail(nil, \stemTap,     [\bus, bus])
            ];
            ("[stems]  bus" + bus + "->" + path).postln;
            i = i + 2;
        });
    }, '/foxdot_stems_start');

    // /foxdot_stems_stop
    OSCdef(\stemsStop, { | msg |
        ("[stems] stopping" + ~stemSynths.size + "stems").postln;
        ~stemSynths.do({ | pair | pair[0].free; pair[1].free; });
        ~stemBufs.do({ | buf |
            AppClock.sched(0.25, { buf.close; buf.free; nil; });
        });
        ~stemSynths = Dictionary.new;
        ~stemBufs   = Dictionary.new;
        "[stems] done".postln;
    }, '/foxdot_stems_stop');

    "[stems] handlers + SynthDefs installed. Ready.".postln;
)

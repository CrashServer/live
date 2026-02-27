SynthDef.new(\timeStretch, {
    arg buf, pos=0, rate=1, sus=1, amp=1, pan=0, stretchratio=1, windowSize=0.2, overlaps=8, bus=0;
    var osc, env;
    osc = Warp1.ar(2, buf,
        Line.kr(pos, pos + ((1-pos)/stretchratio), sus),
        rate, windowSize, -1, overlaps, 0, 2
    );
    env = EnvGen.ar(Env([0,1,1,0],[0.01, sus-0.02, 0.01]), doneAction: 2);
    osc = osc * env * amp;
    Out.ar(bus, Pan2.ar(osc, pan));
}).add;

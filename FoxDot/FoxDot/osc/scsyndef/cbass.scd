SynthDef.new(\cbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, cutoff=200, rq=0.9, boost=1.5, detune=0.01, follow=2|
    var osc1, osc2, subOsc, env, filt, mod, dist, oscSum, freqFollower, dynamicCutoff;

    freq = In.kr(bus, 1);
    freq = [freq, freq+fmod];

    osc1 = Saw.ar(freq * [1 - detune, 1 + detune]);
    osc2 = Pulse.ar(freq * [0.5 - detune, 0.5 + detune], 0.13);

    subOsc = SinOsc.ar(freq * 0.25);
		  subOsc = RHPF.ar(subOsc*0.5, 40, 0.48);

    mod = SinOsc.kr(vib).range(0.9, 1.1);
    osc1 = osc1 * mod;
    osc2 = osc2 * mod;
    subOsc = subOsc * mod;

    oscSum = (osc1 + osc2 + subOsc) * 0.5;

    dist = tanh(oscSum * (1 + boost * 5));

    env = EnvGen.kr(Env.perc(0.01, sus * 1.2), doneAction: 2);

    freqFollower = Lag.kr(freq[0], 0.1);
    dynamicCutoff = Lag.kr(cutoff + (freqFollower * follow), 0.1).clip(1, 20000);

    filt = RLPF.ar(dist, dynamicCutoff, rq);
    filt = Compander.ar(filt, filt, thresh: 0.2, slopeAbove: 0.5, slopeBelow: 1, clampTime: 0.01, relaxTime: 0.1);

    filt = Mix(filt) * env * amp * 0.5;
    filt = Pan2.ar(filt, pan);

    ReplaceOut.ar(bus, filt);
}).add;

SynthDef.new(\swiss,
{|freq,gate=1,decay=1,rate=1,fmod=0,blur=1,rq=0,cutoff=8000,saw=1,pulse=1,sin=1,pw=0.5,atk=0.001,sus=1,rel=0.91,pan=0,bus=0,amp=1,dur=1|
	var osc, sig, vEnv,fEnv, volfunc;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	vEnv = EnvGen.ar(Env.adsr(atk,decay,1,rel),timeScale:sus,doneAction:2);
	fEnv = EnvGen.ar(Env.perc(0.01,1,1,-4),timeScale:sus,doneAction:2);
	sig = (((SawDPW.ar(freq, pw) + SawDPW.ar(freq + rate))*saw) + ((Pulse.ar(freq,pw) + Pulse.ar(freq + rate))*pulse) + ((SinOsc.ar(freq, pw) + SinOsc.ar(freq + rate))*sin));
	sig=sig*vEnv;
	volfunc = pulse+saw+sin;
	sig=sig/10;
	sig = MoogFF.ar(sig,fEnv*cutoff,rq,0);
	sig=Mix(sig*amp);
	osc = Pan2.ar(sig,pan,vEnv);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \basic,
	tags: []
	)
).add;
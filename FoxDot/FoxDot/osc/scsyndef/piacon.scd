SynthDef.new(\piacon,
{|bus=0, freq=440, fmod=0, gate=1, amp=0.5, velocity=64, hard=0.55, sus=1, blur=1, velhard=0.45, pan=0, vib=0, wide=0.6, muffle=0.8, stretch=0.1, sympa=0.4, body=0.3, hammer=0.12, tone=0.4|
	var env, son, piano, pmono, hit, symp, bodyres;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = freq + fmod;

	// --- core exciter: mda piano (warmer defaults than pianovel) ---
	piano = MdaPiano.ar(freq, gate, vel: velocity, release: 0.9,
		hard: hard, velhard: velhard, muffle: muffle, stretch: stretch,
		stereo: wide, sustain: sus);
	pmono = (piano[0] + piano[1]) * 0.4;

	// --- hammer-noise transient (attack thock, velocity scaled) ---
	hit = LPF.ar(PinkNoise.ar, 2200 + (freq * 2))
		* EnvGen.ar(Env.perc(0.0008, 0.045))
		* hammer * (velocity / 90);

	// --- sympathetic string resonance (tuned to the played note) ---
	symp = DynKlank.ar(`[
		[freq, freq * 2, freq * 3.001, freq * 4.02, freq * 5.04],
		[1, 0.5, 0.32, 0.2, 0.12],
		[sus * 2.2, sus * 1.6, sus * 1.1, 0.8, 0.5] ],
		(pmono + hit) * 0.25) * sympa;

	// --- fixed body / soundboard resonances (wooden grand character) ---
	bodyres = Klank.ar(`[
		[82, 116, 161, 226, 312, 408],
		[0.05, 0.04, 0.035, 0.025, 0.018, 0.012],
		[0.2, 0.17, 0.14, 0.11, 0.08, 0.06] ],
		pmono * 0.4) * body;

	son = piano + symp + hit + bodyres;

	// low-end body boost (as in pianovel) + brightness control
	son = (TwoPole.ar(son, 200, 0.4, mul: 0.5) + (son * 0.5));
	son = son + (BPF.ar(son, 2800, 0.8) * tone * 0.5);

	env = EnvGen.ar(Env(times: [sus], levels: [(amp * 1.5), (amp * 1.5)], curve: 'step'), doneAction: 0);
	son = (son * env * 1.3);
	son = HPF.ar(son, 32);
	son = LeakDC.ar(son);
	ReplaceOut.ar(bus, Splay.ar(son, 1, 1, pan))},
	metadata: (
	credit: "CrashServer",
	description: "MdaPiano with hammer transient, sympathetic + body resonance",
	category: \keyboard,
	tags: []
	)
).add;

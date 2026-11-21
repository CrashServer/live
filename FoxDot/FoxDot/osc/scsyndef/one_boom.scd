// one_boom: One's Boom (trap's 808) as a FoxDot synth. Ported from one/src/modules/trap-units/boom/dsp.ts.
//  - a sine with its 2nd and 3rd harmonics (body: 0.5, 0.25), from phase 0, one phase for all three; its pitch thrown
//    up by punch semitones and falling back exponentially (time constant ptime): freq * 2^(tune/12) * 2^(punch e/12)
//  - the click: One's seeded noise (rng(808)) × its 0.93-per-sample decay × 1.5, the 127 samples it lasts, exactly as
//    One's first note plays them (a Dseq), × click
//  - the tail: -60 dB over odecay while held, -60 dB over 60 ms after sus; silent (and freed) below -100 dB, as One's
//  - tanh(x amp velo dg) / tanh(min(3, dg)), dg = 1 + 14 odrive²; two one-poles at tone; One's DC follower (0.0004)
// The slide (glide) is between held notes of One's one voice: not here, a FoxDot note is a new 808 hit.
// Names as One's except decay→odecay (a FoxDot envelope keyword), drive→odrive, vol→level; velo this note's velocity.
SynthDef.new(\one_boom, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	tune = 0, odecay = 2, punch = 12, ptime = 0.04, body = 0.2, click = 0.15, odrive = 0.35, tone = 3000, velo = 0.8, level = -8, choke = -1, gl = 0, beat_dur = 0.5|
	var sig, sr, t, f, fr, ph, w, x, a, dg, la, lp, y;
	var chk, fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	sr = SampleRate.ir;
	t = Sweep.ar(0, 1);   // seconds since the note
	f = freq * (2 ** (tune / 12));
	fr = f * (2 ** (punch * exp(t.neg / ptime.max(0.003)) / 12));
	ph = (Phasor.ar(DC.ar(0), fr / sr) + (fr / sr)).frac;   // One adds the step before it reads the phase
	w = 2pi * ph;
	x = sin(w) + (body * ((0.5 * sin(2 * w)) + (0.25 * sin(3 * w))));
	x = x + (click * Duty.ar(SampleDur.ir, 0, Dseq([-1.35034,0.6212308,-0.552308,-0.6569519,0.4779165,0.4696542,-0.02835315,-0.8049356,0.1421909,-0.4167093,-0.3955938,0.1008677,-0.5614115,-0.3174776,0.3967523,-0.02177649,0.3149141,0.3554591,0.2924854,-0.1550314,0.2163763,0.1328797,-0.04429422,-0.01570016,0.01908244,0.1989526,0.1885993,0.09314946,0.1959381,-0.01357523,0.06579557,0.05886859,0.121169,0.03624359,-0.04089513,0.08714547,0.08348647,0.08657442,-0.05150451,0.08263409,0.004006825,-0.0726857,0.05907756,0.03793882,-0.05039601,-0.01618885,0.005797392,0.01312437,-0.007694254,0.001140865,0.01852499,0.0316914,-0.001290121,-0.02258072,-0.006345575,0.001091406,-0.01328955,0.0004839403,0.02036064,-0.01577999,0.01811259,-0.01083943,0.01534442,0.01056472,-0.00155893,-0.01054195,0.003364722,-0.00096521,-0.0001873613,0.001605833,-0.009142831,-0.005768203,0.004736937,-0.0008440267,-0.004968168,0.004739774,-0.004799395,0.004081041,0.003291051,0.002347064,0.0003987576,-0.0006760272,-0.001795899,-0.002601621,-0.0005240731,-0.0003878516,0.001728011,-0.002499491,0.001028056,0.002219777,-0.001125684,-0.001836051,-0.0003622291,-0.0007364652,-0.0004938168,-0.0002768454,-0.00006255544,0.0002175148,0.000432711,-0.0003437704,-0.0008558476,-0.0002247066,0.0005547777,0.0006310464,-0.000255399,-0.0000851249,0.0004687226,-0.00002775608,0.00004441241,-0.0003694018,0.0004164458,-0.00008237251,0.00006398523,-0.0003638743,-0.0002797281,0.0001693074,0.0001513534,0.00001773705,0.0002380876,0.00004773509,-0.0002082645,-0.00008099546,-0.00004900403,0.00003696451,-0.0001122752,-0.0001472897,-0.00005095775, 0], 1)));
	a = 0.001 ** ((t / odecay.max(0.05)) + ((t - sus).max(0) * ((1 / 0.06) - (1 / odecay.max(0.05)))));
	dg = 1 + (14 * odrive * odrive);
	x = (x * a * velo * dg).tanh / dg.min(3).tanh;
	la = exp(-2pi * tone.clip(60, sr * 0.45) / sr);
	lp = OnePole.ar(OnePole.ar(x, la), la);
	y = (lp - OnePole.ar(lp, 0.9996)) * (a >= 1e-5) * level.dbamp * amp;
	FreeSelf.kr(A2K.kr(a) < 1e-5);
	// One's routing, as one_sub's: dry to FoxDot's bus, the sends to the buses oneFX.py's effects run on.
	sig = Balance2.ar(y, y, pan, 2.sqrt);
	// one voice (choke >= 0, from the exporter): the next note of the same unit takes the voice over, this one fades
	// in 2 ms (its id on control bus 15400 + choke; choke < 0: plays as it is)
	chk = [Rand(1, 1000000), Sweep.kr(1, 1) < (ControlDur.ir * 1.5), Select.kr(choke >= 0, [15399, 15400 + choke.max(0)])];
	chk = chk ++ [In.kr(chk[2])];
	ReplaceOut.kr(chk[2], Select.kr(chk[1], [chk[3], chk[0]]));
	sig = sig * EnvGen.kr(Env.asr(0, 1, 0.002), (chk[1] + ((chk[3] - chk[0]).abs < 0.5) + (choke < 0)).min(1), doneAction: 2);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	// an insert (ins: its bus, from fx_insert): the dry sound goes there, FoxDot's bus keeps the inaudible tone
	Out.ar(ins.max(0), sig * dry * (ins >= 0));
	ReplaceOut.ar(bus, Select.ar((dry > 0) * (ins < 0), [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;

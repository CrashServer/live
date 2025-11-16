SynthDef.new(\prodrums,
	{|amp=1, sus=1, pan=0, freq=60, bus=0, voice=0, layer1_amp=1, layer2_amp=0.7, layer3_amp=0.5, layer_spread=0.05, low_gain=1, mid_gain=1, high_gain=1, low_sat=1, mid_sat=1, high_sat=1, crossover1=250, crossover2=2500, attack_shape=1, sustain_shape=1, transient_freq=3000, harmonic=0, fm_amount=0, fm_ratio=2, waveform=0, body_tone=200, decay=0.3, punch=1, texture=0, mod_rate=0, mod_depth=0|
		
		var sig, env, layers, layer1, layer2, layer3;
		var low_band, mid_band, high_band;
		var transient, body_sig;
		var multiband_out, final_sig;
		var pitch_env, amp_env, filt_env;

		// 0=kick, 1=snare, 2=hat, 3=perc, 4=bass
		freq = In.kr(bus, 1);

		// Amplitude envelope with transient shaping
		amp_env = EnvGen.ar(
			Env([0, attack_shape, sustain_shape * 0.7, sustain_shape * 0.3, 0],
				[0.001, 0.015, decay * 0.3, decay * 0.7],
				curve: [-4, -2, -4, -8]),
			doneAction: 2
		);

		// Pitch envelope (exponential for punch)
		pitch_env = EnvGen.ar(
			Env([4, 1.5, 1, 0.9],
				[0.002, 0.01, 0.05],
				curve: [4, -2, -1])
		);

		// Filter envelope
		filt_env = EnvGen.ar(
			Env([3, 1.5, 1],
				[0.01, decay * 0.5],
				curve: [-2, -4])
		);



		sig = Select.ar(voice.clip(0, 4), [

			// ========== VOICE 0: PROFESSIONAL KICK ==========
			{
				// LAYER 1: Sub punch (sine + FM)
				layer1 = {
					var sub_osc = SinOsc.ar(
						freq * pitch_env *
						(1 + (SinOsc.ar(freq * fm_ratio) * fm_amount * 0.3))
					);

					// Add harmonics via wavetable
					var harmonics = Select.ar(waveform.clip(0, 3), [
						SinOsc.ar(freq * pitch_env * 2) * harmonic * 0.3,
						Pulse.ar(freq * pitch_env * 2, 0.5) * harmonic * 0.3,
						LFTri.ar(freq * pitch_env * 2) * harmonic * 0.3,
						VarSaw.ar(freq * pitch_env * 2, width: 0.7) * harmonic * 0.3
					]);

					(sub_osc + harmonics) * layer1_amp;
				}.value;

				// LAYER 2: Body resonance (filtered pulse)
				layer2 = {
					var body = RLPF.ar(
						Impulse.ar(0) + (Pulse.ar(freq * 0.5, 0.3) * 0.2),
						body_tone * filt_env,
						0.3
					);
					body * layer2_amp * punch;
				}.value;

				// LAYER 3: Click/transient (shaped noise + sine burst)
				layer3 = {
					var click_env = EnvGen.ar(Env.perc(0.0001, 0.008));
					var click = Mix([
						HPF.ar(WhiteNoise.ar(), 2000) * click_env,
						SinOsc.ar(freq * 8) * click_env * 0.5
					]);
					var texture_noise = HPF.ar(PinkNoise.ar(), 800) *
						EnvGen.ar(Env.perc(0.001, 0.02)) * texture * 0.3;
					(click + texture_noise) * layer3_amp;
				}.value;

				// Mix layers with stereo spread
				Pan2.ar(layer1, 0) +
				Pan2.ar(layer2, layer_spread.neg) +
				Pan2.ar(layer3, layer_spread);
			}.value,

			// ========== VOICE 1: PROFESSIONAL SNARE ==========
			{
				// LAYER 1: Tonal body (FM synthesis for richness)
				layer1 = {
					var tone_freq = body_tone;
					var carrier = SinOsc.ar(tone_freq);
					var modulator = SinOsc.ar(tone_freq * fm_ratio);
					var fm_sig = SinOsc.ar(tone_freq + (modulator * tone_freq * fm_amount));

					// Add overtones
					var overtones = Mix([
						SinOsc.ar(tone_freq * 1.5) * 0.4,
						SinOsc.ar(tone_freq * 2.1) * 0.3 * harmonic
					]);

					(fm_sig + overtones) * layer1_amp;
				}.value;

				// LAYER 2: Snares (filtered noise with character)
				layer2 = {
					var snare_noise = HPF.ar(WhiteNoise.ar(), 1000);
					// Multiband noise for depth
					var low_noise = BPF.ar(snare_noise, 400, 0.8) * 0.4;
					var mid_noise = BPF.ar(snare_noise, 2000, 0.5) * 0.6;
					var high_noise = HPF.ar(snare_noise, 5000) * 0.5;
					Mix([low_noise, mid_noise, high_noise]) * layer2_amp;
				}.value;

				// LAYER 3: Snap transient
				layer3 = {
					var snap_env = EnvGen.ar(Env.perc(0.0001, 0.01));
					var snap = BPF.ar(WhiteNoise.ar(), transient_freq, 0.3) *
						snap_env * punch;
					snap * layer3_amp;
				}.value;

				Pan2.ar(layer1, layer_spread.neg) +
				Pan2.ar(layer2, 0) +
				Pan2.ar(layer3, layer_spread);
			}.value,

			// ========== VOICE 2: PROFESSIONAL HAT ==========
			{
				// LAYER 1: Metallic body (ring modulation + FM)
				layer1 = {
					var freq1 = body_tone;
					var freq2 = body_tone * 1.41; // Inharmonic
					var freq3 = body_tone * 1.87;

					var ring1 = SinOsc.ar(freq1) * SinOsc.ar(freq2);
					var ring2 = SinOsc.ar(freq2) * SinOsc.ar(freq3);
					var ring3 = SinOsc.ar(freq1 * 0.7) * SinOsc.ar(freq3 * 1.3);

					Mix([ring1, ring2, ring3 * harmonic]) * 0.4 * layer1_amp;
				}.value;

				// LAYER 2: Noise layers (multiband for depth)
				layer2 = {
					var noise = WhiteNoise.ar();
					var low_band = BPF.ar(noise, 6000, 0.5) * 0.4;
					var mid_band = BPF.ar(noise, 9000, 0.4) * 0.6;
					var high_band = HPF.ar(noise, 12000) * 0.5;
					Mix([low_band, mid_band, high_band]) * layer2_amp;
				}.value;

				// LAYER 3: FM sparkle
				layer3 = {
					var carrier = SinOsc.ar(body_tone * 2);
					var modulator = SinOsc.ar(body_tone * 3.7);
					var fm = SinOsc.ar(body_tone * 2 + (modulator * 500 * fm_amount));
					fm * 0.3 * layer3_amp * harmonic;
				}.value;

				Pan2.ar(HPF.ar(layer1 + layer2 + layer3, 4000), 0);
			}.value,

			// ========== VOICE 3: PROFESSIONAL PERC ==========
			{
				// LAYER 1: Fundamental (wavetable osc)
				layer1 = {
					var base_sig = Select.ar(waveform.clip(0, 3), [
						SinOsc.ar(body_tone * filt_env),
						Pulse.ar(body_tone * filt_env, 0.5),
						LFTri.ar(body_tone * filt_env),
						VarSaw.ar(body_tone * filt_env, width: 0.7)
					]);
					base_sig * layer1_amp;
				}.value;

				// LAYER 2: FM texture
				layer2 = {
					var carrier = SinOsc.ar(body_tone * filt_env);
					var modulator = SinOsc.ar(body_tone * fm_ratio * filt_env);
					var fm_sig = SinOsc.ar(
						body_tone * filt_env +
						(modulator * body_tone * fm_amount)
					);
					fm_sig * 0.6 * layer2_amp;
				}.value;

				// LAYER 3: Attack definition
				layer3 = {
					var attack_env = EnvGen.ar(Env.perc(0.0001, 0.015));
					var attack = BPF.ar(WhiteNoise.ar(), body_tone * 3, 0.5) *
						attack_env * punch;
					attack * layer3_amp * texture;
				}.value;

				Pan2.ar(layer1, layer_spread.neg) +
				Pan2.ar(layer2, 0) +
				Pan2.ar(layer3, layer_spread);
			}.value,

			// ========== VOICE 4: PROFESSIONAL BASS ==========
			{
				// LAYER 1: Sub (sine + sub-harmonic)
				layer1 = {
					var sub = SinOsc.ar(freq * 0.5);
					var sub_harm = SinOsc.ar(freq * 0.25) * harmonic * 0.6;
					(sub + sub_harm) * layer1_amp;
				}.value;

				// LAYER 2: Body (wavetable + FM)
				layer2 = {
					var wave_osc = Select.ar(waveform.clip(0, 3), [
						Pulse.ar(freq * 0.5, 0.5),
						VarSaw.ar(freq * 0.5, width: 0.7),
						LFTri.ar(freq * 0.5),
						SinOsc.ar(freq * 0.5) + (Pulse.ar(freq * 0.5, 0.3) * 0.5)
					]);

					// FM for harmonic richness
					var fm_osc = SinOsc.ar(
						freq * 0.5 + (SinOsc.ar(freq * fm_ratio * 0.5) * freq * fm_amount)
					);

					var mixed = (wave_osc * 0.6) + (fm_osc * 0.4 * harmonic);

					// Resonant filter
					var filtered = RLPF.ar(mixed,
						(body_tone * filt_env).clip(50, 5000),
						0.4
					);

					filtered * layer2_amp;
				}.value;

				// LAYER 3: Harmonics and grit
				layer3 = {
					var harm_sig = Mix([
						SinOsc.ar(freq * 1) * 0.3,
						SinOsc.ar(freq * 2) * 0.2 * harmonic,
						SinOsc.ar(freq * 3) * 0.15 * harmonic
					]);

					// Add texture
					var grit = HPF.ar(PinkNoise.ar(), 500) *
						EnvGen.ar(Env.adsr(0.01, 0.1, 0.3, 0.2)) *
						texture * 0.2;

					(harm_sig + grit) * layer3_amp;
				}.value;

				Pan2.ar(layer1, 0) +
				Pan2.ar(layer2, layer_spread.neg) +
				Pan2.ar(layer3, layer_spread);
			}.value
		]);

		// Apply amplitude envelope
		sig = sig * amp_env;

		// ============================================================
		// MULTIBAND PROCESSING (Professional depth)
		// ============================================================

		// Split into 3 bands
		low_band = LPF.ar(sig, crossover1);
		mid_band = HPF.ar(LPF.ar(sig, crossover2), crossover1);
		high_band = HPF.ar(sig, crossover2);

		// Independent saturation per band
		low_band = (low_band * low_sat * 1.5).tanh * low_gain;
		mid_band = (mid_band * mid_sat * 1.3).tanh * mid_gain;
		high_band = (high_band * high_sat * 1.2).tanh * high_gain;

		// Recombine with phase-coherent crossovers
		multiband_out = low_band + mid_band + high_band;

		// ============================================================
		// TRANSIENT SHAPING (Attack/Sustain enhancement)
		// ============================================================

		// Split transient and body
		transient = HPF.ar(multiband_out, transient_freq) *
			EnvGen.ar(Env.perc(0.0001, 0.02)) * attack_shape;

		body_sig = LPF.ar(multiband_out, transient_freq) * sustain_shape;

		// Recombine
		final_sig = transient + body_sig;

		// ============================================================
		// FINAL PROCESSING
		// ============================================================

		// Subtle modulation
		final_sig = final_sig * (1 + (SinOsc.kr(mod_rate) * mod_depth * 0.1));

		// Professional limiting (transparent)
		final_sig = Compander.ar(final_sig, final_sig,
			thresh: 0.7,
			slopeBelow: 1,
			slopeAbove: 0.5,
			clampTime: 0.001,
			relaxTime: 0.05
		);

		// Final saturation (glue)
		final_sig = (final_sig * 1.1).tanh * 0.95;

		// Output
		final_sig = final_sig * amp;
		final_sig = Balance2.ar(final_sig[0], final_sig[1], pan);

		ReplaceOut.ar(bus, final_sig);
	}
).add;

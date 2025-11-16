SynthDef.new(\choir,
{|bus=0, amp=1, atk=0.001, decay=0.01, sus=1, rel=0.01, level=0.8, peak=1, gate=1, pan=0, freq=0, fmod=0, vib=0, rate=1, blur=1, bendc=0.0, vow=0.0|
var vibs, mods, gens, formantsFemale, formantsMale, vowelsFemale, vowelsMale, vowelMix, panPositions, out, env, noise;

    sus = sus * blur;
    freq = In.kr(bus, 1);
    freq = [freq, freq + fmod];

    // Génération des vibratos
    vibs = Array.fill(8, { |i|
        SinOsc.ar(
            5 + (i * 0.15),
            0,
            EnvGen.kr(Env([0, (i % 2 == 0).if(2, 1)], [(i + 2) * 0.1], 4), 1)
        )
    });

    // Modulateurs
    mods = SinOsc.ar(
        [0.1, -0.23, 0.34, -0.44, 0.5, -0.6, 0.73, -0.81],
        mul: 1
    );

    // Générateurs de base
    gens = LFPulse.ar(
        freq * bendc.midiratio + mods + vibs,
        0,
        0.4 * mods.reverse / 8 + 0.2,
        0.15
    );

    // Formants femmes [ah, eh, ih, oh, uh]
    formantsFemale = [
        [751, 1460, 2841],  // ah
        [431, 2241, 2871],  // eh
        [329, 2316, 2796],  // ih
        [438, 953, 2835],   // oh
        [350, 1048, 2760]   // uh
    ];

    // Formants hommes [ah, eh, ih, oh, uh]
    formantsMale = [
        [608, 1309, 2466],  // ah
        [372, 1879, 2486],  // eh
        [290, 1986, 2493],  // ih
        [380, 907, 2415],   // oh
        [309, 961, 2366]    // uh
    ];

    // Calcul des voyelles pour voix féminines (gen 0-3)
    vowelsFemale = formantsFemale.collect({ |freqSet|
        Mix.fill(4, { |i|
            var gen = gens[i];
            Mix(freqSet.collect({ |f| BBandPass.ar(gen, f, 0.075) }))
        })
    });

    // Calcul des voyelles pour voix masculines (gen 4-7)
    vowelsMale = formantsMale.collect({ |freqSet|
        Mix.fill(4, { |i|
            var gen = gens[i + 4];
            Mix(freqSet.collect({ |f| BBandPass.ar(gen, f, 0.075) }))
        })
    });

    // Combinaison des voix féminines et masculines
    vowelMix = (vowelsFemale + vowelsMale).collect({ |v| v });

    // Sélection de voyelle
    vowelMix = LinSelectX.ar(vow, vowelMix, 0);

    // Ajout de bruit
    noise = Pulse.ar(220) * GrayNoise.ar(0.005);
	vowelMix = vowelMix + noise;

    // Panoramique distribué
    panPositions = [-1, -0.8, -0.6, -0.4, 0.4, 0.6, 0.8, 1];
    out = Mix(panPositions.collect({ |pos|
        Pan2.ar(vowelMix, pos, 0.5)
    }));

	// Enveloppe
    env = EnvGen.ar(Env.asr(2, 1, 0.005), gate, doneAction: 2);

    ReplaceOut.ar(bus, out * amp * 0.5 * env);
}).add;
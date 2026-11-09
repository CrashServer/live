SynthDef.new(\bowed,
{|bus=0, freq=0, amp=1, sus=1, pan=0, fmod=0, atk=0.15, rel=0.4,
  force=1, bowspeed=0.5, bowpos=0.1, vib=1, body=1, bright=6000|
    // Bowed string, physical model (sc3-plugins DWGBowedTor + soundboard).
    // force = bow pressure: low is airy/flautando, high is scratchy.
    // The attack ramps the *pressure*, not the level - a bow digging in.
    // bowpos (0..0.5) = where the bow sits: near the bridge is thin and bright.
    // After soundDesign's bowed archetype; chain after the DWGBowedTor help file.
    var gate, press, vibrato, son, end;
    freq = In.kr(bus, 1);
    freq = freq + fmod;

    gate = Trig1.kr(1, sus.max(0.05));                     // bow on for sus, then lifts
    press = force * EnvGen.kr(Env([0.35, 1, 1], [atk.max(0.01), sus], [2, 0]));
    vibrato = Gendy1.kr(1, 1, 1, 1, 0.1, 4, mul: 0.003 * vib, add: 1);

    son = DWGBowedTor.ar(freq * vibrato, bowspeed, press, gate, bowpos.clip(0.02, 0.5), rel.max(0.05), 0.25, 31);
    son = DWGSoundBoard.ar(son);
    son = son + (body * (BPF.ar(son, 118, 1) + BPF.ar(son, 430, 1) + BPF.ar(son, 490, 1)));
    son = LPF.ar(son, bright.clip(500, 18000));
    son = LeakDC.ar(son) * amp * 0.035;   // calibrated: peaks -17..-5 dBFS (C3..C5, force, bowpos), near pianovel

    end = Line.kr(0, 0, sus + rel + 0.3, doneAction: 2);    // frees once the string has rung out
    ReplaceOut.ar(bus, Pan2.ar(son, pan))},
    metadata: (
        credit: "CrashServer (after soundDesign bowed archetype; DWGBowedTor help)",
        description: "Bowed string physical model: force = pressure, bowpos = position, attack ramps pressure",
        category: \strings,
        tags: [\bowed, \string, \physical, \cello, \violin]
    )
).add;

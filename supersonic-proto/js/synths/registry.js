// Synth registry — add new synths here after compiling their .scd source.
//
// Each entry:
//   scName:      compiled SynthDef name (must match filename in synthdefs/compiled/)
//   defaults:    default param values (also drives autocomplete)
//   extraParams: extra SC params beyond the common base (note, amp, sus, pan, attack, release, out)
//
// To add a synth:
//   1. Create synthdefs/src/synths/mysynth.scd
//   2. Add an entry here
//   3. Run scripts/build.sh

export const SYNTH_DEFS = {
    dbass: {
        scName: 'fd_dbass',
        defaults: { oct: 3, amp: 0.9, dur: 1, pan: 0, attack: 0.02, release: 0.12, cutoff: 2000, rq: 0.5, phase: 0.9 },
        extraParams: ['cutoff', 'rq', 'phase'],
    },
    saw: {
        scName: 'fd_saw',
        defaults: { oct: 4, amp: 0.7, dur: 1, pan: 0, attack: 0.01, release: 0.1, cutoff: 8000, rq: 0.8, rate: 0.5 },
        extraParams: ['cutoff', 'rq', 'rate'],
    },
    sine: {
        scName: 'fd_sine',
        defaults: { oct: 4, amp: 0.7, dur: 1, pan: 0, attack: 0.001, release: 0.05, cutoff: 2800, rq: 0.8, rate: 0.1 },
        extraParams: ['cutoff', 'rq', 'rate'],
    },
    rsin: {
        scName: 'fd_rsin',
        defaults: { oct: 4, amp: 0.7, dur: 1, pan: 0, attack: 0.01, release: 0.2, cutoff: 2000, rq: 0.1, feedback: 0 },
        extraParams: ['cutoff', 'rq', 'feedback'],
    },
    donk: {
        scName: 'fd_donk',
        defaults: { oct: 3, amp: 0.9, dur: 0.5, pan: 0 },
        extraParams: [],
        rawSus: true,  // sus = Ringz decay in seconds — pass dur*secPerBeat directly, no atk/rel subtraction
    },
};

export class SynthCall {
    constructor(name, args) { this.name = name; this.args = args; }
}

// Generic param builder — works for any entry in SYNTH_DEFS.
// outBus: player's private audio bus (0 = direct to output, no FX)
export function buildParams(synthName, midi, r, secPerBeat, outBus = 0) {
    const def = SYNTH_DEFS[synthName];
    if (!def) return null;
    const sus   = r.sus ?? r.dur ?? 1;
    const atkS  = r.attack  ?? def.defaults.attack  ?? 0.01;
    const relS  = r.release ?? Math.min(0.3, sus * secPerBeat * 0.3);

    let base;
    if (def.rawSus) {
        // Synths like donk use sus as raw decay seconds (no atk/rel envelope subtraction)
        base = [
            'out', outBus, 'note', midi,
            'amp', Math.min(1.5, r.amp ?? def.defaults.amp ?? 0.8),
            'pan', r.pan ?? 0,
            'sus', Math.max(0.001, sus * secPerBeat),
        ];
    } else {
        // SynthDefs expect sus = total duration in seconds; they subtract attack+release internally
        const susS = Math.max(atkS + relS + 0.001, sus * secPerBeat);
        base = [
            'out',     outBus,
            'note',    midi,
            'amp',     Math.min(1.5, r.amp ?? def.defaults.amp ?? 0.8),
            'pan',     r.pan  ?? 0,
            'attack',  atkS,
            'sus',     susS,
            'release', relS,
        ];
    }
    const extras = (def.extraParams ?? []).flatMap(p => [p, r[p] ?? def.defaults[p] ?? 0]);
    return { scName: def.scName, params: [...base, ...extras] };
}

// Factory: returns a callable synth function (for use in eval context)
export function makeSynth(name) {
    return function(degree, opts = {}) {
        // Support makeSynth('dbass')([0,2], {oct:3}) or makeSynth('dbass')({degree:[0,2], oct:3})
        if (degree !== null && typeof degree === 'object'
                && !Array.isArray(degree)
                && typeof degree.get !== 'function') {
            opts = degree;
            degree = opts.degree ?? 0;
        }
        const def = SYNTH_DEFS[name];
        return new SynthCall(name, { ...(def?.defaults ?? {}), degree, ...opts });
    };
}

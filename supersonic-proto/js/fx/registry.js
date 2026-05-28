// FX registry — maps user-facing FoxDot-style param names to SC SynthDef params.
//
// To add a new FX:
//   1. Add its section to synthdefs/src/fx/fx_chain.scd
//   2. Add param entries here
//   3. Run scripts/build.sh, reload browser
//
// Keys listed here are treated as FX params in player >> calls
// and are NOT forwarded to the player synth.

export const FX_REGISTRY = {
    // Low-pass filter — lpf = cutoff Hz (0 = off)
    lpf:       { scParam: 'lpf',     default: 0,   desc: 'LPF cutoff Hz (0=off, e.g. 2000)' },
    lpf_rq:    { scParam: 'lpf_rq',  default: 0.7, desc: 'LPF resonance (0.01=sharp, 1=flat)' },

    // High-pass filter — hpf = cutoff Hz (0 = off)
    hpf:       { scParam: 'hpf',     default: 0,   desc: 'HPF cutoff Hz (0=off, e.g. 400)' },
    hpf_rq:    { scParam: 'hpf_rq',  default: 0.7, desc: 'HPF resonance' },

    // Reverb
    reverb:    { scParam: 'reverb',   default: 0,    desc: 'Reverb mix' },
    room:      { scParam: 'rev_room', default: 0.6,  desc: 'Room size' },
    damp:      { scParam: 'rev_damp', default: 0.5,  desc: 'High-freq damping' },

    // Tanh saturation / distortion
    tanh:      { scParam: 'tanh',      default: 0,   desc: 'Soft clip mix' },
    drive:     { scParam: 'tanh_drive',default: 2,   desc: 'Drive amount' },

    // Echo (CombL)
    echo:      { scParam: 'echo',      default: 0,   desc: 'Echo mix' },
    echo_time: { scParam: 'echo_time', default: 0.25,desc: 'Echo delay in seconds' },
    echo_dec:  { scParam: 'echo_dec',  default: 0.5, desc: 'Echo decay/feedback' },
};

export const FX_KEYS = new Set(Object.keys(FX_REGISTRY));

// Build SC param list from resolved user FX args
export function buildFxParams(r) {
    const params = [];
    for (const [key, val] of Object.entries(r)) {
        const reg = FX_REGISTRY[key];
        if (reg) params.push(reg.scParam, val);
    }
    return params;
}

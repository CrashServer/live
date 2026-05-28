// fd_fx_chain — per-player FX processor
//
// One running instance per active player. Reads from that player's private
// audio bus, applies effects in order, writes to main output (bus 0).
//
// ── How to add a new effect ─────────────────────────────────────────────
//  1. Add its params to the |arg list| with defaults
//  2. Add a section below (compute wet, XFade2 with mix * 2 - 1)
//  3. Add the param mapping to js/fx/registry.js
//  4. Run scripts/build.sh, reload browser
//
// ── XFade2 mix convention ────────────────────────────────────────────────
//  XFade2.ar(dry, wet, mix * 2 - 1)
//    mix=0  → -1 → all dry (effect off)
//    mix=0.5 →  0 → 50/50
//    mix=1  → +1 → all wet
//
// After editing: run   scripts/build.sh

SynthDef(\fd_fx_chain, {
    |out=0, in_bus=64,
     lpf=0, lpf_rq=0.7,
     hpf=0, hpf_rq=0.7,
     reverb=0, rev_room=0.6, rev_damp=0.5,
     tanh=0, tanh_drive=2,
     echo=0, echo_time=0.25, echo_dec=0.5|

    var sig, wet;
    sig = In.ar(in_bus, 2);

    // ── Low-pass filter — lpf = cutoff Hz (0 = bypass) ──────────────────
    wet = RLPF.ar(sig, (lpf > 0).if(lpf.clip(20, 20000), 20000), lpf_rq.clip(0.01, 1.0));
    sig = XFade2.ar(sig, wet, (lpf > 0) * 2 - 1);

    // ── High-pass filter — hpf = cutoff Hz (0 = bypass) ─────────────────
    wet = RHPF.ar(sig, (hpf > 0).if(hpf.clip(20, 20000), 20), hpf_rq.clip(0.01, 1.0));
    sig = XFade2.ar(sig, wet, (hpf > 0) * 2 - 1);

    // ── Tanh saturation ──────────────────────────────────────────────────
    wet = (sig * tanh_drive.clip(0.001, 100)).tanh;
    sig = XFade2.ar(sig, wet, tanh * 2 - 1);

    // ── Reverb (Schroeder allpass — avoids FreeVerb2 plugin dependency) ─────
    wet = sig;
    wet = AllpassN.ar(wet, 0.05, [0.047, 0.051], 0.5 + rev_room * 3);
    wet = AllpassN.ar(wet, 0.1,  [0.061, 0.068], 0.5 + rev_room * 2);
    wet = AllpassN.ar(wet, 0.1,  [0.031, 0.037], 0.5 + rev_room * 2);
    wet = wet * (1 - rev_damp * 0.6);
    sig = XFade2.ar(sig, wet, reverb * 2 - 1);

    // ── Echo (CombL delay) ────────────────────────────────────────────────
    wet = sig + CombL.ar(sig, 2.0, echo_time.clip(0.001, 2.0), echo_dec.clip(0, 8));
    sig = XFade2.ar(sig, wet, echo * 2 - 1);

    Out.ar(out, sig);
}).writeDefFile(~outDir);
"fd_fx_chain done".postln;

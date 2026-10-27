# SuperCollider Web: Feasibility Study

## Overview

This document analyzes the feasibility of creating a fully web-based version of FoxDot with SuperCollider-quality audio synthesis.

---

## Current Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Current FoxDot Stack                     │
├─────────────────────────────────────────────────────────────┤
│  Python (FoxDot)     │     SuperCollider (scsynth)         │
│  - Pattern engine    │     - Real-time DSP engine          │
│  - Clock/scheduling  │     - 500+ UGens                    │
│  - OSC commands      │     - SynthDefs                     │
│         │                         ▲                        │
│         └────── OSC (UDP) ────────┘                        │
├─────────────────────────────────────────────────────────────┤
│                    WebTroop (Browser)                       │
│  - Code editor       - Crash panel                         │
│  - Collaboration     - Visual mode                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Option A: Compile scsynth to WebAssembly

### Pipeline

```
SuperCollider Source (C++)
         │
         ▼
┌─────────────────────────────────┐
│     Emscripten (emcc)           │
│  C++ → LLVM IR → WebAssembly    │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│  scsynth.wasm + scsynth.js      │
│  (~2-5MB compressed)            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│    Browser AudioWorklet         │
│  (Real-time audio thread)       │
└─────────────────────────────────┘
```

### Technical Challenges

| Challenge | Native | Browser Solution |
|-----------|--------|------------------|
| Audio threading | pthreads, RT priority | AudioWorklet + SharedArrayBuffer |
| Memory model | Direct access | WASM linear memory, pre-allocate |
| File I/O | POSIX filesystem | Emscripten virtual FS |
| OSC input | UDP sockets | Direct WASM function calls |
| Plugin loading | dlopen() | Static linking all UGens |
| Timing | gettimeofday | performance.now() |

### Required Source Modifications

1. **Audio driver**: Replace PortAudio/JACK with AudioWorklet callback
2. **Threading**: Single-threaded or WASM threads
3. **OSC**: Direct memory/function calls instead of UDP
4. **Plugins**: Static compile all needed UGens

### Estimated Timeline

- Phase 1 (Proof of Concept): 1-2 months
- Phase 2 (Core Engine): 2-3 months
- Phase 3 (Full Engine): 3-4 months
- Phase 4 (Integration): 1-2 months
- **Total: 7-11 months**

### Pros/Cons

**Pros:**
- Identical sound (same DSP code)
- All UGens available
- SynthDef compatible

**Cons:**
- Massive engineering effort
- Browser audio limitations remain
- Large WASM binary (~5MB)

---

## Option B: Transpile SynthDefs to WebAudio

### Concept

```
SynthDef(\bass, { |freq|
    Out.ar(0, SinOsc.ar(freq) * EnvGen.kr(Env.perc))
})

         │ Transpiler
         ▼

const bass = (ctx, freq) => {
    const osc = new OscillatorNode(ctx, {frequency: freq});
    const gain = new GainNode(ctx);
    // ... envelope logic
    return {osc, gain};
}
```

### UGen Mapping Feasibility

| SC UGen | WebAudio Equivalent | Similarity |
|---------|---------------------|------------|
| SinOsc, Saw, Pulse | OscillatorNode | 95% |
| LFNoise0/1/2 | AudioWorklet custom | 85% |
| RLPF, LPF, HPF | BiquadFilterNode | 70% |
| EnvGen | Custom JS + GainNode | 85% |
| FreeVerb | ConvolverNode or custom | 60% |
| PlayBuf | AudioBufferSourceNode | 90% |
| CombN, AllpassN | DelayNode + feedback | 75% |
| GrainBuf | Custom AudioWorklet | 40% |

### Estimated Timeline

- Core transpiler: 2-3 months
- Essential UGens: 2-3 months
- Testing/refinement: 1-2 months
- **Total: 5-8 months**

---

## Option C: Native WebAudio Synths

### Approach

Rewrite synths from scratch using:
- Web Audio API
- Tone.js (higher-level library)
- Custom AudioWorklets for complex DSP

### Timeline by Synth Count

| Synths | Effort | Timeline |
|--------|--------|----------|
| 10 basic | Low | 1 month |
| 20 core | Medium | 2-3 months |
| 40 full | High | 4-6 months |

---

## Realistic Assessment

### Sound Similarity by Approach

| Approach | Similarity | Effort |
|----------|------------|--------|
| scsynth WASM | 98% | 10-14 months |
| Transpiler | 75-85% | 5-8 months |
| WebAudio rewrite | 60-70% | 3-4 months |

### What Will NOT Be Identical (Any Approach)

1. **Latency**: Browser 20-50ms vs SC <10ms
2. **Filter character**: Different implementations
3. **Real-time stability**: Browser can glitch
4. **Sample rate**: Less control

### Recommendation

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Start with WebAudio rewrite ("Good Enough")               │
│                                                             │
│   → Get something working in 3-4 months                     │
│   → Real users can test it                                  │
│   → Identify which synths NEED to sound closer              │
│   → Incrementally improve specific ones                     │
│   → Consider WASM only if truly necessary                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### Easy to Port (JS)

- Pattern engine (P, PRand, PWhite, etc.)
- Clock and scheduling
- Player management
- OSC encoding
- All of WebTroop

### Medium Difficulty

- Basic synths (bass, pluck, keys)
- Simple effects (reverb, delay)
- Sample playback
- Envelopes

### Hard / May Differ

- Complex filters (Moog-style)
- Granular synthesis
- Physical modeling
- Custom UGens

---

## Existing References

| Project | Description | Status |
|---------|-------------|--------|
| Strudel | Tidal Cycles in browser | Production |
| Gibber | Live coding in browser | Production |
| Tone.js | WebAudio framework | Production |
| Csound WASM | Csound compiled to WASM | Working |
| Faust WASM | DSP language to WASM | Production |

---

## Conclusion

A web-based FoxDot is **feasible** with these tradeoffs:

- **4-6 months** for a functional version
- **60-70% sound similarity** with WebAudio approach
- **All pattern features** can be preserved
- **Some synths** will sound different
- **Latency** will be higher

The question is not "can we do it?" but "how close do we need to get?"

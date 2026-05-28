// Player — one per named variable (p1, p2, ...).
// Handles note scheduling, FX chain management, and player methods.

import { buildParams, SynthCall } from '../synths/registry.js';
import { FX_KEYS }               from '../fx/registry.js';
import { FXChain }               from '../fx/chain.js';
import { patGet }                 from '../patterns/sequences.js';
import { toMidi }                 from './scale.js';
import { PlayStringCall, parsePattern, charToBufId } from './sampler.js';

// SC group node IDs — use low IDs (below client allocator range ~1000)
export const PLAYER_GROUP = 2;
export const FX_GROUP     = 3;

// Private bus allocation (stereo, 2 channels each)
const FIRST_BUS = 64;
const STRIDE    = 2;
let   _nextSlot = 0;
function allocBus() { return FIRST_BUS + _nextSlot++ * STRIDE; }

// SuperSonic instance reference — set after boot
let _sc = null;
export function setSuperSonic(sc) { _sc = sc; }

// Resolve all pattern args at the current step
function resolveArgs(args, step) {
    const out = {};
    for (const [k, v] of Object.entries(args)) out[k] = patGet(v, step, v);
    return out;
}

// Split resolved args into synth params vs FX params
function splitArgs(r) {
    const synth = {}, fx = {};
    for (const [k, v] of Object.entries(r)) {
        (FX_KEYS.has(k) ? fx : synth)[k] = v;
    }
    return { synth, fx };
}

// Restore all players' amplitude (undo a solo)
export function unsolo(clock) {
    clock._players.forEach(p => { p._amplify = 1; });
}

// ── drop() — silence a random subset of players, restore after playTime beats
// drop(clock, playTime=14, dropTime=2, nbloop=1)
export function drop(clock, playTime = 14, dropTime = 2, nbloop = 1) {
    const allPlayers = [...clock._players.values()].filter(p => p._active);
    const n = allPlayers.length;
    if (n === 0) return;

    for (let loop = 0; loop < nbloop; loop++) {
        const loopOffset = loop * (playTime + dropTime);
        // Pick a random non-empty subset to silence
        const subsetSize = nbloop === 1
            ? Math.floor(Math.random() * n) + 1
            : Math.max(1, Math.floor(Math.random() * n));
        const shuffled = [...allPlayers].sort(() => Math.random() - 0.5);
        const toSilence = shuffled.slice(0, subsetSize);

        const secPerBeat = 60 / clock.bpm;

        setTimeout(() => {
            for (const p of toSilence) p._amplify = 0;
        }, loopOffset * secPerBeat * 1000);

        setTimeout(() => {
            for (const p of toSilence) p._amplify = 1;
        }, (loopOffset + playTime) * secPerBeat * 1000);
    }
}

export class Player {
    constructor(name, clock) {
        this.name      = name;
        this._clock    = clock;
        this._active   = false;
        this._step     = 0;
        this._nextBeat = 0;
        this._synth    = null;
        this._args     = {};
        this._bus      = allocBus();
        this._fxChain  = null;
        this._every    = [];
        this._amplify  = 1;
        // sample-mode state
        this._mode     = 'synth';   // 'synth' | 'sample'
        this._pattern  = null;      // parsed steps array
        this._playOpts = {};
    }

    // p1 >> dbass([0,2,4], ...) OR b1 >> play("X  o X  o", ...)
    __rshift__(synthCall) {
        if (synthCall === null || synthCall === undefined) { this.stop(); return this; }

        if (synthCall instanceof PlayStringCall) {
            this._mode     = 'sample';
            this._pattern  = parsePattern(synthCall.pattern);
            this._playOpts = { ...synthCall.opts };
            if (!this._active) {
                this._active   = true;
                this._step     = 0;
                const now      = this._clock.now();
                this._nextBeat = Math.ceil(now + 0.001);
                this._clock._schedule(this._nextBeat, () => this._fire());
            }
            return this;
        }

        if (!(synthCall instanceof SynthCall)) {
            console.error(`${this.name} >>: expected synth call or play(), got`, synthCall);
            return this;
        }
        const wasActive = this._active;
        this._mode  = 'synth';
        this._synth = synthCall.name;
        this._args  = { ...synthCall.args };

        if (!wasActive) {
            this._active   = true;
            this._step     = 0;
            this._fxChain  = this._fxChain ?? (_sc ? new FXChain(this._bus, FX_GROUP, _sc) : null);
            const now      = this._clock.now();
            this._nextBeat = Math.ceil(now + 0.001);
            this._clock._schedule(this._nextBeat, () => this._fire());
        }
        return this;
    }

    _fire() {
        if (!this._active) return;
        if (this._mode === 'sample') { this._fireSample(); return; }

        const step = this._step;
        const r    = resolveArgs(this._args, step);
        const { synth: sArgs, fx: fxArgs } = splitArgs(r);
        const dur  = Math.max(0.0625, r.dur ?? 1);
        const oct  = r.oct ?? 5;
        const deg  = r.degree ?? 0;
        const amp  = r.amp ?? 0.8;

        // Lazy FX chain init (if boot happened after first >> call)
        if (!this._fxChain && _sc) {
            this._fxChain = new FXChain(this._bus, FX_GROUP, _sc);
        }

        // Update FX params every step (handles TimeVars on FX params)
        if (this._fxChain && Object.keys(fxArgs).length > 0) {
            this._fxChain.update(fxArgs, _sc);
        }

        // Trigger note(s)
        const degrees  = Array.isArray(deg) ? deg : [deg];
        const ampEach  = (amp * this._amplify) / Math.max(1, degrees.length);
        for (const d of degrees) {
            if (d === null) continue;
            const midi = toMidi(d, oct);
            if (midi === null || midi < 0 || midi > 127) continue;
            this._trigger(midi, { ...sArgs, amp: ampEach });
        }

        // Tick .every() handlers
        for (const h of this._every) {
            if (this._nextBeat >= h.nextBeat) {
                h.fn(this);
                h.nextBeat += h.beats;
            }
        }

        this._step++;
        this._nextBeat += dur;
        this._clock._schedule(this._nextBeat, () => this._fire());
    }

    _fireSample() {
        if (!_sc || !this._pattern?.length) return;
        const opts     = this._playOpts;
        const step     = this._step;
        const baseDur  = Math.max(0.0625, patGet(opts.dur ?? 0.5, step, 0.5));
        const amp      = patGet(opts.amp ?? 0.8, step, 0.8) * this._amplify;
        const pan      = patGet(opts.pan ?? 0, step, 0);
        const rate     = patGet(opts.rate ?? 1, step, 1);
        const sampleIdx = Math.round(patGet(opts.sample ?? 0, step, 0));

        const pat  = this._pattern;
        const entry = pat[((step % pat.length) + pat.length) % pat.length];

        if (entry !== null) {
            if (entry.sub) {
                // Subdivided: fire each in sequence at dur/N, queue them individually
                const n    = entry.sub.length;
                const subD = baseDur / n;
                entry.sub.forEach((ch, i) => {
                    const beatOffset = i * subD;
                    setTimeout(() => {
                        const bufId = charToBufId(ch, sampleIdx);
                        if (bufId !== null) this._triggerSample(bufId, amp, pan, rate);
                    }, beatOffset * 60000 / this._clock.bpm);
                });
            } else {
                // Simultaneous (chars array, usually just 1)
                for (const ch of entry.chars) {
                    const bufId = charToBufId(ch, sampleIdx);
                    if (bufId !== null) this._triggerSample(bufId, amp, pan, rate);
                }
            }
        }

        this._step++;
        this._nextBeat += baseDur;
        this._clock._schedule(this._nextBeat, () => this._fire());
    }

    _triggerSample(bufId, amp, pan, rate) {
        if (!_sc) return;
        const id = _sc.nextNodeId();
        _sc.send('/s_new', 'fd_sampler', id, 0, PLAYER_GROUP,
            'buf', bufId, 'amp', amp, 'pan', pan, 'rate', rate);
    }

    _trigger(midi, r) {
        if (!_sc) return;
        const secPerBeat = 60 / this._clock.bpm;
        const result     = buildParams(this._synth, midi, r, secPerBeat, this._bus);
        if (!result) { console.error(`Unknown synth: ${this._synth}`); return; }

        const id = _sc.nextNodeId();
        _sc.send('/s_new', result.scName, id, 0, PLAYER_GROUP, ...result.params);

        // Auto-free after envelope completes
        const sus  = r.sus ?? r.dur ?? 1;
        const relS = r.release ?? Math.min(0.5, sus * secPerBeat * 0.3);
        setTimeout(() => { try { _sc.send('/n_free', id); } catch (_) {} },
            (sus * secPerBeat + relS + 0.3) * 1000);
    }

    // ── Player methods ──────────────────────────────────────────────────────

    stop() {
        this._active = false;
        this._every  = [];
        if (this._fxChain && _sc) {
            this._fxChain.free(_sc);
            this._fxChain = null;
        }
    }

    // Mute all other players (keeps them running so unsolo can restore them)
    solo() {
        this._clock._players.forEach((p, k) => {
            if (k !== this.name) p._amplify = 0;
        });
        return this;
    }

    // Solo for N beats then restore all
    soloDrop(beats = 8) {
        this.solo();
        const ms = beats * (60000 / this._clock.bpm);
        setTimeout(() => {
            this._clock._players.forEach(p => { p._amplify = 1; });
        }, ms);
        return this;
    }

    // every(beats, fn) — call fn(player) every n beats
    // fn can be a string method name: 'stutter', 'reverse', 'shuffle'
    every(beats, fn, ...args) {
        const method = typeof fn === 'string' ? (p) => p[fn]?.(...args) : fn;
        this._every.push({ beats, nextBeat: this._nextBeat + beats, fn: method });
        return this;
    }

    // Stutter: temporarily shorten dur to repeat current notes rapidly
    stutter(n = 2) {
        const origDur = this._args.dur ?? 1;
        this._args.dur = origDur / n;
        setTimeout(() => { if (this._active) this._args.dur = origDur; },
            n * (origDur / n) * (60000 / this._clock.bpm) + 50);
        return this;
    }

    // Reverse degree array for one cycle
    reverse() {
        if (Array.isArray(this._args.degree)) {
            const orig = [...this._args.degree];
            this._args.degree = [...orig].reverse();
            const durMs = orig.length * (this._args.dur ?? 1) * (60000 / this._clock.bpm);
            setTimeout(() => { if (this._active) this._args.degree = orig; }, durMs + 50);
        }
        return this;
    }

    // Shuffle degree array for one cycle
    shuffle() {
        if (Array.isArray(this._args.degree)) {
            const orig = [...this._args.degree];
            const shuf = [...orig].sort(() => Math.random() - 0.5);
            this._args.degree = shuf;
            const durMs = orig.length * (this._args.dur ?? 1) * (60000 / this._clock.bpm);
            setTimeout(() => { if (this._active) this._args.degree = orig; }, durMs + 50);
        }
        return this;
    }
}

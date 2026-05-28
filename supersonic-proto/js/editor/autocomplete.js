// FoxDot autocomplete using CodeMirror show-hint addon.
// Ctrl+Space: synths after >>, params inside (), methods after ., general otherwise.
// Empty line: insert new player name + " >> " then immediately show synth list.

import { SYNTH_DEFS }   from '../synths/registry.js';
import { FX_REGISTRY }  from '../fx/registry.js';

const SYNTH_NAMES = Object.keys(SYNTH_DEFS);
const FX_PARAMS   = Object.keys(FX_REGISTRY);

const PLAYER_METHODS = [
    'stop()', 'solo()', 'soloDrop()', 'every()', 'stutter()', 'reverse()', 'shuffle()',
];

const COMMON_PARAMS = ['degree','oct','amp','dur','sus','pan','attack','release'];

const SCALE_NAMES = [
    'major','minor','dorian','phrygian','lydian','mixolydian',
    'pentatonic','minPentatonic','chromatic','diminished','bhairav',
];

const PATTERN_NAMES = [
    'PRand','PWalk','PDur','PPing','PStutter','PBern','PEuclid','PAlt',
    'PShuf','PStep','PRange','PSine','PTri','PChain','PMarkov',
    'PWhite','PxRand','PwRand','PSq','PSum','PEuclid2','PBeat','PDelay',
    'PStrum','PRhythm','PDrum',
];

const TIMEVAR_NAMES = ['var(','linvar(','sinvar(','expvar('];

const GLOBALS = ['Clock.bpm = ','Scale.default = ','Root.default = ','play(','drop(','unsolo()','rest()','print('];

// ── Player name generation ───────────────────────────────────────────────────

// Scan editor content for already-declared player names
function usedPlayerNames(cm) {
    const used = new Set();
    const re = /^\s*([a-zA-Z_]\w*)\s*>>/;
    for (let i = 0; i < cm.lineCount(); i++) {
        const m = cm.getLine(i).match(re);
        if (m) used.add(m[1]);
    }
    return used;
}

// Return the first unused player name from the priority list
const NAME_PREFIXES = 'vapbscdefghijklmnoqrtuwxyz'.split('');
function nextPlayerName(cm) {
    const used = usedPlayerNames(cm);
    for (const p of NAME_PREFIXES) {
        for (let n = 1; n <= 9; n++) {
            const name = p + n;
            if (!used.has(name)) return name;
        }
    }
    return 'p' + (Math.floor(Math.random() * 90) + 10);
}

// ── Context detection ────────────────────────────────────────────────────────

function getContext(cm) {
    const cursor = cm.getCursor();
    const line   = cm.getLine(cursor.line);
    const before = line.slice(0, cursor.ch);
    const wordM  = before.match(/([a-zA-Z_][\w.]*)$/);
    const word   = wordM ? wordM[1].replace(/\.$/, '') : '';

    // Empty line → player name suggestion
    if (line.trim() === '') return { type: 'newplayer' };

    if (before.match(/[a-zA-Z_]\w*\.$/))    return { type: 'method', word: '' };
    if (before.match(/[a-zA-Z_]\w*\.\w+$/)) return { type: 'method', word };
    if (before.match(/[a-zA-Z_]\w*\s*>>\s*[a-zA-Z_]*$/)) return { type: 'synth', word };
    const scaleM = before.match(/Scale\s*\.\s*default\s*=\s*["']([a-zA-Z]*)$/);
    if (scaleM) return { type: 'scale', word: scaleM[1] };
    const synthM = before.match(/([a-zA-Z_]\w*)\s*\([^)]*$/);
    if (synthM) {
        const fn = synthM[1];
        if (fn === 'play' || SYNTH_NAMES.includes(fn)) return { type: 'param', synth: fn, word };
        return { type: 'param', synth: null, word };
    }
    return { type: 'general', word };
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function sep(label) {
    return {
        text: '',
        displayText: label,
        className: 'hint-sep',
        hint: () => {},
    };
}

function item(text, cls, display) {
    return { text, displayText: display ?? text, className: cls };
}

// ── Hint function ─────────────────────────────────────────────────────────────

function hintFn(cm) {
    const ctx    = getContext(cm);
    const cursor = cm.getCursor();
    const line   = cm.getLine(cursor.line);
    const before = line.slice(0, cursor.ch);

    const wordM     = before.match(/([a-zA-Z_][\w.]*)$/);
    const wordStart = wordM ? cursor.ch - wordM[1].length : cursor.ch;
    const typedWord = wordM ? wordM[1] : '';
    const from = { line: cursor.line, ch: wordStart };
    const to   = cursor;

    // ── Empty line: suggest a new player name, then auto-show synths ──────────
    if (ctx.type === 'newplayer') {
        const name = nextPlayerName(cm);
        const insertion = name + ' >> ';
        return {
            list: [{
                text:        insertion,
                displayText: insertion,
                className:   'hint-method',
                hint(editor) {
                    editor.replaceRange(insertion, { line: cursor.line, ch: 0 }, { line: cursor.line, ch: line.length });
                    editor.setCursor({ line: cursor.line, ch: insertion.length });
                    // Show synth list immediately after inserting player name
                    setTimeout(() => {
                        editor.showHint({
                            hint:           synthHint,
                            completeSingle: false,
                            alignWithWord:  true,
                        });
                    }, 30);
                },
            }],
            from: { line: cursor.line, ch: 0 },
            to:   { line: cursor.line, ch: line.length },
        };
    }

    function filter(list) {
        if (!typedWord) return list;
        const lw = typedWord.toLowerCase();
        return list.filter(it => {
            const label = (it.displayText ?? it.text).toLowerCase();
            return label.startsWith(lw) || label.replace('=','').startsWith(lw);
        });
    }

    let list = [];

    if (ctx.type === 'method') {
        list = PLAYER_METHODS.map(m => item(m, 'hint-method'));
    } else if (ctx.type === 'synth') {
        list = [item('play(', 'hint-keyword', 'play'), ...SYNTH_NAMES.map(n => item(n, 'hint-synth'))];
    } else if (ctx.type === 'scale') {
        list = SCALE_NAMES.map(n => item(`"${n}"`, 'hint-param', n));
    } else if (ctx.type === 'param') {
        let synthParams;
        if (ctx.synth === 'play') {
            synthParams = ['amp=','dur=','pan=','rate=','sample='].map(p => item(p, 'hint-param'));
        } else if (ctx.synth) {
            synthParams = Object.keys(SYNTH_DEFS[ctx.synth]?.defaults ?? {}).map(p => item(p + '=', 'hint-param'));
        } else {
            synthParams = COMMON_PARAMS.map(p => item(p + '=', 'hint-param'));
        }
        const fxP = ctx.synth === 'play' ? [] : FX_PARAMS.map(p => item(p + '=', 'hint-fx'));
        list = [sep('— params —'), ...synthParams, ...(fxP.length ? [sep('— fx —'), ...fxP] : [])];
        list = list.filter(it => it.className === 'hint-sep' || filter([it]).length > 0);
    } else {
        list = [
            sep('— synths —'),
            ...SYNTH_NAMES.map(n => item(n, 'hint-synth')),
            sep('— patterns —'),
            ...PATTERN_NAMES.map(n => item(n + '(', 'hint-pattern', n)),
            sep('— timevars —'),
            ...TIMEVAR_NAMES.map(n => item(n, 'hint-timevar', n.replace('(', ''))),
            sep('— globals —'),
            ...GLOBALS.map(g => item(g, 'hint-keyword')),
        ];
        if (typedWord) {
            list = list.filter(it => {
                if (it.className === 'hint-sep') return false;
                return (it.displayText ?? it.text).toLowerCase().startsWith(typedWord.toLowerCase());
            });
        }
        return { list, from, to };
    }

    list = filter(list.filter(it => it.className !== 'hint-sep'));
    return { list, from, to };
}

// Minimal hint function for showing just synth names (used after player name insert)
function synthHint(cm) {
    const cursor = cm.getCursor();
    const line   = cm.getLine(cursor.line);
    const before = line.slice(0, cursor.ch);
    const wordM  = before.match(/([a-zA-Z_]\w*)$/);
    const word   = wordM ? wordM[1] : '';
    const from   = { line: cursor.line, ch: cursor.ch - word.length };
    const list   = [
        ...(!word || 'play'.startsWith(word) ? [item('play(', 'hint-keyword', 'play')] : []),
        ...SYNTH_NAMES.filter(n => !word || n.startsWith(word)).map(n => item(n, 'hint-synth')),
    ];
    return { list, from, to: cursor };
}

// ── Public API ────────────────────────────────────────────────────────────────

export function triggerAutocomplete(cm) {
    cm.showHint({
        hint:           hintFn,
        completeSingle: false,
        alignWithWord:  true,
    });
}

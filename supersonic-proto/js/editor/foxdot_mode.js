// FoxDot syntax overlay for CodeMirror 5 — loaded as a plain script (no ES module).
// Registers a "foxdot" mode that layers FoxDot-specific token colors over Python.
(function () {
    'use strict';

    const SYNTHS = [
        'abass','acidbass','alva','ambi','angst','arpy','arpymod','audioin',
        'bass','bbass','bell','bellmod','blip','bnoise','bounce','braids',
        'breakcore','brown','bug','cbass','charm','click','cluster','combs',
        'crackle','creep','cringe','crunch','cs80','dab','dafbass',
        'dbass','dblbass','dirt','donk','donorgan','dopple','dub',
        'dubulse','elpfsaw','fail','feel','fmpiano','fm2','fmvibe','gtr',
        'gun','harp','hoover','jbass','jbass2','keys','kick','kik',
        'lazer','lead','looper','marimba','metronome','mirage','moog',
        'nylon','organ','piano','pads','plaits','plaitsX','pluck',
        'prophet','reese','resonant','rhodes','risset','rsin','rustlead',
        'saw','sawbass','sax','sine','sinepad','sinebass','singer',
        'space','speaky','squarebass','stab','steel','stellar','stepper',
        'sub','supersaw','svdk','theremin','thunder','tribar','tuba',
        'twang','varsaw','vox','wob','wobble','wobblebass',
    ];

    const PATTERNS = [
        'PRand','PWhite','PxRand','PwRand','PChain','PChain2','PZ12','PTree',
        'PWalk','PDelta','PSquare','PIndex','PFibMod','PShuf','PAlt','PStretch',
        'PPairs','PZip','PZip2','PStutter','PSq','P10','PStep','PSum','PRange',
        'PTri','PSine','PEuclid','PEuclid2','PBern','PBeat','PDur','PDelay',
        'PStrum','PQuicken','PRhythm','PJoin','PBin','PSaw','PTime','PTimebin',
        'PFrac','PFr','PDrum','PChords','PGauss','PLog','PTrir','PCoin','PChar',
        'PMarkov','PZero','PBool','PPing','PLife','PBal','PFDur','Pacc','PSwing',
        'PwRand',
    ];

    const TIMEVARS = ['linvar','sinvar','expvar','Pvar','lininf','expinf','linbpm','linmod'];

    const KEYWORDS = [
        'Clock','Scale','Root','drop','rest','print','play','melody','chaos',
        'unsolo','solo','once','norm','clamp','lmap','drummer','fill','brk',
        'renv','clone','switch','start',
    ];

    // Build a fast lookup: word → cm class name
    const tokenMap = new Map();
    SYNTHS.forEach(s   => tokenMap.set(s, 'fd-synth'));
    PATTERNS.forEach(p => tokenMap.set(p, 'fd-pattern'));
    TIMEVARS.forEach(t => tokenMap.set(t, 'fd-timevar'));
    KEYWORDS.forEach(k => tokenMap.set(k, 'fd-keyword'));

    // `var` → fd-timevar (transpiler rewrites it but highlight is useful)
    tokenMap.set('var', 'fd-timevar');

    const WORD_RE = /^[a-zA-Z_]\w*/;
    const PLAYER_RE = /^[a-zA-Z_]\w*(?=\s*>>)/;

    const overlay = {
        token: function (stream) {
            // Player name before >> gets its own color
            if (stream.match(PLAYER_RE, false)) {
                stream.match(WORD_RE);
                return 'fd-player';
            }
            if (stream.match(WORD_RE)) {
                return tokenMap.get(stream.current()) ?? null;
            }
            stream.next();
            return null;
        },
    };

    CodeMirror.defineMode('foxdot', function (config) {
        const py = CodeMirror.getMode(config, 'python');
        return CodeMirror.overlayMode(py, overlay, /* opaque= */ false);
    });

    CodeMirror.defineMIME('text/x-foxdot', 'foxdot');
}());

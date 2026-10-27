// Editor keybinding handlers.

// Nudge number under cursor by delta, then re-eval the block.
export function incrementValue(cm, delta, runBlockFn) {
    const cursor = cm.getCursor();
    const line   = cm.getLine(cursor.line);
    let s = cursor.ch, e = cursor.ch;

    while (s > 0 && /[\d.\-]/.test(line[s - 1])) s--;
    while (e < line.length && /[\d.]/.test(line[e])) e++;

    let numStr = line.slice(s, e);
    if (/^\.\d+$/.test(numStr)) numStr = '0' + numStr;
    if (!/^-?\d+(\.\d+)?$/.test(numStr)) return;

    let result;
    if (numStr.includes('.')) {
        const prec = (numStr.split('.')[1] ?? '').length || 1;
        const step = prec > 1 ? 0.01 : 0.1;
        result = (parseFloat(numStr) + delta * step).toFixed(prec);
    } else {
        const n    = parseInt(numStr, 10);
        const step = Math.abs(n) > 300 ? 100 : 1;
        result = String(n + delta * step);
    }

    if (parseFloat(result) > 22000) result = '22000';
    if (delta < 0 && parseFloat(result) < 0 && !numStr.startsWith('-')) result = '0';

    cm.replaceRange(result, { line: cursor.line, ch: s }, { line: cursor.line, ch: e });
    cm.setCursor({ line: cursor.line, ch: s + result.length });

    if (runBlockFn) runBlockFn();
}

// Parse player name from a line (handles both `p1 >>` and `# p1 >>`)
function playerNameFromLine(line) {
    const m = line.match(/^\s*#?\s*([a-zA-Z_]\w*)\s*>>/);
    return m ? m[1] : null;
}

// Alt+X — toggle comment + stop/restart.
// Comment out → stop player.  Uncomment → restart player (re-eval block).
export function stopPlayerAtCursor(cm, clock, runBlockFn) {
    const cursor  = cm.getCursor();
    const lineNo  = cursor.line;
    const line    = cm.getLine(lineNo);
    const indentM = line.match(/^(\s*)/);
    const indent  = indentM ? indentM[1] : '';
    const trimmed = line.slice(indent.length);

    if (trimmed.startsWith('#')) {
        // Uncomment + restart
        const uncommented = indent + trimmed.replace(/^#\s?/, '');
        cm.replaceRange(uncommented,
            { line: lineNo, ch: 0 },
            { line: lineNo, ch: line.length });
        if (runBlockFn) runBlockFn();
    } else {
        // Comment out + stop
        cm.replaceRange(indent + '# ' + trimmed,
            { line: lineNo, ch: 0 },
            { line: lineNo, ch: line.length });
        const name = playerNameFromLine(line);
        if (name) clock._players.get(name)?.stop();
    }
}

// Alt+S — mute all other players (solo the one at cursor)
export function soloPlayerAtCursor(cm, clock) {
    const line = cm.getLine(cm.getCursor().line);
    const name = playerNameFromLine(line);
    if (name) {
        const p = clock._players.get(name);
        if (p) p.solo();
    }
}

// Alt+O — solo for 8 beats then restore all (soloDrop)
export function soloDropAtCursor(cm, clock, beats = 8) {
    const line = cm.getLine(cm.getCursor().line);
    const name = playerNameFromLine(line);
    if (name) {
        const p = clock._players.get(name);
        if (p) p.soloDrop(beats);
    }
}

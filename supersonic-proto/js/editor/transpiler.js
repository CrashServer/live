// Transpiles FoxDot-style Python syntax to JavaScript.
//
//   p1 >> dbass([0,2,4], oct=3, cutoff=800)
//   → __p('p1').__rshift__(dbass([0,2,4], {oct:3, cutoff:800}))
//
// Also rewrites:
//   var(...)    → _var(...)    (JS reserved word)
//   linvar(...) → _linvar(...) etc.

export function transpile(code) {
    return code.split('\n').map(line => {
        const stripped = line.trim();
        if (!stripped) return line;

        // Full-line Python comment
        if (stripped.startsWith('#')) return line.replace(/^(\s*)#/, '$1//');

        // Strip inline comment
        let main = line, tail = '';
        const ci = findCommentChar(line);
        if (ci !== -1) { main = line.slice(0, ci); tail = '  //' + line.slice(ci + 1); }

        // >> operator: name >> synth(...)
        const m = main.match(/^(\s*)([a-zA-Z_]\w*)\s*>>\s*(.+)$/);
        if (m) {
            const [, indent, player, rhs] = m;
            return `${indent}__p('${player}').__rshift__(${kwargify(rhs.trim())})${tail}`;
        }

        return main + tail;
    }).join('\n');
}

// Apply TimeVar renames so runCode can eval safely
export function applyRenames(js) {
    return js
        .replace(/\bvar\(/g,    '_var(')
        .replace(/\blinvar\(/g, '_linvar(')
        .replace(/\bsinvar\(/g, '_sinvar(')
        .replace(/\bexpvar\(/g, '_expvar(');
}

function findCommentChar(line) {
    let inStr = false, ch = '';
    for (let i = 0; i < line.length; i++) {
        const c = line[i];
        if (inStr)           { if (c === ch) inStr = false; }
        else if (c === '"' || c === "'") { inStr = true; ch = c; }
        else if (c === '#')  { return i; }
    }
    return -1;
}

// Convert Python kwargs inside function call parens to trailing JS object
// bleep([0,2], oct=5, amp=0.7)  →  bleep([0,2], {oct:5, amp:0.7})
function kwargify(expr) {
    let result = '', i = 0;
    while (i < expr.length) {
        let parenIdx = -1;
        for (let j = i; j < expr.length; j++) {
            if (expr[j] === '(') { parenIdx = j; break; }
        }
        if (parenIdx === -1) { result += expr.slice(i); break; }
        result += expr.slice(i, parenIdx + 1);

        // Find matching close paren
        let depth = 1, j = parenIdx + 1;
        while (j < expr.length && depth > 0) {
            const c = expr[j];
            if ('([{'.includes(c)) depth++;
            else if (')]}'. includes(c)) depth--;
            j++;
        }
        const closeIdx = j - 1;
        const inner    = expr.slice(parenIdx + 1, closeIdx);

        const args = splitArgs(inner);
        const pos  = [], kw = {};
        for (const arg of args) {
            const t  = arg.trim();
            const km = t.match(/^([a-zA-Z_]\w*)\s*=(?![=<>!])\s*(.+)$/s);
            if (km) kw[km[1]] = kwargify(km[2].trim());
            else    pos.push(kwargify(t));
        }
        const all = [...pos];
        const keys = Object.keys(kw);
        if (keys.length) all.push('{' + keys.map(k => `${k}: ${kw[k]}`).join(', ') + '}');
        result += all.join(', ') + expr[closeIdx];
        i = closeIdx + 1;
    }
    return result;
}

function splitArgs(str) {
    const args = [];
    let cur = '', depth = 0;
    for (const c of str) {
        if ('([{'.includes(c)) depth++;
        else if (')]}'. includes(c)) depth--;
        else if (c === ',' && depth === 0) { args.push(cur); cur = ''; continue; }
        cur += c;
    }
    if (cur.trim()) args.push(cur);
    return args;
}

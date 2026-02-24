/**
 * VisualMode — highlights the currently playing note/param values in the editor.
 * Zero overhead when disabled: no markers, no parsing, no RAF.
 */

class VisualMode {
    constructor() {
        this.editor = null;
        this.enabled = false;
        this.players = {};       // enriched player data from 'players' message
        this.playerSteps = {};   // { playerName: event_n } from 'beat' message
        this.markers = [];       // active CodeMirror TextMarker instances
        this._rafId = null;
        this._lastUpdate = 0;
        this._throttleMs = 80;   // ~12.5 fps
    }

    init(editor) {
        this.editor = editor;
    }

    enable() {
        this.enabled = true;
        this.scheduleUpdate();
    }

    disable() {
        this.enabled = false;
        this._clearMarkers();
        if (this._rafId) {
            cancelAnimationFrame(this._rafId);
            this._rafId = null;
        }
    }

    toggle() {
        if (this.enabled) this.disable();
        else this.enable();
        return this.enabled;
    }

    setPlayers(playersData) {
        this.players = playersData;
        if (this.enabled) this.scheduleUpdate();
    }

    setPlayerSteps(steps) {
        this.playerSteps = steps;
        if (this.enabled) this.scheduleUpdate();
    }

    scheduleUpdate() {
        if (!this.enabled || this._rafId) return;
        this._rafId = requestAnimationFrame(() => {
            this._rafId = null;
            const now = performance.now();
            if (now - this._lastUpdate < this._throttleMs) {
                // re-schedule if too soon
                this._rafId = requestAnimationFrame(() => {
                    this._rafId = null;
                    this.highlightCurrentNotes();
                    this._lastUpdate = performance.now();
                });
                return;
            }
            this.highlightCurrentNotes();
            this._lastUpdate = now;
        });
    }

    highlightCurrentNotes() {
        if (!this.enabled || !this.editor) return;
        this._clearMarkers();

        const lineCount = this.editor.lineCount();

        for (const [playerName, pData] of Object.entries(this.players)) {
            const step = this.playerSteps[playerName] ?? pData.step ?? 0;
            const patterns = pData.patterns || {};
            const degreePattern = patterns.degree;

            // Find the line where this player is defined
            let playerLine = -1;
            const playerRegex = new RegExp(`^\\s*${this._escapeRegex(playerName)}\\s*>>`);
            for (let i = 0; i < lineCount; i++) {
                if (playerRegex.test(this.editor.getLine(i))) {
                    playerLine = i;
                    break;
                }
            }
            if (playerLine === -1) continue;

            const lineText = this.editor.getLine(playerLine);
            const parsed = this.parseParametersFromLine(lineText);

            // Highlight degree (first positional argument) — yellow glow
            if (parsed.degree && degreePattern && degreePattern.length > 0) {
                const idx = (step - 1) % degreePattern.length;
                const values = this.parsePatternValues(lineText, parsed.degree.start, parsed.degree.end);
                if (values && values.length > 0) {
                    const valueIdx = ((idx % values.length) + values.length) % values.length;
                    const v = values[valueIdx];
                    if (v) {
                        this.markers.push(this.editor.markText(
                            { line: playerLine, ch: v.start },
                            { line: playerLine, ch: v.end },
                            { className: 'playing-note' }
                        ));
                    }
                }
            }

            // Highlight other named params — cyan glow
            for (const [attr, paramInfo] of Object.entries(parsed)) {
                if (attr === 'degree') continue;
                const pat = patterns[attr];
                if (!pat || pat.length === 0) continue;
                const idx = (step - 1) % pat.length;
                const values = this.parsePatternValues(lineText, paramInfo.start, paramInfo.end);
                if (values && values.length > 0) {
                    const valueIdx = ((idx % values.length) + values.length) % values.length;
                    const v = values[valueIdx];
                    if (v) {
                        this.markers.push(this.editor.markText(
                            { line: playerLine, ch: v.start },
                            { line: playerLine, ch: v.end },
                            { className: 'playing-param' }
                        ));
                    }
                }
            }
        }
    }

    /**
     * Parse parameter positions from a FoxDot player line.
     * Returns { degree: {start, end}, dur: {start, end}, ... }
     */
    parseParametersFromLine(line) {
        const result = {};
        // Find the >> operator and the opening paren of the synth call
        const arrowIdx = line.indexOf('>>');
        if (arrowIdx === -1) return result;

        const afterArrow = line.substring(arrowIdx + 2);
        const parenIdx = afterArrow.indexOf('(');
        if (parenIdx === -1) return result;

        const argsStart = arrowIdx + 2 + parenIdx + 1;
        const argsStr = line.substring(argsStart);

        // Find matching closing paren
        let depth = 1;
        let argsEnd = argsStart;
        for (let i = 0; i < argsStr.length; i++) {
            if (argsStr[i] === '(') depth++;
            else if (argsStr[i] === ')') { depth--; if (depth === 0) { argsEnd = argsStart + i; break; } }
        }
        if (depth !== 0) argsEnd = line.length;

        const fullArgs = line.substring(argsStart, argsEnd);

        // Split arguments respecting brackets and parens
        const args = this._splitArgs(fullArgs);

        let firstPositional = true;
        for (const arg of args) {
            const eqIdx = arg.text.indexOf('=');
            if (eqIdx === -1) {
                // Positional — first one is degree
                if (firstPositional) {
                    result.degree = { start: argsStart + arg.offset, end: argsStart + arg.offset + arg.text.length };
                    firstPositional = false;
                }
            } else {
                const paramName = arg.text.substring(0, eqIdx).trim();
                const valueStart = eqIdx + 1;
                const valueText = arg.text.substring(valueStart);
                const trimmedOffset = valueText.length - valueText.trimStart().length;
                result[paramName] = {
                    start: argsStart + arg.offset + valueStart + trimmedOffset,
                    end: argsStart + arg.offset + arg.text.length
                };
            }
        }
        return result;
    }

    /**
     * Parse individual values from a pattern string (e.g., "[0,2,4]" or "xox").
     * Returns array of {start, end} char positions relative to line.
     */
    parsePatternValues(line, start, end) {
        const text = line.substring(start, end).trimEnd();
        const values = [];

        // Handle list patterns: [0, 2, 4]
        if (text.startsWith('[') || text.startsWith('P[')) {
            const bracketStart = text.indexOf('[');
            const inner = text.substring(bracketStart + 1, text.lastIndexOf(']') || text.length);
            let pos = bracketStart + 1;
            const items = this._splitArgs(inner);
            for (const item of items) {
                const trimmed = item.text.trim();
                const trimOffset = item.text.indexOf(trimmed);
                if (trimmed.length > 0) {
                    values.push({
                        start: start + pos + item.offset + trimOffset,
                        end: start + pos + item.offset + trimOffset + trimmed.length
                    });
                }
            }
            return values;
        }

        // Handle string patterns: "xox" or "x-o-x-o-"
        if (text.startsWith('"') || text.startsWith("'")) {
            const quote = text[0];
            const closeIdx = text.lastIndexOf(quote, text.length - 1);
            if (closeIdx > 0) {
                for (let i = 1; i < closeIdx; i++) {
                    values.push({ start: start + i, end: start + i + 1 });
                }
            }
            return values;
        }

        // Single value
        const trimmed = text.trim();
        if (trimmed.length > 0) {
            const offset = text.indexOf(trimmed);
            values.push({ start: start + offset, end: start + offset + trimmed.length });
        }
        return values;
    }

    /** Split comma-separated args respecting brackets/parens/quotes */
    _splitArgs(str) {
        const args = [];
        let depth = 0;
        let inStr = null;
        let current = '';
        let startOffset = 0;

        for (let i = 0; i < str.length; i++) {
            const ch = str[i];
            if (inStr) {
                current += ch;
                if (ch === inStr) inStr = null;
            } else if (ch === '"' || ch === "'") {
                current += ch;
                inStr = ch;
            } else if (ch === '(' || ch === '[' || ch === '{') {
                current += ch;
                depth++;
            } else if (ch === ')' || ch === ']' || ch === '}') {
                current += ch;
                depth--;
            } else if (ch === ',' && depth === 0) {
                args.push({ text: current, offset: startOffset });
                current = '';
                startOffset = i + 1;
            } else {
                current += ch;
            }
        }
        if (current.length > 0) {
            args.push({ text: current, offset: startOffset });
        }
        return args;
    }

    _escapeRegex(str) {
        return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    _clearMarkers() {
        for (const m of this.markers) {
            try { m.clear(); } catch (_) {}
        }
        this.markers = [];
    }
}

export const visualMode = new VisualMode();

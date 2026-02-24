/**
 * Visual Mode - Highlight current playing notes in code
 * Uses server-sent step data for accurate highlighting of all parameters
 */

export class VisualMode {
  constructor() {
    this.enabled = false;
    this.editor = null;
    this.beat = 0;
    this.players = [];
    this.playerSteps = {};
    this.markers = [];
    this.needsUpdate = false;
    this.lastUpdate = 0;
    this.updateInterval = 80;
  }

  init(editor) {
    this.editor = editor;
  }

  enable() {
    this.enabled = true;
    document.body.classList.add('visual-mode-active');
  }

  disable() {
    this.enabled = false;
    document.body.classList.remove('visual-mode-active');
    this.clearMarkers();
  }

  toggle() {
    if (this.enabled) {
      this.disable();
    } else {
      this.enable();
    }
    return this.enabled;
  }

  setBeat(beat) {
    this.beat = beat;
  }

  setBpm() {}
  setTheme() {}

  setPlayers(players) {
    this.players = players;
    this.needsUpdate = true;
    this.scheduleUpdate();
  }

  setPlayerSteps(playerSteps) {
    this.playerSteps = playerSteps;
    this.needsUpdate = true;
    this.scheduleUpdate();
  }

  scheduleUpdate() {
    if (!this.enabled) return;
    const now = performance.now();
    if (now - this.lastUpdate >= this.updateInterval) {
      this.doUpdate();
    }
  }

  doUpdate() {
    if (!this.enabled || !this.editor || !this.needsUpdate) return;
    this.lastUpdate = performance.now();
    this.needsUpdate = false;
    this.highlightCurrentNotes();
  }

  clearMarkers() {
    this.markers.forEach(m => m.clear());
    this.markers = [];
  }

  formatValue(val) {
    if (val === null || val === undefined) return '?';
    if (typeof val === 'number') {
      return Number.isInteger(val) ? val : val.toFixed(1);
    }
    return String(val);
  }

  // ===== Static Pattern Highlighting =====

  parseParametersFromLine(line) {
    const params = {};
    const degreeMatch = line.match(/\(\s*(\[[^\]]+\]|"[^"]+"|'[^']+')/);
    if (degreeMatch) {
      const patternStr = degreeMatch[1];
      const patternStart = line.indexOf(patternStr);
      params.degree = this.parsePatternValues(patternStr, patternStart, line);
    }

    const paramRegex = /(\w+)\s*=\s*(\[[^\]]+\]|"[^"]+"|'[^']+'|[0-9.\/]+)/g;
    let match;
    while ((match = paramRegex.exec(line)) !== null) {
      const paramName = match[1];
      const paramValue = match[2];
      const paramStart = match.index + match[0].indexOf(paramValue);
      if (paramValue.startsWith('[') || paramValue.startsWith('"') || paramValue.startsWith("'")) {
        params[paramName] = this.parsePatternValues(paramValue, paramStart, line);
      }
    }
    return params;
  }

  parsePatternValues(patternStr, patternStart, line) {
    const values = [];
    if (patternStr.startsWith('[')) {
      const inner = patternStr.slice(1, -1);
      let pos = patternStart + 1;
      let current = '';
      let depth = 0;

      for (let i = 0; i < inner.length; i++) {
        const char = inner[i];
        if (char === '(' || char === '[') depth++;
        if (char === ')' || char === ']') depth--;

        if ((char === ',' && depth === 0) || i === inner.length - 1) {
          if (i === inner.length - 1 && char !== ',') current += char;
          const trimmed = current.trim();
          if (trimmed) {
            const valuePos = line.indexOf(trimmed, pos);
            if (valuePos !== -1) {
              values.push({ text: trimmed, start: valuePos, end: valuePos + trimmed.length });
              pos = valuePos + trimmed.length;
            }
          }
          current = '';
        } else {
          current += char;
        }
      }
    } else if (patternStr.startsWith('"') || patternStr.startsWith("'")) {
      const inner = patternStr.slice(1, -1);
      // For play strings, parse FoxDot syntax: {} [] <> are grouping brackets
      let i = 0;
      while (i < inner.length) {
        const char = inner[i];
        const brackets = { '{': '}', '[': ']', '<': '>', '(': ')' };

        if (brackets[char]) {
          const closeBracket = brackets[char];
          let depth = 1;
          let j = i + 1;
          while (j < inner.length && depth > 0) {
            if (inner[j] === char) depth++;
            else if (inner[j] === closeBracket) depth--;
            j++;
          }
          const groupText = inner.slice(i, j);
          values.push({
            text: groupText,
            start: patternStart + 1 + i,
            end: patternStart + 1 + j
          });
          i = j;
        } else {
          values.push({
            text: char,
            start: patternStart + 1 + i,
            end: patternStart + 2 + i
          });
          i++;
        }
      }
    }
    return values;
  }

  highlightCurrentNotes() {
    this.clearMarkers();
    if (!this.editor || this.players.length === 0) return;

    const code = this.editor.getValue();
    const lines = code.split('\n');

    // Debug: log player info once per update
    if (this.players.length > 0 && !this._lastDebugTime || Date.now() - this._lastDebugTime > 2000) {
      this._lastDebugTime = Date.now();
      console.log('[visualMode] players:', this.players.map(p => ({
        id: p.name || p.player || p.id,
        playstring: p.playstring,
        degree: p.patterns?.degree,
        step: this.playerSteps[p.name || p.player || p.id]
      })));
    }

    this.players.forEach(player => {
      const playerId = player.name || player.player || player.id;
      if (!playerId) return;

      const rawStep = this.playerSteps[playerId] ?? player.step ?? 0;
      const serverPatterns = player.patterns || {};
      const generators = player.generators || {};
      const playstring = player.playstring;

      for (let lineNum = 0; lineNum < lines.length; lineNum++) {
        const line = lines[lineNum];
        const playerMatch = line.match(new RegExp(`^\\s*${playerId}\\s*>>`));
        if (!playerMatch) continue;

        const params = this.parseParametersFromLine(line);

        for (const [paramName, values] of Object.entries(params)) {
          if (generators[paramName]) continue;
          if (values.length === 0) continue;

          let patternLength = values.length;
          if (paramName === 'degree' && playstring) {
            // For play synths, use parsed values length (client-side parsing)
            patternLength = values.length;
          } else if (serverPatterns[paramName] && serverPatterns[paramName].length > 0) {
            patternLength = serverPatterns[paramName].length;
          }

          const step = rawStep > 0 ? rawStep - 1 : 0;
          const currentIndex = step % patternLength;
          const safeIndex = currentIndex % values.length;
          const currentValue = values[safeIndex];

          if (currentValue) {
            const className = paramName === 'degree' ? 'playing-note' : 'playing-param';
            const marker = this.editor.markText(
              { line: lineNum, ch: currentValue.start },
              { line: lineNum, ch: currentValue.end },
              { className }
            );
            this.markers.push(marker);
          }
        }
      }
    });
  }
}

// Singleton
export const visualMode = new VisualMode();

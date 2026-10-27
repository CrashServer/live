/**
 * Pattern Log - Text-based ASCII visualization of FoxDot patterns
 * Displays in terminal style matching the rest of the interface
 */

export class PatternLog {
  constructor() {
    this.container = null;
    this.enabled = false;
    this.players = [];
    this.playerSteps = {};
    this.beat = 0;
  }

  init(containerId = 'pattern-log') {
    this.container = document.getElementById(containerId);
  }

  enable() {
    this.enabled = true;
    if (this.container) {
      this.container.style.display = 'block';
    }
    this.render();
  }

  disable() {
    this.enabled = false;
    if (this.container) {
      this.container.style.display = 'none';
      this.container.textContent = '';
    }
  }

  setBeat(beat) {
    this.beat = beat;
    this.render();
  }

  setPlayerSteps(steps) {
    this.playerSteps = steps;
    this.render();
  }

  setPlayers(players) {
    this.players = players;
    this.render();
  }

  render() {
    if (!this.enabled || !this.container) return;

    if (this.players.length === 0) {
      this.container.textContent = '-- no active players --';
      return;
    }

    const lines = this.players.map(player => this.renderPlayer(player));
    this.container.textContent = lines.join('\n');
  }

  renderPlayer(player) {
    const id = player.name || player.player || player.id || '?';
    const name = (player.name || '?').padEnd(6).slice(0, 6);
    const patterns = player.patterns || {};
    const generators = player.generators || {};
    const current = player.current || {};
    const playstring = player.playstring;

    const rawStep = this.playerSteps[id] ?? player.step ?? 0;
    const step = rawStep > 0 ? rawStep - 1 : 0;

    let patternViz = '';
    let currentVal = '';

    // Degree visualization
    if (generators.degree) {
      patternViz = this.renderGenerator(generators.degree);
      currentVal = this.formatVal(current.degree);
    } else if (patterns.degree && patterns.degree.length > 0) {
      if (playstring) {
        patternViz = this.renderPlaystring(patterns.degree, step);
      } else {
        patternViz = this.renderPattern(patterns.degree, step);
      }
      currentVal = this.formatVal(current.degree);
    }

    // Build line
    const idPad = id.padEnd(3);
    const vizPad = patternViz.padEnd(20).slice(0, 20);

    // Add other active generators
    const extras = [];
    for (const [attr, gen] of Object.entries(generators)) {
      if (attr !== 'degree') {
        extras.push(`${attr.slice(0,3)}:${this.renderGeneratorCompact(gen)}`);
      }
    }
    const extrasStr = extras.length > 0 ? ' ' + extras.join(' ') : '';

    return `${idPad} ${name} ${vizPad} ${currentVal}${extrasStr}`;
  }

  renderPattern(pattern, step) {
    const len = pattern.length;
    const idx = step % len;

    // Show pattern with current position marked
    const chars = pattern.map((val, i) => {
      const v = this.formatVal(val);
      if (i === idx) {
        return `[${v}]`;
      }
      return ` ${v} `;
    });

    // Limit display length
    if (chars.length <= 8) {
      return chars.join('');
    }

    // Show window around current position
    const windowSize = 4;
    const start = Math.max(0, idx - windowSize);
    const end = Math.min(len, idx + windowSize + 1);
    const visible = chars.slice(start, end);

    let result = '';
    if (start > 0) result += '..';
    result += visible.join('');
    if (end < len) result += '..';

    return result;
  }

  renderPlaystring(pattern, step) {
    const len = pattern.length;
    const idx = step % len;

    // Show each character, highlight current
    const chars = pattern.map((val, i) => {
      const v = String(val).charAt(0);
      return i === idx ? `[${v}]` : ` ${v} `;
    });

    if (chars.length <= 12) {
      return chars.join('');
    }

    // Window around current
    const start = Math.max(0, idx - 5);
    const end = Math.min(len, idx + 6);
    let result = start > 0 ? '..' : '';
    result += chars.slice(start, end).join('');
    result += end < len ? '..' : '';
    return result;
  }

  renderGenerator(gen) {
    const type = gen.type;
    const cur = gen.current ?? 0;

    if (type === 'PWhite' || type === 'PRand' || type === 'PWalk') {
      const lo = gen.lo ?? 0;
      const hi = gen.hi ?? 7;
      return this.renderRangeBar(lo, hi, cur, type.charAt(1));
    }

    if (type === 'linvar') {
      const vals = gen.values || [0, 1];
      const progress = gen.progress || 0;
      return this.renderProgressBar(vals[0], vals[vals.length-1], progress, cur);
    }

    if (type === 'var') {
      const vals = gen.values || [];
      const idx = gen.index || 0;
      return this.renderVarSteps(vals, idx);
    }

    if (type === 'PwRand') {
      const vals = gen.values || [];
      return `PwR(${vals.slice(0,4).join(',')})`;
    }

    // Generic
    return `${type}`;
  }

  renderGeneratorCompact(gen) {
    const type = gen.type;
    const cur = gen.current;

    if (type === 'PWhite' || type === 'PRand') {
      return `${this.formatVal(cur)}`;
    }
    if (type === 'linvar' || type === 'var') {
      return `${this.formatVal(cur)}`;
    }
    return `${this.formatVal(cur)}`;
  }

  renderRangeBar(lo, hi, cur, typeChar = 'W') {
    // ASCII range bar: lo|----*----|hi
    const range = hi - lo;
    const barLen = 8;
    const pos = range > 0 ? Math.round(((cur - lo) / range) * barLen) : barLen / 2;
    const safePos = Math.max(0, Math.min(barLen, pos));

    let bar = '';
    for (let i = 0; i <= barLen; i++) {
      bar += i === safePos ? '*' : '-';
    }

    return `${typeChar}:${this.formatVal(lo)}|${bar}|${this.formatVal(hi)}`;
  }

  renderProgressBar(start, end, progress, cur) {
    // ASCII progress bar: [=====>    ] 0.5
    const barLen = 8;
    const filled = Math.round(progress * barLen);

    let bar = '';
    for (let i = 0; i < barLen; i++) {
      if (i < filled) bar += '=';
      else if (i === filled) bar += '>';
      else bar += ' ';
    }

    return `lv[${bar}]${this.formatVal(cur)}`;
  }

  renderVarSteps(vals, idx) {
    // Show values with current marked: 0 [4] 7
    const display = vals.slice(0, 5).map((v, i) => {
      const vStr = this.formatVal(v);
      return i === idx ? `[${vStr}]` : vStr;
    });

    let result = 'v:' + display.join(' ');
    if (vals.length > 5) result += '..';
    return result;
  }

  formatVal(val) {
    if (val === null || val === undefined) return '?';
    if (typeof val === 'number') {
      if (Number.isInteger(val)) return String(val);
      return val.toFixed(1);
    }
    if (typeof val === 'string') {
      return val.length > 3 ? val.slice(0, 3) : val;
    }
    return String(val).slice(0, 3);
  }
}

// Singleton
export const patternLog = new PatternLog();

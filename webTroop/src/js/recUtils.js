import { EventEmitter } from './eventBus.js';

export const recUtils = {
  // === AUTOMATION RECORDER ===
  // Floor for a segment length, in beats. Timing now comes from FoxDot's
  // fractional Clock beat, so this only guards a genuine zero-length segment
  // (two captures in the same 100 ms tick) rather than every sub-beat gesture.
  _AUTOREC_MIN_DUR: 0.125,

  _autoRec: {
      armed: false,
      startTime: 0,
      recordings: {},  // { paramName: [{time, value}, ...] }
      marker: null,    // CodeMirror bookmark pinning the armed line
      originalLine: null,
  },

  // The line this recording is pinned to. Uses a bookmark rather than a line
  // number so a collaborator inserting/removing lines above cannot make us
  // overwrite somebody else's line.
  _autoRecLine() {
      const m = this._autoRec.marker;
      if (!m) return null;
      const pos = m.find();
      return pos ? (pos.line !== undefined ? pos.line : pos.from.line) : null;
  },

  autoRecToggle(cm, evaluateFn) {
      const rec = this._autoRec;
      if (!rec.armed) {
          // ARM — start recording, pinned to the cursor's line
          const line = cm.getCursor().line;
          rec.armed = true;
          rec.startTime = performance.now();
          rec.recordings = {};
          if (rec.marker) rec.marker.clear();
          rec.marker = cm.setBookmark({ line: line, ch: 0 }, { insertLeft: true });
          rec.originalLine = cm.getLine(line);
          this._autoRecShowIndicator(true);
      } else {
          // DISARM — stop, convert, write (no evaluation: the user decides when)
          rec.armed = false;
          this._autoRecShowIndicator(false);
          this._autoRecFinalize(cm);
          if (rec.marker) { rec.marker.clear(); rec.marker = null; }
      }
  },

  autoRecCancel(cm, evaluateFn) {
      const rec = this._autoRec;
      if (!rec.armed) return;
      rec.armed = false;
      this._autoRecShowIndicator(false);
      // Restore the line exactly as it was when we armed, rather than trying to
      // patch individual params back with a regex.
      const target = this._autoRecLine();
      if (target !== null && rec.originalLine !== null) {
          const line = cm.getLine(target);
          if (line !== undefined && line !== rec.originalLine) {
              cm.operation(() => {
                  cm.replaceRange(rec.originalLine,
                      { line: target, ch: 0 },
                      { line: target, ch: line.length }
                  );
              });
          }
      }
      if (rec.marker) { rec.marker.clear(); rec.marker = null; }
      rec.recordings = {};
      rec.originalLine = null;
  },

  autoRecCapture(cm) {
      const rec = this._autoRec;
      if (!rec.armed) return;

      // Only record edits on the line we armed on. Previously any nudge
      // retargeted the recording, so touching a second line folded both sets of
      // captures into whichever line was edited last.
      const target = this._autoRecLine();
      const cursor = cm.getCursor();
      if (target === null || cursor.line !== target) {
          this._autoRecShowIndicator(true, 'off-line');
          return;
      }

      const line = cm.getLine(cursor.line);

      // Find number boundaries at cursor
      let numStart = cursor.ch;
      let numEnd = cursor.ch;
      while (numStart > 0 && /[\d.\-]/.test(line.charAt(numStart - 1))) numStart--;
      while (numEnd < line.length && /[\d.]/.test(line.charAt(numEnd))) numEnd++;
      const valueStr = line.substring(numStart, numEnd);
      if (!/^-?\d+(\.\d+)?$/.test(valueStr)) return;

      // Try to find param name (e.g. "tcut" from "tcut=400")
      let paramName = null;
      let eqPos = numStart - 1;
      while (eqPos >= 0 && line.charAt(eqPos) === ' ') eqPos--;
      if (eqPos >= 0 && line.charAt(eqPos) === '=') {
          let nameEnd = eqPos;
          let nameStart = nameEnd - 1;
          while (nameStart >= 0 && /[a-zA-Z_\d]/.test(line.charAt(nameStart))) nameStart--;
          nameStart++;
          paramName = line.substring(nameStart, nameEnd);
      }

      // No param name (degree, value inside list, TimeVar arg) — use position
      if (!paramName) {
          paramName = `@pos${numStart}`;
      }

      // Detect if this number is in a TimeVar duration position
      // Walk backwards from cursor tracking paren depth to find enclosing TimeVar
      const before = line.substring(0, numStart);
      let isDurationArg = false;
      let depth = 0;
      let enclosingFnStart = -1;
      for (let i = before.length - 1; i >= 0; i--) {
          const ch = before.charAt(i);
          if (ch === ')') depth++;
          if (ch === '(') {
              if (depth === 0) {
                  // This is the opening paren that encloses our cursor
                  // Check if it's a TimeVar function
                  const preceding = before.substring(0, i);
                  if (/(?:linvar|sinvar|expvar|var)\s*$/.test(preceding)) {
                      enclosingFnStart = i;
                  }
                  break;
              }
              depth--;
          }
      }
      if (enclosingFnStart >= 0) {
          // We're inside a TimeVar call — check if after "],
          const insideFn = before.substring(enclosingFnStart);
          if (insideFn.indexOf('],') !== -1) {
              isDurationArg = true;
          }
      }

      const beatTime = this._autoRecGetCurrentBeat();

      if (!rec.recordings[paramName]) {
          rec.recordings[paramName] = [];
      }
      rec.recordings[paramName].push({
          time: beatTime,
          value: parseFloat(valueStr),
          charStart: numStart,
          charEnd: numEnd,
          isDurationArg: isDurationArg,
      });
      this._autoRecShowIndicator(true);
  },

  // Match `param=` only when it is a whole word, so nudging `cutoff` cannot
  // rewrite `fbcutoff`, `feed` cannot hit `fbfeed`, `mix` cannot hit `mverbmix`.
  _autoRecParamRe(param, withTimeVar) {
      const value = withTimeVar
          ? '(?:(?:linvar|sinvar|expvar|var)\\([^()]*(?:\\([^()]*\\)[^()]*)*\\)|[\\d.\\-]+)'
          : '[\\d.\\-]+';
      return new RegExp('(^|[^A-Za-z0-9_])' + param + '\\s*=\\s*' + value);
  },

  _autoRecShowIndicator(show, state) {
      let el = document.getElementById('autorec-indicator');
      if (show) {
          if (!el) {
              el = document.createElement('div');
              el.id = 'autorec-indicator';
              el.style.cssText = 'position:fixed;top:8px;right:8px;background:#e33;color:#fff;padding:4px 10px;border-radius:4px;font-size:12px;font-family:monospace;z-index:9999;animation:pulse 1s infinite;';
              const style = document.createElement('style');
              style.textContent = '@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}';
              document.head.appendChild(style);
              document.body.appendChild(el);
          }
          // Say what is actually being captured, so it is not a black box.
          const rec = this._autoRec;
          const names = Object.keys(rec.recordings || {});
          const pts = names.reduce((n, k) => n + rec.recordings[k].length, 0);
          const shown = names.map(n => (n.startsWith('@pos') ? 'value' : n));
          if (state === 'off-line') {
              el.textContent = '● REC — other line, ignored';
              el.style.background = '#a60';
          } else {
              el.textContent = names.length
                  ? `● REC ${shown.join(', ')} (${pts})`
                  : '● REC — nudge a number';
              el.style.background = '#e33';
          }
          el.style.display = 'block';
      } else if (el) {
          el.style.display = 'none';
      }
  },

  _autoRecFinalize(cm) {
      const rec = this._autoRec;
      const recordings = rec.recordings;
      const paramNames = Object.keys(recordings);
      if (paramNames.length === 0) return;

      const target = this._autoRecLine();
      if (target === null) {
          console.warn('autoRec: armed line no longer exists — nothing written');
          rec.recordings = {};
          return;
      }

      // Sort position-based keys in reverse order so replacements don't shift offsets
      const sorted = paramNames.sort((a, b) => {
          const posA = a.startsWith('@pos') ? parseInt(a.slice(4)) : -1;
          const posB = b.startsWith('@pos') ? parseInt(b.slice(4)) : -1;
          return posB - posA; // reverse: replace from right to left
      });

      const line = cm.getLine(target);
      if (line === undefined) { rec.recordings = {}; return; }
      let newLine = line;

      for (const param of sorted) {
          const points = recordings[param];
          if (points.length < 2) continue;

          const isDurArg = points.some(p => p.isDurationArg);
          const converted = this._autoRecConvert(points, isDurArg);

          const last = points[points.length - 1];

          if (param.startsWith('@pos')) {
              // Position-based: use exact position from last capture
              const start = last.charStart;
              const end = last.charEnd;
              if (start >= 0 && end <= newLine.length) {
                  newLine = newLine.substring(0, start) + converted + newLine.substring(end);
              }
          } else {
              // Named param: whole-word match so we cannot clobber a longer
              // param that ends with this name (cutoff vs fbcutoff).
              const regex = this._autoRecParamRe(param, true);
              if (!regex.test(newLine)) {
                  console.warn(`autoRec: ${param} not found on the armed line — skipped`);
                  continue;
              }
              newLine = newLine.replace(regex, (m, lead) => lead + param + '=' + converted);
          }
      }

      if (newLine !== line) {
          // One undo step; no evaluation — the change is visible and the user
          // evaluates it themselves when ready.
          cm.operation(() => {
              cm.replaceRange(newLine,
                  { line: target, ch: 0 },
                  { line: target, ch: line.length }
              );
          });
          cm.setCursor({ line: target, ch: Math.min(newLine.length, line.length) });
      }
      rec.recordings = {};
  },

  _autoRecRoundValue(val) {
      // Round to clean numbers
      if (Math.abs(val) >= 100) return Math.round(val / 50) * 50;
      if (Math.abs(val) >= 10) return Math.round(val / 5) * 5;
      if (Math.abs(val) >= 1) return Math.round(val * 10) / 10;
      return Math.round(val * 100) / 100;
  },

  _autoRecConvert(points, isDurationArg = false) {
      const MIN = this._AUTOREC_MIN_DUR;
      const values = points.map(p => this._autoRecRoundValue(p.value));

      // Collapse runs of the same value, keeping the moment it was SET.
      // Every distinct value the user passed through is preserved: the old
      // peak/valley filter threw away the middle of any one-way gesture, so a
      // 400 -> 800 -> 1200 -> 1600 staircase collapsed to [400, 1600].
      const steps = [];
      for (let i = 0; i < values.length; i++) {
          if (!steps.length || values[i] !== steps[steps.length - 1].value) {
              steps.push({ value: values[i], time: points[i].time });
          }
      }
      if (steps.length === 1) return String(steps[0].value);

      // Dwell of each value = time until the next change. The final value is
      // held until the last capture.
      const lastTime = points[points.length - 1].time;
      const durs = [];
      for (let i = 0; i + 1 < steps.length; i++) {
          durs.push(Math.max(this._autoRecBeatDelta(steps[i].time, steps[i + 1].time), MIN));
      }
      // The final value has no "next change" to measure against. Its dwell is
      // whatever is left after the last change; if that is ~0 (the recording
      // stopped on the change itself) reuse the typical dwell so the list loops
      // evenly instead of flashing past the last value.
      const tail = this._autoRecBeatDelta(steps[steps.length - 1].time, lastTime);
      const typical = durs.length
          ? durs.slice().sort((a, b) => a - b)[Math.floor(durs.length / 2)]
          : MIN;
      durs.push(tail > MIN ? tail : typical);

      let vals = steps.map(s => s.value);
      // A TimeVar list wraps, so a gesture that returns to its starting value
      // does not need that value repeated at the end.
      if (vals.length > 2 && vals[0] === vals[vals.length - 1]) {
          vals = vals.slice(0, -1);
          durs.pop();
      }

      // Duration argument: no TimeVars allowed there, plain list only.
      if (isDurationArg) return `[${vals.join(', ')}]`;

      // Ramp or step? Rapid successive nudges read as one sweep; values set
      // and then left alone are discrete changes. Emitting linvar for the
      // latter turned a hard switch into a slow glide.
      const gaps = durs.slice(0, -1);
      const median = gaps.length
          ? gaps.slice().sort((a, b) => a - b)[Math.floor(gaps.length / 2)]
          : durs[0];
      const isSweep = vals.length >= 3 && median < 1;
      const fn = isSweep ? 'linvar' : 'var';

      const round2 = (n) => Math.round(n * 100) / 100;
      const allSame = durs.every(d => Math.abs(d - durs[0]) < 0.05);
      const durPart = allSame ? String(round2(durs[0]))
                              : `[${durs.map(round2).join(', ')}]`;
      return `${fn}([${vals.join(', ')}], ${durPart})`;
  },

  // Plus utilisé pour le moment, à voir si on snap ou pas sachant qu'on récupère que des entiers de beat.
  _autoRecSnapBeat(beats) {
      // Snap to nearest musical subdivision
      const grid = [0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 32];
      let best = 1;
      let bestDist = Infinity;
      for (const g of grid) {
          const dist = Math.abs(beats - g);
          if (dist < bestDist) {
              bestDist = dist;
              best = g;
          }
      }
      return best;
  },

  // Fractional beat, fed straight from FoxDot's Clock (~10 Hz) via the event
  // bus. Falls back to the rounded DOM readout only if no beat has arrived.
  _beatNow: null,

  _autoRecGetCurrentBeat() {
      if (this._beatNow !== null) return this._beatNow;
      // Fallback: the beat-64 div is whole beats only ("27/64")
      const beatEl = document.getElementById('beat-64');
      if (!beatEl) return 0;
      return parseInt(beatEl.textContent.trim().split('/')[0], 10) || 0;
  },

  _autoRecInit() {
      if (this._beatSubscribed) return;
      this._beatSubscribed = true;
      EventEmitter.on('beat', (b) => {
          if (typeof b === 'number' && isFinite(b)) this._beatNow = b;
      });
  },

  _autoRecBeatDelta(beatStart, beatEnd, cycleSize = 64) {
      // Calculate beat difference, handling wrap-around (e.g., 55 → 8 = 17 beats)
      if (beatEnd >= beatStart) {
          return beatEnd - beatStart;
      }
      // Wrap case: beatEnd < beatStart means we crossed the cycle boundary
      return (cycleSize - beatStart) + beatEnd;
  },
}

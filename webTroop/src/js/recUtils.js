export const recUtils = {
  // === AUTOMATION RECORDER ===
  _autoRec: {
      armed: false,
      startTime: 0,
      recordings: {},  // { paramName: [{time, value}, ...] }
      cursorLine: null,
  },

  autoRecToggle(cm, evaluateFn) {
      const rec = this._autoRec;
      if (!rec.armed) {
          // ARM — start recording
          rec.armed = true;
          rec.startTime = performance.now();
          rec.recordings = {};
          rec.cursorLine = cm.getCursor().line;
          rec.originalLine = cm.getLine(rec.cursorLine);
          this._autoRecShowIndicator(true);
      } else {
          // DISARM — stop, convert, replace
          rec.armed = false;
          this._autoRecShowIndicator(false);
          this._autoRecFinalize(cm, evaluateFn);
      }
  },

  autoRecCancel(cm, evaluateFn) {
      const rec = this._autoRec;
      if (!rec.armed) return;
      rec.armed = false;
      this._autoRecShowIndicator(false);
      // Restore params to their first recorded values
      const line = cm.getLine(rec.cursorLine);
      let newLine = line;
      // Sort position-based in reverse to avoid offset shifts
      const params = Object.keys(rec.recordings).sort((a, b) => {
          const posA = a.startsWith('@pos') ? parseInt(a.slice(4)) : -1;
          const posB = b.startsWith('@pos') ? parseInt(b.slice(4)) : -1;
          return posB - posA;
      });
      for (const param of params) {
          const firstVal = rec.recordings[param][0];
          const lastVal = rec.recordings[param][rec.recordings[param].length - 1];
          if (!firstVal) continue;
          if (param.startsWith('@pos')) {
              // Use exact position from last capture to find current value
              const start = lastVal.charStart;
              const end = lastVal.charEnd;
              if (start >= 0 && end <= newLine.length) {
                  newLine = newLine.substring(0, start) + firstVal.value + newLine.substring(end);
              }
          } else {
              const regex = new RegExp(param + '\\s*=\\s*[\\d.\\-]+');
              newLine = newLine.replace(regex, param + '=' + firstVal.value);
          }
      }
      if (newLine !== line) {
          cm.replaceRange(newLine,
              { line: rec.cursorLine, ch: 0 },
              { line: rec.cursorLine, ch: line.length }
          );
          if (evaluateFn) evaluateFn(cm, false);
      }
      rec.recordings = {};
  },

  autoRecCapture(cm) {
      const rec = this._autoRec;
      if (!rec.armed) return;

      // Track current cursor line (may shift if others add/remove lines)
      rec.cursorLine = cm.getCursor().line;

      const cursor = cm.getCursor();
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
  },

  _autoRecShowIndicator(show) {
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
          el.textContent = '● REC';
          el.style.display = 'block';
      } else if (el) {
          el.style.display = 'none';
      }
  },

  _autoRecFinalize(cm, evaluateFn) {
      const rec = this._autoRec;
      const recordings = rec.recordings;
      const paramNames = Object.keys(recordings);
      if (paramNames.length === 0) return;

      // Sort position-based keys in reverse order so replacements don't shift offsets
      const sorted = paramNames.sort((a, b) => {
          const posA = a.startsWith('@pos') ? parseInt(a.slice(4)) : -1;
          const posB = b.startsWith('@pos') ? parseInt(b.slice(4)) : -1;
          return posB - posA; // reverse: replace from right to left
      });

      const line = cm.getLine(rec.cursorLine);
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
              // Named param: replace "param=VALUE" or "param=expression"
              const regex = new RegExp(param + '\\s*=\\s*(?:(?:linvar|sinvar|expvar|var)\\([^)]*(?:\\([^)]*\\))?[^)]*\\)|[\\d.\\-]+)');
              newLine = newLine.replace(regex, param + '=' + converted);
          }
      }

      if (newLine !== line) {
          cm.replaceRange(newLine,
              { line: rec.cursorLine, ch: 0 },
              { line: rec.cursorLine, ch: line.length }
          );
          if (evaluateFn) evaluateFn(cm, false);
      }
  },

  _autoRecRoundValue(val) {
      // Round to clean numbers
      if (Math.abs(val) >= 100) return Math.round(val / 50) * 50;
      if (Math.abs(val) >= 10) return Math.round(val / 5) * 5;
      if (Math.abs(val) >= 1) return Math.round(val * 10) / 10;
      return Math.round(val * 100) / 100;
  },

  _autoRecConvert(points, isDurationArg = false) {
      const values = points.map(p => this._autoRecRoundValue(p.value));
      const min = Math.min(...values);
      const max = Math.max(...values);

      // No real change — return static
      if (max - min < 0.01) return String(values[0]);

      // Find peaks and valleys with their timestamps
      const extremes = [{ value: values[0], time: points[0].time }];
      for (let i = 1; i < values.length - 1; i++) {
          const prev = values[i - 1];
          const curr = values[i];
          const next = values[i + 1];
          if ((curr >= prev && curr >= next && curr > prev) ||
              (curr <= prev && curr <= next && curr < prev)) {
              const last = extremes[extremes.length - 1];
              if (Math.abs(curr - last.value) > (max - min) * 0.15) {
                  extremes.push({ value: curr, time: points[i].time });
              }
          }
      }
      extremes.push({ value: values[values.length - 1], time: points[points.length - 1].time });

      // Deduplicate consecutive same values (keep latest timestamp)
      const unique = [extremes[0]];
      for (let i = 1; i < extremes.length; i++) {
          if (extremes[i].value !== unique[unique.length - 1].value) {
              unique.push(extremes[i]);
          }
      }

      // Compute durations between extremes and snap to musical grid
      const durations = [];
      for (let i = 1; i < unique.length; i++) {
          const raw = this._autoRecBeatDelta(unique[i - 1].time, unique[i].time);
          durations.push(raw);
      }
      const vals = unique.map(u => u.value);

      // Duration arg position — no TimeVars allowed, plain list only
      if (isDurationArg) {
          if (vals.length === 1) return String(vals[0]);
          return `[${vals.join(', ')}]`;
      }

      // Detect shape
      if (vals.length === 2) {
          return `linvar([${vals[0]}, ${vals[1]}], ${durations[0]})`;
      }

      if (vals.length === 3 && Math.abs(vals[0] - vals[2]) < (max - min) * 0.1) {
          // Symmetric — sinvar
          const totalDur = durations[0] + durations[1];
          return `sinvar([${vals[0]}, ${vals[1]}], ${totalDur})`;
      }

      // Check if all durations are the same (within tolerance)
      const avgDur = durations.reduce((a, b) => a + b, 0) / durations.length;
      const allSame = durations.every(d => Math.abs(d - avgDur) < 0.3);

      if (allSame) {
          // Equal spacing — single duration value
          return `linvar([${vals.join(', ')}], ${durations[0]})`;
      }

      // Varied timing — use duration array
      return `linvar([${vals.join(', ')}], [${durations.join(', ')}])`;
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

  _autoRecGetCurrentBeat() {
      // Read current beat from beat-64 div (format: "27/64")
      const beatEl = document.getElementById('beat-64');
      if (!beatEl) return 0;
      const beatText = beatEl.textContent.trim();
      const beatValue = parseInt(beatText.split('/')[0], 10);
      return beatValue;
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

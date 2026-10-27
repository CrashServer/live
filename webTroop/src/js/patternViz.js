/**
 * Pattern Visualization - Strudel/Gibber-inspired visualizations
 *
 * Features:
 * - Pianoroll: Scrolling timeline showing pattern notes
 * - Timeline: Linear progression with playhead
 * - Spiral: Circular pattern display
 * - Generators: Animated linvar/var/PWhite displays
 */

export class PatternViz {
  constructor() {
    this.container = null;
    this.canvas = null;
    this.ctx = null;
    this.enabled = false;
    this.players = [];
    this.beat = 0;
    this.bpm = 120;
    this.animationId = null;

    // Display options
    this.options = {
      cycles: 4,           // Number of cycles to display
      playheadPos: 0.25,   // Playhead position (0-1)
      colorActive: '#FFCA28',
      colorInactive: '#4a5568',
      colorPlayhead: '#ff3366',
      colorLinvar: '#8b5cf6',
      colorVar: '#10b981',
      backgroundColor: 'rgba(15, 15, 20, 0.95)',
      noteHeight: 8,
      rowGap: 4,
      showLabels: true,
      mode: 'pianoroll'    // 'pianoroll', 'timeline', 'spiral'
    };
  }

  init(containerId = 'pattern-viz') {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      this.container = document.createElement('div');
      this.container.id = containerId;
      document.body.appendChild(this.container);
    }

    // Check if canvas already exists
    this.canvas = this.container.querySelector('canvas');
    if (!this.canvas) {
      this.canvas = document.createElement('canvas');
      this.container.appendChild(this.canvas);
    }
    this.ctx = this.canvas.getContext('2d');

    this.resize();
    window.addEventListener('resize', () => this.resize());
  }

  resize() {
    if (!this.canvas || !this.container) return;
    const rect = this.container.getBoundingClientRect();
    if (rect.width === 0 || rect.height === 0) return;

    this.canvas.width = rect.width * window.devicePixelRatio;
    this.canvas.height = rect.height * window.devicePixelRatio;
    this.canvas.style.width = rect.width + 'px';
    this.canvas.style.height = rect.height + 'px';

    // Reset and scale context
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  enable() {
    this.enabled = true;
    if (this.container) {
      this.container.classList.add('active');
    }
    this.resize();
    this.animate();
  }

  disable() {
    this.enabled = false;
    if (this.container) {
      this.container.classList.remove('active');
    }
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
      this.animationId = null;
    }
  }

  setBeat(beat) {
    this.beat = beat;
  }

  setBpm(bpm) {
    this.bpm = bpm;
  }

  setPlayers(players) {
    this.players = players;
  }

  animate() {
    if (!this.enabled) return;

    this.render();
    this.animationId = requestAnimationFrame(() => this.animate());
  }

  render() {
    if (!this.ctx) return;

    const width = this.canvas.width / window.devicePixelRatio;
    const height = this.canvas.height / window.devicePixelRatio;

    // Clear
    this.ctx.fillStyle = this.options.backgroundColor;
    this.ctx.fillRect(0, 0, width, height);

    if (this.players.length === 0) {
      this.renderEmpty(width, height);
      return;
    }

    switch (this.options.mode) {
      case 'pianoroll':
        this.renderPianoroll(width, height);
        break;
      case 'timeline':
        this.renderTimeline(width, height);
        break;
      case 'spiral':
        this.renderSpiral(width, height);
        break;
    }
  }

  renderEmpty(width, height) {
    this.ctx.fillStyle = 'rgba(100, 100, 120, 0.5)';
    this.ctx.font = '12px monospace';
    this.ctx.textAlign = 'center';
    this.ctx.fillText('No active players', width / 2, height / 2);
  }

  // ===== Pianoroll Mode =====

  renderPianoroll(width, height) {
    const { cycles, playheadPos, colorActive, colorInactive, colorPlayhead } = this.options;
    const padding = 40;
    const availableWidth = width - padding * 2;
    const beatWidth = availableWidth / cycles;

    // Calculate visible beat range
    const currentBeat = this.beat;
    const startBeat = currentBeat - (cycles * playheadPos);
    const endBeat = startBeat + cycles;

    // Draw grid
    this.drawGrid(padding, 0, availableWidth, height, cycles);

    // Draw playhead
    const playheadX = padding + (playheadPos * availableWidth);
    this.ctx.strokeStyle = colorPlayhead;
    this.ctx.lineWidth = 2;
    this.ctx.beginPath();
    this.ctx.moveTo(playheadX, 0);
    this.ctx.lineTo(playheadX, height);
    this.ctx.stroke();

    // Playhead glow
    const gradient = this.ctx.createLinearGradient(playheadX - 20, 0, playheadX + 20, 0);
    gradient.addColorStop(0, 'rgba(255, 51, 102, 0)');
    gradient.addColorStop(0.5, 'rgba(255, 51, 102, 0.3)');
    gradient.addColorStop(1, 'rgba(255, 51, 102, 0)');
    this.ctx.fillStyle = gradient;
    this.ctx.fillRect(playheadX - 20, 0, 40, height);

    // Draw each player's pattern
    let yOffset = 20;
    const rowHeight = Math.min(60, (height - 40) / Math.max(1, this.players.length));

    this.players.forEach((player, playerIdx) => {
      const playerId = player.player || player.id;
      const patterns = player.patterns || {};
      const generators = player.generators || {};
      const current = player.current || {};
      const step = player.step || 0;

      // Player label
      this.ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
      this.ctx.font = 'bold 11px monospace';
      this.ctx.textAlign = 'left';
      this.ctx.fillText(playerId, 5, yOffset + rowHeight / 2 + 4);

      // Draw degree pattern or generator
      if (generators.degree) {
        this.renderGeneratorInPianoroll(
          generators.degree,
          padding, yOffset, availableWidth, rowHeight - 8,
          startBeat, endBeat, currentBeat, current.degree
        );
      } else if (patterns.degree && patterns.degree.length > 0) {
        this.renderPatternInPianoroll(
          patterns.degree,
          padding, yOffset, availableWidth, rowHeight - 8,
          startBeat, endBeat, step, player.patterns.dur
        );
      }

      yOffset += rowHeight;
    });
  }

  renderPatternInPianoroll(pattern, x, y, width, height, startBeat, endBeat, currentStep, durPattern) {
    const { colorActive, colorInactive, noteHeight } = this.options;
    const patternLength = pattern.length;
    const dur = durPattern ? durPattern[0] : 1;
    const beatWidth = width / (endBeat - startBeat);

    // Calculate min/max for vertical scaling
    const numericPattern = pattern.filter(v => typeof v === 'number');
    const minVal = Math.min(...numericPattern, 0);
    const maxVal = Math.max(...numericPattern, 7);
    const range = maxVal - minVal || 1;

    // Draw notes for visible range
    for (let beat = Math.floor(startBeat); beat < Math.ceil(endBeat); beat++) {
      const stepAtBeat = Math.floor(beat / dur) % patternLength;
      if (stepAtBeat < 0) continue;

      const noteValue = pattern[stepAtBeat];
      if (typeof noteValue !== 'number') continue;

      const noteX = x + (beat - startBeat) * beatWidth;
      const noteY = y + height - ((noteValue - minVal) / range) * (height - noteHeight);
      const noteWidth = Math.max(2, beatWidth * dur - 2);

      // Check if this is the current note
      const isActive = Math.abs(beat - this.beat) < dur && stepAtBeat === (currentStep % patternLength);

      this.ctx.fillStyle = isActive ? colorActive : colorInactive;
      this.ctx.beginPath();
      this.ctx.roundRect(noteX, noteY, noteWidth, noteHeight, 2);
      this.ctx.fill();

      // Glow for active
      if (isActive) {
        this.ctx.shadowColor = colorActive;
        this.ctx.shadowBlur = 10;
        this.ctx.fill();
        this.ctx.shadowBlur = 0;
      }
    }
  }

  renderGeneratorInPianoroll(gen, x, y, width, height, startBeat, endBeat, currentBeat, currentValue) {
    const type = gen.type;

    if (type === 'PWhite' || type === 'PRand' || type === 'PWalk') {
      this.renderRandomGeneratorInPianoroll(gen, x, y, width, height, currentValue);
    } else if (type === 'linvar') {
      this.renderLinvarInPianoroll(gen, x, y, width, height, startBeat, endBeat, currentBeat);
    } else if (type === 'var') {
      this.renderVarInPianoroll(gen, x, y, width, height, startBeat, endBeat, currentBeat);
    }
  }

  renderRandomGeneratorInPianoroll(gen, x, y, width, height, currentValue) {
    const lo = gen.lo ?? 0;
    const hi = gen.hi ?? 7;
    const range = hi - lo || 1;

    // Draw range band
    this.ctx.fillStyle = 'rgba(100, 100, 150, 0.2)';
    this.ctx.fillRect(x, y, width, height);

    // Draw dashed lines for bounds
    this.ctx.strokeStyle = 'rgba(150, 150, 180, 0.5)';
    this.ctx.setLineDash([4, 4]);
    this.ctx.beginPath();
    this.ctx.moveTo(x, y);
    this.ctx.lineTo(x + width, y);
    this.ctx.moveTo(x, y + height);
    this.ctx.lineTo(x + width, y + height);
    this.ctx.stroke();
    this.ctx.setLineDash([]);

    // Draw current value line
    if (currentValue !== undefined) {
      const valueY = y + height - ((currentValue - lo) / range) * height;
      this.ctx.strokeStyle = this.options.colorActive;
      this.ctx.lineWidth = 2;
      this.ctx.beginPath();
      this.ctx.moveTo(x, valueY);
      this.ctx.lineTo(x + width, valueY);
      this.ctx.stroke();

      // Value dot at playhead
      const playheadX = x + this.options.playheadPos * width;
      this.ctx.fillStyle = this.options.colorActive;
      this.ctx.beginPath();
      this.ctx.arc(playheadX, valueY, 6, 0, Math.PI * 2);
      this.ctx.fill();
    }

    // Label
    this.ctx.fillStyle = 'rgba(255, 200, 100, 0.8)';
    this.ctx.font = '10px monospace';
    this.ctx.fillText(`${gen.type}(${lo},${hi})`, x + 5, y + 12);
  }

  renderLinvarInPianoroll(gen, x, y, width, height, startBeat, endBeat, currentBeat) {
    const values = gen.values || [0, 1];
    const durs = gen.durs || [4];
    const totalDur = durs.reduce((a, b) => a + b, 0);
    const progress = gen.progress || 0;
    const current = gen.current;

    const minVal = Math.min(...values);
    const maxVal = Math.max(...values);
    const range = maxVal - minVal || 1;
    const beatWidth = width / (endBeat - startBeat);

    // Draw interpolation line
    this.ctx.strokeStyle = this.options.colorLinvar;
    this.ctx.lineWidth = 2;
    this.ctx.beginPath();

    let firstPoint = true;
    for (let beat = startBeat; beat <= endBeat; beat += 0.1) {
      // Calculate value at this beat
      const cyclePos = ((beat % totalDur) + totalDur) % totalDur;
      const segmentProgress = cyclePos / totalDur;

      // Linear interpolation
      const interpolatedValue = values[0] + (values[values.length - 1] - values[0]) * segmentProgress;

      const px = x + (beat - startBeat) * beatWidth;
      const py = y + height - ((interpolatedValue - minVal) / range) * height;

      if (firstPoint) {
        this.ctx.moveTo(px, py);
        firstPoint = false;
      } else {
        this.ctx.lineTo(px, py);
      }
    }
    this.ctx.stroke();

    // Draw gradient fill under line
    const gradient = this.ctx.createLinearGradient(0, y, 0, y + height);
    gradient.addColorStop(0, 'rgba(139, 92, 246, 0.3)');
    gradient.addColorStop(1, 'rgba(139, 92, 246, 0.05)');
    this.ctx.fillStyle = gradient;
    this.ctx.lineTo(x + width, y + height);
    this.ctx.lineTo(x, y + height);
    this.ctx.closePath();
    this.ctx.fill();

    // Current value marker
    if (current !== undefined) {
      const playheadX = x + this.options.playheadPos * width;
      const valueY = y + height - ((current - minVal) / range) * height;

      this.ctx.fillStyle = this.options.colorLinvar;
      this.ctx.beginPath();
      this.ctx.arc(playheadX, valueY, 6, 0, Math.PI * 2);
      this.ctx.fill();

      // Value label
      this.ctx.fillStyle = 'white';
      this.ctx.font = 'bold 10px monospace';
      this.ctx.fillText(current.toFixed(1), playheadX + 10, valueY + 4);
    }

    // Label
    this.ctx.fillStyle = 'rgba(139, 92, 246, 0.9)';
    this.ctx.font = '10px monospace';
    this.ctx.fillText(`linvar [${values.join('→')}]`, x + 5, y + 12);
  }

  renderVarInPianoroll(gen, x, y, width, height, startBeat, endBeat, currentBeat) {
    const values = gen.values || [];
    const durs = gen.durs || [];
    const currentIndex = gen.index || 0;
    const totalDur = durs.reduce((a, b) => a + b, 0) || values.length;
    const beatWidth = width / (endBeat - startBeat);

    const minVal = Math.min(...values.filter(v => typeof v === 'number'), 0);
    const maxVal = Math.max(...values.filter(v => typeof v === 'number'), 7);
    const range = maxVal - minVal || 1;

    // Draw stepped values
    let segmentStart = 0;
    for (let i = 0; i < values.length; i++) {
      const segmentDur = durs[i] || 1;
      const value = values[i];

      // Draw for each cycle in view
      for (let cycle = Math.floor(startBeat / totalDur) - 1; cycle <= Math.ceil(endBeat / totalDur); cycle++) {
        const beatStart = cycle * totalDur + segmentStart;
        const beatEnd = beatStart + segmentDur;

        if (beatEnd < startBeat || beatStart > endBeat) continue;

        const px1 = x + Math.max(0, (beatStart - startBeat)) * beatWidth;
        const px2 = x + Math.min(width, (beatEnd - startBeat) * beatWidth);
        const py = y + height - ((value - minVal) / range) * height;

        const isActive = i === currentIndex &&
          currentBeat >= beatStart && currentBeat < beatEnd;

        // Draw segment
        this.ctx.fillStyle = isActive ? this.options.colorVar : 'rgba(16, 185, 129, 0.4)';
        this.ctx.fillRect(px1, py - 4, px2 - px1 - 1, 8);

        // Step line
        this.ctx.strokeStyle = isActive ? this.options.colorVar : 'rgba(16, 185, 129, 0.6)';
        this.ctx.lineWidth = isActive ? 2 : 1;
        this.ctx.beginPath();
        this.ctx.moveTo(px1, py);
        this.ctx.lineTo(px2, py);
        this.ctx.stroke();
      }

      segmentStart += segmentDur;
    }

    // Label
    this.ctx.fillStyle = 'rgba(16, 185, 129, 0.9)';
    this.ctx.font = '10px monospace';
    this.ctx.fillText(`var [${values.join(',')}]`, x + 5, y + 12);
  }

  drawGrid(x, y, width, height, cycles) {
    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
    this.ctx.lineWidth = 1;

    // Beat lines
    const beatWidth = width / cycles;
    for (let i = 0; i <= cycles; i++) {
      const lineX = x + i * beatWidth;
      this.ctx.beginPath();
      this.ctx.moveTo(lineX, y);
      this.ctx.lineTo(lineX, height);
      this.ctx.stroke();
    }

    // Sub-beat lines (lighter)
    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    for (let i = 0; i < cycles * 4; i++) {
      const lineX = x + i * (beatWidth / 4);
      this.ctx.beginPath();
      this.ctx.moveTo(lineX, y);
      this.ctx.lineTo(lineX, height);
      this.ctx.stroke();
    }
  }

  // ===== Timeline Mode (simpler) =====

  renderTimeline(width, height) {
    // Similar to pianoroll but single row per player, more compact
    // TODO: implement if needed
    this.renderPianoroll(width, height);
  }

  // ===== Spiral Mode =====

  renderSpiral(width, height) {
    const centerX = width / 2;
    const centerY = height / 2;
    const maxRadius = Math.min(width, height) / 2 - 20;

    this.players.forEach((player, idx) => {
      const patterns = player.patterns || {};
      if (!patterns.degree || patterns.degree.length === 0) return;

      const pattern = patterns.degree;
      const step = player.step || 0;
      const radius = maxRadius - idx * 30;

      // Draw spiral
      const anglePerStep = (Math.PI * 2) / pattern.length;
      const currentAngle = ((step % pattern.length) / pattern.length) * Math.PI * 2 - Math.PI / 2;

      pattern.forEach((value, i) => {
        const angle = (i / pattern.length) * Math.PI * 2 - Math.PI / 2;
        const isActive = i === (step % pattern.length);

        const noteRadius = radius - 10 + (value / 12) * 20;
        const x = centerX + Math.cos(angle) * noteRadius;
        const y = centerY + Math.sin(angle) * noteRadius;

        this.ctx.fillStyle = isActive ? this.options.colorActive : this.options.colorInactive;
        this.ctx.beginPath();
        this.ctx.arc(x, y, isActive ? 6 : 4, 0, Math.PI * 2);
        this.ctx.fill();

        if (isActive) {
          this.ctx.shadowColor = this.options.colorActive;
          this.ctx.shadowBlur = 15;
          this.ctx.fill();
          this.ctx.shadowBlur = 0;
        }
      });

      // Player label
      this.ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
      this.ctx.font = '11px monospace';
      this.ctx.textAlign = 'center';
      this.ctx.fillText(player.player || player.id, centerX, centerY + radius + 15);
    });
  }

  setMode(mode) {
    this.options.mode = mode;
  }

  setOption(key, value) {
    this.options[key] = value;
  }
}

// Singleton
export const patternViz = new PatternViz();

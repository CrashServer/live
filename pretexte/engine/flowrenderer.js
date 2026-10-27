// Flow renderer — the actual pretext magic.
//
// Uses pretext's `layoutNextLine` in a loop with a DIFFERENT maxWidth per
// line, computed from an obstacle's position at each y. The obstacle is
// an SVG circle that moves vertically with a sine wave. Text wraps around
// it in real time because every frame we re-run the layout.
//
// This is the one thing CSS genuinely cannot do.

import { prepareWithSegments, layoutNextLine } from '@chenglou/pretext';

const NS = 'http://www.w3.org/2000/svg';
const OBSTACLE_R = 140;
const SINE_PERIOD_S = 4.0;
const SINE_AMPLITUDE = 260;

let svg = null;
let circle = null;
let startTime = 0;
let currentCy = 0;

const lineElements = new Map();  // lineIdx → HTMLDivElement

export function enableFlow() {
  svg = document.createElementNS(NS, 'svg');
  svg.id = 'flow-svg';
  svg.setAttribute('preserveAspectRatio', 'none');
  svg.style.cssText = 'position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:5;';

  circle = document.createElementNS(NS, 'circle');
  circle.setAttribute('r', OBSTACLE_R);
  circle.setAttribute('fill', 'rgba(255, 180, 80, 0.18)');
  circle.setAttribute('stroke', 'rgba(255, 200, 120, 0.9)');
  circle.setAttribute('stroke-width', '2');
  svg.appendChild(circle);

  document.body.appendChild(svg);
  startTime = performance.now();
  currentCy = window.innerHeight / 2;
}

export function disableFlow() {
  if (svg) { svg.remove(); svg = null; circle = null; }
  for (const el of lineElements.values()) el.remove();
  lineElements.clear();
  const container = document.getElementById('code-container');
  if (container) container.style.minHeight = '';
}

export function tickFlow() {
  if (!circle) return;
  const t = (performance.now() - startTime) / 1000;
  const cx = window.innerWidth / 2;
  currentCy = window.innerHeight / 2 + Math.sin(t * (Math.PI * 2 / SINE_PERIOD_S)) * SINE_AMPLITUDE;
  circle.setAttribute('cx', cx);
  circle.setAttribute('cy', currentCy);
}

export function renderFlow(container, sourceText, font, containerWidth, lineHeight) {
  if (!sourceText) {
    for (const el of lineElements.values()) el.remove();
    lineElements.clear();
    return;
  }

  const prepared = prepareWithSegments(sourceText, font, { whiteSpace: 'pre-wrap' });

  const cx = window.innerWidth / 2;
  const r = OBSTACLE_R;
  const containerRect = container.getBoundingClientRect();

  container.style.position = 'relative';
  container.style.minHeight = '100vh';

  // Compute left-column width at a given viewport Y.
  // When the obstacle overlaps this y, we shrink maxWidth so the line
  // lives in the free space to the LEFT of the obstacle.
  function maxWidthAtViewportY(viewportY) {
    const dy = Math.abs(viewportY - currentCy);
    if (dy >= r) return containerWidth;
    const chord = Math.sqrt(r * r - dy * dy);
    const orbLeft = cx - chord;
    const freeLeftW = orbLeft - containerRect.left - 24;  // 24px breathing room
    return Math.max(60, freeLeftW);
  }

  let cursor = { segmentIndex: 0, graphemeIndex: 0 };
  let y = 0;
  let lineIdx = 0;
  const seen = new Set();

  while (true) {
    const viewportY = containerRect.top + y + lineHeight / 2;
    const mw = maxWidthAtViewportY(viewportY);

    const line = layoutNextLine(prepared, cursor, mw);
    if (!line) break;

    seen.add(lineIdx);

    let el = lineElements.get(lineIdx);
    if (!el) {
      el = document.createElement('div');
      el.className = 'flow-line';
      container.appendChild(el);
      lineElements.set(lineIdx, el);
    }
    el.textContent = line.text;
    el.style.cssText = [
      'position:absolute',
      `top:${y}px`,
      'left:0',
      `max-width:${mw}px`,
      'white-space:pre',
    ].join(';');

    // Advance cursor; bail if pretext didn't advance (shouldn't happen, but safe)
    if (line.end.segmentIndex === cursor.segmentIndex &&
        line.end.graphemeIndex === cursor.graphemeIndex) break;
    cursor = line.end;
    y += lineHeight;
    lineIdx++;

    if (y > window.innerHeight * 2) break;  // safety cap
  }

  // Remove lines beyond the current layout
  for (const [idx, el] of [...lineElements]) {
    if (!seen.has(idx)) { el.remove(); lineElements.delete(idx); }
  }
}

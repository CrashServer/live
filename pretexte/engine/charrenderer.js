// Character renderer.
//
// Takes a CharRecord[] from charlayout.js and materializes them as
// absolute-positioned DOM spans inside a container. Reuses spans by ID
// across re-renders so CSS transitions can animate each char's x/y smoothly.
//
// Each span carries data attributes for effects to read:
//   data-char-id     — stable ID (index in visible char stream)
//   data-char        — the glyph
//   data-line-index  — which line the char is on
// Effects can select them with: container.querySelectorAll('.char')

import { layoutCharacters } from './charlayout.js';

const spansById = new Map();  // id → HTMLSpan

/**
 * Render characters into a container. Uses absolute positioning; sets
 * container to `position: relative` and the container's height to the
 * layout height so the outer container auto-sizes.
 *
 * @param {HTMLElement} container — the element to render into
 * @param {string} sourceText
 * @param {string} font
 * @param {number} maxWidth
 * @param {number} lineHeight
 * @param {object} ctx — optional per-char annotation context:
 *   { activeLines: Set<number>, zbdmCursor: {line, ch}, svdkCursor: {line, ch},
 *     windowStartLine: number }
 */
export function renderCharacters(container, sourceText, font, maxWidth, lineHeight, ctx = {}) {
  const layout = layoutCharacters(sourceText, font, maxWidth, lineHeight);

  // Prepare container
  container.style.position = 'relative';
  container.style.minHeight = `${layout.height}px`;

  const seen = new Set();

  for (const rec of layout.chars) {
    seen.add(rec.id);
    let span = spansById.get(rec.id);
    if (!span) {
      span = document.createElement('span');
      span.className = 'char';
      container.appendChild(span);
      spansById.set(rec.id, span);
    }

    // Update content (char may change across layouts even at same id)
    if (span.dataset.char !== rec.char) {
      span.textContent = rec.char;
      span.dataset.char = rec.char;
    }
    span.dataset.charId    = rec.id;
    span.dataset.lineIndex = rec.lineIndex;
    // Base x/y as CSS vars so effects can compose: CSS reads --base-x,
    // --base-y PLUS effect-provided --wobble-y, --glitch-x, etc.
    span.style.setProperty('--base-x', `${rec.x.toFixed(1)}px`);
    span.style.setProperty('--base-y', `${rec.y.toFixed(1)}px`);

    // Mark active line chars (for CSS targeting + effects)
    const isActive = ctx.activeLines && ctx.activeLines.has(rec.lineIndex);
    if (isActive) span.classList.add('active');
    else          span.classList.remove('active');
  }

  // Remove spans that are no longer in the layout
  for (const [id, span] of [...spansById]) {
    if (!seen.has(id)) {
      span.remove();
      spansById.delete(id);
    }
  }

  return layout;
}

/** Clear everything (e.g., when leaving char-mode). */
export function clearCharRenderer() {
  for (const span of spansById.values()) span.remove();
  spansById.clear();
}

/** Read-only view of the current character map (for effects). */
export function getCharSpans() {
  return spansById;
}

/** Remove a single char from DOM AND registry — used by erode-style effects
 *  that want the char to stay gone until the source text re-renders. */
export function removeCharSpan(id) {
  const span = spansById.get(id);
  if (span) {
    span.remove();
    spansById.delete(id);
  }
}

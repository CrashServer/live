// Character-layout engine.
//
// Takes source text, runs pretext's prepareWithSegments + layoutWithLines,
// and returns per-character records with explicit x/y positions.
// Each character gets a stable ID (index in the visible char stream) that
// survives reflow at different widths — the foundation for per-char effects
// like morph, trails, explode, audio-wobble.
//
// Pretext gives us line widths and break points but NOT per-character x
// within a line. We compute those via canvas.measureText, cached per (char, font).

import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext';

const widthCache = new Map();  // `${font}::${ch}` → width
let measureCtx = null;

function ensureCtx() {
  if (!measureCtx) {
    const cvs = document.createElement('canvas');
    measureCtx = cvs.getContext('2d');
  }
  return measureCtx;
}

function charWidth(ch, font) {
  const key = font + '::' + ch;
  let w = widthCache.get(key);
  if (w === undefined) {
    const ctx = ensureCtx();
    ctx.font = font;
    w = ctx.measureText(ch).width;
    widthCache.set(key, w);
  }
  return w;
}

/**
 * Lay out source text into character records.
 * @param {string} sourceText — full text to lay out (one or more \n-separated lines)
 * @param {string} font — CSS font shorthand, e.g. "48px InterBlack"
 * @param {number} maxWidth — wrap width in px
 * @param {number} lineHeight — line height in px
 * @returns {{chars: Array<CharRecord>, lineCount: number, height: number, widestLine: number}}
 *
 * CharRecord = { id, char, x, y, lineIndex, localIndex }
 *   id         — stable ID (index in visible char stream, survives reflow)
 *   char       — the glyph
 *   x, y       — absolute position within the layout box (px)
 *   lineIndex  — which line (0-based)
 *   localIndex — position within the line (0-based)
 */
export function layoutCharacters(sourceText, font, maxWidth, lineHeight) {
  if (!sourceText || maxWidth <= 0) {
    return { chars: [], lineCount: 0, height: 0, widestLine: 0 };
  }

  const prepared = prepareWithSegments(sourceText, font, { whiteSpace: 'pre-wrap' });
  const result   = layoutWithLines(prepared, maxWidth, lineHeight);

  const chars = [];
  let id = 0;
  let widestLine = 0;

  result.lines.forEach((line, lineIndex) => {
    const y = lineIndex * lineHeight;
    let x = 0;
    // Array.from handles most multi-code-unit characters reasonably for ASCII code
    for (const ch of Array.from(line.text)) {
      chars.push({
        id,
        char:       ch,
        x,
        y,
        lineIndex,
        localIndex: id,   // for now same as id; may diverge if we diff across source edits
      });
      id++;
      x += charWidth(ch, font);
    }
    if (line.width > widestLine) widestLine = line.width;
  });

  return { chars, lineCount: result.lineCount, height: result.height, widestLine };
}

/** Clear the measureText width cache (e.g., on font change). */
export function clearCharLayoutCache() { widthCache.clear(); }

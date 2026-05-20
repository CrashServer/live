// Content-diff eval flash: when a line's text changes (new eval, typing, etc),
// briefly animate that line. Uses a per-line text snapshot; diff each frame.

const lastText = new Map();  // lineNumber → text

export const evalFlash = {
  id: 'eval-flash',

  enable() {
    document.body.classList.add('fx-eval-flash');
    lastText.clear();
  },

  disable() {
    document.body.classList.remove('fx-eval-flash');
    lastText.clear();
    for (const ln of document.querySelectorAll('.code-line.eval-hit')) {
      ln.classList.remove('eval-hit');
    }
  },

  tick() {
    const lines = document.querySelectorAll('.code-line');
    const seen = new Set();

    lines.forEach(ln => {
      const num = ln.dataset.lineNumber;
      if (!num) return;
      seen.add(num);
      const text = ln.textContent || '';
      const prev = lastText.get(num);
      if (prev !== undefined && prev !== text) {
        // Re-trigger CSS animation: remove + reflow + add
        ln.classList.remove('eval-hit');
        void ln.offsetWidth;  // force reflow
        ln.classList.add('eval-hit');
      }
      lastText.set(num, text);
    });

    // Clean up entries for lines no longer in DOM (window scrolled)
    for (const k of [...lastText.keys()]) {
      if (!seen.has(k)) lastText.delete(k);
    }
  },
};

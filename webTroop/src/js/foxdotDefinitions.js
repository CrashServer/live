import CodeMirror from 'codemirror';

const definitions = {
    PRand: '(start, stop=None, **kwargs)', PWhite: '(lo=0, hi=1, **kwargs)', PxRand: '(start, stop=None, **kwargs)', PwRand: '(values, weights, **kwargs)', PChain: '(mapping, **kwargs)', PZ12: '(tokens=[1, 0], p=[1, 0.5])', PTree: '(n=0, f=<function PTree.<lambda> at 0x7a8b0ad8fba0>, choose=<function PTree.<lambda> at 0x7a8b0ad8fc40>, **kwargs)', PWalk: '(max=7, step=1, start=0, **kwargs)', PDelta: '(deltas, start=0)', PSquare: '(**kwargs)', PIndex: '(**kwargs)', PFibMod: '(**kwargs)', PShuf: '(seq)', PAlt: '(pat1, pat2, *patN)', PStretch: '(seq, size)', PPairs: '(seq, func=<function <lambda> at 0x7a8b0ada8a40>)', PZip: '(pat1, pat2, *patN)', PZip2: '(pat1, pat2, rule=<function <lambda> at 0x7a8b0ada8c20>)', PStutter: '(x, n=2)', PSq: '(a=1, b=2, c=3)', P10: '(n)', PStep: '(n, value, default=0, offset=0)', PSum: '(n, total, **kwargs)', PRange: '(start, stop=None, step=1)', PTri: '(start, stop=None, step=1)', PSine: '(n=16)', PEuclid: '(n, k)', PEuclid2: '(n, k, lo, hi)', PBern: '(size=16, ratio=0.5)', PBeat: '(string, start=0, dur=0.5)', PDur: '(n, k, start=0, dur=0.25)', PDelay: '(*args)', PStrum: '(n=4)', PQuicken: '(dur=0.5, stepsize=3, steps=6)', PRhythm: '(durations)', PJoin: '(patterns)', linvar: '(values, dur=None, start=0, **kwargs)', expvar: '(values, dur=None, start=0, **kwargs)', sinvar: '(values, dur=None, start=0, **kwargs)', Pvar: '(values, dur=None, **kwargs)', PBin: '(number=0)', PSaw: '(n=16, inverse=0)', PTime: '()', PTimebin: '()', PFrac: '(a=0.63, b=0.0, size=16, mapl=0, maph=1)', PFr: '(mapl=0, maph=1, seedFr=1664, size=16)', lininf: '(start=0, finish=1, time=32)', expinf: '(start=0, finish=1, time=32)', linbpm: '(endBpm=170, durBpm=128)', linmod: '(start, end, duration, default=0)', PDrum: "(style=None, pat='', listen=False, khsor='', duree=0.5, spl=0, charPlayer='d')", PChords: '(chord=None, **kwargs)', PGauss: '(mean=0, deviation=1, **kwargs)', PLog: '(mean=0, deviation=1, **kwargs)', PTrir: '(low=0, high=8, mode=None, **kwargs)', PCoin: '(low=0, high=1, proba=0.5, **kwargs)', PChar: '(case=2, alpha=2, **kwargs)', PMarkov: "(init_value='', **kwargs)", PZero: '(size=2, offset=0)', PBool: '(pat1=P[0], pat2=P[0], operator=0)', PRy: '(total=16, div=4, restProb=0)'
};

function showDefinition(cm) {
  const cursor = cm.getCursor();
  const token = cm.getTokenAt(cursor);
  const word = token.string;
  console.log(word);

  if (definitions[word]) {
    const definition = definitions[word];
    const tooltip = makeTooltip(cm, cursor, definition);
    setTimeout(() => removeTooltip(tooltip), 10000); // Remove tooltip after 3 seconds
  }
}

function makeTooltip(cm, pos, content) {
  const tooltip = document.createElement('div');
  tooltip.className = 'CodeMirror-tooltip';
  tooltip.style.left = `${cm.cursorCoords(pos, 'page').left}px`;
  tooltip.style.top = `${cm.cursorCoords(pos, 'page').bottom}px`;
  tooltip.textContent = content;
  document.body.appendChild(tooltip);
  return tooltip;
}

function removeTooltip(tooltip) {
  if (tooltip && tooltip.parentNode) {
    tooltip.parentNode.removeChild(tooltip);
  }
}

export { showDefinition };
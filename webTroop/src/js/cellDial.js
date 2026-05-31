/* cellDial.js — Radial cell picker  (Ctrl+Shift+G)
 *
 * Portrait panel, ring-dominant, four domains:
 *   CELLS   — A-Z columns, brightness = compat score
 *   ATTACKS — genre/style from attack_category field
 *   PARTS   — #@ sections live from editor
 *   ALL     — flat search, no ring
 *
 * Keys:
 *   Tab / Shift+Tab       → cycle domain
 *   A-Z (CELLS, empty)   → column filter
 *   1-9 (empty input)    → pick Nth visible result
 *   ↑ / ↓               → navigate
 *   Enter                → paste (PARTS: jump to section)
 *   Shift+Enter          → paste + eval
 *   Backspace (empty)    → clear filter
 *   Esc                  → close
 *   ~120                 → filter by BPM ±10
 *   @em                  → filter by key
 */

import { EventEmitter } from "./eventBus.js";
import "../css/cellDial.css";

// Use relative URL so it goes through Vite's proxy (/api → localhost:1235).
// When the grid server is not running the proxy falls back to serving
// cells.json from disk (configured in vite.config.js).
const GRID_API  = "/api/cells";
const CACHE_TTL = 30_000;
const PAGE_SIZE = 7;
const NS = "http://www.w3.org/2000/svg";

// Ring geometry (viewBox -155 -155 310 310)
const OUTER     = 130;
const INNER     = 82;
const ACT_OUTER = 143;
const ACT_INNER = 68;
const DOT_R     = 62;   // cell dot ring radius

const DOMAINS = ["CELLS", "ATTACKS", "PARTS", "ALL"];

const COL_ROLE = {
  A:"pad",   B:"bass",  C:"kick",  D:"snare", E:"hat",
  F:"loop",  G:"lead",  H:"lead2", I:"stab",  J:"acid",
  K:"tex",   L:"vox",   M:"bell",  N:"atmo",  O:"fx",
  P:"misc",  Q:"trk",   R:"trk",   S:"trk",   T:"trk",
  U:"trk",   V:"trk",   W:"trk",   X:"trk",   Y:"trk",  Z:"trk",
};

// ---- Module state -----------------------------------------------

let _editor      = null;
let _getSections = null;
let _open        = false;
let _domain      = 0;
let _colFilter   = null;
let _results     = [];
let _selIdx      = 0;
let _pageStart   = 0;
let _state       = { ctx: {}, cols: [], allItems: [], attacks: [], parts: [] };

// ---- Cell cache -------------------------------------------------

let _cache     = null;
let _cacheTime = 0;

async function fetchCells() {
  const now = Date.now();
  if (_cache && now - _cacheTime < CACHE_TTL) return _cache;
  try {
    const r = await fetch(GRID_API);
    if (!r.ok) throw new Error(r.status);
    _cache = await r.json();
    _cacheTime = now;
  } catch (e) {
    console.warn("[cellDial] fetch failed:", e);
    _cache = _cache ?? {};
  }
  return _cache;
}

// ---- Score helpers ----------------------------------------------

function _blocks(score) {
  const n = Math.round(score * 8);
  return "█".repeat(n) + "░".repeat(8 - n);
}

const NOTE_NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
const NOTE_ALT   = {Db:"C#",Eb:"D#",Fb:"E",Gb:"F#",Ab:"G#",Bb:"A#",Cb:"B"};

function _noteIdx(n) {
  if (!n) return -1;
  const s = n.charAt(0).toUpperCase() + n.slice(1);
  return NOTE_NAMES.indexOf(NOTE_ALT[s] ?? s);
}

function keyScore(k1, k2) {
  if (!k1 || !k2) return 0.5;
  const p1 = k1.split(/\s+/), p2 = k2.split(/\s+/);
  const s1 = (p1[1] || "minor").toLowerCase();
  const s2 = (p2[1] || "minor").toLowerCase();
  const r1 = _noteIdx(p1[0]), r2 = _noteIdx(p2[0]);
  if (r1 < 0 || r2 < 0) return 0.5;
  const dist = Math.min(Math.abs(r1 - r2), 12 - Math.abs(r1 - r2));
  if (r1 === r2 && s1 === s2) return 1.0;
  if (r1 === r2) return (s1 === "major") !== (s2 === "major") ? 0.6 : 0.75;
  if (dist === 3) return 0.85;
  if (dist === 5 || dist === 7) return 0.55;
  if (dist <= 2) return 0.35;
  return 0.1;
}

function tempoScore(t1, t2) {
  if (!t1 || !t2) return 0.5;
  const d = Math.abs(t1 - t2);
  if (d === 0) return 1.0;
  if (d <= 5)  return 0.9;
  if (d <= 10) return 0.75;
  if (d <= 20) return 0.5;
  if (d <= 30) return 0.3;
  const ratio = Math.max(t1, t2) / Math.min(t1, t2);
  if (Math.abs(ratio - 2) < 0.1) return d <= 10 ? 0.55 : 0.3;
  return 0.1;
}

function cellScore(cell, ctx) {
  return (keyScore(ctx.key, cell.key) + tempoScore(ctx.bpm, cell.tempo)) / 2;
}

function detectContext(text) {
  const bpmM   = text.match(/Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)/);
  const scaleM = text.match(/Scale\.default\s*=\s*["']([^"']+)/);
  const rootM  = text.match(/Root\.default\s*=\s*["']?([A-Za-z#b]+)/);
  const bpm    = bpmM  ? +bpmM[1]  : null;
  const scale  = scaleM ? scaleM[1] : null;
  const root   = rootM  ? rootM[1]  : null;
  const key    = (root && scale) ? `${root} ${scale}` : (root ?? scale ?? null);
  return { bpm, key };
}

// ---- Attack category normalization ------------------------------

function _normalizeAttack(raw) {
  if (!raw || raw.includes(".py") || raw.includes("—")) return null;
  const token = raw.split(/[,#]/)[0].trim().toLowerCase();
  return token.length >= 2 ? token : null;
}

// ---- SVG helpers ------------------------------------------------

function _arcPath(rOut, rIn, a0, a1) {
  const ox0 = Math.cos(a0)*rOut, oy0 = Math.sin(a0)*rOut;
  const ox1 = Math.cos(a1)*rOut, oy1 = Math.sin(a1)*rOut;
  const ix0 = Math.cos(a1)*rIn,  iy0 = Math.sin(a1)*rIn;
  const ix1 = Math.cos(a0)*rIn,  iy1 = Math.sin(a0)*rIn;
  const lg  = (a1 - a0 > Math.PI) ? 1 : 0;
  return `M${ox0},${oy0} A${rOut},${rOut} 0 ${lg} 1 ${ox1},${oy1} `
       + `L${ix0},${iy0} A${rIn},${rIn} 0 ${lg} 0 ${ix1},${iy1} Z`;
}

function _svgText(cls, x, y, text) {
  const t = document.createElementNS(NS, "text");
  t.setAttribute("x", x); t.setAttribute("y", y);
  t.setAttribute("text-anchor", "middle");
  t.setAttribute("dominant-baseline", "central");
  t.setAttribute("class", cls);
  t.textContent = text;
  return t;
}

// ---- Ring build -------------------------------------------------

function _buildRing(svg, segments, activeKey) {
  svg.innerHTML = "";

  if (!segments.length) {
    // ALL domain or empty — decorative circles + center label
    _addRingOutline(svg);
    _buildCenterText(svg, activeKey, segments);
    return;
  }

  const n     = segments.length;
  const gap   = Math.min(0.05, (2 * Math.PI / n) * 0.07);
  const step  = (2 * Math.PI) / n;
  const off   = -Math.PI / 2;
  const fsize = n > 20 ? 7 : n > 12 ? 8 : 10;
  const mchars = n > 20 ? 1 : n > 12 ? 3 : 4;

  segments.forEach((seg, i) => {
    const a0  = off + i * step + gap / 2;
    const a1  = off + (i + 1) * step - gap / 2;
    const mid = (a0 + a1) / 2;
    const isActive = seg.key === activeKey;
    const ro = isActive ? ACT_OUTER : OUTER;
    const ri = isActive ? ACT_INNER : INNER;

    const path = document.createElementNS(NS, "path");
    path.setAttribute("d", _arcPath(ro, ri, a0, a1));
    path.setAttribute("class", "ring-slice" + (isActive ? " ring-active" : ""));
    path.setAttribute("data-key", seg.key);
    path.style.opacity = String(0.12 + (seg.score ?? 0.5) * 0.88);
    path.addEventListener("click", () => _handleSegmentClick(seg.key));
    svg.appendChild(path);

    const lr  = (ro + ri) / 2;
    const lx  = Math.cos(mid) * lr;
    const ly  = Math.sin(mid) * lr;
    const txt = _svgText(
      "ring-label" + (isActive ? " ring-label-active" : ""),
      lx, ly,
      seg.label.slice(0, mchars)
    );
    txt.setAttribute("font-size", fsize);
    txt.addEventListener("click", () => _handleSegmentClick(seg.key));
    svg.appendChild(txt);
  });

  // Cell dots along inner edge of active segment (CELLS domain)
  if (_domain === 0 && activeKey) {
    const si = segments.findIndex(s => s.key === activeKey);
    if (si >= 0) {
      const a0    = off + si * step + gap / 2;
      const a1    = off + (si + 1) * step - gap / 2;
      const items = _state.cols.find(c => c.letter === activeKey)?.items ?? [];
      const nDots = Math.min(items.length, 14);
      for (let d = 0; d < nDots; d++) {
        const da = a0 + (a1 - a0) * (d + 0.5) / nDots;
        const dot = document.createElementNS(NS, "circle");
        dot.setAttribute("cx", Math.cos(da) * DOT_R);
        dot.setAttribute("cy", Math.sin(da) * DOT_R);
        dot.setAttribute("r", 2.5);
        dot.setAttribute("class", "ring-dot");
        svg.appendChild(dot);
      }
    }
  }

  _buildCenterText(svg, activeKey, segments);
}

function _addRingOutline(svg) {
  [OUTER, INNER].forEach((r, i) => {
    const c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", 0); c.setAttribute("cy", 0); c.setAttribute("r", r);
    c.setAttribute("fill", "none");
    c.setAttribute("class", i === 0 ? "ring-outline-outer" : "ring-outline-inner");
    svg.appendChild(c);
  });
}

function _buildCenterText(svg, activeKey, segments) {
  const lines = [];

  if (_domain === 3) {
    lines.push({ text: "ALL", cls: "rct-domain" });
    lines.push({ text: `${_state.allItems.length}`, cls: "rct-count" });
  } else if (activeKey) {
    if (_domain === 0) {
      const col = _state.cols.find(c => c.letter === activeKey);
      lines.push({ text: activeKey, cls: "rct-key" });
      lines.push({ text: COL_ROLE[activeKey] ?? "?", cls: "rct-role" });
      if (col) lines.push({ text: `${col.count}`, cls: "rct-count" });
    } else if (_domain === 1) {
      const atk = _state.attacks.find(a => a.key === activeKey);
      lines.push({ text: activeKey.slice(0, 8), cls: "rct-key" });
      if (atk) lines.push({ text: `${atk.count}`, cls: "rct-count" });
    } else if (_domain === 2) {
      const part = _state.parts.find(p => p.key === activeKey);
      lines.push({ text: activeKey.slice(0, 8), cls: "rct-key" });
      if (part?.beats) lines.push({ text: `${part.beats}b`, cls: "rct-role" });
    }
  } else {
    // No active filter — show context
    const ctx = _state.ctx;
    if (ctx.bpm || ctx.key) {
      if (ctx.bpm) lines.push({ text: `${ctx.bpm}`, cls: "rct-key" });
      if (ctx.key) lines.push({ text: ctx.key.split(" ")[0], cls: "rct-role" });
    } else {
      lines.push({ text: DOMAINS[_domain], cls: "rct-domain" });
    }
  }

  const lineH  = 20;
  const totalH = lines.length * lineH;
  const startY = -(totalH - lineH) / 2;

  lines.forEach((l, i) => {
    svg.appendChild(_svgText(l.cls, 0, startY + i * lineH, l.text));
  });
}

// ---- DOM bootstrap ----------------------------------------------

function _buildDom() {
  if (document.getElementById("cellDial")) return;

  const el = document.createElement("div");
  el.id = "cellDial";
  el.className = "cell-dial hidden";
  el.innerHTML = `
    <div class="cell-dial-backdrop"></div>
    <div class="cell-dial-panel">
      <div class="cd-tabs" id="cdTabs">
        ${DOMAINS.map((d, i) => `<button class="cd-tab${i===0?" active":""}" data-domain="${i}">${d}</button>`).join("")}
      </div>
      <div class="cd-ring-wrap" id="cdRingWrap">
        <svg class="cell-dial-ring" id="cellDialRing"
             viewBox="-155 -155 310 310" aria-hidden="true"></svg>
        <div class="cd-parts-list hidden" id="cdPartsList"></div>
      </div>
      <div class="cd-ctx-chips hidden" id="cdCtxChips"></div>
      <div class="cd-search-row">
        <span class="cd-prompt">›</span>
        <span class="cd-filter-tag hidden" id="cdColTag"></span>
        <input id="cellDialSearch" class="cell-dial-search"
               placeholder="search…" autocomplete="off"
               spellcheck="false" aria-label="cell search">
        <span class="cd-count" id="cdCount"></span>
      </div>
      <div id="cellDialResults" class="cd-results" role="listbox"></div>
      <div class="cd-footer">
        [Tab] domain · [A–Z] col · [1–9] pick · ~bpm · @key · [↵] paste · [⇧↵] eval · [⎋] close
      </div>
    </div>
  `;
  document.body.appendChild(el);

  el.querySelector(".cell-dial-backdrop").addEventListener("click", close);
  el.querySelector("#cdTabs").addEventListener("click", e => {
    const btn = e.target.closest(".cd-tab");
    if (btn) _setDomain(+btn.dataset.domain);
  });

  const input = el.querySelector("#cellDialSearch");
  input.addEventListener("input", e => { _runFilter(e.target.value); _updateChipActiveState(); });
  input.addEventListener("keydown", _onInputKey);
}

// ---- Open / close -----------------------------------------------

async function open() {
  if (_open) return;
  _open      = true;
  _domain    = 0;
  _colFilter = null;
  _pageStart = 0;

  const overlay = document.getElementById("cellDial");
  overlay.classList.remove("hidden");
  _updateTabs();

  const input = document.getElementById("cellDialSearch");
  input.value       = "";
  input.placeholder = "search col…";
  document.getElementById("cdColTag").classList.add("hidden");
  input.focus();

  const text = _editor ? _editor.getValue() : "";
  const ctx  = detectContext(text);

  const cells = await fetchCells();
  _buildState(cells, ctx);
}

function close() {
  if (!_open) return;
  _open = false;
  document.getElementById("cellDial").classList.add("hidden");
  if (_editor) _editor.focus();
}

// ---- State build ------------------------------------------------

function _buildState(cells, ctx) {
  const colMap    = {};
  const allItems  = [];
  const attackMap = {};

  Object.entries(cells).forEach(([coord, cell]) => {
    if (!cell || typeof cell !== "object") return;
    const letter = coord.charAt(0).toUpperCase();
    if (!colMap[letter]) colMap[letter] = { letter, items: [] };
    const score = cellScore(cell, ctx);
    const label = cell.label || coord;
    const item  = { coord, cell, score, label };
    colMap[letter].items.push(item);
    allItems.push(item);

    const atk = _normalizeAttack(cell.attack_category);
    if (atk) {
      if (!attackMap[atk]) attackMap[atk] = { key: atk, items: [] };
      attackMap[atk].items.push(item);
    }
  });

  const cols = Object.values(colMap).sort((a, b) => a.letter.localeCompare(b.letter));
  cols.forEach(col => {
    col.count       = col.items.length;
    col.compatRatio = col.items.reduce((s, i) => s + i.score, 0) / col.items.length;
  });

  // Sort by count desc, cap at 16 so the ring stays readable (3-char labels)
  const attacks = Object.values(attackMap)
    .sort((a, b) => b.items.length - a.items.length)
    .slice(0, 16);
  attacks.forEach(atk => {
    atk.count = atk.items.length;
    atk.score = atk.items.reduce((s, i) => s + i.score, 0) / atk.items.length;
  });

  _state     = { ctx, cols, allItems, attacks, parts: _buildParts() };
  _colFilter = null;
  _pageStart = 0;
  _updateContextChips(ctx);
  _refreshRing();
  _runFilter("");
}

function _buildParts() {
  if (!_getSections) return [];
  return (_getSections() ?? [])
    .filter(s => s.type === "section")
    .map(s => ({ key: s.name, label: s.name, score: 0.5, beats: s.beats, line: s.line }));
}

// ---- Domain switch ----------------------------------------------

function _setDomain(d) {
  _domain    = d;
  _colFilter = null;
  _pageStart = 0;
  _updateTabs();
  document.getElementById("cdColTag").classList.add("hidden");
  const input = document.getElementById("cellDialSearch");
  input.value       = "";
  input.placeholder = ["search col…", "filter attacks…", "jump to part…", "search all…"][d];

  if (d === 2) _state = { ..._state, parts: _buildParts() };

  _refreshRing();
  _runFilter("");
}

function _updateTabs() {
  document.querySelectorAll(".cd-tab").forEach(btn => {
    btn.classList.toggle("active", +btn.dataset.domain === _domain);
  });
}

// ---- Context chips (BPM / key from editor) ----------------------

function _updateContextChips(ctx) {
  const wrap = document.getElementById("cdCtxChips");
  if (!wrap) return;
  wrap.innerHTML = "";

  const chips = [];
  if (ctx.bpm) chips.push({ label: `${ctx.bpm} BPM`, filter: `${ctx.bpm}`, title: `filter ±15 BPM` });
  if (ctx.key) {
    const root = ctx.key.split(" ")[0];
    chips.push({ label: ctx.key, filter: `@${root}`, title: `filter by key` });
  }

  if (!chips.length) { wrap.classList.add("hidden"); return; }
  wrap.classList.remove("hidden");

  chips.forEach(c => {
    const btn = document.createElement("button");
    btn.className = "cd-chip";
    btn.textContent = c.label;
    btn.title = c.title;
    btn.addEventListener("click", () => {
      const input = document.getElementById("cellDialSearch");
      // Toggle: if already applied, clear; otherwise apply
      if (input.value === c.filter) {
        input.value = "";
        _runFilter("");
      } else {
        input.value = c.filter;
        _runFilter(c.filter);
      }
      input.focus();
      _updateChipActiveState();
    });
    wrap.appendChild(btn);
  });
  _updateChipActiveState();
}

function _updateChipActiveState() {
  const val = document.getElementById("cellDialSearch")?.value ?? "";
  document.querySelectorAll(".cd-chip").forEach(btn => {
    // Extract the filter value from the chip by checking if it matches current input
    const chip = btn;
    // Re-derive filter: BPM chip filter starts with ~, key chip with @
    const isBpmChip = btn.title === "filter ±10 BPM";
    const isKeyChip = btn.title === "filter by key";
    let active = false;
    if (isBpmChip && /^~?\d{2,3}$/.test(val)) active = true;
    if (isKeyChip && val.startsWith("@")) active = true;
    btn.classList.toggle("active", active);
  });
}

// ---- Parts button list (replaces ring for PARTS domain) ---------

function _buildPartsList() {
  const list = document.getElementById("cdPartsList");
  if (!list) return;
  list.innerHTML = "";

  const parts = _state.parts;
  if (!parts.length) {
    const msg = document.createElement("div");
    msg.className = "cd-parts-empty";
    msg.textContent = "No #@ sections in editor — add #@name(bars) to create parts";
    list.appendChild(msg);
    return;
  }

  parts.forEach(p => {
    const btn = document.createElement("button");
    btn.className = "cd-part-btn" + (_colFilter === p.key ? " active" : "");
    btn.dataset.key = p.key;

    const nameSpan = document.createElement("span");
    nameSpan.className = "cd-part-name";
    nameSpan.textContent = p.label;

    btn.appendChild(nameSpan);
    if (p.beats) {
      const bSpan = document.createElement("span");
      bSpan.className = "cd-part-beats";
      bSpan.textContent = `${p.beats}b`;
      btn.appendChild(bSpan);
    }

    btn.addEventListener("click", () => {
      _colFilter = _colFilter === p.key ? null : p.key;
      _buildPartsList();
      _runFilter(document.getElementById("cellDialSearch").value);
      document.getElementById("cellDialSearch").focus();
    });
    list.appendChild(btn);
  });
}

// ---- Ring refresh -----------------------------------------------

function _refreshRing() {
  const svg     = document.getElementById("cellDialRing");
  const partsList = document.getElementById("cdPartsList");
  if (!svg) return;

  if (_domain === 2) {
    // PARTS: replace ring with button grid
    svg.classList.add("hidden");
    partsList?.classList.remove("hidden");
    _buildPartsList();
  } else {
    svg.classList.remove("hidden");
    partsList?.classList.add("hidden");
    _buildRing(svg, _ringSegments(), _colFilter);
  }
}

function _ringSegments() {
  if (_domain === 0) return _state.cols.map(c => ({ key: c.letter, label: c.letter, score: c.compatRatio }));
  if (_domain === 1) return _state.attacks.map(a => ({ key: a.key, label: a.key, score: a.score }));
  return [];
}

// ---- Segment click ----------------------------------------------

function _handleSegmentClick(key) {
  if (_colFilter === key) {
    _colFilter = null;
    document.getElementById("cdColTag").classList.add("hidden");
    document.getElementById("cellDialSearch").placeholder =
      ["search col…", "filter attacks…", "jump to part…", "search all…"][_domain];
  } else {
    _colFilter = key;
    const tag  = document.getElementById("cdColTag");
    tag.textContent = _domain === 0 ? `${key}·${COL_ROLE[key] ?? "?"}` : key;
    tag.classList.remove("hidden");
    document.getElementById("cellDialSearch").value       = "";
    document.getElementById("cellDialSearch").placeholder = "filter…";
  }
  _pageStart = 0;
  _refreshRing();
  _runFilter(document.getElementById("cellDialSearch").value);
  document.getElementById("cellDialSearch").focus();
}

// ---- Filter + results -------------------------------------------

function _runFilter(query) {
  const q = query.trim().toLowerCase();

  if (_domain === 2) {
    let parts = _state.parts;
    if (_colFilter) parts = parts.filter(p => p.key === _colFilter);
    if (q) parts = parts.filter(p => p.label.toLowerCase().includes(q));
    _results   = parts;
    _selIdx    = 0;
    _pageStart = 0;
    _renderResults();
    return;
  }

  let items = _colFilter ? _segmentItems(_colFilter) : _state.allItems;

  if (q) {
    const bpmM = q.match(/^~?(\d{2,3})$/);   // ~68 or just 68 (2-3 digit number)
    const keyM = q.match(/^@(.+)$/);
    if (bpmM) {
      const t = +bpmM[1];
      items = items.filter(i => i.cell.tempo && Math.abs(i.cell.tempo - t) <= 15);
    } else if (keyM) {
      const kq = keyM[1].toLowerCase();
      items = items.filter(i => (i.cell.key || "").toLowerCase().includes(kq));
    } else {
      items = items.filter(i => {
        const lo = i.label.toLowerCase();
        const ko = (i.cell.key || "").toLowerCase();
        const co = i.coord.toLowerCase();
        const so = (i.cell.source_file || "").toLowerCase();
        return lo.includes(q) || ko.includes(q) || co.includes(q) || so.includes(q);
      });
    }
  }

  _results   = [...items].sort((a, b) => b.score - a.score || a.label.localeCompare(b.label));
  _selIdx    = 0;
  _pageStart = 0;
  _renderResults();
}

function _segmentItems(key) {
  if (_domain === 0) return _state.cols.find(c => c.letter === key)?.items ?? [];
  if (_domain === 1) return _state.attacks.find(a => a.key === key)?.items ?? [];
  return _state.allItems;
}

function _renderResults() {
  const container = document.getElementById("cellDialResults");
  const countEl   = document.getElementById("cdCount");
  if (!container) return;
  container.innerHTML = "";

  const total = _results.length;
  if (!total) {
    const empty = document.createElement("div");
    empty.className = "cd-empty";
    empty.textContent = _domain === 2 ? "no parts — add #@name(bars) to editor" : "no cells match";
    container.appendChild(empty);
    if (countEl) countEl.textContent = "";
    return;
  }

  if (_selIdx < _pageStart)              _pageStart = _selIdx;
  if (_selIdx >= _pageStart + PAGE_SIZE) _pageStart = _selIdx - PAGE_SIZE + 1;
  _pageStart = Math.max(0, Math.min(_pageStart, total - PAGE_SIZE));

  if (countEl) countEl.textContent = total > PAGE_SIZE ? `${_selIdx + 1}/${total}` : `${total}`;

  _results.slice(_pageStart, _pageStart + PAGE_SIZE).forEach((item, vi) => {
    const absIdx = _pageStart + vi;
    const active = absIdx === _selIdx;
    const row    = document.createElement("div");
    row.className = "cd-item" + (active ? " active" : "");
    row.setAttribute("role", "option");
    row.setAttribute("aria-selected", String(active));

    const num = vi < 9 ? `${vi + 1}` : " ";

    if (item.beats !== undefined && item.line !== undefined) {
      // Part row
      row.innerHTML =
        `<span class="cdi-num">${num}</span>` +
        `<span class="cdi-sel">${active ? "›" : " "}</span>` +
        `<span class="cdi-coord">#@</span>` +
        `<span class="cdi-label">${_esc(item.label)}</span>` +
        `<span class="cdi-meta">${item.beats ? item.beats + "b" : ""}</span>`;
    } else {
      // Cell row
      const role = COL_ROLE[item.coord.charAt(0)] ?? "?";
      const meta = [
        item.cell.tempo ? `${item.cell.tempo}` : "",
        item.cell.key   ? item.cell.key.split(" ")[0] : "",
      ].filter(Boolean).join(" ");
      row.innerHTML =
        `<span class="cdi-num">${num}</span>` +
        `<span class="cdi-sel">${active ? "›" : " "}</span>` +
        `<span class="cdi-coord">${_esc(item.coord)}</span>` +
        `<span class="cdi-role">${role}</span>` +
        `<span class="cdi-label">${_esc(item.label)}</span>` +
        `<span class="cdi-meta">${_esc(meta)}</span>` +
        `<span class="cdi-score">${_blocks(item.score)}</span>`;
    }

    row.addEventListener("click", () => { _selIdx = absIdx; _confirm(false); });
    container.appendChild(row);
  });
}

// ---- Keyboard handlers ------------------------------------------

function _onInputKey(e) {
  if (e.key === "Escape")    { e.preventDefault(); close();             return; }
  if (e.key === "ArrowDown") { e.preventDefault(); _move(1);            return; }
  if (e.key === "ArrowUp")   { e.preventDefault(); _move(-1);           return; }
  if (e.key === "Enter")     { e.preventDefault(); _confirm(e.shiftKey || e.ctrlKey); return; }

  if (e.key === "Tab") {
    e.preventDefault();
    _setDomain((_domain + (e.shiftKey ? DOMAINS.length - 1 : 1)) % DOMAINS.length);
    return;
  }

  const input = document.getElementById("cellDialSearch");

  // 1-9 on empty input → pick Nth visible result
  if (/^[1-9]$/.test(e.key) && input.value === "") {
    e.preventDefault();
    const absIdx = _pageStart + (+e.key - 1);
    if (absIdx < _results.length) { _selIdx = absIdx; _confirm(false); }
    return;
  }

  // A-Z shortcut in CELLS domain on empty input without active filter
  if (e.key.length === 1 && /^[A-Za-z]$/.test(e.key) && _domain === 0 && !_colFilter && input.value === "") {
    e.preventDefault();
    _handleSegmentClick(e.key.toUpperCase());
    return;
  }

  // Backspace on empty input → clear filter
  if (e.key === "Backspace" && input.value === "" && _colFilter) {
    e.preventDefault();
    _handleSegmentClick(_colFilter);
  }
}

function _onGlobalKey(e) {
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === "g" || e.key === "G")) {
    e.preventDefault(); e.stopPropagation();
    _open ? close() : open();
    return;
  }
  if (_open && e.key === "Escape") {
    e.preventDefault(); e.stopPropagation(); close();
  }
}

// ---- Navigation + confirm ---------------------------------------

function _move(dir) {
  const newIdx = Math.max(0, Math.min(_results.length - 1, _selIdx + dir));
  if (newIdx === _selIdx) return;
  _selIdx = newIdx;
  _renderResults();
}

function _confirm(evalCode) {
  const item = _results[_selIdx];
  if (!item) return;

  if (item.beats !== undefined && item.line !== undefined) {
    // PARTS domain — jump to section in editor, or paste tag on Shift+Enter
    if (evalCode) {
      const tag = `#@${item.label}${item.beats ? `(${item.beats})` : ""}`;
      EventEmitter.emit("paste_to_editor", tag);
    } else if (_editor) {
      _editor.setCursor({ line: item.line, ch: 0 });
      _editor.scrollIntoView({ line: item.line, ch: 0 }, 80);
    }
  } else {
    if (!item.cell?.code) return;
    EventEmitter.emit("paste_to_editor", item.cell.code);
    if (evalCode) EventEmitter.emit("send_foxdot", item.cell.code);
  }
  close();
}

// ---- Helpers ----------------------------------------------------

function _esc(s) {
  return (s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// ---- Public API -------------------------------------------------

export function setupCellDial(editorInstance, getSectionsCallback) {
  _editor      = editorInstance;
  _getSections = getSectionsCallback ?? null;
  const init = () => {
    _buildDom();
    document.addEventListener("keydown", _onGlobalKey, true);
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
}

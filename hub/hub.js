/**
 * CrashOS Hub — Signal router, state machine, public gateway
 *
 * Runs on YOUR laptop during live performance.
 * Every output (renderer, lights, app) is just a client that subscribes to signals.
 *
 * Connect → Identify → Subscribe → Receive
 *
 * Ports:
 *   1235  — hub WS (all clients)
 *   20001 — FoxDot OSC in (UDP)
 */

import { WebSocketServer, WebSocket } from 'ws';
import { createServer } from 'http';
import { readFileSync, writeFileSync } from 'fs';
import dgram from 'dgram';
import path from 'path';
import { fileURLToPath } from 'url';
import { FeedManager } from './feeds.js';
import { startAudio, getAudio, stopAudio } from './audio.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ─── Config ──────────────────────────────────────────────
let config = {};
try {
  config = JSON.parse(readFileSync(path.join(__dirname, 'hub_config.json'), 'utf8'));
  console.log('[hub] loaded hub_config.json');
} catch { console.log('[hub] no hub_config.json, using defaults'); }

const CONFIG_PATH = path.join(__dirname, 'hub_config.json');

function saveConfig() {
  try {
    writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2) + '\n');
  } catch (e) {
    console.log('[hub] config save failed:', e.message);
  }
}

const HUB_PORT = config.HUB_PORT || 1235;
const OSC_PORT = config.OSC_PORT || 20001;
const WEBTROOP_URL = config.WEBTROOP_URL || null;
const TICK_MS = config.TICK_MS || 50;
const PUBLIC_RATE_LIMIT = config.PUBLIC_RATE_LIMIT || 100;
const UPSTREAM_INTERVAL = config.UPSTREAM_INTERVAL || 2000;
const FOXDOT_WS_URL = config.FOXDOT_WS_URL || null;

// ─── Available Signals ───────────────────────────────────
// Clients subscribe to these. Hub only sends what each client asked for.
const SIGNALS = [
  'beat',           // beat counter, bar, bpm
  'audio',          // audio analysis (levels, spectrum, onset)
  'code',           // code evaluations from IDE
  'grid',           // 5x5 grid state updates
  'phase',          // state machine transitions
  'players',        // active FoxDot player data
  'public',         // aggregated public input (votes, energy, taps)
  'public_raw',     // raw public input (images, motion) — heavy
  'data_feeds',     // GPS, OSM, WiFi, Mastodon, seismic, market, space weather
  'stats',          // performance statistics
  'lights',         // light-specific: colors, chase, strobe triggers
  'game',           // MUD/game events (bidirectional)
  'render',         // render commands → visual renderers (scene, fx, palette, crossfade)
];

// ─── State Machine ───────────────────────────────────────
const PHASES = ['boot', 'scan', 'grid', 'performance', 'stats'];

const state = {
  phase: 'boot',
  beat: 0,
  bpm: 120,
  bar: 0,
  cpu: 0,
  audio: { level: 0, bass: 0, mid: 0, high: 0, onset: false },
  players: {},
  grid: createGrid(),
  publicClients: 0,
  stats: { evals: 0, lines: 0, publicEvents: 0, startTime: Date.now() },
  votes: {},
  crowdEnergy: 0,
  lights: { color: [255, 0, 0], mode: 'pulse', intensity: 1, strobe: false },
};

function createGrid() {
  const grid = [];
  for (let y = 0; y < 5; y++) {
    grid[y] = [];
    for (let x = 0; x < 5; x++) {
      grid[y][x] = { owner: 'neutral', scene: null, health: 100, corrupted: 0 };
    }
  }
  return grid;
}

// ─── Client Registry ────────────────────────────────────
// Every client: { ws, role, id, name, subscriptions, ip, connectedAt }
const allClients = new Map();  // ws → client info
let clientCounter = 0;

function registerClient(ws, info) {
  const client = {
    ws,
    role: info.role || 'public',
    id: info.id || ++clientCounter,
    name: info.name || `${info.role}_${clientCounter}`,
    subscriptions: new Set(info.subscribe || getDefaultSubscriptions(info.role)),
    ip: info.ip,
    connectedAt: Date.now(),
  };
  allClients.set(ws, client);
  state.publicClients = countRole('public');
  return client;
}

function unregisterClient(ws) {
  allClients.delete(ws);
  state.publicClients = countRole('public');
}

function countRole(role) {
  let n = 0;
  allClients.forEach(c => { if (c.role === role) n++; });
  return n;
}

function getDefaultSubscriptions(role) {
  switch (role) {
    case 'renderer': return ['beat', 'audio', 'code', 'render', 'grid', 'phase', 'players', 'public'];
    case 'lights':   return ['beat', 'audio', 'lights'];
    case 'public':   return ['phase', 'grid', 'stats', 'game'];
    case 'control':  return SIGNALS;  // everything
    case 'ide':      return ['public', 'stats', 'game'];
    case 'game':     return ['phase', 'grid', 'public', 'beat', 'data_feeds'];
    default:         return ['phase'];
  }
}

// ─── HTTP Server (serves control panel UI) ───────────────
const httpServer = createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);

  if (url.pathname === '/' || url.pathname === '/index.html') {
    try {
      const html = readFileSync(path.join(__dirname, 'public', 'index.html'), 'utf8');
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(html);
    } catch {
      res.writeHead(500);
      res.end('control panel not found');
    }
  } else if (url.pathname === '/state') {
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(state));
  } else if (url.pathname === '/api/geocode') {
    // Geocode city name → lat/lon
    const city = url.searchParams.get('city');
    if (!city) { res.writeHead(400); res.end('missing city param'); return; }
    handleGeocode(city, res);
  } else if (url.pathname === '/api/set_location') {
    // Set venue location, trigger OSM + feed refresh
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { lat, lon, city } = JSON.parse(body);
        setLocation(lat, lon, city);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: true, lat: state.location.lat, lon: state.location.lon, city: state.location.city }));
      } catch (e) {
        res.writeHead(400);
        res.end(JSON.stringify({ error: e.message }));
      }
    });
  } else if (url.pathname.startsWith('/renderer/')) {
    // Serve renderer controller pages: /renderer/clift2 → proxy its controller
    const name = url.pathname.split('/')[2];
    const renderer = renderers.get(name);
    if (!renderer) { res.writeHead(404); res.end('renderer not found'); return; }
    const rUrl = new URL(renderer.config.url.replace('ws://', 'http://'));
    try {
      const r = await fetch(`http://${rUrl.host}/`, { signal: AbortSignal.timeout(3000) });
      let html = await r.text();
      // Patch the WS URL to point to the renderer directly
      // The controller uses ws://${location.host} so we need to fix it
      html = html.replace(
        "const url = 'ws://' + location.host;",
        `const url = '${renderer.config.url}';`
      );
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(html);
    } catch (e) {
      res.writeHead(502);
      res.end(`cannot reach ${name}: ${e.message}`);
    }
  } else if (url.pathname === '/api/feeds') {
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(feedManager.getStatus()));
  } else if (url.pathname === '/api/feed') {
    // POST: { action: 'enable'|'disable'|'trigger'|'set_interval', name: '...', interval: N }
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { action, name, interval } = JSON.parse(body);
        let ok = false;
        if (action === 'enable') ok = feedManager.enable(name);
        else if (action === 'disable') ok = feedManager.disable(name);
        else if (action === 'trigger') { feedManager.trigger(name); ok = true; }
        else if (action === 'set_interval') ok = feedManager.setInterval(name, interval);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok, name, action }));
      } catch (e) {
        res.writeHead(400); res.end(JSON.stringify({ error: e.message }));
      }
    });
  } else if (url.pathname === '/api/mastodon') {
    if (req.method === 'GET') {
      res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
      res.end(JSON.stringify({ keywords: feedManager.getMastodonKeywords(), instance: config.feeds?.mastodon_instance || 'mastodon.social' }));
    } else {
      let body = '';
      req.on('data', c => body += c);
      req.on('end', () => {
        try {
          const { action, keyword } = JSON.parse(body);
          let ok = false;
          if (action === 'add' && keyword) ok = feedManager.addMastodonKeyword(keyword);
          else if (action === 'remove' && keyword) ok = feedManager.removeMastodonKeyword(keyword);
          if (ok) saveConfig();
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok, keywords: feedManager.getMastodonKeywords() }));
        } catch (e) {
          res.writeHead(400); res.end(JSON.stringify({ error: e.message }));
        }
      });
    }
  } else if (url.pathname === '/api/rss') {
    if (req.method === 'GET') {
      res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
      res.end(JSON.stringify(feedManager.getRssSources()));
    } else {
      let body = '';
      req.on('data', c => body += c);
      req.on('end', () => {
        try {
          const { action, url: rssUrl } = JSON.parse(body);
          let ok = false;
          if (action === 'add' && rssUrl) ok = feedManager.addRss(rssUrl);
          else if (action === 'remove' && rssUrl) ok = feedManager.removeRss(rssUrl);
          if (ok) saveConfig();
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ ok, rss: feedManager.getRssSources() }));
        } catch (e) {
          res.writeHead(400); res.end(JSON.stringify({ error: e.message }));
        }
      });
    }
  } else if (url.pathname === '/api/add_renderer') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      try {
        const { name, url: rUrl } = JSON.parse(body);
        if (!name || !rUrl) { res.writeHead(400); res.end('need name and url'); return; }
        connectRenderer(name, rUrl);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ ok: true, name, url: rUrl }));
      } catch (e) {
        res.writeHead(400); res.end(JSON.stringify({ error: e.message }));
      }
    });
  } else if (url.pathname === '/api/renderers') {
    const list = [];
    renderers.forEach((r, name) => {
      list.push({ name, url: r.config.url, connected: r.connected, scene_a: r.state.deck_a?.scene });
    });
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(list));
  } else {
    res.writeHead(404);
    res.end('not found');
  }
});

httpServer.listen(HUB_PORT, '0.0.0.0', () => {
  console.log(`[hub] http://0.0.0.0:${HUB_PORT} — control panel`);
});

// ─── WebSocket Server (same port as HTTP) ────────────────
const wss = new WebSocketServer({ server: httpServer });
console.log(`[hub] ws://0.0.0.0:${HUB_PORT} — signal router`);

wss.on('connection', (ws, req) => {
  const ip = req.socket.remoteAddress;
  const lastMsg = { time: 0 };
  let client = null;

  ws.on('message', (raw) => {
    let msg;
    try { msg = JSON.parse(raw); } catch { return; }

    // ── Identify ──
    if (msg.type === 'identify') {
      client = registerClient(ws, { ...msg, ip });
      ws.send(JSON.stringify({
        type: 'welcome',
        id: client.id,
        name: client.name,
        subscriptions: [...client.subscriptions],
        signals: SIGNALS,
        phases: PHASES,
        currentPhase: state.phase,
      }));
      console.log(`[hub] + ${client.name} (${client.role}) from ${ip} — [${[...client.subscriptions].join(',')}]`);
      broadcastClientList();
      return;
    }

    if (!client) return;  // must identify first

    // ── Subscribe / Unsubscribe ──
    if (msg.type === 'subscribe') {
      (msg.signals || []).forEach(s => { if (SIGNALS.includes(s)) client.subscriptions.add(s); });
      ws.send(JSON.stringify({ type: 'subscriptions', signals: [...client.subscriptions] }));
      console.log(`[hub] ${client.name} subscribed: [${[...client.subscriptions].join(',')}]`);
      return;
    }
    if (msg.type === 'unsubscribe') {
      (msg.signals || []).forEach(s => client.subscriptions.delete(s));
      ws.send(JSON.stringify({ type: 'subscriptions', signals: [...client.subscriptions] }));
      return;
    }

    // ── Rate limit public ──
    if (client.role === 'public') {
      const now = Date.now();
      if (now - lastMsg.time < PUBLIC_RATE_LIMIT) return;
      lastMsg.time = now;
      handlePublicMessage(msg, client);
      return;
    }

    // ── Control messages ──
    if (client.role === 'control') {
      handleControlMessage(msg);
      return;
    }

    // ── IDE / webTroop events ──
    if (client.role === 'ide') {
      handleIdeMessage(msg);
      return;
    }

    // ── Game / MUD events (bidirectional) ──
    if (client.role === 'game') {
      handleGameMessage(msg, client);
      return;
    }

    // ── Renderer can send capabilities back ──
    if (client.role === 'renderer') {
      handleRendererMessage(msg, client);
      return;
    }

    // ── Any client can emit to a signal it subscribes to ──
    if (msg.type === 'emit' && msg.signal && client.subscriptions.has(msg.signal)) {
      emit(msg.signal, { ...msg.data, from: client.name });
      return;
    }
  });

  ws.on('close', () => {
    if (client) {
      console.log(`[hub] - ${client.name} (${client.role})`);
      unregisterClient(ws);
      broadcastClientList();
    }
  });

  // Auto-assign as public if no identify within 3s
  setTimeout(() => {
    if (!client) {
      client = registerClient(ws, { role: 'public', ip });
      ws.send(JSON.stringify({ type: 'welcome', role: 'public', subscriptions: [...client.subscriptions] }));
    }
  }, 3000);
});

// ─── Signal Broadcast (subscription-based) ───────────────
function emit(signal, data) {
  const msg = JSON.stringify({ type: signal, ...data });
  allClients.forEach(client => {
    if (client.subscriptions.has(signal) && client.ws.readyState === WebSocket.OPEN) {
      client.ws.send(msg);
    }
  });
}

function sendTo(ws, msg) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify(msg));
  }
}

function broadcastAll(msg) {
  const json = JSON.stringify(msg);
  wss.clients.forEach(ws => {
    if (ws.readyState === WebSocket.OPEN) ws.send(json);
  });
}

function broadcastClientList() {
  const list = [];
  allClients.forEach(c => {
    list.push({ id: c.id, name: c.name, role: c.role, subscriptions: [...c.subscriptions], uptime: Date.now() - c.connectedAt });
  });
  emit('stats', { clients: list });
}

// ─── Message Handlers ────────────────────────────────────

function handlePublicMessage(msg, client) {
  state.stats.publicEvents++;

  switch (msg.type) {
    case 'vote': {
      const choice = String(msg.choice).slice(0, 32);
      state.votes[choice] = (state.votes[choice] || 0) + 1;
      emit('public', { event: 'vote', votes: state.votes });
      break;
    }
    case 'motion': {
      if (msg.accel && Array.isArray(msg.accel)) {
        const magnitude = Math.sqrt(msg.accel.reduce((s, v) => s + v * v, 0));
        state.crowdEnergy = state.crowdEnergy * 0.95 + magnitude * 0.05;
      }
      break;
    }
    case 'tap': {
      emit('public', { event: 'tap', energy: state.crowdEnergy, clientId: client.id });
      break;
    }
    case 'image': {
      if (msg.data && msg.data.length < 100000) {
        emit('public_raw', { event: 'image', data: msg.data, clientId: client.id });
      }
      break;
    }
  }
}

function handleControlMessage(msg) {
  switch (msg.type) {
    case 'set_phase': {
      if (PHASES.includes(msg.phase)) {
        state.phase = msg.phase;
        console.log(`[hub] phase → ${msg.phase}`);
        broadcastAll({ type: 'phase', phase: msg.phase });
        if (msg.phase === 'boot') runBootSequence();
      }
      break;
    }
    case 'assign_scene': {
      const { x, y, scene } = msg;
      if (x >= 0 && x < 5 && y >= 0 && y < 5) {
        state.grid[y][x].scene = scene;
        state.grid[y][x].owner = 'player';
        emit('grid', { grid: state.grid });
      }
      break;
    }
    case 'send_to': {
      // Send arbitrary message to a specific client by name or id
      allClients.forEach(c => {
        if (c.name === msg.target || c.id === msg.target) {
          sendTo(c.ws, msg.payload);
        }
      });
      break;
    }
    case 'set_lights': {
      // Direct light control
      Object.assign(state.lights, msg.lights);
      emit('lights', { lights: state.lights });
      break;
    }
    case 'render': {
      // Control panel sends render commands → route to renderers
      console.log(`[hub] render from control:`, JSON.stringify(msg));
      routeRender(msg);
      emit('render', msg);
      break;
    }
    case 'subscribe_client': {
      // Remotely change a client's subscriptions
      allClients.forEach(c => {
        if (c.name === msg.target || c.id === msg.target) {
          (msg.add || []).forEach(s => { if (SIGNALS.includes(s)) c.subscriptions.add(s); });
          (msg.remove || []).forEach(s => c.subscriptions.delete(s));
          sendTo(c.ws, { type: 'subscriptions', signals: [...c.subscriptions] });
          console.log(`[hub] ${c.name} subs updated: [${[...c.subscriptions].join(',')}]`);
        }
      });
      break;
    }
  }
}

function handleIdeMessage(msg) {
  switch (msg.type) {
    case 'eval':
      state.stats.evals++;
      state.stats.lines += (msg.code || '').split('\n').length;
      emit('code', { code: msg.code, player: msg.player });
      break;
    case 'player_update':
      state.players = msg.players || state.players;
      emit('players', { players: state.players });
      break;
    case 'bpm':
      state.bpm = msg.bpm;
      break;
    case 'audio':
      Object.assign(state.audio, msg.audio);
      break;
  }
}

function handleGameMessage(msg, client) {
  switch (msg.type) {
    case 'game_event': {
      // MUD sends game events → broadcast to everyone subscribed to 'game'
      emit('game', { event: msg.event, player: msg.player, data: msg.data, from: client.name });

      // Game events can affect the grid
      if (msg.event === 'attack_cell' && msg.target) {
        const { x, y } = msg.target;
        if (x >= 0 && x < 5 && y >= 0 && y < 5) {
          const cell = state.grid[y][x];
          if (cell.owner === 'server') {
            cell.corrupted -= msg.damage || 15;
            if (cell.corrupted <= 0) {
              cell.owner = 'player';
              cell.corrupted = 0;
              console.log(`[hub] public reclaimed (${x},${y}) via MUD`);
            }
            emit('grid', { grid: state.grid });
          }
        }
      }
      break;
    }
    case 'game_state': {
      // MUD shares its state (online players, rooms, etc)
      emit('game', { event: 'state', state: msg.state, from: client.name });
      break;
    }
    case 'game_chat': {
      // MUD chat → can appear on renderers, feed to IDE
      emit('game', { event: 'chat', text: msg.text, player: msg.player, from: client.name });
      break;
    }
  }
}

function handleRendererMessage(msg, client) {
  switch (msg.type) {
    case 'ready':
      // Renderer reports its capabilities
      console.log(`[hub] ${client.name} ready — capabilities: ${JSON.stringify(msg.capabilities || [])}`);
      break;
    case 'scene_loaded':
      console.log(`[hub] ${client.name} loaded scene: ${msg.scene}`);
      break;
  }
}

// ─── OSC Listener (FoxDot beat data) ─────────────────────
const osc = dgram.createSocket('udp4');

osc.on('message', (buf) => {
  try {
    const str = buf.toString('utf8');
    if (str.includes('/beat')) {
      state.beat++;
      state.bar = Math.floor(state.beat / 4);
      if (state.beat % 4 === 0 && state.phase === 'grid') {
        serverGridMove();
      }
    }
  } catch (e) { /* ignore */ }
});

osc.bind(OSC_PORT, () => {
  console.log(`[hub] OSC listening on udp://0.0.0.0:${OSC_PORT}`);
});

// ─── 5x5 Grid — Server AI ────────────────────────────────
function serverGridMove() {
  const targets = [];
  for (let y = 0; y < 5; y++) {
    for (let x = 0; x < 5; x++) {
      if (state.grid[y][x].owner !== 'server') targets.push({ x, y });
    }
  }
  if (targets.length === 0) return;

  const target = targets[Math.floor(Math.random() * targets.length)];
  const cell = state.grid[target.y][target.x];
  cell.corrupted += 10 + Math.random() * 20;

  if (cell.corrupted >= 100) {
    cell.owner = 'server';
    cell.scene = pickServerScene();
    console.log(`[hub] server captured (${target.x},${target.y})`);
  }

  emit('grid', { grid: state.grid });
}

function pickServerScene() {
  const scenes = ['glitch', 'datamosh', 'interference', 'static', 'corruption', 'void'];
  return scenes[Math.floor(Math.random() * scenes.length)];
}

// ─── Periodic Ticks ──────────────────────────────────────

// Beat tick — only when beat actually changes
let lastEmittedBeat = -1;
let lastOnset = false;

setInterval(() => {
  // Only emit beat when beat counter changes (actual beat from FoxDot)
  if (state.beat !== lastEmittedBeat) {
    lastEmittedBeat = state.beat;
    const tick = {
      beat: state.beat,
      bar: state.bar,
      bpm: state.bpm,
      phase: state.phase,
      crowdEnergy: state.crowdEnergy,
      cpu: state.cpu,
      audio: state.audio,
    };
    emit('beat', tick);

    // Audio-reactive: only trigger on rising edge of onset
    if (state.audio.onset && !lastOnset) {
      routeBeatToRenderers(tick);
    }
    lastOnset = state.audio.onset;

    // Lights only on actual beats, not every tick
    const hasLightClients = [...allClients.values()].some(c => c.subscriptions.has('lights'));
    if (hasLightClients) {
      emit('lights', {
        lights: {
          ...state.lights,
          intensity: state.audio.level,
          bass: state.audio.bass,
          beat: state.beat,
          bpm: state.bpm,
          onset: state.audio.onset,
        },
      });
    }
  }
}, TICK_MS);

// Aggregated upstream relay + stats
setInterval(() => {
  // Upstream to webTroop — send public data so friend sees it too
  if (webtroopUpstream && webtroopUpstream.readyState === WebSocket.OPEN) {
    try {
      webtroopUpstream.send(JSON.stringify({
        type: 'hub_update',
        votes: { ...state.votes },
        crowdEnergy: state.crowdEnergy,
        publicClients: state.publicClients,
        phase: state.phase,
        grid: state.grid,
        players: state.players,
      }));
    } catch {}
  }

  // Stats signal
  const clientList = [];
  allClients.forEach(c => {
    clientList.push({ id: c.id, name: c.name, role: c.role, subscriptions: [...c.subscriptions] });
  });
  // Renderer status
  const rendererList = [];
  renderers.forEach((r, name) => {
    rendererList.push({ name, url: r.config.url, connected: r.connected, scene_a: r.state.deck_a?.scene, scene_b: r.state.deck_b?.scene });
  });

  emit('stats', {
    clients: clientList,
    renderers: rendererList,
    evals: state.stats.evals,
    lines: state.stats.lines,
    publicEvents: state.stats.publicEvents,
    uptime: Date.now() - state.stats.startTime,
  });
}, UPSTREAM_INTERVAL);

// ─── Phase: Boot Sequence ────────────────────────────────
async function runBootSequence() {
  if (state.phase !== 'boot') return;

  const bootMessages = [
    'CRASH OS v2026.03',
    'initializing audio subsystem...',
    'connecting to SuperCollider...',
    'loading synth definitions... 208 found',
    'loading effects chain... 122 found',
    'loading samples... scanning',
    'PipeWire bridge active',
    'WebSocket hub online',
    'scanning network...',
    'ready.',
  ];

  for (const msg of bootMessages) {
    broadcastAll({ type: 'boot_line', text: msg });
    await sleep(300 + Math.random() * 700);
    if (state.phase !== 'boot') break;
  }
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

setTimeout(runBootSequence, 1000);

// ─── Upstream Relay to Friend's webTroop ─────────────────
let webtroopUpstream = null;

function connectUpstream() {
  if (!WEBTROOP_URL) return;
  try {
    webtroopUpstream = new WebSocket(WEBTROOP_URL);
    webtroopUpstream.on('open', () => {
      console.log(`[hub] connected to webTroop at ${WEBTROOP_URL}`);
    });
    webtroopUpstream.on('message', (raw) => {
      try {
        const msg = JSON.parse(raw);

        switch (msg.type) {
          case 'foxdot_log': {
            const data = msg.data || '';

            // Parse code evals from log format: "svdk: d5 >> plaitsX(...)"
            const evalMatch = data.match(/^(svdk|zbdm|SERVER)\s*:\s*(.+)/s);
            if (evalMatch) {
              const userName = evalMatch[1];
              const code = evalMatch[2].trim();
              state.stats.evals++;
              state.stats.lines += code.split('\n').length;

              // Extract BPM
              const bpmMatch = code.match(/Clock\.bpm\s*=\s*(\d+)/);
              if (bpmMatch) {
                state.bpm = parseInt(bpmMatch[1]);
                console.log(`[hub] BPM → ${state.bpm}`);
              }

              // Extract Root changes
              const rootMatch = code.match(/Root\.default\s*=\s*["']?([A-G]#?)["']?/);
              if (rootMatch) {
                state.root = rootMatch[1];
                console.log(`[hub] Root → ${state.root}`);
              }

              // Extract Scale changes
              const scaleMatch = code.match(/Scale\.default\s*=\s*["'](\w+)["']/);
              if (scaleMatch) {
                state.scale = scaleMatch[1];
                console.log(`[hub] Scale → ${state.scale}`);
              }

              // Extract player assignments: "d1 >> synth" or "b2 >> bass(...)"
              const playerLines = code.split('\n');
              for (const line of playerLines) {
                const pm = line.match(/^(\w+)\s*>>\s*(\w+)/);
                if (pm) {
                  state.players[pm[1]] = {
                    synth: pm[2],
                    user: userName,
                    lastEval: Date.now(),
                    code: line.slice(0, 300),
                  };
                }
                // Detect .stop()
                const sm = line.match(/^(\w+)\.stop\(\)/);
                if (sm && state.players[sm[1]]) {
                  delete state.players[sm[1]];
                }
              }
              emit('players', { players: state.players });
              emit('code', { event: 'eval', code, userName, userColor: msg.color });
              routeCodeToRenderers({ event: 'eval', code, userName });

              // Parse video player: v1 >> video(scene=4, ...) → route scene index
              const videoMatch = code.match(/\w+\s*>>\s*video\(([^)]*)\)/);
              if (videoMatch) {
                const args = videoMatch[1];
                const sceneM = args.match(/scene\s*=\s*(\d+)/);
                if (sceneM) {
                  routeRender({ scene_index: parseInt(sceneM[1]) });
                }
              }

              // Parse #@ directives from comments (FoxDot ignores these)
              // #@ scene Plasma
              // #@ fx glitch
              // #@ palette cyber
              // #@ crossfade 0.5
              // #@ ikeda on
              // #@ random
              // #@ zoom 0.3
              // Can combine: #@ scene Plasma fx glitch palette cyber
              for (const line of playerLines) {
                const directive = line.match(/#@\s+(.+)/);
                if (directive) {
                  const parts = directive[1].trim();
                  const renderMsg = {};

                  // Parse key value pairs: scene Plasma, fx glitch, etc.
                  const tokens = parts.split(/\s+/);
                  let i = 0;
                  while (i < tokens.length) {
                    const key = tokens[i].toLowerCase();
                    if (['scene', 'fx', 'palette', 'gradient', 'render_mode', 'xfade_mode', 'deck', 'preset_load', 'preset_save'].includes(key)) {
                      if (i + 1 < tokens.length) { renderMsg[key] = tokens[i + 1]; i += 2; }
                      else i++;
                    } else if (key === 'crossfade' || key === 'xf') {
                      if (i + 1 < tokens.length) { renderMsg.crossfade = parseFloat(tokens[i + 1]); i += 2; }
                      else i++;
                    } else if (key === 'zoom') {
                      renderMsg.zoom = i + 1 < tokens.length ? parseFloat(tokens[i + 1]) : 0.3; i += 2;
                    } else if (key === 'color_a' || key === 'color_b') {
                      if (i + 1 < tokens.length) { renderMsg[key] = parseInt(tokens[i + 1]); i += 2; }
                      else i++;
                    } else if (key === 'ikeda') {
                      renderMsg.ikeda = (i + 1 < tokens.length && tokens[i + 1] === 'off') ? false : true;
                      i += (i + 1 < tokens.length && ['on', 'off'].includes(tokens[i + 1])) ? 2 : 1;
                    } else if (key === 'random' || key === 'randomize') {
                      renderMsg.randomize = true; i++;
                    } else if (key === 'fill') {
                      renderMsg.fill = true; i++;
                    } else if (key === 'freeze') {
                      renderMsg.freeze = true; i++;
                    } else if (key === 'overlay') {
                      renderMsg.code_overlay = true; i++;
                    } else {
                      i++;  // skip unknown
                    }
                  }

                  if (Object.keys(renderMsg).length > 0) {
                    console.log(`[hub] #@ directive:`, JSON.stringify(renderMsg));
                    routeRender(renderMsg);
                    emit('render', renderMsg);
                  }
                }
              }
            }

            // Forward all logs
            emit('code', { event: 'log', data, color: msg.color, attackRequestName: msg.attackRequestName });
            break;
          }
          case 'seq_next': {
            emit('code', { event: 'seq_next', seqId: msg.seqId });
            break;
          }
          case 'compose_start': {
            emit('code', { event: 'compose_start', section: msg.section });
            break;
          }
          case 'rec_script': {
            emit('code', { event: 'rec_script', content: msg.content });
            break;
          }
          case 'cpu_data': {
            state.cpu = (msg.cpu || 0) / 100;
            break;
          }
          case 'sceneName': {
            state.sceneName = msg.sceneName;
            emit('code', { event: 'scene', sceneName: msg.sceneName });
            break;
          }
        }
      } catch {}
    });
    webtroopUpstream.on('close', () => {
      console.log('[hub] webTroop disconnected, retrying in 3s...');
      webtroopUpstream = null;
      setTimeout(connectUpstream, 3000);
    });
    webtroopUpstream.on('error', () => {});
  } catch {}
}

connectUpstream();

// ─── FoxDot WS Connection (port 20000) ──────────────────
let foxdotWs = null;

function connectFoxDot() {
  if (!FOXDOT_WS_URL) return;
  try {
    foxdotWs = new WebSocket(FOXDOT_WS_URL);
    foxdotWs.on('open', () => {
      console.log(`[hub] connected to FoxDot WS at ${FOXDOT_WS_URL}`);
    });
    foxdotWs.on('message', (raw) => {
      try {
        const msg = JSON.parse(raw);
        switch (msg.type) {
          case 'bpm':
            state.bpm = msg.bpm;
            break;
          case 'beat':
            state.beat = msg.beat;
            state.bar = Math.floor(msg.beat / 4);
            if (msg.beat % 4 === 0 && state.phase === 'grid') serverGridMove();
            break;
          case 'cpu':
            state.cpu = (msg.cpu || 0) / 100;
            break;
          case 'scale':
            state.scale = msg.scale;
            emit('code', { event: 'scale', scale: msg.scale });
            break;
          case 'root':
            state.root = msg.root;
            emit('code', { event: 'root', root: msg.root });
            break;
          case 'serverState':
            state.serverActive = msg.serverState;
            emit('code', { event: 'serverState', active: msg.serverState });
            break;
          case 'chrono':
            state.chrono = msg.chrono;
            break;
          case 'players':
            // FoxDot sends full player list
            if (msg.players) {
              state.foxdotPlayers = msg.players;
              emit('players', { players: msg.players });
            }
            break;
          case 'masterFx':
            state.masterFx = msg.masterFx;
            emit('code', { event: 'masterFx', masterFx: msg.masterFx });
            break;
          case 'help':
            emit('code', { event: 'help', help: msg.help });
            break;
          case 'sceneName':
            state.sceneName = msg.sceneName;
            emit('code', { event: 'scene', sceneName: msg.sceneName });
            break;
          case 'render':
            // FoxDot render command → route to renderers
            console.log(`[hub] render from FoxDot:`, JSON.stringify(msg));
            routeRender(msg);
            emit('render', msg);
            break;
        }
      } catch {}
    });
    foxdotWs.on('close', () => {
      console.log('[hub] FoxDot WS disconnected, retrying in 3s...');
      foxdotWs = null;
      setTimeout(connectFoxDot, 3000);
    });
    foxdotWs.on('error', () => {});
  } catch {}
}

connectFoxDot();

// ─── Location / Geocode ──────────────────────────────────
state.location = { lat: config.feeds?.lat || null, lon: config.feeds?.lon || null, city: null };

async function handleGeocode(city, res) {
  try {
    const r = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(city)}&limit=5`, {
      headers: { 'User-Agent': 'CrashOS-Hub/1.0' },
      signal: AbortSignal.timeout(8000),
    });
    const results = await r.json();
    const formatted = results.map(r => ({ name: r.display_name, lat: parseFloat(r.lat), lon: parseFloat(r.lon), type: r.type }));
    res.writeHead(200, { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
    res.end(JSON.stringify(formatted));
  } catch (e) {
    res.writeHead(500);
    res.end(JSON.stringify({ error: e.message }));
  }
}

function setLocation(lat, lon, city) {
  state.location = { lat, lon, city: city || `${lat},${lon}` };
  console.log(`[hub] location → ${state.location.city} (${lat}, ${lon})`);

  // Update feeds config and re-fetch
  if (config.feeds) {
    config.feeds.lat = lat;
    config.feeds.lon = lon;
    saveConfig();
  }

  // Immediately trigger location-dependent feeds
  fetchOSM(lat, lon);
  fetchLocalMastodon(lat, lon);
  feedManager.trigger('wifi');

  // Broadcast location to all clients
  emit('data_feeds', { feed: 'location', lat, lon, city: state.location.city });
}

async function fetchOSM(lat, lon) {
  const radius = config.feeds?.osm_radius || 500;
  try {
    // Buildings
    const query = `[out:json][timeout:15];(way["building"](around:${radius},${lat},${lon});way["highway"](around:${radius},${lat},${lon}););out body;>;out skel qt;`;
    const r = await fetch('https://overpass-api.de/api/interpreter', {
      method: 'POST',
      body: `data=${encodeURIComponent(query)}`,
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'CrashOS-Hub/1.0' },
      signal: AbortSignal.timeout(20000),
    });
    const data = await r.json();
    const buildings = data.elements?.filter(e => e.type === 'way' && e.tags?.building) || [];
    const roads = data.elements?.filter(e => e.type === 'way' && e.tags?.highway) || [];
    const nodes = data.elements?.filter(e => e.type === 'node') || [];
    console.log(`[hub] OSM: ${buildings.length} buildings, ${roads.length} roads, ${nodes.length} nodes`);
    emit('data_feeds', { feed: 'osm', buildings: buildings.length, roads: roads.length, elements: data.elements?.slice(0, 500), center: { lat, lon } });
  } catch (e) {
    console.log(`[hub] OSM fetch failed: ${e.message}`);
  }
}

async function fetchLocalMastodon(lat, lon) {
  // Search Mastodon for posts about the area
  try {
    const instance = config.feeds?.mastodon_instance || 'mastodon.social';
    const r = await fetch(`https://${instance}/api/v2/search?q=${encodeURIComponent(state.location.city || '')}&type=statuses&limit=20`, {
      signal: AbortSignal.timeout(8000),
    });
    const data = await r.json();
    const posts = (data.statuses || []).map(s => ({
      text: (s.content || '').replace(/<[^>]*>/g, '').slice(0, 280),
      author: s.account?.username,
      ts: s.created_at,
    })).filter(p => p.text.length > 5);
    if (posts.length) {
      console.log(`[hub] Mastodon: ${posts.length} local posts`);
      emit('data_feeds', { feed: 'mastodon_local', posts, city: state.location.city });
    }
  } catch {}
}

// ─── Renderers (direct WS connections) ──────────────────
// Hub connects directly to renderers like clift2
const renderers = new Map();  // name → { ws, connected, state, config }

function connectRenderer(name, url) {
  const r = { ws: null, connected: false, state: {}, config: { name, url } };
  renderers.set(name, r);

  function doConnect() {
    try {
      r.ws = new WebSocket(url);
      r.ws.on('open', () => {
        r.connected = true;
        console.log(`[hub] connected to renderer ${name} at ${url}`);
        // Request initial state
        sendRenderer(name, { cmd: 'get_state' });
      });
      r.ws.on('message', (raw) => {
        try {
          const msg = JSON.parse(raw);
          if (msg.type === 'state') {
            r.state = msg;
            // Broadcast renderer state to control clients
            emit('stats', {
              event: 'renderer_state',
              renderer: name,
              scene_a: msg.deck_a?.scene,
              scene_b: msg.deck_b?.scene,
              crossfade: msg.crossfade,
              fx_a: msg.deck_a?.fx,
              fx_b: msg.deck_b?.fx,
              palette_a: msg.deck_a?.palette,
              render_mode: msg.render_mode,
              ikeda: msg.ikeda_mode,
              scenes: msg.scenes,
              fx_list: msg.fx_list,
            });
          }
        } catch {}
      });
      r.ws.on('close', () => {
        r.connected = false;
        console.log(`[hub] renderer ${name} disconnected, retrying...`);
        setTimeout(doConnect, 3000);
      });
      r.ws.on('error', () => {});
    } catch {}
  }
  doConnect();
}

function sendRenderer(name, msg) {
  const r = renderers.get(name);
  if (r && r.connected && r.ws.readyState === WebSocket.OPEN) {
    r.ws.send(JSON.stringify(msg));
  }
}

function sendAllRenderers(msg) {
  renderers.forEach((r, name) => {
    if (r.connected && r.ws.readyState === WebSocket.OPEN) {
      r.ws.send(JSON.stringify(msg));
    }
  });
}

// Route render signals → renderer commands
function routeRender(msg) {
  const deck = msg.deck || 'a';

  if (msg.scene) {
    sendAllRenderers({ cmd: 'set_scene', deck, name: msg.scene });
    console.log(`[hub] render: scene → ${msg.scene} (deck ${deck})`);
  }
  if (msg.scene_index !== undefined) {
    // Get scene name from renderer state if available
    renderers.forEach((r) => {
      if (r.state.scenes && r.state.scenes[msg.scene_index]) {
        sendAllRenderers({ cmd: 'set_scene', deck, name: r.state.scenes[msg.scene_index] });
        console.log(`[hub] render: scene index ${msg.scene_index} → ${r.state.scenes[msg.scene_index]}`);
      }
    });
  }
  if (msg.fx) {
    sendAllRenderers({ cmd: 'set_fx', deck, name: msg.fx });
  }
  if (msg.palette) {
    sendAllRenderers({ cmd: 'set_palette', deck, name: msg.palette });
    if (msg.palette !== 'off' && msg.palette !== 'none') {
      sendAllRenderers({ cmd: 'set_palette_on', deck, value: true });
    } else {
      sendAllRenderers({ cmd: 'set_palette_on', deck, value: false });
    }
  }
  if (msg.crossfade !== undefined) {
    sendAllRenderers({ cmd: 'set_crossfade', value: msg.crossfade });
  }
  if (msg.xfade_mode) {
    sendAllRenderers({ cmd: 'set_xfade_mode', name: msg.xfade_mode });
  }
  if (msg.render_mode) {
    sendAllRenderers({ cmd: 'set_render_mode', deck, name: msg.render_mode });
  }
  if (msg.gradient) {
    sendAllRenderers({ cmd: 'set_gradient', deck, name: msg.gradient });
  }
  if (msg.color_a !== undefined) {
    sendAllRenderers({ cmd: 'set_color_a', deck, value: msg.color_a });
  }
  if (msg.color_b !== undefined) {
    sendAllRenderers({ cmd: 'set_color_b', deck, value: msg.color_b });
  }
  if (msg.ikeda !== undefined) {
    sendAllRenderers({ cmd: 'set_ikeda_mode', value: !!msg.ikeda });
  }
  if (msg.randomize) {
    sendAllRenderers({ cmd: 'randomize' });
  }
  if (msg.zoom) {
    sendAllRenderers({ cmd: 'trigger_zoom_punch', amount: msg.zoom });
  }
  if (msg.fill) {
    sendAllRenderers({ cmd: 'trigger_color_fill' });
  }
  if (msg.freeze !== undefined) {
    sendAllRenderers({ cmd: 'toggle_grid_freeze' });
  }
  if (msg.code_overlay !== undefined) {
    sendAllRenderers({ cmd: 'toggle_code_overlay' });
  }
  if (msg.preset_save) {
    sendAllRenderers({ cmd: 'preset_save', name: msg.preset_save });
  }
  if (msg.preset_load) {
    sendAllRenderers({ cmd: 'preset_load', name: msg.preset_load });
  }
}

// Forward code evals to renderers (code overlay)
function routeCodeToRenderers(msg) {
  if (msg.event === 'eval') {
    sendAllRenderers({
      type: 'evaluate_code',
      code: msg.code || '',
      userName: msg.userName || 'unknown',
    });
  }
}

// Audio-reactive: forward beat data to renderers
function routeBeatToRenderers(tick) {
  if (tick.audio && tick.audio.onset) {
    sendAllRenderers({ cmd: 'trigger_zoom_punch', amount: 0.15 + (tick.audio.bass || 0) * 0.4 });
  }
}

// Connect configured renderers
const rendererConfigs = config.renderers || {};
for (const [name, url] of Object.entries(rendererConfigs)) {
  connectRenderer(name, url);
}

// ─── Startup ─────────────────────────────────────────────
// ─── Data Feeds ──────────────────────────────────────────
const feedManager = new FeedManager((signal, data) => emit(signal, data), config.feeds || {});
feedManager.start();

// Audio analysis — captures system audio via PipeWire
startAudio(config);

// Feed audio into hub state on each tick
setInterval(() => {
  const audio = getAudio();
  state.audio = audio;
}, TICK_MS);

console.log(`[hub] CrashOS Hub ready`);
console.log(`[hub] signals: ${SIGNALS.join(', ')}`);
console.log(`[hub] waiting for clients...`);

// ─── Graceful Shutdown ──────────────────────────────────
function shutdown() {
  console.log('\n[hub] shutting down...');
  feedManager.stop();
  stopAudio();
  renderers.forEach((r) => { if (r.ws) r.ws.close(); });
  wss.clients.forEach(ws => ws.close());
  wss.close();
  httpServer.close();
  if (webtroopUpstream) webtroopUpstream.close();
  if (foxdotWs) foxdotWs.close();
  osc.close();
  console.log('[hub] bye');
  process.exit(0);
}

process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);

// Dome bridge: browser (WebSocket) <-> sclang (OSC/UDP)
//
//   node dome/bridge.mjs            then open http://localhost:8091
//
// browser -> sclang : /dome/listener x y z yaw pitch, /dome/speakers [75], /dome/monitor amp
// sclang  -> browser: /dome/levels [25 rms], /dome/note az elev spread
//
// Env: DOME_HTTP_PORT (8091), DOME_OSC_PORT (57140, where sclang sends), SCLANG_PORT (57120)

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import dgram from 'node:dgram';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(here, '../webTroop/package.json'));
const { WebSocketServer } = require('ws');

const HTTP_PORT = +(process.env.DOME_HTTP_PORT || 8091);
const OSC_PORT = +(process.env.DOME_OSC_PORT || 57140);
const SCLANG_PORT = +(process.env.SCLANG_PORT || 57120);
const SCLANG_HOST = process.env.SCLANG_HOST || '127.0.0.1';

// ---------- minimal OSC ----------
const pad4 = n => (n + 3) & ~3;
function oscString(s) {
  const b = Buffer.alloc(pad4(Buffer.byteLength(s) + 1));
  b.write(s);
  return b;
}
function encode(address, args) {
  const tags = ',' + args.map(a => (typeof a === 'string' ? 's' : 'f')).join('');
  const parts = [oscString(address), oscString(tags)];
  for (const a of args) {
    if (typeof a === 'string') parts.push(oscString(a));
    else { const b = Buffer.alloc(4); b.writeFloatBE(+a || 0); parts.push(b); }
  }
  return Buffer.concat(parts);
}
function readString(buf, off) {
  const end = buf.indexOf(0, off);
  return [buf.toString('utf8', off, end), pad4(end + 1)];
}
function decode(buf) {
  let [address, off] = readString(buf, 0);
  if (address === '#bundle') return null;
  let tags; [tags, off] = readString(buf, off);
  const args = [];
  for (const t of tags.slice(1)) {
    if (t === 'f') { args.push(buf.readFloatBE(off)); off += 4; }
    else if (t === 'i') { args.push(buf.readInt32BE(off)); off += 4; }
    else if (t === 'd') { args.push(buf.readDoubleBE(off)); off += 8; }
    else if (t === 'h') { args.push(Number(buf.readBigInt64BE(off))); off += 8; }
    else if (t === 's') { let s; [s, off] = readString(buf, off); args.push(s); }
  }
  return { address, args };
}

// ---------- UDP ----------
const udp = dgram.createSocket('udp4');
const toSclang = (address, args) => udp.send(encode(address, args), SCLANG_PORT, SCLANG_HOST);

// ---------- HTTP + WebSocket ----------
const server = http.createServer((req, res) => {
  const file = req.url === '/' ? 'dome_listener.html' : decodeURIComponent(req.url.slice(1).split('?')[0]);
  const full = path.join(here, file);
  if (!full.startsWith(here) || !fs.existsSync(full) || !full.endsWith('.html')) {
    res.writeHead(404); res.end('not found'); return;
  }
  res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
  fs.createReadStream(full).pipe(res);
});
const wss = new WebSocketServer({ server });
const broadcast = msg => {
  const s = JSON.stringify(msg);
  for (const c of wss.clients) if (c.readyState === 1) c.send(s);
};

wss.on('connection', ws => {
  console.log('browser connected');
  ws.on('message', raw => {
    let m; try { m = JSON.parse(raw); } catch { return; }
    if (m.type === 'listener') toSclang('/dome/listener', [m.x, m.y, m.z, m.yaw, m.pitch]);
    else if (m.type === 'speakers' && Array.isArray(m.pos)) toSclang('/dome/speakers', m.pos);
    else if (m.type === 'monitor') toSclang('/dome/monitor', [m.amp]);
  });
});

udp.on('message', buf => {
  const m = decode(buf);
  if (!m) return;
  if (m.address === '/dome/levels') broadcast({ type: 'levels', v: m.args });
  else if (m.address === '/dome/note') broadcast({ type: 'note', az: m.args[0], elev: m.args[1], spread: m.args[2] });
});

udp.bind(OSC_PORT, '127.0.0.1', () => {
  server.listen(HTTP_PORT, () => {
    console.log(`Dome bridge: http://localhost:${HTTP_PORT}  (OSC in :${OSC_PORT}, sclang :${SCLANG_PORT})`);
  });
});

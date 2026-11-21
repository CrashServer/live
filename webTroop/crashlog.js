// Journal des problèmes en live : logs/live-AAAAMMJJ.log (à la racine du dépôt).
// - ce que FoxDot écrit sur stderr (tracebacks, avertissements) : lu en continu, sinon le tuyau se remplit (64 Ko)
//   et FoxDot se bloque à sa prochaine écriture ;
// - la sortie de FoxDot (code, signal) s'il s'arrête ;
// - scsynth (port 57110) qui disparaît, avec la pile du plantage (coredumpctl) quand le système l'a gardée ;
// - le code évalué, horodaté, pour voir ce qui jouait juste avant.
// Branché par server.js : crashlog.watch(foxdot) puis crashlog.code(user, code) à chaque évaluation.
import { appendFileSync, mkdirSync } from 'fs';
import { execFile } from 'child_process';
import dgram from 'dgram';
import path from 'path';

const dir = path.join(path.dirname(new URL(import.meta.url).pathname), '..', 'logs');
mkdirSync(dir, { recursive: true });
// heure locale (comme coredumpctl et les journaux du système)
const local = () => { const d = new Date(); return new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString(); };
const file = () => path.join(dir, `live-${local().slice(0, 10).replace(/-/g, '')}.log`);
const stamp = () => local().replace('T', ' ').slice(0, 23);
export const log = (kind, text) => {
  try { appendFileSync(file(), `${stamp()} [${kind}] ${String(text).replace(/\n+$/, '').replace(/\n/g, '\n    ')}\n`); } catch { /* le journal ne doit jamais gêner le live */ }
};

/** Le code évalué (pour le contexte d'un plantage). */
export const code = (user, text) => log('code', `${user ?? ''}: ${text}`);

// ---- charge de scsynth : /status toutes les 2 s (ce que fait l'IDE), les 2 dernières minutes gardées ----
// À la disparition du serveur on écrit ce qui précédait : un plantage sous charge et un arrêt « propre »
// (un /quit, p. ex. un autre sclang qui démarre avec FoxDot.start dans startup.scd puis quitte) ne se lisent pas pareil.
const loadHistory = [];
const oscPad = (b) => Buffer.concat([b, Buffer.alloc(4 - (b.length % 4))]);
const STATUS_MSG = Buffer.concat([oscPad(Buffer.from('/status')), oscPad(Buffer.from(','))]);
const parseStatus = (buf) => {
  // /status.reply : 1, ugens, synths, groups, synthdefs, avgCPU, peakCPU, nominalSR, actualSR
  let i = buf.indexOf(','); if (i < 0) return null;
  const tags = buf.toString('ascii', i + 1, buf.indexOf(0, i)); i += Math.ceil((tags.length + 2) / 4) * 4;
  const v = [];
  for (const t of tags) {
    if (t === 'i') { v.push(buf.readInt32BE(i)); i += 4; }
    else if (t === 'f') { v.push(buf.readFloatBE(i)); i += 4; }
    else if (t === 'd') { v.push(buf.readDoubleBE(i)); i += 8; }
  }
  return v.length >= 7 ? { ugens: v[1], synths: v[2], avg: v[5], peak: v[6] } : null;
};
let lastHighLoad = 0;
const watchLoad = () => {
  const sock = dgram.createSocket('udp4');
  sock.on('error', () => { /* serveur absent : rien à mesurer */ });
  sock.on('message', (m) => {
    const s = parseStatus(m); if (!s) return;
    loadHistory.push({ t: stamp().slice(11, 19), ...s });
    if (loadHistory.length > 60) loadHistory.shift();
    // une pointe au-dessus de 85 % se note (au plus une fois par 10 s) : souvent le prélude d'une coupure
    if (s.peak > 85 && Date.now() - lastHighLoad > 10000) {
      lastHighLoad = Date.now();
      log('scsynth load', `pointe CPU ${s.peak.toFixed(0)} % (moy. ${s.avg.toFixed(0)} %), ${s.synths} synths, ${s.ugens} ugens`);
    }
  });
  setInterval(() => sock.send(STATUS_MSG, 57110, '127.0.0.1', () => {}), 2000).unref();
  sock.unref();
};
const loadSummary = () => {
  const last = loadHistory.slice(-15);   // ~30 s
  if (!last.length) return 'charge inconnue (pas de réponse /status)';
  const max = (k) => Math.max(...last.map((s) => s[k]));
  return `30 s avant : CPU moy. max ${max('avg').toFixed(0)} %, pointe max ${max('peak').toFixed(0)} %, ` +
    `synths max ${max('synths')}, ugens max ${max('ugens')}\n` +
    last.map((s) => `${s.t}  moy ${s.avg.toFixed(0).padStart(3)} %  pointe ${s.peak.toFixed(0).padStart(3)} %  ${s.synths} synths  ${s.ugens} ugens`).join('\n');
};

/** FoxDot : stderr et sa sortie ; scsynth : sa disparition. `onError(text)` reçoit stderr (pour l'afficher aux clients). */
export const watch = (foxdot, onError) => {
  watchLoad();
  log('start', `FoxDot démarré (pid ${foxdot.pid})`);
  foxdot.stderr?.on('data', (d) => { const t = d.toString(); log('foxdot stderr', t); try { onError?.(t); } catch { /* rien */ } });
  foxdot.on('exit', (c, sig) => log('FOXDOT EXIT', `code ${c} signal ${sig ?? '-'}`));
  let pid = null;
  setInterval(() => {
    execFile('pgrep', ['-f', 'scsynth -u 57110'], (err, out) => {
      const now = err ? null : out.trim().split('\n')[0] || null;
      if (pid && now !== pid) {
        const dead = pid;
        log('SCSYNTH DOWN', `scsynth (pid ${dead}) a disparu${now ? `, un nouveau tourne (pid ${now})` : ''}\n${loadSummary()}`);
        // les sclang lancés juste avant : un sclang dont startup.scd fait FoxDot.start quitte le serveur en sortant
        execFile('ps', ['-o', 'pid=,etimes=,args=', '-C', 'sclang'], (e, ps) => {
          const recent = (ps || '').split('\n').map((l) => l.trim()).filter((l) => l && Number(l.split(/\s+/)[1]) <= 30);
          if (recent.length) log('scsynth context', `sclang lancé(s) dans les 30 dernières secondes :\n${recent.join('\n')}`);
        });
        // la pile du plantage, si le système l'a gardée (quelques secondes après) ; sinon c'était un arrêt, pas un plantage
        setTimeout(() => execFile('coredumpctl', ['info', dead, '--no-pager'], { timeout: 8000 }, (e, info) => {
          if (!e && info) log('scsynth crash', 'PLANTAGE\n' + info.split('\n').filter((l) => /Signal|Timestamp|Stack trace of thread|#\d/.test(l)).slice(0, 24).join('\n'));
          else log('scsynth crash', 'pas de core dump : arrêt (un /quit ou un kill), pas un plantage');
        }), 4000);
      }
      if (now && now !== pid) log('scsynth', `scsynth en route (pid ${now})`);
      pid = now;
    });
  }, 2000).unref();
};

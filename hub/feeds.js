/**
 * Data Feeds Module — configurable feed registry
 *
 * Each feed: { name, fn, interval, enabled, timer }
 * All controllable at runtime via API: enable/disable, change interval, trigger now.
 *
 * Usage:
 *   import { FeedManager } from './feeds.js';
 *   const feeds = new FeedManager(emit, config);
 *   feeds.start();
 *   feeds.enable('wifi');
 *   feeds.disable('mastodon');
 *   feeds.trigger('wifi');           // run once now
 *   feeds.setInterval('news', 120);  // seconds
 *   feeds.getStatus();               // { name, enabled, interval, lastRun, lastResult }
 */

export class FeedManager {
  constructor(emit, config = {}) {
    this.emit = emit;
    this.config = config;
    this.feeds = new Map();

    // Register all built-in feeds — all default OFF, enable in config
    this.register('wifi', feedWifi, { interval: 30, enabled: config.wifi !== false });
    this.register('news', feedNews, { interval: 300, enabled: !!(config.rss && config.rss.length) });
    this.register('osm', feedGPS, { interval: 600, enabled: !!(config.lat && config.lon) });
    this.register('mastodon', feedMastodon, { interval: 60, enabled: config.mastodon === true });
    this.register('space_weather', feedSpaceWeather, { interval: 600, enabled: config.space_weather === true });
    this.register('market', feedMarket, { interval: 120, enabled: config.market === true });
    this.register('seismic', feedSeismic, { interval: 300, enabled: config.seismic === true });
  }

  register(name, fn, opts = {}) {
    this.feeds.set(name, {
      name,
      fn,
      interval: opts.interval || 60,    // seconds
      enabled: opts.enabled !== false,
      timer: null,
      lastRun: 0,
      lastResult: null,
      running: false,
    });
  }

  start() {
    console.log('[feeds] starting...');
    for (const [name, feed] of this.feeds) {
      if (feed.enabled) this._startFeed(name);
    }
    console.log(`[feeds] ${[...this.feeds.values()].filter(f => f.enabled).map(f => f.name).join(', ')}`);
  }

  stop() {
    for (const [name] of this.feeds) {
      this._stopFeed(name);
    }
  }

  enable(name) {
    const feed = this.feeds.get(name);
    if (!feed) return false;
    feed.enabled = true;
    this._startFeed(name);
    console.log(`[feeds] enabled: ${name}`);
    return true;
  }

  disable(name) {
    const feed = this.feeds.get(name);
    if (!feed) return false;
    feed.enabled = false;
    this._stopFeed(name);
    console.log(`[feeds] disabled: ${name}`);
    return true;
  }

  setInterval(name, seconds) {
    const feed = this.feeds.get(name);
    if (!feed) return false;
    feed.interval = seconds;
    if (feed.enabled) {
      this._stopFeed(name);
      this._startFeed(name);
    }
    console.log(`[feeds] ${name} interval → ${seconds}s`);
    return true;
  }

  async trigger(name) {
    const feed = this.feeds.get(name);
    if (!feed) return false;
    await this._runFeed(feed);
    return true;
  }

  getMastodonKeywords() {
    return this.config.mastodon_keywords || [];
  }

  addMastodonKeyword(keyword) {
    if (!this.config.mastodon_keywords) this.config.mastodon_keywords = [];
    keyword = keyword.trim();
    if (keyword && !this.config.mastodon_keywords.includes(keyword)) {
      this.config.mastodon_keywords.push(keyword);
      // Auto-enable mastodon feed when keywords exist
      this.enable('mastodon');
      console.log(`[feeds] mastodon keyword added: ${keyword}`);
      return true;
    }
    return false;
  }

  removeMastodonKeyword(keyword) {
    if (!this.config.mastodon_keywords) return false;
    const i = this.config.mastodon_keywords.indexOf(keyword);
    if (i >= 0) {
      this.config.mastodon_keywords.splice(i, 1);
      if (!this.config.mastodon_keywords.length) this.disable('mastodon');
      console.log(`[feeds] mastodon keyword removed: ${keyword}`);
      return true;
    }
    return false;
  }

  getRssSources() {
    return this.config.rss || [];
  }

  addRss(url) {
    if (!this.config.rss) this.config.rss = [];
    if (!this.config.rss.includes(url)) {
      this.config.rss.push(url);
      console.log(`[feeds] added RSS: ${url}`);
      return true;
    }
    return false;
  }

  removeRss(url) {
    if (!this.config.rss) return false;
    const i = this.config.rss.indexOf(url);
    if (i >= 0) {
      this.config.rss.splice(i, 1);
      console.log(`[feeds] removed RSS: ${url}`);
      return true;
    }
    return false;
  }

  getStatus() {
    const status = [];
    for (const [, feed] of this.feeds) {
      status.push({
        name: feed.name,
        enabled: feed.enabled,
        interval: feed.interval,
        lastRun: feed.lastRun,
        running: feed.running,
        lastResult: feed.lastResult,
      });
    }
    return status;
  }

  _startFeed(name) {
    const feed = this.feeds.get(name);
    if (!feed) return;
    this._stopFeed(name);
    // Run immediately
    this._runFeed(feed);
    // Then on interval
    feed.timer = setInterval(() => this._runFeed(feed), feed.interval * 1000);
  }

  _stopFeed(name) {
    const feed = this.feeds.get(name);
    if (!feed) return;
    if (feed.timer) { clearInterval(feed.timer); feed.timer = null; }
  }

  async _runFeed(feed) {
    if (feed.running) return;
    feed.running = true;
    feed.lastRun = Date.now();
    try {
      await feed.fn(this.emit, this.config);
      feed.lastResult = 'ok';
    } catch (e) {
      feed.lastResult = e.message;
    }
    feed.running = false;
  }
}

// ─── Feed Functions ─────────────────────────────────────

async function feedNews(emit, config) {
  const sources = config.rss || [];
  if (!sources.length) return;
  for (const url of sources) {
    try {
      const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
      const text = await res.text();
      // Extract feed title to filter it out from items
      const feedTitle = text.match(/<channel>.*?<title>(.*?)<\/title>/s)?.[1] || '';
      const titles = [...text.matchAll(/<title><!\[CDATA\[(.*?)\]\]>|<title>(.*?)<\/title>/g)]
        .map(m => m[1] || m[2])
        .filter(t => t && t !== feedTitle)
        .slice(0, 10);
      if (titles.length) {
        emit('data_feeds', { feed: 'news', headlines: titles, source: url, ts: Date.now() });
      }
    } catch {}
  }
}

async function feedMastodon(emit, config) {
  const instance = config.mastodon_instance || 'mastodon.social';
  const keywords = config.mastodon_keywords || [];
  if (!keywords.length) return;

  for (const keyword of keywords) {
    try {
      // Use hashtag timeline (no auth required) — strip # prefix if present
      const tag = keyword.replace(/^#/, '');
      const res = await fetch(`https://${instance}/api/v1/timelines/tag/${encodeURIComponent(tag)}?limit=10`, {
        signal: AbortSignal.timeout(8000),
      });
      const data = await res.json();
      const posts = (Array.isArray(data) ? data : []).map(s => ({
        text: (s.content || '').replace(/<[^>]*>/g, '').slice(0, 280),
        author: s.account?.username,
        ts: s.created_at,
        keyword,
      })).filter(p => p.text.length > 5);
      if (posts.length) {
        emit('data_feeds', { feed: 'mastodon', keyword, posts, instance, ts: Date.now() });
      }
    } catch {}
  }
}

async function feedWifi(emit) {
  const { execSync } = await import('child_process');
  try { execSync('nmcli dev wifi rescan 2>/dev/null', { timeout: 5000 }); } catch {}
  const raw = execSync('nmcli -t -f SSID,SIGNAL,SECURITY,BSSID dev wifi list 2>/dev/null', { timeout: 10000 }).toString();
  const networks = raw.trim().split('\n').map(line => {
    const parts = line.split(/(?<!\\):/);
    if (parts.length < 4) return null;
    return { ssid: parts[0], signal: parseInt(parts[1]) || 0, security: parts[2], bssid: parts.slice(3).join(':').replace(/\\/g, '') };
  }).filter(n => n && n.ssid);
  networks.sort((a, b) => b.signal - a.signal);
  // Deduplicate by SSID, keep strongest signal per SSID
  const seen = new Map();
  for (const n of networks) {
    const key = n.ssid || n.bssid;
    if (!seen.has(key) || seen.get(key).signal < n.signal) {
      seen.set(key, n);
    }
  }
  const unique = [...seen.values()].sort((a, b) => b.signal - a.signal);
  emit('data_feeds', { feed: 'wifi', networks: unique, count: unique.length, ts: Date.now() });
}

async function feedGPS(emit, config) {
  const lat = config.lat || null;
  const lon = config.lon || null;
  if (!lat || !lon) return;
  const radius = config.osm_radius || 500;
  const query = `[out:json][timeout:10];(way["building"](around:${radius},${lat},${lon}););out body;>;out skel qt;`;
  const res = await fetch('https://overpass-api.de/api/interpreter', {
    method: 'POST',
    body: `data=${encodeURIComponent(query)}`,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    signal: AbortSignal.timeout(15000),
  });
  const data = await res.json();
  emit('data_feeds', { feed: 'osm', buildings: data.elements?.length || 0, elements: data.elements?.slice(0, 200), center: { lat, lon }, ts: Date.now() });
}

async function feedSpaceWeather(emit) {
  try {
    const res = await fetch('https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json', { signal: AbortSignal.timeout(5000) });
    const data = await res.json();
    emit('data_feeds', { feed: 'space_weather', data: data[data.length - 1], ts: Date.now() });
  } catch {}
  try {
    const res = await fetch('https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json', { signal: AbortSignal.timeout(5000) });
    const data = await res.json();
    emit('data_feeds', { feed: 'kp_index', kp: data[data.length - 1], ts: Date.now() });
  } catch {}
}

async function feedMarket(emit) {
  const res = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true', { signal: AbortSignal.timeout(5000) });
  const data = await res.json();
  emit('data_feeds', { feed: 'crypto', data, ts: Date.now() });
}

async function feedSeismic(emit) {
  const res = await fetch('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson', { signal: AbortSignal.timeout(5000) });
  const data = await res.json();
  const quakes = (data.features || []).map(f => ({ mag: f.properties.mag, place: f.properties.place, time: f.properties.time, coords: f.geometry.coordinates }));
  emit('data_feeds', { feed: 'seismic', quakes, count: quakes.length, ts: Date.now() });
}

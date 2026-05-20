#!/usr/bin/env node
/**
 * clift2 ↔ hub bridge
 *
 * Connects to both clift2's WS server and the hub.
 * - Hub signals (beat, audio, code, render, data_feeds...) → clift2 commands
 * - clift2 state → hub (so hub knows what clift2 is displaying)
 *
 * Usage: node clift2_bridge.js [hub-url] [clift2-url] [name]
 *   default: ws://localhost:1235  ws://localhost:9999  clift2_main
 */

import WebSocket from 'ws';

const HUB_URL = process.argv[2] || 'ws://localhost:1235';
const CLIFT_URL = process.argv[3] || 'ws://localhost:9999';
const CLIENT_NAME = process.argv[4] || 'clift2_main';

let hub = null;
let clift = null;
let hubConnected = false;
let cliftConnected = false;
let cliftState = {};  // last known clift2 state

// ── Connect to Hub ──
function connectHub() {
  hub = new WebSocket(HUB_URL);
  hub.on('open', () => {
    hubConnected = true;
    console.log(`[bridge] connected to hub at ${HUB_URL}`);
    hub.send(JSON.stringify({
      type: 'identify',
      role: 'renderer',
      name: CLIENT_NAME,
      subscribe: ['beat', 'audio', 'code', 'render', 'grid', 'phase', 'players', 'data_feeds', 'public', 'lights'],
    }));
  });

  hub.on('message', (raw) => {
    try {
      const msg = JSON.parse(raw);
      routeToClift(msg);
    } catch {}
  });

  hub.on('close', () => {
    hubConnected = false;
    console.log('[bridge] hub disconnected, retrying...');
    setTimeout(connectHub, 3000);
  });
  hub.on('error', () => {});
}

// ── Connect to clift2 ──
function connectClift() {
  clift = new WebSocket(CLIFT_URL);
  clift.on('open', () => {
    cliftConnected = true;
    console.log(`[bridge] connected to clift2 at ${CLIFT_URL}`);
    sendClift({ cmd: 'get_state' });
  });

  clift.on('message', (raw) => {
    try {
      const msg = JSON.parse(raw);
      if (msg.type === 'state') {
        cliftState = msg;
        // Report state to hub
        if (hubConnected) {
          hub.send(JSON.stringify({
            type: 'emit',
            signal: 'stats',
            data: {
              event: 'renderer_state',
              renderer: CLIENT_NAME,
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
            },
          }));
        }
      }
    } catch {}
  });

  clift.on('close', () => {
    cliftConnected = false;
    console.log('[bridge] clift2 disconnected, retrying...');
    setTimeout(connectClift, 3000);
  });
  clift.on('error', () => {});
}

function sendClift(msg) {
  if (clift && cliftConnected) {
    clift.send(JSON.stringify(msg));
  }
}

// ── Route hub signals → clift2 commands ──
let beatCount = 0;

function routeToClift(msg) {
  if (!cliftConnected) return;

  switch (msg.type) {
    case 'beat': {
      beatCount = msg.beat || 0;
      // Audio-reactive mappings
      if (msg.audio) {
        if (msg.audio.onset) {
          sendClift({ cmd: 'trigger_zoom_punch', amount: 0.15 + msg.audio.bass * 0.4 });
        }
      }
      break;
    }

    case 'render': {
      // Full render command — the main control path
      // scene, fx, palette, crossfade, deck, ikeda, randomize, colors, render_mode, gradient
      const deck = msg.deck || 'a';

      if (msg.scene) {
        sendClift({ cmd: 'set_scene', deck, name: msg.scene });
        console.log(`[bridge] scene → ${msg.scene} (deck ${deck})`);
      }
      if (msg.fx) {
        sendClift({ cmd: 'set_fx', deck, name: msg.fx });
        console.log(`[bridge] fx → ${msg.fx} (deck ${deck})`);
      }
      if (msg.palette) {
        sendClift({ cmd: 'set_palette', deck, name: msg.palette });
        sendClift({ cmd: 'set_palette_on', deck, value: true });
        console.log(`[bridge] palette → ${msg.palette} (deck ${deck})`);
      }
      if (msg.palette === 'off' || msg.palette === 'none') {
        sendClift({ cmd: 'set_palette_on', deck, value: false });
      }
      if (msg.crossfade !== undefined) {
        sendClift({ cmd: 'set_crossfade', value: msg.crossfade });
        console.log(`[bridge] crossfade → ${msg.crossfade}`);
      }
      if (msg.xfade_mode) {
        sendClift({ cmd: 'set_xfade_mode', name: msg.xfade_mode });
      }
      if (msg.render_mode) {
        sendClift({ cmd: 'set_render_mode', deck, name: msg.render_mode });
      }
      if (msg.gradient) {
        sendClift({ cmd: 'set_gradient', deck, name: msg.gradient });
      }
      if (msg.color_a !== undefined) {
        sendClift({ cmd: 'set_color_a', deck, value: msg.color_a });
      }
      if (msg.color_b !== undefined) {
        sendClift({ cmd: 'set_color_b', deck, value: msg.color_b });
      }
      if (msg.ikeda !== undefined) {
        sendClift({ cmd: 'set_ikeda_mode', value: !!msg.ikeda });
        console.log(`[bridge] ikeda → ${msg.ikeda}`);
      }
      if (msg.randomize) {
        sendClift({ cmd: 'randomize' });
        console.log(`[bridge] randomize!`);
      }
      if (msg.zoom) {
        sendClift({ cmd: 'trigger_zoom_punch', amount: msg.zoom });
      }
      if (msg.fill) {
        sendClift({ cmd: 'trigger_color_fill' });
      }
      if (msg.freeze !== undefined) {
        sendClift({ cmd: 'toggle_grid_freeze' });
      }
      if (msg.charset !== undefined) {
        sendClift({ cmd: 'set_charset', value: msg.charset });
      }
      if (msg.code_overlay !== undefined) {
        sendClift({ cmd: 'toggle_code_overlay' });
      }
      // Preset support
      if (msg.preset_save) {
        sendClift({ cmd: 'preset_save', name: msg.preset_save });
      }
      if (msg.preset_load) {
        sendClift({ cmd: 'preset_load', name: msg.preset_load });
      }
      break;
    }

    case 'code': {
      if (msg.event === 'eval') {
        sendClift({
          type: 'evaluate_code',
          code: msg.code || '',
          userName: msg.userName || 'unknown',
        });
      }
      break;
    }

    case 'data_feeds': {
      if (msg.feed === 'wifi') {
        const ssids = (msg.networks || []).slice(0, 5).map(n => n.ssid).join(' | ');
        if (ssids) sendClift({ type: 'evaluate_code', code: ssids, userName: 'wifi' });
      }
      if (msg.feed === 'seismic' && msg.count > 0) {
        sendClift({ cmd: 'trigger_zoom_punch', amount: 0.8 });
      }
      if (msg.feed === 'news') {
        const headline = (msg.headlines || [])[0];
        if (headline) sendClift({ type: 'evaluate_code', code: headline, userName: 'news' });
      }
      break;
    }

    case 'public': {
      if (msg.event === 'tap') {
        sendClift({ cmd: 'trigger_color_fill' });
      }
      break;
    }

    case 'phase': {
      // Optional: map phases to scenes
      break;
    }
  }
}

// ── Start ──
console.log(`[bridge] clift2 ↔ hub bridge`);
console.log(`[bridge] hub:   ${HUB_URL}`);
console.log(`[bridge] clift: ${CLIFT_URL}`);
console.log(`[bridge] name:  ${CLIENT_NAME}`);

connectHub();
connectClift();

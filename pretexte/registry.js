// Module + Scene registry.
// Module contract: { id, enable?, disable?, tick?(reactive, dt) }
// Scene:           { name, modules: [id, id, ...] }

const modules      = new Map();
const enabledIds   = new Set();
let   scenes       = [];
let   currentScene = 0;
let   onSceneChange = null;

export function setSceneChangeHandler(fn) { onSceneChange = fn; }

export function registerModule(mod) {
  if (!mod || !mod.id) throw new Error('Module needs an id');
  modules.set(mod.id, mod);
}

export function setScenes(sceneList) {
  scenes = sceneList;
}

export function getScenes() { return scenes; }
export function getCurrentScene() { return scenes[currentScene]; }

function enable(id) {
  if (enabledIds.has(id)) return;
  const mod = modules.get(id);
  if (!mod) { console.warn(`Module not found: ${id}`); return; }
  enabledIds.add(id);
  if (mod.enable) mod.enable();
}

function disable(id) {
  if (!enabledIds.has(id)) return;
  const mod = modules.get(id);
  enabledIds.delete(id);
  if (mod && mod.disable) mod.disable();
}

export function loadScene(name) {
  const idx = scenes.findIndex(s => s.name === name);
  if (idx < 0) { console.warn(`Scene not found: ${name}`); return false; }
  currentScene = idx;
  const wanted = new Set(scenes[idx].modules || []);
  // Disable modules not in the new scene
  for (const id of [...enabledIds]) {
    if (!wanted.has(id)) disable(id);
  }
  // Enable modules in the new scene
  for (const id of wanted) enable(id);
  // Swap body scene class so CSS can style baseline per scene
  const body = document.body;
  [...body.classList].forEach(c => { if (c.startsWith('scene-')) body.classList.remove(c); });
  body.classList.add(`scene-${name}`);
  // Notify listener (app.js uses this to trigger a re-render on mode change)
  if (onSceneChange) onSceneChange(scenes[idx]);
  return true;
}

export function cycleScene() {
  currentScene = (currentScene + 1) % Math.max(1, scenes.length);
  const s = scenes[currentScene];
  if (s) loadScene(s.name);
  return s;
}

export function tickModules(reactive, dt) {
  for (const id of enabledIds) {
    const mod = modules.get(id);
    if (mod && mod.tick) mod.tick(reactive, dt);
  }
}

export function isEnabled(id) { return enabledIds.has(id); }
export function enabledList() { return [...enabledIds]; }

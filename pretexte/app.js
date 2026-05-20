import { prepare, layout } from '@chenglou/pretext';
import { reactive, handleWsMessage, tickReactive } from './reactive.js';
import { registerModule, setScenes, tickModules, getCurrentScene, setSceneChangeHandler } from './registry.js';
import { SCENES } from './scenes.js';
import { initControl } from './control.js';
import { initReadout, tickReadout } from './readout.js';
import { bpmPulse }  from './effects/bpm-pulse.js';
import { cpuHeat }   from './effects/cpu-heat.js';
import { echo }      from './effects/echo.js';
import { warp }      from './effects/warp.js';
import { orb }       from './effects/orb.js';
import { evalFlash } from './effects/eval-flash.js';
import { explode }   from './effects/explode.js';
import { attractor } from './effects/attractor.js';
import { repulsor }  from './effects/repulsor.js';
import { charWobble }  from './effects/char-wobble.js';
import { charShatter } from './effects/char-shatter.js';
import { charGlitch }  from './effects/char-glitch.js';
import { charRainbow } from './effects/char-rainbow.js';
import { charErode }   from './effects/char-erode.js';
import { charAudio }   from './effects/char-audio.js';
import { initAudio, tickAudio, audioState } from './audio.js';
import { renderCharacters, clearCharRenderer } from './engine/charrenderer.js';
import { enableFlow, disableFlow, tickFlow, renderFlow } from './engine/flowrenderer.js';

/* ─── Font-fit config (unchanged from baseline) ─────────────────────────── */
const FONT_CONFIG = {
    MIN_FONT_SIZE: 6,
    MAX_FONT_SIZE: 200,
    FONT_FAMILY: 'InterBlack, Courier New, monospace',
    LINE_HEIGHT_MULTIPLIER: 0.8
};

let lastCalculatedFontSize = null;
let containerDimensions    = null;
let lastLineCount          = null;
let lastTextContent        = null;

async function calculateOptimalFontSize(text, containerWidth, containerHeight) {
    try {
        let minSize = FONT_CONFIG.MIN_FONT_SIZE;
        let maxSize = FONT_CONFIG.MAX_FONT_SIZE;
        let optimalSize = minSize;
        const lineHeightMultiplier = FONT_CONFIG.LINE_HEIGHT_MULTIPLIER;
        const padding = 80;
        const availableHeight = containerHeight - padding * 4;
        const availableWidth  = containerWidth  - padding;

        for (let i = 0; i < 20; i++) {
            const testSize = (minSize + maxSize) / 2;
            const cssFont = `${testSize}px ${FONT_CONFIG.FONT_FAMILY}`;
            const prepared = prepare(text, cssFont);
            const lineHeightAbsolute = testSize * lineHeightMultiplier;
            const result = layout(prepared, availableWidth, lineHeightAbsolute);
            if (result.height <= availableHeight) { optimalSize = testSize; minSize = testSize; }
            else { maxSize = testSize; }
            if (maxSize - minSize < 0.5) break;
        }
        return Math.round(optimalSize * 10) / 10;
    } catch (error) {
        console.error('Failed to calculate optimal font size:', error);
        return null;
    }
}

function applyFontSize(fontSize) {
    if (fontSize && fontSize > 0) {
        codeContainer.style.setProperty('--font-size', `${fontSize}px`);
        lastCalculatedFontSize = fontSize;
    }
}

function initializeContainerDimensions() {
    const r = codeContainer.getBoundingClientRect();
    containerDimensions = { width: r.width, height: r.height };
}

async function calculateFontSize(allText) {
    if (!containerDimensions) initializeContainerDimensions();
    const lineCount = allText.split('\n').length;
    if (lastLineCount === lineCount && lastCalculatedFontSize && lastTextContent === allText) return;
    lastLineCount = lineCount;
    lastTextContent = allText;
    const optimal = await calculateOptimalFontSize(allText, containerDimensions.width, containerDimensions.height);
    if (optimal) applyFontSize(optimal);
}

function handleWindowResize() {
    containerDimensions = null;
    lastCalculatedFontSize = null;
    lastLineCount = null;
}

/* ─── DOM refs ──────────────────────────────────────────────────────────── */
const codeContainer = document.getElementById('code-container');
const statusElement = document.getElementById('status');

/* ─── Player WS state ───────────────────────────────────────────────────── */
const players = {
    zbdmInstantCode: { windowLines: '', currentLineNumber: 0, cursorCh: 0, windowStartLine: 0, windowEndLine: 0, lastUpdate: 0 },
    svdkInstantCode: { windowLines: '', currentLineNumber: 0, cursorCh: 0, windowStartLine: 0, windowEndLine: 0, lastUpdate: 0 },
};
let lastUpdatedPlayer = null;
let ws = null;
let config = null;

const defaultConfig = { HOST_IP: '192.168.1.38', FOXDOT_WS_PORT: 20000 };

async function loadConfig() {
    try {
        const response = await fetch('config.json', { cache: 'no-store' });
        if (response.ok) {
            config = await response.json();
            console.log('✓ Configuration chargée depuis config.json:', config);
            connectWebSocket();
            return;
        }
    } catch {
        console.log('⚠ config.json indisponible, utilisation des valeurs par défaut');
    }
    config = defaultConfig;
    console.log('Configuration par défaut:', config);
    connectWebSocket();
}

function connectWebSocket() {
    try {
        ws = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);

        ws.onopen = () => { console.log('✓ WebSocket connecté'); updateStatus(true); };

        ws.onmessage = (event) => {
            try {
                const message = JSON.parse(event.data);

                // Ambient signals → reactive store (BPM, CPU, sceneName)
                handleWsMessage(message);

                // Code windows → player-specific state → trigger re-render
                if (message.type && message.type.endsWith('InstantCode')) {
                    const playerType = message.type;
                    if (players[playerType] && message.windowLines !== undefined) {
                        const p = players[playerType];
                        p.windowLines       = message.windowLines;
                        p.windowStartLine   = message.windowStartLine || 0;
                        p.windowEndLine     = message.windowEndLine   || 0;
                        p.currentLineNumber = message.currentLineNumber || 0;
                        p.cursorCh          = message.position || 0;
                        p.lastUpdate        = Date.now();
                        lastUpdatedPlayer   = playerType;
                        renderCode();
                    }
                }
            } catch (error) {
                console.error('Erreur parsing message:', error);
            }
        };

        ws.onerror = (error) => { console.error('✗ WebSocket erreur:', error); updateStatus(false); };
        ws.onclose = () => { console.log('⚠ WebSocket fermé, reconnexion dans 3s...'); updateStatus(false); setTimeout(connectWebSocket, 3000); };
    } catch (error) {
        console.error('✗ Erreur connexion WebSocket:', error);
        updateStatus(false);
        setTimeout(connectWebSocket, 3000);
    }
}

/* ─── Merge & render ────────────────────────────────────────────────────── */
function mergePlayerWindows() {
    const zbdm = players.zbdmInstantCode;
    const svdk = players.svdkInstantCode;
    const lineMap = new Map();

    if (zbdm.windowLines) {
        zbdm.windowLines.split('\n').forEach((text, index) => {
            const lineNum = zbdm.windowStartLine + index;
            if (!lineMap.has(lineNum)) lineMap.set(lineNum, { text, from: [] });
            if (!lineMap.get(lineNum).from.includes('zbdm')) lineMap.get(lineNum).from.push('zbdm');
        });
    }
    if (svdk.windowLines) {
        svdk.windowLines.split('\n').forEach((text, index) => {
            const lineNum = svdk.windowStartLine + index;
            if (!lineMap.has(lineNum)) lineMap.set(lineNum, { text, from: [] });
            else if (lastUpdatedPlayer === 'svdkInstantCode') lineMap.get(lineNum).text = text;
            if (!lineMap.get(lineNum).from.includes('svdk')) lineMap.get(lineNum).from.push('svdk');
        });
    }

    const sortedLineNums = [...lineMap.keys()].sort((a, b) => a - b);
    return sortedLineNums.map(n => ({ lineNumber: n, text: lineMap.get(n).text, from: lineMap.get(n).from }));
}

/* Focus cone: active line biggest (1.0), lines fall off to 0.55 at distance 5+.
 * Always-on — part of the core renderer, not a toggleable module. */
function focusConeScale(lineNumber, activeLines) {
    if (!activeLines.length) return 1.0;
    const d = Math.min(...activeLines.map(n => Math.abs(lineNumber - n)));
    // Smooth falloff: 1.0 at d=0, ~0.55 at d=5, asymptotic
    return Math.max(0.55, 1.0 - d * 0.09);
}

let lastMode = null;

function renderCode() {
    const scene = getCurrentScene();
    const mode  = scene?.mode || 'line';

    // On mode transition, clear the OTHER mode's DOM and start new engine
    if (mode !== lastMode) {
        if (lastMode === 'char') clearCharRenderer();
        if (lastMode === 'line') {
            for (const s of codeContainer.querySelectorAll('.code-line')) s.remove();
        }
        if (lastMode === 'flow') disableFlow();
        if (mode === 'flow') enableFlow();
        lastMode = mode;
    }

    const displayLines = mergePlayerWindows();

    if (displayLines.length === 0) {
        if (mode === 'line') codeContainer.textContent = '...';
        return;
    }

    const allText = displayLines.map(l => l.text).join('\n');
    calculateFontSize(allText);

    const zbdm = players.zbdmInstantCode;
    const svdk = players.svdkInstantCode;
    const activeLines = [zbdm.currentLineNumber, svdk.currentLineNumber].filter(n => n > 0);

    if (mode === 'char') {
        // Character-layout engine path
        const base = lastCalculatedFontSize || 48;
        const font = `${base}px ${FONT_CONFIG.FONT_FAMILY}`;
        const lineH = base * FONT_CONFIG.LINE_HEIGHT_MULTIPLIER;
        const lineNumToIdx = new Map();
        displayLines.forEach((l, i) => lineNumToIdx.set(l.lineNumber, i));
        const activeLocal = new Set(activeLines.map(n => lineNumToIdx.get(n)).filter(i => i !== undefined));
        const maxWidth = (containerDimensions?.width || window.innerWidth) - 40;
        renderCharacters(codeContainer, allText, font, maxWidth, lineH, { activeLines: activeLocal });
        return;
    }

    if (mode === 'flow') {
        // Obstacle-flow engine path — text wraps around a moving SVG circle
        const base = lastCalculatedFontSize || 48;
        const font = `${base}px ${FONT_CONFIG.FONT_FAMILY}`;
        const lineH = base * FONT_CONFIG.LINE_HEIGHT_MULTIPLIER;
        const maxWidth = (containerDimensions?.width || window.innerWidth) - 40;
        renderFlow(codeContainer, allText, font, maxWidth, lineH);
        return;
    }

    codeContainer.innerHTML = '';

    displayLines.forEach(({ lineNumber, text }) => {
        const lineSpan = document.createElement('span');
        lineSpan.className = 'code-line';

        const isZbdm = (lineNumber === zbdm.currentLineNumber);
        const isSvdk = (lineNumber === svdk.currentLineNumber);
        const base = lastCalculatedFontSize || 48;
        const coneScale = focusConeScale(lineNumber, activeLines);

        lineSpan.dataset.lineNumber = lineNumber;
        if (isZbdm) lineSpan.classList.add('active', 'zbdm');
        if (isSvdk) lineSpan.classList.add('active', 'svdk');

        // Active lines: enforce min readable size; inactive: apply focus cone
        if (isZbdm || isSvdk) {
            lineSpan.style.fontSize = `${Math.max(48, base)}px`;
        } else {
            lineSpan.style.fontSize = `${base * coneScale}px`;
            lineSpan.style.opacity  = (0.6 + coneScale * 0.4).toFixed(2);
        }

        if (isZbdm && isSvdk)      renderLineWithTwoCursors(lineSpan, text, zbdm.cursorCh, 'zbdm', svdk.cursorCh, 'svdk');
        else if (isZbdm)           renderLineWithCursor(lineSpan, text, zbdm.cursorCh, 'zbdm');
        else if (isSvdk)           renderLineWithCursor(lineSpan, text, svdk.cursorCh, 'svdk');
        else                       lineSpan.textContent = text || '';

        codeContainer.appendChild(lineSpan);
    });

    if (lastUpdatedPlayer && players[lastUpdatedPlayer].currentLineNumber > 0) {
        const actives = document.querySelectorAll('.code-line.active');
        if (actives.length > 0) actives[actives.length - 1].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function renderLineWithCursor(lineSpan, text, cursorCh, playerType) {
    const safePos = Math.min(Math.max(0, cursorCh), text.length);
    lineSpan.appendChild(document.createTextNode(text.substring(0, safePos)));
    const cursor = document.createElement('span');
    cursor.className = `cursor cursor-${playerType}`;
    lineSpan.appendChild(cursor);
    lineSpan.appendChild(document.createTextNode(text.substring(safePos)));
}

function renderLineWithTwoCursors(lineSpan, text, ch1, pt1, ch2, pt2) {
    const safe1 = Math.min(Math.max(0, ch1), text.length);
    const safe2 = Math.min(Math.max(0, ch2), text.length);
    const positions = [{ pos: safe1, playerType: pt1 }, { pos: safe2, playerType: pt2 }].sort((a, b) => a.pos - b.pos);
    let lastPos = 0;
    positions.forEach((item) => {
        if (item.pos > lastPos) lineSpan.appendChild(document.createTextNode(text.substring(lastPos, item.pos)));
        const cursor = document.createElement('span');
        cursor.className = `cursor cursor-${item.playerType}`;
        lineSpan.appendChild(cursor);
        lastPos = item.pos;
    });
    if (lastPos < text.length) lineSpan.appendChild(document.createTextNode(text.substring(lastPos)));
}

function updateStatus(connected) {
    if (connected)       statusElement.className = 'status connected';
    else { statusElement.textContent = 'Déconnecté'; statusElement.className = 'status disconnected'; }
}

/* ─── Main rAF loop: reactive tick + module tick + readout ──────────────── */
function startReactiveLoop() {
    function frame() {
        const dt = tickReactive();
        tickAudio();
        tickModules(reactive, dt);
        tickReadout(reactive);
        // Flow mode needs a continuous reflow every frame because the obstacle moves
        const scene = getCurrentScene();
        if (scene?.mode === 'flow') {
            tickFlow();
            renderCode();
        }
        requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
}

/* ─── Bootstrap ─────────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('resize', handleWindowResize);

    // Register all effect modules
    registerModule(bpmPulse);
    registerModule(cpuHeat);
    registerModule(echo);
    registerModule(warp);
    registerModule(orb);
    registerModule(evalFlash);
    registerModule(explode);
    registerModule(attractor);
    registerModule(repulsor);
    registerModule(charWobble);
    registerModule(charShatter);
    registerModule(charGlitch);
    registerModule(charRainbow);
    registerModule(charErode);
    registerModule(charAudio);

    // First user gesture → request mic permission for audio-reactive effects.
    const unlockAudio = () => { initAudio(); };
    window.addEventListener('keydown', unlockAudio, { once: true });
    window.addEventListener('click',   unlockAudio, { once: true });

    // Publish the scene list + initial load (via URL hash)
    setScenes(SCENES);
    setSceneChangeHandler(() => renderCode());
    initReadout();
    initControl();

    // Start everything
    startReactiveLoop();
    loadConfig();
});

import { prepare, layout } from '@chenglou/pretext';
// Configuration for dynamic font sizing
const FONT_CONFIG = {
    MIN_FONT_SIZE: 6,
    MAX_FONT_SIZE: 200,
    FONT_FAMILY: 'InterBlack, Courier New, monospace',
    LINE_HEIGHT_MULTIPLIER: 1.1
};


// Font size calculation
let lastCalculatedFontSize = null;
let containerDimensions = null;
let lastLineCount = null;
let lastTextContent = null;
let recalcAttempts = 0;
const MAX_RECALC_ATTEMPTS = 5;

/**
 * Calculate optimal font size to fit text in container using binary search
 * @param {string} text - The text to measure
 * @param {number} containerWidth - Available width in pixels
 * @param {number} containerHeight - Available height in pixels
 * @returns {Promise<number|null>} - Optimal font size in pixels, or null on failure
 */
async function calculateOptimalFontSize(text, containerWidth, containerHeight) {

    try {
        let minSize = FONT_CONFIG.MIN_FONT_SIZE;
        // Reduce max size by 20% for each recalc attempt after the first
        let maxSize = FONT_CONFIG.MAX_FONT_SIZE * Math.pow(0.8, Math.max(0, recalcAttempts - 1));
        let optimalSize = minSize;
        const lineHeightMultiplier = FONT_CONFIG.LINE_HEIGHT_MULTIPLIER;
        const padding = 80; // total padding (top + bottom + buffer for safety)
        const availableHeight = containerHeight - padding;
        const availableWidth = containerWidth - padding;

        // Binary search for the largest font size that fits
        for (let i = 0; i < 15; i++) {
            const testSize = (minSize + maxSize) / 2;
            const cssFont = `${testSize}px ${FONT_CONFIG.FONT_FAMILY}`;

            try {
                const prepared = prepare(text, cssFont);
                const lineHeightAbsolute = testSize * lineHeightMultiplier;
                const result = layout(prepared, availableWidth, lineHeightAbsolute);

                // Check if text fits in height
                if (result.height <= availableHeight) {
                    optimalSize = testSize;
                    minSize = testSize;
                } else {
                    maxSize = testSize;
                }
            } catch (e) {
                console.warn('Error during font size calculation:', e);
                maxSize = testSize;
            }
        }

        return Math.round(optimalSize * 10) / 10; // Round to 0.1px
    } catch (error) {
        console.error('Failed to calculate optimal font size:', error);
        return null;
    }
}

/**
 * Apply calculated font size to the container
 * @param {number} fontSize - Font size in pixels
 */
function applyFontSize(fontSize) {
    if (fontSize && fontSize > 0) {
        codeContainer.style.setProperty('--font-size', `${fontSize}px`);
        lastCalculatedFontSize = fontSize;
    }
}

/**
 * Initialize container dimensions (called once on page load)
 */
function initializeContainerDimensions() {
    const containerRect = codeContainer.getBoundingClientRect();
    containerDimensions = {
        width: containerRect.width,
        height: containerRect.height
    };
}

/**
 * Check if content overflows and needs font size adjustment
 */
function checkContentOverflow() {
    const scrollHeight = codeContainer.scrollHeight;
    const clientHeight = codeContainer.clientHeight;
    const padding = 10;
    const overflows = scrollHeight > clientHeight + padding;

    return overflows;
}

/**
 * Font size calculation - recalculates only if line count changes
 */
async function calculateFontSize(allText) {
    // Lazy initialization of container dimensions on first use
    if (!containerDimensions) {
        initializeContainerDimensions();
    }

    const lineCount = allText.split('\n').filter(line => line.trim().length > 0).length;
    // Skip if nothing changed and we have a valid size
    if (lastLineCount === lineCount && lastCalculatedFontSize && lastTextContent === allText) {
        return;
    }

    recalcAttempts++;
    if (recalcAttempts > MAX_RECALC_ATTEMPTS) {
        return;
    }
    lastLineCount = lineCount;
    lastTextContent = allText;

    const optimalSize = await calculateOptimalFontSize(
        allText,
        containerDimensions.width,
        containerDimensions.height
    );

    if (optimalSize) {
        applyFontSize(optimalSize);
    }
}

/**
 * Reset font size calculation when window is resized
 */
function handleWindowResize() {
    containerDimensions = null;
    lastCalculatedFontSize = null;
    lastLineCount = null;
    console.log('Window resized - container dimensions will be recalculated');
}

const codeContainer = document.getElementById('code-container');
const statusElement = document.getElementById('status');

// Structure pour stocker les données de chaque joueur séparément
const players = {
    zbdmInstantCode: {
        windowLines: '',
        currentLineNumber: 0,
        cursorCh: 0,
        windowStartLine: 0,
        windowEndLine: 0,
        lastUpdate: 0
    },
    svdkInstantCode: {
        windowLines: '',
        currentLineNumber: 0,
        cursorCh: 0,
        windowStartLine: 0,
        windowEndLine: 0,
        lastUpdate: 0
    }
};

let lastUpdatedPlayer = null;
let ws = null;
let config = null;

const defaultConfig = {
    HOST_IP: '192.168.1.42',
    FOXDOT_WS_PORT: 20000
};

async function loadConfig() {
    try {
        console.log('1️⃣  Tentative: charger config.json local...');
        const response = await fetch('config.json');
        if (response.ok) {
            config = await response.json();
            console.log('✓ Configuration chargée depuis ./pretexte/config.json:', config);
            connectWebSocket();
            return;
        }
    } catch (error) {
        console.log('⚠ Échec (normal si pas de serveur)');
    }

    try {
        console.log('2️⃣  Tentative: charger ../../crash_config.json...');
        const response = await fetch('../../crash_config.json');
        if (response.ok) {
            config = await response.json();
            console.log('✓ Configuration chargée depuis ../../crash_config.json:', config);
            connectWebSocket();
            return;
        }
    } catch (error) {
        console.log('⚠ Échec');
    }

    console.log('3️⃣  Utilisation de la configuration par défaut');
    config = defaultConfig;
    console.log('Configuration utilisée:', config);
    connectWebSocket();
}

function connectWebSocket() {
    try {
        ws = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);

        ws.onopen = () => {
            console.log('✓ WebSocket connecté');
            updateStatus(true);
        };

        ws.onmessage = (event) => {
            try {
                const message = JSON.parse(event.data);

                if (message.type && message.type.endsWith('InstantCode')) {
                    const playerType = message.type;

                    if (players[playerType]) {
                        if (message.windowLines !== undefined) {
                            players[playerType].windowLines = message.windowLines;
                            players[playerType].windowStartLine = message.windowStartLine || 0;
                            players[playerType].windowEndLine = message.windowEndLine || 0;
                            players[playerType].currentLineNumber = message.currentLineNumber || 0;
                            players[playerType].cursorCh = message.position || 0;
                            players[playerType].lastUpdate = Date.now();

                            lastUpdatedPlayer = playerType;
                            renderCode();
                        }
                    }
                }
            } catch (error) {
                console.error('Erreur parsing message:', error);
            }
        };

        ws.onerror = (error) => {
            console.error('✗ WebSocket erreur:', error);
            updateStatus(false);
        };

        ws.onclose = () => {
            console.log('⚠ WebSocket fermé, reconnexion dans 3s...');
            updateStatus(false);
            setTimeout(connectWebSocket, 3000);
        };
    } catch (error) {
        console.error('✗ Erreur connexion WebSocket:', error);
        updateStatus(false);
        setTimeout(connectWebSocket, 3000);
    }
}

/**
 * Fusionner les fenêtres de lignes en un flux continu sans séparateur
 */
function mergePlayerWindows() {
    const zbdm = players.zbdmInstantCode;
    const svdk = players.svdkInstantCode;

    // Créer une map de toutes les lignes
    const lineMap = new Map();

    // Ajouter les lignes de zbdm
    if (zbdm.windowLines) {
        const zbdmLines = zbdm.windowLines.split('\n');
        zbdmLines.forEach((text, index) => {
            const lineNum = zbdm.windowStartLine + index;
            if (!lineMap.has(lineNum)) {
                lineMap.set(lineNum, { text, from: [] });
            }
            if (!lineMap.get(lineNum).from.includes('zbdm')) {
                lineMap.get(lineNum).from.push('zbdm');
            }
        });
    }

    // Ajouter les lignes de svdk (fusion en cas de chevauchement)
    if (svdk.windowLines) {
        const svdkLines = svdk.windowLines.split('\n');
        svdkLines.forEach((text, index) => {
            const lineNum = svdk.windowStartLine + index;
            if (!lineMap.has(lineNum)) {
                lineMap.set(lineNum, { text, from: [] });
            } else {
                // Si chevauchement, priorité au dernier joueur qui a écrit
                if (lastUpdatedPlayer === 'svdkInstantCode') {
                    lineMap.get(lineNum).text = text;
                }
            }
            if (!lineMap.get(lineNum).from.includes('svdk')) {
                lineMap.get(lineNum).from.push('svdk');
            }
        });
    }

    // Trier par numéro de ligne
    const sortedLineNums = Array.from(lineMap.keys()).sort((a, b) => a - b);

    return sortedLineNums.map(lineNum => ({
        lineNumber: lineNum,
        text: lineMap.get(lineNum).text,
        from: lineMap.get(lineNum).from
    }));
}

function renderCode() {
    codeContainer.innerHTML = '';

    // Reset recalc attempts for this render cycle
    recalcAttempts = 0;

    const displayLines = mergePlayerWindows()
        .filter(line => line.text.trim().length > 0);

    if (displayLines.length === 0) {
        codeContainer.textContent = '...';
        return;
    }

    // Font size calculation based on content
    const allText = displayLines.map(line => line.text).join('\n');
    calculateFontSize(allText);

    const zbdm = players.zbdmInstantCode;
    const svdk = players.svdkInstantCode;

    displayLines.forEach(({ lineNumber, text, from }) => {
        const lineSpan = document.createElement('span');
        lineSpan.className = 'code-line';

        const isZbdmActiveLine = (lineNumber === zbdm.currentLineNumber);
        const isSvdkActiveLine = (lineNumber === svdk.currentLineNumber);

        if (isZbdmActiveLine) {
            lineSpan.classList.add('active');
            lineSpan.classList.add('zbdm');
        }
        if (isSvdkActiveLine) {
            lineSpan.classList.add('active');
            lineSpan.classList.add('svdk');
        }

        // Rendre la ligne selon les curseurs actifs
        if (isZbdmActiveLine && isSvdkActiveLine) {
            renderLineWithTwoCursors(lineSpan, text,
                zbdm.cursorCh, 'zbdm',
                svdk.cursorCh, 'svdk');
        } else if (isZbdmActiveLine) {
            renderLineWithCursor(lineSpan, text, zbdm.cursorCh, 'zbdm');
        } else if (isSvdkActiveLine) {
            renderLineWithCursor(lineSpan, text, svdk.cursorCh, 'svdk');
        } else {
            lineSpan.textContent = text || '';
        }

        codeContainer.appendChild(lineSpan);
    });

    // Scroll vers la ligne active
    if (lastUpdatedPlayer && players[lastUpdatedPlayer].currentLineNumber > 0) {
        const activeLines = document.querySelectorAll('.code-line.active');
        if (activeLines.length > 0) {
            activeLines[activeLines.length - 1].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Check if rendered content fits in container (with a small delay to ensure layout is done)
    // requestAnimationFrame(() => {
    //     setTimeout(() => {

    //         if (checkContentOverflow() && recalcAttempts < MAX_RECALC_ATTEMPTS) {
    //             lastCalculatedFontSize = null;  // Force recalculation with smaller size
    //         } else {
    //             console.log('[RENDER] Content fits OK or max attempts reached');
    //         }
    //     }, 0);
    // });
}

function renderLineWithCursor(lineSpan, text, cursorCh, playerType) {
    const safePos = Math.min(Math.max(0, cursorCh), text.length);

    const beforeCursor = text.substring(0, safePos);
    lineSpan.appendChild(document.createTextNode(beforeCursor));

    const cursorSpan = document.createElement('span');
    cursorSpan.className = `cursor cursor-${playerType}`;
    lineSpan.appendChild(cursorSpan);

    const afterCursor = text.substring(safePos);
    lineSpan.appendChild(document.createTextNode(afterCursor));
}

function renderLineWithTwoCursors(lineSpan, text, cursorCh1, playerType1, cursorCh2, playerType2) {
    const safePos1 = Math.min(Math.max(0, cursorCh1), text.length);
    const safePos2 = Math.min(Math.max(0, cursorCh2), text.length);

    const positions = [
        { pos: safePos1, playerType: playerType1 },
        { pos: safePos2, playerType: playerType2 }
    ].sort((a, b) => a.pos - b.pos);

    let lastPos = 0;

    positions.forEach((item) => {
        if (item.pos > lastPos) {
            lineSpan.appendChild(document.createTextNode(text.substring(lastPos, item.pos)));
        }

        const cursorSpan = document.createElement('span');
        cursorSpan.className = `cursor cursor-${item.playerType}`;
        lineSpan.appendChild(cursorSpan);

        lastPos = item.pos;
    });

    if (lastPos < text.length) {
        lineSpan.appendChild(document.createTextNode(text.substring(lastPos)));
    }
}

function updateStatus(connected) {
    if (connected) {
        statusElement.className = 'status connected';
    } else {
        statusElement.textContent = 'Déconnecté';
        statusElement.className = 'status disconnected';
    }
}

document.addEventListener('DOMContentLoaded', () => {
  window.addEventListener('resize', () => {
    handleWindowResize();
    recalcAttempts = 0;
  });
  loadConfig();
});

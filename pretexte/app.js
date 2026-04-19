import { prepare, layout} from '@chenglou/pretext';

// Configuration for dynamic font sizing
const FONT_CONFIG = {
    MIN_FONT_SIZE: 6,
    MAX_FONT_SIZE: 500,
    FONT_FAMILY: 'InterBlack, Courier New, monospace',
    LINE_HEIGHT_MULTIPLIER: 1.1
};

// Font size calculation
let lastCalculatedFontSize = null;
let containerDimensions = null;
let lastLineCount = null;
let lastTextContent = null;

/**
 * Calculate optimal font size to fit text in container using binary search
* @return {number} Optimal font size in pixels
 */
function calculateOptimalFontSize(text, containerWidth, containerHeight) {

    try {
        let minSize = FONT_CONFIG.MIN_FONT_SIZE;
        let maxSize = FONT_CONFIG.MAX_FONT_SIZE;
        let optimalSize = minSize;
        const lineHeightMultiplier = FONT_CONFIG.LINE_HEIGHT_MULTIPLIER;
        const padding = 20; // total padding (top + bottom + buffer for safety)
        const availableHeight = containerHeight - padding*3;
        const availableWidth = containerWidth - padding;

        // Binary search for the largest font size that fits
        for (let i = 0; i < 20; i++) {
            const testSize = (minSize + maxSize) / 2;
            const cssFont = `${testSize}px ${FONT_CONFIG.FONT_FAMILY}`;

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
            if (maxSize - minSize < 0.5) break;
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
 * Font size calculation - recalculates only if line count changes
 */
function calculateFontSize(allText) {
    // Lazy initialization of container dimensions on first use
    if (!containerDimensions) {
        initializeContainerDimensions();
    }

    const lineCount = allText.split('\n').length; //.filter(line => line.trim().length > 0).length;
    // Skip if nothing changed and we have a valid size
    if (lastLineCount === lineCount && lastCalculatedFontSize && lastTextContent === allText) {
        return;
    }

    lastLineCount = lineCount;
    lastTextContent = allText;

    const optimalSize = calculateOptimalFontSize(
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
        let renderPending = false;

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
                          if (!renderPending) {
                            renderPending = true;
                            requestAnimationFrame(() => {
                                renderCode();
                                renderPending = false;
                            });
                          }
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
 // Version optimisée de mergePlayerWindows
 function mergePlayerWindows() {
     const zbdm = players.zbdmInstantCode;
     const svdk = players.svdkInstantCode;
     const lineMap = new Map();

     const processLines = (windowLines, startLine, playerName) => {
         if (!windowLines) return;
         let currentIndex = 0;
         let lineNum = startLine;

         // Remplace le split('\n') par une recherche d'index pour éviter
         // de créer de gros tableaux de strings jetables.
         while (currentIndex < windowLines.length) {
             let nextIndex = windowLines.indexOf('\n', currentIndex);
             if (nextIndex === -1) nextIndex = windowLines.length;

             const text = windowLines.substring(currentIndex, nextIndex);

             let lineObj = lineMap.get(lineNum);
             if (!lineObj) {
                 lineObj = { text: text, from: new Set() }; // Set évite les doublons plus vite que .includes()
                 lineMap.set(lineNum, lineObj);
             } else if (lastUpdatedPlayer === `${playerName}InstantCode`) {
                 lineObj.text = text;
             }
             lineObj.from.add(playerName);

             currentIndex = nextIndex + 1;
             lineNum++;
         }
     };

     processLines(zbdm.windowLines, zbdm.windowStartLine, 'zbdm');
     processLines(svdk.windowLines, svdk.windowStartLine, 'svdk');

     return Array.from(lineMap.entries())
         .sort((a, b) => a[0] - b[0])
         .map(([lineNumber, data]) => ({
             lineNumber,
             text: data.text,
             from: Array.from(data.from)
         }));
 }

function renderCode() {
  const displayLines = mergePlayerWindows();
        // .filter(line => line.text.trim().length > 0);

    if (displayLines.length === 0) {
        codeContainer.textContent = '...';
        return;
    }

    // Font size calculation based on content
    const allText = displayLines.map(line => line.text).join('\n');
    calculateFontSize(allText);

    const zbdm = players.zbdmInstantCode;
    const svdk = players.svdkInstantCode;

    const fragement = document.createDocumentFragment();
    displayLines.forEach(({ lineNumber, text, from }) => {
        const lineSpan = document.createElement('span');
        lineSpan.className = 'code-line';

        const isZbdmActiveLine = (lineNumber === zbdm.currentLineNumber);
        const isSvdkActiveLine = (lineNumber === svdk.currentLineNumber);

        if (isZbdmActiveLine) {
            lineSpan.classList.add('active');
            lineSpan.classList.add('zbdm');
            lineSpan.style.fontSize = (lastCalculatedFontSize < 48) ? `48px` : `${lastCalculatedFontSize}px`;
        }
        if (isSvdkActiveLine) {
            lineSpan.classList.add('active');
            lineSpan.classList.add('svdk');
            lineSpan.style.fontSize = (lastCalculatedFontSize < 48) ? `48px` : `${lastCalculatedFontSize}px`;
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

        fragement.appendChild(lineSpan);
    });

    codeContainer.innerHTML = '';
    codeContainer.appendChild(fragement);
    // Scroll vers la ligne active
    if (lastUpdatedPlayer && players[lastUpdatedPlayer].currentLineNumber > 0) {
        const activeLines = document.querySelectorAll('.code-line.active');
        if (activeLines.length > 0) {
            activeLines[activeLines.length - 1].scrollIntoView({ behavior: 'auto', block: 'center' });
        }
    }
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
  });
  loadConfig();
});

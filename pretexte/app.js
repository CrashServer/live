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

    const displayLines = mergePlayerWindows();

    if (displayLines.length === 0) {
        codeContainer.textContent = 'En attente de code...';
        return;
    }

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
    if (!connected) {
        statusElement.className = 'status connected';
    } else {
        statusElement.textContent = 'Déconnecté';
        statusElement.className = 'status disconnected';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadConfig();
    renderCode();
});

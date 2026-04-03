const codeContainer = document.getElementById('code-container');
const statusElement = document.getElementById('status');

let currentLineNumber = 0;
let fullCode = '';
let ws = null;
let config = null;
let cursorLine = 0;           // Position de la ligne du curseur (0-indexed)
let cursorCh = 0;             // Position du caractère dans la ligne

// Configuration par défaut
const defaultConfig = {
    HOST_IP: '192.168.1.42',
    FOXDOT_WS_PORT: 20000
};

// Charger la configuration
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
                    if (message.allCode !== undefined) {
                        fullCode = message.allCode;
                        currentLineNumber = message.currentLineNumber || 0;
                        cursorLine = message.cursorLine || 0;
                        cursorCh = message.cursorCh || 0;
                        console.log(`📍 Curseur: ligne=${cursorLine}, char=${cursorCh}`);
                        renderCode();
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

function renderCode() {
    codeContainer.innerHTML = '';

    if (!fullCode) {
        codeContainer.textContent = 'En attente de code...';
        return;
    }

    const lines = fullCode.split('\n');

    lines.forEach((line, index) => {
        const lineSpan = document.createElement('span');
        lineSpan.className = 'code-line';

        // Mettre en évidence la ligne courante
        if (index + 1 === currentLineNumber) {
            lineSpan.classList.add('active');
        }

        // Si c'est la ligne du curseur, insérer le curseur à la bonne position
        if (index === cursorLine) {
            const beforeCursor = line.substring(0, Math.min(cursorCh, line.length));
            const afterCursor = line.substring(Math.min(cursorCh, line.length));

            // Texte avant le curseur
            lineSpan.appendChild(document.createTextNode(beforeCursor));

            // Bloc clignotant pour le curseur (█)
            const cursorSpan = document.createElement('span');
            cursorSpan.className = 'cursor';
            cursorSpan.textContent = '█';
            lineSpan.appendChild(cursorSpan);

            // Texte après le curseur
            lineSpan.appendChild(document.createTextNode(afterCursor));
        } else {
            lineSpan.textContent = line || '';
        }

        codeContainer.appendChild(lineSpan);
    });

    // Scroll vers la ligne active
    if (currentLineNumber > 0) {
        const activeLines = document.querySelectorAll('.code-line.active');
        if (activeLines.length > 0) {
            activeLines[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }
}

function updateStatus(connected) {
    if (connected) {
        statusElement.textContent = 'Connecté';
        statusElement.className = 'status connected';
    } else {
        statusElement.textContent = 'Déconnecté';
        statusElement.className = 'status disconnected';
    }
}

// Démarrer
document.addEventListener('DOMContentLoaded', () => {
    loadConfig();
    renderCode();
});

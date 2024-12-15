
// @ts-ignore
import CodeMirror from 'codemirror'
import * as Y from 'yjs'
import { WebrtcProvider } from 'y-webrtc'
import { CodemirrorBinding } from 'y-codemirror'
import { Awareness } from 'y-protocols/awareness'
import { EventEmitter } from './eventBus.js';
import { setupConfigPanel } from './configPanel.js'
// import { IndexeddbPersistence } from 'y-indexeddb' 
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/python/python.js' // Importer le mode Python
import '../css/style.css'
import '../css/crashpanel.css'
import 'codemirror/addon/edit/matchbrackets'
import 'codemirror/addon/edit/closebrackets'
import 'codemirror/addon/comment/comment'

document.addEventListener('DOMContentLoaded', () => {
  const ws = new WebSocket('ws://localhost:1234');

  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  // const indexeddbProvider = new IndexeddbPersistence('webtroop', ydoc);
  const provider = new WebrtcProvider('webtroop', ydoc, {
    awareness: awareness,
    signaling: ['ws://localhost:4444']
  });

  const ytext = ydoc.getText('webtroop');
  
  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    theme: 'monokai',
    lineNumbers: true,
    indentUnit: 4,
    autofocus: true,
    matchBrackets: true,
    autoCloseBrackets: true,
  });

  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness);
  
  setupConfigPanel(awareness, editor);

  EventEmitter.on('send_foxdot', (command) => {
    ws.send(JSON.stringify({
        type: 'evaluate_code',
        code: command
    }));
  });

  //Gestion des logs FoxDot pour la console
  ws.onmessage = (event) => {    
    try {
      const message = JSON.parse(event.data);
      if (message.type === 'foxdot_log') {
        appendLog(message.data);
      }
    } catch (error) {
    }
  };

  function appendLog(message) {
    const logs = document.getElementById('logs');
    const entry = document.createElement('pre');
    entry.className = 'log-entry';
    if (message.includes('Traceback')) {
      entry.classList.add('error-log');
    }
    entry.textContent = message;
    logs.appendChild(entry);
    logs.scrollTop = logs.scrollHeight;
  }

  function stopClock(cm) {
    ws.send(JSON.stringify({
        type: 'evaluate_code',
        code: 'Clock.clear()\n'
    }));
  }

  // Gestion de CTRL+ENTER
  editor.setOption('extraKeys', {
    // 'Ctrl-ù': console.log("Ctrl-/"),
    'Ctrl-;': stopClock,
    'Ctrl-Enter': (cm) => {
      // Obtenir la position exacte du curseur
      const cursor = cm.getCursor();
      const selection = cm.getSelection();
      let codeToEvaluate;
      let lineStart, lineEnd;

      if (selection && selection.length > 0) {
        const selections = cm.listSelections();
        const range = selections[0];
        lineStart = Math.min(range.anchor.line, range.head.line);
        lineEnd = Math.max(range.anchor.line, range.head.line);
        codeToEvaluate = selection;
      } else {
        lineStart = cursor.line;
        lineEnd = cursor.line;
        codeToEvaluate = cm.getLine(lineStart);
      }

      if (codeToEvaluate.trim()) {
        // Envoyer le code
        ws.send(JSON.stringify({
          type: 'evaluate_code',
          code: codeToEvaluate
        }));

        // Envoyer l'information de flash via awareness
        awareness.setLocalStateField('flash', {
          lineStart,
          lineEnd,
          timestamp: Date.now()
        });

      }
    },
    'Ctrl-Alt-Enter': (cm) => {
        const cursor = cm.getCursor();
        let startLine = cursor.line;
        let endLine = cursor.line;

        // Recherche début du bloc (vers le haut)
        while (startLine > 0 && cm.getLine(startLine - 1).trim() !== '') {
            startLine--;
        }

        // Recherche fin du bloc (vers le bas)
        while (endLine < cm.lineCount() - 1 && cm.getLine(endLine + 1).trim() !== '') {
            endLine++;
        }

        // Extraire le bloc
        const blockCode = cm.getRange(
            {line: startLine, ch: 0},
            {line: endLine, ch: cm.getLine(endLine).length}
        );

        if (blockCode.trim()) {
            // Envoyer le code
            ws.send(JSON.stringify({
                type: 'evaluate_code',
                code: blockCode
            }));

            // Flash effect
            awareness.setLocalStateField('flash', {
                lineStart: startLine,
                lineEnd: endLine,
                timestamp: Date.now()
            });
        }
    },
  });

  // Ajouter l'écouteur d'awareness
  awareness.on('change', () => {
    const states = awareness.getStates();
    states.forEach((state) => {
        if (state.flash) {
            const { lineStart, lineEnd, timestamp } = state.flash;
            // Vérifier si le flash est récent (moins de 100ms)
            if (Date.now() - timestamp < 100) {
                // Créer l'effet flash
                for (let i = lineStart; i <= lineEnd; i++) {
                    const mark = editor.markText(
                        {line: i, ch: 0},
                        {line: i, ch: editor.getLine(i).length},
                        {className: 'flash-highlight'}
                    );
                    setTimeout(() => mark.clear(), 200);
                }
            }
        }
    });
  });

  class PersistentWebSocket {
    constructor(url) {
        this.url = url;
        this.reconnectAttempts = 0;
        this.maxReconnectDelay = 5000;
        this.ws = null;
        this.connect();
    }

    connect() {
        this.ws = new WebSocket(this.url);
        
        this.ws.onopen = () => {
            console.log('WebSocket connecté');
            this.reconnectAttempts = 0;
            this.startHeartbeat();
        };

        this.ws.onclose = () => {
            console.log('WebSocket fermé, tentative de reconnexion...');
            this.reconnect();
        };

        this.ws.onerror = (error) => {
            console.error('Erreur WebSocket:', error);
        };
    }

    reconnect() {
        const delay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), this.maxReconnectDelay);
        this.reconnectAttempts++;
        
        setTimeout(() => {
            console.log(`Tentative de reconnexion ${this.reconnectAttempts}...`);
            this.connect();
        }, delay);
    }

    startHeartbeat() {
        this.heartbeatInterval = setInterval(() => {
            if (this.ws.readyState === WebSocket.OPEN) {
                this.ws.send(JSON.stringify({ type: 'ping' }));
            }
        }, 30000); // Ping toutes les 30 secondes
    }

    send(data) {
        if (this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(data);
        }
    }
  }

  const crashOsWs = new PersistentWebSocket('ws://192.168.1.7:20000');
  editor.on('cursorActivity', (cm) => {
    // Récupérer les infos utilisateur depuis awareness
    const userState = awareness.getLocalState();
    const userName = userState?.user?.name || 'Anonymous';

    // Récupérer la position du curseur et le contenu
    const cursor = cm.getCursor();
    const currentLine = cm.getLine(cursor.line);
    
    // Préparer le message
    const message = {
        type: `${userName}InstantCode`,
        position: cursor.ch,
        code: currentLine
    };

    crashOsWs.send(JSON.stringify(message));
  });
});

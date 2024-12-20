// @ts-ignore
import { CONFIG} from '../../config.js';
import CodeMirror from 'codemirror'
import { CodemirrorBinding } from 'y-codemirror'
import { EventEmitter } from './eventBus.js';
import { setupConfigPanel } from './configPanel.js'
import * as Y from 'yjs'
import { WebrtcProvider } from 'y-webrtc'
// import { IndexeddbPersistence } from 'y-indexeddb'
import { Awareness } from 'y-protocols/awareness'
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/python/python.js' // Importer le mode Python
import 'codemirror/keymap/sublime'
import 'codemirror/addon/edit/matchbrackets'
import 'codemirror/addon/edit/closebrackets'
import 'codemirror/addon/comment/comment'
import 'codemirror/addon/hint/show-hint'
import 'codemirror/addon/hint/show-hint.css'
import 'codemirror/addon/hint/anyword-hint'
import '../css/style.css'
import '../css/crashpanel.css'
import '../css/configPanel.css'

document.addEventListener('DOMContentLoaded', () => {
  const wsServer = new WebSocket(CONFIG.FOXDOT_SERVER);
  const foxdoxWs = new WebSocket(CONFIG.CRASHOS_SERVER)
  let serverActive = false;

  const otherUserDisplay = document.getElementById('other-user-display');

  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  
  // const indexeddbProvider = new IndexeddbPersistence('webtroop', ydoc)
  
  const provider = new WebrtcProvider('webtroop', ydoc, {
    awareness: awareness,
    signaling: [CONFIG.SIGNALING_SERVER]
  });
  
  const ytext = ydoc.getText('webtroop');
  
  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    theme: 'eclipse',
    lineNumbers: true,
    indentUnit: 4,
    autofocus: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    lineWrapping: true,
    cursorScrollMargin: 50,
    singleCursorHeightPerLine: false,
    keyMap: 'sublime',
  });

  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness);
  
  setupConfigPanel(awareness, editor);

  EventEmitter.on('send_foxdot', (command) => {
    wsServer.send(JSON.stringify({
        type: 'evaluate_code',
        code: command
    }));
  });

  //Gestion des logs FoxDot pour la console
  wsServer.onmessage = (event) => {    
    try {
      const message = JSON.parse(event.data);
      if (message.type === 'foxdot_log') {
        appendLog(message.data, message.color);
      }
    } catch (error) {
    }
  };

  foxdoxWs.onmessage = (event) => {
    try {
      const message = JSON.parse(event.data);
      if (message.type === 'attack') {
        insertAttackContent(message.content);
      }
    } catch (error) {
    }
  };

  function appendLog(message, color) {
    const logs = document.getElementById('logs');
    const entry = document.createElement('pre');
    entry.className = 'log-entry';
    if (color){
      entry.style.color = color;
    }
    if (message.includes('Traceback')) {
      entry.classList.add('error-log');
    }
    else if (!message.includes('>>')) {
      entry.classList.add('help');
    }
    entry.textContent = message;
    logs.insertBefore(entry, logs.firstChild);
    logs.scrollTop = 0;
  }

  function stopClock(cm) {
    wsServer.send(JSON.stringify({
        type: 'evaluate_code',
        code: 'Clock.clear()\n'
    }));
  }

  function insertAttackContent(content) {
    const cursor = editor.getCursor();
    const line = cursor.line + 1; // Insérer en dessous de la ligne actuelle
    editor.replaceRange(content, { line: line, ch: 0 });
  }

  // Gestion de CTRL+ENTER
  editor.setOption('extraKeys', {
    // 'Ctrl-ù': console.log("Ctrl-/"),
    'Ctrl-;': stopClock,
    'Ctrl-Space': 'autocomplete',
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
        // Vérifier s'il faut stopper un player
        const playerPattern = /_([a-zA-Z]\d+|[a-zA-Z]{2})/;;
        const match = codeToEvaluate.trim().match(playerPattern);

        if (match) {
          const player = match[1];
          codeToEvaluate = `${player}.stop()`;
        }  
        // Envoyer le code
        wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: codeToEvaluate,
          userName: awareness.getLocalState().user.name,
          userColor: awareness.getLocalState().user.color 
        }));
        
        crashOsWs.send(JSON.stringify({
          type: (awareness.getLocalState().user.name).toLowerCase() + "Code",
          code: codeToEvaluate,
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
            wsServer.send(JSON.stringify({
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

  // Gestion de l'autocomplétion
  editor.setOption('hintOptions', {
    hint: function(editor) {
        
        const cursor = editor.getCursor();
        const line = editor.getLine(cursor.line);
        const cursorPosition = cursor.ch;
        
        // Regex pour détecter un player suivi de '>>'
        const playerPattern = /([a-zA-Z]\d+)\s*>>\s*$/;
        const beforeCursor = line.slice(0, cursorPosition);
        const match = beforeCursor.match(playerPattern);

        if (match) {
            const suggestions = [
                { text: 'play()', displayText: 'play' },
                { text: 'loop()', displayText: 'loop' },
                { text: 'blip()', displayText: 'blip' }
            ];

            return {
                list: suggestions,
                from: CodeMirror.Pos(cursor.line, match[0].length),
                to: cursor
            };
        } else {
              const suggestions = [
                { text: 'linvar([],[])', displayText: 'linvar' },
                { text: 'var([],[])', displayText: 'var' },
            ];

            return {
                list: suggestions,
                from: CodeMirror.Pos(cursor.line, cursorPosition),
                to: cursor
            };
        }
    }
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
        if (state.otherInstantCode) {
          const { user, code, position, line } = state.otherInstantCode;
          if (user !== awareness.getLocalState().user.name){
            const updatedCode = code.slice(0, position) + '<span class="otherLive-cursor-marker">|</span>' + code.slice(position);
            otherUserDisplay.innerHTML = `${line}: ${updatedCode}`;
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
            // console.log('WebSocket connecté');
            this.reconnectAttempts = 0;
            this.startHeartbeat();
        };

        this.ws.onclose = () => {
            // console.log('WebSocket fermé, tentative de reconnexion...');
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
            // console.log(`Tentative de reconnexion ${this.reconnectAttempts}...`);
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
  const crashOsWs = new PersistentWebSocket(CONFIG.CRASHOS_SERVER);

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

    // envoyer le message dans le live other player display
    try {
        awareness.setLocalStateField('otherInstantCode', {
          user: userName,
          code: currentLine,
          position: cursor.ch,
          line: cursor.line + 1,
        });
      } 
    catch (error) {
      // console.error('Error setting local state field:', error);
    }
    
    crashOsWs.send(JSON.stringify(message));
  });

  crashPanelTitle.addEventListener('click', () => {
    serverActive = !serverActive;
    const message = { "type": "serverState", serverState: serverActive ? 1 : 0 };
    crashOsWs.send(JSON.stringify(message));
  });


  // Redimensionner le panneau de logs
  const separator = document.getElementById('separator')
  const logs = document.getElementById('logs')
  const editorContainer = document.getElementById('editor-container')
  
  let isResizing = false

  separator.addEventListener('mousedown', (e) => {
    isResizing = true
    document.addEventListener('mousemove', resize)
    document.addEventListener('mouseup', stopResize)
  })

  function resize(e) {
    if (isResizing) {
      const containerHeight = editorContainer.clientHeight
      const newLogsHeight = containerHeight - e.clientY
      logs.style.height = `${newLogsHeight}px`
      editor.getWrapperElement().style.height = `${containerHeight - newLogsHeight - separator.clientHeight}px`
      editor.refresh()
    }
  }

  function stopResize() {
    isResizing = false
    document.removeEventListener('mousemove', resize)
    document.removeEventListener('mouseup', stopResize)
  }
});

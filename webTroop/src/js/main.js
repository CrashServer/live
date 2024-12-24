// @ts-ignore
// import { CONFIG} from '../../config.js';
import CodeMirror from 'codemirror'
import { CodemirrorBinding } from 'y-codemirror'
import { EventEmitter } from './eventBus.js';
import { setupConfigPanel } from './configPanel.js'
import * as Y from 'yjs'
import { WebsocketProvider } from 'y-websocket';
import { Awareness } from 'y-protocols/awareness'

import 'codemirror/addon/dialog/dialog.js'
import './foxdot_mode.js'
import 'codemirror/keymap/sublime'
import 'codemirror/addon/edit/matchbrackets'
import 'codemirror/addon/edit/closebrackets'
import 'codemirror/addon/comment/comment'
import 'codemirror/addon/hint/show-hint'
import 'codemirror/addon/selection/active-line.js'

import { chatUtils } from './chatUtils.js';
import { logsUtils } from './logs.js';
import { functionUtils } from './functionUtils.js';

import 'codemirror/lib/codemirror.css'
import 'codemirror/addon/hint/show-hint.css'
import 'codemirror/addon/dialog/dialog.css'
import '../css/style.css'
import '../css/crashpanel.css'
import '../css/configPanel.css'

document.addEventListener('DOMContentLoaded', async () => {
  // Récupération de la configuration
  const configRequest = await fetch('../../crash_config.json' );
  if (!configRequest.ok) {
    throw new Error(`HTTP error! status: ${configRequest.status}`);
  }
  const config = await configRequest.json();
  
  // Connexion aux serveurs
  const wsServer = new WebSocket(`ws://${config.HOST_IP}:1234`);
  const foxdoxWs = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);
  let serverActive = false;

  // Récupération des éléments du DOM
  const chrono = document.getElementById('chrono');
  
  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  const provider = new WebsocketProvider(`ws://localhost:4444`, 'webtroop', ydoc, {
    awareness: awareness,
  });
  const ytext = ydoc.getText('webtroop');
  
  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    theme: 'eclipse',
    lineNumbers: true,
    autofocus: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    lineWrapping: true,
    cursorScrollMargin: 50,
    singleCursorHeightPerLine: false,
    styleActiveLine: true,
    keyMap: 'sublime',
  });

  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness);
  
  // Configuration du panneau de configuration
  setupConfigPanel(awareness, editor);
  
  // Configuration des logs
  logsUtils.initResize(editor);

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
        logsUtils.appendLog(message.data, message.color);
      }
    } catch (error) {
    }
  };

  // Gestion du copy/paste venant de FOXDOT
  foxdoxWs.onmessage = (event) => {
    try {
      const message = JSON.parse(event.data);
      if (message.type === 'attack') {
        functionUtils.insertAttackContent(editor, message.content);
      }
    } catch (error) {
    }
  };

  // Reset du chrono lors du clic sur le chrono
  chrono.addEventListener('click', ()=> functionUtils.resetChrono(wsServer));

  // Gestion des markers
  function setMarker(cm, colorMarker, txtMarker) {
    const isMarker = functionUtils.setMarker(cm, colorMarker, txtMarker)
    if (isMarker){
      chatUtils.insertChatMessage(cm, txtMarker, awareness.getLocalState().user.name, colorMarker);
    }
  }

  function evaluateCode(cm, multi){
    const [blockCode, startLine, endLine] = functionUtils.getCodeAndCheckStop(cm, multi);

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
  

  // Gestion de CTRL+ENTER
  editor.setOption('extraKeys', {
    'Ctrl-;': ()=> functionUtils.stopClock(wsServer),
    'Ctrl-Space': 'autocomplete',
    'Ctrl-Alt-C': 'toggleComment',
    'Alt-J': (cm) => {functionUtils.jumpToOtherPlayer(cm, awareness)},
    'Alt-1': (cm) => setMarker(cm, "Red", "Attention à un truc"),
    'Alt-2': (cm) => setMarker(cm, "Green", "[[ taggué ]]"),
    'Alt-3': (cm) => setMarker(cm, "Blue", "[[ ça c'est cool ]]"),
    'Alt-C': (cm) => {
      chatUtils.getChat(cm, "", (text) => chatUtils.insertChatMessage(cm, text, awareness.getLocalState().user.name));
    }, 
    'Ctrl-Enter': (cm) => {evaluateCode(cm, false)},
    'Ctrl-Alt-Enter': (cm) => {evaluateCode(cm, true)},
  });

  // Gestion de l'autocomplétion
  // editor.setOption('hintOptions', {
  //   hint: function(editor) {
        
  //       const cursor = editor.getCursor();
  //       const line = editor.getLine(cursor.line);
  //       const cursorPosition = cursor.ch;
        
  //       // Regex pour détecter un player suivi de '>>'
  //       const playerPattern = /([a-zA-Z]\d+)\s*>>\s*$/;
  //       const beforeCursor = line.slice(0, cursorPosition);
  //       const match = beforeCursor.match(playerPattern);

  //       if (match) {
  //           const suggestions = [
  //               { text: 'play()', displayText: 'play' },
  //               { text: 'loop()', displayText: 'loop' },
  //               { text: 'blip()', displayText: 'blip' }
  //           ];

  //           return {
  //               list: suggestions,
  //               from: CodeMirror.Pos(cursor.line, match[0].length),
  //               to: cursor
  //           };
  //       } else {
  //             const suggestions = [
  //               { text: 'linvar([],[])', displayText: 'linvar' },
  //               { text: 'var([],[])', displayText: 'var' },
  //           ];

  //           return {
  //               list: suggestions,
  //               from: CodeMirror.Pos(cursor.line, cursorPosition),
  //               to: cursor
  //           };
  //       }
  //   }
  // });

  // Ajouter l'écouteur d'awareness
  awareness.on('change', () => {
    const states = awareness.getStates();
    states.forEach((state) => {
      // Gestion de l'effet flash
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
      // Gestion de l'affichage du code en temps réel des autres utilisateurs
      if (state.otherInstantCode) { 
        const { user, code, position, line } = state.otherInstantCode;
        if (user !== awareness.getLocalState().user.name){
          const updatedCode = code.slice(0, position) + '<span class="otherLive-cursor-marker">|</span>' + code.slice(position);
          logsUtils.insertOtherUserCode(line, updatedCode);
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
  const crashOsWs = new PersistentWebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);

  // Gestion de l'envoi de code en temps réel
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
    }
    
    crashOsWs.send(JSON.stringify(message));
  });

  // Gestion de l'activation/désactivation du serveur dans CrashPanel
  crashPanelTitle.addEventListener('click', () => {
    serverActive = !serverActive;
    const message = { "type": "serverState", serverState: serverActive ? 1 : 0 };
    crashOsWs.send(JSON.stringify(message));
  });
});

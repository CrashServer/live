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
import 'codemirror/addon/scroll/annotatescrollbar.js'
import 'codemirror/addon/search/searchcursor.js'
import 'codemirror/addon/search/search.js'
import 'codemirror/addon/search/jump-to-line.js'
import 'codemirror/addon/search/matchesonscrollbar.js'
import 'codemirror/addon/fold/foldcode.js'
import 'codemirror/addon/fold/foldgutter.js'

import { chatUtils } from './chatUtils.js';
import { logsUtils } from './logs.js';
import { functionUtils } from './functionUtils.js';
import { markerUtils } from './markerUtils.js';
import { foxdotAutocomplete } from './foxdotAutocomplete.js';
import { showDefinition } from './foxdotDefinitions.js';

import 'codemirror/lib/codemirror.css'
import 'codemirror/addon/hint/show-hint.css'
import 'codemirror/addon/dialog/dialog.css'
import 'codemirror/addon/fold/foldgutter.css'
import '../css/style.css'
import '../css/crashpanel.css'
import '../css/configPanel.css'

document.addEventListener('DOMContentLoaded', async () => {
  // Récupération de la configuration
  const configRequest = await fetch('../../crash_config.json');
  if (!configRequest.ok) {
    throw new Error(`HTTP error! status: ${configRequest.status}`);
  }
  const config = await configRequest.json();
  
  // Connexion aux serveurs
  const wsServer = new WebSocket(`ws://${config.HOST_IP}:1234`);
  let foxdotWs = null;
  // let foxdotWs = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);

  // Récupération des éléments du DOM
  const chrono = document.getElementById('chrono');
  
  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  const provider = new WebsocketProvider(`ws://${config.HOST_IP}:4444`, 'webtroop', ydoc, {
    awareness: awareness,
  });
  const ytext = ydoc.getText('webtroop');
  const ychat = ydoc.getArray('chat');
  const ymarkers = ydoc.getArray('markers');

  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    theme: 'material-darker',
    lineNumbers: true,
    autofocus: true,
    matchBrackets: true,
    autoCloseBrackets: {pairs: "()[]{}<>''\"\"", override: true},
    lineWrapping: true,
    fixedGutter: false,
    singleCursorHeightPerLine: false,
    styleActiveLine: true,
    foldGutter: true,
    gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
    keyMap: 'sublime',
  });

  const otherUserDoc = editor.getDoc().linkedDoc({shareHist: false});
  const otherEditor = CodeMirror(document.getElementById('other-editor'), {
    mode: 'python',
    theme: 'material-darker',
    lineNumbers: true,
    readOnly: true,
    lineWrapping: true,
    styleActiveLine: true,
  });

  otherEditor.swapDoc(otherUserDoc);

  let otherUserCursorMark = null;
  let otherUserNameWidget = null;

  // Fonction pour mettre à jour l'affichage de l'autre utilisateur
  function updateOtherUserDisplay(userName, userColor, line, position, code) {
    if (!configPanelControls.isSplitScreenEnabled) {
      return;
    }
    
    // Supprimer l'ancien marqueur de curseur
    if (otherUserCursorMark) {
      otherUserCursorMark.clear();
    }
    if (otherUserNameWidget) {
      otherUserNameWidget.remove();
      otherUserNameWidget = null;
    }

    // Ajouter le nouveau marqueur de curseur si valide
    if (line >= 0 && line < otherEditor.lineCount() && position >= 0) {
      const lineLength = otherEditor.getLine(line).length;
      const endPos = Math.min(position + 1, lineLength);
      
      if (position <= lineLength) {
        otherUserCursorMark = otherEditor.markText(
          {line: line, ch: position},
          {line: line, ch: endPos},
          {
            className: 'other-user-cursor',
            css: `border-left: 2px solid ${userColor}`,
            inclusiveLeft: true,
            inclusiveRight: false
          }
        );

      const nameElement = document.createElement('span');
      nameElement.className = 'other-user-name-widget';
      nameElement.textContent = userName;
      nameElement.style.cssText = `
        background-color: ${userColor};
        color: white;
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 11px;
        font-weight: bold;
        white-space: nowrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.3);
        z-index: 1000;
        position: relative;
        top: -20px;
        left: -10px;
      `;

      // Ajouter le widget au-dessus du curseur
      otherUserNameWidget = otherEditor.addWidget(
        {line: line, ch: position}, 
        nameElement, 
        false // false = au-dessus de la ligne
      );

      otherUserNameWidget = nameElement;

      }
    }

    // Centrer la vue sur le curseur de l'autre utilisateur
    if (line >= 0 && line < otherEditor.lineCount()) {
      otherEditor.scrollIntoView({line: line, ch: position}, 100);
    }
  }

  const resizeObserver = new ResizeObserver(entries => {
    for (let entry of entries) {
      if (entry.target.id === 'editor-container') { 
        logsUtils.refreshEditors();
      }
    }
  });

  resizeObserver.observe(document.getElementById('editor-container'));

  setTimeout(() => {
    logsUtils.refreshEditors();
  }, 100);


  // undo Manager
  const yUndoManager = new Y.UndoManager(ytext, { trackedOrigins: new Set([]) });
  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness, {yUndoManager});

  // Configuration du panneau de configuration
  const configPanelControls = setupConfigPanel(awareness, editor, otherEditor);
  
  // Configuration des logs
  logsUtils.initResize(editor, otherEditor);

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
        if (message.attackRequestName != ""){
          awareness.setLocalStateField('attackRequest', {"attackRequestName": message.attackRequestName});
        }
      }
    } catch (error) {
    }
  };

  // Reset du chrono lors du clic sur le chrono
  chrono.addEventListener('click', ()=> functionUtils.resetChrono(wsServer));

  function evaluateCode(cm, multi){
    const videoCodeResult = functionUtils.isVideoCode(cm);
    if (videoCodeResult){
      var [videoCode, startLine] = videoCodeResult;
      var endLine = startLine;
      foxdotWs.send(JSON.stringify({
        type: 'sceneName',
        sceneName: videoCode
      }))
      }
    else {
      var [blockCode, startLine, endLine] = functionUtils.getCodeAndCheckStop(cm, multi);

      const userState = awareness.getLocalState();
      const userName = userState.user.name;
      const userColor = userState.user.color;
      // Envoyer le code
      wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: blockCode,
          userColor: userColor,
          userName: userName,
      }));

      foxdotWs.send(JSON.stringify({
        type: `${userName}Code`,
        code: blockCode,
      }));
    }   
    
    // Flash effect
    awareness.setLocalStateField('flash', {
        lineStart: startLine,
        lineEnd: endLine,
        timestamp: Date.now()
    });
  }
  
  // Écouter les changements dans le Y.Array des messages de chat
  ychat.observe(event => {
    event.changes.added.forEach(item => {
      const message = item.content.getContent()[0];
      chatUtils.insertChatMessage(editor, message.text, message.userName, message.userColor, message.line);
    });
    // Supprimer les anciens messages pour ne garder que les 20 plus récents
    if (ychat.length > 15) {
      ychat.delete(0, ychat.length - 15);
    }
  });

  // Écouter les changements dans le Y.Array des marqueurs
  ymarkers.observe(event => {
    event.changes.added.forEach(item => {
      const marker = item.content.getContent()[0];
      markerUtils.applyMarker(editor, marker.line, marker.color);
    });

    event.changes.deleted.forEach(item => {
      const marker = item.content.getContent()[0];
      markerUtils.removeMarker(editor, marker.line);
    });
  });

  // Gestion de CTRL+ENTER
  editor.setOption('extraKeys', {
    'Ctrl-;': ()=> functionUtils.stopClock(wsServer),
    'Ctrl-Space': 'autocomplete',
    'Ctrl-S': (cm)=> {functionUtils.saveEditorContent(cm,wsServer)},
    'Alt-X': (cm) => {
      cm.toggleComment();
      evaluateCode(cm, false);
    },
    'Ctrl-Alt-X': (cm) => {
      const {startLine, endLine} = functionUtils.getBlock(cm, cm.getCursor().line);
      cm.setSelection({line: startLine, ch: 0}, {line: endLine, ch: cm.getLine(endLine).length});
      cm.toggleComment();
      evaluateCode(cm, true);
    },
    'Alt-S': (cm) => {functionUtils.soloPlayer(cm, wsServer)},
    'Ctrl-Alt-S': () => {functionUtils.unSoloPlayers(wsServer)},
    'Alt-J': (cm) => {functionUtils.jumpToOtherPlayer(cm, awareness)},
    'Ctrl-Alt-J': (cm) => {functionUtils.previousJump(cm)},
    'Alt-1': (cm) => markerUtils.setMarker(cm, "Red", "[[ Attention à un truc ]]", awareness, ymarkers, ychat),
    'Alt-2': (cm) => markerUtils.setMarker(cm, "Green", "[[ taggué ]]", awareness, ymarkers, ychat),
    'Alt-3': (cm) => markerUtils.setMarker(cm, "Blue", "[[ ça c'est cool ]]", awareness, ymarkers, ychat),
    'Alt-4': () => markerUtils.resetMarkers(ymarkers),
    'Alt-C': (cm) => {
      chatUtils.getChat(cm, "", (text, line) => {
        const userState = awareness.getLocalState();
        const userName = userState?.user?.name || 'Anonymous';
        const userColor = userState?.user?.color || '#000000';
        ychat.push([{ text, userName, userColor, line }]); // Ajouter le message au Y.Array
      });
    }, 
    'Ctrl-Enter': (cm) => {evaluateCode(cm, false)},
    'Ctrl-Alt-Enter': (cm) => {evaluateCode(cm, true)},
    'Alt-I': (cm) => showDefinition(cm),
    'Alt-F': "findPersistent",
    'Ctrl-G': "findNext",
    'Ctrl-Alt-Left': "goLineStart",
    'Ctrl-Alt-Right': "goLineEnd",
    'Alt-Q': (cm) => cm.foldCode(cm.getCursor(), 
      {rangeFinder: (cm,start) => {
        if(!start){return null;}
        let startLine = start.line;
        let endLine = start.line + 1;
        while (startLine > 0 && !cm.getLine(startLine).trim().startsWith("#")){
          startLine--;
        }
     
        while (endLine < cm.lineCount() -1  && !cm.getLine(endLine).trim().startsWith("#")){
          endLine++;
        }

        if (startLine === endLine){
          return null;
        }

        return {
            from: CodeMirror.Pos(startLine+1, 0),
            to: CodeMirror.Pos(endLine, cm.getLine(endLine).length),
        };
      }}),
      'Ctrl-Left': (cm) => {functionUtils.goToPreviousComma(cm)},
      'Ctrl-Right': (cm) => {functionUtils.goToNextComma(cm)},
      'Alt-P': () => {document.getElementById('piano-roll').classList.toggle('hidden')},
      'Alt-Up': (cm) => {
                    functionUtils.incrementValue(cm, 1)
                    evaluateCode(cm, false)
                  },
      'Alt-Down': (cm) => {
                    functionUtils.incrementValue(cm, -1)
                    evaluateCode(cm, false)
                  },
      'Alt-A': (cm) => {functionUtils.randomizer(cm)},
      'Alt-R': (cm) => {functionUtils.resetPlayer(cm, wsServer)},
      // 'Alt-V': (cm) => {functionUtils.sendSceneName(cm, foxdotWs)},
  });

  // Gestion de l'autocomplétion
  editor.setOption('hintOptions', {
    hint: (cm) => foxdotAutocomplete.hint(cm, CodeMirror),
  });

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
      if (state.otherInstantCode && state.user?.name !== awareness.getLocalState().user?.name) {
        const { user, code, position, line } = state.otherInstantCode;
        const userColor = state.user?.color || '#fff';
        
        // Mettre à jour l'affichage (line-1 car votre code utilise line+1)
        updateOtherUserDisplay(user, userColor, line - 1, position, code);
      }
    });
  });

  function foxDotWs(){
    foxdotWs = new WebSocket(`ws://${config.HOST_IP}:${config.FOXDOT_WS_PORT}`);
    foxdotWs.onopen = () => {
      foxdotWs.send(JSON.stringify({ type: 'get_autocomplete' }));
    };
    foxdotWs.onmessage = (event) => {
      try {
        const message = JSON.parse(event.data);
        if (message.type === 'attack') {
          if (awareness.getLocalState().attackRequest.attackRequestName === awareness.getLocalState().user.name){
            functionUtils.insertAttackContent(editor, message.content);
          }
        }
        else if (message.type === 'autocomplete') {
          const { loops, fxList, synthList, attackList } = functionUtils.formatFoxDotAutocomplete(message);

          const toExclude = ["__init__", "1s", ""];
          let filteredLoops = loops.filter(i => !toExclude.includes(i.displayText)); 

          foxdotAutocomplete.loopList = filteredLoops;
          foxdotAutocomplete.fxList = fxList;
          foxdotAutocomplete.synths= synthList;
          foxdotAutocomplete.attackList = attackList;

          if (filteredLoops.length == 0 || fxList.length == 0 || synthList.length == 0 || attackList.length == 0) {
            console.error(`Erreur lors de la récupération de la liste des boucles (${loops.length}), effets (${fxList.length}), synthés (${synthList.length}) ou attaques (${attackList.length})`);
          }
        }
      } catch (error) {
        console.error('Erreur lors de la réception de message FoxDot:', error);
      }
    };
    foxdotWs.onclose = (e) => {
      console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
      setTimeout(function() {
      foxDotWs();
      }, 1000);
    };
    foxdotWs.onerror = (err) => {
      console.error('Socket encountered error: ', err.message, 'Closing socket');
      foxdotWs.close();
    };
  }

  foxDotWs();

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
    
    if(foxdotWs.readyState === WebSocket.OPEN) {
      foxdotWs.send(JSON.stringify(message));
    }
  });

  // Gestion de l'activation/désactivation du serveur dans CrashPanel
  crashPanelTitle.addEventListener('click', () => {
    if (foxdotWs.readyState === WebSocket.OPEN) {
      foxdotWs.send(JSON.stringify({ type: "serverToggle"}));
    }
    
    crashPanelTitle.classList.toggle('loading');
    setTimeout(() => {
      crashPanelTitle.classList.toggle('loading');
    }, 4000);
  });

  // piano insert at cursor
  document.querySelectorAll('#piano-roll .piano-key li').forEach(key => {
    key.addEventListener('click', (event) => {
        const index = event.currentTarget.dataset.index;
        if (index !== undefined) {
            insertAtCursor(index);
        }
    });
  });

  function insertAtCursor(index) {
      // insert index text at cursor position
      const cursor = editor.getCursor();
      const line = cursor.line;
      const ch = cursor.ch;
      editor.replaceRange(index+',', {line, ch}, {line, ch});
  }

});

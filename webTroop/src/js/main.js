
// @ts-ignore
import CodeMirror from 'codemirror'
import * as Y from 'yjs'
import { WebrtcProvider } from 'y-webrtc'
import { CodemirrorBinding } from 'y-codemirror'
import { Awareness } from 'y-protocols/awareness'
// import { IndexeddbPersistence } from 'y-indexeddb' 
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/python/python.js' // Importer le mode Python
import '../css/style.css'

document.addEventListener('DOMContentLoaded', () => {
  const ws = new WebSocket('ws://localhost:1234');

  // Panneau de configuration
  const configButton = document.getElementById('configButton');
  const configPanel = document.getElementById('configPanel');

  configButton.addEventListener('click', () => {
      configPanel.classList.toggle('open');
  });

  // Fermer le panneau en cliquant en dehors
  document.addEventListener('click', (e) => {
      if (!configPanel.contains(e.target) && 
          !configButton.contains(e.target) && 
          configPanel.classList.contains('open')) {
          configPanel.classList.remove('open');
      }
  });

  // Initialisation de YJS
  const ydoc = new Y.Doc();
  const awareness = new Awareness(ydoc);
  // const indexeddbProvider = new IndexeddbPersistence('webtroop', ydoc);

  const provider = new WebrtcProvider('webtroop', ydoc, {
    awareness: awareness,
    signaling: ['ws://localhost:4444']
  });

  // Gestion de l'état utilisateur
  const userNameInput = document.getElementById('userName');
  const userColorInput = document.getElementById('userColor');

  function updateUserInfo() {
    const userInfo = {
      name: userNameInput.value || 'Anonyme',
      color: userColorInput.value
    };
    
    // Sauvegarder dans localStorage
    localStorage.setItem('webtroop-user', JSON.stringify(userInfo));
    
    // Mettre à jour awareness
    awareness.setLocalStateField('user', userInfo);
  }

  const savedUser = localStorage.getItem('webtroop-user');
  
  if (savedUser) {
    const userInfo = JSON.parse(savedUser);
    userNameInput.value = userInfo.name;
    userColorInput.value = userInfo.color;
    updateUserInfo(); // Mettre à jour awareness avec les valeurs sauvegardées
  }

  userNameInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Empêcher le retour à la ligne
      updateUserInfo();
      userNameInput.blur(); // Enlever le focus
    }
  });
  userColorInput.addEventListener('input', updateUserInfo);

  //Gestion des logs FoxDot pour la console
  ws.onmessage = (event) => {    
    try {
      const message = JSON.parse(event.data);

      if (message.type === 'foxdot_log') {
        appendLog(message.data);
      }
    } catch (error) {
      // console.error('Erreur parsing message:', error);
    }
  };

  function appendLog(message) {
    const logs = document.getElementById('logs');
    const entry = document.createElement('pre');
    entry.className = 'log-entry';
    entry.textContent = message;
    logs.appendChild(entry);
    logs.scrollTop = logs.scrollHeight;
  }
  
  const ytext = ydoc.getText('webtroop');
  
  // Configuration de CodeMirror
  const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    theme: 'monokai',
    lineNumbers: true,
    indentUnit: 4,
    autofocus: true
  });

  // Binding YJS avec CodeMirror
  const binding = new CodemirrorBinding(ytext, editor, provider.awareness);
  
  const themeSelect = document.getElementById('themeSelect');
  themeSelect.addEventListener('change', (e) => {
    const theme = e.target.value;
    editor.setOption('theme', theme);
    // Sauvegarder la préférence
    localStorage.setItem('preferredTheme', theme);
    });

  // Restaurer le thème au chargement
  const savedTheme = localStorage.getItem('preferredTheme');
  if (savedTheme) {
    editor.setOption('theme', savedTheme);
    themeSelect.value = savedTheme;
  }

  // Gestion de CTRL+ENTER
  editor.setOption('extraKeys', {
    'Ctrl-;': (cm) => {
      ws.send(JSON.stringify({
        type: 'evaluate_code',
        code: 'Clock.clear()\n'
      }))
    },  
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

        // Effet flash amélioré
        for (let i = lineStart; i <= lineEnd; i++) {
          const mark = cm.markText(
              {line: i, ch: 0},
              {line: i, ch: cm.getLine(i).length},
              {className: 'flash-highlight'}
          );
          setTimeout(() => mark.clear(), 200);
          }
      }
    },
    
  });
});
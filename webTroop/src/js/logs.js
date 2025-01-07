export const logsUtils = {
  isResizing: false,
  editorContainer: document.getElementById('editor-container'),
  logPanel: document.getElementById('logPanel'),
  otherDisplay: document.getElementById('other-user-display'),
  otherDisplayCode: document.getElementById('other-user-code'),
  otherDisplayPosition: document.getElementById('other-user-position'),
  logs: document.getElementById('logs'),

  initResize: function(editor) {
    this.otherDisplay.addEventListener('mousedown', (e) => {
      this.isResizing = true;
      document.addEventListener('mousemove', this.resize.bind(this, editor));
      document.addEventListener('mouseup', this.stopResize.bind(this));
    });
  },

  // Redimensionnement de la console
  resize: function(editor, e) {
    if (this.isResizing) {
      const containerHeight = this.editorContainer.clientHeight;
      const newLogsHeight = containerHeight - e.clientY;
      this.logPanel.style.height = `${newLogsHeight}px`;
      editor.getWrapperElement().style.height = `${containerHeight - newLogsHeight}px`;
      editor.refresh();
    }
  },

  // Arrêt du redimensionnement
  stopResize: function() {
    this.isResizing = false;
    document.removeEventListener('mousemove', this.resize);
    document.removeEventListener('mouseup', this.stopResize);
  },

  // Affichage du code de l'autre joueur
  insertOtherUserCode: function(line, code) {
    this.otherDisplayCode.innerHTML = `${line}: ${code}`;
  },

  // Affichage de la position de l'autre joueur
  insertOtherUserPosition: function(positionIndicator) {
    this.otherDisplayPosition.innerHTML = positionIndicator;
  },

  // Ajout des logs dans la console
  appendLog(message, color) {
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
    this.logs.insertBefore(entry, logs.firstChild);
    this.logs.scrollTop = 0;
  }
};
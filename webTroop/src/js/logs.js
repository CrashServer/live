export const logsUtils = {
  isResizing: false,
  isResizingEditors: false,
  editorContainer: document.getElementById('editor-container'),
  logPanel: document.getElementById('logPanel'),
  separator: document.getElementById('separator'),
  editorResizeHandle: null,
  logs: document.getElementById('logs'),
  mainEditorWrapper: null,
  otherEditorWrapper: null,
  mainEditor: null,
  otherEditor: null,

    initResize: function(mainEditor, otherEditor) {
    this.mainEditor = mainEditor;
    this.otherEditor = otherEditor;
    this.mainEditorWrapper = document.getElementById('main-editor-wrapper');
    this.otherEditorWrapper = document.getElementById('other-editor-wrapper');
    this.editorResizeHandle = document.getElementById('editor-resize-handle');

    // Redimensionnement de la console (existant)
    this.separator.addEventListener('mousedown', (e) => {
      this.isResizing = true;
      document.addEventListener('mousemove', this.resize.bind(this));
      document.addEventListener('mouseup', this.stopResize.bind(this));
    });

    // Nouveau : Redimensionnement entre les éditeurs
    if (this.editorResizeHandle) {
      this.editorResizeHandle.addEventListener('mousedown', (e) => {
        this.isResizingEditors = true;
        document.addEventListener('mousemove', this.resizeEditors.bind(this));
        document.addEventListener('mouseup', this.stopResizeEditors.bind(this));
        e.preventDefault();
      });
    }
  },

  // Redimensionnement de la console (existant)
  resize: function(e) {
    if (this.isResizing) {
      const containerHeight = this.editorContainer.clientHeight;
      const newLogsHeight = containerHeight - e.clientY;
      
      this.logPanel.style.height = `${newLogsHeight}px`;
      
      const availableHeight = containerHeight - newLogsHeight;
      
      // Calculer les hauteurs actuelles des éditeurs
      const mainHeight = this.mainEditorWrapper.clientHeight;
      const otherHeight = this.otherEditorWrapper.clientHeight;
      const totalEditorsHeight = mainHeight + otherHeight;
      
      // Maintenir les proportions relatives entre les éditeurs
      const mainRatio = mainHeight / totalEditorsHeight;
      const otherRatio = otherHeight / totalEditorsHeight;
      
      const newMainHeight = Math.floor(availableHeight * mainRatio);
      const newOtherHeight = availableHeight - newMainHeight;
      
      if (this.mainEditorWrapper && this.otherEditorWrapper) {
        this.mainEditorWrapper.style.height = `${newMainHeight}px`;
        this.otherEditorWrapper.style.height = `${newOtherHeight}px`;
      }
      
      this.refreshEditors();
    }
  },

  // Nouveau : Redimensionnement entre les éditeurs
  resizeEditors: function(e) {
    if (this.isResizingEditors) {
      const containerRect = this.editorContainer.getBoundingClientRect();
      const logPanelHeight = this.logPanel.clientHeight;
      const availableHeight = containerRect.height - logPanelHeight;
      
      // Calculer la nouvelle position relative
      const relativeY = e.clientY - containerRect.top;
      const newMainHeight = Math.max(150, Math.min(availableHeight - 50, relativeY));
      const newOtherHeight = availableHeight - newMainHeight;
      
      // Appliquer les nouvelles tailles
      if (this.mainEditorWrapper && this.otherEditorWrapper) {
        this.mainEditorWrapper.style.height = `${newMainHeight}px`;
        this.otherEditorWrapper.style.height = `${newOtherHeight}px`;
        
        // Mettre à jour les flex pour maintenir les proportions
        this.mainEditorWrapper.style.flex = newMainHeight;
        this.otherEditorWrapper.style.flex = newOtherHeight;
      }
      
      this.refreshEditors();
    }
  },

  // Arrêt du redimensionnement de la console (existant)
  stopResize: function() {
    this.isResizing = false;
    document.removeEventListener('mousemove', this.resize);
    document.removeEventListener('mouseup', this.stopResize);
  },

  // Nouveau : Arrêt du redimensionnement des éditeurs
  stopResizeEditors: function() {
    this.isResizingEditors = false;
    document.removeEventListener('mousemove', this.resizeEditors);
    document.removeEventListener('mouseup', this.stopResizeEditors);
  },

  refreshEditors: function() {
    if (this.mainEditor) {
      this.mainEditor.refresh();
    }
    if (this.otherEditor) {
      this.otherEditor.refresh();
    }
  },


  // Ajout des logs dans la console
  appendLog(message, color) {
    const entry = document.createElement('pre');
    entry.className = 'log-entry';
    if (color){
      entry.style.color = color;
    }
    if (message.includes('Traceback')) {
      message = this.formatErrorMessage(message);
      entry.classList.add('error-log');
    }
    else if (!message.includes('>>')) {
      entry.classList.add('help');
    }
    entry.textContent = message;
    this.logs.insertBefore(entry, logs.firstChild);
    this.logs.scrollTop = 0;
  },

  formatErrorMessage(errorMessage) {
    const lines = errorMessage.split('\n');
    const caretIndex = lines.findIndex(line => line.includes('File "FoxDot", line 1'));
    if (caretIndex) {
        return lines.slice(caretIndex + 1).join('\n');
    } else {
        return errorMessage;
    }
  }
};
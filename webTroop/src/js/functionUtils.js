export const functionUtils = {
    previousPosition: null,

    stopClock(wsServer) {
        wsServer.send(JSON.stringify({
            type: 'evaluate_code',
            code: 'Clock.clear()\n'
        }));
    },

    // jump^ to the other player's position
    jumpToOtherPlayer(cm, awareness) {
        const states = awareness.getStates();
        states.forEach((state) => {
          if (state.otherInstantCode) { 
            const { user, code, position, line } = state.otherInstantCode;
            if (user !== awareness.getLocalState().user.name){
                this.previousPosition = cm.getCursor();
              cm.setCursor({line: line-1, ch: position});
            }
          }
        }
    )},

    // jump to previous position before jump
    previousJump(cm) {
        if (this.previousPosition) {
          cm.setCursor(this.previousPosition);
          this.previousPosition = null;
        }
    },

    // reset the chrono
    resetChrono(wsServer) {
        wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: 'crashpanel.timeInit = time()\n'
        }));
    },

    // insert attack code at the cursor position
    insertAttackContent(editor, attackContent) {
        const cursor = editor.getCursor();
        const line = cursor.line + 1; // Insérer en dessous de la ligne actuelle
        editor.replaceRange(attackContent, { line: line, ch: 0 });
    },

    // Check if the code to evaluate is a player and if it is, stop it
    ifPlayerStop(codeToEvaluate) {
        const playerPattern = /^[#_]\s*([a-zA-Z]\d+|[a-zA-Z]{2})\s*>>|^#\s*[a-zA-Z]\d+\s*\.\w+\s*=\s*\d+/;
       
        // const playerPattern = /^([#_]\s*[a-zA-Z][a-zA-Z0-9])/;
        // const playerPattern = /^([#_]\s?[a-zA-Z]\d+|[#_]\s?[a-zA-Z]{2})/;
        const match = codeToEvaluate.trim().match(playerPattern);

        if (match) {
          const player = match[1].replace(/^[_#]\s?/, '')
          return `${player}.stop()`;
        }
        return codeToEvaluate;
    },

    getCodeAndCheckStop(cm, multi=false) {
        const cursor = cm.getCursor();
        let startLine = cursor.line;
        let endLine = cursor.line;

        // Si multi-lignes
        if (multi) {
            ({startLine, endLine} = this.getBlock(cm, cursor.line));
        }

        // Extraire le bloc
        const blockCode = cm.getRange(
            {line: startLine, ch: 0},
            {line: endLine, ch: cm.getLine(endLine).length}
        );

        if (blockCode.trim()) {
            // Verifier s'il faut stopper un player
            let blockCodeArray = blockCode.split('\n');
            blockCodeArray.forEach((code, index) => {
            blockCodeArray[index] = functionUtils.ifPlayerStop(code);
            });
            const blockCodeJoin = blockCodeArray.join('\n');
            return [blockCodeJoin, startLine, endLine];
        }
        return [blockCode, startLine, endLine];
    },


    // Save the content of the editor into a .py file
    saveEditorContent(cm) {
        const content = cm.getValue();
        const blob = new Blob([content], {type: 'text/plain'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'code.py';
        a.click();   
    },

    // Get the content and the position of a block
    getBlock(cm, line) {
        let startLine = line;
        let endLine = line;

        // Recherche début du bloc (vers le haut)
        while (startLine > 0 && cm.getLine(startLine - 1).trim() !== '') {
            startLine--;
        }

        // Recherche fin du bloc (vers le bas)
        while (endLine < cm.lineCount() - 1 && cm.getLine(endLine + 1).trim() !== '') {
            endLine++;
        }

        return { startLine, endLine };
    },
};
export const functionUtils = {
    stopClock(wsServer) {
        wsServer.send(JSON.stringify({
            type: 'evaluate_code',
            code: 'Clock.clear()\n'
        }));
    },

    jumpToOtherPlayer(cm, awareness) {
        const states = awareness.getStates();
        states.forEach((state) => {
          if (state.otherInstantCode) { 
            const { user, code, position, line } = state.otherInstantCode;
            if (user !== awareness.getLocalState().user.name){
              cm.setCursor({line: line-1, ch: position});
            }
          }
        }
    )},

    resetChrono(wsServer) {
        wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: 'crashpanel.timeInit = time()\n'
        }));
    },

    insertAttackContent(editor, attackContent) {
        const cursor = editor.getCursor();
        const line = cursor.line + 1; // Insérer en dessous de la ligne actuelle
        editor.replaceRange(attackContent, { line: line, ch: 0 });
    },

    // setMarker(cm, color="", txt="") {
    //     const line = cm.getCursor().line
    //     const info = cm.lineInfo(line);
    //     if (info.handle.gutterClass != null && info.handle.gutterClass.includes(`line${color}`)){
    //       cm.removeLineClass(line, "gutter")
    //       cm.removeLineClass(line, "background")
    //     }
    //     else {
    //       cm.removeLineClass(line, "gutter")
    //       cm.removeLineClass(line, "background")
    //       cm.addLineClass(line, "gutter", `line${color}`)
    //       cm.addLineClass(line, "background", `line${color}`)
    //       return true;
          
    //     }
    // },

    ifPlayerStop(codeToEvaluate) {
        const playerPattern = /^_([a-zA-Z]\d+|[a-zA-Z]{2})/;
        const match = codeToEvaluate.trim().match(playerPattern);

        if (match) {
          const player = match[1];
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
            // Recherche début du bloc (vers le haut)
            while (startLine > 0 && cm.getLine(startLine - 1).trim() !== '') {
                startLine--;
            }

            // Recherche fin du bloc (vers le bas)
            while (endLine < cm.lineCount() - 1 && cm.getLine(endLine + 1).trim() !== '') {
                endLine++;
            }
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
};
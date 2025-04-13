export const functionUtils = {
    previousPosition: null,
    playersList: [],

    stopClock(wsServer) {
        wsServer.send(JSON.stringify({
            type: 'evaluate_code',
            code: 'Clock.clear()\nsoff()\n'
        }));
    },

    unSoloPlayers(wsServer) {
        wsServer.send(JSON.stringify({
            type: 'evaluate_code',
            code: 'unsolo()\n'
        }));
    },

    soloPlayer(cm, wsServer) {
        const cursor = cm.getCursor();
        let startLine = cursor.line;
        let endLine = cursor.line;

        // Extraire le bloc
        const blockCode = cm.getRange(
            {line: startLine, ch: 0},
            {line: endLine, ch: cm.getLine(endLine).length}
        );

        const playerName = this.getPlayer(blockCode);
    
        if (playerName) {
            wsServer.send(JSON.stringify({
                type: 'evaluate_code',
                code: `${playerName}.solo()\n`
            }));
        }
    },

    resetPlayer(cm, wsServer) {
        const cursor = cm.getCursor();
        const line = cursor.line;
        const code = cm.getLine(line).trim();
        if (code) {
            wsServer.send(JSON.stringify({
                type: 'evaluate_code',
                code: `~${code}\n`
            }));
        }
    },

    sendSceneName(cm, foxdotWs){
        const cursor = cm.getCursor();
        const line = cursor.line;
        const sceneName = cm.getLine(line).trim();
        foxdotWs.send(JSON.stringify({
            type: 'sceneName',
            sceneName: sceneName
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
        const match = codeToEvaluate.trim().match(playerPattern);

        if (match) {
            const player = match[1].replace(/^[_#]\s?/, '')
            return `${player}.stop()`;
        }
        return codeToEvaluate;
    },

    isVideoCode(cm) {
        const cursor = cm.getCursor();
        const line = cursor.line;
        const code = cm.getLine(cursor.line).trim();
        const videoPattern = /^!/;
        if (videoPattern.test(code)) {
            return [code.substring(1).trim(), line];
        }
        return false
    },

    getPlayer(code) {
        const playerPattern = /^[a-zA-Z][a-zA-Z0-9]/;
        const match = code.trim().match(playerPattern);
        if (match) {
            return match[0];
        }
        return null;
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
    saveEditorContent(cm, wsServer) {
        let content = cm.getValue();
        let filename = '';

        // Vérifier si une partie du texte est sélectionnée
        const selection = cm.getSelection();
        if (selection) {
            content = selection;
            const lines = selection.split('\n');
            // Vérifier si le texte commence par un '#'
            if (lines[0].trim().startsWith('#')) {
                // Extraire le nom du fichier de la première ligne après le '#'
                filename = lines[0].trim().substring(1).trim() + '.py';
            }
        }

        // Si aucun nom de fichier n'a été trouvé, utiliser un timestamp
        if (!filename) {
            const timestamp = new Date().toISOString().replace(/[:.-]/g, '');
            filename = `code_${timestamp}.py`;
        }

        if (selection) {
            const message = {
                type: 'save_file',
                filename: filename,
                content: content
            };
            wsServer.send(JSON.stringify(message));
        } else {
            // sauvegarder le fichier en demandant le chemin
            const blob = new Blob([content], {type: 'text/plain'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
        }
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
    incrementValue(cm, value) {
        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);
        
        // Trouver les limites du nombre à partir de la position du curseur
        let start = cursor.ch;
        let end = cursor.ch;
        
        // Recherche du début du nombre (vers la gauche)
        while (start > 0 && /[\d\.\-]/.test(line.charAt(start - 1))) {
            start--;
        }
        
        // Recherche de la fin du nombre (vers la droite)
        while (end < line.length && /[\d\.]/.test(line.charAt(end))) {
            end++;
        }
        
        // Extraire le nombre complet
        let numberStr = line.substring(start, end);

        // Vérifier si c'est un nombre commençant par un point (comme .5)
        const startsWithDot = /^\.\d+$/.test(numberStr);
    
        // Ajouter un zéro en préfixe pour le traitement interne si nécessaire
        if (startsWithDot) {
            numberStr = "0" + numberStr;
        }
        
        // Vérifier si c'est un nombre valide
        if (/^-?\d+(\.\d+)?$/.test(numberStr)) {
            let result;
            
            // Déterminer s'il s'agit d'un entier ou d'un nombre à virgule
            if (numberStr.includes('.')) {
                // Nombre décimal
                const num = parseFloat(numberStr);
                
                // Récupérer le nombre de décimales
                const decimalPart = numberStr.split('.')[1] || '';
                const precision = decimalPart.length > 0 ? decimalPart.length : 1; // Au moins 1 décimale
                // Incrémenter de 0.01 pour les décimaux et garder le bon format
                const multiplier = (precision > 1) ? 0.01 : 0.1;
                result = (num + (value * multiplier)).toFixed(precision);
                
                // Supprimer les zéros non significatifs à la fin si le nombre original n'en avait pas
                // if (!numberStr.endsWith('0')) {
                //     result = result.replace(/0+$/, '');
                //     if (result.endsWith('.')) {
                //         result = result.slice(0, -1);
                //     }
                // }
            } else {
                // Nombre entier
                const num = parseInt(numberStr, 10);
                
                // Pour les nombres supérieurs à 99, incrémenter par 100
                if (Math.abs(num) > 99) {
                    result = (num + (value * 100)).toString();
                } else {
                    result = (num + value).toString();
                }
            }
            
            // Remplacer l'ancien nombre par le nouveau
            cm.replaceRange(result, {line: cursor.line, ch: start}, {line: cursor.line, ch: end});
            
            // Replacer le curseur
            cm.setCursor({line: cursor.line, ch: start + result.length});
        }
    },

    // Fonction pour aller à la prochaine occurrence de virgule
    goToNextComma(cm) {
        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);
        const nextCommaIndex = line.indexOf(',', cursor.ch + 1);
        if (nextCommaIndex !== -1) {
        cm.setCursor({ line: cursor.line, ch: nextCommaIndex + 1 });
        }
        else {
            cm.execCommand("goWordRight");
        }
    },
  
    // Fonction pour aller à la précédente occurrence de virgule
    goToPreviousComma(cm) {
        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);
        const previousCommaIndex = line.lastIndexOf(',', cursor.ch - 1);
        if (previousCommaIndex !== -1) {
        cm.setCursor({ line: cursor.line, ch: previousCommaIndex });
        } else {
            cm.execCommand("goWordLeft");
        }
    },

    formatFoxDotAutocomplete(message) {
        // Get loop List
        const loopList = message.autocomplete.loopList
        const formattedLoops = loopList.map(loop => {
            const match = loop.match(/\d+/);
            let dur= "";
            if  (loop.startsWith("AKWF")) {
                dur = ``; 
            }
            else {
                dur = match ? `, dur=${parseInt(match[0], 10)}` : ""; // Extraire la durée du nom de la loop ou définir une chaîne vide
            }
            return { text: `"${loop}"${dur}`, displayText: loop };
        });
       
        const fxList = message.autocomplete.fxList;
        const updatedFxList = fxList.map(fx => {
        const fxName = fx.displayText.replace(/_$/, ''); // Retirer le suffixe '_'
        return { text: `${fxName}=`, displayText: fxName };
        });
        const allFx = [...fxList, ...updatedFxList];

        // Get SynthDefs
        const synthDefs = message.autocomplete.synthList;
        const updatedSynthDefs = synthDefs
            .filter(synth => synth.displayText !== 'play2')
            .map(synth => {
            if (synth.displayText === 'play1') {
                return { ...synth, displayText: 'play'};
            }
            return synth;
        });

        const formattedSynthDefs = updatedSynthDefs.map(synth => {
          return { text: synth.displayText, displayText: synth.displayText };
        });
        const argsSynth = updatedSynthDefs.map(synth => {
          return { text: synth.displayText + "(" + synth.text + ")", displayText: synth.displayText + "_" };
        });
        const allSynthDefs = [...formattedSynthDefs, ...argsSynth];

        // Get AttackList
        const attackList = message.autocomplete.attackList;

        return { loops: formattedLoops, fxList: allFx, synthList: allSynthDefs, attackList: attackList };
    }
};

export let playersList = [];

export function updatePlayersList(newPlayersList) {
    playersList = newPlayersList;
}
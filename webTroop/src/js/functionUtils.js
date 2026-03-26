export const functionUtils = {
    previousPosition: null,
    playersList: [],

    // === AUTOMATION RECORDER ===
    _autoRec: {
        armed: false,
        startTime: 0,
        bpm: 120,
        recordings: {},  // { paramName: [{time, value}, ...] }
        cursorLine: null,
    },

    autoRecToggle(cm, evaluateFn, wsServer) {
        const rec = this._autoRec;
        if (!rec.armed) {
            // ARM — start recording
            rec.armed = true;
            rec.startTime = performance.now();
            rec.recordings = {};
            rec.cursorLine = cm.getCursor().line;
            rec.originalLine = cm.getLine(rec.cursorLine);
            // Get BPM from FoxDot
            this._autoRecFetchBpm(wsServer);
            this._autoRecShowIndicator(true);
        } else {
            // DISARM — stop, convert, replace
            rec.armed = false;
            this._autoRecShowIndicator(false);
            this._autoRecFinalize(cm, evaluateFn);
        }
    },

    autoRecCancel(cm, evaluateFn) {
        const rec = this._autoRec;
        if (!rec.armed) return;
        rec.armed = false;
        this._autoRecShowIndicator(false);
        // Restore params to their first recorded values
        const line = cm.getLine(rec.cursorLine);
        let newLine = line;
        // Sort position-based in reverse to avoid offset shifts
        const params = Object.keys(rec.recordings).sort((a, b) => {
            const posA = a.startsWith('@pos') ? parseInt(a.slice(4)) : -1;
            const posB = b.startsWith('@pos') ? parseInt(b.slice(4)) : -1;
            return posB - posA;
        });
        for (const param of params) {
            const firstVal = rec.recordings[param][0];
            const lastVal = rec.recordings[param][rec.recordings[param].length - 1];
            if (!firstVal) continue;
            if (param.startsWith('@pos')) {
                // Use exact position from last capture to find current value
                const start = lastVal.charStart;
                const end = lastVal.charEnd;
                if (start >= 0 && end <= newLine.length) {
                    newLine = newLine.substring(0, start) + firstVal.value + newLine.substring(end);
                }
            } else {
                const regex = new RegExp(param + '\\s*=\\s*[\\d.\\-]+');
                newLine = newLine.replace(regex, param + '=' + firstVal.value);
            }
        }
        if (newLine !== line) {
            cm.replaceRange(newLine,
                { line: rec.cursorLine, ch: 0 },
                { line: rec.cursorLine, ch: line.length }
            );
            if (evaluateFn) evaluateFn(cm, false);
        }
        rec.recordings = {};
    },

    autoRecCapture(cm) {
        const rec = this._autoRec;
        if (!rec.armed) return;

        // Track current cursor line (may shift if others add/remove lines)
        rec.cursorLine = cm.getCursor().line;

        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);

        // Find number boundaries at cursor
        let numStart = cursor.ch;
        let numEnd = cursor.ch;
        while (numStart > 0 && /[\d.\-]/.test(line.charAt(numStart - 1))) numStart--;
        while (numEnd < line.length && /[\d.]/.test(line.charAt(numEnd))) numEnd++;
        const valueStr = line.substring(numStart, numEnd);
        if (!/^-?\d+(\.\d+)?$/.test(valueStr)) return;

        // Try to find param name (e.g. "tcut" from "tcut=400")
        let paramName = null;
        let eqPos = numStart - 1;
        while (eqPos >= 0 && line.charAt(eqPos) === ' ') eqPos--;
        if (eqPos >= 0 && line.charAt(eqPos) === '=') {
            let nameEnd = eqPos;
            let nameStart = nameEnd - 1;
            while (nameStart >= 0 && /[a-zA-Z_\d]/.test(line.charAt(nameStart))) nameStart--;
            nameStart++;
            paramName = line.substring(nameStart, nameEnd);
        }

        // No param name (degree, value inside list, TimeVar arg) — use position
        if (!paramName) {
            paramName = `@pos${numStart}`;
        }

        // Detect if this number is in a TimeVar duration position
        // Walk backwards from cursor tracking paren depth to find enclosing TimeVar
        const before = line.substring(0, numStart);
        let isDurationArg = false;
        let depth = 0;
        let enclosingFnStart = -1;
        for (let i = before.length - 1; i >= 0; i--) {
            const ch = before.charAt(i);
            if (ch === ')') depth++;
            if (ch === '(') {
                if (depth === 0) {
                    // This is the opening paren that encloses our cursor
                    // Check if it's a TimeVar function
                    const preceding = before.substring(0, i);
                    if (/(?:linvar|sinvar|expvar|var)\s*$/.test(preceding)) {
                        enclosingFnStart = i;
                    }
                    break;
                }
                depth--;
            }
        }
        if (enclosingFnStart >= 0) {
            // We're inside a TimeVar call — check if after "],
            const insideFn = before.substring(enclosingFnStart);
            if (insideFn.indexOf('],') !== -1) {
                isDurationArg = true;
            }
        }

        const elapsed = (performance.now() - rec.startTime) / 1000;
        const beatTime = elapsed * (rec.bpm / 60);

        if (!rec.recordings[paramName]) {
            rec.recordings[paramName] = [];
        }
        rec.recordings[paramName].push({
            time: beatTime,
            value: parseFloat(valueStr),
            charStart: numStart,
            charEnd: numEnd,
            isDurationArg: isDurationArg,
        });
    },

    _autoRecFetchBpm(wsServer) {
        // Read BPM from the crashpanel display
        const bpmEl = document.getElementById('bpm');
        if (bpmEl) {
            this._autoRec.bpm = parseFloat(bpmEl.textContent) || 120;
        } else {
            this._autoRec.bpm = 120;
        }
    },

    _autoRecShowIndicator(show) {
        let el = document.getElementById('autorec-indicator');
        if (show) {
            if (!el) {
                el = document.createElement('div');
                el.id = 'autorec-indicator';
                el.style.cssText = 'position:fixed;top:8px;right:8px;background:#e33;color:#fff;padding:4px 10px;border-radius:4px;font-size:12px;font-family:monospace;z-index:9999;animation:pulse 1s infinite;';
                const style = document.createElement('style');
                style.textContent = '@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}';
                document.head.appendChild(style);
                document.body.appendChild(el);
            }
            el.textContent = '● REC';
            el.style.display = 'block';
        } else if (el) {
            el.style.display = 'none';
        }
    },

    _autoRecFinalize(cm, evaluateFn) {
        const rec = this._autoRec;
        const recordings = rec.recordings;
        const paramNames = Object.keys(recordings);
        if (paramNames.length === 0) return;

        // Sort position-based keys in reverse order so replacements don't shift offsets
        const sorted = paramNames.sort((a, b) => {
            const posA = a.startsWith('@pos') ? parseInt(a.slice(4)) : -1;
            const posB = b.startsWith('@pos') ? parseInt(b.slice(4)) : -1;
            return posB - posA; // reverse: replace from right to left
        });

        const line = cm.getLine(rec.cursorLine);
        let newLine = line;

        for (const param of sorted) {
            const points = recordings[param];
            if (points.length < 2) continue;

            const isDurArg = points.some(p => p.isDurationArg);
            const converted = this._autoRecConvert(points, isDurArg);

            const last = points[points.length - 1];

            if (param.startsWith('@pos')) {
                // Position-based: use exact position from last capture
                const start = last.charStart;
                const end = last.charEnd;
                if (start >= 0 && end <= newLine.length) {
                    newLine = newLine.substring(0, start) + converted + newLine.substring(end);
                }
            } else {
                // Named param: replace "param=VALUE" or "param=expression"
                const regex = new RegExp(param + '\\s*=\\s*(?:(?:linvar|sinvar|expvar|var)\\([^)]*(?:\\([^)]*\\))?[^)]*\\)|[\\d.\\-]+)');
                newLine = newLine.replace(regex, param + '=' + converted);
            }
        }

        if (newLine !== line) {
            cm.replaceRange(newLine,
                { line: rec.cursorLine, ch: 0 },
                { line: rec.cursorLine, ch: line.length }
            );
            if (evaluateFn) evaluateFn(cm, false);
        }
    },

    _autoRecRoundValue(val) {
        // Round to clean numbers
        if (Math.abs(val) >= 100) return Math.round(val / 50) * 50;
        if (Math.abs(val) >= 10) return Math.round(val / 5) * 5;
        if (Math.abs(val) >= 1) return Math.round(val * 10) / 10;
        return Math.round(val * 100) / 100;
    },

    _autoRecConvert(points, isDurationArg = false) {
        const values = points.map(p => this._autoRecRoundValue(p.value));
        const min = Math.min(...values);
        const max = Math.max(...values);

        // No real change — return static
        if (max - min < 0.01) return String(values[0]);

        // Find peaks and valleys with their timestamps
        const extremes = [{ value: values[0], time: points[0].time }];
        for (let i = 1; i < values.length - 1; i++) {
            const prev = values[i - 1];
            const curr = values[i];
            const next = values[i + 1];
            if ((curr >= prev && curr >= next && curr > prev) ||
                (curr <= prev && curr <= next && curr < prev)) {
                const last = extremes[extremes.length - 1];
                if (Math.abs(curr - last.value) > (max - min) * 0.15) {
                    extremes.push({ value: curr, time: points[i].time });
                }
            }
        }
        extremes.push({ value: values[values.length - 1], time: points[points.length - 1].time });

        // Deduplicate consecutive same values (keep latest timestamp)
        const unique = [extremes[0]];
        for (let i = 1; i < extremes.length; i++) {
            if (extremes[i].value !== unique[unique.length - 1].value) {
                unique.push(extremes[i]);
            }
        }

        // Compute durations between extremes and snap to musical grid
        const durations = [];
        for (let i = 1; i < unique.length; i++) {
            const raw = unique[i].time - unique[i - 1].time;
            durations.push(this._autoRecSnapBeat(raw));
        }
        const vals = unique.map(u => u.value);

        // Duration arg position — no TimeVars allowed, plain list only
        if (isDurationArg) {
            if (vals.length === 1) return String(vals[0]);
            return `[${vals.join(', ')}]`;
        }

        // Detect shape
        if (vals.length === 2) {
            return `linvar([${vals[0]}, ${vals[1]}], ${durations[0]})`;
        }

        if (vals.length === 3 && Math.abs(vals[0] - vals[2]) < (max - min) * 0.1) {
            // Symmetric — sinvar
            const totalDur = durations[0] + durations[1];
            return `sinvar([${vals[0]}, ${vals[1]}], ${this._autoRecSnapBeat(totalDur)})`;
        }

        // Check if all durations are the same (within tolerance)
        const avgDur = durations.reduce((a, b) => a + b, 0) / durations.length;
        const allSame = durations.every(d => Math.abs(d - avgDur) < 0.3);

        if (allSame) {
            // Equal spacing — single duration value
            return `linvar([${vals.join(', ')}], ${durations[0]})`;
        }

        // Varied timing — use duration array
        return `linvar([${vals.join(', ')}], [${durations.join(', ')}])`;
    },

    _autoRecSnapBeat(beats) {
        // Snap to nearest musical subdivision
        const grid = [0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16, 32];
        let best = 1;
        let bestDist = Infinity;
        for (const g of grid) {
            const dist = Math.abs(beats - g);
            if (dist < bestDist) {
                bestDist = dist;
                best = g;
            }
        }
        return best;
    },

    stopClock(wsServer) {
        wsServer.send(JSON.stringify({
            type: 'evaluate_code',
            code: 'Clock.clear()\nsoff()\nServer.clearFx()\n'
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

    soloDrop(cm, wsServer) {
        const cursor = cm.getCursor();
        let startLine = cursor.line;
        let endLine = cursor.line;
        const code = cm.getLine(cursor.line).trim();

        const playerName = this.getPlayer(code);
        if (playerName) {
            wsServer.send(JSON.stringify({
                type: 'evaluate_code',
                code: `${playerName}.solo()\n`
            }));
            wsServer.send(JSON.stringify({
                type: 'evaluate_code',
                code: `Clock.schedule(unsolo, Clock.mod(64))\n`
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

    isServerFxCode(cm) {
        const cursor = cm.getCursor();
        const line = cursor.line;
        const code = cm.getLine(cursor.line).trim();
        const serverFxPattern = /^# Server\.addFx/;
        if (serverFxPattern.test(code)) {
            return [code, line];
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
            // Verifier s'il faut stopper un player et convertir les syntaxes ! et ?
            let blockCodeArray = blockCode.split('\n');
            let hasChanged = false;

            blockCodeArray.forEach((code, index) => {
                let convertedCode = code;

                // Convertir ?nombre en PRand(0, nombre)
                const convertedQuestion = this.convertQuestionMarkToPRand(convertedCode);
                if (convertedQuestion !== convertedCode) {
                    hasChanged = true;
                    convertedCode = convertedQuestion;
                }

                // Convertir expression!nombre en var(expression, nombre)
                const convertToVar = this.convertExclamationToVar(convertedCode);
                if (convertToVar !== convertedCode) {
                    hasChanged = true;
                    convertedCode = convertToVar;
                }

                blockCodeArray[index] = functionUtils.ifPlayerStop(convertedCode);
            });

            const blockCodeJoin = blockCodeArray.join('\n');

            // Remplacer dans l'éditeur si le code a changé
            if (hasChanged) {
                cm.replaceRange(
                    blockCodeJoin,
                    {line: startLine, ch: 0},
                    {line: endLine, ch: cm.getLine(endLine).length}
                );
            }

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

    // Parse a #@section(beats) or #@section tag line
    // Returns {name, beats, type} or null
    // beats is null when no number is given (play forever)
    parseSectionTag(lineText) {
        const trimmed = lineText.trim();
        const specialTypes = { end: 'end', endfade: 'endfade', loop: 'loop', clear: 'clear' };

        // Try with args: #@name(...)
        const matchArgs = trimmed.match(/^#@(\w+)\(([^)]*)\)/);
        if (matchArgs) {
            const name = matchArgs[1];
            const rawArgs = matchArgs[2];
            const type = specialTypes[name] || 'section';
            let beats = null;
            let targets = [];

            const parts = rawArgs.split(',').map(p => p.trim()).filter(p => p);
            if (parts.length > 0) {
                // First part: beats if numeric (int, float, or fraction)
                const first = parts[0];
                const numVal = first.includes('/')
                    ? first.split('/').reduce((a, b) => parseFloat(a) / parseFloat(b))
                    : parseFloat(first);
                if (!isNaN(numVal)) {
                    beats = numVal;
                    parts.shift();
                }
                // Remaining: targets with optional :weight
                for (const p of parts) {
                    if (p.includes(':')) {
                        const [t, w] = p.split(':');
                        targets.push({ name: t.trim(), weight: parseInt(w.trim()) || 1 });
                    } else {
                        targets.push({ name: p.trim(), weight: 1 });
                    }
                }
            }
            return { name, beats, type, targets };
        }
        // Try without args: #@name
        const matchNoBeat = trimmed.match(/^#@(\w+)$/);
        if (matchNoBeat) {
            const name = matchNoBeat[1];
            const type = specialTypes[name] || 'section';
            return { name, beats: null, type, targets: [] };
        }
        return null;
    },

    // Collect code from the line AFTER a #@ tag until the next #@ or EOF
    getSectionCode(cm, sectionLine) {
        let endLine = sectionLine + 1;
        while (endLine < cm.lineCount()) {
            if (cm.getLine(endLine).trim().startsWith('#@')) break;
            endLine++;
        }
        if (sectionLine + 1 >= endLine) return '';
        return cm.getRange(
            {line: sectionLine + 1, ch: 0},
            {line: endLine - 1, ch: cm.getLine(endLine - 1).length}
        );
    },

    // Return all #@ sections in document order
    findAllSections(cm) {
        const sections = [];
        for (let i = 0; i < cm.lineCount(); i++) {
            const tag = this.parseSectionTag(cm.getLine(i));
            if (tag) sections.push({ line: i, ...tag });
        }
        return sections;
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

            } else {
                // Nombre entier
                const num = parseInt(numberStr, 10);

                // Pour les nombres supérieurs à 99, incrémenter par 100
                if (Math.abs(num) > 300) {
                    result = (num + (value * 100)).toString();
                } else {
                    result = (num + value).toString();
                }
            }

            if (parseInt(result) > 22000) {
                result = "22000";
            }

            if (value == -10 && parseInt(result) < 0) {
                result = "0";
            }

            // Remplacer l'ancien nombre par le nouveau
            cm.replaceRange(result, {line: cursor.line, ch: start}, {line: cursor.line, ch: end});

            // Replacer le curseur
            cm.setCursor({line: cursor.line, ch: start + result.length});
        }
    },

    randomizer(cm) {
        const cursor = cm.getCursor();
        const line = cm.getLine(cursor.line);

        const quoteBefore = line.lastIndexOf('"', cursor.ch);
        const quoteAfter = line.indexOf('"', cursor.ch);

        // Cas 1: Vérifier si le curseur est dans un paramètre de la forme name=value
        const equalPosBefore = line.lastIndexOf('=', cursor.ch);
        if (equalPosBefore !== -1) {
            // Trouver le début du paramètre (le nom avant le =)
            let paramStart = equalPosBefore;
            while (paramStart > 0 && /[a-zA-Z0-9_]/.test(line.charAt(paramStart - 1))) {
                paramStart--;
            }

            // Trouver la fin du paramètre (jusqu'à la virgule ou la fin)
            let paramEnd = equalPosBefore + 1;

            // Tenir compte des structures imbriquées après le =
            let openBrackets = 0;
            let openParens = 0;

            while (paramEnd < line.length) {
                const char = line.charAt(paramEnd);
                if (char === '[') openBrackets++;
                else if (char === ']') openBrackets--;
                else if (char === '(') openParens++;
                else if (char === ')') openParens--;
                else if (char === ',' && openBrackets === 0 && openParens === 0) break;

                paramEnd++;
            }

            // Vérifier si le curseur est dans ce paramètre
            if (cursor.ch > equalPosBefore && cursor.ch < paramEnd) {
                const paramContent = line.substring(equalPosBefore + 1, paramEnd);

                // Vérifier si c'est une valeur simple ou une structure complexe
                if (/^\s*-?\d*\.?\d+\s*$/.test(paramContent) || /^\s*\.\d+\s*$/.test(paramContent)) {
                    // C'est un nombre simple, randomiser directement
                    const trimmedContent = paramContent.trim();
                    const startsWithDot = /^\.\d+$/.test(trimmedContent);
                    const numberStr = startsWithDot ? "0" + trimmedContent : trimmedContent;
                    const result = this.randomizeNumber(numberStr, startsWithDot);

                    // Remplacer la valeur
                    cm.replaceRange(result,
                        {line: cursor.line, ch: equalPosBefore + 1},
                        {line: cursor.line, ch: paramEnd});
                    return;
                } else {
                    // C'est une structure complexe, vérifier les délimiteurs à l'intérieur
                    const innerBrackets = [
                        { open: '[', close: ']' },
                        { open: '(', close: ')' }
                    ];

                    for (const bracket of innerBrackets) {
                        const innerOpenPos = paramContent.indexOf(bracket.open);
                        if (innerOpenPos !== -1) {
                            // Trouver la position correspondante du délimiteur fermant
                            let depth = 1;
                            let innerClosePos = -1;

                            for (let i = innerOpenPos + 1; i < paramContent.length; i++) {
                                if (paramContent[i] === bracket.open) depth++;
                                else if (paramContent[i] === bracket.close) {
                                    depth--;
                                    if (depth === 0) {
                                        innerClosePos = i;
                                        break;
                                    }
                                }
                            }

                            if (innerClosePos !== -1) {
                                // Si le curseur est à l'intérieur de ces délimiteurs
                                const absOpenPos = equalPosBefore + 1 + innerOpenPos;
                                const absClosePos = equalPosBefore + 1 + innerClosePos;

                                if (cursor.ch > absOpenPos && cursor.ch < absClosePos) {
                                    const innerContent = paramContent.substring(innerOpenPos + 1, innerClosePos);
                                    const randomized = this.randomizeNumbersInString(innerContent);

                                    // Remplacer le contenu entre les délimiteurs
                                    cm.replaceRange(randomized,
                                        {line: cursor.line, ch: absOpenPos + 1},
                                        {line: cursor.line, ch: absClosePos});
                                    cm.setCursor({line: cursor.line, ch: absOpenPos + 1});
                                    return;
                                }
                            }
                        }
                    }
                }
            }
        }

        // Cas 2: Vérifier les délimiteurs directs autour du curseur
        const brackets = [
            { open: '[', close: ']' },
            { open: '(', close: ')' }
        ];

        for (const bracket of brackets) {
            // Trouver tous les couples de délimiteurs dans la ligne
            let depth = 0;
            let openPositions = [];
            let matchingClosePositions = [];

            for (let i = 0; i < line.length; i++) {
                if (line[i] === bracket.open) {
                    if (depth === 0) {
                        openPositions.push(i);
                    }
                    depth++;
                } else if (line[i] === bracket.close && depth > 0) {
                    depth--;
                    if (depth === 0) {
                        matchingClosePositions.push(i);
                    }
                }
            }

            // Vérifier chaque paire de délimiteurs
            for (let j = 0; j < openPositions.length; j++) {
                const openPos = openPositions[j];
                const closePos = matchingClosePositions[j];

                // Si le curseur est entre ces délimiteurs
                if (closePos && cursor.ch > openPos && cursor.ch < closePos) {
                    const content = line.substring(openPos + 1, closePos);
                    const randomized = this.randomizeNumbersInString(content);

                    // Remplacer le contenu entre les délimiteurs
                    cm.replaceRange(randomized,
                        {line: cursor.line, ch: openPos + 1},
                        {line: cursor.line, ch: closePos});
                    return;
                }
            }
        }

        // Cas 3: Si aucun délimiteur ou paramètre n'est trouvé, traiter un seul nombre sous le curseur
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

        // Si le curseur est sur un nombre
        if (start !== end) {
            let numberStr = line.substring(start, end);
            const startsWithDot = /^\.\d+$/.test(numberStr);

            if (startsWithDot) {
                numberStr = "0" + numberStr;
            }

            // Vérifier si c'est un nombre valide
            if (/^-?\d+(\.\d+)?$/.test(numberStr)) {
                const result = this.randomizeNumber(numberStr, startsWithDot);

                // Remplacer l'ancien nombre par le nouveau
                cm.replaceRange(result, {line: cursor.line, ch: start}, {line: cursor.line, ch: end});

                // Replacer le curseur
                cm.setCursor({line: cursor.line, ch: start });
            }
        }
    },

    randomizeNumbersInString(str) {
        // Recherche tous les nombres dans la chaîne (entiers et décimaux, incluant .5)
        return str.replace(/(-?\d*\.?\d+)|(\.\d+)/g, match => {
            const startsWithDot = /^\.\d+$/.test(match);
            const numberStr = startsWithDot ? "0" + match : match;
            return this.randomizeNumber(numberStr, startsWithDot);
        });
    },

    randomizeNumber(numberStr, startsWithDot) {
        let result;

        // Déterminer s'il s'agit d'un entier ou d'un nombre à virgule
        if (numberStr.includes('.')) {
            // Nombre décimal
            const num = parseFloat(numberStr);
            const decimalPart = numberStr.split('.')[1] || '';
            const precision = decimalPart.length;

            // Pour les très petits nombres, utiliser une plage adaptée
            let minVal, maxVal;
            if (Math.abs(num) < 0.2) {
                minVal = 0.05;
                maxVal = 0.3;
            } else {
                // Générer un nombre aléatoire du même ordre de grandeur
                minVal = Math.max(0.001, num * 0.5); // Minimum: 50% de la valeur originale avec un plancher
                maxVal = num * 1.5; // Maximum: 150% de la valeur originale
            }

            // Nouvelle valeur aléatoire
            let randomVal = minVal + (Math.random() * (maxVal - minVal));

            // Formater le résultat avec le bon nombre de décimales
            result = randomVal.toFixed(precision);

            // Si le nombre original commençait par un point, enlever le 0 du début
            if (startsWithDot && result.startsWith('0.')) {
                result = result.substring(1);
            }
        } else {
            // Nombre entier
            const num = parseInt(numberStr, 10);

            // Calculer le facteur de randomisation en fonction de la taille du nombre
            const magnitude = Math.abs(num) > 200 ? 100 : 1;

            // Générer un entier aléatoire du même ordre de grandeur
            const minVal = Math.max(magnitude, Math.floor(num * 0.5)); // Minimum: 50% de la valeur originale
            const maxVal = Math.ceil((num < 15000) ? num * 1.5: 15000); // Maximum: 150% de la valeur originale

            // Nouvelle valeur aléatoire
            result = (Math.floor(Math.random() * (maxVal - minVal + magnitude)) + minVal);
            result = (result < 15000 ? result : 15000);
            result = (magnitude*Math.floor(parseInt(result/magnitude))).toString();
        }
        return result;
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
            const match = loop.match(/\d+$/);
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
        // Ne garder que les FX avec '_' mais les afficher sans le '_'
        const formattedFxList = fxList.map(fx => {
            const fxName = fx.displayText.replace(/_$/, ''); // Retirer le suffixe '_' pour l'affichage
            return { text: fx.text, displayText: fxName, tag: fx.tag };
        });

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

        // const formattedSynthDefs = updatedSynthDefs.map(synth => {
        //   return { text: synth.displayText, displayText: synth.displayText, tag: synth.tag };
        // });
        const argsSynth = updatedSynthDefs.map(synth => {
          return { text: synth.displayText + "(" + synth.text + ")", displayText: synth.displayText, tag: synth.tag };
        });
        // const allSynthDefs = [...formattedSynthDefs, ...argsSynth];
        const allSynthDefs = [...argsSynth];


        // Get AttackList
        const attackList = message.autocomplete.attackList;

        return { loops: formattedLoops, fxList: formattedFxList, synthList: allSynthDefs, attackList: attackList };
    },

    // Convertir la syntaxe expression!<number> en var(expression, <number>)
    convertExclamationToVar(code) {
        // Traiter d'abord les cas simples avec crochets
        code = code.replace(/(\[[^\]]+\])!(\d+)/g, 'var($1, [$2, $2])');

        // Pour les fonctions avec parenthèses, on doit gérer les parenthèses imbriquées
        // On cherche pattern: nom_fonction(...contenu_avec_parentheses...)!nombre
        let result = code;
        let match;
        const funcPattern = /(\w+)\(/g;

        while ((match = funcPattern.exec(result)) !== null) {
            const funcName = match[1];
            let startPos = match.index + funcName.length + 1; // Position après la parenthèse ouvrante
            let depth = 1;
            let endPos = startPos;

            // Trouver la parenthèse fermante correspondante
            while (endPos < result.length && depth > 0) {
                if (result[endPos] === '(') depth++;
                else if (result[endPos] === ')') depth--;
                endPos++;
            }

            // Vérifier s'il y a un ! suivi d'un nombre juste après
            if (endPos < result.length && result[endPos] === '!') {
                const numMatch = result.substring(endPos + 1).match(/^(\d+)/);
                if (numMatch) {
                    const num = numMatch[1];
                    const funcArgs = result.substring(startPos, endPos - 1);
                    const fullMatch = result.substring(match.index, endPos + 1 + num.length);
                    const replacement = `var(${funcName}(${funcArgs}), [${num}, ${num}])`;
                    result = result.substring(0, match.index) + replacement + result.substring(endPos + 1 + num.length);
                    // Réinitialiser la recherche
                    funcPattern.lastIndex = match.index + replacement.length;
                }
            }
        }

        return result;
    },

    // Convertir la syntaxe ?<number> en PRand(0, <number>) ou PWhite(0, <number>)
    // Ou nombre1?nombre2 en PRand(nombre1, nombre2) ou PWhite(nombre1, nombre2)
    convertQuestionMarkToPRand(code) {
        // Remplacer nombre1?nombre2 ou ?nombre par PRand/PWhite selon si c'est int ou float
        return code.replace(/([\d.]+)?\?([\d.]+)/g, (match, num1, num2) => {
            const firstNum = num1 || '0';
            // Vérifier si c'est un float (l'un des deux nombres contient un point)
            if (firstNum.includes('.') || num2.includes('.')) {
                return `PWhite(${firstNum}, ${num2})`;
            } else {
                return `PFr(${firstNum}, ${num2})`;
            }
        });
    },


};

export let playersList = [];

export function updatePlayersList(newPlayersList) {
    playersList = newPlayersList;
}

export function toggleRecording(wsServer, record, folder=null) {
  if (record)
      wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: (folder) ? `Server.record("${folder}")\n` : 'Server.record()\n'
      }));
  else {
      wsServer.send(JSON.stringify({
          type: 'evaluate_code',
          code: 'Server.stopRecording()\n'
      }));
  }
}

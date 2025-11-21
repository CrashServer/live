/**
 * MIDI Mapping Module
 * Gère les mappings entre les CC MIDI et les valeurs dans le code
 */

class MIDIMapping {
  constructor() {
    // Structure : { ccNumber: { line, ch, originalValue, currentValue } }
    this.mappings = {};
    this.editor = null;
    this.midiController = null;
    this.onChangeCallback = null;
    this.evaluationThrottle = {}; // Pour limiter les évaluations
    this.updateThrottle = {}; // Pour limiter les mises à jour du texte
    this.throttleDelay = 50; // ms entre chaque évaluation
    this.updateDelay = 16; // ms entre chaque mise à jour de texte (~60fps)
  }

  /**
   * Initialise le module avec l'éditeur et le contrôleur MIDI
   */
  init(editor, midiController) {
    this.editor = editor;
    this.midiController = midiController;

    // Écouter les changements de valeurs CC
    this.midiController.onCCChange((cc, value) => {
      this.updateMappedValue(cc, value);
    });
  }

  /**
   * Définit le callback appelé quand une valeur mappée change
   */
  onChange(callback) {
    this.onChangeCallback = callback;
  }

  /**
   * Détecte le nombre sous le curseur ou à proximité
   * Retourne { value, start, end } ou null
   */
  detectNumberAtCursor() {
    const cursor = this.editor.getCursor();
    const line = this.editor.getLine(cursor.line);
    const ch = cursor.ch;

    // Regex pour détecter les nombres avec ou sans ancien mapping (entiers ou décimaux, suivis optionnellement de *0.XX)
    const numberWithMappingRegex = /(\d+\.?\d*)(\*\d+\.\d+)?/g;
    let match;
    
    while ((match = numberWithMappingRegex.exec(line)) !== null) {
      const fullMatch = match[0];
      const baseNumber = match[1];
      const mappingPart = match[2] || '';
      
      const start = match.index;
      const end = start + fullMatch.length;
      
      // Le curseur est-il dans ou juste après le nombre ?
      if (ch >= start && ch <= end) {
        return {
          value: parseFloat(baseNumber),
          start: { line: cursor.line, ch: start },
          end: { line: cursor.line, ch: start + baseNumber.length },
          fullEnd: { line: cursor.line, ch: end }, // Position incluant l'ancien mapping
          hadMapping: mappingPart !== ''
        };
      }
    }

    return null;
  }

  /**
   * Vérifie si un nombre a déjà un mapping MIDI
   * Retourne le CC number ou null
   */
  findExistingMapping(line, ch) {
    for (const [ccNum, mapping] of Object.entries(this.mappings)) {
      if (mapping.line === line && ch >= mapping.chStart && ch <= mapping.chEnd) {
        return parseInt(ccNum);
      }
    }
    return null;
  }

  /**
   * Ajoute ou retire un mapping MIDI
   */
  toggleMapping(ccNumber) {
    if (!this.editor || !this.midiController) {
      console.error('MIDIMapping non initialisé');
      return false;
    }

    const cursor = this.editor.getCursor();
    
    // Vérifier si ce CC est déjà mappé quelque part
    if (this.mappings[ccNumber]) {
      // Retirer le mapping existant
      this.removeMapping(ccNumber);
      return false;
    }

    // Détecter le nombre sous le curseur
    const numberInfo = this.detectNumberAtCursor();
    if (!numberInfo) {
      console.warn('⚠️  Aucun nombre détecté sous le curseur');
      return false;
    }

    // Récupérer la valeur actuelle du CC
    const ccValue = this.midiController.getCCValue(ccNumber);
    // Si le CC n'a jamais été touché (valeur = 0), utiliser 0.5 par défaut
    const defaultValue = ccValue === 0 ? 0.5 : ccValue;
    const roundedValue = Math.round(defaultValue * 100) / 100;
    
    // Construire la nouvelle valeur avec multiplication
    const newText = `${numberInfo.value}*${roundedValue.toFixed(2)}`;
    
    // Si un ancien mapping existe, le supprimer d'abord
    const endPosition = numberInfo.hadMapping ? numberInfo.fullEnd : numberInfo.end;
    
    // Remplacer dans l'éditeur
    this.editor.replaceRange(
      newText,
      numberInfo.start,
      endPosition
    );

    // Stocker le mapping
    this.mappings[ccNumber] = {
      line: numberInfo.start.line,
      chStart: numberInfo.start.ch,
      chEnd: numberInfo.start.ch + newText.length,
      originalValue: numberInfo.value,
      currentCCValue: roundedValue
    };
    
    // Évaluer le code après le mapping
    if (this.onChangeCallback) {
      this.onChangeCallback(numberInfo.start.line);
    }

    return true;
  }

  /**
   * Retire un mapping et restaure la valeur originale
   */
  removeMapping(ccNumber) {
    const mapping = this.mappings[ccNumber];
    if (!mapping) return;

    // Restaurer la valeur originale
    const line = mapping.line;
    const lineText = this.editor.getLine(line);
    
    // Trouver le pattern "originalValue*X.XXX"
    const pattern = new RegExp(`${mapping.originalValue}\\*\\d+\\.\\d+`);
    const newLineText = lineText.replace(pattern, mapping.originalValue.toString());
    
    this.editor.replaceRange(
      newLineText,
      { line: line, ch: 0 },
      { line: line, ch: lineText.length }
    );

    delete this.mappings[ccNumber];

    // Évaluer le code après suppression
    if (this.onChangeCallback) {
      this.onChangeCallback(line);
    }
  }

  /**
   * Met à jour une valeur mappée quand le CC MIDI change
   */
  updateMappedValue(ccNumber, ccValue) {
    const mapping = this.mappings[ccNumber];
    if (!mapping) return;

    // Vérifier que la ligne existe toujours
    if (mapping.line >= this.editor.lineCount()) {
      delete this.mappings[ccNumber];
      return;
    }

    // Arrondir à 2 décimales pour réduire les updates
    const roundedValue = Math.round(ccValue * 100) / 100;
    
    // Ne rien faire si la valeur n'a pas changé (avec 2 décimales)
    if (mapping.currentCCValue !== undefined && 
        Math.round(mapping.currentCCValue * 100) === Math.round(roundedValue * 100)) {
      return;
    }

    // Throttle les mises à jour du texte
    if (this.updateThrottle[ccNumber]) {
      clearTimeout(this.updateThrottle[ccNumber]);
    }

    this.updateThrottle[ccNumber] = setTimeout(() => {
      delete this.updateThrottle[ccNumber];
      
      const line = mapping.line;
      const lineText = this.editor.getLine(line);
      
      // Chercher le pattern "originalValue*X.XX" et le remplacer
      const oldPattern = new RegExp(`${mapping.originalValue}\\*\\d+\\.\\d+`);
      const newValue = `${mapping.originalValue}*${roundedValue.toFixed(2)}`;
      const newLineText = lineText.replace(oldPattern, newValue);

      if (newLineText !== lineText) {
        // Sauvegarder la position du curseur
        const cursor = this.editor.getCursor();
        
        // Utiliser une opération atomique pour éviter les conflits
        this.editor.operation(() => {
          // Remplacer la ligne
          this.editor.replaceRange(
            newLineText,
            { line: line, ch: 0 },
            { line: line, ch: lineText.length }
          );

          // Restaurer le curseur (si on était sur une autre ligne)
          if (cursor.line !== line) {
            this.editor.setCursor(cursor);
          }
        });

        // Mettre à jour le mapping
        mapping.currentCCValue = roundedValue;
        mapping.chEnd = mapping.chStart + newValue.length;

        // Évaluer le code avec throttle
        this.throttledEvaluate(ccNumber, line);
      }
    }, this.updateDelay);
  }

  /**
   * Évalue le code avec throttle pour éviter trop d'évaluations
   */
  throttledEvaluate(ccNumber, line) {
    // Annuler le timer précédent s'il existe
    if (this.evaluationThrottle[ccNumber]) {
      clearTimeout(this.evaluationThrottle[ccNumber]);
    }
    
    // Créer un nouveau timer
    this.evaluationThrottle[ccNumber] = setTimeout(() => {
      if (this.onChangeCallback) {
        this.onChangeCallback(line);
      }
      delete this.evaluationThrottle[ccNumber];
    }, this.throttleDelay);
  }

  /**
   * Récupère tous les mappings actifs sur une ligne
   */
  getMappingsOnLine(lineNumber) {
    const result = [];
    for (const [ccNum, mapping] of Object.entries(this.mappings)) {
      if (mapping.line === lineNumber) {
        result.push({
          ccNumber: parseInt(ccNum),
          ...mapping
        });
      }
    }
    return result;
  }

  /**
   * Nettoie tous les mappings
   */
  clearAllMappings() {
    Object.keys(this.mappings).forEach(ccNum => {
      this.removeMapping(parseInt(ccNum));
    });
    console.log('🎛️  Tous les mappings MIDI ont été retirés');
  }

  /**
   * Récupère tous les mappings actifs
   */
  getAllMappings() {
    return { ...this.mappings };
  }
}

export const midiMapping = new MIDIMapping();

/**
 * MIDI Controller Module
 * Gère la connexion et la réception des messages MIDI CC via Web MIDI API
 */

class MIDIController {
  constructor() {
    this.midiAccess = null;
    this.ccValues = {}; // Stockage des valeurs CC normalisées (0.0 - 1.0)
    this.listeners = []; // Callbacks pour les changements de valeurs CC
    this.isSupported = false;
    this.connected = false;
  }

  /**
   * Initialise la connexion MIDI
   */
  async init() {
    // Vérifier le support de Web MIDI API
    if (!navigator.requestMIDIAccess) {
      console.warn('Web MIDI API non supportée par ce navigateur');
      return false;
    }

    this.isSupported = true;

    try {
      // Demander l'accès MIDI
      this.midiAccess = await navigator.requestMIDIAccess();
      console.log('✅ Accès MIDI accordé');

      // Lister les périphériques disponibles
      this.listDevices();

      // Écouter les messages MIDI de tous les inputs
      this.setupInputListeners();

      // Écouter les changements de périphériques (branchement/débranchement)
      this.midiAccess.onstatechange = (e) => {
        console.log(`Périphérique MIDI ${e.port.state}: ${e.port.name}`);
        if (e.port.state === 'connected' && e.port.type === 'input') {
          this.setupInputListener(e.port);
        }
      };

      this.connected = true;
      return true;
    } catch (error) {
      console.error('❌ Erreur lors de l\'initialisation MIDI:', error);
      return false;
    }
  }

  /**
   * Liste tous les périphériques MIDI disponibles
   */
  listDevices() {
    console.log('\n📋 Périphériques MIDI disponibles:');
    
    // Inputs
    const inputs = Array.from(this.midiAccess.inputs.values());
    if (inputs.length === 0) {
      console.log('  ⚠️  Aucun périphérique d\'entrée MIDI détecté');
    } else {
      console.log('  🎹 Entrées MIDI:');
      inputs.forEach((input, index) => {
        console.log(`    ${index + 1}. ${input.name} (${input.manufacturer})`);
      });
    }

    // Outputs
    const outputs = Array.from(this.midiAccess.outputs.values());
    if (outputs.length > 0) {
      console.log('  🔊 Sorties MIDI:');
      outputs.forEach((output, index) => {
        console.log(`    ${index + 1}. ${output.name} (${output.manufacturer})`);
      });
    }

    console.log('');
  }

  /**
   * Configure l'écoute des messages MIDI pour tous les inputs
   */
  setupInputListeners() {
    for (const input of this.midiAccess.inputs.values()) {
      this.setupInputListener(input);
    }
  }

  /**
   * Configure l'écoute des messages MIDI pour un input spécifique
   */
  setupInputListener(input) {
    input.onmidimessage = (message) => {
      this.handleMIDIMessage(message);
    };
    console.log(`🎧 Écoute des messages MIDI sur: ${input.name}`);
  }

  /**
   * Traite les messages MIDI reçus
   */
  handleMIDIMessage(message) {
    const [status, cc, value] = message.data;
    
    // 0xB0-0xBF = Control Change (CC) sur les canaux 1-16
    if ((status & 0xF0) === 0xB0) {
      const normalizedValue = value / 127.0; // Normaliser 0-127 vers 0.0-1.0
      
      // Stocker la valeur
      this.ccValues[cc] = normalizedValue;

      // Notifier les listeners
      this.notifyListeners(cc, normalizedValue);
    }
  }

  /**
   * Enregistre un callback pour les changements de valeurs CC
   */
  onCCChange(callback) {
    this.listeners.push(callback);
  }

  /**
   * Notifie tous les listeners d'un changement de valeur CC
   */
  notifyListeners(cc, value) {
    this.listeners.forEach(listener => {
      try {
        listener(cc, value);
      } catch (error) {
        console.error('Erreur dans un listener MIDI:', error);
      }
    });
  }

  /**
   * Récupère la valeur actuelle d'un CC spécifique
   */
  getCCValue(cc) {
    return this.ccValues[cc] || 0.0;
  }

  /**
   * Récupère toutes les valeurs CC actuelles
   */
  getAllCCValues() {
    return { ...this.ccValues };
  }

  /**
   * Vérifie si le MIDI est supporté et connecté
   */
  isReady() {
    return this.isSupported && this.connected;
  }
}

// Export du module
export const midiController = new MIDIController();

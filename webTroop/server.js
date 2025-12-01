import { WebSocketServer, WebSocket } from 'ws';
import { spawn } from 'child_process';
import path from 'path';
import { promises as fs } from 'fs';
import { SerialPort } from 'serialport';

// Fonction pour charger le fichier de configuration
async function loadConfig(){
  try {
    const configPath = path.resolve('./crash_config.json');
    const configFile = await fs.readFile(configPath, 'utf-8');
    return JSON.parse(configFile);
    // return config
  } catch(error) {
    throw new Error("Erreur dans la récupération du fichier de config", error.message)
  }
}

// Fonction pour initialiser la connexion série Arduino
async function initArduino() {
  try {
    // Lister les ports série disponibles
    const ports = await SerialPort.list();
    
    // Chercher l'Arduino (souvent /dev/ttyUSB* ou /dev/ttyACM* sur Linux)
    let arduinoPort = ports.find(port => 
      port.path.includes('ttyUSB') || 
      port.path.includes('ttyACM') || 
      port.manufacturer?.includes('Arduino') ||
      port.manufacturer?.includes('Arduino')
    );
    
    if (!arduinoPort) {
      console.log('Arduino non trouvé automatiquement. Essai avec /dev/ttyUSB0...');
      arduinoPort = { path: '/dev/ttyUSB0' };
    }
        
    const arduino = new SerialPort({
      path: arduinoPort.path,
      baudRate: 115200,
      autoOpen: false
    });
    
    return new Promise((resolve, reject) => {
      arduino.open((err) => {
        if (err) {
          console.error('Erreur de connexion Arduino:', err.message);
          resolve(null); // Continuer sans Arduino
        } else {
          console.log('Arduino connecté avec succès!');
          resolve(arduino);
        }
      });
    });
    
  } catch (error) {
    console.error('Erreur lors de l\'initialisation Arduino:', error.message);
    return null;
  }
}

// Variables pour le cooldown Arduino
let lastArduinoSend = 0;
const ARDUINO_COOLDOWN = 300; // 300ms de cooldown entre les envois
let arduino = null;

// Fonction pour envoyer un caractère à l'Arduino avec cooldown simple
function sendToArduino(arduino, character) {
  const now = Date.now();
  
  // Vérifier le cooldown - ignorer si trop récent
  if (now - lastArduinoSend < ARDUINO_COOLDOWN) {
    return;
  }
  
  if (arduino && arduino.isOpen) {
    arduino.write(character, (err) => {
      if (err) {
        console.error('Erreur envoi Arduino:', err.message);
      } else {
        
        // Flush pour s'assurer que les données sont envoyées immédiatement
        arduino.flush((flushErr) => {
          if (flushErr) {
            console.error('Erreur flush Arduino:', flushErr.message);
          }
        });
      }
    });
    
    // Mettre à jour le timestamp du dernier envoi
    lastArduinoSend = now;
  } 
}

// Fonction pour mapper les userNames aux caractères
function getUserCharacter(userName) {
  if (!userName) return null;
  
  const userMap = {
    'zbdm': 'v',
    'svdk': 'z',
    'server': 's'
  };
  
  return userMap[userName] || null;
}

// Fonction pour mapper le pourcentage CPU aux caractères Arduino
function getCpuCharacter(cpuPercent) {
  if (cpuPercent < 15) return 'a';      // 0-20%
  else if (cpuPercent < 25) return 'b'; // 20-40%
  else if (cpuPercent < 42) return 'c'; // 40-60%
  else if (cpuPercent < 60) return 'd'; // 60-80%
  else if (cpuPercent < 80) return 'e'; // 80-100%
  else return 'f';                       // 100%+
}

// Variables pour le CPU tracking
let lastCpuLevel = -1;
let lastCpuSend = 0;
const CPU_COOLDOWN = 1000; // 1 seconde entre les mises à jour CPU

// Variables pour la gestion du bouton Arduino
let buttonBuffer = '';
let serverState = false; // État actuel du serveur FoxDot
let lastButtonAction = 0;
const BUTTON_COOLDOWN = 2000; // 2 secondes entre les actions du bouton

// Fonction pour envoyer l'état CPU à l'Arduino
function sendCpuToArduino(arduino, cpuPercent) {
  const now = Date.now();
  const cpuChar = getCpuCharacter(cpuPercent);
  
  // Ne pas envoyer si même niveau ou si cooldown actif
  if (cpuChar === lastCpuLevel || now - lastCpuSend < CPU_COOLDOWN) {
    return;
  }
  
  if (arduino && arduino.isOpen) {
    arduino.write(cpuChar, (err) => {
      if (err) {
        console.error('Erreur envoi CPU Arduino:', err.message);
      } else {
        
        arduino.flush((flushErr) => {
          if (flushErr) {
            console.error('Erreur flush CPU Arduino:', flushErr.message);
          }
        });
      }
    });
    
    lastCpuLevel = cpuChar;
    lastCpuSend = now;
  }
}

// Fonction pour gérer les commandes du bouton Arduino
function handleButtonCommand(command, foxdot) {
  const now = Date.now();
  
  // Vérifier le cooldown pour éviter les activations multiples
  if (now - lastButtonAction < BUTTON_COOLDOWN) {
    console.log(`Bouton ignoré (cooldown actif: ${BUTTON_COOLDOWN - (now - lastButtonAction)}ms restantes)`);
    return;
  }
  
  if (command === 'activate' && !serverState) {
    console.log('🟢 Activation du serveur FoxDot via bouton Arduino');
    foxdot.stdin.write('activateServer()' + '\n' + '\n');
    serverState = true;
    lastButtonAction = now;
  } else if (command === 'deactivate' && serverState) {
    console.log('🔴 Désactivation du serveur FoxDot via bouton Arduino');
    foxdot.stdin.write('soff()' + '\n' + '\n');
    serverState = false;
    lastButtonAction = now;
  } else {
    console.log(`Commande bouton '${command}' ignorée (état serveur: ${serverState ? 'activé' : 'désactivé'})`);
  }
}

// Fonction pour traiter les données série de l'Arduino
function processArduinoData(data, foxdot) {
  const chars = data.toString();
  
  for (let char of chars) {
    // Filtrer seulement les caractères 's' et 'c' du bouton
    if (char === 's' || char === 'c') {
      buttonBuffer += char;
      
      // Détecter la séquence d'activation (10 's' consécutifs)
      if (buttonBuffer.endsWith('ssssssssss')) { // 10 's'
        console.log('🔘 Séquence d\'activation détectée du bouton Arduino');
        handleButtonCommand('activate', foxdot);
        buttonBuffer = ''; // Reset buffer
      }
      // Détecter la séquence de désactivation (10 'c' consécutifs)
      else if (buttonBuffer.endsWith('cccccccccc')) { // 10 'c'
        console.log('🔘 Séquence de désactivation détectée du bouton Arduino');
        handleButtonCommand('deactivate', foxdot);
        buttonBuffer = ''; // Reset buffer
      }
      
      // Limiter la taille du buffer pour éviter l'accumulation
      if (buttonBuffer.length > 20) {
        buttonBuffer = buttonBuffer.slice(-10); // Garder les 10 derniers caractères
      }
    }
    // Ignorer les autres caractères (users codes, etc.)
  }
}

// Les données CPU sont maintenant reçues via les messages WebSocket du crashPanel

(async () => {
  const config = await loadConfig();
  const PROJECT_ROOT = path.resolve(config.FOXDOT_PATH, '..');
  const isArduinoEnabled = config.ARDUINO;
  
  // Initialiser la connexion Arduino
  if (isArduinoEnabled){
    arduino = await initArduino();
  } else {
    arduino = null;
    console.log('Arduino désactivé dans la configuration.');
  }
  
  // Lancer FoxDot
  const foxdot = spawn('python', ['-m', 'FoxDot', '-p'], {
    cwd: config.FOXDOT_PATH,
    env: {...process.env, PYTHONUNBUFFERED: '1'}
  });

console.log('FoxDot démarré', foxdot.pid);

// Écouter les données série de l'Arduino pour les commandes du bouton
if (arduino && arduino.isOpen) {
  arduino.on('data', (data) => {
    processArduinoData(data, foxdot);
  });
  
  arduino.on('error', (err) => {
    console.error('Erreur série Arduino:', err.message);
  });
  
  console.log('Écoute des commandes bouton Arduino activée');
}

// Créer serveur WebSocket
const wss = new WebSocketServer({ port: 1234 });

wss.on('connection', (ws, req) => {
  console.log('Nouveau client connecté');
  // Gérer les messages pour FoxDot
  ws.on('message', async (message) => {
    try {
      const data = JSON.parse(message.toString());
      if (data.type === 'evaluate_code') {
        const {code, userName, userColor} = data;
        
        const attackRequest = (code.trim().startsWith('lost') || code.trim().startsWith("attack") || code.trim().startsWith('chaos')) ? userName : "";
        broadcastLog(`${(userName!=undefined) ? userName : ""}: ${code}\n`, userColor, attackRequest);
        foxdot.stdin.write(data.code + '\n' + '\n');
      } else if (data.type === 'cpu_data' && arduino && arduino.isOpen) {
        // Recevoir les données CPU du crashPanel et les envoyer à l'Arduino
        const {cpu} = data;
        if (typeof cpu === 'number' ) {
          sendCpuToArduino(arduino, cpu);
        }
      } else if (data.type === 'save_file') {
        console.log('Sauvegarde du fichier:', data.filename);
        const {filename, content} = data;
        const filePath = path.join(PROJECT_ROOT, 'codeBank', filename);
        await fs.mkdir(path.dirname(filePath), { recursive: true });
        await fs.writeFile(filePath, content, 'utf-8');
        broadcastLog(`Fichier sauvegardé: ${filename}\n`, 'green');
      }
    } catch (e) {
      // Ignorer les messages non-JSON (messages Y.js)
    }
  });
  ws.on('close', () => {
    console.log('Client déconnecté');
  });
});

// Logs FoxDot
foxdot.stdout.on('data', (data) => {
  try {
    const logMessage = data.toString();
    broadcastLog(logMessage);
  } catch (e) {
    console.error('Erreur lors de l\'envoi des logs:', e);
  }
});

// Logs de console de FoxDot
function broadcastLog(message, color=null, attackRequest="") {
  
  // Nettoyer le message (enlever les sauts de ligne, espaces inutiles)
  const cleanMessage = message.trim();
  
  // Regex plus flexible pour capturer différents formats
  const userLogMatch = cleanMessage.match(/(SERVER|zbdm|svdk)\s*:\s*(.+)/);
  
  if (userLogMatch) {
    const userName = userLogMatch[1];
    
    // Envoyer le caractère correspondant à l'Arduino
    const userChar = getUserCharacter(userName.toLowerCase());
    if (userChar && arduino && arduino.isOpen) {
      sendToArduino(arduino, userChar);
    }
  }
  
  const messageObj = {
    type: 'foxdot_log',
    data: message,
    color: color,
    attackRequestName: attackRequest
  };

  wss.clients.forEach(client => {
    if (client.readyState === 1) {
      client.send(JSON.stringify(messageObj));
    }
  });
}

console.log('Serveur démarré sur le port 1234');
})();

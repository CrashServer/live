import { WebSocketServer } from 'ws';
import { spawn } from 'child_process';
// import fetch from 'node-fetch';
import path from 'path';
import { promises as fs } from 'fs';
import { SerialPort } from 'serialport';

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

// Fonction pour envoyer un caractère à l'Arduino avec cooldown simple
function sendToArduino(arduino, character) {
  const now = Date.now();
  
  // Vérifier le cooldown - ignorer si trop récent
  if (now - lastArduinoSend < ARDUINO_COOLDOWN) {
    // console.log(`Caractère '${character}' ignoré (cooldown actif: ${ARDUINO_COOLDOWN - (now - lastArduinoSend)}ms restantes)`);
    return;
  }
  
  if (arduino && arduino.isOpen) {
    arduino.write(character, (err) => {
      if (err) {
        console.error('Erreur envoi Arduino:', err.message);
      } else {
        // console.log(`Caractère '${character}' envoyé à l'Arduino`);
        
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
  } else {
    console.log('Arduino non connecté, impossible d\'envoyer:', character);
  }
}

// Fonction pour mapper les userNames aux caractères
function getUserCharacter(userName) {
  if (!userName) return null;
  
  const userMap = {
    'zbdm': 'z',
    'svdk': 'v', 
    'server': 's'
  };
  
  // Normaliser en minuscules pour gérer les variations de casse
  return userMap[userName] || null;
}

(async () => {
  const config = await loadConfig();
  const PROJECT_ROOT = path.resolve(config.FOXDOT_PATH, '..');
  
  // Initialiser la connexion Arduino
  const arduino = await initArduino();
  
  // Lancer FoxDot
  const foxdot = spawn('python', ['-m', 'FoxDot', '-p'], {
    cwd: config.FOXDOT_PATH,
    env: {...process.env, PYTHONUNBUFFERED: '1'}
  });

console.log('FoxDot démarré', foxdot.pid);

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
    if (userChar) {
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
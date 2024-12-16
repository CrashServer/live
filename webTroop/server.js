import { WebSocketServer } from 'ws';
import { spawn } from 'child_process';
import { CONFIG} from './config.js';

// Lancer FoxDot
const foxdot = spawn('python', ['-m', 'FoxDot', '-p'], {
  cwd: CONFIG.FOXDOT_PATH,
  env: {...process.env, PYTHONUNBUFFERED: '1'}
});

console.log('FoxDot démarré', foxdot.pid);

// Créer serveur WebSocket
const wss = new WebSocketServer({ port: 1234 });

wss.on('connection', (ws, req) => {
  console.log('Nouveau client connecté');
  // Gérer les messages pour FoxDot
  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message.toString());
      // console.log('Message reçu:', data);
      if (data.type === 'evaluate_code') {
        broadcastLog(`>> ${data.code}\n`);
        foxdot.stdin.write(data.code + '\n' + '\n');
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
    // console.log('Log:', logMessage);
    broadcastLog(logMessage);
  } catch (e) {
    console.error('Erreur lors de l\'envoi des logs:', e);
  }
});

// Logs de console de FoxDot
function broadcastLog(message) {
  const messageObj = {
    type: 'foxdot_log',
    data: message
  };

  wss.clients.forEach(client => {
    if (client.readyState === 1) {
      // console.log('Envoi de log à un client', messageObj);
      client.send(JSON.stringify(messageObj));
    }
  });
}

console.log('Serveur démarré sur le port 1234');
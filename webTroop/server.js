import { WebSocketServer } from 'ws';
import { spawn } from 'child_process';

// Lancer FoxDot
const foxdot = spawn('python', ['-m', 'FoxDot', '-p'], {
  cwd: '/home/zbdm/CrashServer/live/FoxDot'
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

      if (data.type === 'evaluate_code') {
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
    const messageObj = {
      type: 'foxdot_log',
      data: logMessage
    };

    console.log(logMessage);
    // Envoyer les logs à tous les clients connectés
    wss.clients.forEach(client => {
        if (client.readyState === 1) {
            client.send(JSON.stringify(messageObj));
        }
    });
  } catch (e) {
    console.error('Erreur lors de l\'envoi des logs:', e);
  }
});

console.log('Serveur démarré sur le port 1234');
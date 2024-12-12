import { WebSocketServer, WebSocket } from 'ws';
import { spawn } from 'child_process';
import { setupWSConnection } from 'y-websocket/bin/utils';
// import * as Y from 'yjs';

// const doc = new Y.Doc();
// const ytext = doc.getText('codemirror');

// Lancer FoxDot
const foxdot = spawn('python', ['-m', 'FoxDot', '-p'], {
  cwd: '/home/zbdm/CrashServer/live/FoxDot'
});

// Créer serveur WebSocket
const wss = new WebSocketServer({ port: 1234 });
const connections = new Set();

wss.on('connection', (ws, req) => {
  setupWSConnection(ws, req);
  
  connections.add(ws);
  console.log('Nouveau client connecté, total:', connections.size);
  
  // Gérer la connexion Y.js

  ws.on('close', () => {
    // Retirer la connexion fermée
    connections.delete(ws);
    console.log('Client déconnecté, total:', connections.size);
  });

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
});

// Logs FoxDot
foxdot.stdout.on('data', (data) => {
  try { 
    const logMessage = data.toString();
    const messageObj = {
      type: 'foxdot_log',
      data: logMessage
    };
    const messageStr = JSON.stringify(messageObj);
    // Envoyer les logs à tous les clients connectés
    wss.clients.forEach(client => {
        if (client.readyState === 1) {
            client.send(messageStr);
        }
    });
  } catch (e) {
    console.error('Erreur lors de l\'envoi des logs:', e);
  }
});

wss.on('connection', (ws, req) => {
  console.log('Nouveau client connecté');
  
  ws.on('close', () => {
    console.log('Client déconnecté');
  });
});

console.log('Serveur démarré sur le port 1234');
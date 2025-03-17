import { WebSocketServer } from 'ws';
import { spawn } from 'child_process';
import fetch from 'node-fetch';
import path from 'path';
import { promises as fs } from 'fs';

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

(async () => {
  const config = await loadConfig();
  const PROJECT_ROOT = path.resolve(config.FOXDOT_PATH, '..');
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
        // console.log('Code évalué:', (code.trim().startsWith('lost') || code.trim().startsWith("attack")) ? 'attack' : "pas attack");
        const attackRequest = (code.trim().startsWith('lost') || code.trim().startsWith("attack")) ? userName : "";
        broadcastLog(`>> ${(userName!=undefined) ? userName : ""}: ${code}\n`, userColor, attackRequest);
        foxdot.stdin.write(data.code + '\n' + '\n');
      } else if (data.type === 'save_file') {
        console.log('Sauvegarde du fichier:', data.filename);
        const {filename, content} = data;
        const filePath = path.join(PROJECT_ROOT, 'codeBank', filename);
        await fs.mkdir(path.dirname(filePath), { recursive: true });
        await fs.writeFile(filePath, content, 'utf-8');
        broadcastLog(`Fichier sauvegardé: ${filename}\n`, 'green');
        // console.log(`File saved: ${filePath}`);
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
    // console.log(logMessage);
    broadcastLog(logMessage);
  } catch (e) {
    console.error('Erreur lors de l\'envoi des logs:', e);
  }
});

// Logs de console de FoxDot
function broadcastLog(message, color=null, attackRequest="") {
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
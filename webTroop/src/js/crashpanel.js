import { EventEmitter } from './eventBus.js';
import { playersList, updatePlayersList } from './functionUtils.js';

const configRequest = await fetch('../../crash_config.json' );
  if (!configRequest.ok) {
    throw new Error(`HTTP error! status: ${configRequest.status}`);
  }
const config = await configRequest.json();

// Toggle Crash Panel
const crashPanel = document.getElementById('crashPanel')
const crashPanelToggle = document.getElementById('crashPanelToggle');
const crashPanelTitle = document.getElementById('crashPanelTitle');

crashPanelToggle.addEventListener('change', () => {
  if (crashPanelToggle.checked) {
    crashPanel.style.display = 'block';
  }
  else {
    crashPanel.style.display = 'none';
  }
})

const ws = new WebSocket(`ws://${config.HOST_IP}:20000`);

ws.onopen = function() {
    console.log('CrashPanel WebSocket connection opened');
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    
    switch(data.type) {
        case 'scale':
            document.getElementById('scale').textContent = data.scale;
            break;
        case 'root':
            document.getElementById('root').textContent = data.root;
            break;
        case 'cpu':
            updateCpu(data.cpu);
            break;
        case 'bpm':
            document.getElementById('bpm').textContent = data.bpm;
            break;
        case 'serverState':
            updateCrashPanelTitle(data.serverState);
            break;
        case 'beat':
            updateBeat(data.beat);
            break;
        case 'chrono':
            document.getElementById('chrono').textContent = formatTime(data.chrono);
            break;
        case 'players':
            formatPlayers(data.players)
            break;
        case 'pdj':
            const pdjContainer = document.getElementById('pdj')
            pdjContainer.textContent = data.intitule + " - " + data.plat;
            pdjContainer.style.height = pdjContainer.scrollHeight + 'px';
            break;
        case 'help':
            const helpContainer = document.getElementById('help')
            helpContainer.textContent = data.help;
            helpContainer.style.height = helpContainer.scrollHeight + 'px';
            break;
        default:
            break;    
            // console.log('Unknown message type:', data.type);
    }
};

ws.onclose = function() {
    console.log('WebSocket Crashpanel connection closed');
};

ws.onerror = function(error) {
    console.error('WebSocket CrashPanel error:', error);
};

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60).toString().padStart(2, '0');
    const remainingSeconds = Math.floor(seconds % 60).toString().padStart(2, '0');
    return `${minutes}:${remainingSeconds}`;
}

function updateBeat(actualbeat) {
    const beatInterval = [8,16,32,64]
    beatInterval.forEach(beatInter => {
        const beat = Math.ceil(actualbeat % beatInter);
        const beatDiv = document.getElementById(`beat-${beatInter}`)
        const progressPercent = (beat / beatInter) * 100
        beatDiv.style.background = `linear-gradient(to right, var(--beat-col-2) ${progressPercent}%, var(--beat-col-1) ${progressPercent}%)`;
        beatDiv.textContent = `${beat}/${beatInter}`;

    });
}

function updateCpu(usagePercent){
    const cpuDiv = document.getElementById("cpu")
    const cpuSection = document.querySelector(".cpu-info > fieldset")
    // Définir les couleurs de la plage
    const green = "#515b54";
    const orange = "#FFAA44";
    const redWarm = "#FF5544";
    const redBright = "#FF0000"

    let borderColor;

    // Interpolation basée sur les plages
    if (usagePercent <= 30) {
        // Entre vert et orange
        borderColor = interpolateColor(green, orange, usagePercent / 30);
    } else if (usagePercent <= 50) {
        // Entre orange et rouge
        borderColor = interpolateColor(orange, redWarm, (usagePercent - 30) / 20);
    } else {
        // Au-delà de 50%, rouge fixe
        borderColor = interpolateColor(redWarm, redBright, (usagePercent - 50) / 50);
    }

    // Mettre à jour la bordure et le texte
    // cpuSection.style.borderColor = borderColor;
    document.documentElement.style.setProperty('--border-col-2', borderColor);
    cpuDiv.textContent = `${usagePercent}%`;
}

function interpolateColor(color1, color2, factor) {
    const c1 = parseInt(color1.slice(1), 16);
    const c2 = parseInt(color2.slice(1), 16);
  
    const r1 = (c1 >> 16) & 0xff, g1 = (c1 >> 8) & 0xff, b1 = c1 & 0xff;
    const r2 = (c2 >> 16) & 0xff, g2 = (c2 >> 8) & 0xff, b2 = c2 & 0xff;
  
    const r = Math.round(r1 + factor * (r2 - r1));
    const g = Math.round(g1 + factor * (g2 - g1));
    const b = Math.round(b1 + factor * (b2 - b1));
  
    return `#${(r << 16 | g << 8 | b).toString(16).padStart(6, '0')}`;
  }

function formatPlayers(message) {
    const players = message.map(ply => {
    const { player: id, name: synth, duration: duration } = JSON.parse(ply);

    const durationColor = getDurationColor(duration);

    return {
    id,
    synth,
    duration,
    durationColor
    };
    }).filter(p => p !== null);

    updatePlayersList(players.map(p => p.id));

    // Créer le HTML formaté
    const playersDiv = document.getElementById('players');
    playersDiv.innerHTML = players.map(p => `
        <div class="player-line" data-player-id="${p.id}">
            <span class="player-id">${p.id}</span>
            <span class="player-synth">${p.synth}</span>
            <span class="player-duration" style="color: ${p.durationColor}">${p.duration}</span>
        </div>
    `).join('');

    document.querySelectorAll('.player-line').forEach(line => {
        line.addEventListener('click', (e) => {
            const playerId = e.currentTarget.dataset.playerId;
            EventEmitter.emit('send_foxdot', `${playerId}.stop()`);
        });
        line.style.cursor = 'pointer';
    });
}

function getDurationColor(duration) {
    // Convertir "MM:SS" en minutes
    const [minutes, seconds] = duration.split(':').map(Number);
    const totalMinutes = minutes + seconds/60;
    
    // Définir les seuils et couleurs
    const green = '#4caf50';
    const orange = '#ff9800';
    const red = '#f44336';
    
    // Calculer la couleur
    if (totalMinutes <= 1) {
        return green;
    } else if (totalMinutes <= 5) {
        // Interpoler entre 1-5 minutes
        const factor = (totalMinutes - 1) / 4; // 4 = (5-1)
        return interpolateColor(green, red, factor);
    }
    return red;
}

function updateCrashPanelTitle (serverState) {
    if (serverState) {
      crashPanelTitle.textContent = 'Server Activated';
      crashPanelTitle.classList.add('server-active');
    } else {
        crashPanelTitle.textContent = 'CrashPanel';
        crashPanelTitle.classList.remove('server-active');
    }
  };
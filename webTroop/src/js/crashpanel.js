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

let isResizing = false;
let startX;
let startWidth;
// let sceneName = "";
// let sceneIntervalId = null;

crashPanel.addEventListener('mousedown', function(e) {
    const rect = crashPanel.getBoundingClientRect();
    if (e.clientX > rect.right - 10 && e.clientX < rect.right) {
        isResizing = true;
        startX = e.clientX;
        startWidth = rect.width;
    }
});

document.addEventListener('mousemove', function(e) {
    if (!isResizing) return;
    const width = startWidth + (e.clientX - startX);
    crashPanel.style.width = `${width}px`;
});

document.addEventListener('mouseup', function() {
    isResizing = false;
});

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
            updatePianoKeys(data.scale, document.getElementById('root').textContent);
            break;
        case 'root':
            document.getElementById('root').textContent = data.root;
            updatePianoKeys(document.getElementById('scale').textContent, data.root);
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
        // case 'pdj':
        //     const pdjContainer = document.getElementById('pdj')
        //     pdjContainer.textContent = data.intitule + " - " + data.plat;
        //     pdjContainer.style.height = pdjContainer.scrollHeight + 'px';
        //     break;
        case 'help':
            const helpContainer = document.getElementById('help')
            helpContainer.textContent = data.help;
            helpContainer.style.height = helpContainer.scrollHeight + 'px';
            break;
        // case 'nameScene':
        //     formatSceneName(data.nameScene);
        //     break;
        // case 'gameData':
        //     createGameTable(data.gameData);
        //     break;
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

document.getElementById('root').addEventListener('click', () => {
    const pianoRoll = document.getElementById('piano-roll');
    pianoRoll.classList.toggle('hidden');
});


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
    const { player: id, name: synth, duration: duration, solo: solo } = JSON.parse(ply);

    // Convertir "MM:SS" en minutes
    const [minutes, seconds] = duration.split(':').map(Number);
    const totalMinutes = minutes + seconds/60;
    const durationColor = getDurationColor(totalMinutes);
    // console.log(solo);
    // const isSolo = (solo == "True") ? "soloed" : "";

    return {
    id,
    synth,
    duration,
    durationColor,
    solo
    };
    }).filter(p => p !== null);

    updatePlayersList(players.map(p => p.id));

    // Vérifier si un ou plusieurs joueurs ont `solo` à `true`
    const hasSolo = players.some(p => p.solo);

    // Créer le HTML formaté
    const playersDiv = document.getElementById('players');
    playersDiv.innerHTML = players.map(p => `
        <div class="player-line ${hasSolo && !p.solo ? 'player-solo' : ''}" data-player-id="${p.id}">
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
    });
}

// Déterminer la couleur en fonction de la durée
function getDurationColor(totalMinutes) {
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

// Update the title of the crash panel
function updateCrashPanelTitle (serverState) {
    if (serverState) {
      crashPanelTitle.textContent = 'Server Activated';
      crashPanelTitle.classList.add('server-active');
    } else {
        crashPanelTitle.textContent = 'CrashPanel';
        crashPanelTitle.classList.remove('server-active');
    }
  };

const checkboxes = document.querySelectorAll('.todo-checkbox');
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {        
        // Vérifier si toutes les checkboxes sont cochées
        checkAllTodos();
    });
  });

resetTodos();

function resetTodos() {
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    })
}

document.querySelector("#todoTitle").addEventListener('click', ()=> {
    checkboxes.forEach(checkbox => {
        checkbox.checked = true;
    } )
    checkAllTodos();
})

function checkAllTodos() {
    const todoSection = document.querySelector('.todo-list');
    const checkboxes = document.querySelectorAll('.todo-checkbox');
    const allChecked = Array.from(checkboxes).every(checkbox => checkbox.checked);

    if (allChecked && checkboxes.length > 0) {
        todoSection.style.display = 'none';
    } else {
        todoSection.style.display = 'block';
    }
}



// function formatSceneName(nameScene) {
//     if (nameScene !== sceneName) {
//         sceneName = nameScene;
//         document.getElementById('sceneName').textContent = nameScene;
//         if (sceneIntervalId !== null) {
//             clearInterval(sceneIntervalId);
//         }

//         let startTime = Date.now();
//         sceneIntervalId = setInterval(() => {
//             const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
//             const color = getDurationColor(elapsedTime/60);
//             const sceneTimeDiv = document.getElementById('sceneTime');
//             sceneTimeDiv.style.color = color;
//             sceneTimeDiv.textContent = formatTime(elapsedTime);
//         }, 1000);
//     }
// }

// Create a table to represent the game data  
// function createGameTable(gameData){
//     const gameDataContainer = document.getElementById('gameData')
//     gameDataContainer.innerHTML = ''; // Clear previous content

//     const table = document.createElement('table');
//     table.style.borderCollapse = 'collapse';
//     table.style.width = '100%';

//     gameData.forEach(row => {
//         const tr = document.createElement('tr');
//         row.forEach(cell => {
//             const td = document.createElement('td');
//             td.textContent = cell;
//             td.style.border = '1px solid black';
//             td.style.padding = '10px';
//             td.style.textAlign = 'center';
//             tr.appendChild(td);
//         });
//         table.appendChild(tr);
//     });
//     gameDataContainer.appendChild(table);
// }

// piano stuff
const scales = {
    chromatic: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    major: [0, 2, 4, 5, 7, 9, 11],
    majorPentatonic: [0, 2, 4, 7, 9],
    minor: [0, 2, 3, 5, 7, 8, 10],
    aeolian: [0, 2, 3, 5, 7, 8, 10],
    minorPentatonic: [0, 3, 5, 7, 10],
    mixolydian: [0, 2, 4, 5, 7, 9, 10],
    melodicMinor: [0, 2, 3, 5, 7, 9, 11],
    melodicMajor: [0, 2, 4, 5, 7, 8, 11],
    harmonicMinor: [0, 2, 3, 5, 7, 8, 11],
    harmonicMajor: [0, 2, 4, 5, 7, 8, 11],
    justMajor: [0, 2, 4, 5, 7, 9, 11],
    justMinor: [0, 2, 3, 5, 7, 8, 10],
    dorian: [0, 2, 3, 5, 7, 9, 10],
    dorian2: [0, 1, 3, 5, 6, 8, 9, 11],
    diminished: [0, 1, 3, 4, 6, 7, 9, 10],
    egyptian: [0, 2, 5, 7, 10],
    yu: [0, 3, 5, 7, 10],
    zhi: [0, 2, 5, 7, 9],
    phrygian: [0, 1, 3, 5, 7, 8, 10],
    prometheus: [0, 2, 4, 6, 11],
    indian: [0, 4, 5, 7, 10],
    locrian: [0, 1, 3, 5, 6, 8, 10],
    locrianMajor: [0, 2, 4, 5, 6, 8, 10],
    lydian: [0, 2, 4, 6, 7, 9, 11],
    lydianMinor: [0, 2, 4, 6, 7, 8, 10],
    custom: [0, 2, 3, 5, 6, 9, 10],
    hungarianMinor: [0, 2, 3, 6, 7, 8, 11],
    romanianMinor: [0, 2, 3, 6, 7, 9, 10],
    chinese: [0, 4, 6, 7, 11],
    wholeTone: [0, 2, 4, 6, 8, 10],
    halfWhole: [0, 1, 3, 4, 6, 7, 9, 10],
    wholeHalf: [0, 2, 3, 5, 6, 8, 9, 11],
    bebopMaj: [0, 2, 4, 5, 7, 8, 9, 11],
    bebopDorian: [0, 2, 3, 4, 5, 9, 10],
    bebopDom: [0, 2, 4, 5, 7, 9, 10, 11],
    bebopMelMin: [0, 2, 3, 5, 7, 8, 9, 11],
    blues: [0, 3, 5, 6, 7, 10],
    minMaj: [0, 2, 3, 5, 7, 9, 11],
    susb9: [0, 1, 3, 5, 7, 9, 10],
    lydianAug: [0, 2, 4, 6, 8, 9, 11],
    lydianDom: [0, 2, 4, 6, 7, 9, 10],
    melMin5th: [0, 2, 4, 5, 7, 8, 10],
    halfDim: [0, 2, 3, 5, 6, 8, 10],
    altered: [0, 1, 3, 4, 6, 8, 10]
};

function updatePianoKeys(scale, root) {
    const notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    const scalePattern = scales[scale];
    const rootIndex = parseInt(root, 10);

    // Clear previous notes
    document.querySelectorAll('#piano-roll .piano-key li').forEach(key => {
        key.textContent = '';
    });

    // Update keys with scale notes
    if (!scalePattern) {
        return;
    }
    scalePattern.forEach((interval, index) => {
        const noteIndex = (rootIndex + interval) % 12;
        const note = notes[noteIndex];
        const key = document.querySelector(`#piano-roll .piano-key li[data-note="${note}"]`);
        if (key) {
            key.innerHTML = `${note}<br>${index}`;
            key.dataset.index = index;
        }
    });

}

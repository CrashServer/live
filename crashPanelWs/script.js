const ws = new WebSocket('ws://192.168.1.7:20000');

ws.onopen = function() {
    console.log('WebSocket connection opened');
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    switch(data.type) {
        case 'scale':
            document.getElementById('scale').value = data.scale;
            break;
        case 'root':
            document.getElementById('root').value = data.root;
            break;
        case 'cpu':
            document.getElementById('cpu').textContent = data.cpu;
            break;
        case 'bpm':
            document.getElementById('bpm').value = data.bpm;
            break;
        case 'serverState':
            document.getElementById('serverState').textContent = data.serverState == 1 ? "Actif" : "Inactif";
            break;
        case 'beat':
            updateBeat(data.beat);
            break;
        case 'chrono':
            document.getElementById('chrono').textContent = formatTime(data.chrono);
            break;
        case 'players':
            const playersContainer = document.getElementById('players');
            playersContainer.value = data.players.join('\n');
            // playersContainer.style.height = playersContainer.scrollHeight + 'px';
            break;
        case 'pdj':
            const pdjContainer = document.getElementById('pdj')
            pdjContainer.value = data.intitule + " - " + data.plat;
            pdjContainer.style.height = pdjContainer.scrollHeight + 'px';
            break;
        case 'help':
            const helpContainer = document.getElementById('help')
            helpContainer.value = data.help;
            helpContainer.style.height = helpContainer.scrollHeight + 'px';
            break;
        default:
            break;    
            // console.log('Unknown message type:', data.type);
    }
};

ws.onclose = function() {
    console.log('WebSocket connection closed');
};

ws.onerror = function(error) {
    console.error('WebSocket error:', error);
};

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60).toString().padStart(2, '0');
    const remainingSeconds = Math.floor(seconds % 60).toString().padStart(2, '0');
    return `${minutes}:${remainingSeconds}`;
}

function updateBeat(beat) {
    document.getElementById('beat-8').textContent = `${Math.ceil(beat % 8)}/8`;
    document.getElementById('beat-16').textContent = `${Math.ceil(beat % 16)}/16`;
    document.getElementById('beat-32').textContent = `${Math.ceil(beat % 32)}/32`;
    document.getElementById('beat-64').textContent = `${Math.ceil(beat % 64)}/64`;
}
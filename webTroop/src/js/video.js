/**
 * Video.js — YouTube IFrame API integration for CrashTroop video popup.
 * Connects via its own WebSocket to server.js on port 1234.
 */

let player = null;
let ws = null;
let loopRegion = null;    // { start, end } or null
let loopPollId = null;
let statusIntervalId = null;

// ─── Config ──────────────────────────────────────────────────

async function loadConfig() {
    try {
        const resp = await fetch('../../crash_config.json');
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        return await resp.json();
    } catch (e) {
        console.warn('Video: config load failed, using defaults', e);
        return { HOST_IP: '127.0.0.1' };
    }
}

// ─── YouTube IFrame API ──────────────────────────────────────

function loadYouTubeAPI() {
    return new Promise((resolve) => {
        if (window.YT && window.YT.Player) {
            resolve();
            return;
        }
        const tag = document.createElement('script');
        tag.src = 'https://www.youtube.com/iframe_api';
        document.head.appendChild(tag);
        window.onYouTubeIframeAPIReady = resolve;
    });
}

function createPlayer(videoId) {
    return new Promise((resolve) => {
        if (player) {
            player.loadVideoById(videoId);
            resolve(player);
            return;
        }
        player = new YT.Player('player', {
            videoId: videoId,
            playerVars: {
                autoplay: 1,
                controls: 1,
                modestbranding: 1,
                rel: 0,
            },
            events: {
                onReady: () => resolve(player),
                onStateChange: onPlayerStateChange,
            }
        });
    });
}

function onPlayerStateChange(event) {
    const states = { '-1': 'unstarted', 0: 'ended', 1: 'playing', 2: 'paused', 3: 'buffering', 5: 'cued' };
    setStatus(states[event.data] || 'unknown');
}

// ─── Command handler ─────────────────────────────────────────

function handleCommand(data) {
    switch (data.type) {
        case 'yt_load':
            if (data.videoId) {
                loadYouTubeAPI().then(() => createPlayer(data.videoId));
                setStatus('Loading...');
            }
            break;

        case 'yt_play':
            if (player) player.playVideo();
            break;

        case 'yt_pause':
            if (player) player.pauseVideo();
            break;

        case 'yt_seek':
            if (player && typeof data.position === 'number') {
                player.seekTo(data.position, true);
            }
            break;

        case 'yt_rate':
            if (player && typeof data.rate === 'number') {
                player.setPlaybackRate(data.rate);
                document.getElementById('video-rate').textContent = data.rate + 'x';
            }
            break;

        case 'yt_stutter': {
            if (!player) break;
            const dur = data.duration || 0.25;
            const currentTime = player.getCurrentTime();
            player.seekTo(Math.max(0, currentTime - dur), true);
            break;
        }

        case 'yt_loop':
            if (typeof data.start === 'number' && typeof data.end === 'number') {
                loopRegion = { start: data.start, end: data.end };
                document.getElementById('loop-indicator').classList.remove('hidden');
                startLoopPolling();
            }
            break;

        case 'yt_unloop':
            loopRegion = null;
            document.getElementById('loop-indicator').classList.add('hidden');
            stopLoopPolling();
            break;

        case 'yt_open_window':
            // Already open — if a new videoId is provided, load it
            if (data.videoId) {
                loadYouTubeAPI().then(() => createPlayer(data.videoId));
                setStatus('Loading...');
            }
            break;

        default:
            break;
    }
}

// ─── Loop polling ────────────────────────────────────────────

function startLoopPolling() {
    stopLoopPolling();
    loopPollId = setInterval(() => {
        if (!player || !loopRegion) return;
        const t = player.getCurrentTime();
        if (t >= loopRegion.end || t < loopRegion.start) {
            player.seekTo(loopRegion.start, true);
        }
    }, 50);
}

function stopLoopPolling() {
    if (loopPollId) {
        clearInterval(loopPollId);
        loopPollId = null;
    }
}

// ─── Status display ──────────────────────────────────────────

function setStatus(text) {
    document.getElementById('video-status').textContent = text;
}

function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
}

function startStatusUpdates() {
    statusIntervalId = setInterval(() => {
        if (!player || typeof player.getCurrentTime !== 'function') return;
        try {
            const current = player.getCurrentTime();
            const duration = player.getDuration();
            document.getElementById('video-time').textContent =
                `${formatTime(current)} / ${formatTime(duration)}`;
        } catch (_) {}
    }, 100);
}

// ─── WebSocket connection ────────────────────────────────────

function connectWs(host) {
    ws = new WebSocket(`ws://${host}:1234`);

    ws.onopen = () => {
        setStatus('Connected');
    };

    ws.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            if (data.type && data.type.startsWith('yt_')) {
                handleCommand(data);
            }
        } catch (_) {}
    };

    ws.onclose = () => {
        setStatus('Disconnected');
        // Reconnect after 2 seconds
        setTimeout(() => connectWs(host), 2000);
    };

    ws.onerror = () => {
        ws.close();
    };
}

// ─── Init ────────────────────────────────────────────────────

(async () => {
    const config = await loadConfig();
    connectWs(config.HOST_IP);
    startStatusUpdates();
})();

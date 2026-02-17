/**
 * WebTroop Video Control
 *
 * Detachable YouTube video player controlled via WebSocket.
 * Receives commands from FoxDot/WebTroop to create real-time video effects.
 *
 * Commands supported:
 * - yt_load: Load a YouTube video by URL or ID
 * - yt_seek: Seek to a specific position (seconds)
 * - yt_stutter: Jump back N seconds (for glitch effects)
 * - yt_rate: Set playback rate (0.25 - 2.0)
 * - yt_play: Play the video
 * - yt_pause: Pause the video
 * - yt_loop: Set loop region (start, end in seconds)
 * - yt_clear_loop: Clear loop region
 * - yt_scrub: Scrub position with offset (for LFO-style effects)
 */

// Configuration - loaded from crash_config.json
let config = null;
let ws = null;
let player = null;
let isPlayerReady = false;

// State
let loopRegion = null; // { start: number, end: number } or null
let loopCheckInterval = null;
let stutterBaseTime = null;
let lastStutterTime = 0;


// DOM elements
const urlInput = document.getElementById('youtube-url');
const loadBtn = document.getElementById('load-video');
const syncBtn = document.getElementById('sync-btn');
const alwaysTopBtn = document.getElementById('always-top-btn');
const minimizeHeaderBtn = document.getElementById('minimize-header-btn');
const statusPosition = document.getElementById('status-position');
const statusDuration = document.getElementById('status-duration');
const statusRate = document.getElementById('status-rate');
const statusState = document.getElementById('status-state');
const wsStatus = document.getElementById('ws-status');
const loopIndicator = document.getElementById('loop-indicator');
const loopStartSpan = document.getElementById('loop-start');
const loopEndSpan = document.getElementById('loop-end');
const clearLoopBtn = document.getElementById('clear-loop');
const playerOverlay = document.getElementById('player-overlay');
const overlayText = document.getElementById('overlay-text');
const videoHeader = document.getElementById('video-header');

// ============================================================================
// INITIALIZATION
// ============================================================================

// URL from query params (passed when opening window)
let initialVideoUrl = null;

async function init() {
  try {
    const configRequest = await fetch('/crash_config.json');
    if (!configRequest.ok) {
      throw new Error(`HTTP error! status: ${configRequest.status}`);
    }
    config = await configRequest.json();

    // Check for video URL in query params
    const urlParams = new URLSearchParams(window.location.search);
    initialVideoUrl = urlParams.get('url');

    // Set window title
    document.title = 'WebTroop Video';

    // Connect to WebSocket
    connectWebSocket();

    // Set up UI event listeners
    setupEventListeners();

    // Start position update loop
    startPositionUpdater();

  } catch (error) {
    console.error('Failed to initialize video control:', error);
  }
}

// ============================================================================
// WEBSOCKET CONNECTION
// ============================================================================

function connectWebSocket() {
  const wsUrl = `ws://${config.HOST_IP}:1234`;
  ws = new WebSocket(wsUrl);

  ws.onopen = () => {
    console.log('WebSocket connected');
    wsStatus.textContent = 'WS: OK';
    wsStatus.className = 'ws-connected';
  };

  ws.onclose = () => {
    console.log('WebSocket disconnected');
    wsStatus.textContent = 'WS: --';
    wsStatus.className = 'ws-disconnected';

    // Attempt reconnect after 2 seconds
    setTimeout(connectWebSocket, 2000);
  };

  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
    wsStatus.textContent = 'WS: ERR';
    wsStatus.className = 'ws-error';
  };

  ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      handleCommand(data);
    } catch (e) {
      // Ignore non-JSON messages
    }
  };
}

// ============================================================================
// COMMAND HANDLING
// ============================================================================

function handleCommand(data) {
  if (!data.type || !data.type.startsWith('yt_')) return;

  switch (data.type) {
    case 'yt_load':
      loadVideo(data.url || data.videoId);
      break;

    case 'yt_seek':
      seekTo(data.time);
      break;

    case 'yt_stutter':
      stutter(data.amount || 0.5);
      break;

    case 'yt_rate':
      setPlaybackRate(data.rate || 1.0);
      break;

    case 'yt_play':
      playVideo();
      break;

    case 'yt_pause':
      pauseVideo();
      break;

    case 'yt_loop':
      setLoopRegion(data.start, data.end);
      break;

    case 'yt_clear_loop':
      clearLoopRegion();
      break;

    case 'yt_scrub':
      scrub(data.offset);
      break;

    case 'yt_jump':
      // Jump to position and set as new stutter base
      jumpTo(data.time);
      break;

    default:
      console.log('Unknown video command:', data.type);
  }
}

// ============================================================================
// VIDEO CONTROL FUNCTIONS
// ============================================================================

function loadVideo(urlOrId) {
  if (!urlOrId) return;

  const videoId = extractVideoId(urlOrId);
  if (!videoId) {
    showOverlay('Invalid URL', 2000);
    return;
  }

  if (player && isPlayerReady) {
    player.loadVideoById(videoId);
    showOverlay('Loading...', 1000);
  } else {
    // Store for when player is ready
    urlInput.value = urlOrId;
    showOverlay('Player not ready', 2000);
  }
}

function extractVideoId(urlOrId) {
  // Already a video ID?
  if (/^[a-zA-Z0-9_-]{11}$/.test(urlOrId)) {
    return urlOrId;
  }

  // Try to extract from URL
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})/,
    /youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})/
  ];

  for (const pattern of patterns) {
    const match = urlOrId.match(pattern);
    if (match) return match[1];
  }

  return null;
}

function seekTo(time) {
  if (!player || !isPlayerReady) return;

  const seekTime = Math.max(0, parseFloat(time) || 0);
  player.seekTo(seekTime, true);
  stutterBaseTime = seekTime;
}

function stutter(amount) {
  if (!player || !isPlayerReady) return;

  const currentTime = player.getCurrentTime();
  const newTime = Math.max(0, currentTime - (parseFloat(amount) || 0.5));

  player.seekTo(newTime, true);

  // Visual feedback
  showOverlay(`-${amount}s`, 200);
}

function jumpTo(time) {
  if (!player || !isPlayerReady) return;

  const jumpTime = Math.max(0, parseFloat(time) || 0);
  player.seekTo(jumpTime, true);
  stutterBaseTime = jumpTime;

  showOverlay(formatTime(jumpTime), 500);
}

function scrub(offset) {
  if (!player || !isPlayerReady || stutterBaseTime === null) return;

  // Scrub relative to base time
  const newTime = Math.max(0, stutterBaseTime + (parseFloat(offset) || 0));
  player.seekTo(newTime, true);
}

function setPlaybackRate(rate) {
  if (!player || !isPlayerReady) return;

  // YouTube supports: 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2
  const validRates = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2];
  const clampedRate = Math.max(0.25, Math.min(2, parseFloat(rate) || 1));

  // Find closest valid rate
  const closestRate = validRates.reduce((prev, curr) =>
    Math.abs(curr - clampedRate) < Math.abs(prev - clampedRate) ? curr : prev
  );

  player.setPlaybackRate(closestRate);
  statusRate.textContent = `${closestRate}x`;

  showOverlay(`${closestRate}x`, 500);
}

function playVideo() {
  if (!player || !isPlayerReady) return;
  player.playVideo();
}

function pauseVideo() {
  if (!player || !isPlayerReady) return;
  player.pauseVideo();
}

function setLoopRegion(start, end) {
  if (!player || !isPlayerReady) return;

  const startTime = parseFloat(start) || 0;
  const endTime = parseFloat(end) || player.getDuration();

  if (startTime >= endTime) {
    showOverlay('Invalid loop', 1000);
    return;
  }

  loopRegion = { start: startTime, end: endTime };

  // Show loop indicator
  loopIndicator.classList.remove('hidden');
  loopStartSpan.textContent = formatTime(startTime);
  loopEndSpan.textContent = formatTime(endTime);

  // Start loop check if not running
  if (!loopCheckInterval) {
    loopCheckInterval = setInterval(checkLoopRegion, 50);
  }

  // Seek to start of loop
  player.seekTo(startTime, true);
  stutterBaseTime = startTime;

  showOverlay(`Loop: ${formatTime(startTime)}-${formatTime(endTime)}`, 1500);
}

function clearLoopRegion() {
  loopRegion = null;
  loopIndicator.classList.add('hidden');

  if (loopCheckInterval) {
    clearInterval(loopCheckInterval);
    loopCheckInterval = null;
  }

  showOverlay('Loop cleared', 500);
}

function checkLoopRegion() {
  if (!loopRegion || !player || !isPlayerReady) return;

  const currentTime = player.getCurrentTime();

  if (currentTime >= loopRegion.end) {
    player.seekTo(loopRegion.start, true);
  }
}

// ============================================================================
// YOUTUBE PLAYER SETUP (IFrame API)
// ============================================================================

// This function is called by the YouTube IFrame API when ready
window.onYouTubeIframeAPIReady = function() {
  player = new YT.Player('player', {
    height: '100%',
    width: '100%',
    playerVars: {
      'autoplay': 0,
      'controls': 1,
      'disablekb': 0,
      'enablejsapi': 1,
      'modestbranding': 1,
      'rel': 0,
      'showinfo': 0,
      'origin': window.location.origin
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange,
      'onError': onPlayerError
    }
  });
};

function onPlayerReady(event) {
  console.log('YouTube player ready');
  isPlayerReady = true;
  statusState.textContent = 'Ready';

  // Load video from URL params (priority) or URL input
  if (initialVideoUrl) {
    loadVideo(initialVideoUrl);
    urlInput.value = initialVideoUrl;
  } else {
    const urlValue = urlInput.value.trim();
    if (urlValue) {
      loadVideo(urlValue);
    }
  }
}

function onPlayerStateChange(event) {
  const states = {
    [-1]: 'Unstarted',
    [0]: 'Ended',
    [1]: 'Playing',
    [2]: 'Paused',
    [3]: 'Buffering',
    [5]: 'Cued'
  };

  statusState.textContent = states[event.data] || 'Unknown';

  // Update duration when video starts
  if (event.data === 1 && player) {
    const duration = player.getDuration();
    statusDuration.textContent = formatTime(duration);
  }
}

function onPlayerError(event) {
  const errors = {
    2: 'Invalid video ID',
    5: 'HTML5 error',
    100: 'Video not found',
    101: 'Embedding disabled',
    150: 'Embedding disabled'
  };

  const errorMsg = errors[event.data] || `Error ${event.data}`;
  showOverlay(errorMsg, 3000);
  statusState.textContent = 'Error';
}

// ============================================================================
// UI HELPERS
// ============================================================================

function formatTime(seconds) {
  if (!seconds || isNaN(seconds)) return '00:00.0';

  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  const ms = Math.floor((seconds % 1) * 10);

  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}.${ms}`;
}

function showOverlay(text, duration = 1000) {
  // Disabled - uncomment below to re-enable
  return;
  /*
  overlayText.textContent = text;
  playerOverlay.classList.remove('hidden');

  setTimeout(() => {
    playerOverlay.classList.add('hidden');
  }, duration);
  */
}

function startPositionUpdater() {
  setInterval(() => {
    if (player && isPlayerReady && player.getCurrentTime) {
      try {
        const currentTime = player.getCurrentTime();
        statusPosition.textContent = formatTime(currentTime);
      } catch (e) {
        // Player might not be ready
      }
    }
  }, 100);
}

function setupEventListeners() {
  // Load button
  loadBtn.addEventListener('click', () => {
    const url = urlInput.value.trim();
    if (url) loadVideo(url);
  });

  // Enter key in URL input
  urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      const url = urlInput.value.trim();
      if (url) loadVideo(url);
    }
  });

  // Sync button - sets current position as stutter base
  syncBtn.addEventListener('click', () => {
    if (player && isPlayerReady) {
      stutterBaseTime = player.getCurrentTime();
      showOverlay(`Base: ${formatTime(stutterBaseTime)}`, 1000);
    }
  });

  // Always on top button (limited browser support)
  alwaysTopBtn.addEventListener('click', () => {
    // Try Picture-in-Picture as an alternative
    if (document.pictureInPictureEnabled) {
      const iframe = document.querySelector('#player iframe');
      if (iframe) {
        showOverlay('PiP not available for iframes', 2000);
      }
    } else {
      showOverlay('Pin not supported', 2000);
    }
  });

  // Minimize header
  let headerMinimized = false;
  minimizeHeaderBtn.addEventListener('click', () => {
    headerMinimized = !headerMinimized;
    videoHeader.classList.toggle('minimized', headerMinimized);
    minimizeHeaderBtn.textContent = headerMinimized ? '+' : '_';
  });

  // Clear loop button
  clearLoopBtn.addEventListener('click', clearLoopRegion);

  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    // Ignore if typing in input
    if (e.target === urlInput) return;

    switch (e.key) {
      case ' ':
        e.preventDefault();
        if (player && isPlayerReady) {
          const state = player.getPlayerState();
          if (state === 1) {
            pauseVideo();
          } else {
            playVideo();
          }
        }
        break;

      case 'ArrowLeft':
        e.preventDefault();
        if (player && isPlayerReady) {
          const currentTime = player.getCurrentTime();
          player.seekTo(currentTime - 5, true);
        }
        break;

      case 'ArrowRight':
        e.preventDefault();
        if (player && isPlayerReady) {
          const currentTime = player.getCurrentTime();
          player.seekTo(currentTime + 5, true);
        }
        break;

      case 's':
        // Sync (same as sync button)
        if (player && isPlayerReady) {
          stutterBaseTime = player.getCurrentTime();
          showOverlay(`Base: ${formatTime(stutterBaseTime)}`, 1000);
        }
        break;

      case 'l':
        // Toggle loop visibility
        loopIndicator.classList.toggle('hidden');
        break;

      case 'Escape':
        clearLoopRegion();
        break;
    }
  });
}

// ============================================================================
// START
// ============================================================================

init();

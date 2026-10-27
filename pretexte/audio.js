// Audio input module — getUserMedia + FFT → shared audioState.
//
// Browsers require a user gesture to unlock getUserMedia.
// Call initAudio() from a key/click handler.
// Once active, tickAudio() (from the rAF loop) updates audioState per frame.

const FFT_SIZE       = 2048;      // 1024 freq bins
const SMOOTH_TIME    = 0.5;       // analyser's own smoothing
const OUT_BINS       = 128;       // downsampled spectrum size
const TEMPORAL_SMOOTH = 0.55;     // per-bin temporal smoothing across frames

export const audioState = {
  active: false,
  volume: 0,
  bass:   0,
  mid:    0,
  treble: 0,
  spectrum: new Float32Array(OUT_BINS),  // 0..1 normalized
  // Derived splits (indices into spectrum)
  bassEnd: Math.floor(OUT_BINS * 0.15),
  midEnd:  Math.floor(OUT_BINS * 0.50),
};

let audioCtx = null;
let analyser = null;
let raw = null;        // Uint8Array raw FFT bins (0..255)
let initStarted = false;

export async function initAudio() {
  if (audioState.active || initStarted) return;
  initStarted = true;
  try {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: false,
        noiseSuppression: false,
        autoGainControl:  false,
      },
    });
    const source = audioCtx.createMediaStreamSource(stream);
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = FFT_SIZE;
    analyser.smoothingTimeConstant = SMOOTH_TIME;
    raw = new Uint8Array(analyser.frequencyBinCount);
    source.connect(analyser);
    audioState.active = true;
    console.log(`✓ Audio input active (${analyser.frequencyBinCount} bins)`);
  } catch (err) {
    console.error('✗ Audio init failed:', err);
    initStarted = false;
  }
}

export function tickAudio() {
  if (!audioState.active) return;
  analyser.getByteFrequencyData(raw);

  // Focus on useful range: skip DC and roll off high freqs.
  // The spectrum is logarithmically more interesting at low bins, so we
  // use a non-linear mapping: bin i of OUT_BINS maps to a log-ish
  // position in raw. For now a simple sqrt mapping gives OK distribution.
  const rawLen = raw.length;
  const binsOut = audioState.spectrum;
  for (let i = 0; i < binsOut.length; i++) {
    const t = i / binsOut.length;               // 0..1
    const tShaped = Math.pow(t, 1.6);           // emphasize lows
    const idx = Math.min(rawLen - 1, Math.floor(tShaped * rawLen));
    const v = raw[idx] / 255;
    binsOut[i] = binsOut[i] * TEMPORAL_SMOOTH + v * (1 - TEMPORAL_SMOOTH);
  }

  // Bass/mid/treble/volume from the smoothed spectrum
  let bass = 0, mid = 0, treble = 0, total = 0;
  const { bassEnd, midEnd } = audioState;
  for (let i = 0; i < binsOut.length; i++) {
    const v = binsOut[i];
    total += v;
    if (i < bassEnd)      bass += v;
    else if (i < midEnd)  mid += v;
    else                  treble += v;
  }
  audioState.volume = total / binsOut.length;
  audioState.bass   = bass / bassEnd;
  audioState.mid    = mid / (midEnd - bassEnd);
  audioState.treble = treble / (binsOut.length - midEnd);
}

/** Read spectral energy at a normalized x position (0..1). */
export function energyAtX(x01) {
  if (!audioState.active) return 0;
  const i = Math.max(0, Math.min(audioState.spectrum.length - 1,
                                 Math.floor(x01 * audioState.spectrum.length)));
  return audioState.spectrum[i];
}

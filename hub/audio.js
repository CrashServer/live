/**
 * Audio Analysis — captures system audio via PipeWire, does FFT
 *
 * Spawns pw-record reading the monitor source, pipes raw PCM,
 * analyzes in 1024-sample windows → bass/mid/high/level/onset
 *
 * Usage:
 *   import { startAudio, getAudio } from './audio.js';
 *   startAudio(config);
 *   setInterval(() => { const a = getAudio(); }, 50);
 */

import { spawn } from 'child_process';

const SAMPLE_RATE = 48000;
const CHANNELS = 1;
const BYTES_PER_SAMPLE = 2;  // s16le
const FFT_SIZE = 1024;
const HOP = FFT_SIZE;  // non-overlapping

// Frequency band boundaries (bin indices for 48kHz, 1024 FFT)
// bin = freq * FFT_SIZE / SAMPLE_RATE
const BASS_END = Math.floor(250 * FFT_SIZE / SAMPLE_RATE);    // ~5
const MID_END = Math.floor(4000 * FFT_SIZE / SAMPLE_RATE);    // ~85
// HIGH = everything above MID_END up to Nyquist

let audioState = { level: 0, bass: 0, mid: 0, high: 0, onset: false, spectrum: [] };
let prevEnergy = 0;
let process_ = null;
let buffer = Buffer.alloc(0);

// Simple DFT magnitude for specific bins (no external FFT lib needed)
// We only compute magnitudes for the bands we care about, not full FFT
function analyzePCM(samples) {
  const N = samples.length;
  if (N < FFT_SIZE) return;

  // RMS level
  let sum = 0;
  for (let i = 0; i < N; i++) sum += samples[i] * samples[i];
  const rms = Math.sqrt(sum / N);
  audioState.level = Math.min(1, rms * 3);  // scale to ~0-1

  // Simple band energy via time-domain bandpass approximation
  // Low-pass for bass: running average
  let bassSum = 0, midSum = 0, highSum = 0;

  // Compute magnitude spectrum for key bins using Goertzel
  const halfN = FFT_SIZE / 2;
  const spectrum = new Float32Array(halfN);

  for (let k = 0; k < halfN; k++) {
    // Goertzel algorithm — efficient single-bin DFT
    const w = 2 * Math.PI * k / FFT_SIZE;
    const coeff = 2 * Math.cos(w);
    let s0 = 0, s1 = 0, s2 = 0;
    for (let n = 0; n < FFT_SIZE; n++) {
      s0 = samples[n] + coeff * s1 - s2;
      s2 = s1;
      s1 = s0;
    }
    const mag = Math.sqrt(s1 * s1 + s2 * s2 - coeff * s1 * s2) / FFT_SIZE;
    spectrum[k] = mag;

    if (k <= BASS_END) bassSum += mag;
    else if (k <= MID_END) midSum += mag;
    else highSum += mag;
  }

  // Normalize
  audioState.bass = Math.min(1, bassSum / (BASS_END + 1) * 8);
  audioState.mid = Math.min(1, midSum / (MID_END - BASS_END) * 12);
  audioState.high = Math.min(1, highSum / (halfN - MID_END) * 20);

  // Onset detection — spectral flux
  const energy = bassSum + midSum * 0.5;
  audioState.onset = energy > prevEnergy * 1.5 && energy > 0.01;
  prevEnergy = prevEnergy * 0.9 + energy * 0.1;

  // Downsample spectrum to 32 bins for transmission
  const outBins = 32;
  const binsPerOut = Math.floor(halfN / outBins);
  audioState.spectrum = [];
  for (let i = 0; i < outBins; i++) {
    let s = 0;
    for (let j = 0; j < binsPerOut; j++) s += spectrum[i * binsPerOut + j];
    audioState.spectrum.push(Math.min(1, s / binsPerOut * 10));
  }
}

export function getAudio() {
  return audioState;
}

export function startAudio(config = {}) {
  const source = config.audio_source || 'alsa_output.pci-0000_00_1b.0.analog-stereo.monitor';

  console.log(`[audio] starting capture from ${source}`);

  function launch() {
    // pw-record --target <monitor> --format s16 --rate 48000 --channels 1 -
    process_ = spawn('pw-record', [
      '--target', source,
      '--format', 's16',
      '--rate', String(SAMPLE_RATE),
      '--channels', String(CHANNELS),
      '-',  // stdout
    ], { stdio: ['ignore', 'pipe', 'ignore'] });

    process_.stdout.on('data', (chunk) => {
      buffer = Buffer.concat([buffer, chunk]);

      // Process complete frames
      const frameBytes = FFT_SIZE * BYTES_PER_SAMPLE;
      while (buffer.length >= frameBytes) {
        const frame = buffer.subarray(0, frameBytes);
        buffer = buffer.subarray(frameBytes);

        // Convert s16le to float -1..1
        const samples = new Float32Array(FFT_SIZE);
        for (let i = 0; i < FFT_SIZE; i++) {
          samples[i] = frame.readInt16LE(i * 2) / 32768;
        }
        analyzePCM(samples);
      }
    });

    process_.on('close', (code) => {
      console.log(`[audio] pw-record exited (${code}), restarting...`);
      setTimeout(launch, 2000);
    });

    process_.on('error', (err) => {
      console.log(`[audio] pw-record error: ${err.message}`);
      setTimeout(launch, 5000);
    });
  }

  launch();
}

export function stopAudio() {
  if (process_) {
    process_.kill();
    process_ = null;
  }
}

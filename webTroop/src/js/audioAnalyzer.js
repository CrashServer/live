export class AudioAnalyzer {
  constructor(containerElement) {
    this.container = containerElement;
    this.canvas = null;
    this.canvasCtx = null;
    this.audioContext = null;
    this.analyser = null;
    this.splitter = null;
    this.analyserLeft = null;
    this.analyserRight = null;
    this.dataArrayLeft = null;
    this.dataArrayRight = null;
    this.animationId = null;
    this.smoothedDataLeft = null;
    this.smoothedDataRight = null;
    this.isRunning = false;

    this.minFreq = 20;
    this.maxFreq = 20000;
    this.fftSize = 4096; // Plus de points pour une meilleure résolution
    this.colorLeft = '#FF4444';
    this.colorRight = '#4444FF';
    this.freqLabels = [0, 20, 30, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 20000];
    
    // Optimisations légères
    this.smoothingFactor = 0.7;
    this.lastFrameTime = 0;
    this.targetFrameTime = 1000 / 30; // 60 fps pour plus de réactivité
    this.canvasScale = 0.75;

    this.setupCanvas();
  }

  setupCanvas() {
    this.canvas = document.createElement('canvas');
    this.canvas.width = Math.floor(this.container.clientWidth * this.canvasScale);
    this.canvas.height = Math.floor(this.container.clientHeight * this.canvasScale);
    this.canvas.style.display = 'block';
    this.canvas.style.width = '100%';
    this.canvas.style.height = '100%';
    this.canvas.style.imageRendering = 'pixelated';
    this.container.appendChild(this.canvas);
    this.canvasCtx = this.canvas.getContext('2d', { alpha: false });

    window.addEventListener('resize', () => this.onWindowResize());
  }

  onWindowResize() {
    this.canvas.width = Math.floor(this.container.clientWidth * this.canvasScale);
    this.canvas.height = Math.floor(this.container.clientHeight * this.canvasScale);
  }

  async init() {
    try {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();

      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const source = this.audioContext.createMediaStreamSource(stream);

      this.splitter = this.audioContext.createChannelSplitter(2);
      this.analyserLeft = this.audioContext.createAnalyser();
      this.analyserRight = this.audioContext.createAnalyser();

      this.analyserLeft.fftSize = this.fftSize;
      this.analyserRight.fftSize = this.fftSize;

      this.analyserLeft.smoothingTimeConstant = 0.3;
      this.analyserRight.smoothingTimeConstant = 0.3;
      
      // Buffers de lissage pour réduire les oscillations
      
      source.connect(this.splitter);
      this.splitter.connect(this.analyserLeft, 0);
      this.splitter.connect(this.analyserRight, 1);
      
      this.dataArrayLeft = new Uint8Array(this.analyserLeft.frequencyBinCount);
      this.dataArrayRight = new Uint8Array(this.analyserRight.frequencyBinCount);
      
      this.smoothedDataLeft = new Uint8Array(this.analyserLeft.frequencyBinCount);
      this.smoothedDataRight = new Uint8Array(this.analyserRight.frequencyBinCount);



      this.isRunning = true;
      this.draw();
    } catch (error) {
      console.error('Erreur lors de l\'initialisation de l\'analyseur audio:', error);
    }
  }

  freqToX(freq) {
    const logMin = Math.log10(this.minFreq);
    const logMax = Math.log10(this.maxFreq);
    const logFreq = Math.log10(Math.max(freq, this.minFreq));
    return ((logFreq - logMin) / (logMax - logMin)) * this.canvas.width;
  }

  draw() {
    if (!this.isRunning) return;

    const now = performance.now();
    const deltaTime = now - this.lastFrameTime;

    // Throttle à 30fps pour réduire les appels de rendu
    if (deltaTime >= this.targetFrameTime) {
      this.lastFrameTime = now - (deltaTime % this.targetFrameTime);

      // Clear canvas
      this.canvasCtx.fillStyle = '#0a0a0a';
      this.canvasCtx.fillRect(0, 0, this.canvas.width, this.canvas.height);

      // Dessiner la grille et les labels
      this.drawGrid();

      // Récupérer les données fréquentielles
      this.analyserLeft.getByteFrequencyData(this.dataArrayLeft);
      this.analyserRight.getByteFrequencyData(this.dataArrayRight);

      this.applySmoothingToArray(this.dataArrayLeft, this.smoothedDataLeft);
      this.applySmoothingToArray(this.dataArrayRight, this.smoothedDataRight);

      // Dessiner les spectres avec lissage
      this.drawSpectrum(this.smoothedDataLeft, this.colorLeft);
      this.drawSpectrum(this.smoothedDataRight, this.colorRight);
    }

    this.animationId = requestAnimationFrame(() => this.draw());
  }

  applySmoothingToArray(dataArray, smoothedArray) {
    for (let i = 0; i < dataArray.length; i++) {
      smoothedArray[i] = Math.round(
        dataArray[i] * (1 - this.smoothingFactor) + 
        smoothedArray[i] * this.smoothingFactor
      );
    }
  }

  drawGrid() {
    const height = this.canvas.height;
    const padding = 30;

    this.canvasCtx.strokeStyle = '#333333';
    this.canvasCtx.fillStyle = '#666666';
    this.canvasCtx.font = '10px monospace';
    this.canvasCtx.textAlign = 'center';

    this.freqLabels.forEach((freq) => {
      const x = this.freqToX(freq);
      if (x >= 0 && x <= this.canvas.width) {
        this.canvasCtx.beginPath();
        this.canvasCtx.moveTo(x, padding);
        this.canvasCtx.lineTo(x, height);
        this.canvasCtx.stroke();

        const label = freq >= 1000 ? `${(freq / 1000).toFixed(1)}k` : `${freq}`;
        this.canvasCtx.fillText(label, x, height - 10);
      }
    });
  }

  drawSpectrum(dataArray, color) {
    const height = this.canvas.height;
    const padding = 30;
    const freqBinCount = dataArray.length;
    const nyquist = this.audioContext.sampleRate / 2;
    
    this.canvasCtx.strokeStyle = color;
    this.canvasCtx.lineWidth = 2;
    this.canvasCtx.beginPath();

    let firstPoint = true;

    // Créer plus de points pour l'affichage en interpolant
    const displayPoints = 128; // Plus de points pour une meilleure résolution visuelle
    for (let p = 0; p < displayPoints; p++) {
      // Mapper linéairement entre minFreq et maxFreq (en log)
      const logMin = Math.log10(this.minFreq);
      const logMax = Math.log10(this.maxFreq);
      const logFreq = logMin + (p / displayPoints) * (logMax - logMin);
      const freq = Math.pow(10, logFreq);

      // Trouver le bin correspondant
      const bin = (freq / nyquist) * freqBinCount;
      
      // Interpoler entre deux bins si nécessaire
      const binFloor = Math.floor(bin);
      const binCeil = Math.min(Math.ceil(bin), freqBinCount - 1);
      const binFraction = bin - binFloor;

      let value;
      if (binFloor === binCeil) {
        value = dataArray[binFloor];
      } else {
        // Interpolation linéaire entre deux bins
        value = dataArray[binFloor] * (1 - binFraction) + 
                dataArray[binCeil] * binFraction;
      }

      const x = this.freqToX(freq);
      const y = height - padding - (value / 255) * (height - padding);

      if (firstPoint) {
        this.canvasCtx.moveTo(x, y);
        firstPoint = false;
      } else {
        this.canvasCtx.lineTo(x, y);
      }
    }

    this.canvasCtx.stroke();
  }

  stop() {
    this.isRunning = false;
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
    }
    if (this.audioContext && this.audioContext.state !== 'closed') {
      this.audioContext.close();
    }
  }
}

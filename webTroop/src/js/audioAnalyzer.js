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
    this.fftSize = 4096;
    // this.colorLeft = '#FF4444';
    this.colorLeft = window.getComputedStyle(document.body).getPropertyValue('--col-full-red');
    this.colorRight = window.getComputedStyle(document.body).getPropertyValue('--col-full-blue');
    this.bgColor = window.getComputedStyle(document.body).getPropertyValue('--bg-col-1');
    this.gridColor = window.getComputedStyle(document.body).getPropertyValue('--flash-col');
    // this.colorRight = '#4444FF';
    this.freqLabels = [20, 30, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 20000];

    // Optimisations cohérentes
    this.smoothingFactor = 0.7; // Réduit pour moins d'accumulation
    this.lastFrameTime = 0;
    this.targetFrameTime = 1000 / 15; // 30 fps
    this.canvasScale = 0.75;
    this.displayPoints = 128*2; // Nombre de points à afficher

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
    // Gérer le cas spécial de 0 Hz (positionner à gauche)
    if (freq <= 0) {
      return 0;
    }

    const logMin = Math.log10(this.minFreq);
    const logMax = Math.log10(this.maxFreq);
    const logFreq = Math.log10(Math.max(freq, this.minFreq));
    return ((logFreq - logMin) / (logMax - logMin)) * this.canvas.width;
  }

  draw() {
    if (!this.isRunning) return;

    const now = performance.now();
    const deltaTime = now - this.lastFrameTime;

    if (deltaTime >= this.targetFrameTime) {
      this.lastFrameTime = now - (deltaTime % this.targetFrameTime);

      // Utiliser la couleur du thème pour le fond
      this.canvasCtx.fillStyle = this.bgColor;
      this.canvasCtx.fillRect(0, 0, this.canvas.width, this.canvas.height);

      this.drawGrid();

      this.analyserLeft.getByteFrequencyData(this.dataArrayLeft);
      this.analyserRight.getByteFrequencyData(this.dataArrayRight);

      this.applySmoothingToArray(this.dataArrayLeft, this.smoothedDataLeft);
      this.applySmoothingToArray(this.dataArrayRight, this.smoothedDataRight);

      this.drawSpectrum(this.smoothedDataLeft, this.colorLeft);
      this.drawSpectrum(this.smoothedDataRight, this.colorRight);
    }

    this.animationId = requestAnimationFrame(() => this.draw());
  }

  applySmoothingToArray(dataArray, smoothedArray) {
    for (let i = 0; i < dataArray.length; i++) {
      if (i <= 2) {
        smoothedArray[i] = dataArray[i];
        continue;
      }
      smoothedArray[i] = Math.round(
        dataArray[i] * (1 - this.smoothingFactor) +
        smoothedArray[i] * this.smoothingFactor
      );
    }
  }

  drawGrid() {
    const height = this.canvas.height;
    const padding = 30;

    // Utiliser la couleur du thème pour la grille
    this.canvasCtx.strokeStyle = this.gridColor;
    this.canvasCtx.fillStyle = this.gridColor;
    this.canvasCtx.font = '10px monospace';
    this.canvasCtx.textBaseline = 'top';

    this.freqLabels.forEach((freq) => {
      const x = this.freqToX(freq);
      if (x >= 0 && x <= this.canvas.width) {
        // Ligne verticale
        this.canvasCtx.beginPath();
        this.canvasCtx.moveTo(x, padding);
        this.canvasCtx.lineTo(x, height);
        this.canvasCtx.stroke();

        // Ajuster l'alignement du texte selon la position
        if (x < 15) {
          this.canvasCtx.textAlign = 'left';
        } else if (x > this.canvas.width - 15) {
          this.canvasCtx.textAlign = 'right';
        } else {
          this.canvasCtx.textAlign = 'center';
        }

        const label = freq >= 1000 ? `${(freq / 1000).toFixed(1)}k` : `${freq}`;
        this.canvasCtx.fillText(label, x, height - 8);
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

    // Boucler à travers les points d'affichage, en commençant EXACTEMENT à minFreq
    for (let p = 0; p <= this.displayPoints; p++) {
      const logMin = Math.log10(this.minFreq);
      const logMax = Math.log10(this.maxFreq);
      const logFreq = logMin + (p / this.displayPoints) * (logMax - logMin);
      const freq = Math.pow(10, logFreq);

      const bin = (freq / nyquist) * freqBinCount;
      const binFloor = Math.floor(bin);
      const binCeil = Math.min(Math.ceil(bin), freqBinCount - 1);
      const binFraction = bin - binFloor;

      let value;
      if (binFloor === binCeil) {
        value = dataArray[binFloor];
      } else {
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

let cpuHist
let colUi, colServer, colStandby
let vectorCode = []
let vectorServer = []
let font, txtSize
let padd
let vid
let pg
let maxLineCode
let mic, fft
let vecCodePos, vecCodeSize 
let vecCpuPos, vecCpuSize
let vecVidPos, vecVidSize
let vecServerPos, vecServerSize

let libs = ["/includes/js/socket.io.js"]

function preload() {
	font = loadFont("includes/fonts/press.ttf")
	vecVidSize = createVector(640,480); // video size
	vid = createVideo("includes/video/01.mp4", vidload);
}

function setup() {
	createCanvas(windowWidth, windowHeight)
	setupOsc('127.0.0.1', 20000, 20005) // oscHost, oscPortIn, oscPortOut
	setAttributes('antialias', true);
	bvl = 15 //bevel
	padd = 5 // padding
	maxLineCode = 13; // maximum of code line displayed
	strokeJoin(BEVEL);
	cpuHist=[0,5];
	
	colStandby = color(30,212,115);
	colServer = color(255,0,0);
	colUi = colStandby;
	
	txtSize = 20;
	textSize(txtSize);
	textFont(font);
	
	mic = new p5.AudioIn();
	mic.start();
	fft = new p5.FFT();
	fft.setInput(mic)
	setPositionSize()
}

function draw() {
	background(0)

	drawFft();
	drawPourtour(colUi);
	
	// players Code
	drawWindow(vecCodePos, vecCodeSize, colUi)
	drawCode(vecCodePos, vecCodeSize)

	// Cpu
	drawWindow(vecCpuPos, vecCpuSize, colUi)
	drawCpu(vecCpuPos, vecCpuSize)

	// Video
	drawWindow(vecVidPos, vecVidSize, colUi);
	image(vid, vecVidPos.x +10, vecVidPos.y, vecVidSize.x-10,vecVidSize.y-10)


	// server Code
	drawWindow(vecServerPos, vecServerSize, colUi)
	drawServer(vecServerPos, vecServerSize)
}

function vidload(){
	vid.loop();
	vid.volume(0);
	vid.hide();
	vecVidSize = createVector(640,480); // video size
	vid.play();
}

function setPositionSize(){
	// Code Players
	vecCodePos = createVector(50,50)
	vecCodeSize = createVector((width-vecCodePos.x)/2.5,height-vecCodePos.y-8*padd)

	// Cpu
	vecCpuSize = createVector(200,200)
	vecCpuPos = createVector(width-vecCpuSize.x - 10*padd,vecCodePos.y + vecCodeSize.y - vecCpuSize.y)
	
	// Video
	vid.size(vecVidSize.x,vecVidSize.y);
	vecVidPos = createVector(width-10*padd-vecVidSize.x,50);

	// Server Code
	vecServerPos = createVector(vecCodePos.x*4+vecCodeSize.x, vecVidPos.y + vecVidSize.y + 8*padd)
	vecServerSize = createVector(width - vecServerPos.x - vecCpuSize.x - 32*padd, height-vecServerPos.y - 8*padd)
}

function drawCode(vecPos, vecSize){
	push()
	translate(vecPos)
	stroke(255)
	fill(255)
	let conCode =""
	for (let i=0; i<vectorCode.length; i++){
		conCode += "\n"
		conCode += vectorCode[i]
	}
	drawingContext.shadowBlur=8;
	drawingContext.shadowColor=colUi;
	text(conCode, txtSize, txtSize, vecSize.x-padd,vecSize.y-padd)
	pop()
}

function drawServer(vecPos, vecSize){
	push()
	translate(vecPos)
	stroke(255)
	fill(255)
	let conCode =""
	for (let i=0; i<vectorServer.length; i++){
		conCode += "\n"
		conCode += vectorServer[i]
	}
	drawingContext.shadowBlur=8;
	drawingContext.shadowColor=colUi;
	text(conCode, txtSize, txtSize, vecSize.x-padd,vecSize.y-padd)
	pop()
}

function drawWindow(vecPos, vecSize, col){
	push()
	translate(vecPos.x, vecPos.y)

	noStroke()
	let backCol = color(col.levels)
	backCol.setAlpha(90)
	fill(backCol)

	beginShape() // the background rectangle
		vertex(0,0)
		vertex(0, vecSize.y-bvl)
		
		vertex(0, vecSize.y-bvl)
		vertex(bvl, vecSize.y)
		
		vertex(bvl, vecSize.y)
		vertex(vecSize.x, vecSize.y)
		
		vertex(vecSize.x, vecSize.y)
		vertex(vecSize.x, 0)
		
		vertex(vecSize.x, 0)
		vertex(0,0)
		
	endShape(CLOSE)
	
	strokeWeight(4)
	stroke(col)
	noFill()

	beginShape(LINES) // the L
		vertex(0,0)
		vertex(0, vecSize.y-bvl)
		vertex(0, vecSize.y-bvl)
		vertex(bvl, vecSize.y)
		vertex(bvl, vecSize.y)
		vertex(vecSize.x, vecSize.y)
	endShape()

	beginShape(LINES) // the outside
		vertex(-bvl, vecSize.y - bvl)
		vertex(-bvl, -bvl)
		
		vertex(-bvl, -bvl)
		vertex(vecSize.x , -bvl)
		
		vertex(vecSize.x, -bvl)
		vertex(vecSize.x + bvl, 0)
				
		vertex(vecSize.x + bvl, 0)
		vertex(vecSize.x + bvl, vecSize.y + bvl)
	endShape()
	pop()
	
}

function drawCpu(vecPos, vecSize){
	push()
	fill(255)
	translate(vecPos.x + vecSize.x/2, vecPos.y + vecSize.y/2)
	let maxSize = max(vecSize.x*0.98, vecSize.y*0.98)/2
	
	for (let i=1; i<cpuHist.length;i++){
		let alpha = 360 / cpuHist.length
		stroke(map(cpuHist[i],0,100,0,255), map(cpuHist[i],100,0,0,255), 0, map(i,0,cpuHist.length,0,255))
		line(cos((i-1)*alpha)*map(cpuHist[i-1],0,100,20,maxSize), sin((i-1)*alpha)*map(cpuHist[i-1],0,100,20,maxSize)
			, cos(i*alpha)*map(cpuHist[i],0,100,20,maxSize), sin(i*alpha)*map(cpuHist[i],0,100,20,maxSize))
		
	}
	textAlign(CENTER, CENTER);
	text("CPU: " + cpuHist.slice(-1) + "%",0,0)
	pop()
}

function drawPourtour(col){
	push()

	strokeWeight(4)
	stroke(col)
	translate(0,0)
	beginShape(LINES)
		vertex(bvl+padd, 0+padd) // up
		vertex(width/2 - 100, 0+padd)
		
		vertex(width/2 - 100, 0+padd)
		vertex(width/2 - 100 + bvl*2, bvl*2+padd)
		
		vertex(width/2 - 100 + bvl*2, bvl*2+padd)
		vertex(width/2 + 100 - bvl*2, bvl*2+padd)
		
		vertex(width/2 + 100 - bvl*2, bvl*2+padd)
		vertex(width/2 + 100, 0+padd)
		
		vertex(width/2 + 100, 0+padd)
		vertex(width-bvl-padd, 0+padd)
		
		vertex(width-bvl-padd, 0+padd) // up right bvl
		vertex(width-padd, bvl+padd)
		
		vertex(width-padd, bvl+padd) // right
		vertex(width-padd, height-bvl-padd)
		
		vertex(width-padd, height-bvl-padd) // down right bvl
		vertex(width-bvl-padd, height-padd)
		
		vertex(width-bvl-padd, height-padd) // down
		vertex(bvl+padd, height-padd)
		
		vertex(bvl+padd, height-padd) // down left
		vertex(0+padd, height-bvl-padd)
		
		vertex(0+padd, height-bvl-padd) // left
		vertex(0+padd, bvl+padd)
		
		vertex(0+padd, bvl+padd)
		vertex(bvl+padd, 0+padd)
	endShape()
	textAlign(CENTER, CENTER)
	text("CRASH OS", width/2, padd+txtSize/2)
	
	pop()
}

// OSC
function setupOsc(oscHost, oscPortIn, oscPortOut) {
	socket = io.connect('http://127.0.0.1:8082')
	socket.on('connect', function() {
		socket.emit('config', {
			server: {
				host: oscHost,
				port: oscPortIn
			},
			client: {
				host: oscHost,
				port: oscPortOut
			}
		})
		console.log('OSC Ready!\n' + oscHost + ', listen: ' + oscPortIn)
	})
	socket.on('message', function(msg) {
		receiveOsc(msg[0], msg.splice(1))
	})
}

function receiveOsc(address, value) {
	let codeLine
	if (address == "/serverCode"){
		codeLine = "SERVER: " + String(value[0])
		vectorServer.unshift(codeLine)
		colUi = colServer
	}
	else if (address == "/zbdmCode"){
		codeLine = "ZBDM: " + String(value[0])	
		vectorCode.unshift(codeLine)
		colUi = colStandby
	}
	else if (address == "/svdkCode"){
		codeLine = "SVDK: " + String(value[0])	
		vectorCode.unshift(codeLine)
		colUi = colStandby
	}
	else if (address == "/CPU"){
		cpuHist.push(round(value[0],1))
	}
	
	if (vectorCode.length > maxLineCode){
		vectorCode.pop()
	}
	
	if (vectorServer.length > maxLineCode){
		vectorServer.pop()
	}
}

function drawFft(){
	push();
	translate(width/2, height/2);
	let spectrum = fft.analyze();
	noFill();
	stroke(255);
	
	// circle vertex
	beginShape();
	for (i = 0; i < spectrum.length; i++) {
		let maxSound = map(spectrum[i], 0,255,0, height/2)
		let x = cos(i)*maxSound
		let y = sin(i)*maxSound
		vertex(x,y);
	}
	endShape();
	pop();
}

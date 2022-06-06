#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

	/// bang is triggered by an code in foxDot
	/// bigbang is the destruction of a module (80% 60% 40% 20%) 
	/// superbigbang is a scene change,  reseting all parameters
	/// rules : a mesh in obj has 5 submeshes to be destroyed (not more)
	/// at some point the will be safeguard for errors, not yet 

    settings.loadFile("xml/config.xml");

    width = settings.getValue("config:width", 1920);
    height = settings.getValue("config:height", 1080);
    barduino = settings.getValue("config:arduino", false);

	/// SETUP 
    ofSetFrameRate(30);
    ofSetWindowShape(width, height);
    uiColor = ofColor(0,20,20);
    ofSetBackgroundColor(0);

	/// NETWORK
    data.setup(barduino);
    postCode.begin();
        boot.draw();
    ofBlendMode(OF_BLENDMODE_MULTIPLY);
    postProc.begin();
        boot.draw();
    postProc.end();
    ofBlendMode(OF_BLENDMODE_DISABLED);
    postCode.end();

	/// 3D MODELS
//    postprocSetup();
    render.setup();
    sphereMap.setup();
    text3d.setup();
    procBackground.setup();

//    tunnel3d.setup();

    /// Windows
    winCode.setup(10, uiColor);
    winCpu.setup(10, uiColor);
    winIntegrity.setup(10, uiColor);
    uiMisc.setup();

    boot.setup();

    /// audio video
    webcam.setup(uiColor);
    videoplayer.setup();
    videoplayer3d.setup3d();
    audioFft.setup();
    dmx.setup();

    // Post processing
    postProc.setup(false, true);
    postCode.setup(true, false, true);

    // Glitcher
    glitcherCam.setup(webcam.camFbo);
    glitcherLogo.setup(uiMisc.uiFbo);
    glitcherVideo.setup(videoplayer.videoFbo);

    // GUI
    parameters.add(defaultParam.set("Reset default parameters", false));
    parameters.add(winCode.parameters);
    parameters.add(winCpu.parameters);
    parameters.add(winIntegrity.parameters);
    parameters.add(webcam.parameters);
    parameters.add(integrityIncr.set("Integrity increment", 5, 0, 100));
    parameters.add(cpuStress.set("CPU stress", 1, 0, 100));
    parameters.add(render.parameters);
    parameters.add(procBackground.parameters);
    parameters.add(audioThresh.set("audio Threshold", 1.0, 0.0, 10.0));
    parameters.add(colorPicker.set("Color Ui", uiColor, ofColor(0,0,0), ofColor(255,255,255)));
    parameters.add(scene.set("scene", 0, 0, 7));

    colorPicker.addListener(this, &ofApp::changeColorUi);
    defaultParam.addListener(this, &ofApp::loadDefaultParam);

    gui.setup(parameters, "xml/mysettings.xml");
    gui.setPosition(50,50);
    gui.minimizeAll();
    gui.loadFromFile("xml/mysettings.xml");
    showGui = true;
}

//--------------------------------------------------------------
void ofApp::update(){
	ofSetWindowTitle("CRASH/OS " + (ofToString((int) ofGetFrameRate())));

    data.update();
    bangUpdate(data.bang);
    audioFft.update();

    if ((data.scCPU*cpuStress)>80){scene=3;}

    switch (scene) {
    case 0:
        scene0Update();
        break;

    case 1: // Video player + webcam + windows
        scene1Update();
        break;

    case 2: // videoplayer + webcam + windows + glitcher logo
        scene2Update();
        break;

    case 3: // Video player 3d + windows + webcam
        scene3Update();
        break;

    case 4: // glitch video & webcam  + code
        scene4Update();
        break;

    case 5:
        scene5Update();
        break;

    default:
        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU*cpuStress);
        winIntegrity.update(integrity);

        uiMisc.update(true);
        webcam.update();
        videoplayer.update(5, integrity);
        break;
    }

	if (camShake) {
		cam.setFov(60 + sin(ofGetElapsedTimef()) / ofRandom(0.2, 8));
        cam.rollDeg(ofRandom(-0.05, 0.05));
        cam.panDeg(ofRandom(-0.05, 0.05));
		camShakeTime--;
		if (camShakeTime <= 0) {
			camShake = false;
			camShakeTime = 60;
		}
	}
	else
		cam.setFov(60 + sin(ofGetElapsedTimef()) / 2);
}

//--------------------------------------------------------------
void ofApp::draw(){

	switch (scene) {

    case 0:
        scene0Draw();
        break;

    case 1: // Video player + webcam + windows
        scene1Draw();
        break;

    case 2: // videoplayer + webcam + windows + glitcher logo
        scene2Draw();
        break;

    case 3: // Video player 3d + windows + webcam
        scene3Draw();
        break;

    case 4: // glitch video & webcam & logo + code
        scene4Draw();
        break;

    case 5:
        scene5Draw();
        break;

	default:
        videoplayer.draw();
        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();

        webcam.draw();
        uiMisc.draw(true);
		break;
	}

    overheating.draw();

    if (showGui) {
        ofDisableAlphaBlending();
        ofDisableDepthTest();
        gui.draw();
    }

}


//--------------------------------------------------------------
void ofApp::keyPressed(int key) {

	if (key == 'b') bang('#');
	if (key == 's') bigBang();
	if (key == 'c') superBang();
	if (key == 'f') ofToggleFullscreen();
	if (key == 'g') showGui = !showGui;
}

//--------------------------------------------------------------
void ofApp::exit(){
    dmx.exit();
}


//--------------------------------------------------------------
void ofApp::keyReleased(int key){
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){
}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){
}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){
	
//	fbo.clear();

	width = w;
	height = h;

    winCode.setup(10, uiColor);
    winCpu.setup(10, uiColor);
    winIntegrity.setup(10, uiColor);
    uiMisc.setup();

    /// audio video
    webcam.setup(uiColor);
    videoplayer.resize();

    // Glitcher
    glitcherCam.setup(webcam.camFbo);
    glitcherLogo.setup(uiMisc.uiFbo);
    glitcherVideo.setup(videoplayer.videoFbo);

    boot.resize();
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}

void ofApp::bangUpdate(char playerID)
{
    switch (playerID) {
    case '0':
        // No bang
        break;
    case 'c':
        // Cpu bang receive
        winCpu.noiseCount ++;
        data.bang = '0';
        break;
    case '#':
        // SVDK bang
        bang('#');
        data.bang = '0';
        break;
    case '!':
        // ZBDM bang
        bang('!');
        data.bang = '0';
        break;
    case '@':
        // Server bang
        bang('@');
        data.bang = '0';
        break;
    default:
        break;
    }

}

void ofApp::bang(char playerID){

    camShake = 1;

    if (integrity <= 1 or integrity >= 4000) { // 4000 is for edgecase missed the [0/1] > doesn't generate -inf +inf numbers
        bigBang();
    }

    if (data.scCPU*cpuStress > 80){
        overheating.add();
        }
    else {
        overheating.clear();
    }
    switch (scene) {
    case 0:
        scene0Bang(playerID);
        break;
    case 1:
        scene1Bang(playerID);
        break;
    case 2:
        scene2Bang(playerID);
        break;
    case 3:
        scene3Bang(playerID);
        break;
    case 4:
        scene4Bang(playerID);
        break;

    default:

        break;
    }
}

void ofApp::bigBang()
{    
    switch (scene) {
    case 0:
//        videoplayer.newSeq();
//        if (ofRandom(0,100)>70){superBang();}
        break;
    case 1:
//        videoplayer.newSeq();
//        if (ofRandom(0,100)>70){superBang();}
        break;
    case 2:
//        videoplayer.newSeq();
//        if (ofRandom(0,100)>70){superBang();}
        break;
    case 3:
//        videoplayer.newSeq();
//        if (ofRandom(0,100)>70){superBang();}
        break;
    case 4:
//        if (render.currentModelSubAttack >= 2){
//            render.currentModelSubAttack = 1;}
//        else {render.currentModelSubAttack+=1;}
        render.currentModelSubAttack = ofRandom(0,render.objList.size());
        render.changeModel(render.currentModelSubAttack);
        break;

    default:
//        videoplayer.newSeq();
//        if (ofRandom(0,100)>70){superBang();}
        break;
    }

    integrity = 100 + integrityIncr;
    uiMisc.changeLogo();
}

void ofApp::superBang()
{
    scene = ofRandom(1,3);
}

void ofApp::changeColorUi(ofColor &){
    winCode.uiColor = colorPicker;
    winCpu.uiColor = colorPicker;
    winIntegrity.uiColor = colorPicker;
    webcam.uiColor = colorPicker;
}

void ofApp::loadDefaultParam(bool &){
    gui.loadFromFile("xml/default_settings.xml");
}




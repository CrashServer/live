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
    string textPres = settings.getValue("config:textPres", "");
    glm::vec2 textPresPos = glm::vec2(settings.getValue("config:textPosX", 80), settings.getValue("config:textPosY", 1060));
    int dmxAddr1 = settings.getValue("config:dmxAddr1", 1);
    int dmxAddr2 = settings.getValue("config:dmxAddr2", 8);

	/// SETUP 
    ofSetFrameRate(30);
    ofSetWindowShape(width, height);
    uiColor = ofColor(0,20,20);
    ofSetBackgroundColor(0);

	/// NETWORK
    data.setup(barduino);

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
    uiMisc.setup(textPres, textPresPos);

    boot.setup();

    /// audio video
    webcam.setup(uiColor);
    videoplayer.setup();
    videoplayer3d.setup3d();
    audioFft.setup();
    dmx.setup(dmxAddr1, dmxAddr2);

    // Post processing
    postCode.setup(
        /* Bloom */            true,
        /* pixelate */         false,
        /* Bleach */           false,
        /* shift */            false,
        /* Edge*/              false,
        /* Kali */             false,
        /* Aces */             false,
        /* Noise */            false,
        /* TV */               false,
        /* Glitch */           false,
        /* filmGrain*/         false,
        /* Toon */             false
    );

    // TV GLITCH VIDEO PLAYER
    postTV.setup(
        /* Bloom */            true,
        /* pixelate */         false,
        /* Bleach */           false,
        /* shift */            false,
        /* Edge*/              false,
        /* Kali */             false,
        /* Aces */             true,
        /* Noise */            false,
        /* TV */               true,
        /* Glitch */           false,
        /* filmGrain*/         false,
        /* Toon */             false

    );

    // AUDIO REACTIVE POST-FX KALI
    postKali.setup(
        /* Bloom */            false,
        /* pixelate */         false,
        /* Bleach */           false,
        /* shift */            false,
        /* Edge*/              false,
        /* Kali */             true,
        /* Aces */             false,
        /* Noise */            false,
        /* TV */               false,
        /* Glitch */           false,
        /* filmGrain*/         false,
        /* Toon */             false
    );
    //postKali.gKaleiSegments = 2;
    postKali.kali->setSegments(2);


    // GENERIC FILTER / ACES LUT VIDEO PLAYER
    postProc.setup(
        /* Bloom */            true,
        /* pixelate */         false,
        /* Bleach */           false,
        /* shift */            false,
        /* Edge*/              false,
        /* Kali */             false,
        /* Aces */             true,
        /* Noise */            false,
        /* TV */               false,
        /* Glitch */           false,
        /* filmGrain*/         false,
        /* Toon */             false
    );

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
    parameters.add(scene.set("scene", 0, 0, 10));

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

    // update obligatoire
    data.update();
    bangUpdate(data.bang);
    audioFft.update();

//    if ((data.scCPU*cpuStress)>80){scene=3;}

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

    case 6:
        scene6Update();
        break;

    case 7:
        scene7Update();
        break;

    case 8:
        scene8Update();
        break;

    case 9:
        scene9Update();
        break;

    default:
        sceneDefaultUpdate();
        break;
    }

//	if (camShake) {
//		cam.setFov(60 + sin(ofGetElapsedTimef()) / ofRandom(0.2, 8));
//        cam.rollDeg(ofRandom(-0.05, 0.05));
//        cam.panDeg(ofRandom(-0.05, 0.05));
//		camShakeTime--;
//		if (camShakeTime <= 0) {
//			camShake = false;
//			camShakeTime = 60;
//		}
//	}
//	else
//		cam.setFov(60 + sin(ofGetElapsedTimef()) / 2);
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
    case 6:
        scene6Draw();
        break;
    case 7:
        scene7Draw();
        break;
    case 8:
        scene8Draw();
        break;
    case 9:
        scene9Draw();
        break;

	default:
        sceneDefaultDraw();
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

//    camShake = 1;

    if (integrity <= 1 or integrity >= 4000) { // 4000 is for edgecase missed the [0/1] > doesn't generate -inf +inf numbers
        bigBang();
    }

    // Test overheating
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
    case 5:
        scene5Bang(playerID);
        break;
    case 6:
        scene6Bang(playerID);
        break;
    case 7:
        scene7Bang(playerID);
        break;
    case 8:
        scene8Bang(playerID);
        break;
    case 9:
        scene9Bang(playerID);
        break;

    default:
        sceneDefaultBang(playerID);
        break;
    }
}

void ofApp::bigBang()
{    
    switch (scene) {
    case 0:
        scene0BigBang();
        break;
    case 1:
        scene1BigBang();
        break;
    case 2:
        scene2BigBang();
        break;
    case 3:
        scene3BigBang();
        break;
    case 4:
        scene4BigBang();
        break;
    case 5:
        scene5BigBang();
        break;
    case 6:
        scene6BigBang();
        break;
    case 7:
        scene7BigBang();
        break;
    case 8:
        scene8BigBang();
        break;
    case 9:
        scene9BigBang();
        break;

    default:
        sceneDefaultBigBang();
        break;
    }

//    uiMisc.changeLogo();
    scene = data.scene;
    integrity = 100+integrityIncr;
}

void ofApp::superBang()
{
//    scene = ofRandom(1,3);
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

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

    width = w;
    height = h;

    winCode.resize();
    winCpu.resize();
    winIntegrity.resize();
    uiMisc.resize();

    /// audio video
    //webcam.setup(uiColor);
    videoplayer.resize();

    // Glitcher
    glitcherCam.setup(webcam.camFbo);
    glitcherLogo.setup(uiMisc.uiFbo);
    glitcherVideo.setup(videoplayer.videoFbo);

    boot.resize();
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ }

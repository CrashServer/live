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
    data.update(cpuStress, winCode.maxCodeWidth);
    bangUpdate(data.bang);

    audioFft.update();
//    dmx.update(ofColor(255,0,audioFft.beat.getBand(0)*255), ofColor(0,audioFft.beat.getBand(5)*255,255));

    //changeColorUi();

    if (data.scCPU>80){scene=3;}

    switch (scene) {
    case 0:
        boot.update();
        break;

    case 1: // Video player + webcam + windows
        webcam.update();

        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity);

        uiMisc.update(true);

        videoplayer.update(integrity, false);
        break;

    case 2: // videoplayer + webcam + windows + glitcher logo
        glitcherLogo.update(uiMisc.uiFbo);

        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity);

        uiMisc.update(true);
        webcam.update();

        videoplayer.update(integrity, false);
        break;

    case 3: // Video player 3d + windows + webcam
        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity);

        uiMisc.update(true);
        webcam.update();
//        audioFft.update();

        videoplayer.update(integrity, true, audioFft.beat.getMagnitude()*audioThresh/20);
        break;

    case 4: // glitch video & webcam  + code
        audioFft.update();
        glitcherLogo.update(uiMisc.uiFbo, audioFft.beat.getMagnitude()*audioThresh/20);
        glitcherCam.update(webcam.camFbo, audioFft.beat.getMagnitude()*audioThresh/20);
        glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

        // Windows update
        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity);

        uiMisc.update(true);
        webcam.update();

        videoplayer.update();
        break;

    case 5:
        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity, render.currentText);

//        tunnel3d.update();
        break;

    default:
        winCode.update(data.vectorCode);
        winCpu.update(data.scCPU);
        winIntegrity.update(integrity);

        uiMisc.update(true);
        webcam.update();
        videoplayer.update();
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
        postCode.begin();
            boot.draw();
        ofBlendMode(OF_BLENDMODE_MULTIPLY);
        postProc.begin();
            boot.draw();
        postProc.end();
        ofBlendMode(OF_BLENDMODE_DISABLED);
        postCode.end();

        break;

    case 1: // Video player + webcam + windows

            videoplayer.draw();
//        ofBlendMode(OF_BLENtrueDMODE_MULTIPLY);
//        postProc.begin();
            webcam.draw();
//        postProc.end();
//        ofBlendMode(OF_BLENDMODE_DISABLED);

        postCode.begin();
        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();
        postCode.end();


//        cout << "is active : " << data.isServerActive << endl;
        uiMisc.draw(true, data.isServerActive);

        break;

    case 2: // videoplayer + webcam + windows + glitcher logo
        videoplayer.draw();
        webcam.draw();

        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();

        uiMisc.draw(true, data.isServerActive);

        glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
        break;

    case 3: // Video player 3d + windows + webcam
        videoplayer.draw(true);
        webcam.draw();

        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();

        uiMisc.draw(true, data.isServerActive);
        break;

    case 4: // glitch video & webcam & logo + code
        glitcherVideo.draw(videoplayer.pos, videoplayer.size);

        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();

        webcam.draw();
        uiMisc.draw(false, data.isServerActive);

        glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
        glitcherCam.draw(webcam.pos, webcam.size);

        break;

    case 5:
        cam.begin();
        cam.setDistance(260);
            sphereMap.draw();
            render.draw();
            text3d.draw(render.currentText);
            //tunnel3d.draw();
        cam.end();

        winCode.draw();
        winCpu.draw();
        winIntegrity.draw();
        uiMisc.draw(false, data.isServerActive);

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

    if (data.scCPU > 80){
        overheating.add();
        }
    else {
        overheating.clear();
    }
    switch (scene) {
    case 0:

        videoplayer.videoSrcub();
        integrity -= integrityIncr;
        break;
    case 1:
        if (playerID =='!'){
            ofColor dmx1 = ofColor(0,255,0);
            dmx.update(dmx1, ofColor(0,0,0));
        }
        else if (playerID =='#'){
            ofColor dmx1 = ofColor(0,0,255);
            dmx.update(dmx1, ofColor(0,0,0));
        }
        else if (playerID =='@'){
            ofColor dmx1 = ofColor(255,0,0);
            dmx.update(dmx1, ofColor(0,0,0));
        }
        videoplayer.videoSrcub();
        integrity -= integrityIncr;
        break;
    case 2:
        videoplayer.videoSrcub();
        integrity -= integrityIncr;
        break;
    case 3:
        videoplayer.videoSrcub();
        integrity -= integrityIncr;
        break;
    case 4:
        render.destroyMesh(integrityIncr);
        integrity = (int) render.intergrity;
        break;

    default:
        videoplayer.videoSrcub();
        break;
    }

    //	// based on 4 submeshes
    //	pointLight.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
    //	materialText.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
    //	materialEnv.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
    //	materialEnv.setShininess(120);
    //	materialEnv.setSpecularColor( (ofGetElapsedTimef()*255, ofRandom(255), ofRandom(255)));
}

void ofApp::bigBang()
{
    if (data.scCPU<80){scene=1;}

    switch (scene) {
    case 0:
        videoplayer.newSeq();
        if (ofRandom(0,100)>70){superBang();}
        break;
    case 1:
        videoplayer.newSeq();
        if (ofRandom(0,100)>70){superBang();}
        break;
    case 2:
        videoplayer.newSeq();
        if (ofRandom(0,100)>70){superBang();}
        break;
    case 3:
        videoplayer.newSeq();
        if (ofRandom(0,100)>70){superBang();}
        break;
    case 4:
//        if (render.currentModelSubAttack >= 2){
//            render.currentModelSubAttack = 1;}
//        else {render.currentModelSubAttack+=1;}
        render.currentModelSubAttack = ofRandom(0,render.objList.size());
        render.changeModel(render.currentModelSubAttack);
        break;

    default:
        videoplayer.newSeq();
        if (ofRandom(0,100)>70){superBang();}
        break;
    }

    integrity = 100 + integrityIncr;
    uiMisc.changeLogo();
//  intMeshSlider = ofRandom(0, intMeshSlider.getMax());
//	extMeshSlider = ofRandom(0, extMeshSlider.getMax());
//	midMeshSlider = ofRandom(0, midMeshSlider.getMax());
//	pillarMeshSlider = ofRandom(0, pillarMeshSlider.getMax());
//	pointLight.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
//	materialText.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
//	materialEnv.setDiffuseColor(ofColor(ofRandom(255), ofRandom(255), ofRandom(255)));
//	materialEnv.setShininess(120);
//	materialEnv.setSpecularColor((ofGetElapsedTimef() * 255, ofRandom(255), ofRandom(255)));

	//if (scene = 0) { currentModelSubAttack = currentModelSubAttack++; }
	//else currentModelSubAttack = 0;
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



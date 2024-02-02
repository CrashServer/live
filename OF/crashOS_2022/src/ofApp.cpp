#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

	/// bang is triggered by an code in foxDot
	/// bigbang is the destruction of a module (80% 60% 40% 20%) 
	/// superbigbang is a scene change,  reseting all parameters
	/// rules : a mesh in obj has 5 submeshes to be destroyed (not more)
	/// at some point the will be safeguard for errors, not yet 

    settings.load("xml/config.xml");

    width = settings.getValue("config:width", 1920);
    height = settings.getValue("config:height", 1080);
    bdmx = settings.getValue("config:dmxActive", false);
    int arduinoPort = settings.getValue("config:arduinoPort", 0);
    bvideoFox = settings.getValue("config:videoFox", false);
    string textPres = settings.getValue("config:textPres", "");
    glm::vec2 textPresPos = glm::vec2(settings.getValue("config:textPosX", 80), settings.getValue("config:textPosY", 1060));
    int dmxAddr1 = settings.getValue("config:dmxAddr1", 1);
    int dmxAddr2 = settings.getValue("config:dmxAddr2", 8);
    string troopIp = settings.getValue("config:troopIp", "192.168.0.42");
    int troopPort = settings.getValue("config:troopPort", 2887);
    bserverScene = settings.getValue("config:serverScene", true);

	/// SETUP 
    ofSetFrameRate(30);
    ofSetWindowShape(width, height);
    uiColor = ofColor(0,20,20);
    ofSetBackgroundColor(0);

    /// Player Color
    ofColor zbdmColor=ofColor::paleTurquoise;
    ofColor svdkColor=ofColor::greenYellow;
    ofColor serverColor=ofColor::red;
    playerColor.push_back(zbdmColor);
    playerColor.push_back(svdkColor);
    playerColor.push_back(serverColor);

    /// GAME LOGIC
    integrity = 100;
    zbdmScore = 0;
    svdkScore = 0;
    serverScore = 0;

    /// NETWORK & arduino
    data.setup(troopIp, troopPort, arduinoPort, bvideoFox);

    /// FFT
    initTime = 0;

    /// Windows
    winCode.setup(10, uiColor, playerColor);
    winCpu.setup(10, uiColor);
    winBpm.setup(10, uiColor);
    winIntegrity.setup(10, uiColor);
    uiMisc.setup(textPres, textPresPos);
    winScore.setup(10, uiColor);
    textris.setup(playerColor);

    boot.setup();

    /// audio video
    webcam.setup(uiColor);
    videoplayer.setup();
    //videoplayer3d.setup3d();
    //videoplayerAscii.setupAscii();
    videoplayerHap.setup("videoHap/video/");
    videoplayerHap2.setup("videoHap/video/");
    videoHapServer.setup("videoHap/server/");
    // videoplayerHapInter.setup("videoHap/intervention/");
    audioFft.setup();
    if(bdmx){dmx.setup(dmxAddr1, dmxAddr2);}


    // Glitcher
    glitcherCam.setup(webcam.camFbo);
    glitcherLogo.setup(uiMisc.uiFbo);
    glitcherVideo.setup(videoplayer.videoFbo);

    // GUI
    parameters.add(defaultParam.set("Reset default parameters", false));
    parameters.add(winCode.parameters);
    parameters.add(winCpu.parameters);
    parameters.add(winBpm.parameters);
    parameters.add(winIntegrity.parameters);
    parameters.add(winScore.parameters);
    parameters.add(webcam.parameters);
    parameters.add(integrityIncr.set("Integrity increment", 5, 0, 100));
    parameters.add(cpuStress.set("CPU stress", 1, 0, 100));
    parameters.add(audioThresh.set("audio Threshold", 1.0, 0.0, 10.0));
    parameters.add(colorPicker.set("Color Ui", uiColor, ofColor(0,0,0), ofColor(255,255,255)));
    parameters.add(scene.set("scene", 0, 0, 12));
    parameters.add(bWaitingMsg.set("enableWaitingMessage", false));
    parameters.add(data.parameters);



    colorPicker.addListener(this, &ofApp::changeColorUi);
    defaultParam.addListener(this, &ofApp::loadDefaultParam);
    scene.addListener(this, &ofApp::setScene);
    bWaitingMsg.addListener(this, &ofApp::setWaitingMsg);
    data.button.addListener(this, &ofApp::runTest);

    gui.setup(parameters, "xml/mysettings.xml");
    gui.setPosition(50,50);
    gui.minimizeAll();
    gui.loadFromFile("xml/mysettings.xml");
    showGui = true;

    imageplayer.setup(integrityIncr);

//    vidFbo1.allocate(width, height, GL_RGBA);
//    vidFbo2.allocate(width, height, GL_RGBA);

    // backup infos for serverCorruption
    serverBackup.uiColor = uiColor;
    serverBackup.codePos = winCode.pos;
    serverBackup.cpuPos = winCpu.pos;
    serverBackup.bpmPos = winBpm.pos;
    serverBackup.integrityPos = winIntegrity.pos;
    serverBackup.scorePos = winScore.pos;
    serverBackup.codeSize = winCode.size;
    serverBackup.cpuSize = winCpu.size;
    serverBackup.bpmSize = winBpm.size;
    serverBackup.integritySize = winIntegrity.size;
    serverBackup.scoreSize = winScore.size;
    serverBackup.scene = scene;
    serverBackup.isRestored = false;
}

//--------------------------------------------------------------
void ofApp::update(){
	ofSetWindowTitle("CRASH/OS " + (ofToString((int) ofGetFrameRate())));

    /// test server active for switching scene
    if (data.isServerActive && bserverScene){scene = 404;}
    else if (!data.isServerActive && scene != 404){serverBackup.scene = scene;}

    // update obligatoire
    data.update();
    bangUpdate(data.bang);

    /// audio update
    audioFft.update();
    auto duration = 25.f;
    auto endTime = initTime + duration;
    auto now = ofGetElapsedTimef();
    rms = ofxeasing::map_clamp(now, initTime, endTime, 0,audioFft.beat.getMagnitude()*audioThresh,&ofxeasing::cubic::easeIn);
    kick = ofxeasing::map_clamp(now, initTime, endTime, 0,audioFft.beat.kick()*audioThresh,&ofxeasing::cubic::easeIn);
    snare = ofxeasing::map_clamp(now, initTime, endTime, 0,audioFft.beat.snare()*audioThresh,&ofxeasing::cubic::easeIn);
    hihat = ofxeasing::map_clamp(now, initTime, endTime, 0,audioFft.beat.hihat()*audioThresh,&ofxeasing::cubic::easeIn);

    switch (scene) {
    case 0:
        scene0Update();
        break;
    case 1:
        scene1Update();
        break;
    case 2:
        scene2Update();
        break;
    case 3:
        scene3Update();
        break;
    case 4:
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
    case 10:
        scene10Update();
        break;
    case 11:
        scene11Update();
        break;
    case 12:
        scene12Update();
        break;
//    case 13:
//        scene13Update();
//        break;
//    case 14:
//        scene14Update();
//        break;
//    case 15:
//        scene15Update();
//        break;
//    case 16:
//        scene16Update();
//        break;
    case 404:
        sceneServerUpdate();
        break;

    default:
        sceneDefaultUpdate();
        break;
    }
}

//--------------------------------------------------------------
void ofApp::draw(){

	switch (scene) {

    case 0:
        scene0Draw();
        break;
    case 1:
        scene1Draw();
        break;
    case 2:
        scene2Draw();
        break;
    case 3:
        scene3Draw();
        break;
    case 4:
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
    case 10:
        scene10Draw();
        break;
    case 11:
        scene11Draw();
        break;
    case 12:
        scene12Draw();
        break;
//    case 13:
//        scene13Draw();
//        break;
//    case 14:
//        scene14Draw();
//        break;
//    case 15:
//        scene15Draw();
//        break;
//    case 16:
//        scene16Draw();
//        break;
    case 404:
        sceneServerDraw();
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
    if (key == 's') {data.isServerActive = !data.isServerActive;
                    data.delayServerActivity = 4000;}
	if (key == 'f') ofToggleFullscreen();
	if (key == 'g') showGui = !showGui;
}

//--------------------------------------------------------------
void ofApp::exit(){
    if(bdmx){dmx.exit();}
}


void ofApp::bangUpdate(char playerID)
{
    switch (playerID) {
    case '0':
        // No bang
        break;
    case 'c':
        // Cpu bang receive
        winCpu.noiseCount++;
        data.bang = '0';
        break;
    case '#':
        // SVDK bang
        bang('#');
        winCode.evalSvdk = 255;
        data.bang = '0';
        svdkScore += 1;
        break;
    case '!':
        // ZBDM bang
        bang('!');
        data.bang = '0';
        winCode.evalZbdm = 255;
        zbdmScore += 1;
        break;
    case '@':
        // Server bang
        bang('@');
        data.bang = '0';
        serverScore += 1;
        break;
    default:
        break;
    }
}

void ofApp::bang(char playerID){

//    camShake = 1;

    if (integrity <= 1 or integrity >= 4000) { // 4000 is for edgecase missed the [0/1] > doesn't generate -inf +inf numbers
        bigBang();
        winIntegrity.newText(videoplayerHap.filename);
    }

    // Test overheating
    if (data.scCPU*cpuStress > 80){
        overheating.add();
        }
    else {
        overheating.clear();
    }

    // corruption if server active
    if (data.isServerActive){
        serverCorruptionBang();
    }
    else if (!data.isServerActive && !serverBackup.isRestored){
        serverCorruptionRestore();
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
    case 10:
        scene10Bang(playerID);
        break;
    case 11:
        scene11Bang(playerID);
        break;
    case 12:
        scene12Bang(playerID);
        break;
//    case 13:
//        scene13Bang(playerID);
//        break;
//    case 14:
//        scene14Bang(playerID);
//        break;
//    case 15:
//        scene15Bang(playerID);
//        break;
//    case 16:
//        scene16Bang(playerID);
//        break;
    case 404:
        sceneServerBang(playerID);

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
    case 10:
        scene10BigBang();
        break;
    case 11:
        scene11BigBang();
        break;
    case 12:
        scene12BigBang();
        break;
//    case 13:
//        scene13BigBang();
//        break;
//    case 14:
//        scene14BigBang();
//        break;
//    case 15:
//        scene15BigBang();
//        break;
//    case 16:
//        scene16BigBang();
//        break;
    case 404:
        sceneServerBigBang();

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
    winBpm.uiColor = colorPicker;
    winIntegrity.uiColor = colorPicker;
    webcam.uiColor = colorPicker;
    winScore.uiColor = colorPicker;
}

void ofApp::loadDefaultParam(bool &){
    gui.loadFromFile("xml/default_settings.xml");
}

void ofApp::setScene(int&){
    data.scene = scene;
}

void ofApp::setWaitingMsg(bool&){
    settings.load("xml/config.xml");
    boot.waitingMsg = settings.getValue("waitingMsg" , "");
    boot.bShowMsg = bWaitingMsg;
}

void ofApp::serverCorruptionBang(){
    float speed = 0.001;
//    winCpu.pos = glm::vec3 (ofMap(ofNoise(ofGetFrameNum()*9*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetWidth() - winCpu.size->x),
//                            ofMap(ofNoise(ofGetFrameNum()*7*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetHeight() - winCpu.size->y),0);
//    winCode.pos = glm::vec3 (ofMap(ofNoise(ofGetFrameNum()*8*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetWidth() - winCode.size->x),
//                            ofMap(ofNoise(ofGetFrameNum()*6*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetHeight() - winCode.size->y),0);
//    winIntegrity.pos = glm::vec3 (ofMap(ofNoise(ofGetFrameNum()*9*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetWidth() - winIntegrity.size->x),
//                            ofMap(ofNoise(ofGetFrameNum()*6.5*speed + 150, ofGetElapsedTimef()*speed), 0,1,0,ofGetHeight() - winIntegrity.size->y),0);
//    winScore.pos = glm::vec3 (ofMap(ofNoise(ofGetFrameNum()*7.5*speed, ofGetElapsedTimef()*speed), 0,1,0,ofGetWidth() - winScore.size->x),
//                            ofMap(ofNoise(ofGetFrameNum()*9.9*speed + 100, ofGetElapsedTimef()*speed), 0,1,0,ofGetHeight() - winScore.size->y),0);
//    uiMisc.posAlert = glm::vec3 (ofMap(ofNoise(ofGetFrameNum()*7.5*speed + 1500, ofGetElapsedTimef()*speed + 180), 0,1,0,ofGetWidth() - uiMisc.sizeAlert.x),
//                            ofMap(ofNoise(ofGetFrameNum()*9.9*speed + 9500, ofGetElapsedTimef()*speed + 250), 0,1,0,ofGetHeight() - uiMisc.sizeAlert.y),0);

    winCpu.uiColor = ofColor (ofMap(ofNoise(ofGetFrameNum()), 0,1, 255,serverBackup.uiColor.r, true),
                              serverBackup.uiColor.g, serverBackup.uiColor.b);
    winCode.uiColor = ofColor(ofNoise(ofGetFrameNum()+800)*255,0,0,ofNoise(ofGetFrameNum(), ofGetElapsedTimef()+20)*255);
    winIntegrity.uiColor = ofColor(ofNoise(ofGetFrameNum() + 100)*255,0,0,ofNoise(ofGetFrameNum(), ofGetElapsedTimef()+480)*255);
    winScore.uiColor = ofColor(ofNoise(ofGetFrameNum() + 300)*255,0,0,ofNoise(ofGetFrameNum(), ofGetElapsedTimef()+855)*255);
    winBpm.uiColor = ofColor(ofNoise(ofGetFrameNum() + 300)*255,0,0,ofNoise(ofGetFrameNum(), ofGetElapsedTimef()+855)*255);
    serverBackup.isRestored = false;
}

void ofApp::serverCorruptionRestore(){
        winCode.uiColor = serverBackup.uiColor;
        winCpu.uiColor = serverBackup.uiColor;
        winBpm.uiColor = serverBackup.uiColor;
        winIntegrity.uiColor = serverBackup.uiColor;
        winScore.uiColor = serverBackup.uiColor;
        winCode.pos = serverBackup.codePos;
        winCpu.pos = serverBackup.cpuPos;
        winBpm.pos = serverBackup.bpmPos;
        winIntegrity.pos = serverBackup.integrityPos;
        winScore.pos = serverBackup.scorePos;
        winCode.size = serverBackup.codeSize;
        winCpu.size = serverBackup.cpuSize;
        winBpm.size = serverBackup.bpmSize;
        winIntegrity.size = serverBackup.integritySize;
        winScore.size = serverBackup.scoreSize;
        scene = serverBackup.scene;
        data.scene = serverBackup.scene;
        serverFade = 1;
        serverBackup.isRestored = true;
    }

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

    width = w;
    height = h;

    winCode.resize();
    winCpu.resize();
    winBpm.resize();
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

void ofApp::runTest(){
    /// Arduino
    if (!data.barduino){data.testArduino();}
    else{data.arduinoTest.set("Arduino OK", true);}
    /// CPU
    if (data.scCPU>0.2){data.cpuTest.set("Cpu OK", true);}
    /// BPM
    if (data.bpm>0){data.bpmTest.set("Bpm OK", true);}
    /// DMX
    if ( dmx.dmxInterface_ == 0 || !dmx.opened) {;}
    else {data.dmxTest.set("Dmx OK", true);}
    // Light
    data.serial.writeByte('v'); // send arduino svdk
    data.serial.flush();
    data.serial.writeByte('z'); // send arduino zbdm
    data.serial.flush();
    data.serial.writeByte('s'); // send arduino server
    data.serial.flush();
    // button
    if (data.testButton){data.buttonTest.set("Button OK", true);}
    else {data.buttonTest.set("Button NOT", false);}
    // OSC
    if (data.vectorInstant[0].code.size()>0){
        data.oscTestZbdm.set("OSC ZBDM OK", true);
    }
    else {data.oscTestZbdm.set("OSC ZBDM NOT", false);}
    if (data.vectorInstant[1].code.size()>0){
        data.oscTestSvdk.set("OSC SVDK OK", true);
    }
    else {data.oscTestSvdk.set("OSC SVDK NOT", false);}
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

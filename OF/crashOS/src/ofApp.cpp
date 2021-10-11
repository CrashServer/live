#include "ofApp.h"
#include "Poco/Base64Decoder.h"
//--------------------------------------------------------------
void ofApp::setup(){
    // rendering setup
    ofEnableDepthTest();
    ofDisableAlphaBlending();
    ofSetFrameRate(0);
    ofSetVerticalSync(true);
    ofSetWindowTitle("CRASH/OS");
//    ofEnableSmoothing();
    ofEnableArbTex();
    ofSetBackgroundColor(0);

    // set dimension w * h
    width = 1920;
    height = 1080;
    setting.width  = width;
    setting.height = height;

    // Fx setup
    original.allocate(setting);
    fx.setup(&original, setting);

    post.init(width, height);
    post.createPass<BloomPass>();
    //post.createPass<PixelatePass>();
    //post.createPass<EdgePass>();
    //post.createPass<BleachBypassPass>();

    // interface
    firstCol.set(0,255,0); // green 1st player
    secCol.set(255,127,0); // orange 2nd player
    serverCol.set(255,0,0); // red Server
    fontBackColor.set(150); // font shadow
    firstPlayerAlpha = 255;
    secPlayerAlpha = 255;
    serverAlpha = 255;

    font.load("PressStart2P_Regular.ttf", 16, true, false);
    vagRounded.load("vag.ttf", 32, true, false);
    vagRoundedMini.load("vag.ttf", 16, true, false);

    // Top interface
    icoSphere.setRadius(30);
    icoSphere.setResolution(1);
    topBorder = height*0.1;

    bottomBorder = height * 1/15;

    // init variable
    activeServer = false;
    cpu = 0.0;
    textFirstPlayer = ">> ";
    textSecPlayer = ">> ";
    textServer = ">>";
    nbrOfState = 5;    // Number of State
    videoPlayer.resize(nbrOfState);
    videoCurrent = 1;
    paddingSide = 30; // padding text
    maxTextWidth = (int) (width/2 - paddingSide*2) / (font.getStringBoundingBox("P",0,0).width); // max code text char witdh
    maxLogWidth = (int) (width/2 - paddingSide*2) / (vagRoundedMini.getStringBoundingBox("P",0,0).width); // max code text char witdh

    //XML & video loading
    ofxXmlSettings xmlSettings;
    xmlSettings.loadFile("settings.xml");
    serverName = xmlSettings.getValue("crashos:serverName", "anonymous_server");
    serverBoot = xmlSettings.getValue("crashos:serverBoot", "generic booting");
    bArduinoActive = xmlSettings.getValue("crashos:bArduinoActive", false);
    bDrawActive = xmlSettings.getValue("crashos:bDrawActive", false);
    string txtLog = xmlSettings.getValue("crashos:logText", "******");

    if (bDrawActive){
        for (int i=0; i<nbrOfState; i++){
            string c = ofToString(i);
            stateString.push_back(xmlSettings.getValue("crashos:serverState" + c, "current_" + c + "_state")); // load xml
            videoPlayer[i].load("videos/0" + c + ".mp4"); // load video
            videoPlayer[i].play(); // play video
            videoPlayer[i].setPaused(true);
            }
        videoPlayer[videoCurrent].setPaused(false);

    stringstream s_stream(txtLog);
    while(s_stream.good()){
        string substr;
        getline(s_stream, substr, ',');
        logString.push_back(substr);
            }
    logStringIndex = 0;

    // TEXTURE LOADING
    crashos.load("crashos.jpg");
    alertImage.load("alert.jpg");
        }

    stateColor.push_back(ofColor (255,0,0,180));  // state 0 - RED
    stateColor.push_back(ofColor (69,88,90,180)); // state 1 - POWERBLUE
    stateColor.push_back(ofColor (0,255,0,180)); // state 2 - GREEN
    stateColor.push_back(ofColor (255,170,0,180)); // state 3 - ORANGE
    stateColor.push_back(ofColor (139,0,0,180)); // state 4 - DARKRED


    // gui
    gui.setup();
    showGui = false;
    gui.add(codeFirstPos.set("1st Code box", glm::vec2(paddingSide,(height - (topBorder+bottomBorder))*1/4), glm::vec2(0,0), glm::vec2(width,height)));
    gui.add(codeSecondPos.set("2nd Code Box", glm::vec2(paddingSide,(height - (topBorder+bottomBorder))*2/4), glm::vec2(0,0), glm::vec2(width, height)));
    gui.add(serverPos.set("server Code Box", glm::vec2(paddingSide,(height - (topBorder+bottomBorder))*3/4), glm::vec2(0,0), glm::vec2(width, height)));
    gui.add(cpuPos.set("CPU Box", glm::vec2(width-250,(height-bottomBorder+vagRounded.getAscenderHeight())), glm::vec2(0,0), glm::vec2(width, height)));
    gui.add(stateSlider.setup("State slider", 1, 0, 4));
    gui.add(cpuStress.setup("CPU stress", 100, 0, 100));
    gui.add(bNoise.setup("Noise", false));
    gui.add(bEdge.setup("Edge", false));
    gui.add(bFringe.setup("Fringe", false));
    gui.add(bInvert.setup("Invert", false));
    gui.add(bShift.setup("Shift", false));
    gui.add(bChip.setup("Chip", false));
    gui.add(bVNoise.setup("V - Noise", false));
    gui.add(bSlide.setup("Slide", false));


    // arduino
    if (bArduinoActive){
        // serial.setup("/dev/ttyACM0", 115200);
        serial.setup(0, 115200);
        }

    // OSC & UDP
        oscSc.setup(PORTCPU);
        ofxUDPSettings settings;
        settings.receiveOn(20000);
        settings.blocking = false;
        udpConnection.Setup(settings);
}


//--------------------------------------------------------------
void ofApp::update(){
    // Osc & udp & arduino
    getData();

    if (bDrawActive){
        // fx
        setFx();

        // video
        if (stateSlider != videoCurrent){
            videoPlayer[videoCurrent].setPaused(true);
            videoPlayer[stateSlider].setPaused(false);
            videoCurrent = stateSlider;
        }
        videoPlayer[stateSlider].update();

        if (firstPlayerAlpha>0){firstPlayerAlpha -= 0.4;}
        if (secPlayerAlpha>0){secPlayerAlpha -= 0.4;}
        if (serverAlpha>0){serverAlpha -= 0.4;}
        }
   }


//--------------------------------------------------------------
void ofApp::draw(){
    if (bDrawActive){
        original.begin();
        //ofClear(0, 0, 0, 255);
        ofSetColor(255);
        videoPlayer[stateSlider].draw(0,0,width,height);

        ofSetBackgroundColor(0);
        ofSetColor(stateColor[stateSlider]);

        ofDisableDepthTest();
        ofEnableAlphaBlending();
        drawTop();
        drawCode();
        drawBottom();
        ofDisableAlphaBlending();
        original.end();

        //apply active Effects
        fx.applyFx();

        post.begin();
        //draw applied buffer
        original.draw(0, 0);
        post.end();

        if (activeServer) { alertImage.draw((width/2.25) - 200,0); }
        if (showGui){
            gui.draw();
        }
    }
}

//--------------------------------------------------------------
void ofApp::getData(){
    // Arduino
    if (bArduinoActive){
        if (serial.available()){
            char button = serial.readByte();
            if (button == 's' && !activeServer){
                activeServer = true;
                stateSlider = 0;
                }
            else if (button == 'c' && activeServer){
                activeServer = false;
                stateSlider = (int) ofRandom(1, nbrOfState);
                }
            }
        }

    // Osc CPU
    if(oscSc.hasWaitingMessages()){
        ofxOscMessage mSc;
        oscSc.getNextMessage(mSc);

        if (mSc.getAddress()=="/CPU"){
           cpu = mSc.getArgAsFloat(0);
            }
        }

    // Udp Code player *2 + Code Server
    char udpMessage[500];
    udpConnection.Receive(udpMessage,500);
    string message=udpMessage;
    char *msgType = &message[0];
    if (message!=""){
        if (*msgType == '#'){
            textFirstPlayer = message.erase(0,1);
            textFirstPlayer = insertNewlines(textFirstPlayer, maxTextWidth);
            firstPlayerAlpha = 255;
            if(bArduinoActive){serial.writeByte('g');}
            logStringIndex = (int) ofRandom(0, logString.size()-1);
            }
        else if (*msgType == '!'){
            textSecPlayer = message.erase(0,1);
            textSecPlayer = insertNewlines(textSecPlayer, maxTextWidth);
            secPlayerAlpha = 255;
            if(bArduinoActive){serial.writeByte('o');}
            logStringIndex = (int) ofRandom(0, logString.size()-1);
            }
        else if (*msgType == '@'){
            textServer = message.erase(0,1);
            textServer = insertNewlines(textServer, maxTextWidth);
            serverAlpha = 255;
            if(bArduinoActive){serial.writeByte('r');}
            }
        else if (*msgType == '_'){
            string msgState = message.erase(0,1);
            stateSlider = ofToInt(msgState);
            if (stateSlider >= nbrOfState){
                stateSlider = nbrOfState-1;
                }
            }
        }
    // cout << textSecPlayer << endl;
}

//--------------------------------------------------------------
void ofApp::drawTop(){
    ofPushStyle();
    // rectangle
    ofFill();
    ofSetColor(stateColor[stateSlider]);
    ofDrawRectangle(0,0,width, topBorder);
    ofPushMatrix();
    ofScale(topBorder / crashos.getHeight(), topBorder / crashos.getHeight(), 1);
    crashos.draw(width/2 + crashos.getWidth()/2,0);
    ofPopMatrix();
    ofSetColor(255);
    string logTextI= logString[logStringIndex];
    logTextI = insertNewlines(logTextI, maxLogWidth);
    vagRoundedMini.drawString(logTextI, paddingSide, topBorder/2);
    // icosphere
    float cpuMult = ofMap(cpu,0,100,0.2,8);
    float spinX = sin(ofGetElapsedTimef()*0.05f);
    float spinY = cos(ofGetElapsedTimef()*0.75f);
    ofNoFill();
    icoSphere.setPosition(width-100, 50,0);
    icoSphere.rotateDeg(spinX, 0.8*cpuMult, 0.03*cpuMult, 0.7*cpuMult);
    icoSphere.rotateDeg(spinY, 0.3*cpuMult, 0.8*cpuMult, 0.4*cpuMult);
    icoSphere.drawWireframe();
    ofPopStyle();

}

void ofApp::drawBottom(){
    ofPushMatrix();
    ofPushStyle();
    int shadowLetter = 3;
    ofTranslate(0,height-bottomBorder);
    ofFill();
    ofDrawRectangle(0,0, width, bottomBorder);
    ofSetColor(ofColor(ofMap((int) cpu, 0, 100,0,255), 0,0),160);
    ofDrawRectangle(width-300,0, 300,bottomBorder);

    ofSetColor(0,120);
    vagRounded.drawString(serverName, paddingSide, vagRounded.getAscenderHeight()); // server name

    ofSetColor(255);
    vagRounded.drawString(serverName, paddingSide - shadowLetter, vagRounded.getAscenderHeight() - shadowLetter);
    ofPopStyle();
    ofPopMatrix();

    ofSetColor(0,120);
    vagRounded.drawString("CPU : " + ofToString(cpu) + " %", cpuPos->x, cpuPos->y); // CPU
    ofSetColor(255);
    vagRounded.drawString("CPU : " + ofToString(cpu) + " %", cpuPos->x - shadowLetter , cpuPos->y - shadowLetter);
}


//--------------------------------------------------------------
void ofApp::drawCode(){
    ofPushStyle();
    // First Player code box
    ofPushMatrix();
    ofTranslate(codeFirstPos->x, codeFirstPos->y);
    firstCol.a = firstPlayerAlpha;
    fontBackColor.a = secPlayerAlpha;
    ofSetColor(fontBackColor);
    font.drawString(textFirstPlayer, 0, 0);
    ofSetColor(firstCol);
    font.drawString(textFirstPlayer, -1, -1);
    ofPopMatrix();

    // Second Player code box
    ofPushMatrix();
    ofTranslate(codeSecondPos->x, codeSecondPos->y);
    secCol.a = secPlayerAlpha;
    fontBackColor.a = secPlayerAlpha;
    ofSetColor(fontBackColor);
    font.drawString(textSecPlayer, 0, 0);
    ofSetColor(secCol);
    font.drawString(textSecPlayer, -1, -1);
    ofPopMatrix();

    // Server code box
    ofPushMatrix();
    ofTranslate(serverPos->x, serverPos->y);
    serverCol.a = serverAlpha;
    ofSetColor(serverCol);
    font.drawString(textServer, 0, 0);
    ofPopMatrix();
    ofPopStyle();
}


//-------------------------
void ofApp::exit(){
  for (int i=0; i<nbrOfState; i++){
    videoPlayer[i].close();
  }
}

//-------------------------
void ofApp::setFx(){
    if (!showGui){
    bNoise = false;
    bEdge = false;
    bFringe = false;
    bInvert = false;
    bShift = false;
    bChip = false;
    bVNoise = false;
    bSlide = false;

        switch(stateSlider)
          {
            case 0:            // server attack
                bNoise = true;
                bEdge = true;
                bShift = true;
                bChip = true;
                bSlide = true;
                break;
            case 1:
                break;
            case 2:
                bShift = true;
                bChip = true;
                break;
            case 3:
                bVNoise = true;
                bSlide = true;
                break;
            case 4:
                bEdge = true;
                bFringe = true;
                break;
          }
        }
    fx.getfxUnit(KSMR_FRAGFX_NOISE)->bEnable		= bNoise;
    fx.getfxUnit(KSMR_FRAGFX_EDGEONTOP)->bEnable	= bEdge;
    fx.getfxUnit(KSMR_FRAGFX_FRINGE)->bEnable		= bFringe;
    fx.getfxUnit(KSMR_FRAGFX_INVERT)->bEnable		= bInvert;
    fx.getfxUnit(KSMR_FRAGFX_SLANTSHIFT)->bEnable	= bShift;
    fx.getfxUnit(KSMR_FRAGFX_TEXCHIP)->bEnable		= bChip;
    fx.getfxUnit(KSMR_FRAGFX_VERTNOISE)->bEnable	= bVNoise;
    fx.getfxUnit(KSMR_FRAGFX_VERTSLIDE)->bEnable	= bSlide;

    fx.getfxUnit(KSMR_FRAGFX_NOISE)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_EDGEONTOP)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_FRINGE)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_INVERT)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_SLANTSHIFT)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_TEXCHIP)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_VERTNOISE)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);
    fx.getfxUnit(KSMR_FRAGFX_VERTSLIDE)->u_Volume = ofMap(cpu, 0,cpuStress,0,1);

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    switch (key) {
    case 'g':
        showGui = !showGui;
        break;
    case 'f':
        ofToggleFullscreen();
    default:
        break;
    }
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
    width = w;
    height = h;
    codeFirstPos.setMax(ofVec2f(w,h));
    codeSecondPos.setMax(ofVec2f(w,h));
    serverPos.setMax(ofVec2f(w,h));
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){

}

// return a text with a new line every x
string ofApp::insertNewlines(string in, const size_t every_n)
{
    string out;
    out.reserve(in.size() + in.size() / every_n);
    for(std::string::size_type i = 0; i < in.size(); i++) {
        if (!(i % every_n) && i) {
            out.push_back('\n');
        }
        out.push_back(in[i]);
    }
    return out;
}


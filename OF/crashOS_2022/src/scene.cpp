#include "scene.h"
#include "ofApp.h"

////// HELP //////////
////// UPDATE GRAMMAR
/// videoplayer.update("Category", integrity)
/// winCode.update(data.vectorCode);
/// winCpu.update(data.scCPU*cpuStress);
/// winIntegrity.update(integrity);
/// winIntegrity.update(integrity, render.currentText); // For 3d render
/// uiMisc.update(bool blogo);
/// glitcher.update(fbo, audioFft.beat.getMagnitude()*audioThresh/20);
/// webcam.update();
/// videoplayer3d.update3d("Category", integrity, audioFft.beat.getMagnitude()*audioThresh/20);
/// dmx.update(ofColor dmx1, ofColor dmx2);


///// DRAW GRAMMAR
/// videoplayer.draw();
/// webcam.draw();
/// winCode.draw(data.vectorCode);
/// winCpu.draw();
/// winIntegrity.draw();
/// uiMisc.draw(true, data.isServerActive);
/// glitcher.draw(glm::vec3 vecPos, glm::vec2 vecSize, bool alpha=false)
/// sphereMap.draw();
/// render.draw();
/// text3d.draw(render.currentText);


//// FUNCTION GRAMMAR
/// uiMisc.changeLogo(index);
/// videoplayer.videoSrcub();
/// render.destroyMesh(integrityIncr);


//////////////////////////////////

///// SCENE 0/////
/// BOOT SEQUENCE
///
void ofApp::scene0Update(){
   videoplayer.update(0);
   boot.update();
   // DMX White
   float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
   float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
   dmx1Col = ofColor::fromHsb(36, sinCol, 5);
   dmx2Col = ofColor::fromHsb(36, sinCol2, 5);
   dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene0Draw(){
    postCode.begin();
        videoplayer.draw();
        boot.draw(integrity);
    postCode.end();
}

void ofApp::scene0Bang(char playerID){
    integrity -= integrityIncr;
}

void ofApp::scene0BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
    uiMisc.changeLogo(1);
    videoplayer.bthread = true;
}

/////////////////


//// SCENE 1 /////////
/// SCAN DU RESEAU
///
void ofApp::scene1Update(){
    videoplayer.update(1, integrity);
    //webcam.update();
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    uiMisc.update(true);

    // DMX jaune oscillation
    float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
    float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
    dmx1Col = ofColor::fromHsb(36, sinCol, 10-kick*10);
    dmx2Col = ofColor::fromHsb(36, sinCol2, 10-snare*10);
    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene1Draw(){
    postCode.begin();
    videoplayer.draw();
    //webcam.draw();
    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();
    postCode.end();
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene1Bang(char playerID){

    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}

void ofApp::scene1BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
/////////////////////

//// SCENE 2 ////////
//// target selected

void ofApp::scene2Update(){
//    glitcherLogo.update(uiMisc.uiFbo);
    videoplayer.bthread = false;
    videoplayer.update(2, integrity);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    uiMisc.update(true);
    webcam.update();

    uiMisc.changeLogo(2);
    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene2Draw(){
    postProc.begin();
    videoplayer.draw();


    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(true, data.isServerActive);
    webcam.draw();
    postProc.end();

//    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
}

void ofApp::scene2Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
    // DMX reagit au code
    if (playerID =='!'){
        dmx1Col = ofColor::paleTurquoise;
        dmx2Col = ofColor(0,0,0);
    }
    else if (playerID =='#'){
        dmx1Col = ofColor(0,0,0);
        dmx2Col = ofColor::greenYellow;
    }
    else if (playerID =='@'){
        dmx1Col = ofColor(255,0,0);
        dmx2Col = ofColor(255,0,0);
    }
}

void ofApp::scene2BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
///////////////////////

//// SCENE 3 ////////
void ofApp::scene3Update(){
//    videoplayer3d.update3d(3, integrity, audioFft.beat.getMagnitude()*audioThresh/20);
    videoplayer.bthread = true;
    videoplayer.update(3, integrity);

    webcam.update();

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    glitcherLogo.update(uiMisc.uiFbo);

    uiMisc.update(true);
    uiMisc.changeLogo(3);

    dmx1Col = ofColor(rms*255*audioThresh/20);
    dmx2Col = ofColor(rms*255*audioThresh/20);

    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene3Draw(){
    postTV.begin();
    postTV.tv->setRollSpeed(kick*0.001*audioThresh);
    videoplayer.draw();
    webcam.draw();
    postTV.end();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(true, data.isServerActive);
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
}

void ofApp::scene3Bang(char playerID){
    // DMX reagit au code
        if (playerID =='!'){
            dmx1Col = ofColor::paleTurquoise;
            dmx2Col = ofColor(0,0,0);
        }
        else if (playerID =='#'){
            dmx1Col = ofColor(0,0,0);
            dmx2Col = ofColor::greenYellow;
        }
        else if (playerID =='@'){
            dmx1Col = ofColor(255,0,0);
            dmx2Col = ofColor(255,0,0);
        }

    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}

void ofApp::scene3BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}

////////////////////////

//// SCENE 4 ////////
void ofApp::scene4Update(){
    videoplayer.update(4, integrity);
//    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    // DMX blue oscillation
    float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
    float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
    dmx1Col = ofColor::fromHsb(207, sinCol, 67);
    dmx2Col = ofColor::fromHsb(207, sinCol2, 67);
    dmx.update(dmx1Col, dmx2Col);


}

void ofApp::scene4Draw(){
//    glitcherVideo.draw(videoplayer.pos, videoplayer.size);
    videoplayer.draw();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

//    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
//    glitcherCam.draw(webcam.pos, webcam.size);
}

void ofApp::scene4Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}

void ofApp::scene4BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
////////////////////////

//// SCENE 5 ////////
void ofApp::scene5Update(){
    videoplayer.update(5, integrity);
//    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    webcam.update();

    uiMisc.update(true);
    uiMisc.changeLogo(5);

    dmx.update(dmx1Col, dmx2Col);

    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
    glitcherCam.update(webcam.camFbo, rms*audioThresh/20);
}

void ofApp::scene5Draw(){
    postKali.begin();
        postKali.kali->setSegments(2);
    videoplayer.draw();
    postKali.end();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(false, data.isServerActive);
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    glitcherCam.draw(webcam.pos, webcam.size);
}

void ofApp::scene5Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
    // DMX reagit au code
    if (playerID =='!'){
        dmx1Col = ofColor::paleTurquoise;
        dmx2Col = ofColor(0,0,0);
    }
    else if (playerID =='#'){
        dmx1Col = ofColor(0,0,0);
        dmx2Col = ofColor::greenYellow;
    }
    else if (playerID =='@'){
        dmx1Col = ofColor(255,0,0);
        dmx2Col = ofColor(255,0,0);
    }
}

void ofApp::scene5BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
////////////////////////

//// SCENE 6 ////////
void ofApp::scene6Update(){
    videoplayer3d.update3d(6, integrity, rms*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    uiMisc.update(true);
    uiMisc.changeLogo(6);

    dmx1Col = ofColor(rms*audioThresh/20*255);
    dmx2Col = ofColor(rms*audioThresh/20*255);

    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene6Draw(){
    videoplayer3d.draw3d();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene6Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;

}

void ofApp::scene6BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
////////////////////////

//// SCENE 7 ////////
void ofApp::scene7Update(){
    videoplayer.bthread = false;
    videoplayer.update(7, integrity);
//    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    webcam.update();

    uiMisc.update(true);
    uiMisc.changeLogo(7);

    dmx.update(dmx1Col, dmx2Col);

    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
//    glitcherCam.update(webcam.camFbo, audioFft.beat.getMagnitude()*audioThresh/20);

}

void ofApp::scene7Draw(){
    postProc.begin();
    videoplayer.draw();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    webcam.draw();

    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
//    glitcherCam.draw(webcam.pos, webcam.size);
    postProc.end();
}

void ofApp::scene7Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
    // DMX reagit au code
    if (playerID =='!'){
        dmx1Col = ofColor::paleTurquoise;
        dmx2Col = ofColor(0,0,0);
    }
    else if (playerID =='#'){
        dmx1Col = ofColor(0,0,0);
        dmx2Col = ofColor::greenYellow;
    }
    else if (playerID =='@'){
        dmx1Col = ofColor(255,0,0);
        dmx2Col = ofColor(255,0,0);
    }
}

void ofApp::scene7BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
////////////////////////

//// SCENE 8 ////////
void ofApp::scene8Update(){
    videoplayer.bthread = true;
    videoplayer.update(8, integrity);
//    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    webcam.update();

    uiMisc.update(true);
    uiMisc.changeLogo(0);

    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
    glitcherCam.update(webcam.camFbo, rms*audioThresh/20);

    dmx1Col = ofColor(rms*255*audioThresh/20);
    dmx2Col = ofColor(rms*255*audioThresh/20);

    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene8Draw(){
    postProc.begin();
    videoplayer.draw();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

//    webcam.draw();

    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    glitcherCam.draw(webcam.pos, webcam.size);
    postProc.end();
}

void ofApp::scene8Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
    // DMX reagit au code
    if (playerID =='!'){
        dmx1Col = ofColor::paleTurquoise;
        dmx2Col = ofColor(0,0,0);
    }
    else if (playerID =='#'){
        dmx1Col = ofColor(0,0,0);
        dmx2Col = ofColor::greenYellow;
    }
    else if (playerID =='@'){
        dmx1Col = ofColor(255,0,0);
        dmx2Col = ofColor(255,0,0);
    }
}

void ofApp::scene8BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}

////////////////////////

//// SCENE 9 ////////
void ofApp::scene9Update(){
    videoplayer.bthread = true;
    videoplayer3d.update3d(9, integrity, rms*audioThresh/20);
//    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
//    webcam.update();

    uiMisc.update(true);
    uiMisc.changeLogo(0);

    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
//    glitcherCam.update(webcam.camFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    dmx1Col = ofColor(rms*255*audioThresh/20);
    dmx2Col = ofColor(rms*255*audioThresh/20);

    dmx.update(dmx1Col, dmx2Col);
}

void ofApp::scene9Draw(){
    postKali.begin();
    postKali.kali->setSegments(rms*audioThresh);
    videoplayer3d.draw3d();

    winCode.draw(data.vectorCode);

//    webcam.draw();

    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
//    glitcherCam.draw(webcam.pos, webcam.size);
    postKali.end();
    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();
}

void ofApp::scene9Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
    // DMX reagit au code
    if (playerID =='!'){
        dmx1Col = ofColor::paleTurquoise;
        dmx2Col = ofColor(0,0,0);
    }
    else if (playerID =='#'){
        dmx1Col = ofColor(0,0,0);
        dmx2Col = ofColor::greenYellow;
    }
    else if (playerID =='@'){
        dmx1Col = ofColor(255,0,0);
        dmx2Col = ofColor(255,0,0);
    }
}

void ofApp::scene9BigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
}
////////////////////////
/// Scene 10
/// Training room
/////////////////////////

void ofApp::scene10Update(){

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    uiMisc.changeLogo(10);
    uiMisc.update(true);
}

void ofApp::scene10Draw(){
    ofPushMatrix();
    ofPushStyle();
        postCode.begin();
        postCode.bloom->setBlurXY(sin(ofGetElapsedTimef()*0.01)*0.01, sin(ofGetElapsedTimef()*0.005)*0.01);
        ofEnableAntiAliasing();
        ofTranslate(ofGetWidth()/2, ofGetHeight()/2);
        ofRotateDeg(ofGetElapsedTimef()*0.1, 1,1,1);
        ofNoFill();
        ofSetColor(ofColor::blueSteel);
        ofSetLineWidth(4);
        ofDrawSphere(width*4);
        postCode.end();
    ofPopMatrix();
    ofPopStyle();
    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene10Bang(char playerID){
    integrity -= integrityIncr;
}

void ofApp::scene10BigBang(){
    scene = data.scene;
    winCpu.cpuFbo.allocate(400, 400, GL_RGBA);
    winCpu.cpuFbo.begin();
        ofClear(255,255,255, 0);
    winCpu.cpuFbo.end();
    winCpu.noiseCount = 0;
}



//// SCENE DEFAULT ////////
void ofApp::sceneDefaultUpdate(){
    cpuStress = 1000;
//    webcam.update();
//    glitcherCam.update(webcam.camFbo);

}

void ofApp::sceneDefaultDraw(){
//    webcam.draw();
    //postEdge.begin();
    //postEdge.end();
    postCode.begin();
    ofSetColor(0,125);
//    glitcherCam.draw(glm::vec3 (0,0,0), glm::vec2 (ofGetWidth(), ofGetHeight()));
    postCode.bloom->setBlurXY(ofRandom(0,0.01),ofRandom(0,0.01));
    postCode.bloom->setEnabled(ofRandom(0,100)>80);
    overheating.drawEnding(data.scCPU*cpuStress);
    postCode.end();
}

void ofApp::sceneDefaultBang(char playerID){
    integrity -= integrityIncr;
}

void ofApp::sceneDefaultBigBang(){
    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
    videoplayer.videoFbo.end();
    scene = data.scene;
    cpuStress = 1;
}


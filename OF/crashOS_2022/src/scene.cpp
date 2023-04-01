//#include "scene.h"
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
//   videoplayer.update(0);
   boot.update();
   if (bdmx){
       // DMX White
       float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
       float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
       dmx1Col = ofColor::fromHsb(36, sinCol, 5);
       dmx2Col = ofColor::fromHsb(36, sinCol2, 5);
       dmx.update(dmx1Col, dmx2Col);
       }
}

void ofApp::scene0Draw(){
    postCode.begin();
//        videoplayer.draw();
        boot.draw(integrity);
    postCode.end();
}

void ofApp::scene0Bang(char playerID){
    integrity -= integrityIncr;

//    vector<string> vect{ofToString(videoplayer.vidCat), ofToString(videoplayer.vidId), ofToString(videoplayer.vidTotal), ofToString(integrity)};
//    data.sendOSC("/cmd/Video", vect);
}

void ofApp::scene0BigBang(){
//    videoplayer.videoFbo.allocate(ofGetWidth(), ofGetHeight(), GL_RGBA);
//    videoplayer.videoFbo.begin();
        ofClear(0,0,0, 0);
//    videoplayer.videoFbo.end();
    scene = data.scene;
    uiMisc.changeLogo(1);
//    videoplayer.bthread = true;
}

/////////////////


//// SCENE 1 /////////
/// HARDWARE/SCANDURESEAU/DEMARRAGE///
///44
void ofApp::scene1Update(){
    videoplayerHap.newCat(1);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.update(true);
    if(bdmx){
        // DMX jaune oscillation
        float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
        float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
        dmx1Col = ofColor::fromHsb(36, sinCol, 10-kick*10);
        dmx2Col = ofColor::fromHsb(36, sinCol2, 10-snare*10);
        dmx.update(dmx1Col, dmx2Col);
 //       dmx1Col = ofColor::fromHsb(36, sinCol, euroCent(kick, 0.2);
    }
}

void ofApp::scene1Draw(){
    ofEnableAlphaBlending();
    postPixel.begin();
    postPixel.pixel->resolution = ofVec2f(ofMap(integrity,100,0,1920, 50),ofMap(integrity,100,0,1080,50));
    videoplayerHap.draw();
    postPixel.end();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene1Bang(char playerID){
    integrity -= integrityIncr;
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
}

void ofApp::scene1BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
/////////////////////

//// SCENE 2 ////////
//// BIRTHSOMETHING

void ofApp::scene2Update(){
    videoplayerHap.newCat(2);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.update(true);
    webcam.update();
    uiMisc.changeLogo(2);
    if(bdmx){dmx.update(dmx1Col, dmx2Col);}
}

void ofApp::scene2Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(true, data.isServerActive);
    webcam.draw();
}

void ofApp::scene2Bang(char playerID){
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;

    if (bdmx){
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
}

void ofApp::scene2BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
///////////////////////

//// SCENE 3 ////////
void ofApp::scene3Update(){
    videoplayerHap.newCat(3);
    webcam.update();
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    glitcherLogo.update(uiMisc.uiFbo);
    uiMisc.update(true);
    uiMisc.changeLogo(3);

    if (bdmx){
        dmx1Col = ofColor(rms*255*audioThresh/20);
        dmx2Col = ofColor(rms*255*audioThresh/20);
        dmx.update(dmx1Col, dmx2Col);
        }
}

void ofApp::scene3Draw(){
    videoplayerHap.draw();
    webcam.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(true, data.isServerActive);
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
}

void ofApp::scene3Bang(char playerID){
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;

    if(bdmx){
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

}

void ofApp::scene3BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}

////////////////////////

//// SCENE 4 ////////
void ofApp::scene4Update(){
    videoplayerHap.newCat(4);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
//    videoplayerHap.videoScrub(rms*audioThresh*0.135*0.2);


    if (bdmx){
        // DMX blue oscillation
        float sinCol = (abs(sin(ofGetElapsedTimef()*0.1)))*255;
        float sinCol2 = (abs(sin((ofGetElapsedTimef()+50)*0.1)))*255;
        dmx1Col = ofColor::fromHsb(207, sinCol, 67);
        dmx2Col = ofColor::fromHsb(207, sinCol2, 67);
        dmx.update(dmx1Col, dmx2Col);
    }

}

void ofApp::scene4Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
}

void ofApp::scene4Bang(char playerID){
//    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;
}

void ofApp::scene4BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
////////////////////////

//// SCENE 5 ////////
void ofApp::scene5Update(){
    videoplayerHap.newCat(5);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    webcam.update();
    uiMisc.update(true);
    uiMisc.changeLogo(5);
    if(bdmx){dmx.update(dmx1Col, dmx2Col);}
    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
    glitcherCam.update(webcam.camFbo, rms*audioThresh/20);
}

void ofApp::scene5Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(false, data.isServerActive);
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    glitcherCam.draw(webcam.pos, webcam.size);
}

void ofApp::scene5Bang(char playerID){
    if (bdmx){
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
        videoplayerHap.videoScrub(0);
        vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
        data.sendOSC("/cmd/Video", vect);
        integrity -= integrityIncr;
}

void ofApp::scene5BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
////////////////////////

//// SCENE 6 ////////
void ofApp::scene6Update(){
    videoplayerHap.newCat(6);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.update(true);
    uiMisc.changeLogo(6);

    if (bdmx){
        dmx1Col = ofColor(rms*audioThresh/20*255);
        dmx2Col = ofColor(rms*audioThresh/20*255);
        dmx.update(dmx1Col, dmx2Col);
    }
}
void ofApp::scene6Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene6Bang(char playerID){
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;
}

void ofApp::scene6BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
////////////////////////
//// SCENE 7 ////////
void ofApp::scene7Update(){
    videoplayerHap.newCat(7);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.update(true);
    uiMisc.changeLogo(7);
    if(bdmx){dmx.update(dmx1Col, dmx2Col);}
    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
}
void ofApp::scene7Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
}

void ofApp::scene7Bang(char playerID){
    if (bdmx){
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
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;
}

void ofApp::scene7BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}
////////////////////////

//// SCENE 8 ////////
void ofApp::scene8Update(){
    videoplayerHap.newCat(8);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    webcam.update();
    uiMisc.update(true);
    uiMisc.changeLogo(0);
    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
    glitcherCam.update(webcam.camFbo, rms*audioThresh/20);
    if (bdmx){
        dmx1Col = ofColor(rms*255*audioThresh/20);
        dmx2Col = ofColor(rms*255*audioThresh/20);
        dmx.update(dmx1Col, dmx2Col);
    }
}

void ofApp::scene8Draw(){
    videoplayerHap.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    glitcherCam.draw(webcam.pos, webcam.size);
}

void ofApp::scene8Bang(char playerID){
    if (bdmx){

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
    videoplayerHap.videoScrub(0);
    vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;
 }

void ofApp::scene8BigBang(){
    videoplayerHap.newSeq();
    scene = data.scene;
}

////////////////////////

//// SCENE 9 ////////
void ofApp::scene9Update(){
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.update(true);
    uiMisc.changeLogo(0);
    glitcherLogo.update(uiMisc.uiFbo, rms*audioThresh/20);
    if (bdmx){
        dmx1Col = ofColor(rms*255*audioThresh/20);
        dmx2Col = ofColor(rms*255*audioThresh/20);
        dmx.update(dmx1Col, dmx2Col);
        }
}
void ofApp::scene9Draw(){
    postKali.begin();
    postKali.kali->setSegments(rms*audioThresh);
    winCode.draw(data.vectorCode, data.vectorInstant);
    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    postKali.end();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
}

void ofApp::scene9Bang(char playerID){
    integrity -= integrityIncr;
    if (bdmx){
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
}

void ofApp::scene9BigBang(){
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
    winScore.update(svdkScore, zbdmScore, serverScore);
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

    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
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
    uiMisc.changeLogo(1);
    winCpu.noiseCount = 0;
    svdkScore = 0;
    zbdmScore = 0;
    serverScore = 0;
}


////////////////////////
/// Scene 11
/// Image Player
/////////////////////////

void ofApp::scene11Update(){
    imageplayer.update(integrity);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    //uiMisc.changeLogo(11);
    uiMisc.update(true);
}

void ofApp::scene11Draw(){
    ofPushMatrix();
    ofPushStyle();
//        postCode.begin();
        imageplayer.draw();
//        postCode.end();
    ofPopMatrix();
    ofPopStyle();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(false, data.isServerActive);
}

void ofApp::scene11Bang(char playerID){
    integrity -= integrityIncr;
    imageplayer.destroy();
}

void ofApp::scene11BigBang(){
    scene = data.scene;
    imageplayer.newImage();
}

////////////////////////
/// Scene 12
/// Textris
/////////////////////////
void ofApp::scene12Update(){
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.changeLogo(12);
    uiMisc.update(true);
    textris.update(audioFft.beat.getFft());
}

void ofApp::scene12Draw(){
    postProc.begin();
    winCode.draw(data.vectorCode, data.vectorInstant, false);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();
    uiMisc.draw(true, data.isServerActive);
    textris.draw();
    postProc.end();
}

void ofApp::scene12Bang(char playerID){
    integrity -= integrityIncr;
    if (!data.vectorCode.empty())
       textris.addText(data.vectorCode.back().code, data.vectorCode.back().symbol);
}

void ofApp::scene12BigBang(){
    scene = data.scene;
    textris.clear();
}

////   SCENE 404  //////
//// SCENE SERVER /////
void ofApp::sceneServerUpdate(){
    videoHapServer.newCat(0);
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    winScore.update(svdkScore, zbdmScore, serverScore);
    uiMisc.changeLogo(4);
    uiMisc.update(true);
}

void ofApp::sceneServerDraw(){
    videoHapServer.draw();
    winCode.draw(data.vectorCode, data.vectorInstant);
    winCpu.draw();
    winIntegrity.draw();
    winScore.draw();

    uiMisc.draw(true, false);

}

void ofApp::sceneServerBang(char playerID){
    scene = data.scene;
    /// server code injection virus
    for (int i=0; i<data.vectorCode.size(); i++){
        data.vectorCode[i].code = winCode.textInjection(data.vectorCode[i].code);
    }
    winIntegrity.targetText = winIntegrity.textInjection(winIntegrity.targetText);

    //videoplayerHap.videoScrub(0);
    //vector<string> vect{ofToString(videoplayerHap.vidDirIndex), ofToString(videoplayerHap.vidIndex), ofToString(videoplayerHap.vidTotal), ofToString(integrity)};
    //data.sendOSC("/cmd/Video", vect);
    integrity -= integrityIncr;
}

void ofApp::sceneServerBigBang(){
    videoHapServer.newSeq();
    scene = data.scene;
}



//// SCENE DEFAULT ////////
void ofApp::sceneDefaultUpdate(){
    cpuStress = 1000;
    data.serial.writeByte('f');
    data.serial.flush();
}

void ofApp::sceneDefaultDraw(){
    postCode.begin();
    ofSetColor(0,125);
    postCode.bloom->setBlurXY(ofRandom(0,0.01),ofRandom(0,0.01));
    postCode.bloom->setEnabled(ofRandom(0,100)>80);
    overheating.drawEnding(data.scCPU*cpuStress);
    postCode.end();
}

void ofApp::sceneDefaultBang(char playerID){
    integrity -= integrityIncr;
}

void ofApp::sceneDefaultBigBang(){
    scene = data.scene;
    cpuStress = 1;
}


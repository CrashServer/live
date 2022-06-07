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
   boot.update();
}

void ofApp::scene0Draw(){
    postCode.begin();
        boot.draw();
    postCode.end();
}

void ofApp::scene0Bang(char playerID){
    integrity -= integrityIncr;
}

/////////////////


//// SCENE 1 /////////
/// SCAN DU RESEAU
///
void ofApp::scene1Update(){
    videoplayer.update(1, integrity);
    webcam.update();
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);
    uiMisc.update(true);
}

void ofApp::scene1Draw(){
    videoplayer.draw();
    webcam.draw();
    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene1Bang(char playerID){
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
}
/////////////////////

//// SCENE 2 ////////

void ofApp::scene2Update(){
    glitcherLogo.update(uiMisc.uiFbo);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    uiMisc.update(true);
    webcam.update();

    videoplayer.update(2, integrity);
}

void ofApp::scene2Draw(){
    videoplayer.draw();
    webcam.draw();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(true, data.isServerActive);

    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
}

void ofApp::scene2Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}
///////////////////////

//// SCENE 3 ////////
void ofApp::scene3Update(){
    videoplayer3d.update3d(3, integrity, audioFft.beat.getMagnitude()*audioThresh/20);
    webcam.update();

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    uiMisc.update(true);
}

void ofApp::scene3Draw(){
    videoplayer3d.draw3d();
    webcam.draw();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    uiMisc.draw(true, data.isServerActive);
    uiMisc.draw(true, data.isServerActive);
}

void ofApp::scene3Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}
////////////////////////

//// SCENE 4 ////////
void ofApp::scene4Update(){
    videoplayer.update(4, integrity);
    glitcherVideo.update(videoplayer.videoFbo, audioFft.beat.getMagnitude()*audioThresh/20);

    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity);

    webcam.update();
    uiMisc.update(true);

    glitcherLogo.update(uiMisc.uiFbo, audioFft.beat.getMagnitude()*audioThresh/20);
    glitcherCam.update(webcam.camFbo, audioFft.beat.getMagnitude()*audioThresh/20);
}

void ofApp::scene4Draw(){
    glitcherVideo.draw(videoplayer.pos, videoplayer.size);

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();

    webcam.draw();
    uiMisc.draw(false, data.isServerActive);

    glitcherLogo.draw(uiMisc.pos, uiMisc.size, true);
    glitcherCam.draw(webcam.pos, webcam.size);
}

void ofApp::scene4Bang(char playerID){
    videoplayer.videoSrcub();
    integrity -= integrityIncr;
}
////////////////////////

//// SCENE 5 ////////
void ofApp::scene5Update(){
    winCode.update(data.vectorCode);
    winCpu.update(data.scCPU*cpuStress);
    winIntegrity.update(integrity, render.currentText);
}

void ofApp::scene5Draw(){
    cam.begin();
    cam.setDistance(260);
        sphereMap.draw();
        render.draw();
        text3d.draw(render.currentText);
        //tunnel3d.draw();
    cam.end();

    winCode.draw(data.vectorCode);
    winCpu.draw();
    winIntegrity.draw();
    uiMisc.draw(false, data.isServerActive);
}

void ofApp::scene5Bang(char playerID){
    render.destroyMesh(integrityIncr);
    integrity = (int) render.intergrity;
}
////////////////////////

//// SCENE 6 ////////
void ofApp::scene6Update(){

}

void ofApp::scene6Draw(){

}

void ofApp::scene6Bang(char playerID){

}
////////////////////////

//// SCENE 7 ////////
void ofApp::scene7Update(){

}

void ofApp::scene7Draw(){

}

void ofApp::scene7Bang(char playerID){

}
////////////////////////

//// SCENE 8 ////////
void ofApp::scene8Update(){

}

void ofApp::scene8Draw(){

}

void ofApp::scene8Bang(char playerID){

}
////////////////////////

//// SCENE 9 ////////
void ofApp::scene9Update(){

}

void ofApp::scene9Draw(){

}

void ofApp::scene9Bang(char playerID){

}
////////////////////////

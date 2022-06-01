#include "Camera.h"

Camera::Camera(){
//    vector<ofVideoDevice> devices = webcam.listDevices();

//     for(size_t i = 0; i < devices.size(); i++){
//         if(devices[i].bAvailable){
//             //log the device
//             ofLogNotice() << devices[i].id << ": " << devices[i].deviceName;
//         }else{
//             //log the device and note it as unavailable
//             ofLogNotice() << devices[i].id << ": " << devices[i].deviceName << " - unavailable ";
//         }
//     }
//    webcam.setDeviceID(1);
    webcam.setup(320,240);
}


void Camera::setup(ofColor uiColor){
    width = ofGetWidth();
    height = ofGetHeight();
    if (parameters.size()==0){
        parameters.setName("webcam");
        parameters.add(size.set("Webcam size", glm::vec2(320, 240), glm::vec2(0, 0), glm::vec2(width, height)));
        parameters.add(pos.set("Webcam Box", glm::vec3(1480, 220, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
        size.addListener(this, &Camera::resize);
        }
    camFbo.allocate(size->x, size->y, GL_RGBA);
    this->uiColor = uiColor;
}


void Camera::update(){
    webcam.update();
}

void Camera::draw(){
    ofPushMatrix();
    ofPushStyle();
    ofDisableDepthTest();
    ofDisableAlphaBlending();
    ofDisableLighting();
    ofDisableNormalizedTexCoords();
        camFbo.begin();
            ofSetColor(ofColor::paleGreen);
            webcam.draw(0,0, size->x, size->y);
        //webcam.draw(webcamPos.x,webcamPos.y, webcamSize.x,webcamSize.y);
        //ofApp::windowDraw(webcamPos, webcamSize, uiColor);
        camFbo.end();
        cameraWin.drawWin(pos, size, this->uiColor);
        camFbo.draw(pos->x,pos->y, size->x, size->y);

    ofPopStyle();
    ofPopMatrix();
}

void Camera::resize(glm::vec2 &){
//    webcam.setup(size->x,size->y);
    camFbo.allocate(size->x, size->y, GL_RGBA);
}


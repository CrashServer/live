#include "ofApp.h"
#include "boot.h"

Boot::Boot(){

}

void Boot::setup(){
    width = ofGetWidth();
    height = ofGetHeight();

    font.load("ui/font/pixe.ttf", 36);
    fontCharBox = font.getStringBoundingBox("P", 0, 0);
    xml.load("xml/boot.xml");
    string xmlString = xml.getValue("logText", "bootServer");

    maxLine = (int) (height+25) /  (fontCharBox.height+15);

    posIntegrity = glm::vec2((width - (fontCharBox.width*10) - 10),
                             height- fontCharBox.height - 10);

    std::stringstream stringStream(xmlString);
    while(stringStream.good())
        {
            std::string substr;
            getline(stringStream, substr, ',');
            bootLine.push_back(substr);
        }

    cBoot.assign(maxLine, " ");
    rtime = ofRandom(20,142);
    incr=0;
    _integrity = 100;

    logoCrash.load("ui/crashlogo.svg");   
}

void Boot::update(int integrity){
    this->_integrity = integrity; 
    incr++;
    if (incr >= rtime){
        if (cBoot.size() >= maxLine) {
            cBoot.erase(cBoot.begin());
            }
        string selectLine = bootLine[ofRandom(0, bootLine.size())];
        cBoot.push_back(selectLine);
        incr=0;
        rtime = ofRandom(ofMap(_integrity,100,5,20,0.1,true), ofMap(_integrity, 100,5,140,0.2,true));
    }
}

void Boot::draw(){
    ofPushStyle();
    ofSetColor(ofColor::greenYellow);
    for (unsigned int i=0; i< (cBoot.size()); i++){
            if (i == (cBoot.size()-1)){
                string subString = cBoot[i].substr(0,ofMap(incr,0,rtime,0,cBoot[i].size()-1));
                font.drawString(subString, 50, 50+(i*(fontCharBox.height+15)));
                }
            else {
                font.drawString(cBoot[i], 50, 50+(i*(fontCharBox.height+15)));
                }
            }

    ofPushMatrix();
            ofTranslate(posIntegrity.x, posIntegrity.y);
            int integrityDiv = _integrity/10;
            for (int i=integrityDiv; i>0; i--){
            font.drawString("*", (fontCharBox.width)*i, 0);
        }
    ofPopMatrix();
        ofPopStyle();


    if (bShowMsg) {
        ofPushMatrix();
        ofSetColor(255, 0, 0, ofMap(sin(ofGetFrameNum()*0.1),-1,1,0,255));
        ofTranslate(width * 2/3, height * 1/3);
        font.drawString(waitingMsg, 0, 0);
        ofPopMatrix();
    }

    ofPushMatrix();
    ofPushStyle();
    ofTranslate((ofMap(_integrity, 100, 5, width/2 - logoCrash.getWidth()/2, 50)), ofMap(_integrity, 100, 5, height, height/2 - logoCrash.getHeight()*0.55));
    ofScale(ofMap(_integrity, 100,5, 0, 1, true));
    logoCrash.draw();
    ofPopStyle();
    ofPopMatrix();

}


void Boot::resize(){
    this->width = ofGetWidth();
    this->height = ofGetHeight();
    maxLine = (int) (height-25) /  (fontCharBox.height+15);
    cBoot.resize(maxLine);
    posIntegrity = glm::vec2((this->width - (fontCharBox.width*10) - 50),
                             this->height - fontCharBox.height - 50);
}

#include "boot.h"
#include "ofApp.h"

Boot::Boot(){

}

void Boot::setup(){
    maxLine = 30;
    width = ofGetWidth();
    height = ofGetHeight();

    font.load("ui/font/pixe.ttf", 36);
    fontCharBox = font.getStringBoundingBox("P", 0, 0);
    xml.loadFile("xml/boot.xml");
    string xmlString = xml.getValue("logText", "bootServer");

    std::stringstream stringStream(xmlString);
    while(stringStream.good())
        {
            std::string substr;
            getline(stringStream, substr, ',');
            bootLine.push_back(substr);
        }
    for (int i=0; i<10; i++){
        cout << bootLine[ofRandom(0, bootLine.size())] << endl;
    }

    cBoot.assign(maxLine, " ");

}

void Boot::update(){
    static int incr=0;
    static int rtime = ofRandom(3, 142);
    if (incr == rtime){
        if (cBoot.size() >= maxLine) {
            cBoot.erase(cBoot.begin());
            }
        string selectLine = bootLine[ofRandom(0, bootLine.size())];
        cBoot.push_back(selectLine);
    }
    incr++;
    if (incr>rtime){
        incr=0;
        rtime = ofRandom(6, 14);
    }


}

void Boot::draw(){
    ofSetColor(ofColor::greenYellow);
    for (unsigned int i=0; i<cBoot.size(); i++){
        if (ofRandom(0,100)>90){
            font.drawString(" ", 100, 100+ (i*(fontCharBox.height+15)));
        }
        else {
        font.drawString(cBoot[i], 100, 100+(i*(fontCharBox.height+15)));
        }
        }
}


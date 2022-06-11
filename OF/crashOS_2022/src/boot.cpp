#include "ofApp.h"
#include "boot.h"

Boot::Boot(){

}

void Boot::setup(){
    width = ofGetWidth();
    height = ofGetHeight();

    font.load("ui/font/pixe.ttf", 36);
    fontCharBox = font.getStringBoundingBox("P", 0, 0);
    xml.loadFile("xml/boot.xml");
    string xmlString = xml.getValue("logText", "bootServer");

    maxLine = (int) (height-300) /  (fontCharBox.height+15);

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

}

void Boot::update(){
    incr++;
    if (incr >= rtime){
        if (cBoot.size() >= maxLine) {
            cBoot.erase(cBoot.begin());
            }
        string selectLine = bootLine[ofRandom(0, bootLine.size())];
        cBoot.push_back(selectLine);
        incr=0;
        rtime = ofRandom(20,142);
    }
}

void Boot::draw(int integrity){
    ofSetColor(ofColor::greenYellow);
    for (unsigned int i=0; i< (cBoot.size()); i++){
//        if (ofRandom(0,100)>90){
//            font.drawString(" ", 100, 100+ (i*(fontCharBox.height+15)));
//        }
//        else {
            if (i == (cBoot.size()-1)){
                string subString = cBoot[i].substr(0,ofMap(incr,0,rtime,0,cBoot[i].size()-1));
                font.drawString(subString, 50, 50+(i*(fontCharBox.height+15)));
                }
            else {
                font.drawString(cBoot[i], 50, 50+(i*(fontCharBox.height+15)));
                }
            }

    ofPopMatrix();
    ofTranslate(posIntegrity.x, posIntegrity.y);
    int integrityDiv = integrity/10;
    for (int i=integrityDiv; i>0; i--){
        font.drawString("*", (fontCharBox.width)*i, 0);
        }
    ofPushMatrix();
}


void Boot::resize(){
    this->width = ofGetWidth();
    this->height = ofGetHeight();
    maxLine = (int) (height-300) /  (fontCharBox.height+15);
    cBoot.resize(maxLine);
    posIntegrity = glm::vec2((this->width - (fontCharBox.width*10) - 50),
                             this->height - fontCharBox.height - 50);
}

#include "drawwindows.h"

Windo::Windo(){
//    // Parametre
    width = ofGetWidth();
    height = ofGetHeight();
    font.load("ui/font/pixe.ttf", 24);
    fontCharBox = font.getStringBoundingBox("P", 0, 0); // size of a char
    //gui.setup();
    //gui.setPosition(50,50);
}

//-------------------------
void Windo::drawWin(glm::vec3 windowPos, glm::vec2 windowSize, ofColor uiColor) {
    ofPushStyle();
    ofPushMatrix();
    ofDisableDepthTest();
    ofEnableAlphaBlending();

    glm::vec2 bvl = glm::vec2(10, 10); // bevel size
    ofPath path;

    ofTranslate(windowPos.x, windowPos.y, windowPos.z);

    // the transparent background
    ofColor backCol = uiColor;
    backCol.a = 180;
    ofSetColor(backCol);
    path.moveTo(0, 0);
    path.lineTo(0, windowSize.y - bvl.y);
    path.lineTo(bvl.y, windowSize.y);
    path.lineTo(windowSize.x, windowSize.y);
    path.lineTo(windowSize.x, 0);
    path.close();
    path.setFillColor(backCol);
    path.draw();

    ofSetLineWidth(8.0);
    ofSetColor(uiColor);

    // the L
    ofDrawLine(0, 0, 0, (int)(windowSize.y - bvl.y));
    ofDrawLine(0, (int)(windowSize.y - bvl.y), bvl.y, windowSize.y);
    ofDrawLine(bvl.x, windowSize.y, bvl.x, windowSize.y);
    ofDrawLine(bvl.x, windowSize.y, windowSize.x, windowSize.y);

    // the outside
    ofDrawLine(-bvl.x, windowSize.y - bvl.y, -bvl.x, -bvl.y);
    ofDrawLine(-bvl.x, -bvl.y, windowSize.x, -bvl.y);
    ofDrawLine(windowSize.x, -bvl.y, windowSize.x + bvl.x, 0);
    ofDrawLine(windowSize.x + bvl.x, 0, windowSize.x + bvl.x, windowSize.y + bvl.y);

    ofPopMatrix();
    ofPopStyle();
}

//-------------------------
void WinCode::setup(int padding, ofColor uiColor){
    this->uiColor = uiColor;
    this->padding = padding;
    // code
    maxLineCode = 40; // size of the code vector
    maxCodeWidth = width/2;
    //nbrLineCode = 10;
    codeFbo.allocate(width, height, GL_RGBA);
    codeFbo.begin();
        ofClear(255,255,255, 0);
    codeFbo.end();

    parameters.setName("code");
    parameters.add(nbrLineCode.set("Nbr of line of Code", 20, 1, maxLineCode));
    parameters.add(pos.set("CodeBox pos", glm::vec3(50, 82, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    parameters.add(size.set("CodeBox size", glm::vec2(width / 2, 5), glm::vec2(50, 0), glm::vec2(width, 40)));
}

//-------------------------
void WinCode::update(vector<string> vectorCode){
    maxCodeWidth = (int)(size->x) / fontCharBox.width; // max code text char witdh
    codeTotalHeight = 0;
    codeTotalWidth = 0;

    for (int i = vectorCode.size() - 1; i >= (maxLineCode - this->nbrLineCode); --i) {
        ofRectangle rectString = font.getStringBoundingBox(vectorCode[i], 0, 0);
        codeTotalHeight += rectString.height + size->y;
        if (rectString.width > codeTotalWidth) {
            codeTotalWidth = rectString.width;
        }
    }
}

//--------------------------------------------------------------
void WinCode::draw(vector<string> vectorCode, vector<char> vectorSymbol) {
    ofPushStyle();
    ofPushMatrix();
        Windo::drawWin(this->pos, glm::vec2(codeTotalWidth + 2 * this->padding, codeTotalHeight + (2*this->padding)), this->uiColor);
        ofTranslate(pos->x + this->padding, pos->y + font.getLineHeight(), pos->z);
        for (int i = vectorCode.size() - 1; i >= (maxLineCode - this->nbrLineCode); --i) {
            float stringHeight;

            if (vectorSymbol[i] == '#') {
                ofSetColor(ofColor(0, 255, 0));
            }
            else if (vectorSymbol[i] == '!') {
                ofSetColor(ofColor::paleTurquoise);
            }
            else if (vectorSymbol[i] == '@') {
                ofSetColor(ofColor(255, 0, 0));
            }

            font.drawString(vectorCode[i], 0, 0);
            stringHeight = font.stringHeight(vectorCode[i]);
            ofTranslate(0, stringHeight + size->y);
            }
    ofPopMatrix();
    ofPopStyle();
}

//--------------------------------------------------------------
void WinCpu::setup(int padding, ofColor uiColor){
    this->uiColor = uiColor;
    this->padding = padding;
    cpuStringBox = font.getStringBoundingBox("CPU: 99.99%", 0, 0); // size cpu string
    cpuFbo.allocate(400, 400, GL_RGBA);
    cpuFbo.begin();
        ofClear(255,255,255, 0);
    cpuFbo.end();
    noiseCount = 0;

    parameters.setName("cpu");
    parameters.add(pos.set("CPU Box", glm::vec3(1600, 780, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    parameters.add(size.set("CPU Box size", glm::vec2(200, 200), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));
}

void WinCpu::update(int scCPU){
//    this->pos = cpuPos;
//    this->size = cpuSize;
    this->scCPU = scCPU;

    cpuFbo.begin(); // draw cpu history
        ofPushStyle();
        ofSetColor(ofColor(ofMap(scCPU, 0,70,0,255, true),ofMap(scCPU, 0,70,255,0, true),0));
        ofDrawCircle(ofMap(ofNoise(noiseCount*0.001, noiseCount*0.003),0,1,0,400),
                     ofMap(ofNoise(noiseCount*0.004 , noiseCount*0.002),0,1,0,400),2);
        ofPopStyle();
    cpuFbo.end();

}

void WinCpu::draw() {
    ofEnableAlphaBlending();
    int shadowLetter = 3;
    ofPushStyle();
    ofPushMatrix();

        Windo::drawWin(this->pos, this->size, this->uiColor);
        ofTranslate(this->pos);
        cpuFbo.draw(0,0,size->x,size->y);

        ofTranslate(ofClamp(size->x / 2 - cpuStringBox.width / 2, 0, size->x / 2), ofClamp(size->y / 2 + cpuStringBox.height / 2, 0, size->y / 2));//;
        ofSetColor(255, 190);

        string cpuConv = ofToString(this->scCPU);
        if (scCPU < 10) {
            cpuConv = "0" + cpuConv;
        }

        ofSetColor(0, 120);
        font.drawString("CPU: " + ofToString(cpuConv) + "%", 0, 0); // CPU text
        ofSetColor(255);
        font.drawString("CPU: " + ofToString(cpuConv) + "%", 0 - shadowLetter, 0 - shadowLetter);

    ofPopMatrix();
    ofPopStyle();
    ofDisableAlphaBlending();
}

////-------------------------------------------------------------
//// Txt Integrity

//--------------------------------------------------------------
void WinIntegrity::setup(int padding, ofColor uiColor){
    this->uiColor = uiColor;
    this->padding = padding;
    integrityFbo.allocate(400, 400, GL_RGBA);
    integrityFbo.begin();
        ofClear(255,255,255, 0);
    integrityFbo.end();

    parameters.setName("integrity");
    parameters.add(pos.set("Integrity Box", glm::vec3(1480, 100, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    parameters.add(size.set("Integrity size", glm::vec2(320, 100), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));

}

void WinIntegrity::update(int integrity, string nameModel){
    this->integrity = integrity;
    this->nameModel = nameModel;
}

void WinIntegrity::draw()
{
    ofPushStyle();
    ofPushMatrix();
        Windo::drawWin(this->pos, this->size, this->uiColor);
        ofTranslate(pos->x + this->padding, pos->y + size->y/2 - fontCharBox.height, pos->z);
        ofEnableBlendMode(OF_BLENDMODE_MULTIPLY);
        ofSetColor(ofColor::white);
        font.drawString("TARGET INTEGRITY " + ofToString(this->integrity) + "%"
                + "\n" + nameModel, 0,0);
        ofEnableBlendMode(OF_BLENDMODE_DISABLED);
    ofPopMatrix();
    ofPopStyle();
}

//void ofApp::windowImageDraw(glm::vec3 windowPos, glm::vec2 windowSize, ofColor winColor){
//    ofPushStyle();
//    ofPushMatrix();
//    ofDisableDepthTest();
//    ofEnableAlphaBlending();
//        ofTranslate(windowPos.x, windowPos.y, windowPos.z);
//        ofScale(windowSize.x/windows.getWidth(), windowSize.y/windows.getHeight());
//        windows.draw(0,0);
//    ofDisableAlphaBlending();
//    ofPopMatrix();
//    ofPopStyle();
//}

// Draw cpu



//--------------------------------------------------------------
//void ofApp::drawLog(){
//    ofPushStyle();
//    ofPushMatrix();
//
//    drawWindow(logPos, logSize, uiColor);
//    ofTranslate(logPos->x, logPos->y+30, logPos->z);
//    ofSetColor(255);
//    string logTextI= logString[logStringIndex];
//    int maxLogWidth = (int) (logSize->x - 70) / fontCharBox.width; // max log text char witdh
//    logTextI = insertNewlines(logTextI, maxLogWidth);
//    ofRectangle logBox = font.getStringBoundingBox(logTextI,0,0);
//    logSize = glm::vec2(logSize->x, logBox.height+40);
//    font.drawString(logTextI, 10, 0);
//    ofPopMatrix();
//    ofPopStyle();
//}

/*
//-------------------------
void ofApp::drawScore(){
    drawWindow(scorePos, scoreSize, stateColor[stateSlider]);

    ofPushStyle();
    ofPushMatrix();

    ofTranslate(scorePos + glm::vec3(10,30,0));
    ofSetColor(ofColor(255, 150));
    font.drawString("CrashServer : +" + ofToString(csScore),0,0);
    font.drawString("Server : " + ofToString(serverScore),0,30);
    font.drawString("Total : " + ofToString(totalScore),0,60);

    ofPopMatrix();
    ofPopStyle();
}
*/
/*//-------------------------
void ofApp::drawTargetWindow(){
    ofPushStyle();
    drawWindow(targetWindowPos, targetWindowSize, stateColor[stateSlider]);
    ofSetColor(ofColor(255, 150));
    ofPushMatrix();
    ofTranslate(targetWindowPos + glm::vec3(10,30,0));
    font.drawString("Attack Node [" + ofToString(shapeComplexity-2) +"]",0,0);
    ofTranslate(0,30);
    font.drawString("Cells left : " + ofToString(restCell) + "/" + ofToString(totalCell), 0,0);
    if (restFireWall > 0){
        ofTranslate(0,30);
        font.drawString("FireWall left : " + ofToString(restFireWall) + "/" + ofToString(totalFireWall), 0,0);
        }
    ofPopMatrix();
    ofPopStyle();
}

*/


#include "ofApp.h"
#include "drawwindows.h"
#include "Getdata.h"

Windo::Windo(){
//    // Parametre
    width = ofGetWidth();
    height = ofGetHeight();
    font.load("ui/font/press.ttf", 16);
    fontCharBox = font.getStringBoundingBox("Q", 0, 0); // size of a char
}

OverHeating::OverHeating(){
    font.load("ui/font/press.ttf", 32);
    fontBox = font.getStringBoundingBox("Garbage collector coming soon",0,0);
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

    ofSetLineWidth(4.0);
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
void WinCode::setup(int padding, ofColor uiColor, vector<ofColor> playerColor){
    this->uiColor = uiColor;
    this->padding = padding;
    this->zbdmColor = playerColor[0];
    this->svdkColor = playerColor[1];
    this->serverColor = playerColor[2];

    // code
    maxLineCode = 40; // size of the code vector
    maxCodeWidth = width/2;
    evalSvdk = 0;
    evalZbdm = 0;

    if (parameters.size()==0){
        parameters.setName("code");
        parameters.add(nbrLineCode.set("Nbr of line of Code", 20, 1, maxLineCode));
        parameters.add(size.set("CodeBox size", glm::vec2(width / 2, 5), glm::vec2(50, 0), glm::vec2(width, 40)));
        parameters.add(pos.set("CodeBox pos", glm::vec3(50, 180, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    }
}

void Windo::resize(){
    width = ofGetWidth();
    height = ofGetHeight();
    pos.setMax(glm::vec3(width, height, 500));
}

//-------------------------
void WinCode::update(vector<CodeLine>& vectorCode){
    maxCodeWidth = (int)(size->x) / fontCharBox.width; // max code text char witdh
    codeTotalHeight = 0;
    codeTotalWidth = 0;
    if (evalSvdk > 0){evalSvdk -= 10;} // fade in eval color
    if (evalZbdm > 0){evalZbdm -= 10;} // fade in eval color

    for (int i = vectorCode.size() - 1; i >= (maxLineCode - this->nbrLineCode); --i) {
        string codeString = insertNewlines(vectorCode[i].code, maxCodeWidth);
        ofRectangle rectString = font.getStringBoundingBox(codeString, 0, 0);
        codeTotalHeight += rectString.height + size->y;
        if (rectString.width > codeTotalWidth) {
            codeTotalWidth = ofClamp(rectString.width, 0, size->x);
        }

    }
}

//--------------------------------------------------------------
void WinCode::draw(vector<CodeLine>& vectorCode, vector<CodeInstant> &vectorInstant, bool showCode) {
    ofEnableAlphaBlending();

    /// Instant Code
    ofPushStyle();
    ofPushMatrix();
        string codeZbdm = insertNewlines(vectorInstant[0].code, maxCodeWidth);
        string codeSvdk = insertNewlines(vectorInstant[1].code, maxCodeWidth);
        ofRectangle codeBoxZbdm = font.getStringBoundingBox(codeZbdm,0,0);
        ofRectangle codeBoxSvdk = font.getStringBoundingBox(codeSvdk,0,0);

        if (codeBoxSvdk.width > codeTotalWidth){codeTotalWidth = ofClamp(codeBoxSvdk.width, 0, size->x);}
        if (codeBoxZbdm.width > codeTotalWidth){codeTotalWidth = ofClamp(codeBoxZbdm.width, 0, size->x);}

        Windo::drawWin(this->pos, glm::vec2(codeTotalWidth + 4 * this->padding, (codeBoxZbdm.height + codeBoxSvdk.height) + this->padding*3), this->uiColor);
        ofTranslate(pos->x + this->padding, pos->y + font.getLineHeight() + this->padding, pos->z);

        // draw Zbdm

        // eval highlight
        ofSetColor(svdkColor, evalZbdm);
        ofDrawRectangle(codeBoxZbdm);

        // draw string
        ofSetColor(zbdmColor);
        font.drawString(codeZbdm,0,0);

        // draw cursor
        if (ofGetFrameNum()%3 == 0){
            ofSetColor(ofColor::gray);}
        else {ofSetColor(svdkColor);}

        const auto& zbdmFontMesh = font.getStringMesh(codeZbdm, 0, 0);
        const auto& zbdmFontVertices = zbdmFontMesh.getVertices();
        if(zbdmFontVertices.size() > 0 && vectorInstant[0].posMark > 0){// just make sure you are not falling out of bounds
            size_t vertIndex = (vectorInstant[0].posMark -1 ) * 4;
            ofSetLineWidth(8);
            ofDrawLine(zbdmFontVertices[vertIndex + 2] + glm::vec2(3, 3), zbdmFontVertices[vertIndex + 2] + glm::vec2(3,fontCharBox.height*-1 - 6));
            }

        // draw Svdk
        ofTranslate(0, codeBoxZbdm.height + this->padding);

        // eval highlight
        ofSetColor(svdkColor, evalSvdk);
        ofDrawRectangle(codeBoxSvdk);

        // draw string
        ofSetColor(svdkColor);
        font.drawString(codeSvdk,0,0);

        // draw cursor
        if (ofGetFrameNum()%3 == 0){
            ofSetColor(ofColor::gray);}
        else {ofSetColor(zbdmColor);}

        const auto& svdkFontMesh = font.getStringMesh(codeSvdk, 0, 0);
        const auto& svdkFontVertices = svdkFontMesh.getVertices();
        if(svdkFontVertices.size() > 0 && vectorInstant[1].posMark > 0){// just make sure you are not falling out of bounds
            size_t vertIndex = (vectorInstant[1].posMark -1 ) * 4;
            ofSetLineWidth(8);
            ofDrawLine(svdkFontVertices[vertIndex + 2] + glm::vec2(3, 3), svdkFontVertices[vertIndex + 2] + glm::vec2(3,fontCharBox.height*-1 - 6));
            }

//    ofPopMatrix();
    ofPopStyle();

    /// Code History
    if (showCode){
    ofPushStyle();
        ofTranslate(0, codeBoxSvdk.height + 100);
        Windo::drawWin(glm::vec3(0,0,0) - glm::vec3(this->padding,0,0), glm::vec2(codeTotalWidth + 4 * this->padding, codeTotalHeight + (2*this->padding)), this->uiColor);
        ofTranslate(0,fontCharBox.height + this->padding,0);
        float stringHeight;
        for (int i = vectorCode.size() - 1; i >= (maxLineCode - this->nbrLineCode); --i) {
            if (vectorCode[i].symbol == '#') { // svdk
                ofSetColor(svdkColor);
            }
            else if (vectorCode[i].symbol == '!') { // zbdm
                ofSetColor(zbdmColor);
            }
            else if (vectorCode[i].symbol == '@') { // server
                ofSetColor(serverColor);
            }

            string code = insertNewlines(vectorCode[i].code, maxCodeWidth);

            if (i == (vectorCode.size()-1)){
                int maxCod = code.size();
                string subString = code.substr(0,ofClamp(vectorCode[i].typeCodePos,0,maxCod));
                font.drawString(subString, 0, 0);

                if (vectorCode[i].typeCodePos <= maxCod){
                vectorCode[i].typeCodePos+= ofRandom(0,3);}
            }
            else {
                font.drawString(code, 0, 0);
                }

            stringHeight = font.stringHeight(code);
            ofTranslate(0, stringHeight + size->y);
            }
    ofPopMatrix();
    ofPopStyle();
    ofDisableAlphaBlending();
    }
}


//--------------------------------------------------------------
void WinCpu::setup(int padding, ofColor uiColor){
    this->uiColor = uiColor;
    this->padding = padding;
    cpuStringBox = font.getStringBoundingBox("CPU: 99%", 0, 0); // size cpu string
    cpuFbo.allocate(400, 400, GL_RGBA);
    cpuFbo.begin();
        ofClear(255,255,255, 0);
    cpuFbo.end();
    noiseCount = 0;

    if (parameters.size()==0){
        parameters.setName("cpu");
        parameters.add(size.set("CPU Box size", glm::vec2(200, 200), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));
        parameters.add(pos.set("CPU Box", glm::vec3(1480, 596, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    }

}

void WinCpu::update(int scCPU){
//    this->pos = cpuPos;
//    this->size = cpuSize;
    this->scCPU = scCPU;

    cpuFbo.begin(); // draw cpu history
        ofPushStyle();
        ofSetColor(ofColor(ofMap(scCPU, 0,70,0,255, true),ofMap(scCPU, 0,70,255,0, true),0));
        ofDrawCircle(ofMap(ofNoise(noiseCount*0.001, noiseCount*0.003),0,1,0,400),
                     ofMap(ofNoise(noiseCount*0.004 , noiseCount*0.002),0,1,0,400),ofMap(scCPU, 0,100,2,15, true));
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

//--------------------------------------------------------------
//-----------  BPM ---------------------------------------------
//--------------------------------------------------------------
void WinBpm::setup(int padding, ofColor uiColor){
    this->uiColor = uiColor;
    this->padding = padding;
    bpmStringBox = font.getStringBoundingBox("BPM: 1000%", 0, 0); // size BPM string
    
    if (parameters.size()==0){
        parameters.setName("Bpm");
        parameters.add(size.set("BPM Box size", glm::vec2(200, 200), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));
        parameters.add(pos.set("BPM Box", glm::vec3(1480, 354, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
    }

}

void WinBpm::update(int bpm){
//    this->pos = cpuPos;
//    this->size = cpuSize;
    this->bpm = bpm;
}

void WinBpm::draw() {
    ofEnableAlphaBlending();
    int shadowLetter = 3;
    ofPushStyle();
    ofPushMatrix();

        Windo::drawWin(this->pos, this->size, this->uiColor);
        ofTranslate(this->pos);

        ofTranslate(ofClamp(size->x / 2 - bpmStringBox.width / 2, 0, size->x / 2), ofClamp(size->y / 2 + bpmStringBox.height / 2, 0, size->y / 2));//;
        ofSetColor(255, 190);

        ofSetColor(0, 120);
        font.drawString("BPM: " + ofToString(bpm), 0, 0); // CPU text
        ofSetColor(255);
        font.drawString("BPM: " + ofToString(bpm), 0 - shadowLetter, 0 - shadowLetter);

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

    if (parameters.size()==0){
        parameters.setName("integrity");
        parameters.add(pos.set("Integrity Box", glm::vec3(1480, 100, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
        parameters.add(size.set("Integrity size", glm::vec2(320, 100), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));
    }
    newText("");
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
        ofSetColor(ofMap(integrity,100,0,0,255), ofMap(integrity,100,0,255,0),0);
        font.drawString(targetText + "\n\n" + "COMPLETE: " + ofToString(100- this->integrity) + "%"
                + "\n" + nameModel, 0,0);
        ofEnableBlendMode(OF_BLENDMODE_DISABLED);
    ofPopMatrix();
    ofPopStyle();
}

void WinIntegrity::newText(string target){
    vector<string> textAction{
        "compiling", "destroying", "uploading", "sequencing", "generating", "revoking", "sending", "splicing", "abording",
        "accessing","refusing", "reseting", "removing", "cleaning", "recovering", "requesting", "seeking", "probing", "opening",
        "executing", "interpreting", "reading", "playing", "implementing", "corrupting", "linking", "leaking", "quarantine", "security", "initialize",
        "saving", "updating", "scanning", "secure", "allocating", "adding", "grabbing", "creating", "adjusting", "disrupting", "bending", "spinning", "tokenizing", "testing",
        "filtering", "cracking", "mining", "aesthesizing", "bureacritizing", "calculating", "compounding", "depixelating", "dicing", "gathering", "populating", "realigning",
        "scrubbing", "setting", "compressing", "synthesizing", "testing", "simulating", "mapping", "optimizing", "recycling", "activating" ,"encryting", "phishing", "spoofing",

    };
    vector<string> textTarget{
        "file", "archive", "memory", "libraries", "slot", "protocol", "address", "communication", "socket", "software",
        "connection", "structure", "I/O", "error", "destination", "state", "channel", "driver", "key","service", "argument", "code", "stream",
        "pipe", "resource", "range", "permission", "block", "data", "directory", "hardware", "CPU", "host", "kernel", "processor", "USB", "harddrive", "partition", "boot",
        "ACPIPCI", "wlan", "cache", "node", "event", "IRQ", "clock", "core", "hash", "energy", "shield", "time", "space", "z-axis", "life", "fuse", "web", "bitcoins", "system32", "RAM", "virus",
        "matrices", "probability", "message", "particle", "mesh","neural", "gravity", "simulation", "metavers", "underworld", "database", "chaos", "decimals", "binaries", "git", "package", "screen", "keyboard", "FAQ", "password",
        "login", "spyware", "trojan", "blacklist", "backup", "cookie", "firewall", "fan", "motherboard", "bandwidth", "algorithm", "cyberspace", "inbox", "path", "server", "backdoor", "zero-day", "DDoS", "brute force", "SSL", "bot",
        "rootkit", "worm",
};
    ofRandomize(textAction);
    //ofRandomize(textTarget);
    this->targetText = ofToUpper(textAction[0]) + "\n" + ofToUpper(target);
}

////-------------------------------------------------------------
//// HighScore

//--------------------------------------------------------------
void WinScore::setup(int padding, ofColor uiColor, vector<ofColor> playerColor){
    this->uiColor = uiColor;
    this->padding = padding;
    this->zbdmColor = playerColor[0];
    this->svdkColor = playerColor[1];
    this->serverColor = playerColor[2];

    if (parameters.size()==0){
        parameters.setName("HighScore");
        parameters.add(pos.set("Score Box", glm::vec3(1480, 230, 0), glm::vec3(0, 0, -500), glm::vec3(width, height, 500)));
        parameters.add(size.set("Score size", glm::vec2(320, 85), glm::vec2(0, 0), glm::vec2(width / 2, height / 2)));
    }
}

void WinScore::update(int svdkScore, int zbdmScore, int serverScore){
    this->svdkScore = svdkScore;
    this->zbdmScore = zbdmScore;
    this->serverScore = serverScore;
}

void WinScore::draw(){
    ofPushStyle();
    ofPushMatrix();
        Windo::drawWin(this->pos, this->size, this->uiColor);
        ofTranslate(pos->x + this->padding, pos->y + fontCharBox.height + padding, pos->z);
        ofEnableBlendMode(OF_BLENDMODE_MULTIPLY);
        // Svdk
        ofSetColor(svdkColor);
        font.drawString("SVDK: " + ofToString(this->svdkScore),0,0);
        ofTranslate(glm::vec2(0,1*(fontCharBox.height +5)));
        // Zbdm
        ofSetColor(zbdmColor);
        font.drawString("ZBDM: " + ofToString(this->zbdmScore),0,0);
        ofTranslate(glm::vec2(0,1*(fontCharBox.height +5)));
        // Server
        ofSetColor(serverColor);
        if (serverScore >0){
            font.drawString("SERVER: " + ofToString(this->serverScore),0,0);}
        ofEnableBlendMode(OF_BLENDMODE_DISABLED);
    ofPopMatrix();
    ofPopStyle();
}

void OverHeating::add(){
    if (vecOverWindow.size() >= maxWindow){
        vecOverWindow.erase(vecOverWindow.begin());
        vecStringError.erase(vecStringError.begin());
    }
    Windo newWin;
    newWin.size = glm::vec2(ofRandom(50,ofGetWidth()/2),ofRandom(50,ofGetHeight()/2));
    newWin.pos = glm::vec3(ofRandom(0, ofGetWidth() - newWin.size->x),
                           ofRandom(0, ofGetHeight() - newWin.size->y),
                           0);
    newWin.uiColor = ofColor(ofRandom(50,255), ofRandom(0,50), ofRandom(0,50));
    vecOverWindow.push_back(newWin);
    // generate string code error
    float maxWidth = newWin.size->x / newWin.fontCharBox.width;
    float maxHeight = newWin.size->y / newWin.fontCharBox.height;
    float maxNbrChar = ( maxWidth * maxHeight * 0.4);
    string generateString;
    for (u_int i=0; i< (int) maxNbrChar; i++){
        char ch = ofRandom(33,126);
        generateString.push_back(ch);
        }
    generateString = insertNewlines(generateString, (int) ofClamp((maxWidth - 3), 3.0,200.0));
    vecStringError.push_back(generateString);
}


void OverHeating::draw(){
    ofDisableAlphaBlending();
    ofDisableDepthTest();
    for (unsigned int i=0; i<vecOverWindow.size(); i++){
        vecOverWindow[i].drawWin(vecOverWindow[i].pos, vecOverWindow[i].size, vecOverWindow[i].uiColor);
        vecOverWindow[i].font.drawString(vecStringError[i],vecOverWindow[i].pos->x + 15, vecOverWindow[i].pos->y + 25);
    }
}

void OverHeating::drawEnding(int scCPU){
    ofPushMatrix();
    ofPushStyle();
    ofDisableAlphaBlending();
    ofDisableDepthTest();
    ofTranslate(ofGetWidth()/2 - fontBox.width/2, ofGetHeight()/2 - fontBox.height/2);
    if(ofGetFrameNum()%10==0){ofTranslate(ofRandom(-100,100), ofRandom(-100,100));}
    ofSetColor(ofColor::red);
    font.drawString("CPU: " + ofToString(scCPU) + " %", 0, 0);
    font.drawString("cp server.* /dev/null", 0, fontBox.height + 10);
    font.drawString("Garbage collector coming soon", 0, fontBox.height*2 + 20);
    font.drawString("Thank you everybody << end;", 0, fontBox.height*3 + 30);
    ofPopMatrix();
    ofPopStyle();
}

void OverHeating::clear(){
    vecOverWindow.clear();
    vecStringError.clear();
}

string Windo::insertNewlines(string in, const size_t every_n)
{
    string out;
    out.reserve(in.size() + in.size() / every_n);
    for (std::string::size_type i = 0; i < in.size(); i++) {
        if (!(i % every_n) && i) {
            out.push_back('\n');
        }
        out.push_back(in[i]);
    }
    return out;
}


string OverHeating::insertNewlines(string in, const size_t every_n)
{
    string out;
    out.reserve(in.size() + in.size() / every_n);
    for (std::string::size_type i = 0; i < in.size(); i++) {
        if (!(i % every_n) && i) {
            out.push_back('\n');
        }
        out.push_back(in[i]);
    }
    return out;
}


string Windo::textInjection(string textIn){
    char ch = ofRandom(33,126);
    textIn[ofRandom(0, textIn.length())] = ch;
    return textIn;
}


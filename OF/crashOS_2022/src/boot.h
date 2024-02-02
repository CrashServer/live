#pragma once
#ifndef BOOT_H
#define BOOT_H

//#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "ofTrueTypeFont.h"
#include "ofxSvg.h"

class Boot{
public:
    void setup();
    void update(int integrity);
    void draw();
    void resize();

    int width, height;
    int maxLine;
    int rtime, incr;
    glm::vec2 posIntegrity;

    ofxXmlSettings xml;
    ofTrueTypeFont font;
    ofRectangle fontCharBox;

    vector<string> bootLine, cBoot;

    string waitingMsg = "defaultMsg";
    bool bShowMsg = false;

    ofxSvg logoCrash;
    int _integrity;

    Boot();
private:

};

#endif // BOOT_H

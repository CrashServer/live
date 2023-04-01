#pragma once
#ifndef BOOT_H
#define BOOT_H

//#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "ofTrueTypeFont.h"
#include "ofxPostProcessing.h"

class Boot{
public:
    void setup();
    void update();
    void draw(int integrity);
    void resize();

    int width, height;
    int maxLine;
    int rtime, incr;
    glm::vec2 posIntegrity;

    ofxXmlSettings xml;
    ofTrueTypeFont font;
    ofRectangle fontCharBox;

    ofxPostProcessing post;

    vector<string> bootLine, cBoot;

    string waitingMsg = "defaultMsg";
    bool bShowMsg = false;

    Boot();
private:

};




#endif // BOOT_H

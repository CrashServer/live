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
    void draw();
    void resize();

    int width, height;
    int maxLine;
    int rtime, incr;
    ofxXmlSettings xml;
    ofTrueTypeFont font;
    ofRectangle fontCharBox;

    ofxPostProcessing post;


    vector<string> bootLine, cBoot;

    Boot();
private:

};




#endif // BOOT_H

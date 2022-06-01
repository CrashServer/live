#ifndef BOOT_H
#define BOOT_H

#include "ofMain.h"
#include "ofxXmlSettings.h"
#include "ofTrueTypeFont.h"
#include "ofxPostProcessing.h"

class Boot{
public:
    void setup();
    void update();
    void draw();

    int width, height;
    int maxLine;
    ofxXmlSettings xml;
    ofTrueTypeFont font;
    ofRectangle fontCharBox;

    ofxPostProcessing post;


    vector<string> bootLine, cBoot;

    Boot();
private:

};

#endif // BOOT_H

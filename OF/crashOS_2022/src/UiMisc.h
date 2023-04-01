#pragma once
#ifndef UIMISC_H
#define UIMISC_H

//#include "ofMain.h"
#include "ofxImageSequencePlayback.h"

class UiMisc {
public:
    // methods
    void setup(string textPres, glm::vec2 textPresPos);
    void update(bool blogo);
    void draw(bool blogo, bool isServerActive=false);
    void changeLogo(int index=0);
    void resize();

    // variables
    int width, height;
    int logoWidth, logoHeight;

    glm::vec3 pos, posAlert;
    glm::vec2 size, sizeAlert;

    ofxImageSequencePlayback logo;
    ofFbo uiFbo;
    ofxImageSequencePlayback alert;

    ofTrueTypeFont font;
    string textPres;
    glm::vec2 textPresPos;

    int logoIndex=0;

    // constructor
    UiMisc();

private:
};

#endif // UIMISC_H

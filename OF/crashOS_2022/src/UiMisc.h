#pragma once
#ifndef UIMISC_H
#define UIMISC_H

#include "ofMain.h"
#include "ofxImageSequencePlayback.h"

class UiMisc {
public:
    // methods
    void setup();
    void update(bool blogo);
    void draw(bool blogo, bool isServerActive=false);
    void changeLogo(int index=0);

    // variables
    int width, height;
    int logoWidth, logoHeight;

    glm::vec3 pos;
    glm::vec2 size;

    ofxImageSequencePlayback logo;
    ofFbo uiFbo;
    ofxImageSequencePlayback alert;

    // constructor
    UiMisc();

private:
};

#endif // UIMISC_H

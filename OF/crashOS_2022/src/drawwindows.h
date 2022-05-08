#pragma once
#ifndef DRAWWINDOWS_H
#define DRAWWINDOWS_H

#include "ofMain.h"
#include "ofTrueTypeFont.h"
#include "ofxGui.h"

class Windo {
public:
    void drawWin(glm::vec3 winPos, glm::vec2 winSize, ofColor uiColor);

    int width, height;
    int padding;
    ofColor uiColor;
    ofTrueTypeFont font;

    // Gui window
    //ofxPanel gui;
    ofParameterGroup parameters;
    ofParameter<glm::vec3> pos;
    ofParameter<glm::vec2> size;

    int paddingWindow;
    ofRectangle fontCharBox;

//    glm::vec3 pos;
//    glm::vec2 size;

    Windo();

private:
};

class WinCode : public Windo{
public:
    void setup(int padding = 10, ofColor uiColor=ofFloatColor::blue);
    void update(vector<string> vectorCode);
    void draw(vector<string> vectorCode, vector<char> vectorSymbol);

    ofParameter<int> nbrLineCode;


    //int nbrLineCode;
    int codeTotalHeight, codeTotalWidth;
    int maxLineCode, maxCodeWidth;

    ofFbo codeFbo;

private:

};

class WinCpu : public Windo{
public:
    void setup(int padding = 10, ofColor uiColor=ofFloatColor::blue);
    void update(int scCPU);
    void draw();


    ofRectangle cpuStringBox;
    ofFbo cpuFbo;
    int noiseCount;

    float scCPU;

private:
};

class WinIntegrity : public Windo{
public:
    void setup(int padding = 10, ofColor uiColor=ofFloatColor::blue);
    void update(int integrity, string nameModel=" ");
    void draw();

    int integrity;
    string nameModel;
    ofFbo integrityFbo;

private:
};



#endif // DRAWWINDOWS_H



#pragma once
#ifndef DRAWWINDOWS_H
#define DRAWWINDOWS_H

//#include "ofMain.h"
#include "ofTrueTypeFont.h"
#include "ofxGui.h"
#include "Getdata.h"

class Windo {
public:
    void drawWin(glm::vec3 winPos, glm::vec2 winSize, ofColor uiColor);
    void resize();
    string insertNewlines(string in, const size_t every_n);

    int width, height;
    int padding;
    ofColor uiColor;
    ofTrueTypeFont font;

    // Gui window
    //ofxPanel gui;
    ofParameterGroup parameters;
    ofParameter<glm::vec3> pos;
    ofParameter<glm::vec2> size;

    vector <CodeLine> vecCode;

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
    void update(vector<CodeLine> &vectorCode);
    void draw(vector<CodeLine>& vectorCode);


    ofParameter<int> nbrLineCode;


    //int nbrLineCode;
    int codeTotalHeight, codeTotalWidth;
    int maxLineCode, maxCodeWidth;

//    ofFbo codeFbo;

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

class OverHeating{
public:
    //void setup();
    //void update();
    void draw();
    void add();
    void clear();
    void drawEnding(int scCPU);
    string insertNewlines(string in, const size_t every_n);

    bool isOverheating;
    float initTime;
    int maxWindow = 100;
    vector <Windo> vecOverWindow;
    vector <string> vecStringError;

    ofTrueTypeFont font;
    ofRectangle fontBox;


    OverHeating();
private:
};


#endif // DRAWWINDOWS_H



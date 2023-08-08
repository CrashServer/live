#pragma once
#ifndef GETDATA_H
#define GETDATA_H

//#include "ofMain.h"
#include "ofxOsc.h"
#include "ofxNetwork.h"
#define PORTOSC 20000 // OSC

class CodeLine {
public:
    glm::vec3 pos;
    string code;
    char symbol;
    int typeCodePos;

    CodeLine();
private:
};

class CodeInstant {
public:
    string name;
    string code;
    int posMark;

    CodeInstant();
private:
};


class Data {
public:
    // methods
    void setup(string troopIp="127.0.0.1", int troopPort=2887, int arduinoPort=0, bool bvideoFox=false);
    void update();
    void draw();
    void detectServerActivity();
    bool isNumber(const string& s);
    void sendOSC(string adress, vector<string> param);
    int setScene(string sceneMsg);
    void setCodeWidth(string code);

    // test Routine
    void testCpu();
    void testArduino();
    void testOsc();

    // Gui Test
    ofParameterGroup parameters;
    ofParameter<bool> lightTest, cpuTest, arduinoTest, oscTestZbdm, oscTestSvdk, dmxTest, buttonTest;
    ofParameter<void> button;

    // variables
    int width, height;
    int maxLineCode;
    int scene=0;

    ofxOscReceiver oscReceiver;
    ofxOscSender oscSender;
    float scCPU;
    vector<CodeLine> vectorCode;
    vector<CodeInstant> vectorInstant; // containt instant code [0] zbdm [1] svdk
//    vector<char> vectorSymbol;
    char bang;

    ofSerial serial;
    bool barduino, bvideoFox;
    int arduinoPort;
    bool isServerActive, testButton;
    char prevButton = 'c';

    // video osc
    float vidpos1 = 0.0;
    float vidpos2 = 0.0;
    int vidid1 = 0;
    int vidid2 = 0;
    int vidblend1 = 255;
    int vidblend2 = 55;

    int delayServerActivity= 0;
    int serverInitTimer = 300;

    // constructor
    Data();

private:
};





#endif // GETDATA_H

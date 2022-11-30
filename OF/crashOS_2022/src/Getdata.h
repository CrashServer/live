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
    void setup(bool barduino=false);
    void update();
    void draw();
    void detectServerActivity();
    bool isNumber(const string& s);
    int setScene(string sceneMsg);

//    string insertNewlines(string in, const size_t every_n);

    // variables
    int width, height;
    int maxLineCode;
    int scene=0;

    ofxOscReceiver oscReceiver;
    float scCPU;
    vector<CodeLine> vectorCode;
    vector<CodeInstant> vectorInstant; // containt instant code [0] zbdm [1] svdk
//    vector<char> vectorSymbol;
    char bang;

    ofSerial serial;
    bool barduino;
    bool isServerActive;

    int delayServerActivity= 0;
    int serverInitTimer = 300;

    // constructor
    Data();

private:
};





#endif // GETDATA_H

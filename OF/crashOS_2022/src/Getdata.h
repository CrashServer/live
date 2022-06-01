#pragma once
#ifndef GETDATA_H
#define GETDATA_H

#include "ofMain.h"
#include "ofxOsc.h"
#include "ofxNetwork.h"

#define PORTOSC 20000 // OSC

class Data {
public:
    // methods
    void setup(bool barduino=false);
    void update(int cpuStress, int maxCodeWidth);
    void draw();
    void detectServerActivity();

    string insertNewlines(string in, const size_t every_n);

    // variables
    int width, height;
    int maxLineCode;

    ofxOscReceiver oscReceiver;
    float scCPU;
    vector<string> vectorCode;
    vector<char> vectorSymbol;
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

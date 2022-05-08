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
    void setup();
    void update(int cpuStress, int maxCodeWidth);
    void draw();

    string insertNewlines(string in, const size_t every_n);

    // variables
    int width, height;
    int maxLineCode;

    ofxOscReceiver oscReceiver;
    ofSerial serial;
    float scCPU;
    vector<string> vectorCode;
    vector<char> vectorSymbol;
    char bang;


    // constructor
    Data();

private:
};



#endif // GETDATA_H

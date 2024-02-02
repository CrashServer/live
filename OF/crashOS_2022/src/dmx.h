#pragma once
#ifndef DMX_H
#define DMX_H

#include "ofMain.h"
#include "ofxGenericDmx.h"

#define DMX_DATA_LENGTH 494

class Dmx{
public:
    void setup(int dmxAddr1, int dmxAddr2);
    void update(ofColor dmx1, ofColor dmx2);
    void exit();

    DmxDevice* dmxInterface_;
    unsigned char dmxData_[DMX_DATA_LENGTH];

    int dmxAddr1, dmxAddr2;
    bool opened;

    Dmx();

private:

};

#endif // DMX_H

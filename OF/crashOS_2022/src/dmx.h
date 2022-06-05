#pragma once
#ifndef DMX_H
#define DMX_H

#include "ofMain.h"
#include "ofxGenericDmx.h"

#define DMX_DATA_LENGTH 494

class Dmx{
public:
    void setup();
    void update(ofColor dmx1, ofColor dmx2);
    void exit();

    DmxDevice* dmxInterface_;
    unsigned char dmxData_[DMX_DATA_LENGTH];

    Dmx();

private:

};

#endif // DMX_H

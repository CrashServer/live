#pragma once
#ifndef AUDIO_H
#define AUDIO_H

#include "ofMain.h"
#include "fft.h"
#include "ofxBeat.h"

#define BUFFER_SIZE 256 //1024
#define NUM_WINDOWS 4

class AudioFft : public ofBaseApp {
public:
    // methods
    void setup();
    void update();
    void draw();
//    void audioIn(ofSoundBuffer &input);
    void audioReceived(float*, int, int);

    ofxBeat beat;

    // variables
//    float rmsAudio =0.0;

    ofSoundStream soundStream;

//    fft myFft;
//    float magnitude[BUFFER_SIZE];
//    float phase[BUFFER_SIZE];
//    float power[BUFFER_SIZE];

//    float freq[NUM_WINDOWS][BUFFER_SIZE/2];
//    float freq_phase[NUM_WINDOWS][BUFFER_SIZE/2];
//    float * left;
//    float * right;
//    int bufferCounter;

    int width, height;

    // constructor
    AudioFft();

private:
};




#endif // AUDIO_H

#include "Audio.h"
#include "ofApp.h"

AudioFft::AudioFft(){
}

void AudioFft::setup(){
    width = ofGetWidth();
    height = ofGetHeight();

    ofSoundStreamSettings settings;
#ifdef TARGET_LINUX
    settings.setApi(ofSoundDevice::Api::PULSE);
#endif

#ifdef TARGET_WIN32
    settings.setApi(ofSoundDevice::Api::MS_DS);
#endif

    settings.setInListener(this);
    settings.sampleRate = 44100;
    settings.numOutputChannels = 2;
    settings.numInputChannels = 2;
    settings.bufferSize = BUFFER_SIZE;
    soundStream.setup(settings);

    left = new float[BUFFER_SIZE];
    right = new float[BUFFER_SIZE];
    for (int i = 0; i < NUM_WINDOWS; i++){
        for (int j = 0; j < BUFFER_SIZE/2; j++){
                freq[i][j] = 0;
                }
            }
}

void AudioFft::update(){
    static int index=0;
    float avg_power = 0.0f;

    if(index < NUM_WINDOWS)
        index += 1;
    else
        index = 0;

    /* do the FFT	*/
    myFft.powerSpectrum(0,(int)BUFFER_SIZE/2, left,BUFFER_SIZE,&magnitude[0],&phase[0],&power[0],&avg_power);

    /* start from 1 because mag[0] = DC component */
    /* and discard the upper half of the buffer */
    for(int j=1; j < BUFFER_SIZE/2; j++) {
        freq[index][j] = magnitude[j];
    }
}

void AudioFft::draw(){
    ofPushMatrix();
    ofPushStyle();
        ofTranslate(0, height/2);
        ofSetLineWidth(3);
        ofSetColor(245,58,135);

        /* draw the FFT */
        for (int i = 1; i < (int)(BUFFER_SIZE/2); i++){
            ofDrawLine(200+(i*8),400,200+(i*8),400-magnitude[i]*10.0f);
        }
        ofTranslate(width/2,0);
        ofDrawCircle(0,0, rmsAudio*200);

    ofPopMatrix();
    ofPopStyle();
}

void AudioFft::audioIn(ofSoundBuffer &input){
    float rms = 0.0;
    int numCounted =0;
    for (int i = 0; i < input.getNumFrames(); i++){
            left[i] = input[i*2];
            right[i] = input[i*2+1];
            rmsAudio += left[i]*left[i];
            rmsAudio += right[i]*right[i];
            numCounted += 2;
        }
        rmsAudio /= (float)numCounted;
        rmsAudio = sqrt(rmsAudio);
}




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
    settings.numOutputChannels = 0;
    settings.numInputChannels = 2;
    settings.bufferSize = BUFFER_SIZE;
    settings.numBuffers = 4;
    soundStream.setup(settings);

//    left = new float[BUFFER_SIZE];
//    right = new float[BUFFER_SIZE];
//    for (int i = 0; i < NUM_WINDOWS; i++){
//        for (int j = 0; j < BUFFER_SIZE/2; j++){
//                freq[i][j] = 0;
//                }
//            }
}

void AudioFft::update(){
    beat.update(ofGetElapsedTimeMillis());
    //    static int index=0;
//    float avg_power = 0.0f;

//    if(index < NUM_WINDOWS)
//        index += 1;
//    else
//        index = 0;

//    /* do the FFT	*/
//    myFft.powerSpectrum(0,(int)BUFFER_SIZE/2, left,BUFFER_SIZE,&magnitude[0],&phase[0],&power[0],&avg_power);

//    /* start from 1 because mag[0] = DC component */
//    /* and discard the upper half of the buffer */
//    for(int j=1; j < BUFFER_SIZE/2; j++) {
//        freq[index][j] = magnitude[j];
//    }
}

void AudioFft::draw(){
    ofPushMatrix();
    ofPushStyle();
        ofSetLineWidth(3);
        ofSetColor(245,58,135);

        /* draw the FFT */
        for (int i = 1; i < 32; i++){
            ofSetColor(145,58,135);
            ofDrawRectangle(i*width/32, height/2, width/32 -15, beat.getBand(i)*-height/3);
            ofSetColor(255);
            ofDrawBitmapString(ofToString(i), i*width/32 + 30, height*1/3);
        }
        ofSetColor(ofColor::darkBlue);
        ofTranslate(width/2,height/2);
        ofDrawCircle(0,0, beat.isSnare()*200);
        ofSetColor(ofColor::azure);
        ofDrawRectangle(0,0, beat.isKick()*200, beat.isKick()*200);
        ofSetColor(ofColor::burlyWood);
        ofDrawRectangle(-50,50, 60, beat.isHat()*150);


    ofPopMatrix();
    ofPopStyle();
}

void AudioFft::audioReceived(float* input, int bufferSize, int nChannels) {
    beat.audioReceived(input, bufferSize, nChannels);
}


//void AudioFft::audioIn(ofSoundBuffer &input){
//    float rms = 0.0;
//    int numCounted =0;
//    for (int i = 0; i < input.getNumFrames(); i++){
//            left[i] = input[i*2];
//            right[i] = input[i*2+1];
//            rmsAudio += left[i]*left[i];
//            rmsAudio += right[i]*right[i];
//            numCounted += 2;
//        }
//        rmsAudio /= (float)numCounted;
//        rmsAudio = sqrt(rmsAudio);
//}




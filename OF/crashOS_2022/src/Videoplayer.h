#pragma once
#ifndef VIDEOPLAYER_H
#define VIDEOPLAYER_H

//#include "ofMain.h"
#include "ofxImageSequencePlayback.h"

class Videoplayer {
public:
    // methods
    void setup();
    void update(int _videoCat=0, int integrity=100);
    void draw();
    void newSeq();
    void videoSrcub();
    void resize();


    // variables
    ofxImageSequencePlayback mySequence;

    string videoPath="video/";
    ofDirectory videoCat; // dir of category
    ofDirectory videoDir; // dir of video

    int vidCat;
    int vidId;
    float vidFps;
    ofFbo videoFbo, fxFbo;
    int width, height;

    bool bthread=false, bnewSeq=false;
    int integrity;
    vector<glm::vec2> vecGlitch;

    glm::vec3 pos;
    glm::vec2 size;


    // constructor
    Videoplayer();

private:
};

class Videoplayer3d : public Videoplayer {
public:
    void setup3d();
    void update3d(int _videoCat, int integrity, float audioRms);
    void draw3d();

    // 3D
    ofVboMesh mesh;
    ofImage image;
    ofPixels fboPixels;

private:
    int W = 100; //Grid size
    int H = 100;
    int meshSize = 20;
};



#endif // VIDEOPLAYER_H

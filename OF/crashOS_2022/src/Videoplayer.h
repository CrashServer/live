#pragma once
#ifndef VIDEOPLAYER_H
#define VIDEOPLAYER_H

#include "ofMain.h"
#include "ofxImageSequencePlayback.h"

class Videoplayer {
public:
    // methods
    void setup();
    void update(int _videoCat=0, bool b3d=false, float audioRms=1);
    void draw(bool b3d=false);
    void newSeq();
    void videoSrcub();

    void update3d(float audioRms);
    void draw3d();

    // variables
    ofxImageSequencePlayback mySequence;

    ofDirectory videoDir;
    ofDirectory videoGrp;
    ofDirectory vid;
    int vidCat;
    int vidId;
    ofFbo videoFbo;
    int width, height;
    int alpha;

    bool bthread;

    glm::vec3 pos;
    glm::vec2 size;

    // 3D
    ofMesh mesh;
    ofImage image;
    ofPixels fboPixels;

    // constructor
    Videoplayer();

private:
    int W = 200; //Grid size
    int H = 200;
    int meshSize = 6;
};



#endif // VIDEOPLAYER_H

#pragma once
#ifndef VIDEOPLAYER_H
#define VIDEOPLAYER_H

//#include "ofMain.h"
#include "ofxImageSequencePlayback.h"

class Videoplayer {
public:
    // methods
    void setup();
    void update(int integrity=100, bool b3d=false, float audioRms=1);
    void draw(bool b3d=false);
    void newSeq();
    void newSeq(int _vidCat);
    void videoSrcub();
    void setupIndex();
    void resize();

    void update3d(float audioRms);
    void draw3d();

    // variables
    ofxImageSequencePlayback mySequence;

//    ofDirectory videoDir; //-> category
//    ofDirectory videoGrp; //-> dir

    ofDirectory videoCat; // dir of category
    ofDirectory videoDir; // dir of video
    vector <int> vecVideoCat; // store category to track empty
    vector <vector <int>> vecVideoDirIdx; // store videos sequence for each category


    int vidCat;
    int vidId;
    float vidFps;
    ofFbo videoFbo, fxFbo;
    int width, height;

    bool bthread;
    int integrity;
    vector<glm::vec2> vecGlitch;


    glm::vec3 pos;
    glm::vec2 size;

    // 3D
    ofVboMesh mesh;
    ofImage image;
    ofPixels fboPixels;

    // constructor
    Videoplayer();

private:
    int W = 100; //Grid size
    int H = 100;
    int meshSize = 20;
};



#endif // VIDEOPLAYER_H

#pragma once
#ifndef VIDEOPLAYERHAP_H
#define VIDEOPLAYERHAP_H

#include "ofxHapPlayer.h"

class VideoPlayerHap {
public:
    void setup(string path="videoHap/");
    void update();
    void draw();
    void newSeq();
    void newCat(int index);
    void videoScrub(float audioRms=0);

    ofxHapPlayer hapPlayer;
    string videoPath;
    ofDirectory videoDir, videoList; // list all directory - list all video

    int vidIndex; // index of the actual video
    int vidDirIndex; // index of the actual folder
    int vidTotal;

    int width, height;
    glm::vec3 pos;
    glm::vec2 size;

    VideoPlayerHap();
};


#endif // VIDEOPLAYERHAP_H

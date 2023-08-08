//#include "ofApp.h"
#include "VideoplayerHap.h"

VideoPlayerHap::VideoPlayerHap(){
}

void VideoPlayerHap::setup(string path){
    this->videoPath = path;
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    vidDirIndex = 0;

    // list all directories
    videoDir.listDir(videoPath);
    videoDir.sort();

    videoList.listDir(videoDir.getPath(vidDirIndex));
    videoList.sort();
    vidIndex = 0;
    vidTotal = videoList.size();
    string videoActual = videoList.getPath(0);
    filename = ofFilePath::removeExt(ofFilePath::getFileName(videoActual));

    ofSetVerticalSync(true);
    ofBackground(0,0,0);

    hapPlayer.load(videoActual);
    hapPlayer.setLoopState(OF_LOOP_NORMAL);
    hapPlayer.setSpeed(1);
    hapPlayer.setPaused(false);

    vidpos = 0.0;
}

void VideoPlayerHap::update(float vidpos, int vidid){
    if (vidpos != this->vidpos){
        hapPlayer.setPosition(vidpos);
        this->vidpos = vidpos;
    }
    if (vidid != vidIndex){
        vidIndex = vidid - 1;
        //newSeq();
    }
}


void VideoPlayerHap::draw(){
    //ofEnableAlphaBlending();

    if (hapPlayer.isLoaded()){
        //ofRectangle videoRect(0, 0, hapPlayer.getWidth(), hapPlayer.getHeight());
        //videoRect.scaleTo(ofGetWindowRect());
        hapPlayer.draw(this->pos.x, this->pos.y, this->size.x, this->size.y);

    }
    else
    {
        if (hapPlayer.getError().length())
        {
            ofDrawBitmapStringHighlight(hapPlayer.getError(), 20, 20);
        }
        else
        {
            ofDrawBitmapStringHighlight("Movie is loading...", 20, 20);
        }
    }

}

void VideoPlayerHap::newCat(int index){
    // change video category (folder) based on index
    if (index != (vidDirIndex%(videoDir.size()-1))){
        vidDirIndex = index;
        videoDir.listDir(videoPath);
        videoDir.sort();
        //cout << "index : " << ofToString(vidDirIndex%(videoDir.size())) << endl;
        videoList.listDir(videoDir.getPath(vidDirIndex%(videoDir.size())));
        videoList.sort();
        vidTotal = videoList.size();
        vidIndex = -1;
        this->newSeq();
    }
}

void VideoPlayerHap::newSeq(){
    // load a new video sequence from current directory
    vidIndex++;
    vidIndex = ofClamp(vidIndex, 0, vidTotal-1);
    string videoActual = videoList.getPath(vidIndex);
    filename = ofFilePath::removeExt(ofFilePath::getFileName(videoActual));
    hapPlayer.load(videoActual);
}

void VideoPlayerHap::videoScrub(float audioRms){
    if (audioRms==0){
        hapPlayer.setPosition(ofRandom(0,1));
    }
    else{
        if(audioRms>0.1){
            hapPlayer.setPosition(ofMap(audioRms,0,4,0,1));
        }
    }
}

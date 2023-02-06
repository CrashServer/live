//#include "ofApp.h"
#include "VideoplayerHap.h"

VideoPlayerHap::VideoPlayerHap(){
}

void VideoPlayerHap::setup(){
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);

    // list all directories
    videoDir.listDir(videoPath);
    videoDir.sort();

    videoList.listDir(videoDir.getPath(0));
    videoList.sort();
    vidIndex = 0;
    vidTotal = videoList.size();
    string videoActual = videoList.getPath(0);

    ofSetVerticalSync(true);
    ofBackground(0,0,0);

    hapPlayer.load(videoActual);
    hapPlayer.setLoopState(OF_LOOP_NORMAL);
    hapPlayer.setSpeed(1);
    hapPlayer.setPaused(false);

    hapPlayer2.load("videoHap/1/fire1.mov");
    hapPlayer2.setLoopState(OF_LOOP_NORMAL);
    hapPlayer2.setSpeed(1);
    hapPlayer2.setPaused(false);
}

void VideoPlayerHap::update(){

}


void VideoPlayerHap::draw(){
    ofEnableAlphaBlending();

    if (hapPlayer.isLoaded()){
        ofSetColor(255, 255, 255);
        ofRectangle videoRect(0, 0, hapPlayer.getWidth(), hapPlayer.getHeight());
        videoRect.scaleTo(ofGetWindowRect());
        ofRectangle videoRect2(0, 0, hapPlayer2.getWidth(), hapPlayer2.getHeight());
        videoRect2.scaleTo(ofGetWindowRect());
        hapPlayer.draw(videoRect.x, videoRect.y, videoRect.width, videoRect.height);
        hapPlayer2.draw(videoRect2.x, videoRect2.y, videoRect2.width, videoRect2.height);
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

void VideoPlayerHap::newSeq(){
    vidIndex++;
    vidIndex = ofClamp(vidIndex, 0, vidTotal-1);
    string videoActual = videoList.getPath(vidIndex);
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

#include "glitcher.h"

Glitcher::Glitcher(){
}

void Glitcher::setup(ofFbo &targetFbo){
    width = targetFbo.getWidth();
    height = targetFbo.getHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    glitcherFbo.allocate(size.x, size.y, GL_RGBA);
}

void Glitcher::update(ofFbo &targetFbo, float trigger){
    ofPushStyle();
    glitcherFbo.begin();
        //ofSetColor(col);
        if (trigger == 0){trigger= ofRandom(0,100)/100;}
        if (trigger >= 0.5) {
            for (int i=0; i<500; i++){
                ofSetColor(ofRandom(0, 255), ofRandom(150, 255));
                ofDrawRectangle(ofRandom(0,size.x), ofRandom(0,size.y),10,50);
                }
         }
         else if (trigger >= 0.20) {
             glitcherFbo.allocate(ofRandom(20, (int) size.x), ofRandom(50, size.y), GL_RGBA);
             ofSetColor(ofRandom(0, 255), ofRandom(0, 255), ofRandom(0, 255));
         }
         else {
             targetFbo.draw(pos.x,pos.y, size.x, size.y);
             }


        targetFbo.draw(pos.x,pos.y,size.x,size.y);
    ofPopStyle();
    glitcherFbo.end();
}

void Glitcher::draw(glm::vec3 vecPos, glm::vec2 vecSize, bool alpha){
    if (alpha){ofEnableBlendMode(OF_BLENDMODE_ADD);}
    glitcherFbo.draw(vecPos.x,vecPos.y, vecSize.x, vecSize.y);
    ofDisableBlendMode();
}

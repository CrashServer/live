#include "ofApp.h"
#include "UiMisc.h"

UiMisc::UiMisc(){
}

void UiMisc::setup(){
    width = ofGetWidth();
    height = ofGetHeight();
    logo.loadSequence("ui/crashos0/", 24.0f);
    logo.setShouldLoop(true);
    logo.play();

    alert.loadSequence("ui/alert/", 24.0f);
    alert.setShouldLoop(true);
    alert.play();

    size = glm::vec2(logo.mSequence.getWidth(),logo.mSequence.getHeight());
    pos = glm::vec3(width / 2 - size.x/2, 0,0);
    uiFbo.allocate(size.x, size.y, GL_RGBA);
}

void UiMisc::update(bool blogo){
    if (blogo){
        logo.update();
        uiFbo.begin();
        if(logo.mSequence.isLoaded()){
            logo.draw();}
        uiFbo.end();
    }
}

void UiMisc::draw(bool blogo, bool isServerActive){
    if (blogo){
        ofPushMatrix();
        ofPushStyle();
        ofEnableBlendMode(OF_BLENDMODE_SCREEN);

            ofTranslate(pos.x, pos.y); // logo is 600 pixels, take half
            uiFbo.draw(0,0,size.x, size.y);

        ofEnableBlendMode(OF_BLENDMODE_DISABLED);
        ofPopMatrix();
        ofPopStyle();
    }

    /// Alert logo
    if (isServerActive){
        ofPushMatrix();
        ofPushStyle();
        ofEnableBlendMode(OF_BLENDMODE_SCREEN);
            ofTranslate(width/2, height/2);
            alert.update();
            alert.draw();
        ofDisableBlendMode();
        ofPopMatrix();
        ofPopStyle();
    }

}

void UiMisc::changeLogo(int index){
    if (index==0){
        index = ofRandom(0,3);
    }

    switch (index) {
    case 0:
        logo.loadSequence("ui/crashos0/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 1:
        logo.loadSequence("ui/crashos1/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 2:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;


    default:
        logo.loadSequence("ui/crashos0/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    }



}


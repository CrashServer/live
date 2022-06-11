#include "ofApp.h"
#include "UiMisc.h"
#include "ofTrueTypeFont.h"

UiMisc::UiMisc(){
}

void UiMisc::setup(string textPres, glm::vec2 textPresPos){
    width = ofGetWidth();
    height = ofGetHeight();
    font.load("ui/font/pixe.ttf", 24);
    this->textPres = textPres;
    this->textPresPos = textPresPos;

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

    // Draw text description
    if (this->textPres.size()>1){
        ofPushMatrix();
        ofTranslate(textPresPos);
            font.drawString(textPres,0,0);
        ofPopMatrix();
    }
}

void UiMisc::changeLogo(int index){
    if (index!=logoIndex){
        logoIndex = index;
    if (index==0){
        index = ofRandom(0,10);
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
    case 3:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 4:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 5:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 6:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 7:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 8:
        logo.loadSequence("ui/crashos2/", 24.0f);
        logo.setShouldLoop(true);
        logo.play();

        logoWidth = logo.mSequence.getWidth();
        logoHeight = logo.mSequence.getHeight();
        uiFbo.allocate(logoWidth, logoHeight, GL_RGBA);
        break;
    case 9:
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
}

void UiMisc::resize(){
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(width / 2 - size.x/2, 0,0);
}


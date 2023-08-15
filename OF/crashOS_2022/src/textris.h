#pragma once
#ifndef TEXTRIS_H
#define TEXTRIS_H

#include "ofTrueTypeFont.h"
#include "ofxBox2d.h"

#define FFT_BANDS 16

class CustomBox : public ofxBox2dRect {
//string oscText;
ofColor color;
float boxWidth;
float boxHeight;
vector <string> textVect;

public:
    CustomBox(b2World * world, float x, float y, float _boxWidth, float _boxHeight, vector<string> _textVect, ofColor textColor) {
        textVect = _textVect;
        boxWidth = _boxWidth;
        boxHeight = _boxHeight;
        //setPhysics(ofRandom(0.1,5.0), ofRandom(0.1,1), 0.3);
        setPhysics(3.0, 0.53, 0.1);
        setup(world, x, y, boxWidth, boxHeight);
        setVelocity(ofRandom(-30,30), ofMap(textVect.size(), 1,120,3000,-3000, true));
        color.set(textColor);
    }

void draw(ofTrueTypeFont * fontref) {
    ofPushMatrix();
    ofTranslate(getPosition());
    ofRotateDeg(getRotation());
    ofSetColor(color);
    ofNoFill();
    ofSetRectMode(OF_RECTMODE_CENTER);
    ofSetLineWidth(4);
    ofDrawRectangle(0,0,boxWidth, boxHeight);
    ofSetRectMode(OF_RECTMODE_CORNER);
    ofTranslate(-boxWidth/2, -boxHeight/2 + fontref->getLineHeight() +5);
    float y = 0;
        for (auto& l : textVect){
            fontref->drawString(l, 10, y);
            y += fontref->getLineHeight();
        }

    ofPopMatrix();
}
};

class particle {
public:
    ofColor particleColor;
    float size;
    int hue;
    bool isDead;
    glm::vec2 force, position, direction;

    particle(int x, int y);
    ~particle();

    void update();
    void draw();
};

class Textris{
  public:
    ofxBox2d box2d;
    vector <shared_ptr<CustomBox> > rectangles, fftRectangle;
    ofRectangle rect, fftrect;

    const int maxBox = 40; // nbr of maximum osc message box
    const int padding = 10; // box padding-
    int boxErase = 0;
    const int maxParticles = 5000;

    string msgTxt;
    vector <string> textVect;
    ofColor zbdmColor, svdkColor, serverColor;
    ofTrueTypeFont font;

    vector<particle> particles;
    vector<float> fftBand;

//    ofPolyline groundLine;
    ofxBox2dEdge ground;

    string insertNewlines(string in, const size_t every_n);

    void setup(vector<ofColor> playerColor=vector<ofColor>{ofColor::paleTurquoise, ofColor::greenYellow, ofColor::red});
    void update();
    void draw();
    void addText(string textrisText, char player);
    void clear();

    Textris();
};


#endif // TEXTRIS_H

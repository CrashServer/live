#pragma once
#ifndef TEXTRIS_H
#define TEXTRIS_H

#include "ofTrueTypeFont.h"
#include "ofxBox2d.h"

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
        setVelocity(ofMap(textVect.size(), 1,30,30,-30, true), ofMap(textVect.size(), 1,30,30,-30, true));
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
            fontref->drawString(l, 5, y);
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
    vector <shared_ptr<CustomBox> > rectangles;
    ofRectangle rect;
    const int maxBox = 40; // nbr of maximum osc message box
    const int padding = 10; // box padding-
    int boxErase = 0;
    const int maxParticles = 5000;

    string msgTxt;
    vector <string> textVect;
    ofColor zbdmColor, svdkColor, serverColor;
    ofTrueTypeFont font;

    vector<particle> particles;

    string insertNewlines(string in, const size_t every_n);

    void setup(vector<ofColor> playerColor=vector<ofColor>{ofColor::paleTurquoise, ofColor::greenYellow, ofColor::red});
    void update();
    void draw();
    void addText(string textrisText, char player);
    void clear();

    Textris();
};


#endif // TEXTRIS_H

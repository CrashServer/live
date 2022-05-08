#pragma once
#ifndef GLITCH_H
#define GLITCH_H
#include "ofMain.h"

class Glitcher {
public:
    // methods
    void setup(ofFbo &targetFbo);
    void update(ofFbo &targetFbo, float trigger=0);
    void draw(glm::vec3 vecPos, glm::vec2 vecSize, bool alpha=false);

    // variables
    ofFbo glitcherFbo;
    int width, height;

    glm::vec3 pos;
    glm::vec2 size;

    // constructor
    Glitcher();

private:
};



#endif // GLITCH_H

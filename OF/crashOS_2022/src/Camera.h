#pragma once
#ifndef CAMERA_H
#define CAMERA_H

#include "ofMain.h"
#include "drawwindows.h"

class Camera {
public:
    // methods
    void setup(ofColor uiColor);
    void update();
    void draw();
    void resize(glm::vec2 &);

    // variables
    int width;
    int height;

    ofParameterGroup parameters;
    ofParameter<glm::vec3> pos;
    ofParameter<glm::vec2> size;

    ofVideoGrabber webcam;
    ofFbo camFbo;

    ofColor uiColor;
    Windo cameraWin;

    // constructor
    Camera();

private:
};

#endif // CAMERA_H

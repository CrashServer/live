#pragma once
#ifndef RENDER_H
#define RENDER_H
#include "ofMain.h"
#include "ofxAssimpModelLoader.h"

class Render {
public:
    void setup();
    void update(int targetID=0);
    void draw();

    int width, height;
    glm::vec3 pos;
    glm::vec2 size;

    ofFbo renderFbo;

    ofParameterGroup parameters;
    ofParameter<int> targetMeshSlider;
    ofParameter<int> currentModelSubAttack;

    ofLight pointLight;

    ofxAssimpModelLoader targetModel;
//    ofVboMesh targetMesh;
    ofMaterial materialMesh, materialAttack;

    vector<string> currentModelSubNames;
    int currentTargetID = 0;
    string currentText;
    Render();

private:
};

class ProcBackground {
public:
    void setup();
    void update();
    void draw();

    int width, height;

    int intId = 0;
    int pillarId = 0;
    int midId = 0;
    int extId = 0;

    ofParameterGroup parameters;
    ofParameter<int> intMeshSlider;
    ofParameter<int> midMeshSlider;
    ofParameter<int> extMeshSlider;
    ofParameter<int> pillarMeshSlider;

    ofLight pointLight;
    ofMaterial materialEnv;

    ofxAssimpModelLoader intModel;
    ofxAssimpModelLoader midModel;
    ofxAssimpModelLoader pillarModel;
    ofxAssimpModelLoader extModel;
    ofVboMesh intMesh;
    ofVboMesh midMesh;
    ofVboMesh pillarMesh;
    ofVboMesh extMesh;

    ProcBackground();
private:
};

class SphereMap {
public:
    void setup();
    void update();
    void draw();

    int width, height;

    ofSpherePrimitive sphere;
    ofImage sphereMapTex;

    SphereMap();
private:
};

class Text3d {
public:
    void setup();
    void update();
    void draw(string currentText);

    int width, height;

    ofxAssimpModelLoader alphabet;
    ofVboMesh alphabetLetter;

    ofMaterial materialText;

    Text3d();
private:
};


#endif // RENDER_H

#pragma once
#ifndef RENDER_H
#define RENDER_H
#include "ofMain.h"
#include "ofxAssimpModelLoader.h"

class Render {
public:
    void setup();
    void update();
    void draw();

    void changeModel(int targetID=0);
    void destroyMesh(int amount);
    void meshDestroyed();
    void getAllMesh();
    void getAllMeshListener(int &);
    void changeModelListener(int &);

    int width, height;
    glm::vec3 pos;
    glm::vec2 size;

    ofFbo renderFbo;

    ofParameterGroup parameters;
    ofParameter<int> targetMeshInt;
    ofParameter<int> currentModelSubAttack;

    ofDirectory objList;

    ofLight pointLight;

    ofxAssimpModelLoader targetModel;
    ofVboMesh targetMeshAttack, targetMeshNotAttack, targetMeshDestroyed;
    ofMaterial materialMesh, materialAttack, materialDestroyed;

    vector<bool> destroyedMeshVector;
    vector<string> currentModelSubNames;
    int currentTargetID = 0;
    string currentText;
    int meshIntegrityInit, meshIntegrityCurrent;
    double intergrity;
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

class ObjectTunnel {
public:
    glm::vec3 pos;
    glm::vec3 size;

    ofBoxPrimitive object;

    ObjectTunnel();
private:
};


class Tunnel3d {
public:
    void setup();
    void update();
    void draw();

    int width, height;
    int nbrObject;
    vector<ObjectTunnel> vecObject;

    Tunnel3d();

private:

};

#endif // RENDER_H

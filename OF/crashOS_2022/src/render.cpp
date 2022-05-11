#include "render.h"
#include "ofApp.h"

Render::Render(){}

ProcBackground::ProcBackground(){}

SphereMap::SphereMap(){}

Text3d::Text3d(){}

void Render::setup()
{
    /// MATERIAL
	materialMesh.setShininess(56);
	materialMesh.setDiffuseColor(ofFloatColor::blue);
	materialMesh.setSpecularColor(ofColor(255, 0, 0, 255));

	materialAttack.setDiffuseColor(ofFloatColor::yellow);
	materialAttack.setShininess(120);
	materialAttack.setSpecularColor(ofColor(0, 25, 255, 255));

	/// LIGHT CONFIG
	ofSetSmoothLighting(true);
	pointLight.setDiffuseColor(ofFloatColor::floralWhite);
	pointLight.setSpecularColor(ofFloatColor(1.f, 1.f, 1.f));

    // Load mesh
    targetModel.loadModel("target/2.obj");
//    targetMesh = targetModel.getMesh(2);

    // GUI
    parameters.setName("Target sub attack");
    parameters.add(currentModelSubAttack.set("target Sub attack", 0, 0, targetModel.getMeshCount() - 1));
    currentModelSubNames = targetModel.getMeshNames();
}

void Render::update(int targetID){
    if (targetID != currentTargetID){
        switch (targetID) {
        case 1:
            targetModel.loadModel("target/1.obj");
            break;
        case 2:
            targetModel.loadModel("target/2.obj");
            break;
        default:
            break;
        }
        currentTargetID = targetID;
    }
}


void Render::draw()

{
    ofPushStyle();
    ofPushMatrix();
    /// LIGHT & INIT
    ofEnableDepthTest();
    ofEnableLighting();
    pointLight.enable();
    ofEnableNormalizedTexCoords();
    //ofClear(0);


        /// TARGET

    materialMesh.begin();
    // submesh not under attack (before)
    for (int i = 0; i < currentModelSubAttack; i++) {
        targetModel.getMesh(i).drawFaces();
    }
    // submesh not under attack (after)
    for (int i = currentModelSubAttack + 1; i < targetModel.getMeshCount(); i++) {
        targetModel.getMesh(i).drawFaces();
    }

    materialMesh.end();

    materialAttack.begin();
    // mesh under attack
    targetModel.getMesh(currentModelSubAttack).drawWireframe();
    materialAttack.end();

    /// <summary>
    ///  3D TEXT RENDERING
    /// </summary>

    currentText = currentModelSubNames[currentModelSubAttack];
    ofDisableDepthTest();
    ofDisableLighting();
    ofDisableNormalizedTexCoords();
    ofPopMatrix();
    ofPopStyle();
}




void Text3d::setup(){
    materialText.setDiffuseColor(ofFloatColor::green);
    materialText.setShininess(120);
    materialText.setSpecularColor(ofColor(0, 0, 155, 255));

    alphabet.loadModel("ui/alphabet.obj"); // 3D font;
}

void Text3d::update(){
}

void Text3d::draw(string currentText){
    materialText.begin();
    for (int i = 0; i < currentText.size(); i++) {
        int a = (currentText[i] - 'A');
        alphabetLetter = alphabet.getMesh(a);
        ofPushMatrix();
        ofScale(0.2, 0.2, 0.2);
        ofTranslate((i * 100) + 300, 0, 0);
        //ofTranslate(pos);
        //ofRotate(ang, vec.x, vec.y, vec.z);
        //ofRotate(i * vec.x,0, 1, 0);       // rotate alittle bit, so you can see the "box" of the object
        //ofScale(-1, 1, 1);
        alphabetLetter.drawFaces();
        ofPopMatrix();
    }
    materialText.end();
}

/// Sphere map
void SphereMap::setup(){
    sphereMapTex.load("spheremap/3.jpg");
}

void SphereMap::update(){
}

void SphereMap::draw(){
    ///  SPHERE MAP
    ofEnableDepthTest();
    ofEnableNormalizedTexCoords();

    sphereMapTex.bind();
        ofPushMatrix();
            ofScale(100, 100, 100);
            sphere.drawFaces();
        ofPopMatrix();
    sphereMapTex.unbind();

    ofDisableNormalizedTexCoords();
    ofDisableDepthTest();
}

void ProcBackground::setup(){
    // load model
    intModel.loadModel("envi/s_int.obj");
    intMesh = intModel.getMesh(0);
    extModel.loadModel("envi/s_ext.obj");
    extMesh = extModel.getMesh(0);
    midModel.load("envi/s_mid.obj");
    midMesh = midModel.getMesh(0);
    pillarModel.loadModel("envi/s_pillar.obj");
    pillarMesh = intModel.getMesh(0);

    // Light
    ofSetSmoothLighting(true);
    pointLight.setDiffuseColor(ofFloatColor::floralWhite);
    pointLight.setSpecularColor(ofFloatColor(1.f, 1.f, 1.f));

    // Material
    materialEnv.setDiffuseColor(ofFloatColor::black);
    materialEnv.setShininess(120);
    materialEnv.setSpecularColor(ofColor(0, 124, 255, 255));

    // GUI
    parameters.setName("Procedural BackGround");
    parameters.add(intMeshSlider.set("intMeshSlider", 0, 0, 10));
    parameters.add(extMeshSlider.set("extMeshSlider", 0, 0, 10));
    parameters.add(pillarMeshSlider.set("pillarMeshSlider", 0, 0, 10));
    parameters.add(midMeshSlider.set("midMeshSlider", 0, 0, 10));

}

void ProcBackground::update(){
    intMesh = intModel.getMesh(int(intMeshSlider));
    midMesh = midModel.getMesh(int(midMeshSlider));
    extMesh = extModel.getMesh(int(extMeshSlider));
    pillarMesh = pillarModel.getMesh(int(pillarMeshSlider));
//    targetMesh = targetModel.getMesh(int(targetMeshSlider));
}


void ProcBackground::draw(){
    ofPushMatrix();
    ofPushStyle();
    ofEnableDepthTest();
    ofEnableLighting();
    pointLight.enable();
    ofEnableNormalizedTexCoords();

        materialEnv.begin();

        ofEnableBlendMode(OF_BLENDMODE_MULTIPLY);
        ofScale(5, 5, 5);
        pillarMesh.drawWireframe();
        midMesh.drawWireframe();
        extMesh.drawWireframe();
        intMesh.drawWireframe();
        //materialEnv.end();
        ofPopMatrix();
        ofEnableBlendMode(OF_BLENDMODE_SCREEN);
        ofPushMatrix();
        ofScale(5, 5, 5);

        pillarMesh.drawFaces();
        midMesh.drawWireframe();
        extMesh.drawFaces();
        intMesh.drawFaces();

        materialEnv.end();

    ofEnableBlendMode(OF_BLENDMODE_DISABLED);
    ofDisableNormalizedTexCoords();
    ofDisableLighting();
    ofPopMatrix();
    ofPopStyle();
}


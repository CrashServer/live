#include "ofApp.h"
#include "render.h"

Render::Render(){}

ProcBackground::ProcBackground(){}

SphereMap::SphereMap(){}

Text3d::Text3d(){}

////////////
/// 3D Model
void Render::setup()
{
    width = ofGetWidth();
    height = ofGetHeight();
    /// MATERIAL
	materialMesh.setShininess(56);
	materialMesh.setDiffuseColor(ofFloatColor::blue);
	materialMesh.setSpecularColor(ofColor(255, 0, 0, 255));

	materialAttack.setShininess(120);
    materialAttack.setDiffuseColor(ofFloatColor::yellow);
	materialAttack.setSpecularColor(ofColor(0, 25, 255, 255));

    materialDestroyed.setShininess(12);
    materialDestroyed.setDiffuseColor(ofColor::red);
    materialDestroyed.setSpecularColor(ofColor::antiqueWhite);

	/// LIGHT CONFIG
	ofSetSmoothLighting(true);
	pointLight.setDiffuseColor(ofFloatColor::floralWhite);
	pointLight.setSpecularColor(ofFloatColor(1.f, 1.f, 1.f));


    objList.allowExt("obj");
    objList.listDir("target/");
    objList.sort();

    // GUI
    parameters.setName("Target mMdel attack");
    parameters.add(currentModelSubAttack.set("target Sub attack", 0, 0, 10));
    parameters.add(targetMeshInt.set("target Model", 0, 0, objList.size()-1));

    changeModel(99); // load and init model 0

    currentModelSubAttack.setMax(targetModel.getMeshCount()-1);

    currentModelSubAttack.addListener(this, &Render::getAllMeshListener);
    targetMeshInt.addListener(this, &Render::changeModelListener);
}

void Render::changeModel(int targetID){
    if (targetID != currentTargetID){
        // check if end of directory obj.
        if (targetID >= objList.size()){
            targetID = 0;
            targetMeshInt = 0; // restart to begin
        }

        targetModel.loadModel("target/" + ofToString(targetID) + ".obj");
        destroyedMeshVector.assign(targetModel.getMeshCount(), false);
        currentModelSubAttack= 0;
        currentModelSubNames = targetModel.getMeshNames();
        currentTargetID = targetID;

        getAllMesh();
    }
}

void Render::update(){
}

void Render::getAllMeshListener(int &){
    getAllMesh();
}

void Render::changeModelListener(int &){
    changeModel(targetMeshInt);
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
        targetMeshNotAttack.drawFaces();
    materialMesh.end();

    materialAttack.begin();
        targetMeshAttack.drawWireframe();
    materialAttack.end();

    materialDestroyed.begin();
        targetMeshDestroyed.drawWireframe();
    materialDestroyed.end();

    ofDisableDepthTest();
    ofDisableLighting();
    ofDisableNormalizedTexCoords();
    ofPopMatrix();
    ofPopStyle();
}

void Render::destroyMesh(int amount){
    int amountDestroy = (int) ofClamp(((amount+1)*0.01*meshIntegrityInit), 1, targetMeshAttack.getNumVertices());

    for (int i=0; i< amountDestroy; i++){
        int targetIndex = ofRandom(0,targetMeshAttack.getNumVertices());
        targetMeshAttack.removeVertex(targetIndex);
    }

    meshIntegrityCurrent = targetMeshAttack.getNumVertices();
    intergrity = 100-((double)(meshIntegrityInit-meshIntegrityCurrent)/ (double) meshIntegrityInit)*100;

    if (targetMeshAttack.getNumVertices()<=2){
        meshDestroyed();
        }

    // remove 3d vertex
    //    prevCoord = targetCoord;
    //    targetCoord = meshTarget.getVertex(targetIndex);
}

void Render::meshDestroyed(){
    /// If a mesh is destroyed, load new obj if all destroyed
    cout << "mesh destroyed" << endl;
    destroyedMeshVector[currentModelSubAttack] = true;

    // load new obj if all are part are destroyed
    if (find(destroyedMeshVector.begin(), destroyedMeshVector.end(), false) == destroyedMeshVector.end())
        {changeModel(targetMeshInt++);
            cout << "all destroyed" << endl;
        }
    else{
        currentModelSubAttack++;
        getAllMesh();
    }
}

void Render::getAllMesh(){
    /// load all mesh to ofVboMesh
    targetMeshAttack.clear();
    targetMeshNotAttack.clear();
    targetMeshDestroyed.clear();

    for (unsigned int i=0; i < targetModel.getMeshCount(); i++){
        if (i == currentModelSubAttack){ // mesh to attack
           targetMeshAttack = targetModel.getMesh(currentModelSubAttack);
        }
        else{
            if (destroyedMeshVector[i] == true){ // mesh always destroyed
                targetMeshDestroyed.append(targetModel.getMesh(i));
                }
            else{  // mesh remain
                targetMeshNotAttack.append(targetModel.getMesh(i));
                }
            }
        }
    // get all integrity
    meshIntegrityInit = targetMeshAttack.getNumVertices();
    meshIntegrityCurrent = targetMeshAttack.getNumVertices();
    intergrity = 100.0; // must be a double for division
    currentText = currentModelSubNames[currentModelSubAttack];
}

////////////////
/// TEXT 3D
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
    midModel.loadModel("envi/s_mid.obj");
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

ObjectTunnel::ObjectTunnel(){}
Tunnel3d::Tunnel3d(){}

void Tunnel3d::setup(){
    width=ofGetWidth();
    height=ofGetHeight();
    nbrObject = 20;
    vecObject.reserve(nbrObject);
    glm::vec3 boxSize = glm::vec3(50,50,50);

    for (int i=0; i<nbrObject; i++){
        ObjectTunnel box;
        box.size = boxSize;
        box.pos = glm::vec3(0,0,i*boxSize.z);
        box.object.set(box.pos.x, box.pos.y, box.pos.z);
        vecObject.push_back(box);
    }
}

void Tunnel3d::update(){

}

void Tunnel3d::draw(){
    ofPushMatrix();
    ofPushStyle();
    ofEnableDepthTest();
    ofSetLineWidth(10);
    ofTranslate(0, 0);
    ofSetColor(255,0,0);
        for (int i=0; i<nbrObject;i++){
            vecObject[i].object.draw();
        }
    ofDisableDepthTest();

    ofPopMatrix();
    ofPopStyle();
}

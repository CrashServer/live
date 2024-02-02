#include "ofApp.h"
#include "imageplayer.h"

Imageplayer::Imageplayer(){

}

void Imageplayer::setup(int incrIntegrity){
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    this->nbrIntegrity = int(100/incrIntegrity);
    this->incrIntegrity = incrIntegrity;
    incX = width/nbrIntegrity;
    incY = height/nbrIntegrity;
    imageDir.listDir(imagePath);

    newImage();

}

void Imageplayer::update(int integrity){
    this->integrity = integrity;
}

void Imageplayer::destroy(){
    for (int c=0; c<this->incrIntegrity; c++){
        randomImg.pop_back();
        randomPos.pop_back();
    }
}

void Imageplayer::draw(){
    image.draw(pos, size.x, size.y);
    for (int i=0; i< int(randomPos.size()*integrity/100); i++){
            image.drawSubsection(randomPos[i].x, randomPos[i].y, incX, incY, randomImg[i].x, randomImg[i].y);
        }
}

void Imageplayer::newImage(){
    image.load(imageDir[imageIndex]);
    randomImg.clear();
    randomPos.clear();
    randomImg.resize(nbrIntegrity*nbrIntegrity);
    randomPos.resize(nbrIntegrity*nbrIntegrity);
    for(int y=0; y<int(nbrIntegrity); y++){
        for(int x=0; x<int(nbrIntegrity); x++){
            randomImg.push_back(glm::vec2(x*incX, y*incY));
            randomPos.push_back(glm::vec2(x*incX, y*incY));
            }
        }
    ofRandomize(randomPos);
    ofRandomize(randomImg);
    imageIndex++;
    if (imageIndex>=imageDir.size()){imageIndex=0;}
}

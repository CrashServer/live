#pragma once
#ifndef IMAGEPLAYER_H
#define IMAGEPLAYER_H

class Imageplayer {
public:
    // methods
    void setup(int incrIntegrity);
    void update(int integrity);
    void draw();
    void destroy();
    void newImage();
    void resize();

    ofImage image;
    int width, height;

    glm::vec3 pos;
    glm::vec2 size;

    vector<glm::vec2> randomPos;
    vector<glm::vec2> randomImg;
    int nbrIntegrity=10;
    int incrIntegrity=5;
    float incX, incY;
    int integrity;

    string imagePath="image/";
    ofDirectory imageDir;
    int imageIndex = 0;

    // constructor
    Imageplayer();

private:

};


#endif // IMAGEPLAYER_H

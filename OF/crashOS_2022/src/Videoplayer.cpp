#include "ofApp.h"
#include "Videoplayer.h"

Videoplayer::Videoplayer(){
}

void Videoplayer::setup(){
    // Don't forget in ofxImageSequencePlayback.h to change mSequence to public and not private.
    // and add mSequence.enableThreadedLoad(true); in ofxImageSequencePlayback::newSequenceSetup()

    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    bthread = true;
    vidFps = 60.0f;

    // Fbo init
    videoFbo.allocate(width, height, GL_RGBA);
    videoFbo.begin();
        ofClear(0,0,0, 0);
    videoFbo.end();

    fxFbo.allocate(width/10, height/10, GL_RGBA);

    // video category directory
    videoCat.listDir(videoPath);
    videoCat.sort();

    // list all video from category 0 and random select a video
    vidCat = 1;
    videoDir.listDir(videoCat.getPath(vidCat));
    videoDir.sort();
    vidId = 0;

    // load and play video
    mySequence.mSequence.enableThreadedLoad(bthread);
    mySequence.loadSequence(videoDir.getPath(vidId), vidFps);
    mySequence.setShouldLoop(true);
    mySequence.play();

    // Glitch Fbo
    vecGlitch.reserve(100);
    for (int x=0; x<10; x++){
        for (int y=0; y<10; y++){
            vecGlitch.push_back(glm::vec2(x,y));
        }
    }
    ofRandomize(vecGlitch);
}

void Videoplayer::update(int _videoCat, int integrity){

    this->integrity = integrity;
    // reset vector glitch order at new video
    if (integrity<=0 && bnewSeq){
        ofRandomize(vecGlitch);
        vidId++;
        newSeq();
        }
    if (integrity>0){bnewSeq=true;}

    // load new category
    if (_videoCat != vidCat){
            vidCat = _videoCat;
            newSeq();
        }

     if (!mySequence.mSequence.isLoading() && integrity>0){
        // draw video and glitch squares
        mySequence.update();

        videoFbo.begin();
            ofEnableAlphaBlending();
            ofSetColor(255, 255, 255, ofMap(integrity, 0,100,30,255, true)); // feedback video
            ofScale(size.x / 1280.0, size.y / 720.0);
            mySequence.draw();
            ofDisableAlphaBlending();
        videoFbo.end();

        /// FXfbo remplissage des carrés de destruction
        fxFbo.begin();
            for (int i = 0; i < 10; i++) {
                ofSetColor(ofRandom(0, 255), ofRandom(10,180));
                ofDrawRectangle(ofRandom(0, width/10), ofRandom(0, height/10), ofRandom(1, 5), ofRandom(1, 5));
                }
        fxFbo.end();
    }
    else {
        // loading screen glitch random
        ofPushStyle();
        float loading = mySequence.mSequence.percentLoaded();
        if (loading<1.98){ // test if glitch in main video (0.98)
            videoFbo.allocate((int) ofMap(width*loading+ofRandom(1,30), 0,width+30,1,width, true),
                              (int) ofMap(height*loading+ofRandom(1,30), 0,height+30,1,height, true) , GL_RGBA);
            videoFbo.begin();
            fxFbo.draw(ofRandom(0,width),ofRandom(0,height));
            ofSetColor(ofColor(ofRandom(0,255)));
            ofDrawRectangle(ofRandom(0,width), ofRandom(0,height), ofRandom(1,100), ofRandom(1,100));
            ofDrawBitmapString("Loading " + ofToString(loading*100) + " %", ofRandom(0,width*loading), ofRandom(0,height*loading));
            videoFbo.end();
        }
       else{
            videoFbo.allocate(width, height, GL_RGBA);
            videoFbo.begin();
                ofClear(0,0,0, 0);
            videoFbo.end();
        }
        ofPopStyle();
    }
}

void Videoplayer::draw(){
    ofSetBackgroundColor(0,0,0);

    ofPushMatrix();
    ofPushStyle();
        ofSetColor(ofColor::white);
        videoFbo.draw(0, 0, size.x, size.y);

        // draw FX Fbo
        ofDisableAlphaBlending();
        ofDisableDepthTest();
        float xpos = width/10;
        float ypos = height/10;
        for (int i=0; i< (100 - this->integrity); i++){
            ofEnableBlendMode(OF_BLENDMODE_MULTIPLY);
            fxFbo.draw(vecGlitch[i].x*xpos, vecGlitch[i].y*ypos, xpos, ypos);
            }
        ofDisableBlendMode();
    ofPopStyle();
    ofPopMatrix();
    }

void Videoplayer::newSeq(){
    // load a new video from current category
    videoDir.listDir(videoCat.getPath(vidCat));
    videoDir.sort();
    vidId = ofClamp(vidId, 0,videoDir.size()-1);
    mySequence.loadSequence(videoDir.getPath(vidId), vidFps);
    bnewSeq = false;
}

void Videoplayer::videoSrcub(){
    mySequence.mSequence.getTextureForPercent(ofRandom(1,99));
}

void Videoplayer::resize(){
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);

    // Fbo init
    videoFbo.allocate(width, height, GL_RGBA);
    videoFbo.begin();
        ofClear(0,0,0, 0);
    videoFbo.end();

    fxFbo.allocate(width/10, height/10, GL_RGBA);
}

/// Videoplayer3d

void Videoplayer3d::setup3d(){
    // Don't forget in ofxImageSequencePlayback.h to change mSequence to public and not private.
    // and add mSequence.enableThreadedLoad(true); in ofxImageSequencePlayback::newSequenceSetup()

    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    bthread = true;
    vidFps = 60.0f;

    // Fbo init
    videoFbo.allocate(width, height, GL_RGBA);
    videoFbo.begin();
        ofClear(0,0,0, 0);
    videoFbo.end();

    // video category directory
    videoCat.listDir(videoPath);
    videoCat.sort();

    // list all video from category 0 and random select a video
    vidCat = 1;
    videoDir.listDir(videoCat.getPath(vidCat));
    videoDir.sort();
    vidId = 0;

    // load and play video
    mySequence.mSequence.enableThreadedLoad(bthread);
    mySequence.loadSequence(videoDir.getPath(vidId), vidFps);
    mySequence.setShouldLoop(true);
    mySequence.play();

    // 3D setup
    videoFbo.readToPixels(fboPixels);
    image.setFromPixels(fboPixels);
    //Set up vertices
    for (int y=0; y<H; y++) {
        for (int x=0; x<W; x++) {
            mesh.addVertex(glm::vec3((x - W/2) * meshSize, (y - H/2) * meshSize, 0 ));
            // adding texure coordinates allows us to bind textures to it later
            // --> this could be made into a function so that textures can be swapped / updated
            mesh.addTexCoord(glm::vec2(x * (size.x / W), y * (size.y / H)));
            mesh.addColor(ofColor(255, 255, 255));
            }
    }
    //Set up triangles' indices
    for (int y=0; y<H-1; y++) {
        for (int x=0; x<W-1; x++) {
            int i1 = x + W * y;
            int i2 = x+1 + W * y;
            int i3 = x + W * (y+1);
            int i4 = x+1 + W * (y+1);
            mesh.addTriangle( i1, i2, i3 );
            mesh.addTriangle( i2, i4, i3 );
            }
        }
}


void Videoplayer3d::update3d(int _videoCat, int integrity, float audioRms){
    this->integrity = integrity;
    // reset vector glitch order at new video
    if (integrity<=0){
        ofRandomize(vecGlitch);
        vidId++;
        newSeq();
        }

    // load new category
    if (_videoCat != vidCat){
        vidCat = _videoCat;
        newSeq();
        }

    if (mySequence.mSequence.isLoaded()){
        // update and draw to fbo video sequence
        mySequence.update();

        videoFbo.begin();
            ofEnableAlphaBlending();
            ofSetColor(255, 255, 255, ofMap(integrity, 0,100,30,255, true)); // feedback video
            ofScale(size.x / 1280.0, size.y / 720.0);
            mySequence.draw();
            ofDisableAlphaBlending();
        videoFbo.end();

        // video on a 3d mesh audio reactive
        //convert fbo to ofImage format
        videoFbo.readToPixels(fboPixels);
        image.setFromPixels(fboPixels);
        //Change vertices
        for (int y=0; y<H; y++) {
            for (int x=0; x<W; x++) {
                //Vertex index
                int i = x + W * y;
                glm::vec3 p = mesh.getVertex( i );

                float scaleX = size.x / W;
                float scaleY = size.y / H;

                // get brightness
                int index = (int) ((x * scaleX) + size.x * (y * scaleY)) * 4; // FBO has four components (including Alpha)
                int brightness = fboPixels[index] * audioRms * 20; // 4 is an arbitrary scalar to reduce the amount of distortion

                //Change z-coordinate of vertex
                p.z = brightness; // ofNoise(x * 0.05, y * 0.05, ofGetElapsedTimef() * 0.5) * 100;
                mesh.setVertex( i, p );

                //Change color of vertex
                mesh.setColor(i , ofColor(255, 255, 255));
                }
            }
         }
    else if (mySequence.mSequence.isLoading()){
        // 3d mesh audio reactive with color waiting for video loading
        for (int y=0; y<H; y++) {
            for (int x=0; x<W; x++) {
                //Vertex index
                int i = x + W * y;
                glm::vec3 p = mesh.getVertex( i );

                //Change z-coordinate of vertex
                p.z = audioRms*ofNoise(x * 0.15, y * 0.15, ofGetElapsedTimef()) * 255;
                mesh.setVertex( i, p );

                //Change color of vertex
                mesh.setColor(i , ofColor::fromHsb(p.z, ofNoise(x * 0.05 + 100, y * 0.05 + 400, ofGetElapsedTimef()) * 255,
                                                   ofNoise(x * 0.05 + 300, y * 0.05 + 700, ofGetElapsedTimef()) * 255));
                }
            }
        }
}


void Videoplayer3d::draw3d(){
    ofPushMatrix();
    ofPushStyle();
    if (mySequence.mSequence.isLoading()){
        // 3D loading
        ofSetColor(255);
        ofTranslate( width/2, height/2, 0);
        ofRotateDeg(ofGetElapsedTimef()*5, 1,1,1);
        mesh.drawWireframe();
    }
    else{
        // 3D showing
        ofSetColor(255);
        ofTranslate( width/2, height/2, 0);
        ofRotateDeg(ofGetElapsedTimef()*5, 1,1,1);
        image.bind();
        mesh.draw();
        image.unbind();
    }
    ofPopMatrix();
    ofPopStyle();
}

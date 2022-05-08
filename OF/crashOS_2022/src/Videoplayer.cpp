#include "Videoplayer.h"

Videoplayer::Videoplayer(){
}

void Videoplayer::setup(){
    // Don't forget in ofxImageSequencePlayback.h to change mSequence to public and not private.
    // and add mSequence.enableThreadedLoad(true); in ofxImageSequencePlayback::newSequenceSetup()

    // videoPlayer
    width = ofGetWidth();
    height = ofGetHeight();
    pos = glm::vec3(0,0,0);
    size = glm::vec2(width, height);
    bthread = true;

    videoFbo.allocate(width, height, GL_RGBA);
    videoFbo.begin();
        ofClear(0,0,0, 0);
    videoFbo.end();

    videoFbo.readToPixels(fboPixels);
    image.setFromPixels(fboPixels);

    alpha = 20; // video blending
    vidCat = 0;
    vidId = 0;
    videoDir.listDir("video/");
    videoDir.sort();
    // outputs main themes [0/1/2]
    videoGrp.listDir(videoDir.getPath(vidCat));
    videoGrp.sort();
    // output all selected videos in selected [vidCat] theme
    for (unsigned int i = 0; i < videoGrp.size(); i++) {
        ofLogNotice("output all selected videos in selected theme");
        ofLogNotice(videoGrp.getPath(i));
    }

    vid.listDir(videoGrp.getPath(vidId));
    vid.sort();
    ofLogNotice("display selected video");
    ofLogNotice(videoGrp.getPath(vidId));
    mySequence.mSequence.enableThreadedLoad(bthread);
    mySequence.loadSequence(videoGrp.getPath(vidId), 30.0f);
    mySequence.setShouldLoop(true);
    mySequence.play();

    // 3D
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

void Videoplayer::update(int _videoCat, bool b3d, float audioRms){
    if (_videoCat != vidCat){
        videoGrp.listDir(videoDir.getPath(_videoCat));
        mySequence.loadSequence(videoGrp.getPath(ofRandom(0,videoGrp.size())), 30.0f);
        vidCat = _videoCat;
    }

    if (!mySequence.mSequence.isLoading()){
        mySequence.update();

        videoFbo.begin();
            ofEnableAlphaBlending();
            ofSetColor(255, 255, 255, alpha);
            ofScale(size.x / 1280.0, size.y / 720.0);
            mySequence.draw();
            ofDisableAlphaBlending();
        videoFbo.end();
    }
    else {
        ofPopStyle();
        float loading = mySequence.mSequence.percentLoaded();
        if (loading<90){
            videoFbo.allocate((int) ofMap(width*loading+ofRandom(1,30), 0,width+30,1,width, true),
                              (int) ofMap(height*loading+ofRandom(1,30), 0,height+30,1,height, true) , GL_RGBA);
            videoFbo.begin();
            ofSetColor(ofColor(ofRandom(0,255),ofRandom(0,255),ofRandom(0,255)));
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
        ofPushStyle();
    }

    if (b3d && mySequence.mSequence.isLoaded()){
    //3D
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
    else if (b3d && mySequence.mSequence.isLoading()){
        for (int y=0; y<H; y++) {
            for (int x=0; x<W; x++) {
                //Vertex index
                int i = x + W * y;
                glm::vec3 p = mesh.getVertex( i );

                //Change z-coordinate of vertex
                p.z = audioRms*20*ofNoise(x * 0.05, y * 0.05, ofGetElapsedTimef() * 0.5) * 100;
                mesh.setVertex( i, p );

                //Change color of vertex
                mesh.setColor(i , ofColor(ofRandom(0,255), ofRandom(0,255), ofRandom(0.255), ofRandom(0,255)));
                }
            }


    }
}

void Videoplayer::draw(bool b3d){
    ofSetBackgroundColor(0,0,0);

    ofPushMatrix();
    ofPushStyle();
    if (b3d){
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
    }
    // 2D
    else {
        ofSetColor(ofColor::white);
        videoFbo.draw(0, 0, size.x, size.y);
        }
    ofPopStyle();
    ofPopMatrix();
    }


void Videoplayer::newSeq(){
    videoGrp.listDir(videoDir.getPath(ofRandom(0,videoDir.size())));
    mySequence.loadSequence(videoGrp.getPath(ofRandom(0,videoGrp.size())), 30.0f);
}

void Videoplayer::videoSrcub(){
    mySequence.mSequence.getTextureForPercent(ofRandom(1,99));
}



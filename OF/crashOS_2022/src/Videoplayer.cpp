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

    // index all video directory
    setupIndex();

    // list all video from category 0 and random select a video
    vidCat = 0;
    videoDir.listDir(videoCat.getPath(vidCat));
    videoDir.sort();
    vidId = ofRandom(0, videoDir.size());

    // load and play video
    mySequence.mSequence.enableThreadedLoad(bthread);
    mySequence.loadSequence(videoDir.getPath(vecVideoDirIdx[vidCat][vidId]), vidFps);
    mySequence.setShouldLoop(true);
    mySequence.play();

    // remove video index
    vecVideoDirIdx[vidCat].erase(std::remove(vecVideoDirIdx[vidCat].begin(), vecVideoDirIdx[vidCat].end(), vidId), vecVideoDirIdx[vidCat].end());

//    for (int cat=0; cat < vecVideoDirIdx.size(); cat++){
//        cout << ofToString(cat) << " : " << ofToString(vecVideoDirIdx[cat]) << endl;
//        }

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

    // Glitch Fbo
    vecGlitch.reserve(100);
    for (int x=0; x<10; x++){
        for (int y=0; y<10; y++){
            vecGlitch.push_back(glm::vec2(x,y));
        }
    }
    ofRandomize(vecGlitch);

}

void Videoplayer::update(int integrity, bool b3d, float audioRms){
    // reset vector glitch order at new video
    this->integrity = integrity;
    if (integrity<1){ofRandomize(vecGlitch);}

    if (!mySequence.mSequence.isLoading()){
        mySequence.update();

        videoFbo.begin();
            ofEnableAlphaBlending();
            ofSetColor(255, 255, 255, ofMap(integrity, 0,100,30,255, true));
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
        ofPopStyle();
        float loading = mySequence.mSequence.percentLoaded();
        if (loading<0.98){
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
        ofPushStyle();
    }

    if (b3d){
        update3d(audioRms);
    }

}

void Videoplayer::draw(bool b3d){
    ofSetBackgroundColor(0,0,0);

    ofPushMatrix();
    ofPushStyle();
    if (b3d){
        draw3d();
    }
    // 2D
    else {
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

        }
    ofPopStyle();
    ofPopMatrix();
    }

void Videoplayer::update3d(float audioRms){
    if (mySequence.mSequence.isLoaded()){
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

void Videoplayer::draw3d(){
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

void Videoplayer::setupIndex(){
    // List all video category and populate vector vecVideoDirIdx[cat][video]
    videoCat.listDir("video/");
    videoCat.sort();
    vecVideoDirIdx.clear();
    vecVideoDirIdx.reserve(videoCat.size());
    vecVideoCat.reserve(videoCat.size());
    for (unsigned int cat=0; cat< videoCat.size(); cat++){
        vecVideoCat.push_back(cat);
        videoDir.listDir(videoCat.getPath(cat));
        vector <int> vidIdx;
        for (unsigned int vid=0; vid<videoDir.size(); vid++){
            vidIdx.push_back(vid);
            }
        vecVideoDirIdx.push_back(vidIdx);
        }
    vidCat = 0;
}

void Videoplayer::newSeq(){
    // load a random new video from a random new category
    if( find(vecVideoCat.begin(), vecVideoCat.end(), vidCat) != vecVideoCat.end() ){
//        vidCat = vecVideoCat[vidCat];
        vidId = ofRandom(0, vecVideoDirIdx[vidCat].size());

//     cout << "Video count. " << "vidcat : "<< vidCat << " / vidId : " << vidId << endl;

        videoDir.listDir(videoCat.getPath(vidCat));
        mySequence.loadSequence(videoDir.getPath(vecVideoDirIdx[vidCat][vidId]), vidFps);
        // remove video index
        vecVideoDirIdx[vidCat].erase(std::remove(vecVideoDirIdx[vidCat].begin(), vecVideoDirIdx[vidCat].end(), vecVideoDirIdx[vidCat][vidId]), vecVideoDirIdx[vidCat].end());

        // remove category if no more videos
        if (vecVideoDirIdx[vidCat].size()<=0){
            vecVideoCat.erase(std::remove(vecVideoCat.begin(), vecVideoCat.end(), vidCat), vecVideoCat.end());
            vidCat++;// next category
        }
        // reload all video if no more
        if (vecVideoCat.size() <=0){
            setupIndex();
            }
        }
    else{
        vidCat = vecVideoCat[ofRandom(0,vecVideoCat.size())];
    }
    //

//    for (int cat=0; cat < vecVideoDirIdx.size(); cat++){
//        cout << ofToString(cat) << " : " << ofToString(vecVideoDirIdx[cat]) << endl;
//    }
//    cout << "------------------" << endl;
}

void Videoplayer::newSeq(int _vidCat){
    // load a random video from a category and check if category not empty
    vidCat = _vidCat;
    if( find(vecVideoCat.begin(), vecVideoCat.end(), vidCat) != vecVideoCat.end() ){
        vidId = ofRandom(0, vecVideoDirIdx[vidCat].size());
        videoDir.listDir(videoCat.getPath(vidCat));
        mySequence.loadSequence(videoDir.getPath(vecVideoDirIdx[vidCat][vidId]), vidFps);

        // remove video index
        vecVideoDirIdx[vidCat].erase(std::remove(vecVideoDirIdx[vidCat].begin(), vecVideoDirIdx[vidCat].end(), vecVideoDirIdx[vidCat][vidId]), vecVideoDirIdx[vidCat].end());

        // remove category if no more videos
        if (vecVideoDirIdx[vidCat].size()<=0){
            vecVideoCat.erase(std::remove(vecVideoCat.begin(), vecVideoCat.end(), vidCat), vecVideoCat.end());
            vidCat++; // next category
            }
        // reload all video if no more
        if (vecVideoCat.size() <= 0){
            setupIndex();
            }

//    cout << "Video count. " << "vidcat : "<< vidCat << "/ vidId : " << vidId << endl;
//    for (int cat=0; cat < vecVideoDirIdx.size(); cat++){
//        cout << ofToString(cat) << " : " << ofToString(vecVideoDirIdx[cat]) << endl;
//    }
//    cout << "------------------" << endl;
    }
    else {
        if (vecVideoCat.size() <= 0){
            setupIndex();
            }
        newSeq();
    }

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


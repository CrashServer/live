#pragma once

#include "ofMain.h"
//#include "ofxOsc.h"
#include "ofxNetwork.h"
#include "ofTrueTypeFont.h"
//#include "ofxXmlSettings.h"

#define PORTUDP 20000

class ofApp : public ofBaseApp{

public:
    void setup();
    void update();
    void draw();

    void keyPressed(int key);
    void keyReleased(int key);
    void mouseMoved(int x, int y );
    void mouseDragged(int x, int y, int button);
    void mousePressed(int x, int y, int button);
    void mouseReleased(int x, int y, int button);
    void mouseEntered(int x, int y);
    void mouseExited(int x, int y);
    void windowResized(int w, int h);
    void dragEvent(ofDragInfo dragInfo);
    void gotMessage(ofMessage msg);
    void exit();

    void getData();

    // OSC & udp messages
    //ofxOscReceiver oscSc;
    ofxUDPManager udpConnection;

    // arduino
    ofSerial serial;

    // Variable;
    //bool activeServer;
    //bool bArduinoActive;
};

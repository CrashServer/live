#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
#include "ofxNetwork.h"
#include "ofTrueTypeFont.h"
#include "ofxGui.h"
#include "ofxXmlSettings.h"
#include "ofxPostProcessing.h"
#include "ofxKsmrFragmentFx.h"

#define PORTUDP 20000
#define PORTCPU 20002

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

    string insertNewlines(string in, const size_t every_n);

    // void codeMsgAdd(ofxOscMessage);
    // void serverMsgAdd(ofxOscMessage);
    void setFx();
    void getData();

    void drawCode();
    void drawTop();
    void drawBottom();

    // OSC & udp messages
    ofxOscReceiver oscSc;
    ofxUDPManager udpConnection;

    // arduino
    ofSerial serial;

    // Variable;
    int width, height;
    float cpu;
    string textFirstPlayer;
    string textSecPlayer;
    string textServer;
    float firstPlayerAlpha, secPlayerAlpha, serverAlpha;
    bool activeServer;
    int nbrOfState;
    bool bArduinoActive, bDrawActive;
    int paddingSide, maxTextWidth, maxLogWidth;

    // gui
    ofxPanel gui;
    ofxIntSlider stateSlider;
    ofxIntSlider cpuStress; // stress vritualy the cpu
    ofParameter<ofVec2f> codeFirstPos, codeSecondPos, serverPos, cpuPos;
    ofxToggle bBleach, bBloom, bContrast, bConvolution, bEdge, bFxaa, bKaleid, bLUT,bNoizeWarp, bPixelate, bRGB, bRimHigh, bToon, bZoom;
    bool showGui;

    // interface
    ofImage crashos;  // Crash OS picture
    ofImage alertImage;
    ofIcoSpherePrimitive icoSphere;
    int topBorder, bottomBorder;

    // colors
    //ofColor colState0, colState1, colState2, colState3, colState4;
    vector <ofColor> stateColor;
    ofColor bg, fontColor, fontBackColor;
    ofColor firstCol, secCol, serverCol;

    // fonts
    ofTrueTypeFont font;
    ofTrueTypeFont vagRounded;
    ofTrueTypeFont vagRoundedMini;

    // videoPlayer
    vector <ofVideoPlayer> videoPlayer;

    // XML DATA / TITLES & such
    string serverState0, serverState1, serverState2, serverState3, serverState4;
    string serverName, serverBoot;
    vector <string> stateString, logString;
    int logStringIndex;

    // elapsed time, logic & states
    string timeString;
    string eventString;
    int state = 0;

    //vector <string> videoArray;
    int videoCurrent;

    // 3D STUFF
    //ofEasyCam easyCam;
    //ofVboMesh mesh;

    // Fx & post processing
    ofxPostProcessing post;
    BloomPass::Ptr bloom;
    BleachBypassPass::Ptr bleach;
    ContrastPass::Ptr contrast;
    ConvolutionPass::Ptr convo;
    EdgePass::Ptr edge;
    FxaaPass::Ptr fxaa;
    KaleidoscopePass::Ptr kaleido;
    LUTPass::Ptr lut;
    NoiseWarpPass::Ptr warp;
    PixelatePass::Ptr pixelate;
    RGBShiftPass::Ptr rgb;
    RimHighlightingPass::Ptr rim;
    ToonPass::Ptr toon;
    ZoomBlurPass::Ptr zoom;

    //ofFbo::Settings		setting;
    //ofFbo				original;
    //ofxKsmrFragmentFx	fx;
    //vector <bool> fxVect[8];
};

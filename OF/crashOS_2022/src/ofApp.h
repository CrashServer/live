#pragma once
#ifndef OFAPP_H
#define OFAPP_H



#include "ofMain.h"

#include "ofxAssimpModelLoader.h"
#include "ofEasyCam.h" 
#include "ofxGui.h"
#include "ofxXmlSettings.h"
//#include "ofTrueTypeFont.h"
//#include "ofxOsc.h"
//#include "ofxNetwork.h"
#include "easing.h"

#include "Camera.h"
#include "Videoplayer.h"
#include "Audio.h"
#include "UiMisc.h"
#include "Getdata.h"
#include "glitcher.h"
#include "drawwindows.h"
#include "render.h"
#include "boot.h"
#include "postproc.h"
#include "dmx.h"
#include "scene.h"
#include "imageplayer.h"
#include "textris.h"

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

        void bangUpdate(char playerID);
		void bang(char playerID);
		void bigBang();
		void superBang();

        void changeColorUi(ofColor&);
        void loadDefaultParam(bool&);
        void setScene(int&);

        // Post processingideoplaye
//        void postprocSetup();

        // PANEL GUI
		ofxPanel gui;
        ofParameter<bool> defaultParam;
        ofParameter<int> cpuStress; // stress vritualy the cpu
        ofParameter<int> scene;
        ofParameter<int> integrityIncr;
        ofParameter<float> audioThresh;
        ofParameter<ofColor> colorPicker;

        bool showGui;

        ofParameterGroup parameters;

		/// UI
		int height, width;
        ofColor uiColor;
        vector <ofColor> playerColor;

        /// Settings
        ofxXmlSettings settings;
        bool barduino, bdmx;


        /// CAMERA
		ofEasyCam cam;
        bool camShake;
        float camShakeTime;

        /// game logic;
		int integrity = 100;
        int zbdmScore, svdkScore, serverScore;

        /// audio fft
        float rms, kick, hihat, snare, initTime;


        Render render;
        ProcBackground procBackground;
        SphereMap sphereMap;
        Text3d text3d;

        /// Win win;
        Data data;
        WinCode winCode;
        WinCpu winCpu;
        WinIntegrity winIntegrity;
        WinScore winScore;
        AudioFft audioFft;
        Videoplayer videoplayer;
        Videoplayer3d videoplayer3d;
        VideoplayerAscii videoplayerAscii;
        Camera webcam;
        UiMisc uiMisc;
        Glitcher glitcherCam, glitcherLogo, glitcherVideo;
        Imageplayer imageplayer;
        Textris textris;

        OverHeating overheating;
        Boot boot;

        PostProc postCode, postPixel, postProc, postGlitch, postShift, postEdge, postTV, postKali, postToon;
        Dmx dmx;

        ofColor dmx1Col;
        ofColor dmx2Col;

        /// SCENES
        void scene0Update();
        void scene1Update();
        void scene2Update();
        void scene3Update();
        void scene4Update();
        void scene5Update();
        void scene6Update();
        void scene7Update();
        void scene8Update();
        void scene9Update();
        void scene10Update();
        void scene11Update();
        void scene12Update();
        void scene13Update();
        void scene14Update();
        void scene15Update();
        void scene16Update();

        void scene0Draw();
        void scene1Draw();
        void scene2Draw();
        void scene3Draw();
        void scene4Draw();
        void scene5Draw();
        void scene6Draw();
        void scene7Draw();
        void scene8Draw();
        void scene9Draw();
        void scene10Draw();
        void scene11Draw();
        void scene12Draw();
        void scene13Draw();
        void scene14Draw();
        void scene15Draw();
        void scene16Draw();

        void scene0Bang(char playerID);
        void scene1Bang(char playerID);
        void scene2Bang(char playerID);
        void scene3Bang(char playerID);
        void scene4Bang(char playerID);
        void scene5Bang(char playerID);
        void scene6Bang(char playerID);
        void scene7Bang(char playerID);
        void scene8Bang(char playerID);
        void scene9Bang(char playerID);
        void scene10Bang(char playerID);
        void scene11Bang(char playerID);
        void scene12Bang(char playerID);
        void scene13Bang(char playerID);
        void scene14Bang(char playerID);
        void scene15Bang(char playerID);
        void scene16Bang(char playerID);

        void scene0BigBang();
        void scene1BigBang();
        void scene2BigBang();
        void scene3BigBang();
        void scene4BigBang();
        void scene5BigBang();
        void scene6BigBang();
        void scene7BigBang();
        void scene8BigBang();
        void scene9BigBang();
        void scene10BigBang();
        void scene11BigBang();
        void scene12BigBang();
        void scene13BigBang();
        void scene14BigBang();
        void scene15BigBang();
        void scene16BigBang();

        void sceneDefaultUpdate();
        void sceneDefaultDraw();
        void sceneDefaultBang(char playerID);
        void sceneDefaultBigBang();

//        Tunnel3d tunnel3d;

};
#endif // OFAPP_H

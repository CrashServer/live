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

        /// Settings
        ofxXmlSettings settings;
        bool barduino;


        /// CAMERA
		ofEasyCam cam;
        bool camShake;
        float camShakeTime;

        /// game logic;
		int integrity = 100;
			
        Render render;
        ProcBackground procBackground;
        SphereMap sphereMap;
        Text3d text3d;

        /// Win win;
        Data data;
        WinCode winCode;
        WinCpu winCpu;
        WinIntegrity winIntegrity;
        AudioFft audioFft;
        Videoplayer videoplayer;
        Videoplayer3d videoplayer3d;
        Camera webcam;
        UiMisc uiMisc;
        Glitcher glitcherCam, glitcherLogo, glitcherVideo;

        OverHeating overheating;
        Boot boot;

        PostProc postCode, postPixel, postProc, postShift, postEdge, postTV, postKali;
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

        void sceneDefaultUpdate();
        void sceneDefaultDraw();
        void sceneDefaultBang(char playerID);
        void sceneDefaultBigBang();

//        Tunnel3d tunnel3d;

};
#endif // OFAPP_H

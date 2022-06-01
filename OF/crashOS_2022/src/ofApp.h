#pragma once

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

        void bangUpdate(char playerID);
		void bang(char playerID);
		void bigBang();
		void superBang();

        void changeColorUi(ofColor&);
        void loadDefaultParam(bool&);

        // Post processingideoplaye
        void postprocSetup();

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
        Camera webcam;
        UiMisc uiMisc;
        Glitcher glitcherCam, glitcherLogo, glitcherVideo;

        OverHeating overheating;
        Boot boot;
        PostProc postCode, postPixel, postProc;

//        Tunnel3d tunnel3d;

		/// DMX

		///
        /// 3D
//		int intId = 0;
//		int pillarId = 0;
//		int midId = 0;
//		int extId = 0;
//        int currentTargetID = 0;

//		ofLight pointLight;
//		ofxAssimpModelLoader targetModel;
//		ofVboMesh targetMesh;
//		ofxAssimpModelLoader alphabet;
//		ofVboMesh alphabetLetter;
//		string currentText;
//		ofSpherePrimitive sphere;
//		ofImage sphereMapTex;
//		vector<string> currentModelSubNames;
        /// MATERIALS
//		ofMaterial materialMesh, materialAttack, materialEnv;
//		ofMaterial materialText;


//		ofxAssimpModelLoader intModel;
//		ofxAssimpModelLoader midModel;
//		ofxAssimpModelLoader pillarModel;
//		ofxAssimpModelLoader extModel;
//		ofVboMesh intMesh;
//		ofVboMesh midMesh;
//		ofVboMesh pillarMesh;
//		ofVboMesh extMesh;


        // POST PROCESSING
//		ofFbo fbo;

//		ofFbo secondPassFbo;
//		ofFbo renderFbo;

//		ofShader shaderBlurY;
//		ofShader swell;
//		ofShader glow;
//		ofShader glitch;
//		ofShader crBlueinvert;
//		ofShader test;

		
};

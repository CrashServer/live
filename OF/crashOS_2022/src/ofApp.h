#pragma once

#include "ofMain.h"

#include "ofxAssimpModelLoader.h"
#include "ofEasyCam.h" 
#include "ofxGui.h"
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

        //void getData();
//        void dataSetup();
//        void dataUpdate();
//        string insertNewlines(string in, const size_t every_n);

        void bangUpdate(char playerID);
		void bang(char playerID);
		void bigBang();
		void superBang();

        // 3d render
        void renderSetup();
        void renderUpdate(int targetID);
        void renderDraw();

        void procBackgroundUpdate();
        void procBackgroundDraw();
        void sphereMapDraw();
        void sphereMapSetup();

        // Post processingideoplaye
        void postprocSetup();

        // PANEL GUI
		ofxPanel gui;
        ofParameter<int> cpuStress; // stress vritualy the cpu
        ofParameter<glm::vec2> webcamSize; // logSize, scoreSize, targetWindowSize,;
        ofParameter<glm::vec3> webcamPos;// targetWindowPos, logPos, scorePos;
        ofParameter<int> currentModelSubAttack;
        ofParameter<int> intMeshSlider;
        ofParameter<int> pillarMeshSlider;
        ofParameter<int> extMeshSlider;
        ofParameter<int> midMeshSlider;
        ofParameter<int> targetMeshSlider;
        ofParameter<int> scene;
        ofParameter<int> integrityIncr;
		bool showGui;

        ofParameterGroup parameters;

		/// UI
        //ofImage alertCpu;
        //ofImage windows;
		int height, width;
        //ofTrueTypeFont font;
        ofColor uiColor;

		// WINDOWS MANAGEMENT 
//        int paddingWindow, maxLineCode, maxCodeWidth;
//        int codeTotalHeight, codeTotalWidth;
//        ofRectangle fontCharBox, cpuStringBox;

		// CAMERA 
		ofEasyCam cam;
		bool camShake; 
		float camShakeTime;

		// game logic;
		int integrity = 100;
			
        /// data
//        ofxOscReceiver oscReceiver;
//        ofSerial serial;
//        float scCPU;
//        vector<string> vectorCode;
//        vector<char> vectorSymbol;

		/// 3D
		int intId = 0; 
		int pillarId = 0;
		int midId = 0;
		int extId = 0;
        int currentTargetID = 0;

		ofLight pointLight;
		ofxAssimpModelLoader targetModel;
		ofVboMesh targetMesh;
		ofxAssimpModelLoader alphabet;
		ofVboMesh alphabetLetter;
		string currentText;
		ofSpherePrimitive sphere;
		ofImage sphereMapTex; 
		vector<string> currentModelSubNames;
		/// MATERIALS 
		ofMaterial materialMesh, materialAttack, materialEnv;
		ofMaterial materialText;
		
	
		ofxAssimpModelLoader intModel;
		ofxAssimpModelLoader midModel;
		ofxAssimpModelLoader pillarModel;
		ofxAssimpModelLoader extModel;
		ofVboMesh intMesh;
		ofVboMesh midMesh;
		ofVboMesh pillarMesh;
		ofVboMesh extMesh;


		// POST PROCESSING
		ofFbo fbo;

        //ofFbo videoFbo;
        //ofFbo uiFbo;
		ofFbo secondPassFbo;
		ofFbo renderFbo;

		ofShader shaderBlurY;
		ofShader swell;
		ofShader glow;
		ofShader glitch;
		ofShader crBlueinvert;
		ofShader test;

		
		/// VARIABLES 
//        ofFbo fboCpu;
        /// Modules call
        ///

//        Win win;
        Data data;
        WinCode winCode;
        WinCpu winCpu;
        WinIntegrity winIntegrity;
        AudioFft audioFft;
        Videoplayer videoplayer;
        Camera webcam;
        UiMisc uiMisc;
        Glitcher glitcherCam, glitcherLogo, glitcherVideo;

		/// DMX

		///

		
};

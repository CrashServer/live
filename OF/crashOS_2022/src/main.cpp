#include "ofMain.h"
#include "ofApp.h"

int main(){
//Use ofGLFWWindowSettings for more options like multi-monitor fullscreen
ofGLWindowSettings settings;
settings.setSize(1920, 1080);
settings.windowMode = OF_WINDOW; //can also be OF_FULLSCREEN

auto window = ofCreateWindow(settings);

ofRunApp(window, make_shared<ofApp>());
ofRunMainLoop();
}

//========================================================================

//int main() {

//#ifdef OF_TARGET_OPENGLES
//    ofGLESWindowSettings settings;
//    settings.glesVersion = 2;
//#else
//    ofGLWindowSettings settings;
//    settings.setGLVersion(4, 1);
//#endif
//    settings.setSize(1920, 1080);
//    ofCreateWindow(settings);

	// this kicks off the running of my app
	// can be OF_WINDOW or OF_FULLSCREEN
	// pass in width and height too:
	//settings.windowMode = OF_FULLSCREEN;
    //ofRunApp(new ofApp());

//}


//int main() {
//
//	ofGLWindowSettings settings;
//	settings.setGLVersion(3, 2);
//	settings.setSize(1920, 1080);
//	//settings.windowMode = OF_FULLSCREEN;
//	ofCreateWindow(settings);
//	ofRunApp(new ofApp());
//
//}

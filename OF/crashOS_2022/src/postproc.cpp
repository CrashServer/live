#include "postproc.h"
#include "ofApp.h"


void ofApp::postprocSetup(){
//#ifdef TARGET_OPENGLES
//	shaderBlurX.load("shadersES2/shaderBlurX");
//	shaderBlurY.load("shadersES2/shaderBlurY");
//#else
//	if (ofIsGLProgrammableRenderer()) {
//		shaderBlurY.load("shadersGL3/shaderBlurY");
//	}
//	else {
//		shaderBlurY.load("shadersGL2/shaderBlurY");
//	}
//#endif
    //glow.load("shadersGL3/glow");
    shaderBlurY.load("shadersGL3/shaderBlurY");
    //swell.load("shaderGL3/swell");
    //glitch.load("shaderGL3/glitch");
    //crBlueinvert.load("shaderGL3/crBlueinvert");
    //test.load("shaderGL3/test");
}

#include "ofApp.h"
#include "postproc.h"

PostProc::PostProc(){

}

void PostProc::setup(bool bBloom, bool bPixel, bool bBleach){
    post.init(ofGetWidth(), ofGetHeight());

    // Bloom
    bloom = post.createPass<BloomPass>();
    bloom->setEnabled(bBloom);

    // Pixelate
    pixel = post.createPass<PixelatePass>();
    pixel->setEnabled(bPixel);

    //  Bleach
    bleach = post.createPass<BleachBypassPass>();
    bleach->setEnabled(bBleach);

    //    post.createPass<EdgePass>()->setEnabled(true);
}

void PostProc::begin(){
    ofEnableDepthTest();
    post.begin();
}

void PostProc::end(){
    post.end();
    ofDisableDepthTest();
}












//void ofApp::postprocSetup(){
////#ifdef TARGET_OPENGLES
////	shaderBlurX.load("shadersES2/shaderBlurX");
////	shaderBlurY.load("shadersES2/shaderBlurY");
////#else
////	if (ofIsGLProgrammableRenderer()) {
////		shaderBlurY.load("shadersGL3/shaderBlurY");
////	}
////	else {
////		shaderBlurY.load("shadersGL2/shaderBlurY");
////	}
////#endif
//    //glow.load("shadersGL3/glow");

////    shaderBlurY.load("shadersGL3/shaderBlurY");

//    //swell.load("shaderGL3/swell");
//    //glitch.load("shaderGL3/glitch");
//    //crBlueinvert.load("shaderGL3/crBlueinvert");
//    //test.load("shaderGL3/test");
//}

#include "postproc.h"
//#include "ofApp.h"

PostProc::PostProc() {

}

void PostProc::setup(bool bBloom, bool bPixel, bool bBleach, bool bShift, bool bEdge, bool bKali, bool bAces, bool bNoise, bool bTv, bool bGlitch, bool bFilm, bool bToon) {
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

    //  shift
    shift = post.createPass<RGBShiftPass>();
    shift->setEnabled(bShift);

    //edge
    edge = post.createPass<EdgePass>();
    edge->setEnabled(bEdge);

    //kali
    kali = post.createPass<KaleidoscopePass>();
//    kali->setSegments(gKaleiSegments);
    kali->setEnabled(bKali);


    // Color ACES
    aces = post.createPass<ACESFilmicToneMappingPass>();
    aces->setEnabled(bAces);

    //19-Noise Grains Filter
    noise = post.createPass<NoisePass>();
    noise->setEnabled(bNoise);

    //17-Bad TV
    tv = post.createPass<BadTVPass>();
    tv->setEnabled(bTv);

    //15-Glitch
    glitch = post.createPass<DigitalGlitchPass>();
    glitch->setEnabled(bGlitch);

    //13-FilmGrainLines
//    film = post.createPass<FilmGrainLinesPass>();
//    film->setEnabled(bFilm);

    //14-Toon
    toon = post.createPass<ToonPass>();
    toon->setEnabled(bToon);

}

void PostProc::begin() {
    ofEnableDepthTest();
    post.begin();
}

void PostProc::end() {
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

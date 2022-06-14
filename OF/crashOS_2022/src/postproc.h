#pragma once
#ifndef POSTPROC_H
#define POSTPROC_H
//#include "ofMain.h"
#include "ofxPostProcessing.h"

//// Post Processing parameters
/// kaleid : post.kali->setSegments(float -20,20);
/// Bloom : post.bloom->setBlurXY(float 0.01,0.01); // max (0.01,0.01)
/// pixel : none
/// bleach : post.bleach->setOpacity(float);
/// rgb : post.shift->setAmount(float 0,1) && post.shift->setAngle(float 0, TWO_PI)
/// edge : post.edge->setHue(float) && post.edge->setSaturation(float)
/// aces : post.aces−>setExposure(float 0.0, 1.0);
/// noise : post.noise->setSpeed(float 0,1) && post.noise->setAmount(float 0,1);
/// tv : post.tv->setDistortion(float 0,20.0) && ->setDistortion2(float 0,20.0) && −>setSpeed(float 0,20.0) && ->setRollSpeed(float 0.0,1.0);
/// glitch : post.glitch->setAmount(float 0.0,0.1)  && ->setAngle(float ofRandom(0, TWO_PI)) && ->setSeed(float 0,1) && setSeedX(float 0,1) && setSeedY(float 0,1)
///             && setDistortionX(float ofSignedNoise(ofGetFrameNum() * 0.04)) && setDistortionY(float ofSignedNoise(ofGetFrameNum() * 0.01)) && setCols(float ofRandom(0.00001, 0.3))
/// film : post.film->setnIntensity(float 0,1) && setsIntensity(float 0,1) && setCount(float 1,10000) && setGrayScale(int true, false)
/// toon : post.toon->setEdgeThreshold(float) && setLevel(float) && setAmbientColor(const ofVec4f&) && setDiffuseColor(const ofVec4f&) && setSpecularColor(const ofVec4f&)
///           setEnableSpecular(bool) && setShinyness(float)

//// Examples fft:
//// shift : postCode.shift->setAmount(audioFft.beat.getMagnitude()*0.005*audioThresh);
//// bleach : postCode.bleach->setOpacity(audioFft.beat.getMagnitude()*0.2*audioThresh);
//// edge : postCode.edge->setEnabled(audioFft.beat.getMagnitude()*0.2*audioThresh>1);
///  kali: postCode.kali->setSegments(audioFft.beat.getMagnitude()*0.4);
///        postCode.kali->setEnabled(audioFft.beat.getMagnitude()*0.2*audioThresh>1);
///  aces :     postCode.aces->setExposure(audioFft.beat.getMagnitude()*0.4*audioThresh);
////            postCode.aces->setEnabled(audioFft.beat.getMagnitude()*0.2*audioThresh>1);
///  noise: postCode.noise->setAmount(audioFft.beat.getMagnitude()*0.2*audioThresh);
///  tv : postTV.tv->setRollSpeed(audioFft.beat.getMagnitude()*0.001*audioThresh);



class PostProc {
public:
    void setup(bool bBloom = false, bool bPixel = false, bool bBleach = false, bool bShift = false, bool bEdge = false, bool bKali = false, bool bAces = false, bool bNoise = false, bool bTv = false, bool bGlitch = false, bool bFilm = false, bool bToon = false);
    void begin();
    void end();

    ofxPostProcessing post;
//    KaleidoscopePass::Ptr kaleido;
    BloomPass::Ptr bloom;
    PixelatePass::Ptr pixel;
    BleachBypassPass::Ptr bleach;
    RGBShiftPass::Ptr shift;
    EdgePass::Ptr edge;
    KaleidoscopePass::Ptr kali;
    ACESFilmicToneMappingPass::Ptr aces;
    NoisePass::Ptr noise;
    BadTVPass::Ptr tv;
    DigitalGlitchPass::Ptr glitch;
    FilmGrainLinesPass::Ptr film;
    ToonPass::Ptr toon;

//    int gKaleiSegments;
//    float kaleiParam;
//    glm::vec2 bloomPara;



    PostProc();


};


#endif // POSTPROC_H

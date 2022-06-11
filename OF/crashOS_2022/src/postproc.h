#pragma once
#ifndef POSTPROC_H
#define POSTPROC_H
//#include "ofMain.h"
#include "ofxPostProcessing.h"

class PostProc {
public:
    void setup(bool bBloom = false, bool bPixel = false, bool bBleach = false, bool bShift = false, bool bEdge = false, bool bKali = false, bool bAces = false, bool bNoise = false, bool bTv = false, bool bGlitch = false, bool bFilm = false, bool bToon = false);
    void begin();
    void end();

    ofxPostProcessing post;
    KaleidoscopePass::Ptr kaleido;
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

    int gKaleiSegments;

    PostProc();


};


#endif // POSTPROC_H

#pragma once
#ifndef POSTPROC_H
#define POSTPROC_H

//#include "ofMain.h"
#include "ofxPostProcessing.h"

class PostProc{
public:
    void setup(bool bBloom=false, bool bPixel=false,bool bBleach=false);
    void begin();
    void end();

    ofxPostProcessing post;

    KaleidoscopePass::Ptr kaleido;
    BloomPass::Ptr bloom;
    PixelatePass::Ptr pixel;
    BleachBypassPass::Ptr bleach;

    PostProc();


};


#endif // POSTPROC_H

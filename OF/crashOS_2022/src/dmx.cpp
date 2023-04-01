#include "ofApp.h"
#include "dmx.h"

Dmx::Dmx(){}

void Dmx::setup(int dmxAddr1, int dmxAddr2){
    this->dmxAddr1 = dmxAddr1;
    this->dmxAddr2 = dmxAddr2;
    memset( dmxData_, 0, DMX_DATA_LENGTH );
    dmxInterface_ = ofxGenericDmx::createDevice(DmxDevice::DMX_DEVICE_RAW);
    bool opened = dmxInterface_->open();
    if ( dmxInterface_ == 0 || !opened ) printf( "No FTDI Device Found\n" );
    else printf( "isOpen: %i\n", dmxInterface_->isOpen() );
}

void Dmx::update(ofColor dmx1, ofColor dmx2){
    dmxData_[dmxAddr1] = dmx1.r;
    dmxData_[dmxAddr1+1] = dmx1.g;
    dmxData_[dmxAddr1+2] = dmx1.b;

    dmxData_[dmxAddr2] = dmx2.r; // 8
    dmxData_[dmxAddr2+1] = dmx2.g;
    dmxData_[dmxAddr2+2] = dmx2.b;

    if ( ! dmxInterface_ || ! dmxInterface_->isOpen() ) {
        printf( "Not updating, enttec device is not open.\n");
    }
    else{
        //send the data to the dmx interface
        dmxInterface_->writeDmx( dmxData_, DMX_DATA_LENGTH );
    }

}

void Dmx::exit(){
    if ( dmxInterface_ && dmxInterface_->isOpen() ) {
        // send all zeros (black) to every dmx channel and close!
        for ( int i = 0; i <= DMX_DATA_LENGTH; i++ ) dmxData_[i] = 0;
        dmxInterface_->writeDmx( dmxData_, DMX_DATA_LENGTH );
        dmxInterface_->close();
    }
}

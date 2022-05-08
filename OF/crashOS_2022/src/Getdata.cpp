#include "Getdata.h"
#include "ofApp.h"

Data::Data(){}

void Data::setup(){
    oscReceiver.setup(PORTOSC);
    maxLineCode = 40;
    vectorCode.assign(maxLineCode + 1, ">> CrashServer OS");
    vectorSymbol.assign(maxLineCode + 1, '!');
    bang = '0';
    //oscReceiver.setup(PORTUDP);
    //ofxUDPSettings settings;
    //settings.receiveOn(PORTUDP);
    //settings.blocking = false;
    //udpConnection.Setup(settings);

}

void Data::update(int cpuStress, int maxCodeWidth) {
    if (vectorCode.size() >= maxLineCode) {
        vectorCode.erase(vectorCode.begin());
        vectorSymbol.erase(vectorSymbol.begin());
    }
    if (oscReceiver.hasWaitingMessages()) {
        ofxOscMessage messageOsc;
        oscReceiver.getNextMessage(messageOsc);
        string oscAdress = messageOsc.getAddress();
        
        if (oscAdress == "/CPU") {
            scCPU = messageOsc.getArgAsFloat(0) * cpuStress;
            bang = 'c';
            }
        else if (oscAdress == "/svdkCode") {
            string txt = messageOsc.getArgAsString(0);
            txt = insertNewlines(txt, maxCodeWidth);
            vectorCode.push_back(txt);
            vectorSymbol.push_back('#');
            bang ='#';
        }
        else if (oscAdress == "/zbdmCode") {
            string txt = messageOsc.getArgAsString(0);
            txt = insertNewlines(txt, maxCodeWidth);
            vectorCode.push_back(txt);
            vectorSymbol.push_back('!');
            bang='!';
        }
        else if (oscAdress == "/serverCode") {
            string txt = messageOsc.getArgAsString(0);
            txt = insertNewlines(txt, maxCodeWidth);
            vectorCode.push_back(txt);
            vectorSymbol.push_back('@');
            bang='@';
        }
    }

    //    // Udp Code player *2 + Code Server
    //    char udpMessage[500];
    //    udpConnection.Receive(udpMessage,500);
    //    string message=udpMessage;
    //    char msgType = message[0];
    //    if (vectorCode.size() >= maxLineCode){
    //        vectorCode.erase(vectorCode.begin());
    //        vectorSymbol.erase(vectorSymbol.begin());
    //        }
    //    if (message!=""){
    //        if (msgType == '_'){
    //            superBang();
    //        }
    //        else {
    //            string txt = message.erase(0,1);
    //            txt = insertNewlines(txt, maxCodeWidth); // do on receive to avoid on udpate, cpu efficience
    //            vectorCode.push_back(txt);
    //            vectorSymbol.push_back(msgType);
    //            bang(msgType);
    //            }
    //        }
}

// return a text with a new line every x
string Data::insertNewlines(string in, const size_t every_n)
{
    string out;
    out.reserve(in.size() + in.size() / every_n);
    for (std::string::size_type i = 0; i < in.size(); i++) {
        if (!(i % every_n) && i) {
            out.push_back('\n');
        }
        out.push_back(in[i]);
    }
    return out;
}


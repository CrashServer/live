#include "ofApp.h"
//#include "Getdata.h"

Data::Data(){}
CodeLine::CodeLine(){
    code = ">> CrashServer";
    symbol = '!';
    typeCodePos = 0;
}


void Data::setup(bool barduino){
    oscReceiver.setup(PORTOSC);
    maxLineCode = 40;
    for (int i=0; i<maxLineCode; i++){
        CodeLine lineC;
        vectorCode.push_back(lineC);
    }

    //    vectorCode.assign(maxLineCode + 1, CodeLine);
    bang = '0';

    if (barduino){
        serial.setup(0, 115200);
        this->barduino = barduino;
    }
    else {barduino = false;}
    isServerActive = false;
}

void Data::update(int cpuStress, int maxCodeWidth) {
    if (vectorCode.size() >= maxLineCode) {
        vectorCode.erase(vectorCode.begin());
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
            //string txt = messageOsc.getArgAsString(0);
            //txt = insertNewlines(txt, maxCodeWidth);
            CodeLine codeLine;
            codeLine.code = messageOsc.getArgAsString(0);
            codeLine.symbol = '#';
            vectorCode.push_back(codeLine);
            //vectorCode.push_back(txt);
            //vectorSymbol.push_back('#');
            bang ='#';
            if (barduino){
                serial.writeByte('g'); // send arduino
                serial.flush();
            }
        }
        else if (oscAdress == "/zbdmCode") {
//            string txt = messageOsc.getArgAsString(0);
//            txt = insertNewlines(txt, maxCodeWidth);
//            vectorCode.push_back(txt);
//            vectorSymbol.push_back('!');
            CodeLine codeLine;
            codeLine.code = messageOsc.getArgAsString(0);
            codeLine.symbol = '!';
            vectorCode.push_back(codeLine);
            bang='!';
            if (barduino){
                serial.writeByte('o'); // send arduino
                serial.flush();
            }
        }
        else if (oscAdress == "/serverCode") {
//            string txt = messageOsc.getArgAsString(0);
//            txt = insertNewlines(txt, maxCodeWidth);
//            vectorCode.push_back(txt);
//            vectorSymbol.push_back('@');
            CodeLine codeLine;
            codeLine.code = messageOsc.getArgAsString(0);
            codeLine.symbol = '@';
            vectorCode.push_back(codeLine);
            bang='@';
            if (barduino){
                serial.writeByte('r'); // send arduino
                serial.flush();
            }
            delayServerActivity = serverInitTimer;
            isServerActive = true;
        }
    }
    if (delayServerActivity > 0) {
        delayServerActivity--;
    }
    else {isServerActive = false;}
}

// return a text with a new line every x
//string Data::insertNewlines(string in, const size_t every_n)
//{
//    string out;
//    out.reserve(in.size() + in.size() / every_n);
//    for (std::string::size_type i = 0; i < in.size(); i++) {
//        if (!(i % every_n) && i) {
//            out.push_back('\n');
//        }
//        out.push_back(in[i]);
//    }
//    return out;
//}


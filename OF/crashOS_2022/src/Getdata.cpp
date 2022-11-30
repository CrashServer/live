#include "ofApp.h"
//#include "Getdata.h"

Data::Data(){}
CodeLine::CodeLine(){
    code = ">> CrashServer";
    symbol = '!';
    typeCodePos = 1;
}

CodeInstant::CodeInstant(){
    name = "";
    code = "";
    posMark = 0;
}


void Data::setup(bool barduino){
    oscReceiver.setup(PORTOSC);
    maxLineCode = 40;
    for (int i=0; i<maxLineCode; i++){
        CodeLine lineC;
        vectorCode.push_back(lineC);
    }
    CodeInstant codeI;
    vectorInstant.push_back(codeI); // Zbdm
    vectorInstant.push_back(codeI); // Svdk

    //    vectorCode.assign(maxLineCode + 1, CodeLine);
    bang = '0';

    if (barduino){
        serial.setup(0, 115200);
        this->barduino = barduino;
    }
    else {barduino = false;}
    isServerActive = false;
}

void Data::update() {
    if (vectorCode.size() >= maxLineCode) {
        vectorCode.erase(vectorCode.begin());
    }
    if (oscReceiver.hasWaitingMessages()) {
        ofxOscMessage messageOsc;
        oscReceiver.getNextMessage(messageOsc);
        string oscAdress = messageOsc.getAddress();
        
        if (oscAdress == "/CPU") {
            scCPU = messageOsc.getArgAsFloat(0);
            bang = 'c';
            // send arduino cpu state
            if (barduino){
                if (scCPU < 20.0){
                    serial.writeByte('a');
                    serial.flush();
                    }
                if (scCPU >= 20.0 && scCPU < 40.0){
                    serial.writeByte('b');
                    serial.flush();
                    }
                if (scCPU >= 40.0 && scCPU < 60.0){
                    serial.writeByte('c');
                    serial.flush();
                    }
                if (scCPU >= 60.0 && scCPU < 80.0){
                    serial.writeByte('d');
                    serial.flush();
                    }
                if (scCPU >= 80.0 && scCPU < 100.0){
                    serial.writeByte('e');
                    serial.flush();
                    }
                if (scCPU >= 100.0){
                    serial.writeByte('f');
                    serial.flush();
                    }
                }

            }
        else if (oscAdress == "/svdkCode") {
            string msg = messageOsc.getArgAsString(0);
            size_t found = msg.find("scene");
            if (found!=std::string::npos){
                string sceneStr = msg.substr(5);
                if (isNumber(sceneStr)){
                    scene = stoi(sceneStr);
                    }
                }

            CodeLine codeLine;
            codeLine.code = msg;
            codeLine.symbol = '#';
            vectorCode.push_back(codeLine);
            bang ='#';
            if (barduino){
                serial.writeByte('v'); // send arduino
                serial.flush();
            }
        }
        else if (oscAdress == "/zbdmCode") {
            string msg = messageOsc.getArgAsString(0);
            size_t found = msg.find("scene");
            if (found!=std::string::npos){
                string sceneStr = msg.substr(5);
                if (isNumber(sceneStr)){
                    scene = stoi(sceneStr);
                    }
                }

            CodeLine codeLine;
            codeLine.code = messageOsc.getArgAsString(0);
            codeLine.symbol = '!';
            vectorCode.push_back(codeLine);
            bang='!';
            if (barduino){
                serial.writeByte('z'); // send arduino
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
                serial.writeByte('s'); // send arduino
                serial.flush();
            }
            delayServerActivity = serverInitTimer;
            isServerActive = true;
        }

        else if (oscAdress == "/zbdmTypeCode"){
            vectorInstant[0].name = messageOsc.getArgAsString(0);
            vectorInstant[0].code = messageOsc.getArgAsString(1);
            vectorInstant[0].posMark = messageOsc.getArgAsInt(2);
            //vectorInstant[0].code.insert(vectorInstant[0].posMark, "_");
        }

        else if (oscAdress == "/svdkTypeCode"){
            vectorInstant[1].name = messageOsc.getArgAsString(0);
            vectorInstant[1].code = messageOsc.getArgAsString(1);
            vectorInstant[1].posMark = messageOsc.getArgAsInt(2);
        }

    }
    if (delayServerActivity > 0) {
        delayServerActivity--;
    }
    else {isServerActive = false;}
}

bool Data::isNumber(const string &s){
    for (char const &ch : s) {
            if (isdigit(ch) == 0)
                return false;
        }
        return true;
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


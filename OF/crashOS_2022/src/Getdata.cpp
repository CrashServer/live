#include "ofApp.h"

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


void Data::setup(string troopIp, int troopPort, int arduinoPort, bool bvideoFox){
    oscReceiver.setup(PORTOSC);
    oscSender.setup(troopIp, troopPort);
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
    this->arduinoPort = arduinoPort;
    this->bvideoFox = bvideoFox;
    testArduino();
    isServerActive = false;

    if (parameters.size()==0){
        parameters.setName("Test");
        parameters.add(cpuTest.set("Cpu", false));
        parameters.add(bpmTest.set("Bpm", false));
        parameters.add(arduinoTest.set("Arduino", false));
        parameters.add(oscTestZbdm.set("Osc ZBDM", false));
        parameters.add(oscTestSvdk.set("Osc Svdk", false));
        parameters.add(dmxTest.set("Dmx", false));
        parameters.add(buttonTest.set("Button", false));
        parameters.add(button.set("Test"));
    }
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
            if (this->barduino){
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
            if (this->barduino){
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
            if (this->barduino){
                serial.writeByte('z'); // send arduino
                serial.flush();
            }
        }
        else if (oscAdress == "/serverCode") {
            CodeLine codeLine;
            codeLine.code = messageOsc.getArgAsString(0);
            codeLine.symbol = '@';
            vectorCode.push_back(codeLine);
            bang='@';
            if (this->barduino){
                serial.writeByte('s'); // send arduino
                serial.flush();
            }
            else {delayServerActivity = serverInitTimer;
                isServerActive = true;}
        }

        else if (oscAdress == "/zbdmTypeCode"){
            vectorInstant[0].name = messageOsc.getArgAsString(0);
            vectorInstant[0].code = messageOsc.getArgAsString(1);
            vectorInstant[0].posMark = messageOsc.getArgAsInt(2);
        }

        else if (oscAdress == "/svdkTypeCode"){
            vectorInstant[1].name = messageOsc.getArgAsString(0);
            vectorInstant[1].code = messageOsc.getArgAsString(1);
            vectorInstant[1].posMark = messageOsc.getArgAsInt(2);
        }

        else if (oscAdress == "/video" && this->bvideoFox){
            vidpos1 = messageOsc.getArgAsFloat(1);
            vidid1 = messageOsc.getArgAsInt(2);
            vidpos2 = messageOsc.getArgAsFloat(3);
            vidid2 = messageOsc.getArgAsInt(4);
            vidblend1 = messageOsc.getArgAsInt(5);
            vidblend2 = messageOsc.getArgAsInt(6);
            scene = messageOsc.getArgAsInt(7);
        }
        else if (oscAdress == "/OSbpm") {
            bpm = messageOsc.getArgAsInt(0);
        }
    }
    if (!this->barduino){
        if (delayServerActivity > 0) {
            delayServerActivity--;
            }
        else {isServerActive = false;}
    }
    //// read button state
    if (this->barduino){
        char button = serial.readByte();
        if (button == 's' && prevButton == 'c' && isServerActive == false && scene!=0){ // activate server
            isServerActive = true;
            vector<string> param;
            param.push_back("1");
            sendOSC("/cmd/serverState", param);
            prevButton = button;
        }
        else if (button == 's' && prevButton == 'c' && isServerActive == false && scene==0){
            testButton = true;
        }
        else if (button == 'c' && prevButton == 's' && isServerActive == true){ // shutdown server
            isServerActive = false;
            vector<string> param;
            param.push_back("0");
            sendOSC("/cmd/serverState", param);
            prevButton = button;
            testButton = false;
        }
    }
}

void Data::sendOSC(string address, vector<string> param){
    ofxOscMessage m;
    m.setAddress(address);
    for (int i=0; i<param.size(); i++){
        m.addStringArg(param[i]);
    }
    oscSender.sendMessage(m, false);
}

void Data::setCodeWidth(string code){

}

bool Data::isNumber(const string &s){
    for (char const &ch : s) {
            if (isdigit(ch) == 0)
                return false;
        }
        return true;
}

void Data::testArduino(){
        //serial.listDevices();
        if (!serial.isInitialized()) {
            vector<ofSerialDeviceInfo> devices = serial.getDeviceList();

        for (auto& device : devices) {
            string portName = device.getDeviceName();
                if (portName.compare(3, 3, "ACM") == 0) {
                serial.setup(portName, 115200);  // Adjust the baud rate if needed

                if (serial.isInitialized()) {
                    cout << "Arduino connected on port: " << device.getDeviceName() << endl;
                    this->barduino = true;
                    break;
                    }
                else {
                    this->barduino = false;
                    }
            }
        }
        }
    /*
        serial.setup(this->arduinoPort, 115200);
        int testByte = 0;
        testByte = serial.readByte();
        if (testByte == OF_SERIAL_ERROR){
            this->barduino = false;
            cout << "no arduino found, sorry no push button :-(" << endl;
        }
        else {
            this->barduino = true;
            cout << "arduino ready to get pushed !" << endl;
        }*/
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


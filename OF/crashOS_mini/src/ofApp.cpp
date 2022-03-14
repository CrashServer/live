#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    ofSetFrameRate(60);
    // init variable
    //activeServer = false;

    // arduino
    // serial.setup("/dev/ttyACM0", 115200);
    serial.setup(0, 115200);

    // OSC & UDP
    ofxUDPSettings settings;
    settings.receiveOn(PORTUDP);
    settings.blocking = false;
    udpConnection.Setup(settings);
}


//--------------------------------------------------------------
void ofApp::update(){

    // Osc & udp & arduino
    getData();
   }


//--------------------------------------------------------------
void ofApp::draw(){

}

//--------------------------------------------------------------
void ofApp::getData(){
    // Arduino
//    if (serial.available()){
//        char button = serial.readByte();
//            if (button == 's' && !activeServer){
//                activeServer = true;
//                }
//            else if (button == 'c' && activeServer){
//                activeServer = false;
//                }
//            }

    // Udp Code player *2 + Code Server
    char udpMessage[500];
    udpConnection.Receive(udpMessage,500);
    string message=udpMessage;
    char *msgType = &message[0];
    if (message!=""){
        if (*msgType == '#'){ // player 1
            serial.writeByte('g'); // send arduino
            cout << "SVDK : " + message.erase(0,1) << endl;
            }
        else if (*msgType == '!'){ // player 2
            serial.writeByte('o'); // send Arduino
            cout << "ZBDM : " + message.erase(0,1) << endl;
            }
        else if (*msgType == '@'){ // server code
            serial.writeByte('r'); // send Arduino
            cout << "SERVER : " + message.erase(0,1) << endl;
            }
        }
}

//-------------------------
void ofApp::exit(){
}


//--------------------------------------------------------------
void ofApp::keyPressed(int key){
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){

}

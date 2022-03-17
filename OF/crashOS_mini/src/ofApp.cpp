#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    ofSetFrameRate(5);
    // init variable
    //activeServer = false;

    // arduino
    // serial.setup("/dev/ttyACM0", 115200);
    serial.setup(0, 115200);

    // OSC & UDP
    ofxUDPSettings settings;

    ofxUDPManager manager;
//    manager.SetNonBlocking("true");
//    manager.
    settings.receiveOn(PORTUDP);

    //settings.blocking = true;
    udpConnection.SetNonBlocking(true);
    udpConnection.Setup(settings);
}


//--------------------------------------------------------------
void ofApp::update(){



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
    char udpMessage[5000];
    string message;
    string tempMessage;
    bool getNext = true;

    while(getNext){
        udpConnection.Receive(udpMessage,5000);
        tempMessage = udpMessage;
        if (tempMessage==""){
            getNext = false;
        }
        else {
            message = tempMessage;
        }
    }

        char *msgType = &message[0];
        if (message!=""){
            if (*msgType == '#'){ // player 1
                serial.writeByte('g'); // send arduino
                serial.flush();
                cout << "\033[32mSVDK : \033[0m" + message.erase(0,1) << endl;
                }
            else if (*msgType == '!'){ // player 2
                serial.writeByte('o'); // send Arduino
                serial.flush();
                cout << "\033[33mZBDM : \033[0m" + message.erase(0,1) << endl;
                }
            else if (*msgType == '@'){ // server code
                serial.writeByte('r'); // send Arduino
                serial.flush();
                string randomServerCode = "\033[" + ofToString(int (ofRandom(1,100))) + "m";

                cout << randomServerCode + "SERVER : " + message.erase(0,1) + "\033[0m"<< endl;
                }
              }
        else {serial.flush();}
    }


//        if (message!=""){
//            serial.writeByte('g'})
//            if (*msgType == '#'){ // player 1
//               serial.writeByte('g'); // send arduino
//                }
//            else if (*msgType == '!'){ // player 2
//                serial.writeByte('o'); // send Arduino
//                }
//            else if (*msgType == '@'){ // server code
//                serial.writeByte('r'); // send Arduino
//                }
//            }




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

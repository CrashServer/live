//#include "ofApp.h"
#include "textris.h"


Textris::Textris(){
}

void Textris::setup(vector<ofColor> playerColor){
    font.load("PressStart2P_Regular.ttf", 16, true, false);
    box2d.init();
    box2d.setGravity(0,30);
    box2d.createBounds();
    box2d.setFPS(30.0);

    boxErase = (int) ofRandom(5,maxBox);
    this->zbdmColor = playerColor[0];
    this->svdkColor = playerColor[1];
    this->serverColor = playerColor[2];

//    for (int i=0; i<FFT_BANDS; i++){
//        groundLine.addVertex(i*ofGetWidth()/FFT_BANDS,0);
//}
}

void Textris::update(vector<float> fftSubbands){
    for (std::vector<int>::size_type i=0; i != particles.size(); i++){
        particles[i].update();
    }
    if (!particles.empty() && (particles.back().position[1] < 0)){
        particles.clear();
    }
    box2d.update();
//    fftBand = fftSubbands;

//    ground.clear();
//    ground.addVertices(groundLine);
    //ground.addVertexes(groundLine);
//    ground.create(box2d.getWorld());
}

void Textris::clear(){
    if ((int) rectangles.size() > boxErase){
        rectangles.erase(rectangles.begin(), rectangles.begin()+ boxErase);
        for (int i=0; i < (int) ofMap(500*boxErase, 0, maxBox*500, 0, maxParticles, true); i++){
            particle newParticle(ofRandom(0,ofGetWidth()), ofGetHeight());
            particles.push_back(newParticle);
        }
        boxErase = (int) ofRandom(5,maxBox);
    }

}

void Textris::addText(string textrisText, char player){
    this->msgTxt = textrisText;

    // add random new line or cut if > 100;
//    if (msgTxt.size() > 100){
//        msgTxt.resize(100);
//    }
    msgTxt = insertNewlines(msgTxt, (int) ofRandom(5,35));
    textVect = ofSplitString(msgTxt, "\n");
    for (auto& l : textVect){
        l = ofTrim(l);
    }

    // get the size of the msg text
    rect = font.getStringBoundingBox(msgTxt, 0,0);
    rect.width += padding*2;
    rect.height += padding*3;

    ofColor playerColor;
    if (player=='!'){
        playerColor = zbdmColor;}
    else if (player=='#'){
        playerColor = svdkColor;
    }
    else if (player=='@'){
        playerColor = ofColor::red;
    }

    // add to vector
    auto box = std::make_shared<CustomBox>(box2d.getWorld(),
                ofGetWidth()/2, 15, rect.width, rect.height, textVect, playerColor);
    rectangles.push_back(box);
}

void Textris::draw(){
    for(auto & box : rectangles) {
        box->draw(&font);
    }
    for (std::vector<int>::size_type i=0; i != particles.size(); i++){
        particles[i].draw();
    }

//    if (ofGetFrameNum()%4==0){
//    for (int i=groundLine.size(); i>=1; i--){
//        groundLine[i].y = ofGetHeight()-(fftBand[i]*ofGetHeight()/4);
//    }
//    }
//    ofSetColor(ofColor::white);
//    ground.updateShape();

//    ground.draw();
//    for (int i=0; i<16; i++){
//        ofDrawRectangle(i*(ofGetWidth()/16), ofGetHeight(), ofGetWidth()/16, fftSubbands[i]*(ofGetHeight()/8)*-1);
//        }
}


// return a text with a new line every x
string Textris::insertNewlines(string in, const size_t every_n)
{
    string out;
    out.reserve(in.size() + in.size() / every_n);
    for(std::string::size_type i = 0; i < in.size(); i++) {
        if (!(i % every_n) && i) {
            out.push_back('\n');
        }
        out.push_back(in[i]);
    }
    return out;
}

particle::particle(int startx, int starty){
    position = glm::vec2(startx, starty);
    force = glm::vec2(0,-0.2);
    direction = glm::vec2(ofRandom(-2.0,2.0), ofRandom(-10.0,10.0));
    size = 10;
    particleColor.setHsb(120, ofRandom(0,255), 255, 200);
}

particle::~particle(){}

void particle::update(){
    position += direction;
    direction += force;
    if (size > 0.1){
        size -= 0.1;
    }
    float brightness = particleColor.getBrightness();
    float hue = particleColor.getHue();

    if (brightness > 20){
        hue -=0.5;
        particleColor.setHue(hue);
    }
}

void particle::draw(){
    ofFill();
    ofSetColor(particleColor);
    ofDrawCircle(position, size);
}

#include <FastLED.h>

FASTLED_USING_NAMESPACE

#define DATA_PIN 3
#define LED_TYPE WS2812B
#define COLOR_ORDER GRB
#define NUM_LEDS 300
#define PLY_LENGTH 50  // define the length of the players position
#define BUTTON 2
#define LEDOUT 13

//CRGB leds[NUM_LEDS];
CRGBArray<NUM_LEDS> leds;
CRGB plyColor[] = { 0xFF0000, 0x7CFC00, 0x37B5F0 };          // color zbdm, svdk, server
CRGBSet metaBrain(leds(PLY_LENGTH, NUM_LEDS - PLY_LENGTH));  // Central meta brain Server led
//CHSV metaColor = CHSV(42,100,100);
CHSV metaColor[] = { CHSV(70, 150, 1), CHSV(60, 155, 255), CHSV(40, 255, 255), CHSV(20, 155, 255), CHSV(0, 255, 255), CHSV(224, 255, 255) };
uint8_t metaIndex = 0;
uint16_t metaSpeed[] = {4,10,30,60,120,240};

const uint8_t nbrPulseMax = 12;
int pos[nbrPulseMax];
bool activePulse[nbrPulseMax];
CRGB color[nbrPulseMax];
uint8_t ply[nbrPulseMax];
uint8_t prevButtonState = 0;
uint8_t switchTimer = 0;
uint8_t buttonState = 0;
char val = 'g';


/// Color & ply index ///
/// ZBDM -> 1
/// SVDK -> 2
/// SERVER -> 0

void setup() {
  delay(3000);  // 3 second delay for recovery
  Serial.begin(115200);
  pinMode(BUTTON, INPUT);
  pinMode(LEDOUT, OUTPUT);
  
  FastLED.setBrightness(96);
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  for (int i = 0; i < nbrPulseMax; i++) {
    pos[i] = 0;
    activePulse[i] = false;
    ply[i] = 4;
    color[i] = CRGB(0x000000);  // black
  }
}

void loop() {
  buttonState = digitalRead(BUTTON);
  if (buttonState != prevButtonState){
    switchTimer =0;
    prevButtonState = buttonState;
  }
  if(buttonState == 1){
    digitalWrite(LEDOUT, HIGH);
    if (switchTimer < 10) {
      Serial.write('s');
      switchTimer ++;
    }
  }
  else {
    digitalWrite(LEDOUT, LOW);
    if (switchTimer < 10) {
      Serial.write('c');
      switchTimer++;  
    }
  }
 
  FastLED.show();
  // insert a delay to keep the framerate modest
  FastLED.delay(1000 / 120);
  fadeToBlackBy(leds, NUM_LEDS, 20);

  metaBrain = metaColor[metaIndex];
  metaColor[metaIndex].v = (beatsin16(metaSpeed[metaIndex], 0, 255));
  
  if (Serial.available() > 0) {
    val = Serial.read();
    //// ZBDM /////
    if (val == 'v') {  ///
      for (int i = 0; i < nbrPulseMax; i++) {
        if (!activePulse[i]) {
          activePulse[i] = true;
          pos[i] = 0;
          color[i] = plyColor[2];  // GREEN  0xFFA500 // CRGB(0x37B5F0); // Blue //
          ply[i] = 1;
          break;
        }
      }
    }
    //// SVDK ////
    else if (val == 'z') {
      for (int i = 0; i < nbrPulseMax; i++) {
        if (!activePulse[i]) {
          activePulse[i] = true;
          pos[i] = NUM_LEDS;
          color[i] = plyColor[1];  // ORANGE CRGB(0xE027F5); // Viiolet //
          ply[i] = 2;
          break;
        }
      }
    }
    //// SERVER ////
    else if (val == 's') {
      for (int i = 0; i < nbrPulseMax+1; i++) {
        if (!activePulse[i]) {
          activePulse[i] = true;
          activePulse[i + 1] = true;
          pos[i] = PLY_LENGTH;
          pos[i + 1] = NUM_LEDS - PLY_LENGTH;
          color[i] = plyColor[0];      // RED
          color[i + 1] = plyColor[0];  // RED
          ply[i] = 0;
          ply[i + 1] = 0;
          metaBrain = CHSV(0,0,255);
          break;
        }
      }
    }
    // ////  SERVER STATE ////
    else if (val == 'a') {  // 0 -> 20%
      metaIndex = 0;
    }
    else if (val == 'b') { // 20 - 40%
      metaIndex = 1;
    }
    else if (val == 'c') { // 40 - 60 %
      metaIndex = 2;
    }
    else if (val == 'd') { // 60 - 80 %
      metaIndex = 3;
    }
    else if (val == 'e') { // 80 - 100%
      metaIndex = 4;
    }
    else if (val == 'f') { // 100% - more
      metaIndex = 5;
    }
    }

  if (val != -1) {
    //if (val == 'g'|| val == 'o' || val == 'r'){
    for (int i = 0; i < nbrPulseMax+1; i++) {
      if (activePulse[i]) {
        leds[pos[i]] = color[i];
        if (ply[i] == 1) {
          pos[i]++;
          if (pos[i] > PLY_LENGTH) {
            pos[i] = 0;
            activePulse[i] = false;
            if(metaIndex > 0){metaBrain = CHSV(0,0,255);}
          }
        } else if (ply[i] == 2) {
          pos[i]--;
          if (pos[i] < NUM_LEDS - PLY_LENGTH) {
            pos[i] = 0;
            activePulse[i] = false;
            if(metaIndex > 0){metaBrain = CHSV(0,0,255);}
          }
        } else if (ply[i] == 0 && ply[i + 1] == 0) {
          pos[i]--;
          pos[i + 1]++;
        }
        if (pos[i] > NUM_LEDS || pos[i] < 0) {
          pos[i] = 0;
          activePulse[i] = false;
        }
      }
    }
    //}
  }


  //  metaBrain = metaColor;
  //  metaColor.v = (beatsin16(10,0,255));
  /*
  for (int i=PLY_LENGTH+1; i<NUM_LEDS-PLY_LENGTH+1; i++){
    leds[i] = CRGB(0xFFD076);*/
}

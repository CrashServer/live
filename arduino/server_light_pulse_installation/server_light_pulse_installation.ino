#include <FastLED.h>

FASTLED_USING_NAMESPACE

#define DATA_PIN    3
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB
#define NUM_LEDS    450

CRGB leds[NUM_LEDS];

const uint8_t nbrPulseMax = 20;
int pos[nbrPulseMax];
bool activePulse[nbrPulseMax]; 
CRGB color[nbrPulseMax];
char val = 'g';

void setup() {
 delay(3000); // 3 second delay for recovery
 Serial.begin(115200);
  
 // tell FastLED about the LED strip configuration
 FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  // set master brightness control
  FastLED.setBrightness(96);
  for (int i=0; i<nbrPulseMax; i++){
    pos[i] = 0;
    activePulse[i] = false;
    color[i] = CRGB(0x000000); // black
    }
  
}

void loop() {
    
  FastLED.show();  
  // insert a delay to keep the framerate modest
  FastLED.delay(1000/120); 
  fadeToBlackBy( leds, NUM_LEDS, 20);
if (Serial.available()>0) {
    val = Serial.read();
     if (val == 'g'){
      for (int i=0; i < nbrPulseMax; i++){
          if(!activePulse[i]){
            activePulse[i] = true;
            color[i] = CRGB(0x7CFC00); // GREEN CRGB(0x37B5F0); // Blue //
          break;
          }
         }
      }
     else if (val == 'o'){
      for (int i=0; i < nbrPulseMax; i++){
          if(!activePulse[i]){
            activePulse[i] = true;
            color[i] = CRGB(0xFFA500);  // ORANGE CRGB(0xE027F5); // Viiolet // 
          break;
            }
          }
     }  
     else if (val == 'r'){
           for (int i=0; i < nbrPulseMax; i++){
          if(!activePulse[i]){
            activePulse[i] = true;
            //color[i] = CRGB(0xFF0000);   // RED
            color[i] = CHSV(random8(), 255, 255);   // RED
          break;
          }
         }
      }
}
if (val!=-1){
   if (val == 'g'|| val == 'o' || val == 'r'){
      for (int i=0; i < nbrPulseMax; i++){
        if (activePulse[i]){
          leds[pos[i]] = color[i];         
          pos[i]++;
          if (pos[i]>NUM_LEDS){
            pos[i]=0;
            activePulse[i]=false;      
            }
         }
      }
    }
  }
}  

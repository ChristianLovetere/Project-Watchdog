/*
 
  NeoPixel LEDs
 
  modified on 7 May 2019
  by Saeed Hosseini @ Electropeak
  https://electropeak.com/learn/
 
*/
 
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif
 
#define PIN        7
#define NUMPIXELS 60
 
 
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
 
void NeoBlink(int num, int wait)
{
  for (int j = 0; j < num; j++)
  {
    pixels.setPixelColor(j, 255,85,5);
  }
  pixels.show();
  delay(wait);
}
 
void setup()
{
  pixels.begin();
  pixels.setBrightness(80);
}
 
void loop()
{
  NeoBlink(60, 500);
}
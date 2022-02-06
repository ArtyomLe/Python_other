#include <FastLED.h>
#define LENGTH_LED 14
#define PIN_LED 7

CRGB leds[LENGTH_LED];
String msg = "";
byte parseStart = 0;

void setup() {
  FastLED.addLeds<NEOPIXEL, PIN_LED>(leds, LENGTH_LED);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available())
  {
    char in = Serial.read();
    if(!(in == '\n' || in == '\r'))
    {
      if(in == ';')
      {
        parseStart = 1;
      }
      if(in == '#')
      {
        parseStart = 2;
      }
      if((parseStart == 2) && (in != '#'))
      {
        msg += in;
      }
    }
  }
  if(parseStart == 1)
  {
    int message = msg.toInt();
    // Указываем(ограничиваем) ширину экрана
    if(message < 200) message = 200;
    if(message > 600) message = 600;
    // Преобразуем значения
    message = map(message, 200, 600, 0, 255);
    for(int led = 0; led < LENGTH_LED; led++)
    {
      leds[led] = CHSV(96, 255, message); //(цвет, насыщенность, яркость)
    }
    FastLED.show();
    parseStart = 0;
    msg = ""; 
  }
}
//========================================================================================

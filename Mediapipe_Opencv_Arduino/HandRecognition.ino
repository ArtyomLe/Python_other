#include <FastLED.h>      // подключаем библиотеку управления лентой
#define LENGTH_LED 14     // количество светодиодов в ленте
#define PIN_LED 7         // управляющий пин ленты

CRGB leds[LENGTH_LED];

String msg;             // переменная для хранения сообщения
byte parseStart = 0;    // переменная запуска парсинга

bool colorLED = 0;      // флаг управления цветом ленты
bool powerLED = 0;      // флаг управления яркостью ленты

int prevPower = 0;      // хранение предыдущего значения яркости
int prevColor = 0;      // хранение предыдущего значения цвета

void setup() 
{
  FastLED.addLeds<NEOPIXEL, PIN_LED>(leds, LENGTH_LED);           // FastLED.addLeds - инициализация ленты, <NEOPIXEL> - Адресная лента типа WS2812B 
  Serial.begin(9600);
}

void loop() 
{
  if (Serial.available())                 //  если что-то пришло в Serial-порт
  {
    char in = Serial.read();              //  читаем один байт (символ)
    if (!(in == '\n' || in == '\r'))      //  отсеиваем символы возврата картеки и переноса строки
    {
        switch (in)       // в зависимости от принятого символа, делаем выбор
        {
            case '@': parseStart = 0; msg = ""; koza(); break;  // символ "коза"
            case '^': parseStart = 0; msg = ""; like(); break;  // символ "лайк"
            case ';': parseStart = 1; break;                    // окончание сообщения
            case '#': parseStart = 2;  powerLED = 1; break;     // начало сообщения (управляем яркостью)
            case '$': parseStart = 2;  colorLED = 1; break;     // начало сообщения (управляем цветом)
        }

        // если парсинг запущен и это не символы начала или окончания посылки (т.е идёт передача (значений)координат пальцев на экране)
        if ((parseStart == 2) && (in != '#') && (in != '$') && (in != '^') && (in != '@')) 
        {  
          msg += in;    // запоминаем переданное число (складываем по одному байту в общую строку)
        }
     }
  }
  
  if(parseStart == 1)   //  если прием остановлен
  {
      int message = msg.toInt();                          // преобразуем полученную строку в целое число
      // ВАЖНО мин и макс пареметры зависят от разрешения веб камеры(нужно подбирать индивидуально)
      if (message < 50) message = 50;                     // защита от выхода руки слева
      if (message > 450) message = 450;                   // защита от выхода руки справа
      message = map(message, 50, 450, 0, 255);            // преобразуем принятые координаты в значения яркости от 0 до 255
       
      for(int led = 0; led < LENGTH_LED; led++)           // перебираем светодиоды ленты
      {
        if(powerLED)                                 //если был флажок управления яркостью
        {
          leds[led] = CHSV(prevColor, 255, message); // задаем предыдущее значение цвета и меняем яркость на новую "CHSV(цвет, насыщенность, яркость)"
          prevPower = message;                       // запоминаем новое значение яркости
        }
        if(colorLED)                                 //если был флажок управления цветом
        {
          leds[led] = CHSV(message, 255, prevPower); // задаем предыдущее значение яркости и меняем цвет на новый
          prevColor = message;                       // запоминаем новое значение цвета ленты
        }
      }
      FastLED.show();   //  отображаем изменения на ленте
      colorLED = 0;
      powerLED = 0;
      parseStart = 0;
      msg = ""; 
    }   
}

void koza() // случайно переключающиеся синие огоньки
{
  for (int i = 0; i < LENGTH_LED; i++ ) 
  {
    int temprand = random(0, 100);
    if (temprand > 50) 
    {
      leds[i].b = 255;               // .b = blue
    }
    if (temprand <= 50) 
    {
      leds[i].b = 0;                
    }
    leds[i].r = 0;                   // .r = red
    leds[i].g = 0;                   // .g = green
  }
  LEDS.show();
}


void like()
{
    CRGBPalette16 currentPalette;
    TBlendType    currentBlending;
    
    extern CRGBPalette16 myRedWhiteBluePalette;
    extern const TProgmemPalette16 myRedWhiteBluePalette_p PROGMEM;

    currentPalette = RainbowStripeColors_p;
    currentBlending = LINEARBLEND; 
    static uint8_t colorIndex = 0;
    colorIndex = colorIndex + 1;
    
    uint8_t brightness = 255;
    
    for( int i = 0; i < LENGTH_LED; i++) {
        leds[i] = ColorFromPalette( currentPalette, colorIndex, brightness, currentBlending);
        colorIndex += 3;
    }
    
    FastLED.show();
    FastLED.delay(1);
}

#include <DHT.h>
#include <LiquidCrystal_I2C.h> 

LiquidCrystal_I2C lcd(0x27, 16, 2);

// inicializando os componentes
const uint8_t ledverde = 19;  
const uint8_t ledazul = 18;   
const uint8_t buttonPin1 = 2;
const uint8_t buttonPin2 = 15;
const uint8_t dhtPin = 4;
const uint8_t photoresistorPin = 34;
const uint8_t relayPin = 5;  

#define DHTTYPE DHT22
DHT dht(dhtPin, DHTTYPE);

// Colocando um valor aleatório para umidade
float humidity = 32.0; 

// Contador de pressionamentos do botão
uint8_t buttonPressCount = 0; 
bool lastButtonState2 = HIGH; 

// Variáveis para o temporizador
unsigned long relayOnTime = 0;  
const unsigned long relayTimeout = 30000;  // Constante para timeout de 30 segundos

void setup() {
    lcd.init();
    lcd.backlight();

    pinMode(ledverde, OUTPUT);
    pinMode(ledazul, OUTPUT);
    pinMode(buttonPin1, INPUT_PULLUP);
    pinMode(buttonPin2, INPUT_PULLUP);
    pinMode(photoresistorPin, INPUT);
    pinMode(relayPin, OUTPUT);
    digitalWrite(relayPin, LOW); 
    Serial.begin(9600);
    Serial.println("todos os leds estao apagados, inicializando!");
    dht.begin();
}

void loop() {
    // Verifica e imprime o status do relé
    if (digitalRead(relayPin) == HIGH) {
        Serial.println("Relay is ON");
    } else {
        Serial.println("Relay is OFF");
    }

    uint8_t buttonState1 = digitalRead(buttonPin1); 
    uint8_t buttonState2 = digitalRead(buttonPin2); 

    if (buttonState1 == LOW) {
        digitalWrite(ledverde, HIGH);
        Serial.println("LED verde está aceso! Nutriente Fósforo coletado");
    } else {
        digitalWrite(ledverde, LOW);
    }

    if (buttonState2 == LOW && lastButtonState2 == HIGH) {
        buttonPressCount++; // Incrementa o contador de pressionamentos
        Serial.print("Botão de coleta de Potássio pressionado ");
        Serial.print(buttonPressCount);
        Serial.println(" vezes.");
        
        // Verifica se o botão foi pressionado 3 vezes
        if (buttonPressCount >= 3) {
            // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
            uint16_t lightLevelRaw = analogRead(photoresistorPin); 
            uint8_t lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100);
            uint8_t lightLevelOutOf14 = lightLevelPercentage * 14 / 100;

            // Verifica se o nível de luz é superior a 2
            if (lightLevelOutOf14 > 2) {
                Serial.println("-------------------------------------------------------");
                Serial.println("Está na hora de irrigar. Processo de irrigação ativado!");
                Serial.println("-------------------------------------------------------");
                digitalWrite(relayPin, HIGH);  // Liga o relay
                relayOnTime = millis();  // Salva o tempo em que o relay foi ligado
                buttonPressCount = 0;
            } else {
                Serial.println("Ainda não é hora de irrigar.");
            }
        }
    }

    digitalWrite(ledazul, buttonState2 == LOW ? HIGH : LOW);
    if (buttonState2 == LOW) {
        Serial.println("LED azul está aceso, nutriente Potássio coletado!");
    }

    // Verifica se já passou o tempo de 300 segundos para desligar o relé
    if (digitalRead(relayPin) == HIGH) {
        if (millis() - relayOnTime >= relayTimeout) {
            digitalWrite(relayPin, LOW);  // Desliga o relay após 30 segundos
            Serial.println("Relé desligado após 30 segundos.");
        }
    }

    // Ler o valor do fotoresistor e converter para porcentagem de nível de luz
    uint16_t lightLevelRaw = analogRead(photoresistorPin);
    uint8_t lightLevelPercentage = map(lightLevelRaw, 0, 4095, 0, 100);
    uint8_t lightLevelOutOf14 = lightLevelPercentage * 14 / 100;

    // Exibir o nível de luz em uma escala de 0 a 14
    Serial.print("Nível de luz (no caso, pH) em uma escala de 0 a 14: ");
    Serial.println(lightLevelOutOf14);

    if (isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
    } else {
        Serial.print("A medição da humidade está em: ");
        Serial.print(humidity);
        Serial.println(" %, desde a última medição");
    }

    lastButtonState2 = buttonState2;
    delay(2000);

    lcd.setCursor(0, 0);
    lcd.print("Luminosidade: ");
    lcd.print(lightLevelOutOf14); 
    lcd.setCursor(0, 1);
    lcd.print("Umidade: ");
    lcd.print(humidity, 0); 
    delay(2000);
    lcd.clear();
}

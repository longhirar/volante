#define ENCODER_OPTIMIZE_INTERRUPTS 
#include <Encoder.h>

#define btnA_pin 8
#define btnB_pin 9
#define btnX_pin 10
#define btnY_pin 11

Encoder steering(2,3);

bool btnA = false;
bool btnB = false;
bool btnX = false;
bool btnY = false;

void setup() {
  Serial.begin(115200);
  digitalWrite(12, true); // VCC for ABXY buttons
}
void loop() {
  Serial.println(steering.read());

  if (btnA != digitalRead(btnA_pin)) {
    btnA = !btnA;
    if (btnA) {
      Serial.println("uA");
    } else {
      Serial.println("dA");
    }
  }

  if (btnB != digitalRead(btnB_pin)) {
    btnB = !btnB;
    if (btnB) {
      Serial.println("uB");
    } else {
      Serial.println("dB");
    }
  }

  if (btnX != digitalRead(btnX_pin)) {
    btnX = !btnX;
    if (btnX) {
      Serial.println("uX");
    } else {
      Serial.println("dX");
    }
  }

  if (btnY != digitalRead(btnY_pin)) {
    btnY = !btnY;
    if (btnY) {
      Serial.println("uY");
    } else {
      Serial.println("dY");
    }
  }
}

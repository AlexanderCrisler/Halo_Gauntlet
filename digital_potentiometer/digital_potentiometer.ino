#include <C:\Users\alexc\Documents\Programming\Python\Halo_Gauntlet\digital_potentiometer\X9C.h>

const int tranPin = 2;

void pulse(int pin, int repititions) {
  for(int i = 0; i < repititions; i++){
    digitalWrite(pin, HIGH);
    delay(100);
    digitalWrite(pin, LOW);
    delay(100);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);

  pinMode(tranPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // see if there's incoming serial data:
  if (Serial.available() > 0)
  {
    // read the string in the serial buffer:
    String incomingString = Serial.readString();
    int incomingInt = incomingString.toInt();

    if (incomingInt == 1){
      pulse(tranPin, 5);
      Serial.println(incomingInt);
    }
    else if (incomingInt == 2){
      pulse(tranPin, 4);
      Serial.println(incomingInt);
    }
    else if (incomingInt == 3){
      pulse(tranPin, 3);
      Serial.println(incomingInt);
    }
    else if (incomingInt == 4){
      pulse(tranPin, 2);
      Serial.println(incomingInt);
    }
    else if (incomingInt == 5){
      pulse(tranPin, 1);
      Serial.println(incomingInt);
    }
    else
    {
      //digitalWrite(tranPin, LOW);
      Serial.write("INVALID INPUT.");
    }
  }
}

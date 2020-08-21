#include <C:\Users\alexc\Documents\Programming\Python\Halo_Gauntlet\digital_potentiometer\X9C.h>

const int tranPin = 2;

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
      digitalWrite(tranPin, HIGH);
      Serial.println(incomingInt);
    }
    else
    {
      digitalWrite(tranPin, LOW);
      Serial.write("INVALID INPUT.");
    }
  }
}

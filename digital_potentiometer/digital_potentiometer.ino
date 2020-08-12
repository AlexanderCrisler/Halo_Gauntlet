#include <C:\Users\alexc\Documents\Programming\Python\Halo_Gauntlet\digital_potentiometer\X9C.h>

X9C pot;
const int inc = 2, ud = 4, cs = 7;
const int mySize = 3;
int incomingByte[mySize];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
 
  pot.begin(cs, inc, ud);
 
  pot.setPotMax();
  
}

void loop() {
  // put your main code here, to run repeatedly:

  // see if there's incoming serial data:
  if (Serial.available() > 0)
  {
    // read the string in the serial buffer:
    String incomingString = Serial.readString();
    int incomingInt = incomingString.toInt();

    if (incomingInt >= 1 && incomingInt <= 100){
      pot.setPot(incomingInt);
      Serial.println(incomingInt);
    }
    else
    {
      Serial.write("INVALID INPUT.");
    }

  }
}

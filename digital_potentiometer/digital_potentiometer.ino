#include <C:\Users\alexc\Documents\Programming\Python\Halo_Gauntlet\digital_potentiometer\X9C.h>

X9C pot;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9200);
  int inc = 2, ud = 4, cs = 7;
 
  pot.begin(cs, inc, ud);
 
  pot.setPot(1);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  pot.setPot(1);
  delay(2000);
  pot.setPot(2);
  delay(2000);
  pot.setPot(3);
  delay(2000);
  pot.setPot(4);
  delay(2000);
  pot.setPot(5);
  delay(2000);

}

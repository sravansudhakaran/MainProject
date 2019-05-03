#include <dht.h>
#define dht_pin A2

dht DHT;
int vbe_pin = A0;
int vce_pin = A1;
int vbe_val = 0;
int vce_val = 0;
 
void setup(){
Serial.begin(9600);
}
 

void loop(){

vbe_val = analogRead(vbe_pin);
vce_val = analogRead(vce_pin);
DHT.read11(dht_pin);

//Serial.print("Temperature :");
Serial.print(DHT.temperature);
Serial.print(",");
Serial.print(float(vbe_val)*(5.0/1024.0));
Serial.print(",");
Serial.println(float(vce_val)*(5.0/1024.0)*2.4);


delay(100);
}

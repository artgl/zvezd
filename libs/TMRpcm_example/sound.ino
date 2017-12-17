#include <SD.h>
#include <TMRpcm.h>

void setup() {
  // put your setup code here, to run once:

  tone(9, 4000);
  delay(200);
  noTone(9);
  delay(1000);

  Serial.begin(9600);

  SD.begin(8); // номер ножки CS
  if(SD.exists("test.wav"))
  {
    Serial.println("good");
  }
  else
  {
    Serial.println("bad");    
  }                           

  TMRpcm tmrpcm;  
  tmrpcm.speakerPin = 9;
  tmrpcm.setVolume(4);
  tmrpcm.play("test.wav"); 

}

void loop() {
  // put your main code here, to run repeatedly:

}

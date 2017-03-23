int myVar = 0;

//runs on reset
void setup() {
  Serial.begin(9600);
    
  for (int i = 0; i < 4; i++){//set pins to be used to OUPUT mode
   pinMode(13 - i * 2, OUTPUT); 
  }
  Serial.write('1');
}

// the loop routine runs over and over again forever:
void loop() {
  for (int count = 0; count < 4; count++){
    if (Serial.available() > 0){
      myVar = Serial.read() - '0';// convert from byte
      if(myVar){
       digitalWrite(13 - count * 2, HIGH);
      }
      else{
        digitalWrite(13 - count * 2, LOW);
      }
    }
    else{count--;}//loop until serial is available
  }
}

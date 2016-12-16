//stuff goes here
int myVar = 0;

//runs on reset
void setup() {
  Serial.begin(9600);
    
//set delay according to tempo
  for (int i = 0; i < 4; i++){
   pinMode(13 - i * 2, OUTPUT); 
  }
  Serial.write('1');
//read file with info
//create array of tracks, assign each track to a pin
}

// the loop routine runs over and over again forever:
void loop() {
  for (int count = 0; count < 4; count++){
    if (Serial.available() > 0){
      myVar = Serial.read() - '0';
      if(myVar){
       digitalWrite(13 - count * 2, HIGH);
      }
      else{
        digitalWrite(13 - count * 2, LOW);
      }
    }
    else{count--;}
  }
}

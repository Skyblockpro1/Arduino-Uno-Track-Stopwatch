// potentiometer.ino
// reads a potentiometer sensor and sends the reading over serial
int sensorV;
int c;
int sensorAct = A3;
int sensorPin = A2; // the potentiometer is connected to analog pin 0
int ledPin = 13; // the LED is connected to digital pin 13
int sensorValue; // an integer variable to store the potentiometer reading
void setup() { // this function runs once when the sketch starts up
  pinMode (ledPin, OUTPUT);
  // initialize serial communication :
  Serial.begin(9600);

  c=0;
  
  while(c==   0){
  sensorV = analogRead(sensorAct); // read the sensor
    if(sensorV==1023){
      c=1;}
    }
}



void loop(){  
  sensorValue = analogRead(sensorPin); // read the sensor
  Serial.println(sensorValue); // output reading to the serial line
  if (sensorValue < 900){
    digitalWrite(ledPin , LOW );} // turn the LED off
  else {
    digitalWrite(ledPin , HIGH );} // keep the LED on
  delay (25); // Pause in milliseconds before next reading
}

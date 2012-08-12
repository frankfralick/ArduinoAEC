/*
This Arduino sketch reads values from a sensor and sends it
out through serial.

Based on example code by Tom Igoe.
 
 */

// A0 will be the pin the sensor will be connected to.
//If using a 3 pin pot or sensor, typically the middle pin
//will be the one to connect to A0.  One of the other pins
//needs to be connected to +5, and the other pin to ground.
const int analogInPin = A0;  

//If you would like to also write the sensor/pot value out to 
//another piece of hardware like a servo or LED, uncomment the following line.

//const int analogOutPin = 9; 

//first we initialize some variables
int sensorValue = 0;        
int outputValue = 0;

void setup() {
  // initialize serial with a baud rate of 9600
  Serial.begin(9600); 
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);  
  
  //If yoi want to send values out of pin 9, uncomment the following line.  
  //analogWrite(analogOutPin, outputValue);           

  // print the results to the serial monitor:
  Serial.print("sensor = " );                       
  Serial.print(sensorValue);      
  Serial.print("\t output = ");      
  Serial.println(outputValue);   

//Setting the delay amount controls how often "serial.Serial.readline()" in our Python 
//program will return a series of values.  The effect is that the higher this number is, the
//slower the model will update its position.  Currently this is set for .25 seconds.
  delay(250);                     
}

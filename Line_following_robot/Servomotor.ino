#include<Servo.h>
Servo servoright;
Servo servoleft;

void setup() {  
  Serial.begin(115200);
  servoright.attach(12);
  servoleft.attach(13);
}

void loop() { 
  if(Serial.available()){
    char msg = Serial.read();
    //reverse();
    switch(msg){
      case 'W':
        forward();
        break;
      case 'D':
        turnRight();
        break;
      case 'A':
        turnLeft();
        break;
    }
  }
}

void forward()                       
{
  servoleft.writeMicroseconds(1530);         
  servoright.writeMicroseconds(1470);        
}

void turnRight()                     
{
  servoleft.writeMicroseconds(1530);         
  servoright.writeMicroseconds(1530);       
}

void turnLeft()                     
{
  servoleft.writeMicroseconds(1470);         
  servoright.writeMicroseconds(1470);       
}

void reverse()
{
  servoleft.writeMicroseconds(1470);           
  servoright.writeMicroseconds(1530);
}

void stop()                         
{
  servoleft.writeMicroseconds(1500);         
  servoright.writeMicroseconds(1500);       
} 

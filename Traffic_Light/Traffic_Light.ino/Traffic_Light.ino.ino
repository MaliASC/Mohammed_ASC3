int carRed = 12;
int carYellow = 11;
int carGreen = 10;
int pedRed = 8; 
int pedYellow = 9; 
int button = 2;
int crossTime = 5000;
int buttonState;  
unsigned long changeTime ; 

void setup () {
  pinMode(carRed, OUTPUT);
  pinMode(carYellow, OUTPUT);
  pinMode(carGreen, OUTPUT);
  pinMode(pedRed, OUTPUT);
  pinMode(pedYellow, OUTPUT);
  pinMode(button, INPUT);
  
  //turn on the green
  digitalWrite(carGreen, HIGH);
   //turn on the ped red LED
  digitalWrite(pedRed,HIGH);
 }

void loop(){
   
   //reads the button status if it is pressed or not
   buttonState = digitalRead(button);
   
   if (buttonState == HIGH){
       
           //turn off green and turn on yellow for 2 seconds
       digitalWrite(carGreen,LOW);
       digitalWrite(carYellow,HIGH);
       delay(2000);
       
       //turn off carYellow and turn on carRed for 1 second    
       digitalWrite(carYellow,LOW);
       digitalWrite(carRed,HIGH);
       delay(1000);
       
       //turn off ped red and turn on ped Yellow for  3second
       digitalWrite(pedYellow, HIGH);
       digitalWrite(pedRed,LOW);
       delay(3000);

       int i = 0;
        for (i=0;i<10;i+=1){
          digitalWrite(pedYellow,LOW);
          delay(100);
          digitalWrite(pedYellow,HIGH);
          delay(100);
        }
       
       //Turn off ped yellow and turn on ped red, turn on car green 
       digitalWrite(pedYellow,LOW);
       digitalWrite(pedRed,HIGH);
       digitalWrite(carRed,LOW);
       digitalWrite(carGreen,HIGH);

    }
}     

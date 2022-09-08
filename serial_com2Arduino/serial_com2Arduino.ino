
typedef struct{
  
   int16_t val;
   int16_t other_val;
   int16_t other_val2;
   
   uint16_t checksum;
   
   //int16_t a;
} SerialCommand;

SerialCommand Command;



typedef struct{
  
   int16_t val;
   int16_t other_val;
   int16_t other_val2;
   
   uint16_t checksum;
   
   //int16_t a;
} SerialCommand2;

SerialCommand2 Command2;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Command.val=(int16_t)15;
  Command.other_val=(int16_t)42;
  Command.other_val2=(int16_t)25;
  //Command.a=(int16_t)"Hello World";
  Command.checksum = (uint16_t)(Command.val^ Command.other_val ^ Command.other_val2);

  Command2.val=(int16_t)15;
  Command2.other_val=(int16_t)42;
  Command2.other_val2=(int16_t)25;
  //Command.a=(int16_t)"Hello World";
  Command2.checksum = (uint16_t)(Command2.val^ Command2.other_val ^ Command2.other_val2);
  
  
  Serial.write((uint8_t *) &Command, sizeof(Command));
  Serial.println();
  Serial.write((uint8_t *) &Command2, sizeof(Command2));
  Serial.println();
}



#define Sensor1 55
#define Sensor2 25

typedef struct {
  int x;
  int y;
}Point;
typedef struct{
   // arrangment is important our value list
  
    struct structVal{
    int x;
    int y;
  };
   
   int16_t val;
   int16_t other_val;
   int16_t other_val2;  
    Point point;
    structVal stcVal;
   // checksum is bellow must be
   uint16_t checksum;

 
} SerialCommand;

SerialCommand Command;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Command.val=(int16_t)15;
  Command.other_val=(int16_t)42;
  Command.other_val2=(int16_t)16;
  //Command.a=(int16_t)"Hello World";
  //Command.checksum = (uint16_t)(Command.val^ Command.other_val ^ Command.other_val2);

  Command.point.x=11;
  Command.point.y=12;

  Command.stcVal.x=21;
  Command.stcVal.y=22;
  
  Command.checksum=(uint16_t)Sensor1;
  
  Serial.write((uint8_t *) &Command, sizeof(Command));
  Serial.println();

}

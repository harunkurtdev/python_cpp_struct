

#define Sensor1 55
#define Sensor2 25

typedef struct {
  int x;
  int y;
}Point;
typedef struct{
  
   int16_t val;
   int16_t other_val;
   int16_t other_val2;  
   uint16_t checksum;

    struct structVal{
    int x;
    int y;
  };
 
    Point point;
    structVal stcVal;
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
  Command.other_val2=(int16_t)25;
  //Command.a=(int16_t)"Hello World";
  //Command.checksum = (uint16_t)(Command.val^ Command.other_val ^ Command.other_val2);

  Command.point.x=15;
  Command.stcVal.x=15;
  
  Command.checksum=(uint16_t)Sensor1;
  
  Serial.write((uint8_t *) &Command, sizeof(Command));
  Serial.println();

}

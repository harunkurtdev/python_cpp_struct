
import serial
import struct
try:
  ser = serial.Serial( # set parameters, in fact use your own :-)
    port="/dev/ttyUSB0",
    baudrate=9600,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
  )
  ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
  print ("port is opened!")

except IOError: # if port is already opened, close it and open it again and print message
  ser.close()
  ser.open()
  print ("port was already open, was closed and opened again!")


# typedef struct {
#   int x;
#   int y;
# }Point;
# typedef struct{
#    // arrangment is important our value list
  
#     struct structVal{
#     int x;
#     int y;
#   };
   
#    int16_t val;
#    int16_t other_val;
#    int16_t other_val2;  
#     Point point;
#     structVal stcVal;
#    // checksum is bellow must be
#    uint16_t checksum;

 
# } SerialCommand;

# serial_com2Arduino2

while True:
    val=ser.readline()
    # print(val)
    # https://docs.python.org/3/library/struct.html#format-characters
    """
    page is our c/cpp struct valuable datas
    """
    value=struct.unpack_from("HHHHHHHH",val)
    print(value) # read value
    print(value[7])
    
    if value[7]==55:
        print(value[0:3])
    else:
        print("not true val")

ser.close()
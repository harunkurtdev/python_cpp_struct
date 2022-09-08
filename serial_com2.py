
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
  
#    int16_t val;
#    int16_t other_val;
#    int16_t other_val2;  
#    uint16_t checksum;

#     struct structVal{
#     int x;
#     int y;
#   };
 
#     Point point;
#     structVal stcVal;
# } SerialCommand;

while True:
    val=ser.readline()
    # print(val)
    # https://docs.python.org/3/library/struct.html#format-characters
    """
    page is our c/cpp struct valuable datas
    """
    value=struct.unpack_from("HHHH",val)
    # print(value)
    if value[3]==25:
        print(value[0:3])
    elif value[3]==55:
        print(value[0:3])
    # if value[2]==
    else:
        print("not true val")
        # print(value[0:3])
    # print(value)

ser.close()
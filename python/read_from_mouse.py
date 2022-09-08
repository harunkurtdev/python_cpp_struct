
import struct


mouse=open('/dev/input/mice',"rb") #read byte

while True:
    
    event=mouse.read(3)
    # print(event)
    
    x,y=struct.unpack_from("bb",event[1:])# from byte read
    #currently mouse x and y position
    
    print(x,y)
    
mouse.close()
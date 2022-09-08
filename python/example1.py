import struct
  
  
# struct x{
#    short int; 
#    short int; 
#    l int; 
# }y;
# Format: h is short in C type
# Format: l is long in C type
# Format 'hhl' stands for 'short short long'
# var = struct.pack('hhl',1,2,3)

# print(var)
  
# Format: i is int in C type
# Format 'iii' stands for 'int int int'
  
# struct x{
#    int; 
#    int; 
#    int; 
# }y;
var = struct.pack('iii',2147483647,2,3)
print(var)

tup = struct.unpack('iii', var)
print(tup)


### MEMORY

List the amount of memory currently in use. For example: Program: 0K ( 0%) Program (0 lines) 180K (100%) Free Saved Variables: 16K (100%) Free RAM: 0K ( 0%) 0 Variables 0K ( 0%) General 228K (100%) Free Notes:  Memory usage is rounded to the nearest 1K byte.  General memory (RAM) is used by arrays, strings, serial I/O buffers, etc.

### MEMORY SET address, byte, numberofbytes

This command will set a region of memory to a value. BYTE = One byte per memory address.

### MEMORY SET BYTE address, byte, numberofbytes

SHORT = Two bytes per memory address. WORD = Four bytes per memory address. FLOAT = Eight bytes per memory address.

### MEMORY SET SHORT address, short, numberofshorts

‘increment’ is optional and controls the increment of the ‘address’ pointer as the operation is executed. For example, if increment=3 then only every third element of the target is set. The default is 1.

### MEMORY SET WORD address, word, numberofwords



### MEMORY SET INTEGER address, integervalue ,numberofintegers [,increment]



### MEMORY SET FLOAT address, floatingvalue ,numberofloats [,increment]



### MEMORY COPY sourceaddress, destinationaddres, numberofbytes [,sourceincrement][,destination increment]

This command will copy one region of memory to another. COPY INTEGER and FLOAT will copy eight bytes per operation. ‘sourceincrement’ is optional and controls the increment of the ‘sourceaddress’ pointer as the operation is executed. For example, if sourceincrement=3 then only every third element of the source will be copied. The default is 1. ‘destinationincrement’ is similar and operates on the ‘destinationaddress’ pointer.

### MEMORY COPY INTEGER sourceaddress, destinationaddress, numberofintegers [,sourceincrement][,destination increment]



### MEMORY COPY FLOAT sourceaddress, destinationaddress, numberoffloats [,sourceincrement][,destination increment]



### MEMORY PRINT #]fnbr , nbr, address%/array()

These commands save or read ‘nbr’ of data bytes from or to memory from or to an open disk file. The memory to be saved can be specified as an integer array in which case the

### MEMORY INPUT [#]fnbr , nbr, address%/array()

nbr of bytes to be saved or read is checked against the array size. Alternatively, a memory address can be used in which case no checking can take place and user errors could result in a crash of the firmware..

### MEMORY PACK source%()/sourceaddress%, dest%()/destaddress%, number, size

Memory pack and unpack allow integer values from one array to be compressed into another or uncompressed from one to the other. The two arrays are always normal integer arrays but the packed array can have 2, 4, 8, 16 or 64 values “packed into them. Thus a single integer array element could store 2 off 32-bit words, 4 off 16 bit values, 8 bytes, 16 nibbles, or 64

### MEMORY UNPACK source%()/sourceaddress%, dest%()/destaddress%, number, size

booleans (bits). “number specifies the number of values to be packed or unpacked and “size” specifies the number of bits (1,4,8,16,or 32) Alternatively, memory address(es) can be used in which case no checking can take place and user errors could result in a crash of the firmware.
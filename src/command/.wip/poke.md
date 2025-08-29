

### POKE BYTE addr%, byte or

 POKE BYTE will set the byte (i.e. 8 bits) at the memory location 'addr%' to 'byte'. 'addr%' should be an integer.

### POKE SHORT addr%, short% or

 POKE SHORT will set the short integer (i.e. 16 bits) at the memory location 'addr%' to 'word%'. 'addr%' and short%' should be integers.

### POKE WORD addr%, word% or

 POKE WORD will set the word (i.e. 32 bits) at the memory location 'addr%' to

### POKE INTEGER addr%, int% or

 'word%'. 'addr%' and 'word%' should be integers. POKE INTEGER will set the MMBasic integer (i.e. 64 bits) at the memory

### POKE FLOAT addr%, float! or

 location 'addr%' to int%'. 'addr%' and int%' should be integers. POKE FLOAT will set the word (i.e. 64 bits) at the memory location 'addr%' to

### POKE VAR var, offset, byte or

 'float!'. 'addr%' should be an integer and 'float!' a floating point number. POKE VAR will set a byte in the memory address of 'var'. 'offset' is the

### POKE VARTBL, offset, byte or

 ±offset from the address of the variable. An array is specified as var(). POKE VARTBL will set a byte in MMBasic's variable table. 'offset' is the ±offset from the start of the variable table. Note that a comma is required after the keyword VARTBL.

### POKE DISPLAY command [,data1] [,data2] [,datan]

 This command sends commands and associated data to the display controller for a connected display. This allows the programmer to change parameters of how the display is configured. eg, POKE DISPLAY &H28 will turn off an SSD1963 display and POKE DISPLAY &H29 will turn it back on again. Works for all displays except the ST7790.

### POKE DISPLAY HRES n



### POKE DISPLAY VRES n

 These commands change the stored value of MM.HRES and MM.VRES allowing the programmer to configure non-standard displays.
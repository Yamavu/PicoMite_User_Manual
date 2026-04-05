## PEEK Overview

Returns a value from the processor's virtual memory space. Various subcommands allow access to different data types and memory regions.

### PEEK(BYTE addr%)

Returns the byte (8-bits) located at `addr%`.

### PEEK(SHORT addr%)

Returns the short integer (16-bits) located at `addr%`. Will give an error if not aligned (e.g., PEEK(SP)).

### PEEK(WORD addr%)

Returns the word (32-bits) located at `addr%`.

### PEEK(INTEGER addr%)

Returns the integer (64-bits) located at `addr%`.

### PEEK(FLOAT addr%)

Returns the floating point number (64-bits) located at `addr%`.

### PEEK(VARADDR var)

Returns the address (32-bits) of the variable `var` in memory.

An array is specified as `var()`.

### PEEK(CFUNADDR cfun)

Returns the address (32-bits) of the CFunction `cfun` in memory. This address can be passed to another CFunction which can then call it to perform some common process.

### PEEK(VAR var, ±offset)

Returns a byte in the memory allocated to `var`. An array is specified as `var()`.

### PEEK(VARTBL, ±offset)

Returns a byte in the memory allocated to the variable table maintained by MMBasic. Note that there is a comma after the keyword VARTBL.

### PEEK(PROGMEM, ±offset)

Returns a byte in the memory allocated to the program. Note that there is a comma after the keyword PROGMEM.

**Note:** `addr%` should be an integer.


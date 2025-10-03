.wip


### RAM

RP2350 with PSRAM enabled only The RAM command allows access to up to 5 RAM program slots (similar to flash slots). RAM slots survive a H/W and software reset but not a power cycle.

### RAM LIST

Displays a list of all ram locations including the first line of the program.

### RAM LIST n [,all]

List the program saved to slot n. Use ALL to list without page breaks.

### RAM ERASE n

Erase a ram program location.

### RAM ERASE ALL

Erase all ram program locations.

### RAM SAVE n

Save the current program to the ram location specified.

### RAM LOAD n

Load a program from the specified ram location into program memory.

### RAM RUN n

Runs the program in ram location n, clear all variables. Does not change the program memory.

### RAM CHAIN n

Runs the program in ram location n, leaving all variables intact (allows for a program that is much bigger than the program memory). Does not change the program memory. NB: if the chained program uses the READ command it must call RESTORE before the first read.

### RAM OVERWRITE n

Erase a ram program location and then save the current program to the ram location specified.

### RAM FILE LOAD n, fname$ [,O[VERWRITE]]

Loads the MMBasic file fname$ into the ram slot specified. If the optional parameter OVERWRITE (or O) is specified the content of the flash slot will be overwritten without an error being raised.
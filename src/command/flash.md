.wip


### FLASH

Manages the storage of programs in the flash memory. Up to three programs can be stored in the flash memory and retrieved as required. Note that these saved programs will be erased with a firmware upgrade. One of these flash memory locations can be automatically loaded and run when power is applied using the OPTION AUTORUN n command. In the following ‘n’ is a number 1 to 3.

### FLASH LIST

Displays a list of all flash locations including the first line of the program.

### FLASH LIST n [,all]

List the program saved to slot n. Use ALL to list without page breaks.

### FLASH ERASE n

Erase a flash program location.

### FLASH ERASE ALL

Erase all flash program locations.

### FLASH SAVE n

Save the current program to the flash location specified.

### FLASH LOAD n

Load a program from the specified flash location into program memory.

### FLASH RUN n

Runs the program in flash location n, clear all variables. Does not change the program memory.

### FLASH CHAIN n

Runs the program in flash location n, leaving all variables intact (allows for a program that is much bigger than the program memory). Does not change the program memory. NB: if the chained program uses the READ command it must call RESTORE before the first read.

### FLASH OVERWRITE n

Erase a flash program location and then save the current program to the flash location specified.

### FLASH DISK LOAD n, fname$ [,O[VERWRITE]]

Loads the contents of file fname$ into flash slot n as a binary image. The file can be created using LIBRARY DISK SAVE. Also, any file created externally with data required by a program can be loaded and accessed using commands like PEEK and MEMORY COPY using the address of the flash slot. If the optional parameter OVERWRITE (or O) is specified the content of the flash slot will be overwritten without an error being raised.
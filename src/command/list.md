.wip


### LIST [fname$] or

List a program on the console. LIST on its own will list the program with a pause at every screen full.

### LIST ALL [fname$]

LIST ALL will list the program without pauses. This is useful if you wish to transfer the program to a terminal emulator on a PC that has the ability to capture its input stream to a file. I f the optional ‘fname$’ is specified then that file on the Flash Filesystem or SD Card will be listed.

### LIST PINS

Lists the current status of all pins on the processor

### LIST SYSTEM I2C

Lists a map of all I²C devices connected to the system I²C bus

### LIST COMMANDS or

Lists all valid commands or functions

### LIST FUNCTIONS



### LIST VARIABLES [s%()]

Lists all global variables and contants and, if invoked in a subroutine, the variable used by that subroutine and any subroutines that called it. If the optional parameter s$() is used the variables will be listed to s%() treated as a longstring (see LONGSTRING command).
## OPTION SERIAL CONSOLE uartapin, uartbpin [,B]

Specify that the console be accessed via a hardware serial port (instead
of virtual serial over USB).

`uartapin` and `uartbpin` can be any valid pair of rx and tx pins for either
COM1 or COM2. The order that they are specified is not important.

The speed defaults to 115200 baud but can be changed with OPTION
BAUDRATE. Adding the "B" parameter means output will go to "B"oth
the serial port and the USB.

*This command must be run at the command prompt (not in a program).*


### XMODEM SEND or

 Transfers a BASIC program to or from a remote computer using the XModem protocol. The transfer is done over the USB console connection.

### XMODEM SEND file$ or

 XMODEM SEND will send the current program held in the PicoMite's program memory to the remote device. XMODEM RECEIVE will accept a program sent by the remote device and

### XMODEM RECEIVE or

 save it into the PicoMite's the program memory overwriting the program currently held there.

### XMODEM RECEIVE file$ or

 In both cases you can also specify 'file$' which will transfer the data to/from a file on the Flash Filesystem or SD Card. If the file already exists it will be overwritten when receiving a file.

### XMODEM CRUNCH

 Note that the data is buffered in RAM which limits the maximum transfer size. This command also creates a backup of the program in flash memory which will be automatically retrieved if the CPU is reset of the power is lost. The CRUNCH option works like RECEIVE but will remove all comments, blank lines and unnecessary spaces from the program before saving. This can be used on large programs to allow them to fit into limited memory. SEND, RECEIVE and CRUNCH can be abbreviated to S, R and C. The XModem protocol requires a cooperating software program running on the remote computer and connected to its serial port. It has been tested on Tera Term running on Windows and it is recommended that this be used. After running the XMODEM command in MMBasic select: File -> Transfer -> XMODEM -> Receive/Send from the Tera Term menu to start the transfer. The transfer can take up to 15 seconds to start and if the XMODEM command fails to establish communications it will return to the MMBasic prompt after 60 seconds and leave the program memory untouched. Download Tera Term from http://ttssh2.sourceforge.jp/
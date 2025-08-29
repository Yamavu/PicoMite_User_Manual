

### I2C

 More detail is in Appendix B

### I2C OPEN speed, timeout

 Enables the first I2C module in master mode. ‘speed’ is the clock speed (in KHz) to use and must be one of 100, 400 or 1000. ‘timeout’ is a value in milliseconds after which the master send and receive commands will be interrupted if they have not completed. The minimum value is 100. A value of zero will disable the timeout (though this is not recommended).

### I2C WRITE addr, option, sendlen, senddata [,sendata ..]

 Send data to the I2C slave device. ‘addr’ is the slave’s I2C address. ‘option’ can be 0 for normal operation or 1 to keep control of the bus after the command (a stop condition will not be sent at the completion of the command) ‘sendlen’ is the number of bytes to send. ‘senddata’ is the data to be sent - this can be specified in various ways (all values sent will be between 0 and 255). Notes:  The data can be supplied as individual bytes on the command line. Example: I2C WRITE &H6F, 0, 3, &H23, &H43, &H25  The data can be in a one dimensional array specified with empty brackets (i.e. no dimensions). ‘sendlen’ bytes of the array will be sent starting with the first element. Example: I2C WRITE &H6F, 0, 3, ARRAY() The data can be a string variable (not a constant). Example: I2C WRITE &H6F, 0, 3, STRING$

### I2C READ addr, option, rcvlen, rcvbuf

 Get data from the I2C slave device. ‘addr’ is the slave’s I2C address. ‘option’ can be 0 for normal operation or 1 to keep control of the bus after the command (a stop condition will not be sent at the completion of the command) ‘rcvlen’ is the number of bytes to receive. ‘rcvbuf’ is the variable or array used to save the received data - this can be:  A string variable. Bytes will be stored as sequential characters.  A one dimensional array of numbers specified with empty brackets. Received bytes will be stored in sequential elements of the array starting with the first. Example: I2C READ &H6F, 0, 3, ARRAY() A normal numeric variable (in this case rcvlen must be 1).

### I2C CHECK addr

 Will set the read only variable MM.I2C to 0 if a device responds at the address ‘addr’. MM.I2C will be set to 1 if there is no response.

### I2C CLOSE

 Disables the master I2C module. This command will also send a stop if the bus is still held.

### I2C SLAVE

 See Appendix B
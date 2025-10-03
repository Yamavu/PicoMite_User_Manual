.wip


### ONEWIRE RESET pin or

Commands for communicating with 1-Wire devices. ONEWIRE RESET will reset the 1-Wire bus

### ONEWIRE WRITE pin, flag, length, data [, data…] or

ONEWIRE WRITE will send a number of bytes ONEWIRE READ will read a number of bytes 'pin' is the I/O pin (located in the rear connector) to use. It can be any pin

### ONEWIRE READ pin, flag, length, data [, data…]

capable of digital I/O. 'flag' is a combination of the following options: 1 - Send reset before command 2 - Send reset after command 4 - Only send/recv a bit instead of a byte of data 8 - Invoke a strong pullup after the command (the pin will be set high and open drain disabled) 'length' is the length of data to send or receive 'data' is the data to send or variable to receive. The number of data items must agree with the length parameter. See also Appendix C.
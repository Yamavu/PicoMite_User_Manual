# Appendix A – Serial Communications
Appendix A – Serial Communications
Serial Communications
Two serial interfaces are available for asynchronous serial communications. They are labelled COM1: and
COM2:.

I/O Pins
Before a serial interface can be used the I/O pins must be defined using the following command for the first
channel (referred as COM1):
SETPIN rx, tx, COM1
Valid pins are
RX:
GP1, GP13 or GP17
TX:
GP0, GP12, GP16 or GP28
And the following command for the second channel (referred to as COM2):
SETPIN rx, tx, COM2
Valid pins are
RX:
GP5, GP9 or GP21
TX:
GP4, GP8 or GP20
TX is data from the Raspberry Pi Pico and RX is data to it.
Note that on the WebMite version COM1 and COM2 are not available on GP20 to GP28
The signal polarity is standard for devices running at TTL voltages. Idle is voltage high, the start bit is voltage
low, data uses a high voltage for logic 1 and the stop bit is voltage high. These signal levels allow you to
directly connect to devices like GPS modules (which generally use TTL voltage levels).

Commands
After being opened the serial port will have an associated file number and you can use any commands that operate
with a file number to read and write to/from it. A serial port can be closed using the CLOSE command.
The following is an example:
SETPIN GP13, GP16, COM1
' assign the I/O pins for the first serial port
OPEN "COM1:4800" AS #5
' open the first serial port with a speed of 4800 baud
PRINT #5, "Hello"
' send the string "Hello" out of the serial port
dat$ = INPUT$(20, #5)
' get up to 20 characters from the serial port
CLOSE #5
' close the serial port

The OPEN Command
A serial port is opened using the command:
OPEN comspec$ AS #fnbr
‘fnbr’ is the file number to be used. It must be in the range of 1 to 10. The # is optional.
‘comspec$’ is the communication specification and is a string (it can be a string variable) specifying the serial
port to be opened and optional parameters. The default is 9600 baud, 8 data bits, no parity and one stop bit.
It has the form "COMn: baud, buf, int, int-trigger, EVEN, ODD, S2, 7BIT"
where:





‘n’ is the serial port number for either COM1: or COM2:.
‘baud’ is the baud rate. This can be any number from 1200 to 921600. Default is 9600.
‘buf’ is the receive buffer size in bytes (default size is 256). The transmit buffer is fixed at 256 bytes.
‘int’ is interrupt subroutine to be called when the serial port has received some data.

 ‘int-trigger’ is the number of characters received which will trigger an interrupt.
All parameters except the serial port name (COMn:) are optional. If any one parameter is left out then all the
following parameters must also be left out and the defaults will be used.
Five options can be added to the end of 'comspec$'. These are:
 'S2' specifies that two stop bits will be sent following each character transmitted.
 EVEN specifies that an even parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set.
 ODD specifies that an odd parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set
 7BIT specifies that there a 7bits of data. This is normally used with EVEN or ODD
Page 186

PicoMite User Manual

 INV specifies that the output signals will be inverted and input assumed to be inverted

Examples
Opening a serial port using all the defaults:
OPEN "COM1:" AS #2

Opening a serial port specifying only the baud rate (4800 bits per second):
OPEN "COM1:4800" AS #1

Opening a serial port specifying the baud rate (9600 bits per second) and receive buffer size (1KB):
OPEN "COM2:9600, 1024" AS #8

The same as above but with two stop bits enabled:
OPEN "COM2:9600, 1024, S2" AS #8

An example specifying everything including an interrupt, an interrupt level, and two stop bits:
OPEN "COM2:19200, 1024, ComIntLabel, 256, S2" AS #5

Reading and Writing
Once a serial port has been opened you can use any command or function that uses a file number to read from
and write to the port. Data received by the serial port will be automatically buffered in memory by MMBasic
until it is read by the program and the INPUT$() function is the most convenient way of doing that. When
using the INPUT$() function the number of characters specified will be the maximum number of characters
returned but it could be less if there are less characters in the receive buffer. In fact the INPUT$() function will
immediately return an empty string if there are no characters available in the receive buffer.
The LOC() function is also handy; it will return the number of characters waiting in the receive buffer (i.e. the
maximum number characters that can be retrieved by the INPUT$() function). Note that if the receive buffer
overflows with incoming data the serial port will automatically discard the oldest data to make room for the
new data.
The PRINT command is used for outputting to a serial port and any data to be sent will be held in a memory
buffer while the serial port is sending it. This means that MMBasic will continue with executing the commands
after the PRINT command while the data is being transmitted. The one exception is if the output buffer is full
and in that case MMBasic will pause and wait until there is sufficient space before continuing. The LOF()
function will return the amount of space left in the transmit buffer and you can use this to avoid stalling the
program while waiting for space in the buffer to become available.
If you want to be sure that all the data has been sent (perhaps because you want to read the response from the
remote device) you should wait until the LOF() function returns 256 (the transmit buffer size) indicating that
there is nothing left to be sent.
Serial ports can be closed with the CLOSE command. This will wait for the transmit buffer to be emptied then
free up the memory used by the buffers and cancel the interrupt (if set). A serial port is also automatically
closed when commands such as RUN and NEW are issued.

Interrupts
The interrupt subroutine (if specified) will operate the same as a general interrupt on an external I/O pin (see
the chapter Using the I/O pins for a description).
When using interrupts you need to be aware that it will take some time for MMBasic to respond to the interrupt
and more characters could have arrived in the meantime, especially at high baud rates. For example, if you
have specified the interrupt level as 200 characters and a buffer of 256 characters then quite easily the buffer
will have overflowed by the time the interrupt subroutine can read the data. In this case the buffer should be
increased to 512 characters or more.

PicoMite User Manual


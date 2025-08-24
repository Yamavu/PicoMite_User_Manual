# Appendix D – SPI Communications

SPI Communications
The Serial Peripheral Interface (SPI) communications protocol is used to send and receive data between
integrated circuits. The Raspberry Pi Pico acts as the master (i.e. it generates the clock).

I/O Pins
Before an SPI interface can be used the I/O pins for the channel must be allocated using the following
commands. For the first channel (referred as SPI) it is:
SETPIN rx, tx, clk, SPI
Valid pins are
RX:
GP0, GP4, GP16 or GP20
TX:
GP3, GP7 or GP19
CLK: GP2, GP6 or GP18
And the following command for the second channel (referred to as SPI2) is:
SETPIN rx, tx, clk, SPI2
Valid pins are
RX:
GP8, GP12 or GP28
TX:
GP11, GP15 or GP27
CLK: GP10, GP14 or GP26
TX is data from the Raspberry Pi Pico and RX is data to it.
Note that on the WebMite version SPI1 and SPI2 are not available on GP20 to GP28

SPI Open
To use the SPI function the SPI channel must be first opened.
The syntax for opening the first SPI channel is (use SPI2 for the second channel):
SPI OPEN speed, mode, bits
Where:
 ‘speed’ is the speed of the clock. It is a number representing the clock speed in Hz.
 'mode' is a single numeric digit representing the transmission mode – see Transmission Format below.
 'bits' is the number of bits to send/receive. This can be any number in the range of 4 to 16 bits.
 It is the responsibility of the program to separately manipulate the CS (chip select) pin if required.

Transmission Format
The most significant bit is sent and received first. The format of the transmission can be specified by the 'mode'
as shown below. Mode 0 is the most common format.
Mode

Description

CPOL

CPHA

0

Clock is active high, data is captured on the rising edge and output on the falling edge

0

0

1

Clock is active high, data is captured on the falling edge and output on the rising edge

0

1

2

Clock is active low, data is captured on the falling edge and output on the rising edge

1

0

3

Clock is active low, data is captured on the rising edge and output on the falling edge

1

1

For a more complete explanation see: http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus

Standard Send/Receive
When the first SPI channel is open data can be sent and received using the SPI function (use SPI2 for the
second channel). The syntax is:
received_data = SPI(data_to_send)
Note that a single SPI transaction will send data while simultaneously receiving data from the slave.
‘data_to_send’ is the data to send and the function will return the data received during the transaction.
‘data_to_send’ can be an integer or a floating point variable or a constant.

Page 192

PicoMite User Manual

If you do not want to send any data (i.e. you wish to receive only) any number (eg, zero) can be used for the
data to send. Similarly if you do not want to use the data received it can be assigned to a variable and ignored.

Bulk Send/Receive
Data can also be sent in bulk (use SPI2 for the second channel):
SPI WRITE nbr, data1, data2, data3, … etc
or
SPI WRITE nbr, string$
or
SPI WRITE nbr, array()
In the first method 'nbr' is the number of data items to send and the data is the expressions in the argument list
(i.e. 'data1', data2' etc). The data can be an integer or a floating point variable or a constant.
In the second or third method listed above the data to be sent is contained in the 'string$' or the contents of
'array()' (which must be a single dimension array of integer or floating point numbers). The string length, or the
size of the array must be the same or greater than nbr. Any data returned from the slave is discarded.
Data can also be received in bulk (use SPI2 for the second channel):
SPI READ nbr, array()
Where 'nbr' is the number of data items to be received and array() is a single dimension integer array where the
received data items will be saved. This command sends zeros while reading the data from the slave.

SPI Close
If required the first SPI channel can be closed as follows (the I/O pins will be set to inactive):
SPI CLOSE
Use SPI2 for the second channel.

Examples
The following example shows how to use the SPI port for general I/O. It will send a command 80 (hex) and
receive two bytes from the slave SPI device using the standard send/receive function:
PIN(10) = 1 : SETPIN 10, DOUT
SETPIN GP20, GP3, GP2, SPI
SPI OPEN 5000000, 3, 8
PIN(10) = 0
junk = SPI(&H80)
byte1 = SPI(0)
byte2 = SPI(0)
PIN(10) = 1
SPI CLOSE

' pin 10 will be used as the enable signal

' assign the I/O pins
' speed is 5 MHz and the data size is 8 bits
' assert the enable line (active low)
' send the command and ignore the return
' get the first byte from the slave
' get the second byte from the slave
' deselect the slave
' and close the channel

The following is similar to the example given above but this time the transfer is made using the bulk
send/receive commands:
OPTION BASE 1
DIM data%(2)
SETPIN GP20, GP3, GP2, SPI
PIN(10) = 1 : SETPIN 10, DOUT
SPI OPEN 5000000, 3, 8
PIN(10) = 0
SPI WRITE 1, &H80
SPI READ 2, data%()
PIN(10) = 1
SPI CLOSE

PicoMite User Manual

' our array will start with the index 1
' define the array for receiving the data

' assign the I/O pins
' pin 10 will be used as the enable signal
' speed is 5 MHz, 8 bits data
' assert the enable line (active low)
' send the command
' get two bytes from the slave
' deselect the slave
' and close the channel

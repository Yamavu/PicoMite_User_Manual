# Appendix D – SPI Communications

The Serial Peripheral Interface (SPI) communications protocol is used to send and receive data between integrated circuits.

The Raspberry Pi Pico acts as the master (i.e. it generates the clock).


## I/O Pins

*Note that on the WebMite version SPI and SPI2 are not available on GP20 to GP28*

Before an SPI interface can be used the I/O pins for the channel must be allocated using `SETPIN`.

`TX` is data from the Raspberry Pi Pico and `RX` is data to it. `CLK` is the clock signal.


### first channel (referred as SPI)

```basic
SETPIN rx, tx, clk, SPI
```

| | Valid pins |
| :-: | :- |
| `RX` | GP0, GP4, GP16 or GP20 |
| `TX` | GP3, GP7 or GP19 |
| `CLK` | GP2, GP6 or GP18 |


### second channel (referred to as SPI2)

```basic
SETPIN rx, tx, clk, SPI2
```

| |Valid pins are |
| :-: | :- |
| `RX` | GP8, GP12 or GP28 |
| `TX` | GP11, GP15 or GP27 |
| `CLK` | GP10, GP14 or GP26 |


## Open SPI Connection

To use the SPI function the SPI channel must be first opened.

The syntax for opening the first SPI channel is (use SPI2 for the second channel):

```basic
SPI OPEN speed, mode, bits
```

`speed` is the speed of the clock. It is a number representing the clock speed in Hz. 

`mode` is a single numeric digit representing the transmission mode – see Transmission Format below.

`bits` is the number of bits to send/receive. This can be any number in the range of 4 to 16 bits.

It is the responsibility of the program to separately manipulate the CS (chip select) pin if required.


## Transmission Format

The most significant bit is sent and received first. The format of the transmission can be specified by the `mode` as shown below. Mode 0 is the most common format.

Mode | Description | CPOL | CPHA
 :-: | :- | :-: | :-: 
0 | Clock is active high, data is captured on the rising edge and output on the falling edge | 0 | 0
1 | Clock is active high, data is captured on the falling edge and output on the rising edge | 0 | 1 
2 | Clock is active low, data is captured on the falling edge and output on the rising edge | 1 | 0
3 | Clock is active low, data is captured on the rising edge and output on the falling edge | 1 | 1

For a more complete explanation see the [SPI article on Wikipedia](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus)

## Standard Send/Receive

When the first SPI channel is open data can be sent and received using the `SPI`/`SPI2` function.

The syntax is:

```basic
received_data = SPI(data_to_send)
```

Note that a single SPI transaction will send data while simultaneously receiving data from the slave.

- `data_to_send` is the data to send and the function will return the data received during the transaction.
- `data_to_send` can be an integer or a floating point variable or a constant.

If you do not want to send any data (i.e. you wish to receive only) any number (eg, zero) can be used for the data to send. Similarly if you do not want to use the data received it can be assigned to a variable and ignored.


## Bulk Send

Data can also be sent in bulk (use SPI2 for the second channel):

```basic
SPI WRITE nbr, data1, data2, data3, … etc
```

`nbr` is the number of data items to send . 

The data is the expressions in the argument list (i.e. `data1`, `data2` etc). The data can be an integer or a floating point variable or a constant.

```basic
SPI WRITE nbr, string$
```

The data to be sent is contained in the `string$`. 

The string length, must be the same or greater than `nbr`. Any data returned from the slave is discarded.

```basic
SPI WRITE nbr, array()
```

The data to be sent is contained in the contents of `array()` (which must be a single dimension array of integer or floating point numbers). 

The size of the array must be the same or greater than `nbr`. Any data returned from the slave is discarded.


## Bulk Recieve

Data can also be received in bulk (use SPI2 for the second channel):

```basic
SPI READ nbr, array()
```

Where `nbr` is the number of data items to be received and `array()` is a single dimension integer array where the received data items will be saved.

This command sends zeros while reading the data from the slave.

## Close SPI Connection

If required the first SPI channel can be closed as follows (the I/O pins will be set to inactive):

```basic
SPI CLOSE
```

*Use SPI2 for the second channel.*

## Examples

The following example shows how to use the SPI port for general I/O. It will send a command 80 (hex) and
receive two bytes from the slave SPI device using the standard send/receive function:

```basic
PIN(10) = 1 : SETPIN 10, DOUT  ' pin 10 will be used as the enable signal
SETPIN GP20, GP3, GP2, SPI     ' assign the I/O pins
SPI OPEN 5000000, 3, 8         ' speed is 5 MHz and the data size is 8 bits
PIN(10) = 0                    ' assert the enable line (active low)
junk = SPI(&H80)               ' send the command and ignore the return
byte1 = SPI(0)                 ' get the first byte from the slave
byte2 = SPI(0)                 ' get the second byte from the slave
PIN(10) = 1                    ' deselect the slave
SPI CLOSE                      ' and close the channel
```

The following is similar to the example given above but this time the transfer is made using the bulk send/receive commands:

```basic
OPTION BASE 1                    ' our array will start with the index 1
DIM data%(2)                     ' define the array for receiving the data
SETPIN GP20, GP3, GP2, SPI       ' assign the I/O pins
PIN(10) = 1 : SETPIN 10, DOUT    ' pin 10 will be used as the enable signal
SPI OPEN 5000000, 3, 8           ' speed is 5 MHz, 8 bits data
PIN(10) = 0                      ' assert the enable line (active low)
SPI WRITE 1, &H80                ' send the command
SPI READ 2, data%()              ' get two bytes from the slave
PIN(10) = 1                      ' deselect the slave
SPI CLOSE                        ' and close the channel
```
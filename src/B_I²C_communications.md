# Appendix B – I²C Communications

I²C (Inter-Integrated Circuit, also known as I2C and IIC) is a synchronous, multi-master/multi-slave, single-ended, serial communication bus invented in 1980 by Philips Semiconductors (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral integrated circuits (ICs) to processors and microcontrollers in short-distance, intra-board communication. 

When running the I²C bus at above 100 kHz the cabling between the devices becomes important. Ideally the cables should be as short as possible (to reduce capacitance) and the data and clock lines should not run next to each other but have a ground wire between them (to reduce crosstalk).

If the data line is not stable when the clock is high, or the clock line is jittery, the I²C peripherals can get "confused" and end up locking the bus (normally by holding the clock line low). If you do not need the higher speeds then operating at 100 kHz is the safest choice.

The command `I2C CHECK addr` can be used to check if a device is present at the address `addr`. This will set the read only variable MM.I2C to 0 if a device responds or 1 if there is no response.

## I/O Pins

Before the I²C interface can be used the I/O pins must be configured using `SETPIN`:

There are two I²C channels. They can operate in master or slave mode.

### first channel (I2C)

```basic
SETPIN sda, scl, I2C
```

*Note that on the WebMite version I2C SDA is not available on GP28*

| | Valid pins |
| :-: | :- |
| `SDA` | GP0, GP4, GP8, GP12, GP16, GP20 or GP28 |
| `SCL` | GP1, GP5, GP9, GP13, GP17 or GP21 |


### second channel (I2C2)

```basic
SETPIN sda, scl, I2C2
```

| | Valid pins |
| :-: | :- |
| `SDA` | GP2, GP6, GP10, GP14, GP18, GP22 or GP26 |
| `SCL` | GP3, GP7, GP11, GP15, GP19 or GP27 |


## I²C Master Commands

There are four commands that can be used for the first channel `I2C` in master mode as follows.

The commands for the second channel `I2C2` are identical except that the command is I2C2


### I2C OPEN speed, timeout

Enables the I2C module in master mode.

`speed` is the clock speed (in KHz) to use and must be either 100, 400 or 1000.

`timeout` is a value in milliseconds after which the master send and receive commands will be interrupted if they have not completed. The minimum value is 100. A value of zero will disable the timeout (though this is not recommended).


### I2C WRITE addr, option, sendlen, senddata [,sendata ..]

Send data to the I2C slave device. 

`addr` is the slave’s I2C address.

`option` can be 0 for normal operation or 1 to keep control of the bus after the command (a stop condition will not be sent at the completion of the command)

`sendlen` is the number of bytes to send.

`senddata` is the data to be sent - this can be specified in various ways (all data sent will be sent as bytes with a value between 0 and 255):

* The data can be supplied as individual bytes on the command line.<br>
  Example: `I2C WRITE &H6F, 0, 3, &H23, &H43, &H25`

* The data can be in a one dimensional array specified with empty brackets (i.e. no dimensions). <br>
  `sendlen` bytes of the array will be sent starting with the first element. <br>
  Example: `I2C WRITE &H6F, 0, 3, ARRAY()`

* The data can be a string variable (not a constant).<br>
  Example: `I2C WRITE &H6F, 0, 3, STRING$`


### I2C READ addr, option, rcvlen, rcvbuf

Get data from the I2C slave device. 

`addr` is the slave’s I2C address.

`option` can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)

`rcvlen` is the number of bytes to receive.

`rcvbuf` is the variable or array used to save the received data - this can be:

* A string variable. Bytes will be stored as sequential characters in the string.
* A one dimensional array of numbers specified with empty brackets. Received bytes will be stored in sequential elements of the array starting with the first.<br>
  Example: `I2C READ &H6F, 0, 3, ARRAY()`
* A normal numeric variable (in this case `rcvlen` must be 1).


### I2C CLOSE

Disables the master I²C module and returns the I/O pins to a "not configured" state.

This command will also send a stop if the bus is still held.


## I2C Slave Commands


### I2C SLAVE OPEN addr, send_int, rcv_int

Enables the I2C module in slave mode.

`addr` is the slave I2C address.

`send_int` is the subroutine to be invoked when the module has detected that the master is expecting data.

`rcv_int` is the subroutine to be called when the module has received data from the master. Note that this is triggered on the first byte received so your program might need to wait until all the data is received.


### I2C SLAVE WRITE sendlen, senddata [,sendata ..]

Send the data to the I2C master.

This command should be used in the send interrupt (ie in the `send_int` subroutine when the master has requested data). Alternatively, a flag can be set in the interrupt subroutine and the command invoked from the main program loop when
the flag is set.

`sendlen` is the number of bytes to send.

`senddata` is the data to be sent. This can be specified in various ways, see the `I2C WRITE` commands for details.


### I2C SLAVE READ rcvlen, rcvbuf, rcvd

Receive data from the I2C master device.

This command should be used in the receive interrupt (ie in the `rcv_int` subroutine when the master has sent some data). Alternatively a flag can be set in the receive interrupt subroutine and the command invoked from the main program loop when
the flag is set.

`rcvlen` is the maximum number of bytes to receive.

`rcvbuf` is the variable to receive the data. This can be specified in various ways, see the `I2C READ` commands for details.

`rcvd` is a variable that, at the completion of the command, will contain the actual number of bytes received (which might differ from `rcvlen`).


### I2C SLAVE CLOSE

Disables the slave I2C module and returns the external I/O pins to a "not configured" state. They can then be configured using [SETPIN](./command/setpin.md).


## Errors

Following an I²C write or read the automatic variable `MM.I2C` will be set to indicate the result as follows:

MM.I2C | Description
:-: | :-
0 | The command completed without error.
1 | Received a NACK response (NACK = not acknowledged/error)
2 | Command timed out


## 7-Bit Addressing

The standard addresses used in these commands are 7-bit addresses (without the read/write bit). MMBasic will
add the read/write bit and manipulate it accordingly during transfers.

Some vendors provide 8-bit addresses which include the read/write bit. You can determine if this is the case
because they will provide one address for writing to the slave device and another for reading from the slave. In
these situations you should only use the top seven bits of the address. 

For example: If the read address is `9B` (hex) and the write address is `9A` (hex) then using only the top seven bits will give you an address of `4D` (hex).

Hex | Binary
:-:| :-
9B | `10011011`
9A | `10011010`
4D | `1001101`

Another indicator that a vendor is using 8-bit addresses instead of 7-bit addresses is to check the address range.
All 7-bit addresses should be in the range of `08` to `77` (hex). If your slave address is greater than this range then
probably your vendor has provided an 8-bit address.


## Examples

As an example of a simple communications where the Raspberry Pi Pico is the master, the following program will read and display the current time (hours and minutes) maintained by a PCF8563 real time clock chip connected to the second I²C channel:

```basic
DIM AS INTEGER RData(2)             ' this will hold received data
SETPIN GP6, GP7, I2C2               ' assign the I/O pins for I2C2
I2C2 OPEN 100, 1000                 ' open the I2C channel
I2C2 WRITE &H51, 0, 1, 3            ' set the first register to 3
I2C2 READ &H51, 0, 2, RData()       ' read two registers
I2C2 CLOSE                          ' close the I2C channel
PRINT "Time is " RData(1) ":" RData(0)
```

This is an example of communications between two Raspberry Pi Picos. The master will send the characters
`A` to `Z` and after each transmission issue a query to the slave and print the response. The slave will read the
byte sent by the master and print it. In response to the query from the master it will send the current time.

First the master:

```basic
SETPIN GP2, GP3, I2C2
I2C2 OPEN 100, 1000
FOR i = 65 to 90
  a$ = CHR$(i)
  I2C2 WRITE &H50, 0, 1, a$
  PAUSE 500
  I2C2 READ &H50, 0, 8, a$
  PRINT a$
  PAUSE 500
NEXT i
```

Then the slave:

```basic
SETPIN GP2, GP3, I2C2
I2C2 SLAVE OPEN &H50, tint, rint
DO : LOOP

SUB rint
  LOCAL count, a$
  I2C2 SLAVE READ 10, a$, count
  PRINT LEFT$(a$, count)
END SUB

SUB tint
  LOCAL a$ = Time$
  I2C2 SLAVE WRITE LEN(a$), a$
END SUB
```

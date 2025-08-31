# Predefined Read Only Variables

These variables are set by MMBasic and cannot be changed by the running program. Note that they do not do
anything on their own, they must be printed or assigned to a variable.
For example:
```basic
> PRINT MM.VER
6.0002
>
```

or, in a program:

```basic
If MM.VER < 6.0002 Then Error "Needs version 6.00.02 or greater"
```

### MM.VER

Returns the version number of the firmware as a floating point number in the
form aa.bbcc where aa is the major version number, bb is the minor version
number and cc is the revision number. For example version 6.03.00 would
return `6.03` and version 6.03.01 will return `6.0301`.


### MM.ADDRESS$

*WEBMITE VERSION ONLY*

This variable returns the IP address of the sender of the last UDP datagram received


### MM.CMDLINE$

This constant variable containing any command line arguments passed to the
current program is automatically created when an MMBasic program runs.

see [RUN](command/run.md) and [*](commands_single_character.md) commands for details.

* Programs run from the Editor or using `OPTION AUTORUN` will set MM.CMDLINE$ to the empty string.
* If not required this constant variable may be removed from memory using `ERASE MM.CMDLINE$`


### MM.DEVICE$

A string representing the device or platform that MMBasic is running on.



### MM.DISPLAY

Returns `1` if a physical display is configured, otherwise `0`



### MM.ERRNO

If a statement caused an error which was ignored these variables will be set
accordingly.

MM.ERRNO is a number where non zero means that there was an error and

They are reset to zero and an empty string by `RUN`, `ON ERROR IGNORE` or `ON ERROR SKIP`.


### MM.ERRMSG$

If a statement caused an error which was ignored these variables will be set
accordingly.

MM.ERRNO is a number where non zero means that there was an error and

MM.ERRMSG$ is a string representing the error message that would have normally been displayed on the console. 

They are reset to zero and an empty string by `RUN`, `ON ERROR IGNORE` or `ON ERROR SKIP`.



### MM.FLAGS

Returns the value of the system flags register


### MM.FONTHEIGHT

Returns the height of the current font in pixels


### MM.FONTWIDTH

Returns the width of the current font in pixels


### MM.HRES

Integers representing the current horizontal of the VGA/HDMI video output or the LCD display panel (if configured) in pixels.


### MM.VRES

Integers representing the current vertical resolution of the VGA/HDMI video output or the LCD display panel (if configured) in pixels.



### MM.HEIGHT


### MM.WIDTH

Returns the number of characters across the physical display with the current
font or the number of characters down the display with the current font



### MM.HPOS


### MM.VPOS

Returns the current horizontal and vertical position (in pixels) following the
last graphics or print command.


### MM.INFO() MM.INFO$()

These two versions can be used interchangeably but good programming
practice would require that you use the one corresponding to the returned
datatype.



### MM.INFO$(AUTORUN)

Returns the setting of the OPTION AUTORUN command



### MM.INFO(ADC)

Returns the number of the buffer currently ready to read when using ADC
RUN (1 or 2). Returns 0 if nothing ready.



### MM.INFO(ADC DMA)

Returns true (1) if the ADC DMA is active.



### MM.INFO(BOOT)

Tells you the reason for the last restart of the Pico 

Returns:
* Restart - the device has been restarted with `CPU RESTART` or an `OPTION` command
* S/W Watchdog - the device has been restarted by a software watchdog timeout
* H/W Watchdog - the device has been restarted by a hardware watchdog timeout
* Firmware update - the device has been restarted following a firmware update
* Power On - the device has been powered up
* Reset Switch - the device has been restarted using the reset switch
* Unknown code &Hn - unknown reason - please report the code and version RP2040/2350


### MM.INFO(BOOT COUNT)

Returns the number of times the Pico has been restarted since the flash drive
was last formatted.


### MM.INFO$(CPUSPEED)

Returns the CPU speed as a string.


### MM.INFO$(LCDPANEL)

Returns the name of the configured LCD panel or a blank string.


### MM.INFO(LCD320)

Returns true if the display is capable of 320x240 operation using the
OPTION LCD320 command


### MM.INFO$(SDCARD)

Returns the status of the SD Card. Valid returns are:
DISABLED, NOT PRESENT, READY, and UNUSED


### MM.INFO$(CURRENT)

Returns the name of the current program when loaded from a file or NONE
if called after a NEW, AUTOSAVE, XMODEM or EDIT Command.



### MM.INFO$(PATH)

Returns the path of the current program or NONE if called after a NEW or
EDIT Command.



### MM.INFO(DISK SIZE)

Returns the capacity of the Flash Filesystem or SD Card, whichever is the
active drive, in bytes



### MM.INFO$(DRIVE)

Returns the active drive “A:” or “B:”



### MM.INFO(EXISTS FILE
fname$)

Returns 1 if the file specified exists, returns -1 if fname$ is a directory,
otherwise returns 0.



### MM.INFO(EXISTS DIR
dirname$)

Returns a Boolean indicating whether the directory specified exits.



### MM.INFO(FREE SPACE)

Returns the free space on the Flash Filesystem or SD Card whichever is the
active drive.



### MM.INFO(FILESIZE file$)

Returns the size of file$ in bytes or 0 if not found.

PicoMite User Manual

Page 85

MM.INFO$(MODIFIED file$)

Returns the date/time that file$ was modified, Empty string if not found.



### MM.INFO$(SYSTEM I2C)


### MM.INFO(FCOLOUR)

Returns “I2C”, “I2C2”, or “Not set” depending on the status of OPTION
SYSTEM I2C
Returns the current foreground colour.



### MM.INFO(BCOLOUR)

Returns the current background colour.



### MM.INFO(FONT)

Returns the number of the currently active font.



### MM.INFO(FONT ADDRESS
n)

Returns the address of the memory location with the address of FONT n .



### MM.INFO(FONT POINTER n)

Returns a POINTER to the start of FONT n in memory.



### MM.INFO(FONTHEIGHT)


### MM.INFO(FONTWIDTH)

Integers representing the height and width of the current font (in pixels).



### MM.INFO(FLASH)

Reports which flash slot the program was loaded from if applicable.



### MM.INFO(FLASH ADDRESS
n)

Returns the address of the flash slot n.



### MM.INFO(HEAP)

Returns the amount of MMbasic Heap memory free. MMBasic heap is used
for strings, arrays and various other temporary and permanent buffers (eg,
audio)



### MM.INFO(HPOS)


### MM.INFO(VPOS)

The current horizontal and vertical position (in pixels) following the last
graphics or print command.



### MM.INFO(ID)

Returns the unique ID of the Pico.



### MM.INFO$(IP ADDRESS)

Returns the IP address of the WebMite



### MM.INFO(MAX GP)

Returns the highest valid GPno on the chip



### MM.INFO$(MODBUFF
ADDRESS)

Returns the address in memory of the buffer used for storing MOD files



### MM.INFO$(OPTION option)

Returns the current value of a range of options that affect how a program
will run. “option” can be one of AUTORUN, AUDIO, BASE, BREAK,
CONSOLE, DEFAULT, EXPLICIT, KEYBOARD, ANGLE, HEIGHT,
WIDTH, FLASH SIZE



### MM.INFO$(PIN pinno)

Returns the status of I/O pin 'pinno'. Valid returns are:
OFF, DIN, DOUT, AIN, etc



### MM.INFO(PINNO GPnn)

Returns the physical pin number for a given GP number. GPnn can be an
unquoted string (GP01), a string literal(“GP01”) or a string variable. Ie,
A$=”GP01”: MM.INFO(PINNO A$) .



### MM.INFO(PIO RX DMA)

Indicates whether the PIO RX DMA channel is busy



### MM.INFO(PIO TX DMA)

Indicates whether the PIO TX DMA channel is busy



### MM.INFO$(PLATFORM)

Returns the string previously set with OPTION PLATFORM.



### MM.INFO(PROGRAM)

Returns the address in memory of the currently running program



### MM.INFO(PS2)

Reports the last raw message received on the PS2 interface if enabled.

Page 86

PicoMite User Manual

MM.INFO(PWM COUNT)

Returns the number of PWM channels supported by the chip



### MM.INFO(PWM DUTY C%,
n%)

Returns the current duty cycle in clock counts of PWM channel C%,N%
Where N%=0 for A and 1 for B



### MM.INFO$(SOUND)

Returns the current activity on the audio output (OFF, PAUSED, TONE,
WAV, FLAC, SOUND)



### MM.INFO(SPI SPEED

Returns the actual speed of the SYSTEM SPI or an error if not set



### MM.INFO(STACK)

Returns the C stack pointer. Complex or recursive Basic code may result in
the error "Stack overflow, expression too complex at depth %" This will
occur when the stack is below &H 2003f800. Monitoring the stack will
allow the programmer to identify simplifications to the Basic code to avoid
the error.



### MM.INFO$(SYSTEM I2C)

Returns I2C, I2C2, or NOT SET as applicable.



### MM.INFO(SYSTEM HEAP)

Returns the free space on the System Heap.



### MM.INFO(SYSTICK)

Returns the current value of the system 24-bit systick timer which runs at the
CPU clock speed



### MM.INFO(TILE HEIGHT)

VGA AND HDMI VERSIONS ONLY
Returns the current setting of the tile height.



### MM.INFO(TRACK)

Returns the name of the FLAC, MP3, WAV or MIDI file currently playing
on the audio output.



### MM.INFO$(TOUCH)

Returns the status of the Touch controller. Valid returns are:
“Disabled”, “Not calibrated”, and “Ready”.



### MM.INFO(USB n)

Return the device code for any device connected to channel ‘n’ which is a
number from 1 to 4. The returned device code can be:
0=not in use, 1=keyboard, 2=mouse, 128=ps4, 129=ps3, 130=SNES/Generic
By default a connected keyboard will be allocated to channel 1, a mouse the
channel 2, and gamepads to channel 3 and then channel 4. If 2 or more
keyboards or mice are connected or 3 or more gamepads then the additional
devices will be allocated to the highest available channel.



### MM.INFO(USB VID n)

Returns the VID of the USB device on channel n



### MM.INFO(USB PID n)

Returns the PID of the USB device on channel n



### MM.INFO(VARCNT)

Returns the number of variables in use in the MMBasic program.



### MM.INFO$(LINE)

Returns the current line number as a string. LIBRARY returned if in the
Library and UNKNOWN if not in a program. Assists in diagnostics while
unit testing.



### MM.INFO(UPTIME)

Returns the time in seconds since booted as a floating point number.



### MM.INFO(VALID
CPUSPEED speed%)

Returns 1 if ‘speed%’ is valid for OPTION CPUSPEED ‘speed%’



### MM.INFO(VERSION)

The version number of the firmware (MM.VER converts to this)

PicoMite User Manual

Page 87

MM.INFO(WRITEBUFF)



### MM.INFO(TCP PORT)


### MM.INFO(UDP PORT)



### MM.INFO(TCPIP STATUS)


### MM.INFO(WIFI STATUS)

Returns the address in memory of the current buffer used for drawing
commands.
WEBMITE ONLY
Returns the TCP port set as a server or 0 if not set
Returns the UDP port set as a server or 0 if not set
WEBMITE ONLY
Returns the TCPIP status of the connection
Returns the WIFI status of the connection.
Valid returns are:
0 WiFi is down
1 Connected to WiFi
2 Connected to WiFi, but no IP address (TCPIP STATUS only)
3 Connected to WiFi with an IP address (TCPIP STATUS only)
-1 Connection failed
-2 No matching SSID found (could be out of range, or down)
-3 Authentication failure



### MM.MESSAGE$

WEBMITE ONLY
Returns the contents of the last UDP datagram received or last MQTT packet
received



### MM.TOPIC$

WEBMITE ONLY
Returns the topic of the last MQTT packet received



### MM.ADDRESS$

WEBMITE ONLY
Returns the address of the sender of the last UDP datagram received or last
MQTT packet received



### MM.ONEWIRE

Following a 1-Wire reset function this integer variable will be set to indicate
the result of the operation: 0 = Device not found, 1 = Device found,
2=Device timeout.



### MM.I2C

Following an I2C write or read command this integer variable will be set to
indicate the result of the operation as follows:
0 = The command completed without error.
1 = Received a NACK response
2 = Command timed out



### MM.PERSISTENT

Returns a value saved with the command SAVE PERSISTENT



### MM.PS2

Returns the last code received on the PS2 interface if enabled.



### MM.WATCHDOG

An integer which is true if MMBasic was restarted as the result of a
Watchdog timeout (see the WATCHDOG command) otherwise false.


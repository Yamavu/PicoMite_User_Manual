# Options

Detailed Listing
This table lists the various option commands which can be used to configure MMBasic and change the way it
operates. Options that are marked as permanent will be saved in non-volatile memory and automatically
restored when the PicoMite firmware is restarted. Options that are not permanent will be reset on start-up, reset
and in many cases when a program is run and/or exited.
Many OPTION commands will force a restart of the PicoMite firmware and that will cause the USB console
interface to be reset. The program in memory will not be lost as it is held in non-volatile flash memory.
Permanent?
OPTION ANGLE RADIANS |
DEGREES

This command switches trig functions between degrees and radians.
Acts on SIN, COS, TAN, ATN, ATAN2, MATH ATAN3, ACOS, ASIN

OPTION AUDIO PWMnApin,
PWMnBpin
or
OPTION AUDIO DISABLE

 Configures one of the PWM channels as an audio output.

OPTION AUDIO SPI CSpin,
CLKpin, MOSIpin
or
OPTION AUDIO DISABLE

the audio output to be directed to a MCP48n2 DAC
 Configures
connected to the specified pins. The LDAC pin on the DAC should be

OPTION AUDIO VS1053
CLKpin, MOSIpin, MISOpin,
XCSpin, XDCSpin, DREQpin,
XRSTpin
or
OPTION AUDIO DISABLE

the audio output to be directed to a VS1053 CODEC. This
 Configures
allows MP3 and MIDI playback in addition to the other formats

OPTION AUDIO I2S
BCLKpin, DINpin
or
OPTION AUDIO DISABLE

the audio output to be directed to an I2S DAC connected to
 Configures
the specified pins. The LRCK pin on the DAC should be connected to

OPTION AUTOREFRESH
OFF | ON

Black and white displays can only be updated a full screen at a time. By
using OPTION AUTOREFRESH OFF/ON you can control whether a
write command immediately updates the display or not. If
AUTOREFRESH is OFF the REFRESH command can be used to
trigger the write. This applies to the following displays: N5110,
SSD1306I2C, SSD1306I2C32, SSD1306SPI and ST7920

OPTION AUTORUN ON
[,NORESET]

PicoMite User Manual

‘PWMnApin’ is the left audio channel, ‘PWMnBpin’ is the right. Both
pins must belong to the same audio channel.
Example, OPTION AUDIO GP18, GP19 would use PWM1A and
PWM1B on pins 24 and 25 respectively.
This option prevents use of these pins in the BASIC program.
The audio output is generated using PWM so a low pass filter is
necessary on the output. The audio output from the Raspberry Pi Pico is
very noisy. Using OPTION POWER and/or supplying power via a
separate 3.3V linear regulator can reduce this.
This command must be run at the command prompt (not in a program).

connected to GND.

supported and also supports real-time MIDI output. See the PLAY
command for more details

the next consecutive GPIO pin to BCLKpin.

MMBasic to automatically run a program on power up or
 Instructs
restart.

Page 89

or
OPTION AUTORUN n
[,NORESET]
or
OPTION AUTORUN OFF

ON will cause the current program in program memory to be run.
Specifying ‘n’ will cause that location in flash memory to be run. ‘n’
must be in the range 1 to 3.
Specifying the optional parameter “NORESET” will maintain
AUTORUN even if the program causes a system error (by default this
will cause the firmware to cancel any OPTION AUTORUN setting).
OFF will disable the autorun option and is the default for a new
program.
Entering the break key (default CTRL-C) at the console will interrupt the
running program and return to the command prompt.

OPTION BASE 0 | 1

Set the lowest value for array subscripts to either 0 or 1.
This must be used before any arrays are declared and is reset to the
default of 0 on power up.

OPTION BAUDRATE nn

Set the baudrate of the serial console (if it is configured).

OPTION BREAK nn

Set the value of the break key to the ASCII value 'nn'. This key is used to
interrupt a running program.
The value of the break key is set to CTRL-C key at power upand when a
program is run but it can be changed to any keyboard key using this
command in a program (for example, OPTION BREAK 4 will set the break
key to the CTRL-D key). Setting this option to zero will disable the break
function entirely.

OPTION CASE LOWER |
UPPER | TITLE

the case used for listing command and function names when
 Change
using the LIST command. The default is TITLE but the old standard of
MMBasic can be restored using OPTION CASE UPPER.

OPTION COLOURCODE ON
or
OPTION COLOURCODE
OFF

on or off colour coding for the editor's output. Keywords will be in
 Turn
cyan, comments in yellow, etc. The default is OFF.
The keyword COLORCODE (USA spelling) can also be used.
This will work on VGA/HDMI video and the serial console using a
terminal emulator with VT100 emulation (eg, Tera Term). This
command must be run at the command prompt (not in a program).

OPTION CONSOLE output

Specifies where print statements will output. Valid settings are BOTH (i.e.
SCREEN and SERIAL), SERIAL, SCREEN, NONE. This is a temporary
option that is reset when a program exits.

OPTION CONTINUATION
LINES ON/OFF

or disables the use of continuation lines in the editor and with the
 Enables
LIST command. Line continuation is indicated by a space followed by an
underscore character at the end of a line. When enabled the editor will
automatically split lines as it reads them from file and add the continuation
characters required. When exiting the editor, the continuation characters
are removed before saving. While in the editor the user can create long
lines by adding their own continuation characters. This makes using a
small screen as a console much easier.

OPTION CPUSPEED speed

Page 90



NOT ON HDMI OR VGA VERSIONS
Change the CPU clock speed.
‘speed’ is the CPU clock in KHz in the range of 48000 to 378000. Speeds
above 200MHz (150MHz for the RP2350) are regarded as overclocking as
that is the specified maximum speed of the standard Raspberry Pi Pico.

PicoMite User Manual

Default speed is 200000 for the RP2040 and 150000 for the RP2350.
This command must be run at the command prompt (not in a program).
OPTION COUNT pin1, pin2,
pin3, pin4

which pins are to be used as Count inputs. By default these are
 Specifies
GP6, GP7, GP8 and GP9. The SETPIN command defines the Counter
mode.
This command must be run at the command prompt (not in a program).

OPTION DEFAULT FLOAT |
INTEGER | STRING | NONE

Used to set the default type for a variable which is not explicitly defined.
If OPTION DEFAULT NONE is used then all variables must have their
type explicitly defined or the error “Variable type not specified” will
occur.
When a program is run the default is set to FLOAT for compatibility with
Microsoft BASIC and previous versions of MMBasic.

OPTION DEFAULT
COLOURS foreground
[,background]

Set the default foreground and background colours for both the
monochrome and colour modes. The colour must be one of the following:
white, yellow, lilac, brown, fuchsia, rust, magenta, red, cyan, green,
cerulean, midgreen, cobalt, myrtle, blue and black. A numeric value
cannot be used. The default is white, black.
If background is omitted it defaults to black.



OPTION DEFAULT MODE n

sets the default display mode on boot. This command must be run at
 This
the command prompt (not in a program).

OPTION DISK SAVE fname$
OPTION DISK LOAD fname$

commands let the user save and restore the complete set of options
 These
defined to and from a disk file. The file could then be transferred to a host
computer using XMODEM allowing additional devices to be easily
configured or options recovered after a firmware upgrade

OPTION DISPLAY lines
[,chars]

the characteristics of the display terminal used for the console. Both
 Set
the LIST and EDIT commands need to know this information to
correctly format the text for display.
'lines' is the number of lines on the display and 'chars' is the width of the
display in characters. The default is 24 lines x 80 chars and when
changed this option will be remembered even when the power is
removed. Maximum values are 100 lines and 240chars.
This will send an ESC sequence to set the VT100 terminal to the
matching size. TerraTerm, Putty and MMCC respond to this sequence
and set the terminal width (if the option is enabled in the terminal setup).
This option is not available if an LCD display is being used as the
console.

OPTION ESCAPE

Enables the ability to insert escape sequences into string constants. See
the section Special Characters in Strings.

OPTION EXPLICIT

Placing this command at the start of a program will require that every
variable be explicitly declared using the DIM, LOCAL or STATIC
commands before it can be used in the program.
This option is disabled by default when a program is run. If it is used it
must be specified before any variables are used.

OPTION FAST AUDIO
ON|OFF

When using the PLAY SOUND command, changes to sounds, volumes,
or frequencies can cause audible clicks in the output. The firmware
attempts to mitigate this by ramping the volume down on the channel’s
previous output before changing the output and ramping it back up
again. This significantly improves the audio output but at the expense of

PicoMite User Manual

Page 91

a short delay in the PLAY SOUND command (worst case 3mSec). This
delay can be avoided using OPTION FAST AUDIO ON in a program.
The audible clicks may then re-appear but this is at the programmer’s
discretion.
This is a temporary option that is reset to OFF whenever a program is
run.
OPTION FNKey string$

the string that will be generated when a function key is pressed at
 Define
the command prompt. ‘FNKey’ can be F1, and F5 thru to F9.
Example:
OPTION F8 “RUN “+chr$(34)+”myprog” +chr$(34)+chr$(13)+chr$(10).

This command must be run at the command prompt (not in a program).
OPTION HEARTBEAT
ON/OFF [HEARTBEATpin]

 Enables or disables the output of the heartbeat LED.

In the case of the Pico-W the heartbeat is on a pin controlled by the
CWY43 chip.
NOT WEBMITE VERSION
By default, for RP2350A chips the heartbeat is enabled on GP25.
If it is disabled the program can control the LED via GP25.
For RP2350B chips the heartbeat is not enabled.
If the heartbeat is disabled then the command can be used both to
enable it and optionally specify the pin to use (default GP25)
HDMI VERSION ONLY
Set the I/O pins used for the HDMI video output. This is only required to
suit nonstandard PCB layouts.
The positive HDMI signal pins are set according to 'nbr' below. Valid
values are 0-7 and the pins must not overlap for each channel. If 'nbr' is an
even number the negative output is on physical pin+1, if 'nbr' is odd it will
be on physical pin-1.
nbr
HSTX Nbr
Physical Pin
0
HSTX0
GP12
1
HSTX1
GP13
2
HSTX2
GP14
3
HSTX3
GP15
4
HSTX4
GP16
5
HSTX5
GP17
6
HSTX6
GP18
7
HSTX7
GP19
The default is: OPTION HDMI PINS 2, 0, 6, 4
Which means that:
CK+ and CK- are allocated to GP14 and GP15
D0+ and D0- are allocated to GP12 and GP13
D1+ and D1- are allocated to GP18 and GP19
D2+ and D2- are allocated to GP16 and GP17

OPTION HDMI PINS
clockpositivepin, d0positivepin,
d1positivepin, d2positivepin



OPTION KEYBOARD nn
[,capslock] [,numlock]
[,repeatstart] [,repeatrate]
or
OPTION KEYBOARD
DISABLE

a keyboard. This can be used for console input and any
 Configure
characters typed will be available via any commands that read from the

Page 92

console (serial over USB).
‘nn is a two character code defining the keyboard layout. The choices are
US for the standard keyboard layout in the USA, Australia and New
Zealand and UK for the United Kingdom, GR for Germany, FR for
France, BR for Brazil and ES for Spain.

PicoMite User Manual

This command must be entered at the command line and will cause a
reboot. This setting can be reset with: OPTION KEYBOARD DISABLE
The optional parameters 'capslock' and 'numlock' are true/false integers
that set the initial state of the keyboard (default is 0 and 1).
The optional parameters 'repeatstart' and 'repeatrate' set the time for the
first repeat of a key that is held down and subsequent repeats. For a
USB keyboard they are 100 to 2000mSec and 25 to 2000mSec. For a
PS2 keyboard they are 0 to 3 indicating 250mSec, 500mSec, 750mSec and
1000mSec (default is 1) and 0 to 31 indicating 33mSec to 500mSec as per
the PS2 keyboard specification (default is 12 or 100mSec).
OPTION KEYBOARD I2C

support for the Solderparty bbq20 mini I2C keyboard.
 Configures
Note: OPTION SYSTEM I2C must be set before executing this command

OPTION KEYBOARD PINS
clockpin, datapin

the user to select the pins to be used for connecting a PS2
 Allows
keyboard. The default is pin 11 (GP8) and pin 12 (GP9).
The PS2 keyboard must be disabled (OPTION KEYBOARD DISABLE)

OPTION KEYBOARD
REPEAT repeatstart , repeatrate

OPTION LCDPANEL




USB KEYBOARD ONLY
Sets the time for the first repeat of a key that is held down (100-2000)
and subsequent repeats (25-2000) in milliseconds.
NOT VGA OR HDMI VERSIONS
Configures an LCD panel on versions that accept a connected LCD.

OPTION LCDPANEL
VIRTUAL_C
or
OPTION LCDPANEL
VIRTUAL_M

Configures a virtual LCD panel without a physically connected panel.
VIRTUAL _C = Colour, 4bit, 320 x 240
VIRTUAL _M = Monochrome, 640 x 480
Using this feature a program can draw graphical images on this virtual
panel and then save them as a BMP file. Useful for creating a graphic
image for export without an attached display

OPTION LCDPANEL options
or
OPTION LCDPANEL DISABLE

Configures the PicoMite firmware to work with an attached LCD panel.
See the chapter LCD Displays for the details.
This command must be run at the command prompt (not in a program).

OPTION LCDPANEL
CONSOLE [font [, fc [, bc [,
blight]]] [,NOSCROLL]
or
OPTION LCDPANEL
NOCONSOLE

Configures the LCD display panel for use as the console output. The LCD
must support transparent text (i.e. the SSD1963_x, ILI9341 or
ST7789_320 controllers).
'font' is the default font, 'fc' is the default foreground colour, 'bc' is the
default background colour. These parameters are optional and default to
font 1, white, black and 100%. These settings are applied at power up.
The optional NOSCROLL command changes the firmware such that
when outputting to the last line of the display rather than the display
scrolling it is cleared and output continues at the top of the display. This
allows displays that don’t support reading to be used as a console device
and:
Note that for displays other than the SSD1963 scrolling for any console
output is very slow so it is recommended to use the NOSCROLL option
for these displays. This setting is saved in flash and will be automatically
applied on startup. To disable it use the OPTION LCDPANEL
NOCONSOLE command.
This command must be run at the command prompt.

PicoMite User Manual

Page 93

OPTION LCDPANEL USER
hres, vres

OPTION LCDPANEL
CONSOLE [font [, fc [,bc]]
or
OPTION LCDPANEL
NOCONSOLE

OPTION LCD320 ON/OFF

Configures a user written display driver in MMBasic. See the file “User
Display Driver.txt” in the PicoMite firmware distribution for a description
of how to write the driver.



VGA AND HDMI VERSIONS ONLY
Changes the default font used on the VGA or HDMI display.
‘fc’ is the foreground colour and ‘bc’ is the background colour.
Disables the console output to the VGA/HDMI display.
This option is permanent, both print output and console output will be
disabled and only graphics commands will output to the VGA screen
If output is required to be temporarily disabled in a program use the
OPTION CONSOLE command
For SSD1963 based displays in landscape and SPI displays in portrait the
firmware uses H/W scrolling to improve display console performance.
NOT VGA OR HDMI VERSIONS
This enables or disables 16-bit LCD displays in 320x240 mode allowing
things like games on these larger LCD displays. In the case of 800x480
displays the 320x240 image is scaled by 2 and occupies the screen area
80,0 to 719,479
In the case of 480x272 displays the 320x240 image is windowed and
occupies the screen area 80,16 to 399,255

OPTION LEGACY ON
or
OPTION LEGACY OFF

This will turn on or off compatibility mode with the graphic commands
used in the original Colour Maximite. The commands COLOUR, LINE,
CIRCLE and PIXEL use the legacy syntax and all drawing commands
will accept colours in the range of 0 to 7. Notes:
 Keywords such as RED, BLUE, etc are not implemented so they
should be defined as constants if needed.
 Refer to the Colour Maximite MMBasic Language Manual for the
syntax of the legacy commands. This can be downloaded from
https://geoffg.net/OriginalColourMaximite.html .

OPTION LIST

This will list the settings of any options that have been changed from their
default setting and are the permanent type. OPTION LIST also shows the
version number and which firmware is loaded.
This command must be run at the command prompt (not in a program).

OPTION MILLISECONDS
ON|OFF

OPTION MODBUFF
ENABLE/DISABLE [sizeinK]

This enables or disables a millisecond output in the TIME$ function.
Ie, HH:MM:SS.mmm
The milliseconds counter is set to zero whenever the time is updated
using the TIME command, WEB NTP command or RTC GETTIME
command. Default is OFF.
or removes an area of flash memory used for loading and
 Creates
playing .MOD files. If enabled then a mod buffer is created with a size
of 128Kbytes. This can be overridden with “sizeinK”.
Note that this option reserves part of the Flash Filesystem (ie, it shrinks
the Flash Filesystem). The default is disabled.
Note: This option is not required on an RP2350 with PSRAM enabled.
In this case the MOD file will be loaded to space in the PSRAM.

Page 94

PicoMite User Manual

NON USB FIRMWARE ONLY
Set the pins to be used to connect a PS2 mouse. Using this command the
mouse is automatically configured on boot and you can set up interrupts
and read values with no additional commands. This is different from the
MOUSE OPEN which only connects to a mouse while the program is
running. The PS2 mouse MUST be is disabled.

OPTION MOUSE CLKpin,
DATApin



OPTION MOUSE DISABLE

the automatic connection to a PS2 mouse and frees up the pins
 Disables
for normal usage.

OPTION NOCHECK ON/OFF

This command, when set ON, disables the standard checking for
interrupts and ctrl-C at the end of every command. Setting it to ON
allows time critical processing to take place without risk of interruption.
However, the command should be used carefully or the program may
only be stopped with a H/W reset.

OPTION PICO ON/OFF

OPTION PIN nbr

OPTION PLATFORM name$



ALL VERSIONS EXCEPT WEBMITE
When set to OFF pins GP23, GP24 and GP29 are not set up for normal
Pico use and are immediately available to use. Default ON for RP2350A
and RP2040, OFF for RP2350B
Set 'nbr' as the PIN (Personal Identification Number) for access to the
console prompt. 'nbr' can be any non zero number of up to eight digits.
Whenever a running program tries to exit to the command prompt for
whatever reason MMBasic will request this number before the prompt is
presented. This is a security feature as without access to the command
prompt an intruder cannot list or change the program in memory or
modify the operation of MMBasic in any way. To disable this feature
enter zero for the PIN number (i.e. OPTION PIN 0).
A permanent lock can be applied by using 99999999 for the PIN
number. If a permanent lock is applied or the PIN number is lost the
only way to recover is to reload the PicoMite firmware.
This command must be run at the command prompt (not in a program).

a user to identify a particular hardware configuration that can
 Allows
then be used in programs to control the program's operation.
'name$' can be up to 31 characters long. This is a permanent option.
MM.INFO$(PLATFORM) returns this string.
For example, this can be used on a particular hardware configuration:
OPTION PLATFORM "GameMite"
Then programs that might run on this or other platforms can use:
IF MM.INFO$(PLATFORM) = "GameMite" THEN …

OPTION POWER PFM |
PWM

 Changes operation of the 3.3V supply switch mode power supply.

OPTION PSRAM PIN n
or
OPTION PSRAM PIN
DISABLE

 Enable/disable PSRAM support.

PicoMite User Manual

By default this runs in PFM mode. PWM gives better noise performance
but is less power-efficient. Note that under heavy load the system will
run in PWM mode regardless of this setting.

‘n’ is the PSRAM chip select (CS) pin and can be GP0, GP8, GP19, or
GP47.
Typically GP47 is used for Pimoroni boards. Default is disabled.

Page 95

OPTION RESET

 Reset all saved options to their default values.

This command must be run at the command prompt (not in a program).

OPTION RESET cfg
or
OPTION RESET LIST

OPTION RESOLUTION nn
[,cpuspeedinKhz]



Reset all options to default values for the configuration ‘cfg’.
OPTION RESET LIST will list all available configurations.
This command must be run at the command prompt (not in a program).
HDMI and VGA VERSIONS ONLY
For firmware with HDMI video set the video resolution to ‘nn’.
Where ‘nn’ is:
640x480 or 640
720x400 or 720
800x600 or 800 (RP2350 only)
848x480 or 848 (RP2350 only)
1280x720 or 1280 (HDMI only)
1024x768 or 1024 (HDMI only)
For 640x480 the display frequency can be set to 60Hz (252Mhz or
378MHz) or 75Hz (315MHz) by appending 'cpuspeedinKHz' to the
command (ie, 252000, 378000 or 315000).
Each VGA and HDMI resolution can operate in a number of modes
which are set using the MODE command.
Note that 800x600 and 848x480 resolutions reduce both the maximum
program size and the variable space available to the Basic programs

OPTION RTC AUTO
ENABLE | DISABLE

auto-load time$ & date$ from RTC on boot & every hour. If
 Enable
enabled and the RTC does not respond then any running program will
abort with an error. At the command prompt an information message
will be output.
This command must be run at the command prompt (not in a program).

OPTION SDCARD CSpin
[,CLKpin, MOSIpin,
MISOpin]
or
OPTION SDCARD DISABLE

 Specify or disable the I/O pins to use for the SD Card interface.

OPTION SDCARD
COMBINED CS

specifies that the touch chip select pin is also used for the SDcard.
 This
In this case external circuitry is needed to implement the SD chip select.

If the optional pins are not specified the SD Card will use the pins
specified by OPTION SYSTEM SPI.
Note: The pins specified by OPTION SYSTEM SPI must be a valid set
of hardware SPI pins (SPI or SPI2), however, the pins specified by
OPTION SDCARD can be any pins. The pins specified by OPTION
SYSTEM SPI and OPTION SDCARD cannot be the same.
This command must be run at the command prompt (not in a program).

See “SD Cards” in the chapter “Program and Data Storage”.
OPTION SERIAL CONSOLE
uartapin, uartbpin [,B]

that the console be accessed via a hardware serial port (instead
 Specify
of virtual serial over USB).
‘uartapin’ and ‘uartbpin’ can be any valid pair of rx and tx pins for either
COM1 or COM2. The order that they are specified is not important.
The speed defaults to 115200 baud but can be changed with OPTION
BAUDRATE. Adding the "B" parameter means output will go to "B"oth
the serial port and the USB.

Page 96

PicoMite User Manual

OPTION SERIAL CONSOLE
DISABLE

Revert to the normal the USB console.
These commands must be run at the command prompt (not in a program).

OPTION SYSTEM I2C sdapin,
sclpin [,SLOW/FAST]

2

the I C port and pins for use by system devices (LCD panel, and
 Specify
RTC).
The PicoMite firmware uses a specific I2C port for system devices,
leaving the other for the programmer. This command specifies which
pins are to be used, and hence which of the I2C ports is to be used.
The pins allocated to the SYSTEM I2C will not be available for other
MMBasic SETPIN settings but can be used for additional I2C devices
using the standard I2C command. Note: I2C(2) OPEN and I2C(2)
CLOSE are not available in this case.
By default the I2C port is opened at a speed of 400KHz and with a
100mSec timeout. The I2C frequency can be set using the optional third
parameter which can take the values FAST = 400KHz or SLOW =
100KHz.
This command must be run at the command prompt (not in a program).

OPTION SYSTEM SPI
CLKpin, MOSIpin, MISOpin
or
OPTION SYSTEM SPI
DISABLE

or disable the SPI port and pins for use by system devices (SD
 Specify
Card, LCD panel, etc).

OPTION TAB 2 | 3 | 4 | 8

 Set the spacing for the tab key. Default is 2.

OPTION TCP SERVER PORT
n

OPTION TELNET CONSOLE
OFF|ONLY|ON

OPTION TFTP OFF|ON

OPTION TOUCH T_CS pin,
T_IRQ pin [, Beep]
or
OPTION TOUCH DISABLE

PicoMite User Manual

The PicoMite firmware uses a specific hardware SPI port for system
devices, leaving the other for the user. This command specifies which
pins are to be used, and hence which of the SPI ports is to be used. The
pins allocated to the SYSTEM SPI will not be available to other
MMBasic commands.
This command must be run at the command prompt (not in a program).








WEBMITE ONLY
Launches a TCP server on port 'n' during every restart of the WebMite.
Typically HTTP servers use port 80.
USE "OPTION TCP SERVER PORT 0" to disable
When the server is running it can respond to up to MM.INFO(MAX
CONNECTIONS)
WEBMITE ONLY
Configures the handling the console over Telnet.
ON = Console output sent to USB and Telnet
ONLY= Console output sent to Telnet only
OFF = Console output sent to USB only
WEBMITE ONLY
Enables or disables the TFTP server. Default is on.
NOT VGA OR HDMI VERSIONS
Configures MMBasic for the touch sensitive feature of an attached LCD
panel.
'T_CS pin' and 'T_IRQ pin' are the I/O pins to be used for chip select and
touch interrupt respectively (any free pins can be used). The remaining
pins are connected to those specified using the OPTION SYSTEM SPI
command.

Page 97

‘Beep’ is an optional pin which can be connected to a small
buzzer/beeper to generate a "click" or beep sound when an Advanced
Graphics control is touched (ie, radio button, switch, etc). This is
described in Advanced Graphics Functions.pdf.
This command must be run at the command prompt (not in a program).

OPTION TOUCH FT6336
IRQpin, RESETpin [,BEEPpin]
[,sensitivity]



OPTION VCC voltage

OPTION UDP SERVER
PORT n

OPTION VGA PINS
HSYNCpin, BLUEpin

Specifies the voltage (Vcc) supplied to the Raspberry Pi Pico.
When using the ADC pins to measure voltage the PicoMite firmware
uses the voltage on the pin marked VREF as its reference. This voltage
can be accurately measured using a DMM and set using this command
for more accurate measurement.
The parameter is not saved and should be initialised either on the
command line or in a program. The default if not set is 3.3.



Page 98

WEBMITE VERSION ONLY
Sets up a listening socket on the port specified. Any UDP datagrams
received on that port will be processed and the contents saved in
MM.MESSAGE$. The IP address of the sender will be stored in
MM.ADDRESS$. Note: If the UDP datagram is longer than 255
characters then any extra is discarded.
USE "OPTION UDP SERVER PORT 0" to disable

 VGA VERSION ONLY

Changes the pins used for VGA display output allowing more flexibility
in PCB design or wiring. “HSYNCpin” defines the start of a pair of
contiguous GP numbered pins that are connected to HSYNC and
VSYNC
“BLUEpin” defines the start of four contiguous GP numbered pins that
are connected to BLUE, GREEN_LSB, GREEN_MSB, and RED.
WEBMITE VERSION ONLY
Disable informational web messages when set to OFF. Default is ON

OPTION WEB MESSAGES
ON/OFF

OPTION WIFI ssid$, passwd$,
[name$] [,ipaddress$, mask$,
gateway$]

NOT VGA OR HDMI VERSIONS
Enables touch support for FT6336 capacitive touch chip. Sensitivity is a
number between 0 and 255 - defaults to 50, lower is more sensitive.
SDA and SCK should be connected to valid I2C pins and set up with
OPTION SYSTEM I2C. See also the TOUCH function.



WEBMITE VERSION ONLY
Configures the firmware to automatically connect to a WiFi network on
restart.
'ssid$' is the name of the network and 'password$' is the access
password. Both are strings and if string constants are used they should
be quoted.
Optionally a name for the device can be specified ‘name$’, otherwise a
name is created from the unique device ID.
Optionally, a static IP address, IP mask, and gateway address can be
specified as ‘ipaddress$’, ‘mask$’, ‘gateway$’
eg, OPTION WIFI “mysid”,”mypassword”, ”myPico”,
“192.168.1.111”, ”255.255.255.0”, ”192.168.1.1”


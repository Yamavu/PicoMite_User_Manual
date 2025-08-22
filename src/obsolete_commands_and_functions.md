# Obsolete Commands and Functions

Appendix A – Serial Communications ................................................................................ 153
Appendix B – I2C Communications .................................................................................... 155
Appendix C – 1-Wire Communications ............................................................................... 158
Appendix D – SPI Communications.................................................................................... 159
Appendix E – Regex Syntax ............................................................................................... 161
Appendix F – The PIO Programming Package................................................................... 163
Appendix G – Programming in BASIC - A Tutorial ............................................................. 170



Introduction
The PicoMite is a Raspberry Pi Pico running the MMBasic interpreter.
MMBasic is a Microsoft BASIC compatible implementation of the BASIC
language with floating point, integer and string variables, arrays, long
variable names, a built in program editor and many other features.
Using MMBasic you can control the I/O pins and use communications
protocols such as I2C or SPI to get data from a variety of sensors. You can
display data on low-cost colour LCD displays, measure voltages, detect
digital inputs and drive output pins to turn on lights, relays, etc.
The PicoMite firmware is totally free to download and use.
The emphasis with MMBasic is on ease of use and development. The development cycle is very fast with the
ability to instantly switch from edit to run. Errors are listed in plain English and when an error does occur a
single keystroke will invoke the built-in editor with the cursor positioned on the line that caused the error.
In summary the features of the PicoMite are:


The BASIC interpreter is full featured with floating point, 64-bit integers and string variables, long
variable names, arrays of floats, integers or strings with multiple dimensions, extensive string handling
and user defined subroutines and functions. Typically, it will execute a program up to 100,000 lines per
second. MMBasic allows the embedding of compiled C programs for high performance functions and
the running program can be protected from being listed or modified by a PIN number.



Support for all Raspberry Pi Pico input/output pins. These can be independently configured as
digital input or output, analog input, frequency or period measurement and counting. Within MMBasic
the I/O pins can be dynamically configured as inputs or outputs. MMBasic commands will generate
pulses and can be used to transfer data in parallel. Interrupts can be used to notify when an input pin has
changed state. PWM outputs can be used to create various sounds, control servos or generate computercontrolled voltages for driving equipment that uses an analogue input (e.g. motor controllers). In
addition, pins that are not exposed on the Raspberry Pi Pico can be accessed using MMBasic allowing it
to be used on other modules that use the RP2040 processor.



Support for TFT LCD display panels using parallel, SPI and I2C interfaces allowing the BASIC
program to display text and draw lines, circles, boxes, etc in up to 16 million colours. Resistive touch
controllers on these panels are also supported allowing them to be used as sophisticated input devices.
LCD panels can cost as little as US$7 and provide a low cost, high tech graphical user interface. For
higher speed and greater resolution parallel interface TFT screens are also supported.



Flexible program and data storage. Programs and data can be read/written from an internal file system
(approx 688KB) or to an externally connected SD Card up to 32GB formatted as FAT16 or FAT32. This
includes opening files for reading, writing or random access and loading and saving programs. The SD
Card can also be read/written on personal computers running Windows, Linux or the Mac operating system.



Programming and control is done via the USB interface. All that is needed is a laptop/desktop
computer running a VT100 terminal emulator. Once the program has been written and debugged the
PicoMite can be instructed to automatically run the program on power up with no user intervention.



A full screen editor is built into the PicoMite and can edit the whole program in one session. It includes
advanced features such as colour coded syntax, search and copy, cut and paste to and from a clipboard.



Programs can be easily transferred from a desktop or laptop computer (Windows, Mac or Linux) using
the XModem protocol or by streaming the program over the serial console input.



A comprehensive range of communications protocols are implemented including I2C, asynchronous
serial, RS232, SPI and 1-Wire. These can be used to communicate with many sensors (temperature,
humidity, acceleration, etc) as well as for sending data to test equipment.



The PicoMite has built in commands to directly interface with infrared remote controls, the DS18B20
temperature sensor, LCD display modules, battery backed clock, numeric keypads and more.



Power requirements are 2.0 to 5.5 volts at 10 to 42 mA.



Getting Started
Loading the PicoMite Firmware
The Raspberry Pi Pico comes with its own built in firmware loader that is easy to use. Just follow these steps:
 Download the PicoMite firmware from http://geoffg.net/picomite.html and unzip the file. Identify the
firmware which should be named something like “PicoMiteV5.xx.xx.uf2”.


Using a USB cable plug the Raspberry Pi Pico into your computer (Windows, Linux or Mac) while
holding down the white BOOTSEL button on the Raspberry Pi Pico.



The Raspberry Pi Pico should connect to your computer and create a virtual drive (the same as if you had
plugged in a USB memory stick) called “RPI-RP2”. This drive will contain two files which you can
ignore.



Copy the firmware file (with the extension .uf2) to this virtual drive.



When the copy has completed the Raspberry Pi Pico will restart and create a virtual serial port on your
computer. The LED on the Raspberry Pi Pico will blink slowly indicating that the PicoMite firmware
with MMBasic is now running.

While the virtual drive created by the Raspberry Pi Pico looks like a USB memory stick it is not, the firmware
file will vanish once copied and if you try copying any other type of file it will be ignored.
Loading the PicoMite firmware will erase the flash memory including the current program, any programs saved
in flash memory slots and all saved variables. So make sure that you backup this data before you upgrade the
firmware.
It is possible for the flash memory to be corrupted resulting in unusual and unpredictable behaviour. In that
case you should load the firmware file https://geoffg.net/Downloads/picomite/Clear_Flash.uf2 which will reset
the Raspberry Pi Pico to its factory fresh state, then you can reload the PicoMite firmware.

Virtual Serial Port
The virtual serial port created by the PicoMite firmware acts
like a normal serial port but it operates over USB.
Windows 10 includes a driver for this virtual serial port but
with other versions you may have to load a driver to make it
work with the operating system (see below).
Once this is done you should note the port number created by
your computer for the virtual serial connection. In Windows
this can be done by starting Device Manager and checking the
"Ports (COM & LPT)" entry for a new COM port as shown on
the right.

Terminal Emulator
You also need a terminal emulator program on your desktop computer. This program acts like an old fashioned
computer terminal where it will display text received from a remote computer and any key presses will be sent
to the remote computer over the serial link. The terminal emulator that you use should support VT100
emulation as that is what the editor built into the PicoMite expects.
For Windows users it is recommended that you use Tera Term as this has a good VT100 emulator and is known
to work with the XModem protocol which you can use to transfer
programs to and from the PicoMite (Tera Term can be downloaded from:
http://tera-term.en.lo4d.com ).
The screen shot on the right shows the setup for Tera Term. Note that the
"Port:" setting will vary depending on which USB port your Raspberry Pi
Pico was plugged into. The PicoMite ignores the baud rate setting so it can
be set to any speed (other than 1200 baud which puts the Pico into
firmware upgrade mode).
If you are using Tera Term do not set a delay between characters and if
you are using Putty set the backspace key to generate the backspace
character.



The Console
Once you have identified the virtual serial port and
have connected your terminal emulator to it you
should be able to press return on your keyboard and
see the MMBasic prompt, which is the greater than
symbol (e.g. “>”).
This is the console and you use it to issue
commands to configure the PicoMite, load the
BASIC program, edit and run it. MMBasic also
uses the console to display error messages.
The console is the only method of communicating
with the PicoMite and programming it, so it is
important that you can connect to it.

Some Tests
Here are a few things that you can try out to prove that you have a working PicoMite.
All of these commands should be typed at the command prompt (">"). What you type is shown in bold and the
PicoMite’s output is shown in normal text.
Try a simple calculation:

> PRINT 1/7
0.1428571429
See how much memory you have:

> MEMORY
Program:
0K ( 0%) Program (0 lines)
80K (100%) Free
RAM:
0K ( 0%) 0 Variables
0K ( 0%) General
112K (100%) Free
What is the current time? Note that the PicoMite's clock starts at midnight on power up.

> PRINT TIME$
00:04:01
Set the clock to the current time:

> TIME$ = "10:45"
Check the time again:

> PRINT TIME$
10:45:09
How many milliseconds have elapsed since power up:

> PRINT TIMER
440782 .748
Count to 20:

> FOR a = 1 to 20 : PRINT a; : NEXT a
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20



Windows 7 and 8.1
The USB serial port uses the CDC protocol and the drivers for this are standard in Windows 10 and 11 and will
load automatically.
The Raspberry Pi Foundation lists Windows 7 or 8.1 as “unsupported” however you can use a tool like Zadig
( https://zadig.akeo.ie ) to install a generic driver for a “usbser” device and that should allow these computers to
connect. This post describes the process: https://github.com/raspberrypi/pico-feedback/issues/118

Apple Macintosh
The Apple Macintosh (OS X) is somewhat easier as it has the device driver and terminal emulator built in.
First start the application ‘Terminal’ and at the prompt list the connected serial devices by typing in:
ls /dev/tty.*.
The USB to serial converter will be listed as something like /dev/tty.usbmodem12345. While still at the
Terminal prompt you can run the terminal emulator at 38400 baud by using the command:
screen
/dev/tty.usbmodem12345 38400
By default the function keys will not be correctly defined for use in the PicoMite's built in program editor so
you will have to use the control sequences as defined in the section Full Screen Editor of this manual. To avoid
this you can reconfigure the terminal emulator to generate these codes when the appropriate function keys are
pressed.
Documentation for the screen command is here: https://www.systutorials.com/docs/linux/man/1-screen/

Linux
For Linux see these posts:
https://www.thebackshed.com/forum/ViewTopic.php?TID=14157&PID=175474#175474#175466
and
https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=16312&LastEntry=Y#213664#213594

Android
For Android devices see this post:
https://www.thebackshed.com/forum/ViewTopic.php?TID=16312&PID=213594#213594#213594



Quick Start Tutorial
A Simple Program
To enter a program, you can use the EDIT command which is described later in this manual. However, for the
moment, all that you need to know is that anything that you type will be inserted at the cursor, the arrow keys
will move the cursor and backspace will delete the character before the cursor.
To get a quick feel for how the PicoMite works, try this sequence (your terminal emulator must be VT100
compatible):
 At the command prompt type EDIT followed by the ENTER key.


The editor should start up and you can enter this line: PRINT "Hello World"



Press the F1 key in your terminal emulator (or CTRL-Q which will do the same thing). This tells the
editor to save your program and exit to the command prompt.



At the command prompt type RUN followed by the ENTER key.



You should see the message: Hello World

Congratulations. You have just written and run your first program on the PicoMite. If you type EDIT again
you will be back in the editor where you can change or add to your program.

Flashing a LED
Connect a LED to pin GP21 (marked on the underside of the board)
and a ground pin as shown in the diagram on the right.
Then use the EDIT command to enter the following program:
SETPIN GP21, DOUT
DO
PIN(GP21) = 1
PAUSE 300
PIN(GP21) = 0
PAUSE 300
LOOP

GP21
470 ohms LED
GND

When you have saved and run this program you should be greeted by the LED flashing on and off. It is not a
great program but it does illustrate how the PicoMite can interface to the physical world via your programming.
The program itself is simple. The first line sets pin GP21 as an output. Then the program enters a continuous
loop where the output of that pin is set high to turn on the LED followed by a short pause (300 milliseconds).
The output is then set to low followed by another pause. The program then repeats the loop.
If you leave it this way, the PicoMite will sit there forever with the LED flashing. If you want to change
something (for example, the speed of flashing) you can interrupt the program by typing CTRL-C on the console
and then edit it as needed. This is the great benefit of MMBasic, it is very easy to write and change a program.
If you want this program to automatically start running every time power is applied you can use the command:
OPTION AUTORUN ON
To test this you can remove the power and then re-apply it. The PicoMite should start up flashing the LED.

Tutorial on Programming in the BASIC Language
If you are new to the BASIC programming language now would be a good time to turn to Appendix G
(Programming in BASIC - A Tutorial) at the rear of this manual. This is a comprehensive tutorial on the
language which will take you through the fundamentals in an easy to read format with lots of examples.



PicoMite Hardware
This diagram shows the possible uses within MMBasic for each I/O pin on the Raspberry Pi Pico:
PWM0A COM1 TX I2C SDA
PWM0B COM1 RX I2C SCL
PWM1A
PWM1B
PWM2A COM2 TX
PWM2B COM2 RX
PWM3A
PWM3B
PWM4A COM2 TX
PWM4B COM2 RX
PWM5A
PWM5B
PWM6A COM1 TX
PWM6B COM1 RX
PWM7A
PWM7B

SPI RX

GP0
1
GP1
2
GND
I2C2 SDA SPI CLK GP2
4
I2C2 SCL SPI TX
GP3
5
I2C SDA SPI RX
GP4
6
I2C SCL
GP5
7
GND
I2C2 SDA SPI CLK GP6
9
I2C2 SCL SPI TX
GP7 10
I2C SDA SPI2 RX GP8 11
I2C SCL
GP9 12
GND
I2C2 SDA SPI2 CLK GP10 14
I2C2 SCL SPI2 TX
GP11 15
I2C SDA SPI2 RX GP12 16
I2C SCL
GP13 17
GND
I2C2 SDA SPI2 CLK GP14 19
I2C2 SCL SPI2 TX
GP15 20

VREF
ADC2
AGND
ADC1
ADC0

VBUS
VSYS
GND
3V3EN
3V3
ADC VREF
34 GP28 SPI2 RX I2C SDA COM1 TX
GND
32 GP27 SPI2 TX I2C2 SCL
31 GP26 SPI2 CLK I2C2 SDA
RUN
29 GP22
I2C2 SDA
GND
27 GP21
I2C SCL COM2 RX
26 GP20 SPI RX I2C SDA COM2 TX
25 GP19 SPI TX I2C2 SCL
24 GP18 SPI CLK I2C2 SDA
GND
22 GP17
I2C SCL COM1 RX
21 GP16 SPI RX I2C SDA COM1 TX

PWM6A
PWM5B
PWM5A
PWM3A
PWM2B
PWM2A
PWM1B
PWM1A
PWM0B
PWM0A

The notation is as follows:
GP0 to GP28
Can be used for digital input or output.
COM1, COM2
Can be used for asynchronous serial I/O (UART0 and UART1 pins on the Pico
datasheet).
I2C, I2C2
Can be used for I2C communications (I2C0 and I2C1 pins on the Pico datasheet).
SPI, SPI2
Can be used for SPI I/O (see Appendix D). (SPI0 and SPI1 pins on the Pico datasheet).
PWMnx
Can be used for PWM output (see the PWM command).
GND
Common ground.
VBUS
5V supply directly from the USB port.
VSYS
5V supply used by the SMPS to provide 3.3V. This can be used as a 5V output or input.
3V3EN
Enable 3.3V regulator (low = off, high = enabled).
RUN
Reset pin, low will hold the PicoMite in reset.
ADCn
These pins can be used to measure voltage (analog input).
ADC VREF
Reference voltage for voltage measurement.
AGND
Analog ground.
All pins can be used for digital input or output however they are limited to a maximum voltage of 3.6V. This
means that level shifting will be required if they are used with devices operating at 5V or higher.
Within the MMBasic program I/O pins can be referred to using the physical pin number (i.e. 1 to 40) or the GP
number (i.e. GP0 to GP28). For example, the following refer to the same pin and operate identically:

SETPIN 32, DOUT
and

SETPIN GP27, DOUT
On the PicoMite on-chip functions such as the SPI and I2C interfaces are not allocated to fixed pins, unlike (for
example) the Micromite. The PicoMite makes extensive use of the SETPIN command, not only to configure
I/O pins but also to configure the pins used for interfaces such as serial, SPI, I2C, etc.
Pins must be allocated according to this drawing. For example, the SPI TX can be allocated to pins GP3, GP7
or GP19 but it cannot be allocated to pin GP11 which can only be allocated to the SPI2 channel. Allocations
don't have to be in the same "block" so you could, for example, allocate SPI2 TX to pin GP11 and SPI2 RX to
pin GP28.


Pins that are not exposed on the Raspberry Pi Pico can still be accessed using MMBasic via a pseudo pin
number or their GPn number. This allows MMBasic to be used on other modules that use the RP2040
processor. These hidden pins are Pin 41 or GP23, Pin 42 or GP24, Pin 43 or GP25 and Pin 44 or GP29.
On the Raspberry Pi Pico these pins are used for internal functions as follows:
 Pin 41 or GP23 is a digital output set to the value of OPTION POWER. (ON=PWM, OFF=PFM).
 Pin 42 or GP24 is a digital input, which is high when VBUS is present.
 Pin 43 or GP25 is also PWM4B. It is an output connected to the on-board LED.
 Pin 44 or GP29 is also ADC3 which is an analog input reading ⅓ of VSYS.

I/O Pin Limits
The maximum voltage that can be applied to any I/O pin is 3.6V.
As outputs all I/O pins can individually source or sink a maximum of 12mA. At this load the output voltage
will sag to about 2.3V. A more practical load is 5mA where the output voltage would typically be 3V. To
drive a red LED at 5mA the recommended resistor is 220Ω. Other colours may require a different value.
The maximum total I/O current load for the entire chip is 50mA.

Power Supply
The Raspberry Pi Pico has a flexible power
system.
The input voltage from either the USB or VBUS
inputs is connected through a Schottky diode to the
buck-boost SMPS (Switch Mode Power Supply)
which has an output of 3.3V. The SMPS will
accommodate input voltages from 1.8V to 5.5V
allowing the PicoMite to run from a wide range of
power sources including batteries.

VBUS

VSYS

3V3EN

3V3

100K

USB
Input

BUCK-BOOST
SMPS

RP2040
& Flash

External circuitry can be powered by VBUS
(normally 5V) or by the 3V3 (3.3V) output which
can source up to 300mA.
For embedded controller applications generally an external power source (other than USB) is required and this
can be connected to VSYS via a Schottky diode. This will allow the PicoMite to be powered by whichever
supply is producing the highest voltage (USB or VSYS). The diodes will prevent feedback into the lower
voltage supply.
To minimize power supply noise it is possible to ground 3V3EN to turn off the SMPS. When shutdown the
converter will stop switching, internal control circuitry will be turned off and the load disconnected. You can
then power the board via a 3.3V linear regulator feeding into the 3V3 pin.

Clock Speed
By default the clock speed for the PicoMite is 133MHz which is the recommended maximum for the Raspberry
Pi Pico. However, by using the OPTION CPUSPEED command, the CPU can be overclocked up to 378MHz
or run slower to a minimum of 48MHz. Nearly all tested Raspberry Pi Picos have worked correctly at 378MHz
so overclocking can be useful. If the processor fails to restart at its new clock speed you can reset it by loading
this firmware file onto the Pico: https://geoffg.net/Downloads/picomite/Clear_Flash.uf2. The procedure to do
this is same as loading any other firmware.
This option is saved and will be reapplied on power up. When changing the clock speed the PicoMite will be
reset then rebooted so the USB connection will be disconnected.

Power Consumption
The power consumption is dependent on the clock speed. These are typical readings for the PicoMite and do
not include any current sourced or sunk by the I/O pins or the 3V3 pin:
250MHz
43mA
133MHz
21mA
48MHz
10mA.



Using MMBasic
Commands and Program Input
At the command prompt you can enter a command and it will be immediately run. Most of the time you will
do this to tell the PicoMite to do something like run a program or set an option. But this feature also allows you
to test out commands at the command prompt.
To enter a program the easiest method is to use the EDIT command. This will invoke the full screen program
editor which is built into the PicoMite and is described later in this manual. It includes advanced features such
as search and copy, cut and paste to and from a clipboard.
You could also compose the program on your desktop computer using something like Notepad and then
transfer it to the PicoMite via the XModem protocol (see the XMODEM command) or by streaming it up the
console serial link (see the AUTOSAVE command).
A third and convenient method of writing and debugging a program is to use MMEdit. This is a program
running on your Windows computer which allows you to edit your program on your computer then transfer it to
the PicoMite with a single click of the mouse. MMEdit was written by Jim Hiley and can be downloaded for
free from https://www.c-com.com.au/MMedit.htm.
One thing that you cannot do is use the old BASIC way of entering a program which was to prefix each line
with a line number. Line numbers are optional in MMBasic so you can still use them if you wish but if you
enter a line with a line number at the prompt MMBasic will simply execute it immediately.

Program Structure
A BASIC program starts at the first line and continues until it runs off the end of the program or hits an END
command - at which point MMBasic will display the command prompt (>) on the console and wait for
something to be entered.
A program consists of a number of statements or commands, each of which will cause the BASIC interpreter to
do something (the words statement and command generally mean the same and are used interchangeably).
Normally each statement is on its own line but you can have multiple statements in the one line separated by
the colon character (:). For example.
A = 24.6 : PRINT A
Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters however
modern implementations (such as MMBasic) do not need them. You can still use them if you wish but they
have no benefit and generally just clutter up your programs. This is an example of a program that uses line
numbers:
50 A = 24.6
60 PRINT A
A line can also start with a label which can be used as the target for a program jump using the GOTO
command. For example (the label name is JmpBack):
JmpBack: A = A + 1
PRINT A
GOTO JmpBack

A label has the same specifications (length, character set, etc) as a variable name but it cannot be the
same as a command name. When used to label a line the label must appear at the beginning of a line
but after a line number (if used) and be terminated with a colon character (:).
Editing the Command Line
When entering a line at the command prompt the line can be edited using the left and right arrow keys to move
along the line, the Delete key to delete a character and the Insert key to switch between insert and overwrite.
At any point the Enter key will send the line to MMBasic which will execute it.
The up and down arrow keys will move through a history of previously entered command lines which can be
edited and reused.



Shortcut Keys
The function keys on the keyboard or the serial console can be used at the command prompt to automatically
enter common commands. These function keys will insert the text followed by the Enter key so that the
command is immediately executed:
F2
RUN
F3
LIST
F4
EDIT
F10
AUTOSAVE
F11
XMODEM RECEIVE
F12
XMODEM SEND
Function keys F1, and F5 to F9 can be programmed with custom text. See the OPTION FNKey command.

Interrupting A Running Program
A program is set running by the RUN command. You can interrupt MMBasic and the running program at any
time by typing CTRL-C on the console input and MMBasic will return to the command prompt.

Setting Options
Many options can be set by using commands that start with the keyword OPTION. They are listed in their own
section of this manual. For example, you can change the CPU clock speed with the command:
OPTION CPUSPEED speed

Saved Variables
Because the PicoMite does not necessarily have a normal storage system it needs to save data that can be
recovered when power is restored. This can be done with the VAR SAVE command which will save the
variables listed on its command line in non-volatile flash memory. The space reserved for saved variables is
16KB.
These variables can be restored with the VAR RESTORE command which will add all the saved variables to
the variable table of the running program. Normally this command is placed near the start of a program so that
the variables are ready for use by the program.
This facility is intended for saving calibration data, user selected options and other items which change
infrequently. It should not be used for high-speed saves as you may wear out the flash memory. The flash used
for the Raspberry Pi Pico has a high endurance but this can be exceeded by a program that repeatedly saves
variables. If you do want to save data often you should add a real time clock chip. The RTC commands can
then be used to store and retrieve data from the RTC's battery backed memory. See the RTC command for
more details.

Watchdog Timer
The main use for the PicoMite is as an embedded controller. It can be programmed in MMBasic and when the
program is debugged and ready for "prime time" the OPTION AUTORUN configuration setting can be turned
on. The module will then automatically run its program when power is applied and act as a custom circuit
performing some special task. The user need not know anything about what is running inside it.
However, there is the possibility that a fault in the program could cause MMBasic to generate an error and
return to the command prompt. This would be of little use in an embedded situation as the PicoMite would not
have anything connected to the console. Another possibility is that the BASIC program could get itself stuck in
an endless loop for some reason. In both cases the visible effect would be the same… the program would stop
running until the power was cycled.
To guard against this the watchdog timer can be used. This is a timer that counts down to zero and when it
reaches zero the processor will be automatically restarted (the same as when power was first applied), this will
occur even if MMBasic was sitting at the command prompt. Following the restart the automatic variable
MM.WATCHDOG will be set to true to indicate that the restart was caused by a watchdog timeout.
The WATCHDOG command should be placed in strategic locations in the program to keep resetting the timer
and therefore preventing it from counting down to zero. Then, if a fault occurs, the timer will not be reset, it
will count down to zero and the program will be restarted (assuming the AUTORUN option is set).



PIN Security
Sometimes it is important to keep the data and program in an embedded controller confidential. In the
PicoMite this can be done by using the OPTION PIN command. This command will set a pin number (which
is stored in flash) and whenever the PicoMite returns to the command prompt (for whatever reason) the user at
the console will be prompted to enter the PIN number. Without the correct PIN the user cannot get to the
command prompt and their only option is to enter the correct PIN or reboot the PicoMite. When it is rebooted
the user will still need the correct PIN to access the command prompt.
Because an intruder cannot reach the command prompt they cannot list or copy a program, they cannot change
the program or change any aspect of MMBasic or the PicoMite. Once set the PIN can only be removed by
providing the correct PIN as set in the first place. If the number is lost the only method of recovery is to reload
the PicoMite firmware (which will erase the program and all options).
There are other time consuming ways of accessing the data (such as using a programmer to examine the flash
memory) so this should not be regarded as the ultimate security but it does act as a significant deterrent.

The Library
Using the LIBRARY feature it is possible to create BASIC functions, subroutines and embedded fonts and add
them to MMBasic to make them permanent and part of the language. For example, you might have written a
series of subroutines and functions that perform sophisticated bit manipulation; these could be stored as a
library and become part of MMBasic and perform the same as other built-in functions that are already part of
the language. An embedded font can also be added the same way and used just like a normal font.
To install components into the library you need to write and test the routines as you would with any normal
BASIC routines. When they are working correctly you can use the LIBRARY SAVE command. This will
transfer the routines (as many as you like) to a non-visible part of flash memory where they will be available to
any BASIC program but will not show when the LIST command is used and will not be deleted when a new
program is loaded or NEW is used. However, the saved subroutines and functions can be called from within
the main program and can even be run at the command prompt (just like a built-in command or function).
Some points to note:
 Library routines act exactly like normal BASIC code and can consist of any number of subroutines,
functions, embedded C routines and fonts. The only difference is that they do not show when a program
is listed and are not deleted when a new program is loaded.


Library routines can create and access global variables and are subject to the same rules as the main
program – for example, respecting OPTION EXPLICIT if it is set.



When the routines are transferred to the library MMBasic will compress them by removing comments,
extra spaces, blank lines and the hex codes in embedded C routines and fonts. This makes the library
space efficient, especially when loading large fonts. Following the save the program area is cleared.



You can use the LIBRARY SAVE command multiple times. With each save the new contents of the
program space are appended to the already existing code in the library.



You can use line numbers in the library but you cannot use a line number on an otherwise empty line as
the target for a GOTO, etc. This is because the LIBRARY SAVE command will remove any blank lines.



You can use READ commands in the library but they will default to reading DATA statements in the
main program memory. If you want to read from DATA statements in the library you must use the
RESTORE command before the first READ command. This will reset the pointer to the library space.



The library is saved to program flash memory Slot 3 and this will not be available for storing a program if
LIBRARY SAVE is used.



You can see what is in the library by using the LIBRARY LIST command which will list the contents of
the library space.



The LIBRARY contents can be saved to disk using LIBRARY DISK SAVE fname$ and restored using
LIBRARY DISK LOAD fname$

To delete the routines in the library space you use the LIBRARY DELETE command. This will clear the space
and return the Flash Slot 3 used by the library back to being available for storage for normal programs. The
only other way to delete a library is to use OPTION RESET.



Program Initialisation
The library can also include code that is not contained within a subroutine or function. This code (if it exists)
will be run automatically before a program starts running (ie, via the RUN command). This feature can be used
to initialise constants or setup MMBasic in some way. For example, if you wanted to set some constants you
could include the following lines in the library code:
CONST TRUE = 1
CONST FALSE = 0
For all intents and purposes, the identifiers TRUE and FALSE have been added to the language and will be
available to any program that is run on the PicoMite.

MM.STARTUP
There may be a need to execute some code on initial power up, perhaps to initialise some hardware, set some
options or print a custom start-up banner. This can be accomplished by creating a subroutine with the name
MM.STARTUP. When the PicoMite is first powered up or reset it will search for this subroutine and, if found,
it will be run once.
For example, if the PicoMite has a real time clock attached, the program could contain the following code:
SUB MM.STARTUP
RTC GETTIME
END SUB
This would cause the internal clock within MMBasic to be set to the current time on every power up or reset.
After the code in MM.STARTUP has been run MMBasic will continue with running the rest of the program in
program memory. If there is no other code MMBasic will return to the command prompt.
Note that you should not use MM.STARTUP for general setup of MMBasic (like dimensioning arrays, opening
communication channels, etc) before running a program. The reason is that when you use the RUN command
MMBasic will clear the interpreter's state ready for a fresh start.

MM.PROMPT
If a subroutine with this name exists it will be automatically executed by MMBasic instead of displaying the
command prompt. This can be used to display a custom prompt, set colours, define variables, etc all of which
will be active at the command prompt.
Note that MMBasic will clear all variables and I/O pin settings when a program is run so anything set in this
subroutine will only be valid for commands typed at the command prompt (i.e. in immediate mode).
As an example the following will display a custom prompt:
SUB MM.PROMPT
PRINT TIME$ "> ";
END SUB
Note that while constants can be defined, they will not be visible because a constant defined inside a subroutine
is local to a subroutine. However, DIM will create variables that are global that that should be used instead.



Full Screen Editor
An important productivity feature is the built-in full screen editor. When running it looks like this:

When the editor starts up the cursor will be automatically positioned at the last place that you were editing or, if
your program had just been stopped by an error, the cursor will be positioned at the line that caused the error.
At the bottom of the screen the status line lists details such as the current cursor position and the common
functions supported by the editor.
If you have previously used an editor like Windows Notepad you will find that the operation of this editor is
familiar. The arrow keys will move the cursor around in the text, home and end will take you to the beginning
or end of the line. Page up and page down will do what their titles suggest. The delete key will delete the
character at the cursor and backspace will delete the character before the cursor. The insert key will toggle
between insert and overtype modes. About the only unusual key combination is that two home key presses will
take you to the start of the program and two end key presses will take you to the end.
At the bottom of the screen the status line will list the various function keys used by the editor and their action.
In more details these are:
ESC

F1: SAVE
F2: RUN
F3: FIND
SHIFT-F3
F4: MARK
F5: PASTE

This will cause the editor to abandon all changes and return to the command prompt with the
program memory unchanged. If you have changed the text you will be asked if you really what
want to abandon your changes.
This will save the program to program memory and return to the command prompt.
This will save the program to program memory and immediately run it.
This will prompt for the text that you want to search for. When you press enter the cursor will
be placed at the start of the first entry found.
Once you have used the search function you can repeat the search by pressing SHIFT-F3.
This is described in detail below.
This will insert (at the current cursor position) the text that had been previously cut or copied
(see below).

If you pressed the mark key (F4) the editor will change to the mark mode. In this mode you can use the arrow
keys to mark a section of text which will be highlighted in reverse video. You can then delete, cut or copy the
marked text. In this mode the status line will change to show the functions of the function keys in the mark
mode. These keys are:
ESC
F4: CUT
F5: COPY
DELETE

Will exit mark mode without changing anything.
Will copy the marked text to the clipboard and remove it from the program.
Will just copy the marked text to the clipboard.
Will delete the marked text leaving the clipboard unchanged.



You can also use control keys instead of the function keys listed above. These control keystrokes are:

LEFT
HOME
DEL
F3

Ctrl-S
Ctrl-U
Ctrl-]
Ctrl-R

RIGHT
END
INSERT
ShiftF3

Ctrl-D
Ctrl-K
Ctrl-N
Ctrl-G

UP
PageUp
F1
F4

Ctrl-E
Ctrl-P
Ctrl-Q
Ctrl-T

DOWN
PageDn
F2
F5

Ctrl-X
Ctrl-L
Ctrl-W
Ctrl-Y

If you are using Tera Term, Putty, MMEdit or GFXterm as the terminal emulator it is also possible to position
the cursor by left clicking the PC's mouse in the terminal emulator's window.
The best way to learn how to use the editor is to simply fire it up and experiment.
The editor is a very productive method of writing a program. With the command EDIT you can enter your
program then, by pressing the F2 key, you can save and run the program. If your program stops with an error
pressing the function key F4 at the command prompt will run the command EDIT and place you back in the
editor with the cursor positioned at the line that caused the error. This edit/run/edit cycle is very fast.

Colour Coded Editor Display
The editor can colour code the edited program with keywords, numbers and comments displayed in different
colours. This feature can be turned on or off with the command:
OPTION COLOURCODE ON or OPTION COLOURCODE OFF
This setting requires a compatible terminal emulator like Tera Term and is saved in non-volatile memory and
automatically applied on start-up.



Program and Data Storage
The BASIC program is held in flash memory and is run from there. When a program is edited via EDIT or
loaded via the console it will be saved there. Flash memory is non-volatile so the program will not be lost if the
power is lost or the processor is reset. The maximum program size is 160KB.
In addition to this program memory there are three other locations where programs can be saved. These are
described in detail below and are Flash Slots, the Flash Filesystem and an attached SD Card

Flash Slots
There are four of these which can be used to save completely different programs or previous versions of the
program you are working on (in case you need to revert to an earlier version). In addition, MMBasic will allow
a BASIC program to load and run another program saved to a numbered flash location while retaining all the
variables and settings of the original program – this is called chaining and allows for a much larger program to
be run than the amount of program memory would normally allow.
To manage these numbered locations in flash you can use the following commands (note that in the following n
is a number from 1 to 3):
FLASH SAVE n
Save the program in the program memory to the flash location n.
FLASH LOAD n
Load a program from flash location n into the program memory.
FLASH RUN n
Run a program from flash location n, clears all variables but does not erase
or change the program held in the main program memory.
FLASH LIST
Display a list of all flash locations including the first line of the program.
FLASH LIST n [,ALL]
Lists the program held in location n. Use FLASH LIST n,ALL to list
without page breaks
FLASH ERASE n
Erase flash location n.
FLASH ERASE ALL
Erase all flash locations.
FLASH CHAIN n
Load and run a program from flash location n, leaving all variables intact.
As with FLASH RUN this command but does not erase or change the
program held in the main program memory.
FLASH OVERWRITE n
Erase flash location n and then save the program in the program memory to
that location.
FLASH DISK LOAD f$ [,O] Loads a flash slot from the binary file specified. Overwrites the slot if the
optional “O” is specified.
In addition, the command OPTION AUTORUN can be used to specify a flash program location to be set
running when power is applied or the CPU restarted. This option can also used without specifying a flash
location and in that case MMBasic will automatically load and run the program that is in the program memory.
Notes:
 It is recommended that you include a comment describing the program as the first line of the program. This
will then be displayed by the FLASH LIST command and will help identify the program.
 All BASIC programs saved to flash may be erased if you upgrade (or downgrade) the PicoMite firmware.
So make sure that you backup these first.
 The LIBRARY command uses Slot 3 for saving library data therefore only 2 slots will be available if the
library feature is used.

Flash Filesystem
This is an area of the Raspberry Pi Pico’s flash memory which is automatically created by the firmware and
will look like a normal disk drive to MMBasic. It is called drive A: and data and programs can be read/written
using the normal BASIC file commands (SAVE, RUN, OPEN, etc). In addition, sub directories can be created
and deleted and long filenames used.
For example, to run a program:
RUN "A:/MyProgram.bas"
Open a text file for random access:
OPEN "A:/data/database.dat" FOR RANDOM as #4



Nothing needs to be done to create this drive so it will always be available to the BASIC program.
The system will create and maintain the file "BOOTCOUNT" on the Flash Filesystem. This keeps a count of
the number of times the PicoMite has been restarted and can be read with the function MM.INFO(boot count).

SD Cards
An SD Card socket can be connected to the PicoMite and accessed as drive B:. Like the Flash Filesystem the
normal BASIC file commands can be used to save/load programs as well as opening data files for read/write.
Cards up to 32 GB formatted in FAT16 or FAT32 are supported and the files created can also be read/written
on personal computers running Windows, Linux or the Mac operating system. The PicoMite uses the SPI
protocol to talk to the card and this is not influenced by the card type, so all types (Class 4, 10, UHS-1 etc) are
supported
The SPI protocol needs to be specifically configured before it can be used. First the “system” SPI port needs to
be configured. This is a port that will be used for system use (SD Card, LCD display and the touch controller
on an LCD panel).
There are a number of ports and pins that can be used (see the section PicoMite Hardware) but this example
uses SPI on pins GP18, GP19 and GP16 for Clock, MOSI and MISO.

OPTION SYSTEM SPI GP18, GP19, GP16
Then MMBasic must be told that there is an SD Card attached and what pin is used for the Chip Select signal:

OPTION SDCARD GP22
These commands must be entered at the command prompt (not in a program) and will cause the PicoMite to
restart. This has the side effect of disconnecting the USB console interface which will need to be reconnected.
When the PicoMite is restarted MMBasic will automatically initialise the SD Card interface. This SPI port will
then not be available to BASIC programs (i.e. it is reserved). To verify the configuration, you can use the
command OPTION LIST to list all options that have been set including the configuration of the SD Card.
The basic circuit diagram for connecting the SD Card connector using these pin allocations is illustrated below.

PicoMite
GP22
GP19
GP18
GP16

Note that you can use many different configurations using various pin allocations – this is just an example
based on the configuration commands listed above.
Care must be taken when the SPI port is shared between a number of devices (SD Card, touch, etc). In this case all
the Chip Select signals must configured in MMBasic or alternatively disabled by a permanent connection to 3.3V.
If this is not done any floating Chip Select signal lines will cause the wrong controller to respond to commands on
the SPI bus.
Where no other devices share the SPI bus the SD Card can be set up with:
OPTION SDCARD CSpin, CLKpin, MOSIpin, MISOpin
In this case the pins can be assigned completely flexibly and do not need to be capable of SPI operation.

MMBasic Support for Flash and SD Card Filesystems
The MMBasic support for the Flash Filesystem and SD Cards is almost identical. This allows programs to use
either filesystem with minimal modification. The Flash Filesystem is referred to as drive A: while the SD Card
(when connected) is drive B:. The default drive can be set with the DRIVE command and then the drive prefix is
not needed.
In the following note that:
 On startup the active drive (ie, the default) is A: (the Flash Filesystem).







Any file path that uses the drive letter must be a full path from the root (ie, “A:/mypath/myfile.txt”).
Long file/directory names are supported in addition to the old 8.3 format.
The maximum file/path length is 63 characters.
Upper/lowercase characters and spaces are allowed. The file system on the SD Card is NOT case
sensitive however the Flash Filesystem IS case sensitive.
 Directory paths are allowed in file/directory strings. (i.e., OPEN "A:\dir1\dir2\file.txt" FOR …).
 Either forward or back slashes can be used in paths. E.g. \dir\file.txt is the same as /dir/file.txt.
 The current PicoMite time is used for file create and last access times.
 Up to ten files can be simultaneously open and they can be on both the A: drive and the B: drive.
 Except for INPUT, LINE INPUT and PRINT the # in #fnbr is optional and may be omitted.
Programs can be loaded from or saved to the Flash Filesystem and SD Cards using these commands.


LOAD fname$ [, R]
Load a BASIC program. The optional suffix ",R" will cause the program to be run after it has been loaded
(in this case fname$ must be a string constant).



RUN fname$
Load a BASIC program and run it. fname$ must be a string constant.



SAVE fname$
Save the current program to the Flash Filesystem or SD Card.

These are the basic commands for reading and writing data.


OPEN fname$ FOR mode AS #fnbr
Opens a file for reading or writing. 'fname$' is the file name in 8.3 format. 'mode' can be INPUT,
OUTPUT, APPEND or RANDOM. ‘#fnbr’ is the file number (1 to 10).



PRINT #fnbr, expression [[,; ]expression] … etc
Outputs text to the file opened as #fnbr.



INPUT #fnbr, list of variables
Read a list of comma separated data into the variables specified from the file previously opened as #fnbr.



LINE INPUT #fnbr, variable$
Read a complete line into the string variable specified from the file previously opened as #fnbr.



FLUSH #fnbr
Forces any buffered writes to be written to the Flash Filesystem or SD Card. It is recommended that this
command be used regularly where data loss could occur in the event of power loss.



CLOSE #fnbr [,#fnbr] …
Close the file(s) previously opened with the file number ‘#fnbr’.

Basic file and directory manipulation. Most can be done at the command prompt or from within a BASIC
program.


DRIVE drive$
Sets the active disk drive as ‘drive$’. ‘drive$’ can be “A:” or “B:” where A is the flash drive and B is the
SD Card (if configured).



DRIVE "A:/FORMAT"
Reformat the Flash Filesystem (drive A:) to its initial state.



FILES [wildcard]
Search the current directory and list the files/directories found. Note: Can only be used at the command
prompt, not within a program.



LIST fname$
List the contents of a program or text file on the console.





KILL fname$
Delete a file in the current directory on the current drive. See the command reference for more details on
wildcard deletes.



MKDIR dname$
Creates a sub directory in the current directory on the current drive.



CHDIR dname$
Change into to the directory $dname. $dname can also be "." (dot dot) for up one directory or "\" for the
root directory. The starting point is the current directory on the current drive.



RMDIR dir$
Remove, or delete, the directory ‘dir$’ in the current directory on the current drive.



SEEK #fnbr, pos
Will position the read/write pointer in a file that has been opened for RANDOM access to the 'pos' byte.



RENAME fromname$ AS toname$
Will rename the file fromname$ to have the name toname$ in the current directory on the current drive



COPY [mode] fromname$ TO toname$
Will copy the file fromname$ to have the file toname$. See the command reference for more details on the
optional mode and wildcard copies.

Also there are a number of functions that support the above commands.


INPUT$(nbr, #fnbr)
Will return a string composed of ‘nbr’ characters read from a file previously opened for INPUT with the
file number ‘#fnbr’. If less than ‘nbr’ characters are available the function will return with what it has
(including an empty string if no characters are available).



DIR$( fspec, type )
Will search for files and return the names of entries found.



CWD$
Will return the current working directory.



EOF( #fnbr )
Will return true if the file previously opened for INPUT with the file number ‘#fnbr’ is positioned at the
end of the file.



LOC( #fnbr )
For a file opened as RANDOM this will return the current position of the read/write pointer in the file.



LOF( #fnbr )
Will return the current length of the file in bytes.



MM.INFO(drive)
Will return the current active drive – ie, "A:" or "B:"



MM.INFO(free space)
Will return how much space is left on the active drive



MM.INFO(disk size)
Will return the size of the active drive



MM.INFO(exists file fname$)
Will return true if the file exists



MM.INFO(exists dir dirname$)
Will return true if the directory exists



XModem Transfer
In addition to the standard method of XModem transfer which copies to or from the program memory the
PicoMite can also copy to and from a file on the Flash Filesystem or SD Card. The syntax is:
XMODEM SEND filename$
or
XMODEM RECEIVE filename$
Where ‘filename$’ is the file to save or send. ‘filename$’ can be a string expression, variable or constant. If it
is a constant the string must be quoted (e.g., XMODEM SEND "prbas.bas"). In the case of receiving a file, any
file with the same name will be overwritten.

Load and Save Image
An image can be loaded from the Flash Filesystem or SD Card for display on an attached LCD display panel.
This can be used to draw a logo or add a background on the display. The syntax is:
LOAD IMAGE filename$ [, StartX, StartY]
or
LOAD JPG filename$ [, StartX, StartY]
Where ‘filename$’ is the image to load and ‘StartX’/’StartY’ are the coordinates of the top left corner of the
image (these are optional and will default to the top left corner of the display if not specified).
The image must be in the BMP format (for LOAD IMAGE) or JPG format (for LOAD JPG) and MMBasic will
add “.BMP” or “.JPG” to the file name if an extension is not specified. All types of the BMP or JPG formats
are supported including black and white and true colour 24-bit images.
The current image on a ILI9341 based LCD screen can be saved to a file using the following command:
SAVE IMAGE filename$ [,StartX, StartY, width, height]
This will save the image, or part of the image, as a 24-bit true colour BMP file (the extension .BMP) will be
added if an extension is not supplied.

Example of Sequential I/O
In the example below a file is created and two lines are written to the file (using the PRINT command). The
file is then closed.
OPEN "fox.txt" FOR OUTPUT AS #1
PRINT #1, "The quick brown fox"
PRINT #1, "jumps over the lazy dog"
CLOSE #1
You can read the contents of the file using the LINE INPUT command. For example:
OPEN "fox.txt" FOR INPUT AS #1
LINE INPUT #1,a$
LINE INPUT #1,b$
CLOSE #1
LINE INPUT reads one line at a time so the variable a$ will contain the text "The quick brown fox" and b$
will contain "jumps over the lazy dog".
Another way of reading from a file is to use the INPUT$() function. This will read a specified number of
characters. For example:
OPEN "fox.txt" FOR INPUT AS #1
ta$ = INPUT$(12, #1)
tb$ = INPUT$(3, #1)
CLOSE #1



The first INPUT$() will read 12 characters and the second three characters. So the variable ta$ will contain
"The quick br" and the variable tb$ will contain "own".
Files normally contain just text and the print command will convert numbers to text. So in the following
example the first line will contain the line "123" and the second "56789".
nbr1 = 123 : nbr2 = 56789
OPEN "numbers.txt" FOR OUTPUT AS #1
PRINT #1, nbr1
PRINT #1, nbr2
CLOSE #1
Again you can read the contents of the file using the LINE INPUT command but then you would need to
convert the text to a number using VAL().
For example:
OPEN "numbers.txt" FOR INPUT AS #1
LINE INPUT #1, a$
LINE INPUT #1, b$
CLOSE #1
x = VAL(a$) : y = VAL(b$)
Following this the variable x would have the value 123 and y the value 56789.

Random File I/O
For random access the file should be opened with the keyword RANDOM. For example:
OPEN "filename" FOR RANDOM AS #1
To seek to a record within the file you would use the SEEK command which will position the read/write
pointer to a specific byte. The first byte in a file is numbered one so, for example, the fifth record in a file that
uses 64 byte records would start at byte 257. In that case you would use the following to point to it:
SEEK #1, 257
When reading from a random access file the INPUT$() function should be used as this will read a fixed number
of bytes (i.e. a complete record) from the file. For example, to read a record of 64 bytes you would use:
dat$ = INPUT$(64, #1)
When writing to the file a fixed record size should be used and this can be easily accomplished by adding
sufficient padding characters (normally spaces) to the data to be written. For example:
PRINT #1, dat$ + SPACE$(64 – LEN(dat$);
The SPACE$() function is used to add enough spaces to ensure that the data written is an exact length (64 bytes
in this example). The semicolon at the end of the print command suppresses the addition of the carriage return
and line feed characters which would make the record longer than intended.
Two other functions can help when using random file access. The LOC() function will return the current byte
position of the read/write pointer and the LOF() function will return the total length of the file in bytes.
The following program demonstrates random file access. Using it you can append to the file (to add some data
in the first place) then read/write records using random record numbers. The first record in the file is record
number 1, the second is 2, etc.
RecLen = 64
OPEN "test.dat" FOR RANDOM AS #1
DO
abort: PRINT
PRINT "Number of records in the file =" LOF(#1)/RecLen
INPUT "Command (r = read, w = write, a = append, q = quit): ", cmd$
IF cmd$ = "q" THEN CLOSE #1 : END
IF cmd$ = "a" THEN



SEEK #1, LOF(#1) + 1
ELSE
INPUT "Record Number: ", nbr
IF nbr < 1 or nbr > LOF(#1)/RecLen THEN PRINT "Invalid record" : GOTO abort
SEEK #1, RecLen * (nbr - 1) + 1
ENDIF
IF cmd$ = "r" THEN
PRINT "The record = " INPUT$(RecLen, #1)
ELSE
LINE INPUT "Enter the data to be written: ", dat$
PRINT #1,dat$ + SPACE$(RecLen - LEN(dat$));
ENDIF
LOOP

Random access can also be used on a normal text file. For example, this will print out a file backwards:
OPEN "file.txt" FOR RANDOM AS #1
FOR i = LOF(#1) TO 1 STEP -1
SEEK #1, i
PRINT INPUT$(1, #1);
NEXT i
CLOSE #1



Variables and Expressions
In MMBasic command names, function names, labels, variable names, file names, etc are not case sensitive, so
that "Run" and "RUN" are equivalent and "dOO" and "Doo" refer to the same variable.

Variables
Variables can start with an alphabetic character or underscore and can contain any alphabetic or numeric
character, the period (.) and the underscore (_). They may be up to 31 characters long.
A variable name or a label must not be the same as a function or one of the following keywords: THEN, ELSE,
GOTO, GOSUB, TO, STEP, FOR, WHILE, UNTIL, LOAD, MOD, NOT, AND, OR, XOR, AS.
E.g. step = 5 is illegal as STEP is a keyword.
MMBasic supports three types of variables:
1. Double Precision Floating Point.
These can store a number with a decimal point and fraction (e.g. 45.386) however they will lose accuracy
when more than 14 digits of precision are used. Floating point variables are specified by adding the
suffix '!' to a variable's name (e.g. i!, nbr!, etc). They are also the default when a variable is created
without a suffix (e.g. i, nbr, etc).
2. 64-bit Signed Integer.
These can store positive or negative numbers with up to 19 decimal digits without losing accuracy but
they cannot store fractions (i.e. the part following the decimal point). These are specified by adding the
suffix '%' to a variable's name. For example, i%, nbr%, etc.
3. A String.
A string will store a sequence of characters (e.g. "Tom"). Each character in the string is stored as an
eight bit number and can therefore have a decimal value of 0 to 255. String variable names are
terminated with a '$' symbol (e.g. name$, s$, etc). Strings can be up to 255 characters long.
Note that it is illegal to use the same variable name with different types. E.g. using nbr! and nbr% in the
same program would cause an error.
Most programs use floating point variables for arithmetic as these can deal with the numbers used in typical
situations and are more intuitive than integers when dealing with division and fractions. So, if you are not
bothered with the details, always use floating point.

Constants
Numeric constants may begin with a numeric digit (0-9) for a decimal constant, &H for a hexadecimal
constant, &O for an octal constant or &B for a binary constant. For example &B1000 is the same as the
decimal constant 8. Constants that start with &H, &O or &B are always treated as 64-bit unsigned integer
constants.
Decimal constants may be preceded with a minus (-) or plus (+) and may be terminated with 'E' followed by an
exponent number to denote exponential notation. For example 1.6E+4 is the same as 16000.
When a constant number is used it will be assumed that it is an integer if a decimal point or exponent is not
used. For example, 1234 will be interpreted as an integer while 1234.0 will be interpreted as a floating point
number.
String constants must be surrounded by double quote marks ("). E.g. "Hello World".

OPTION DEFAULT
A variable can be used without a suffix (i.e. !, % or $) and in that case MMBasic will use the default type of
floating point. For example, the following will create a floating point variable:
Nbr = 1234
However. the default can be changed with the OPTION DEFAULT command. For example, OPTION
DEFAULT INTEGER will specify that all variables without a specific type will be integer. So, the following
will create an integer variable:
OPTION DEFAULT INTEGER
Nbr = 1234



The default can be set to FLOAT (which is the default when a program is run), INTEGER, STRING or NONE.
In the latter all variables must be specifically typed otherwise an error will occur.
The OPTION DEFAULT command can be placed anywhere in the program and changed at any time but good
practice dictates that if it is used it should be placed at the start of the program and left unchanged.

OPTION EXPLICIT
By default MMBasic will automatically create a variable when it is first referenced. So, Nbr = 1234 will
create the variable and set it to the number 1234 at the same time. This is convenient for short and quick
programs but it can lead to subtle and difficult to find bugs in large programs. For example, in the third line of
this fragment the variable Nbr has been misspelt as Nbrs. As a consequence the variable Nbrs would be
created with a value of zero and the value of Total would be wrong.
Nbr = 1234
Incr = 2
Total = Nbrs + Incr
The OPTION EXPLICIT command tells MMBasic to not automatically create variables. Instead they must be
explicitly defined using the DIM, LOCAL or STATIC commands (see below) before they are used. The use of
this command is recommended to support good programming practice. If it is used it should be placed at the
start of the program before any variables are used.

DIM and LOCAL
The DIM and LOCAL commands can be used to define a variable and set its type and are mandatory when the
OPTION EXPLICIT command is used.
The DIM command will create a global variable that can be seen and used throughout the program including
inside subroutines and functions. However, if you require the definition to be visible only within a subroutine
or function, you should use the LOCAL command at the start of the subroutine or function. LOCAL has
exactly the same syntax as DIM.
If LOCAL is used to specify a variable with the same name as a global variable then the global variable will be
hidden to the subroutine or function and any references to the variable will only refer to the variable defined by
the LOCAL command. Any variable created by LOCAL will vanish when the program leaves the subroutine.
At its simplest level DIM and LOCAL can be used to define one or more variables based on their type suffix or
the OPTION DEFAULT in force at the time. For example:
DIM nbr%, s$
But it can also be used to define one or more variables with a specific type when the type suffix is not used:
DIM INTEGER nbr, nbr2, nbr3, etc
In this case nbr, nbr2, nbr3, etc are all created as integers. When you use the variable within a program you do
not need to specify the type suffix. For example, MyStr in the following works perfectly as a string variable:
DIM STRING MyStr
MyStr = "Hello"
The DIM and LOCAL commands will also accept the Microsoft practice of specifying the variable's type after
the variable with the keyword "AS". For example:
DIM nbr AS INTEGER, s AS STRING
In this case the type of each variable is set individually (not as a group as when the type is placed before the list
of variables).
The variables can also be initialised while being defined. For example:
DIM INTEGER a = 5, b = 4, c = 3
DIM s$ = "World", i% = &H8FF8F
DIM msg AS STRING = "Hello" + " " + s$
The value used to initialise the variable can be an expression including user defined functions.
The DIM or LOCAL commands are also used to define an array and all the rules listed above apply when
defining an array. For example, you can use:
DIM INTEGER nbr(10), nbr2, nbr3(5,8)



When initialising an array the values are listed as comma separated values with the whole list surrounded by
brackets. For example:
DIM INTEGER nbr(5) = (11, 12, 13, 14, 15, 16)
or
DIM days(7) AS STRING = ("","Sun","Mon","Tue","Wed","Thu","Fri","Sat")

STATIC
Inside a subroutine or function it is sometimes useful to create a variable which is only visible within the
subroutine or function (like a LOCAL variable) but retains its value between calls to the subroutine or function.
You can do this by using the STATIC command. STATIC can only be used inside a subroutine or function and
uses the same syntax as LOCAL and DIM. The difference is that its value will be retained between calls to the
subroutine or function (i.e. it will not be initialised on the second and subsequent calls).
For example, if you had the following subroutine and repeatedly called it, the first call would print 5, the
second 6, the third 7 and so on.
SUB Foo
STATIC var = 5
PRINT var
var = var + 1
END SUB
Note that the initialisation of the static variable to 5 (as in the above example) will only take effect on the first
call to the subroutine. On subsequent calls the initialisation will be ignored as the variable had already been
created on the first call.
As with DIM and LOCAL the variables created with STATIC can be float, integers or strings and arrays of
these with or without initialisation. The length of the variable name created by STATIC and the length of the
subroutine or function name added together cannot exceed 31 characters.

CONST
Often it is useful to define an identifier that represents a value without the risk of the value being accidently
changed - which can happen if variables were used for this purpose (this practice encourages another class of
difficult to find bugs).
Using the CONST command you can create an identifier that acts like a variable but is set to a value that cannot
be changed. For example:
CONST InputVoltagePin = 31
CONST MaxValue = 2.4
The identifiers can then be used in a program where they make more sense to the casual reader than simple
numbers. For example:
IF PIN(InputVoltagePin) > MaxValue THEN SoundAlarm
A number of constants can be created on the one line:
CONST InputVoltagePin = 31, MaxValue = 2.4, MinValue = 1.5
The value used to initialise the constant is evaluated when the constant is created and can be an expression
including user defined functions.
The type of the constant is derived from the value assigned to it; so for example, MaxValue above will be a
floating point constant because 2.4 is a floating point number. The type of a constant can also be explicitly set
by using a type suffix (i.e. !, % or $) but it must agree with its assigned value.

Special Characters in Strings
Special, non-printable characters can be inserted in string constants using the backslash (ie, \) as an escape
symbol. To enable this facility the command OPTION ESCAPE must be placed at the start of the program.
These are the valid escape sequences:
Hex Value
\a
\b
\e


07
08
1B

Description
Alert (Beep, Bell)
Backspace
Escape character


\f
\n
\r
\q
\t
\v
\\
\nnn
\&hh

0C
0A
0D
22
09
0B
5C
any
any

Formfeed Page Break
Newline (Line Feed)
Carriage Return
Quote symbol
Horizontal Tab
Vertical Tab
Backslash
The byte whose value is given by nnn interpreted as a decimal number
The byte whose value is given by hh… interpreted as a hexadecimal number

For example, the following will print the words Hello and World on separate lines:
OPTION ESCAPE
PRINT "Hello\r\nWorld"

Expressions and Operators
MMBasic will evaluate a mathematical expression using the standard mathematical rules. For example,
multiplication and division are performed first followed by addition and subtraction. These are called the rules
of precedence and are detailed below.
This means that 2 + 3 * 6 will resolve to 20, so will 5 * 4 and also 10 + 4 * 3 – 2.
If you want to force the interpreter to evaluate parts of the expression first you can surround that part of the
expression with brackets. For example, (10 + 4) * (3 – 2) will resolve to 14 not 20 as would have been the case
if the brackets were not used. Using brackets does not appreciably slow down the program so you should use
them liberally if there is a chance that MMBasic will misinterpret your intention.
The following operators, in order of precedence, are implemented in MMBasic. Operators that are on the same
level (for example + and -) are processed with a left to right precedence as they occur on the program line.
Arithmetic operators:
Exponentiation (e.g. b^n means bn)

^
*

/ \ MOD

+ -

Multiplication, division, integer division and modulus (remainder)
Addition and subtraction

Shift operators:
x << y

x >> y

These operate in a special way. << means that the value returned
will be the value of x shifted by y bits to the left while >> means the
same only right shifted. They are integer functions and any bits
shifted off are discarded and any bits introduced are set to zero.

Logical operators:
NOT INV

invert the logical value on the right (e.g. NOT a=b is a<>b)
or bitwise inversion of the value on the right (e.g. a = INV b)

<>
>=

Inequality, less than, greater than, less than or equal to, less than or
equal to (alternative version), greater than or equal to, greater than or
equal to (alternative version)

< > <= =<
=>

=
AND

equality
OR

XOR

Conjunction, disjunction, exclusive or

For Microsoft compatibility the operators AND, OR and XOR are integer bitwise operators. For example,
PRINT (3 AND 6) will output the number 2. Because these operators can act as both logical operators (for
example, IF a=5 AND b=8 THEN …) and as bitwise operators (e.g. y% = x% AND &B1010) the interpreter
will be confused if they are mixed in the same expression. So, always evaluate logical and bitwise expressions
in separate expressions.
The other logical operations result in the integer 0 (zero) for false and 1 for true. For example the statement
PRINT 4 >= 5 will print the number zero on the output and the expression A = 3 > 2 will store +1 in A.


The NOT operator will invert the logical value on its right (it is not a bitwise invert) while the INV operator
will perform a bitwise invert. Both of these have the highest precedence so they will bind tightly to the next
value. For normal use of NOT or INV the expression to be operated on should be placed in brackets. Eg:
IF NOT (A = 3 OR A = 8) THEN …
String operators:
+
<>
>=

Join two strings
< > <= =<
=>

=

Inequality, less than, greater than, less than or equal to, less than or
equal to (alternative version), greater than or equal to, greater than or
equal to (alternative version)
Equality

String comparisons respect case. For example "A" is greater than "a".

Mixing Floating Point and Integers
MMBasic automatically handles conversion of numbers between floating point and integers. If an operation
mixes both floating point and integers (e.g. PRINT A% + B!) the integer will be converted to a floating point
number first, then the operation performed and a floating point number returned. If both sides of the operator
are integers then an integer operation will be performed and an integer returned.
The one exception is the normal division ("/") which will always convert both sides of the expression to a
floating point number and then returns a floating point number. For integer division you should use the integer
division operator "\".
MMBasic functions will return a float or integer depending on their characteristics. For example, PIN() will
return an integer when the pin is configured as a digital input but a float when configured as an analog input.
If necessary you can convert a float to an integer with the INT() function. It is not necessary to specifically
convert an integer to a float but if it was needed the integer value could be assigned to a floating point variable
and it will be automatically converted in the assignment.

64-bit Unsigned Integers
MMBasic on the PicoMite supports 64-bit signed integers. This means that there are 63 bits for holding the
number and one bit (the most significant bit) which is used to indicate the sign (positive or negative). However
it is possible to use full 64-bit unsigned numbers as long as you do not do any arithmetic on the numbers.
64-bit unsigned numbers can be created using the &H, &O or &B prefixes to a number and these numbers can
be stored in an integer variable. You then have a limited range of operations that you can perform on these.
They are << (shift left), >> (shift right), AND (bitwise and), OR (bitwise or), XOR (bitwise exclusive or), INV
(bitwise inversion), = (equal to) and <> (not equal to). Arithmetic operators such as division or addition may
be confused by a 64-bit unsigned number and could return nonsense results.
To display 64-bit unsigned numbers you should use the HEX$(), OCT$() or BIN$() functions.
For example, the following 64-bit unsigned operation will return the expected results:
X% = &HFFFF0000FFFF0044
Y% = &H800FFFFFFFFFFFFF
X% = X% AND Y%
PRINT HEX$(X%, 16)
Will display "800F0000FFFF0044"



Subroutines and Functions
A program defined subroutine or function is simply a block of programming code that is contained within a
module and can be called from anywhere within your program. It is the same as if you have added your own
command or function to the language.

Subroutines
A subroutine acts like a command and it can have arguments (sometimes called a parameter list). In the
definition of the subroutine they look like this:
SUB MYSUB arg1, arg2$, arg3
<statements>
<statements>
END SUB
And when you call the subroutine you can assign values to the arguments. For example:
MYSUB 23, "Cat", 55
Inside the subroutine arg1 will have the value 23, arg2$ the value of "Cat", and so on. The arguments act
like ordinary variables but they exist only within the subroutine and will vanish when the subroutine ends. You
can have variables with the same name in the main program and they will be hidden by the arguments defined
for the subroutine.
When calling a subroutine you can supply less than the required number of values and in that case the missing
values will be assumed to be either zero or an empty string. You can also leave out a value in the middle of the
list and the same will happen. For example:
MYSUB

23, , 55

Will result in arg2$ being set to the empty string "".
Rather than using the type suffix (e.g. the $ in arg2$) you can use the suffix AS <type> in the definition of the
subroutine argument and then the argument will be known as the specified type, even when the suffix is not
used. For example:
SUB MYSUB arg1, arg2 AS STRING, arg3
IF arg2 = "Cat" THEN …
END SUB
Inside a subroutine you can define a variable using LOCAL (which has the same syntax as DIM). This variable
will only exist within the subroutine and will vanish when the subroutine exits.

Functions
Functions are similar to subroutines with the main difference being that the function is used to return a value in
an expression. The rules for the argument list in a function are similar to subroutines. The only difference is
that brackets are required around the argument list when you are calling a function, even if there are no
arguments (they are optional when calling a subroutine).
To return a value from the function you assign a value to the function's name within the function. If the
function's name is terminated with a $, a % or a ! the function will return that type, otherwise it will return
whatever the OPTION DEFAULT is set to. You can also specify the type of the function by adding AS <type>
to the end of the function definition.
For example:
FUNCTION Fahrenheit(C) AS FLOAT
Fahrenheit = C * 1.8 + 32
END FUNCTION

Passing Arguments by Reference
If you use an ordinary variable (i.e., not an expression) as the value when calling a subroutine or a function, the
argument within the subroutine/function will point back to the variable used in the call and any changes to the
argument will also be made to the supplied variable. This is called passing arguments by reference.



For example, you might define a subroutine to swap two values, as follows:
SUB Swap a, b
LOCAL t
t = a
a = b
b = t
END SUB
In your calling program you would use variables for both arguments:
Swap nbr1, nbr2
And the result will be that the values of nbr1 and nbr2 will be swapped.
For this to work the type of the variable passed (e.g. nbr1) and the defined argument (e.g. a) must be the same
(in the above example both default to float).
Unless you need to return a value via the argument you should not use an argument as a general purpose
variable inside a subroutine or function. This is because another user of your routine may unwittingly use a
variable in their call and that variable could be "magically" changed by your routine. It is much safer to assign
the argument to a local variable and manipulate that instead.

Passing Arrays
Single elements of an array can be passed to a subroutine or function and they will be treated the same as a
normal variable. For example, this is a valid way of calling the Swap subroutine (discussed above):
Swap dat(i), dat(i + 1)
This type of construct is often used in sorting arrays.
You can also pass one or more complete arrays to a subroutine or function by specifying the array with empty
brackets instead of the normal dimensions. For example, a(). In the subroutine or function definition the
associated parameter must also be specified with empty brackets. The type (i.e., float, integer or string) of the
argument supplied and the parameter in the definition must be the same.
In the subroutine or function the array will inherit the dimensions of the array passed and these must be
respected when indexing into the array. If required the dimensions of the array could be passed as additional
arguments to the subroutine or function so it could correctly manipulate the array. The array is passed by
reference which means that any changes made to the array within the subroutine or function will also apply to
the supplied array.
For example, when the following is run the words "Hello World" will be printed out:
DIM MyStr$(5, 5)
MyStr$(4, 4) = "Hello" : MyStr$(4, 5) = "World"
Concat MyStr$()
PRINT MyStr$(0, 0)
SUB Concat arg$()
arg$(0,0) = arg$(4, 4) + " " + arg$(4, 5)
END SUB

Early Exit
There can be only one END SUB or END FUNCTION for each definition of a subroutine or function. To exit
early from a subroutine (i.e., before the END SUB command has been reached) you can use the EXIT SUB
command. This has the same effect as if the program reached the END SUB statement. Similarly you can use
EXIT FUNCTION to exit early from a function.

Recursion
Recursion is where a subroutine or function calls itself. You can do recursion in MMBasic but there are a
number of issues (these are a direct consequence of the limitations of microcontrollers and the BASIC
language):
 There is a fixed limit to the depth of recursion. In the PicoMite this is 50 levels.
 If you have many arguments to the subroutine or function and many LOCAL variables (especially strings)
you could easily run out of memory before reaching the 50 level limit.
 Any FOR…NEXT loops and DO…LOOPs will be corrupted if the subroutine or function is recursively
called from within these loops.



Examples
There is often the need for a special command or function to be implemented in MMBasic but in many cases
these can be constructed using an ordinary subroutine or function which will then act exactly the same as a built
in command or function.
For example, sometimes there is a requirement for a TRIM function which will trim specified characters from
the start and end of a string. The following provides an example of how to construct such a simple function in
MMBasic.
The first argument to the function is the string to be trimmed and the second is a string containing the
characters to trim from the first string. RTrim$() will trim the specified characters from the end of the string,
LTrim$() from the beginning and Trim$() from both ends.
' trim any characters in c$ from the start and end of s$
Function Trim$(s$, c$)
Trim$ = RTrim$(LTrim$(s$, c$), c$)
End Function
' trim any characters in c$ from the end of s$
Function RTrim$(s$, c$)
RTrim$ = s$
Do While Instr(c$, Right$(RTrim$, 1))
RTrim$ = Mid$(RTrim$, 1, Len(RTrim$) - 1)
Loop
End Function
' trim any characters in c$ from the start of s$
Function LTrim$(s$, c$)
LTrim$ = s$
Do While Instr(c$, Left$(LTrim$, 1))
LTrim$ = Mid$(LTrim$, 2)
Loop
End Function
As an example of using these functions:
S$ = "
****23.56700
PRINT Trim$(s$, " ")

"

Will give "****23.56700"
PRINT Trim$(s$, " *0")
Will give "23.567"
PRINT LTrim$(s$, " *0")
Will give "23.56700"



Using the I/O pins
The Raspberry Pi Pico has 26 input/output pins which can be controlled from within the BASIC program with 3
of these supporting a high speed ADC (Analog to Digital Converter).
An I/O pin is referred to by its pin number and this can be the number (e.g., 2) or its GP number (e.g., GP1).

Digital Inputs
A digital input is the simplest type of input configuration. If the input voltage is higher than 2.5V the logic
level will be true (numeric value of 1) and anything below 0.65V will be false (numeric value of 0). The inputs
use a Schmitt trigger input so anything in between these levels will retain the previous logic level. All pins are
limited to a maximum voltage of 3.6V. This means that resistor divider will be required if they are used with
input voltages greater than that.
In your BASIC program you would set the input as a digital input and use the PIN() function to get its level.
For example:
SETPIN GP4, DIN
IF PIN(GP4) = 1 THEN PRINT "High"
The SETPIN command configures pin GP4 as a digital input and the PIN() function will return the value of that
pin (the number 1 if the pin is high). The IF command will then execute the command after the THEN
statement if the input was high. If the input pin was low the program would just continue with the next line in
the program.
The SETPIN command also recognises a couple of options that will connect an internal resistor from the input
to either the supply or ground. This is called a "pullup" or "pulldown" resistor and is handy when connecting to
a switch as it saves having to install an external resistor to place a voltage across the contacts.

Analog Inputs
Pins marked as ADC can be configured to measure the voltage on the pin. The input range is from zero to 3.3V
and the PIN() function will return the voltage. For example:
> SETPIN 31, AIN
> PRINT PIN(31)
2.345
>
You will need a voltage divider if you want to measure voltages greater than 3.3V. For small voltages you may
need an amplifier to bring the input voltage into a reasonable range for measurement.
The measurement uses 3.3V power supply to the CPU as its reference and it is assumed that this is exactly
3.3V. This value can be changed with the OPTION command.
The ADC commands provide an alternate method of recording analog inputs and are intended for high speed
recording of many readings into an array.

Counting Inputs
Any four pins can be used as counting inputs to measure frequency, period or just count pulses on the input.
The pins used for this function can be configured using the OPTION COUNT command but, if not changed,
will default to GP6, GP7, GP8 and GP9.
As an example, the following will print the frequency of the signal on pin GP7:
> SETPIN GP7, FIN
> PRINT PIN(GP7)
110374
>
In this case the frequency is 110.374 kHz.
By default the gate time is one second which is the length of time that MMBasic will use to count the number
of cycles on the input and this means that the reading is updated once a second with a resolution of 1 Hz. By
specifying a third argument to the SETPIN command it is possible to specify an alternative gate time between
10 ms and 100000 ms. Shorter times will result in the readings being updated more frequently but the value


returned will have a lower resolution. The PIN() function will always scale the returned number as the
frequency in Hz regardless of the gate time used.
For example, the following will set the gate time to 10ms with a corresponding loss of resolution:
> SETPIN GP7, FIN, 10
> PRINT PIN(GP7)
110300
>
For accurate measurement of signals less than 10 Hz it is generally better to measure the period of the signal.
When set to this mode the PicoMite will measure the number of milliseconds between sequential rising edges
of the input signal. The value is updated on the low to high transition so if your signal has a period of (say) 100
seconds you should be prepared to wait that amount of time before the PIN() function will return an updated
value.
The count pins can also count the number of pulses on their input. When a pin is configured as a counter (for
example, SETPIN 7,CIN) the counter will be reset to zero and PicoMite will then count every transition from
a low to high voltage. The counter can be reset to zero again by executing PIN(7) = 0.
Counting inputs are accurate up to about 200KHz at the default processor frequency. A minimum pulse width
of about 40nS is needed to trigger the counter

Digital Outputs
All I/O pins can be configured as a digital output using the DOUT parameter to the SETPIN command. For
example:
SETPIN GP15, DOUT
This means that when an output pin is set to logic low it will pull its output to zero and when set high it will
pull its output to 3.3V. In MMBasic this is done with the PIN command. For example PIN(GP15) = 0
will set pin GP15 to low while PIN(GP15) = 1 will set it high.

Pulse Width Modulation
The PWM (Pulse Width Modulation) command allows the PicoMite to generate square waves with a program
controlled duty cycle. By varying the duty cycle you can generate a program controlled voltage output for use
in controlling external devices that require an analog input (power supplies, motor controllers, etc). The PWM
outputs are also useful for driving servos and for generating a sound output via a small transducer.
The PWM outputs consists of up to 8 channels (numbered 0 to 7) with each channel having two outputs (A and
B). For each channel the frequency can be selected and for each output a different duty cycle can be set.
Up to 16 pins can be configured as PWM outputs using the SETPIN command.

Communications Interfaces (Serial, SPI and I2C)
These are described in the appendices at the rear of this manual. Before these interfaces can be used the pins
that are to be used for the relevant signals must be configured using the SETPIN command.
Some devices such as an SD Card, LCD panels, touch, etc also use SPI or I2C interfaces and the pins used for
these must similarly be configured using the OPTION SYSTEM command before they can be used.

Interrupts
Interrupts are a handy way of dealing with an event that can occur at an unpredictable time. An example is
when the user presses a button. In your program you could insert code after each statement to check to see if
the button has been pressed but an interrupt makes for a cleaner and more readable program.
When an interrupt occurs MMBasic will execute a special subroutine and when finished return to the main
program. The main program is completely unaware of the interrupt and will carry on as normal.
Any I/O pin that can be used as a digital input can be configured to generate an interrupt using the SETPIN
command with up to ten interrupts active at any one time. Interrupts can be set up to occur on a rising or falling
digital input signal (or both) and will cause an immediate branch to the specified user defined subroutine. The
target can be the same or different for each interrupt. Return from an interrupt is via the END SUB or EXIT
SUB commands. Note that no parameters can be passed to the subroutine however within the interrupt calls to
other subroutines and functions are allowed.



If two or more interrupts occur at the same time they will be processed in order of the interrupts as defined
below. During the processing of an interrupt all other interrupts are disabled until the interrupt subroutine
returns. During an interrupt (and at all times) the value of the interrupt pin can be accessed using the PIN()
function.
Interrupts can occur at any time but they are disabled during INPUT statements. Also interrupts are not
recognised during some long hardware related operations (e.g. the TEMPR() function, LCD drawing
commands, and SD access commands) although they will be recognised if they are still present when the
operation has finished. When using interrupts the main program is completely unaffected by the interrupt
activity unless a variable used by the main program is changed during the interrupt.
Because interrupts run in the background they can cause difficult to diagnose bugs. Keep in mind the following
factors when using interrupts:
 Interrupts are only checked by MMBasic at the completion of each command, and they are not latched by
the hardware. This means that an interrupt that lasts for a short time can be missed, especially when the
program is executing commands that take some time to execute. Most commands will execute in under
15µs however some commands such as the TEMPR() function can take up to 200ms so it is possible for
an interrupt to occur and vanish within this window and thus not be recognised.


When inside an interrupt all other interrupts are blocked so your interrupts should be short and exit as
soon as possible. For example, never use PAUSE inside an interrupt. If you have some lengthy
processing to do you should simply set a flag and immediately exit the interrupt, then your main program
loop can detect the flag and do whatever is required.



The subroutine that the interrupt calls (and any other subroutines or functions called by it) should always
be exclusive to the interrupt. If you must call a subroutine that is also used by an interrupt you must
disable the interrupt first (you can reinstate it after you have finished with the subroutine).



Remember to disable an interrupt when you have finished needing it – background interrupts can cause
strange and non-intuitive bugs.

In addition to interrupts generated by the change in state of an I/O pin, an interrupt can also be generated by
other sections of MMBasic including timers and communications ports and the above notes also apply to them.
The list of all these interrupts (in high to low priority ranking) is:
1. ON KEY individual
2. ON KEY general
3. PIO RX FIFO
4. PIO TX FIFO
5. PIO RX DMA completion
6. PIO TX DMA completion
7. GUI Int Down
8. GUI Int Up
9. ADC completion
10. I2C Slave Rx
11. I2C Slave Tx
12. I2C2 Slave Rx
13. I2C2 Slave Tx
14. WAV Finished
15. COM1: Serial Port
16. COM2: Serial Port
17. IR Receive
18. Keypad
19. Interrupt command/CSub Interrupt
20. I/O Pin Interrupts in order of definition
21. Tick Interrupts (1 to 4 in that order)
As an example: If an ON KEY interrupt occurred at the same time as a COM1: interrupt the ON KEY interrupt
subroutine would be executed first and then, when the interrupt subroutine finished, the COM1: interrupt
subroutine would then be executed.


Sound Output
The PicoMite can play stereo FLAC, MOD, or WAV files located on the Flash Filesystem or SD Card or
generate precise sine waves using the PLAY command. Note that the switching power regulator on the
Raspberry Pi Pico will cause some interference with the output. This can be reduced by disabling the regulator
and powering the module via an external linear regulator

Allocating the Output Pins
The audio is created using PWM outputs so before the PLAY commands can be used the PWM output pins to
be used must be allocated as audio outputs follows :
This is done using the OPTION AUDIO command as follows:
OPTION AUDIO PWM-A-PIN, PWM-B-PIN
This command should be entered at the command prompt and will be saved, so it only needs to be run once.
Both pins must be on the same PWM channel with PWM-A the left audio channel and PWM-B the right.
For example:
OPTION AUDIO GP0, GP1
The audio output can also be generated through a connected MCP48n2 DAC (e.g. MCP4822) in which case it
is configured using the command
OPTION AUDIO SPI CS-PIN, CLK-PIN, MOSI-PIN
In this case there is no requirement for a complex low pass filter and a 120ohm resistor connected to the DAC
output and with the other end of the resistor connected to GND via a 100nF capacitor will be more than
adequate. When a MCP4822 is used the LDAC pin on the DAC should be connected to GND.
In addition, the audio output can be generated using a VS1053 CODEC module which is configured using the
command
OPTION AUDIO VS1053 CLKpin, MOSIpin, MISOpin, XCSpin, XDCSpin, DREQpin, XRSTpin

This requires no output filtering and can drive 32ohm headphones direct. It also supports additional playback
capabilities.

Low Pass Filter
The audio signal is superimposed on a square wave as a pulse width modulated (PWM) signal. This means that
a low pass filter, as shown below, is required to recover the audio signal. This circuit is intended to drive an
amplifier (not headphones or speakers) and relies on capacitor coupling into the following amplifier (most have
this) and has an output level of about 1V peak to peak (650mV RMS).
Stereo
Output

4.7mH

Left
Right
Common

PWM-A Pin
220Ω

2.7nF

PicoMite
Outputs

4.7mH
220Ω

PWM-B Pin
2.7nF
33nF


33nF

68nF

68nF


Playing WAV FLAC and MOD Files
The PLAY command will play an audio file residing on the Flash Filesystem or SD Card to the sound output.
It can be used to provide background music, add sound effects to programs and provide informative
announcements.
The commands are:
PLAY WAV file$, interrupt
PLAY FLAC file$, interrupt
PLAY MODFILE file$, interrupt
file$ is the name of the audio file to play. It must be on the Flash Filesystem or SD Card and the appropriate
extension (eg .WAV) will be appended if missing. The audio will play in the background (ie, the program will
continue without pause). interrupt is optional and is the name of a subroutine which will be called when the
file has finished playing.

VS1053 support
If a VS1053 codec is used as the audio output device, additional commands are available:
PLAY MP3 file$, interrupt
PLAY MIDIFILE file$, interrupt
PLAY MIDI
PLAY MIDI CMD cmd%, data1% [,data2%]
PLAY NOTE ON channel, note, velocity
PLAY NOTE OFF channel, note [,velocity]
PLAY HALT
PLAY CONTINUE track$
PLAY STREAM buffer%(), readpointer%, writepointer%
These are explained in more detail in the commands listing section.

Generating Sine Waves
The PLAY TONE command uses the audio output to generate sine waves with selectable frequencies for the
left and right channels. This feature is intended for generating attention catching sounds but, because the
frequency is very accurate, it can be used for many other applications. For example, signalling DTMF tones
down a telephone line or testing the frequency response of loudspeakers.
The syntax of the command is:
PLAY TONE left, right, duration, interrupt
left and right are the frequencies in Hz to use for the left and right channels. The tone plays in the background
(the program will continue running after this command) and 'dur' specifies the number of milliseconds that the
tone will sound for.
duration is optional and if not specified the tone will continue until explicitly stopped or the program
terminates. interrupt (if specified) will be triggered when the duration has finished.
The frequency can be from 1 Hz to 20 KHz and is very accurate (it is based on a crystal oscillator). The
frequency can be changed at any time by issuing a new PLAY TONE command. Note that the sine wave is
generated by stepping through a lookup table so to reduce the distortion the audio output should be passed
through a low pass filter.

Specialised Audio Output
The PLAY SOUND command will generate an output based on a mixture of sine, square, etc waveforms. See
the details in the command listing.

Using PLAY
It is important to realise that the PLAY command will generate the audio in the background. This allows a
program (for example) to play the sound of a bell while continuing with its control function. Without the
background facility the whole BASIC program would freeze while the sound was heard.
However, generating the audio in the background has some subtle inferences which can trip up newcomers.
For example, take the following program:
PLAY TONE 500, 500, 2000
END


You may expect the 500Hz tone to sound for 2 seconds but in practice it will not make any sound at all. This is
because MMBasic will execute the PLAY TONE command (which will start generating the sound in the
background) and then it will immediately execute the END command which will terminate the program and the
background sound. This will happen so fast that nothing is heard.
Similarly the following program will not work either:
PLAY TONE 500, 500, 2000
PLAY TONE 300, 300, 5000
This is because the first command will set a 500Hz the tone playing but then the second PLAY command will
immediately replace that with a 300Hz tone and following that the program will run off the end terminating the
program (and the background audio), resulting in nothing being heard.
If you want MMBasic to wait while the PLAY command is doing its thing you should use suitable PAUSE
commands. For example:
PLAY TONE 500, 500
PAUSE 2000
PLAY TONE 300, 300
PAUSE 5000
PLAY STOP
This applies to all versions of the PLAY command including PLAY WAV.

Utility Commands
There are a number of commands that can be used to manage the sound output:
PLAY PAUSE
Temporarily halt (pause) the currently playing file or tone.
PLAY RESUME
Resume playing a file or tone that was previously paused.
PLAY NEXT
Play the next WAV or FLAC file in a directory
PLAY PREVIOUS
PLAY STOP
PLAY VOLUME L, R


Play the previous WAV or FLAC file in a directory
Terminate the playing of the file or tone. The sound output will also be
automatically stopped when the program ends.
Set the volume to between 0 and 100 with 100 being the maximum volume. The
volume will reset to the maximum level when a program is run. A logarithmic
scale is used so that PLAY VOLUME 50,50 should sound half as loud as 100,100.


Special Device Support
To make it easier for a program to interact with the external world the PicoMite includes drivers for a number
of common peripheral devices.
These are:








Infrared remote control receiver and transmitter
The DS18B20 temperature sensor and DHT22 temperature/humidity sensor
LCD display modules
Numeric keypads
Battery backed clock
Ultrasonic distance sensor
WS2812 RGB LEDs



PS2 Keyboard

Infrared Remote Control Decoder
You can easily add a remote control to your project using the IR command. When enabled this function will
run in the background and interrupt the running program whenever a key is pressed on the IR remote control.
It will work with any NEC or Sony compatible remote
controls including ones that generate extended
IR Receiver
messages. Most cheap programmable remote controls
will generate either protocol and using one of these you
3.3V
can add a sophisticated flair to your PicoMite based
project. The NEC protocol is also used by many other
PicoMite
manufacturers including Apple, Pioneer, Sanyo, Akai
and Toshiba so their branded remotes can be used.
To detect the IR signal you need an IR receiver. NEC
remotes use a 38kHz modulation of the IR signal and
suitable receivers tuned to this frequency include the
Vishay TSOP4838, Jaycar ZD1952 and Altronics Z1611A. Note that the I/O pins on the PicoMite are only
3.3V tolerant and so the receiver must be powered by a maximum of 3.3V.
Sony remotes use a 40 kHz modulation but receivers for this frequency can be hard to find. Generally 38 kHz
receivers will work but maximum sensitivity will be achieved with a 40 kHz receiver.
The IR receiver can be connected to any pin on the PicoMite. This pin must be configured by the program
using the command:
SETPIN n, IR
where n is the I/O pin to use for this function.
To setup the decoder you use the command:
IR dev, key, interrupt
Where dev is a variable that will be updated with the device code and key is the variable to be updated with the
key code. Interrupt is the interrupt subroutine to call when a new key press has been detected. The IR
decoding is done in the background and the program will continue after this command without interruption.
This is an example of using the IR decoder connected to the GP6 pin:
SETPIN GP6, IR
' define the pin to be used
DIM INTEGER DevCode, KeyCode
' variables used by the decoder
IR DevCode, KeyCode, IRInt
' start the IR decoder
DO
' < body of the program >
LOOP
SUB IRInt
PRINT "Received
END SUB


' a key press has been detected
device = " DevCode " key = " KeyCode


IR remote controls can address many different devices (VCR, TV, etc) so the program would normally examine
the device code first to determine if the signal was intended for the program and, if it was, then take action
based on the key pressed. There are many different devices and key codes so the best method of determining
what codes your remote generates is to use the above program to discover the codes.

Infrared Remote Control Transmitter
Using the IR SEND command you can transmit a 12 bit Sony
infrared remote control signal. This is intended for PicoMite to
PicoMite or Micromite communications but it will also work with
Sony equipment that uses 12 bit codes. Note that all Sony
products require that the message be sent three times with a 26 ms
delay between each message.
The circuit on the right illustrates what is required. The transistor
is used to drive the infrared LED because the output capability of
the PicoMite is limited. This circuit provides about 50 mA to the
LED.
To send a signal you use the command:
IR SEND pin, dev, key

+5V

58 ohms

IR
LED

PicoMite

BC338
1K

Where pin is the I/O pin used, dev is the device code to send and key is the key code. Any I/O pin on the
PicoMite can be used and you do not have to set it up beforehand (IR SEND will automatically do that).
The modulation frequency used is 38 kHz and this matches the common IR receivers (described in the previous
page) for maximum sensitivity when communicating between two PicoMites or with a Micromite.

Measuring Temperature
The TEMPR() function will get the temperature from a DS18B20
3.3V
temperature sensor. This device can be purchased on eBay for about $5
4.7K
in a variety of packages including a waterproof probe version.
The DS18B20 can be powered separately by a 3.3V supply or it can
Any
PicoMite
operate on parasitic power from the PicoMite as shown on the right.
I/O Pin
Multiple sensors can be used but a separate I/O pin and a 4.7K pullup
resistor is required for each one.
Normal Power
To get the current temperature you just use the TEMPR() function in an
expression. For example:
PRINT "Temperature: " TEMPR(pin)
Where 'pin' is the I/O pin to which the sensor is connected. You do not
have to configure the I/O pin, that is handled by MMBasic.
3.3V
The returned value is in degrees C with a resolution of 0.25 ºC and is
4.7K
accurate to ±0.5 ºC. If there is an error during the measurement the
returned value will be 1000.
Any
PicoMite
The time required for the overall measurement is 200ms and the running
I/O Pin
program will halt for this period while the measurement is being made.
This also means that interrupts will be disabled for this period. If you do
Parasitic Power
not want this you can separately trigger the conversion using the
TEMPR START command then later use the TEMPR() function to
retrieve the temperature reading. The TEMPR() function will always wait if the sensor is still making the
measurement.
For example:
TEMPR START GP15
< do other tasks >
PRINT "Temperature: " TEMPR(GP15)



Measuring Humidity and Temperature
The DEVICE HUMID command will read the humidity and
temperature from a DHT22 humidity/temperature sensor. This
device is also sold as the RHT03 or AM2302 but all are
compatible and can be purchased on eBay for under $5. The
DHT11 sensor is also supported.
The DHT22 must be powered from 3.3V (the maximum voltage
for the PicoMite’s I/O pins) and it should have a pullup resistor
on the data line as shown. This is suitable for long cable runs
(up to 20 meters) but for short runs the resistor can be omitted
as the PicoMite also provides an internal weak pullup.

3.3V

4.7K
Any
PicoMite
I/O Pin

To get the temperature or humidity you use the HUMID command with three arguments as follows:
DEVICE HUMID pin, tVar, hVar [,DHT11]
Where 'pin' is the I/O pin to which the sensor is connected. The I/O pin will be automatically configured by
MMBasic.
'tVar' is a floating point variable in which the temperature is returned and 'hVar' is a second variable for the
humidity. The temperature is returned as degrees C with a resolution of one decimal place (e.g. 23.4) and the
humidity is returned as a percentage relative humidity (e.g. 54.3).
If the optional DHT11 parameter is set to 1 then the command will use device timings suitable for that device.
In this case the results will be returned with a resolution of 1 degree and 1% humidity
For example:
DIM FLOAT temp, humidity
DEVICE HUMID GP15, temp, humidity
PRINT "The temperature is" temp " and the humidity is" humidity

Real Time Clock Interface
Using the RTC GETTIME command it is easy to get the current time from a PCF8563, DS1307, DS3231 or
DS3232 real time clock as well as compatible devices such as the M41T11. These integrated circuits are
popular and cheap, will keep accurate time even with the power removed and can be purchased for $2 to $8 on
eBay. Complete modules including the battery can also be purchased on eBay for a little more.
The PCF8563 and DS1307 will keep time to within a minute or two over a month while the DS3231 and
DS3232 are particularly precise and will remain accurate to within a minute over a year.
These chips are I2C devices and should be connected to the I2C I/O pins of the PicoMite.
Internal pullup resistors (100KΩ) are applied to the I2C I/O pins so in many cases external resistors are not
needed.
In order to enable the RTC you first need to allocate the I2C pins to be used using the command:
OPTION SYSTEM I2C SDApin, SCLpin
The time used by the RTC must also be set. That is done with the RTC SETTIME command which uses the
format RTC SETTIME year, month, day, hour, minute, second. Note that the hour must be in 24 hour format.
For example, the following will set the real time clock to 4PM on the 10th November 2021:
RTC SETTIME 2021, 11, 10, 16, 0, 0
To get the time you use the RTC GETTIME command which will read the time from the real time clock chip
and set the clock inside the PicoMiteVGA . Normally this command will be placed at the beginning of the
program or in the subroutine MM.STARTUP so that the time is set on power up. The command OPTION RTC
AUTO ENABLE can also be used to set an automatic update of the time$ & date$ from RTC on boot & every
hour.



Measuring Distance
Using a HC-SR04 ultrasonic sensor and the DISTANCE() function you can
measure the distance to a target.
This device can be found on eBay for about $4 and it will measure the
distance to a target from 3cm to 3m. It works by sending an ultrasonic sound
pulse and measuring the time it takes for the echo to be returned.
Compatible sensors are the SRF05, SRF06, Parallax PING and the DYPME007 (which is waterproof and therefore good for monitoring the level of a
water tank).
On the PicoMite you use the DISTANCE function as follows:
d = DISTANCE(trig, echo)
The value returned is the distance in centimetres to the target.
Where trig is the I/O pin connected to the "trig" input of the sensor and echo is the pin connected the "echo"
output of the sensor. You can also use 3-pin devices and in that case only one pin number is specified. The
maximum voltage on the PicoMite’s I/O pins is 3.3V so a resistor divider will be required to interface the
PicoMite to the echo pin of the sensor (which operates on 5V).

LCD Display
The LCD command will display text on a standard LCD module with the
minimum of programming effort.
This command will work with LCD modules that use the KS0066,
HD44780 or SPLC780 controller chip and have 1, 2 or 4 lines. Typical
displays include the LCD16X2 (futurlec.com), the Z7001
(altronics.com.au) and the QP5512 (jaycar.com.au). eBay is another
good source where prices can range from $10 to $50.
To setup the display you use the DEVICE LCD INIT command:
DEVICE LCD INIT d4, d5, d6, d7, rs, en
d4, d5, d6 and d7 are the numbers of the I/O pins that connect to inputs D4, D5, D6 and D7 on the LCD module
(inputs D0 to D3 and R/W on the module should be connected to ground). 'rs' is the pin connected to the
register select input on the module (sometimes called CMD or DAT). 'en' is the pin connected to the enable or
chip select input on the module.
Any I/O pins on the PicoMite can be used and you do not have to set them up beforehand (the LCD command
automatically does that for you). The following shows a typical set up.
+5V

10K

2
Vdd
RS

4

EN

6

PicoMite

RS
EN

3
CONTRAST

LCD Module

D7
D6
D5
D4
D3
14
13
12
11
10

D2
9

D1
8

D0
7

GND R/W
1
5

D7
D6
D5
D4

To display characters on the module you use the LCD command:
DEVICE LCD line, pos, data$
Where line is the line on the display (1 to 4) and pos is the position on the line where the data is to be written
(the first position on the line is 1). data$ is a string containing the data to write to the LCD display. The
characters in data$ will overwrite whatever was on that part of the LCD.


The following shows a typical usage where d4 to d7 are connected to pins GP2 to GP4 on the PicoMite, rs is
connected to pin GP6 and en to pin GP7.
DEVICE LCD INIT GP2, GP3, GP4, GP5, GP6, GP7
DEVICE LCD 1, 2, "Temperature"
DEVICE LCD 2, 6, STR$(TEMPR(GP15))
' DS18B20 connected to pin GP15
Note that this example also uses the TEMPR() function to get the temperature (described above).

Keypad Interface
A keypad is a low tech method of entering data into a PicoMite based system. The PicoMite supports either a
4x3 keypad or a 4x4 keypad and the monitoring and decoding of key presses is done in the background. When
a key press is detected an interrupt will be issued where the program can deal with it.
Examples of a 4x3 keypad and a 4x4 keypad are the Altronics S5381 and S5383 (go to www.altronics.com).
To enable the keypad feature you use the command:
KEYPAD

var, int, r1, r2, r3, r4, c1, c2, c3, c4

Where var is a variable that will be updated with the key code and int is the name of the interrupt subroutine to
call when a new key press has been detected. r1, r2, r3 and r4 are the pin numbers used for the four row
connections to the keypad (see the diagram below) and c1, c2, c3 and c4 are the column connections. c4 is only
used with 4x4 keypads and should be omitted if you are using a 4x3 keypad.
Any I/O pins on the PicoMite can be used and you do not have to set them up beforehand, the KEYPAD
command will automatically do that for you.

R1
R2
R3
R4

PicoMite

1

2

3

20

4

5

6

21

7

8

9

22

10

0

11

23

C1
C2
C3
C4

The detection and decoding of key presses is done in the background and the program will continue after this
command without interruption. When a key press is detected the value of the variable var will be set to the
number representing the key (this is the number inside the circles in the diagram above). Then the interrupt
will be called.
For example:
Keypad KeyCode, KP_Int,GP2,GP3,GP4,GP5,GP6,GP7,GP8
' 4x3 keybd
DO
< body of the program >
LOOP
SUB KP_Int
PRINT "Key press = " KeyCode
END SUB


' a key press has been detected


WS2812 Support
The PicoMite has built in support for the WS2812 multicolour LED chip. This chip needs a very specific
timing to work properly and with the DEVICE WS2812 command it is easy to control these devices with
minimal effort.
This command will output the required signals needed to drive a chain of WS2812 LED chips connected to the
pin specified and set the colours of each LED in the chain. The syntax of the command is:
DEVICE WS2812 type, pin, nbr%, colours%[()]
Note that the pin must be set to a digital output before this command is used. The colours%() array should be
sized to have at least the same number of elements as the number of LEDs to be driven (nbr%). Each element
in the array should contain the colour in the normal RGB888 format (0 - HFFFFFF). Where a single LED is to
be driven then colours% should be a simple variable.
Up to 256 WS2812 chips in a string are supported.
'type' is a single character specifying the type of chip being driven as follows:
O = original WS2812
B = WS2812B
S = SK6812
W = SK6812W (RGBW)
As an example:
DIM b%(4)=(RGB(red), Rgb(green), RGB(blue), RGB(Yellow), rgb(cyan))
SETPIN GP5, DOUT
DEVICE WS2812 O, GP5, 5, b%()
will output the specified colours to an array of five WS2812 LEDs daisy chained off pin GP5.
It is possible that a WS2812 will not work reliably with the 3.3V output from the PicoMite. In this case there
are a number of solutions:
 Use the WS2812B which will work with a 3.3V supply and inputs.
 Use a level shifter to drive the WS2812.
 Use a single WS2812 powered from 3.3V as a first stage to buffer the input of the first "real" LED in the
string. The minimum supply for the WS2812 is 4V but in many cases it will work at 3.3V.

PS2 Keyboard
On the PicoMite you can attach a PS2 keyboard and, display the output of the interpreter on the LCD (see the
LCD Display as the Console Output section below). This turns the PicoMite into a completely self contained
computer with its own keyboard and display. Using the built in colour coded editor programs can be entered,
edited and run without requiring another computer.
Because the PicoMite I/O is specified for a maximum of 3.6V and PS2 keyboards
run off 5V level conversion should be used on the CLOCK and DATA pins. A
suitable commercially available Adafruit 4 channel bi-directional level converter is
pictured on the right. The PS2 CLOCK pin should be connected via the level
converter to PicoMite pin 11 (GP8) and the PS2 DATA pin to PicoMite pin 12
(GP9).
Before the keyboard can be used it must first be enabled by specifying the language
of the keyboard:
OPTION KEYBOARD language [,capslock][,numlock][,repeatstart] [,repeatrate]
Where ‘language’ is a two character code such as US for the standard keyboard used in the USA, Australia and
New Zealand. Other keyboard layouts that can be specified are United Kingdom (UK), French (FR), German
(GR), Belgium (BE), Italian (IT) ), Brazilian (BR) or Spanish (ES). Note that the non US layouts map some of
the special keys present on these keyboards but the corresponding special character will not display as they are
not part the standard PicoMite fonts (another character will be used instead).
This command configures the I/O pins dedicated to the keyboard and initialises it for use. As with similar
commands this option will be saved in flash memory and automatically applied on power up. If you need to
remove the keyboard you can do this with the OPTION KEYBOARD DISABLE command.
See the OPTION KEYBOARD command for details of the optional parameters.



LCD Display as the Console Output
The keyboard can be used on its own as an alternative input method but it works particularly well when the
LCD display panel is used as the console output. The LCD should be one of the SSD1963 versions in the
landscape orientation and it must be first configured using OPTION LCDPANEL.
To enable the output to the LCD panel you should use the following command:
OPTION LCDPANEL CONSOLE [font [, fc [, bc [, blight]]]
'font' is the default font, 'fc' is the default foreground colour, 'bc' is the default background colour and 'blight' is
the default backlight brightness (2 to 100). These settings are saved in flash and are used to configure MMBasic
at power up. They are all optional and default to font 2, white, black and 100%.
Colour coding in the editor (see below) is also turned on by this command (OPTION COLOURCODE OFF
will turn it off again). To disable using the LCD panel as the console the command is OPTION LCDPANEL
NOCONSOLE.
There are three SPI displays that can also be used as console devices. ILI9341 (but only if MISO is connected),
ILI9488/86 (connect MISO with a 680Ω series resistor as the controller does not tri-state its output properly)
and the 2.8" Waveshare ST7789. Note that with all of these the scrolling of text on the screen will be very
slow.
Used with a PS2 keyboard this option turns the PicoMite into a self contained computer with its own keyboard
and display. Rather like a modern version of the Maximite (see http://geoffg.net/maximite.html).

OV7670 Camera module
The PicoMite has support for a OV7670 camera module. See the DEVICE CAMERA command for details



Display Panels
The PicoMite includes support for many LCD display panels using an SPI, I2C or parallel interface.
These commands must be entered at the command prompt (not in a program) and will cause the PicoMite to
restart. This has the side effect of disconnecting the USB console interface which will need to be reconnected.
Note that the maximum voltage on all the PicoMite I/O pins is 3.3V. Level shifting will be required if a display
uses 5V levels for signalling.

SPI Based Display Panels
The SPI based display controllers share the SYSTEM SPI channel interface on the PicoMite with the touch
controller (if present). An SD Card can also be configured to use the same pins. When this is done the pins
allocated to the SYSTEM SPI will not be available to other MMBasic commands. The speed of drawing to SPI
based displays will be largely unaffected by the CPU speed.
These panels are configured using the following commands. In all commands the parameters are:
 OR = This is the orientation of the display and it can be LANDSCAPE, PORTRAIT, RLANDSCAPE or
RPORTRAIT. These can be abbreviated to L, P, RL or RP. The R prefix indicates the reverse or "upside
down" orientation.


DC = Display Data/Command control pin.



RESET = Display Reset pin (when pulled low).



CS = Display Chip Select pin.



BACKLIGHTPIN = Optional pin used to control the backlight brightness.

Any free pins can be used.

OPTION LCDPANEL ILI9341, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ILI9341 controller. This supports 320 * 240 resolution. Displays using this
controller are capable of transparent text and will work with the BLIT and BLIT READ commands.

OPTION LCDPANEL ILI9163, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ILI9163 controller. This supports 128 * 128 resolution.

OPTION LCDPANEL ILI9481, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ILI9481 controller. This supports 480 * 320 resolution.

OPTION LCDPANEL ILI9481IPS, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises an IPS display using the ILI9481 controller. This supports 480 * 320 resolution.

OPTION LCDPANEL ILI9488, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ILI9488 controller. This supports 480 * 320 resolution. Note that this
controller has an issue with the MISO pin which interferes with the touch controller. For this display to work the
MISO pin must not be connected.

OPTION LCDPANEL ILI9488W, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ILI9488 controller. This supports the Waveshare 3.5" display as used on their
Pico Eval board and the normal 3.5" display adapter.



OPTION LCDPANEL N5110, OR, DC, RESET, CS [,contrast]
Initialises a LCD display using the Nokia 5110 controller. This supports 84 * 48 resolution. An additional
parameter ‘contrast’ may be specified to control the contrast of the display. Try contrast values between &HA8
and &HD0 to suit your display, default if omitted is &HB1

OPTION LCDPANEL SSD1306SPI, OR, DC, RESET, CS [,offset]
Initialises a OLED display using the SSD1306 controller with an SPI interface. This supports 128 * 64 resolution.
An additional parameter ‘offset’ may be specified to control the position of the display. 0.96" displays typically
need a value of 0. 1.3" displays typically need a value of 2. Default if omitted is 0.

OPTION LCDPANEL SSD1331, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a colour OLED display using the SSD1331 controller. This supports 96 * 64 resolution.

OPTION LCDPANEL ST7735, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a TFT display using the ST7735 controller. This supports 160 * 128 resolution.

OPTION LCDPANEL ST7735S, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a IPS display using the ST7735S controller. This supports 160 * 80 resolution.

OPTION LCDPANEL ST7735S_W, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a Waveshare 128x128 ST7735S display. This supports 128 * 128 resolution.

OPTION LCDPANEL ST7789, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a IPS display using the 7789 controller. This supports 240 * 240 resolution.
NOTE: display boards without a CS pin are not currently supported on the PicoMite unless modified.

OPTION LCDPANEL ST7789_135, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a IPS display using the 7789 controller. This supports 240 * 135 resolution.
NOTE: display boards without a CS pin are not currently supported on the PicoMite unless modified.

OPTION LCDPANEL ST7789_320, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a IPS display using the 7789 controller. This type supports the 320 * 240 resolution display from
Waveshare ( https://www.waveshare.com/wiki/Pico-ResTouch-LCD-2.8 ).
These are capable of transparent text and will work with the BLIT and BLIT READ commands.
NOTE: display boards without a CS pin are not currently supported on the PicoMite unless modified.

OPTION LCDPANEL GC9A01, OR, DC, RESET, CS [,BACKLIGHTPIN]
Initialises a IPS display using the GC9A01 controller. This supports 240 * 240 resolution.

OPTION LCDPANEL ST7920, OR, DC, RESET
Initialises a LCD display using the ST7920 controller. This supports 128 * 64 resolution. Note this display does
not support a chip select so the SPI bus cannot be shared if this display is used.

I2C Based LCD Panels
The I2C based display controllers use the SYSTEM I2C pins as per the pinout for the specific device. Other I2C
devices can share the bus subject to their addresses being unique. To setup the system I2C bus use the
command: OPTION SYSTEM I2C sdapin, sclpin



If an I2C display is configured it will not be necessary to "open" the I2C port for an additional device (I2C
OPEN), I2C CLOSE is blocked, and all I2C devices must be capable of 100KHz operation. The I2C bus speed
is not affected by changes to the CPU clock speed
These panels are configured using the following commands. In all commands the parameters OR is the
orientation of the display and it can be LANDSCAPE, PORTRAIT, RLANDSCAPE or RPORTRAIT. These
can be abbreviated to L, P, RL or RP. The R prefix indicates the reverse or "upside down" orientation.

OPTION LCDPANEL SSD1306I2C, OR [,offset]
Initialises a OLED display using the SSD1306 controller with an I2C interface. This supports 128 * 64 resolution.
An additional parameter offset may be specified to control the position of the display. 0.96" displays typically
need a value of 0. 1.3" displays typically need a value of 2. Default if omitted is 0.
NB many cheap I2C versions of SSD1306 displays do not implement I2C properly due to a wiring error. This
seems to be particularly the case with 1.3" variants

OPTION LCDPANEL SSD1306I2C32, OR
Initialises a OLED display using the SSD1306 controller with an I2C interface. This supports 128 * 32 resolution.

8-bit Parallel LCD Panels
In addition to the SPI and I2C based
controllers the PicoMite supports
LCD displays using the SSD1963
controller (as illustrated) and the
ILI9341 controller.
These use a parallel interface, are
available in sizes from 2.8" to 9" and
have better specifications than the
smaller displays. All these displays
have an SD Card socket which is fully
supported by MMBasic on the
PicoMite.
On eBay you can find suitable
displays by searching for the
controller’s name (eg SSD1963).
Because they use a parallel interface the PicoMite can transfer data
much faster than an SPI interface resulting in a very quick screen
update.
The SSD1963 displays in particular are also much larger, have more
pixels and are brighter. MMBasic can drive some of them using 24-bit
true colour for a full colour rendition (16 million colours).
The characteristics of these displays are:
 A 2.8, 3.2, 4.3, 5, 7, 8 or 9 inch display
 Resolution of 320 x 240, 480 x 272 pixels (4.3" version) or 800
x 480 pixels (5”, 7", 8" or 9" versions).
 An SSD1963 display controller or ILI9341 display controller
with a parallel interface (8080 format)
 A touch controller (SPI interface).
 A full sized SD Card socket.
There are a number of different designs using the SSD1963 controller
but fortunately most Chinese suppliers have standardised on a single
connector as illustrated on the right.
It is strongly recommended that any display purchased has a matching
connector – this provides some confidence that the manufacturer has
followed the standard that the PicoMite is designed to use.



Connecting an 8-bit parallel LCD Panel
The controller uses a parallel interface while the touch controller and SD Card use an SPI interface. The touch and
SD Card features are optional but if they are used they will use the second SPI port (SPI2).
The following table lists the connections required between the display board and the PicoMite to support the 8-bit
parallel interface and the LCD display. The touch controller and SD Card interfaces are listed further below.
8-bit parallel
Display

PicoMite

Description

DB0

Parallel Data Bus bit 0

Pin 1/GP0

DB1

Parallel Data Bus bit 1

Pin 2/GP1

DB2

Parallel Data Bus bit 2

Pin 4/GP2

DB3

Parallel Data Bus bit 3

Pin 5/GP3

DB4

Parallel Data Bus bit 4

Pin 6/GP4

DB5

Parallel Data Bus bit 5

Pin 7/GP5

DB6

Parallel Data Bus bit 6

Pin 9/GP6

DB7

Parallel Data Bus bit 7

Pin 10/GP7

CS

Chip Select (active low)

Ground (ie, always selected)

WR

Write (active low)

Pin 19/GP14*

RD

Read (active low)

Pin 20/GP15*

DC

Command/Data

Pin 17/GP13*

RESET

Reset the SSD1963

Pin 21/GP16*

LED_A

Backlight control for an unmodified display panel

Configurable see OPTION
LCDPANEL

5V

5V power for the backlight on some displays (most displays use the 3.3V supply for this).

3.3V

Power supply.

GND
Ground
* Pins DC, WR, RD, RESET can be allocated to other pins as a block of 4 using the optional parameter DCpin
The following table lists the connections required to support the touch controller interface:
8-bit parallel
Display

PicoMite

Description

T_CS

Touch Chip Select

Recommend Pin 24/GP18

T_IRQ

Touch Interrupt

Recommend Pin 25/GP19

T_DIN

Touch Data In (MOSI)

Recommend Pin 15/GP11

T_CLK

Touch SPI Clock

Recommend Pin 14/GP10

T_DO

Touch Data Out (MISO)

Recommend Pin 16/GP12

The following table lists the connections required to support the SD Card connector:
8-bit parallel
Display

Description

PicoMite

SD_CS

SD Card Chip Select

Recommend Pin 29/GP22

SD_DIN

SD Card Data In (MOSI)

Recommend Pin 15/GP11

SD_CLK

SD Card SPI Clock

Recommend Pin 14/GP10

SD_DO

SD Card Data Out (MISO)

Recommend Pin 16/GP12



Where a PicoMite connection is listed as "Recommend" the specific pin should be specified in the appropriate
OPTION command (see below).
Generally 7 inch and larger displays have a separate pin on the connector (marked 5V) for powering the backlight
from a 5V supply. If this pin is not provided the backlight power will be drawn from the 3.3V pin. Note that the
power drawn by the backlight can be considerable. For example, a 7 inch display will typically draw 330 mA
from the 5V pin.
The current drawn by the backlight can cause a voltage drop on the LCD display panel’s ground pin which can in
turn shift the logic levels as seen by the display controller resulting in corrupted colours or text. An easy way of
diagnosing this effect is to reduce the CPU speed to (say) 48MHz. If this fixes the problem it is a strong
indication that this is the cause. Soldering power and ground wires direct to the LCD display panel’s PCB is one
workaround.
Care must be taken with display panels that share the SPI port between a number of devices (SD Card, touch, etc).
In this case all the Chip Select signals must configured in MMBasic or disabled by a permanent connection to
3.3V. If this is not done the pin will float causing the wrong controller to respond to commands on the SPI bus.
On the PicoMite either SPI channel can used to communicate with the touch controller and the SD Card interface
as defined by the OPTION SYSTEM SPI setting. If this is set, that SPI channel will be unavailable to BASIC
programs (which can use the other SPI channel).

Configuring an 8-bit parallel LCD Panel
To use the display MMBasic must be configured using the OPTION LCDPANEL command which is normally
entered at the command prompt. Every time the PicoMite is restarted MMBasic will automatically initialise the
display.
The syntax is:
OPTION LCDPANEL controller, orientation [,backlightpin] [,DCpin]

Where 'controller' can be either:
 SSD1963_4
 SSD1963_5
 SSD1963_5A

For a 4.3 inch display
For a 5 inch display
For an alternative version of the 5 inch display if SSD1963_5 does not work

 SSD1963_7
For a 7 inch display
 SSD1963_7A
For an alternative version of the 7 inch display if SSD1963_7 does not work.
 SSD1963_8
For 8 inch or 9 inch displays.
 ILI9341_8
For a 2.8” or 3.2” display
'orientation' can be LANDSCAPE, PORTRAIT, RLANDSCAPE or RPORTRAIT. These can be abbreviated to
L, P, RL or RP. The R prefix indicates the reverse or "upside down" orientation.
‘DCpin’ is optional and is the Data/Command pin (previously called the RS pin). If this parameter is omitted the
pin assignment will be as above in the table. If it is specified then DC, WR, RD and RESET pins will be assigned
sequentially from DC pin.
This command only needs to be run once. From then on MMBasic will automatically initialise the display on
startup or reset. In some circumstances it may be necessary to interrupt power to the LCD panel while the
PicoMite is running (eg, to save battery power) and in that case the GUI RESET LCDPANEL command can be
used to reinitialise the display.
If the LCD panel is no longer required the command OPTION LCDPANEL DISABLE can be used which will
return the I/O pins for general use.
To verify the configuration you can use the command OPTION LIST to list all options that have been set
including the configuration of the LCD panel.
To test the display you can enter the command GUI TEST LCDPANEL. You should see an animated display of
colour circles being rapidly drawn on top of each other. Press the space bar on the console’s keyboard to stop the
test.

8 and 9 inch Displays
The controller configuration SSD1963_8 has only been tested with the 8 and 9 inch displays made by EastRising
(available at www.buydisplay.com). These must be purchased as a TFT LCD panel with 8080 interface, 800x480
pixel LCD, SSD1963 display controller and XPT2046 touch controller. Note that the EastRising panels use a
non-standard interface connector pin-out so you will need to refer to their data sheets when connecting these to the


PicoMite. A suitable adapter to convert to the standard 40-pin connection can be purchased from:
https://www.rictech.nz/micromite-products

Backlight Control
For the ILI9163, ILI9341, ST7735, ST7735S, SSD1331, ST7789, ILI9481, ILI9488, ILI9488W, ST7789_135
ILI9341_8 and ST7789_320 displays an optional parameter ‘, backlight’ can be added to the end of the
configuration parameters which specifies a pin to use to control the brightness of the backlight (LED_A). This
will setup a PWM output on that pin with a frequency of 50KHz and an initial duty cycle of 99%.
You can then use the BACKLIGHT command to change the brightness between 0 and 100%. The PWM channel
is blocked for normal PWM use and must not conflict with the PWM channel that may be set up for audio.
For example:

OPTION LCDPANEL ILI9341, OR, DC, RESET, CS, GP11
The backlight can then be set to 40% with this command:

BACKLIGHT 40
Most SSD1963 based LCD panels have three pairs of
solder pads on the PCB which are grouped under the
heading "Backlight Control" as illustrated on the right.
Normally the pair marked "LED-A" are shorted together
with a zero ohm resistor and this allows control of the
backlight's brightness with a PWM (pulse width
modulated) signal on the LED-A pin of the display
panel's main connector.
However, it is better to use the SSD1963 controller to
generate this signal as it frees up one I/O pin. To use the
SSD1963 for brightness control the zero ohm resistor
should be removed from the pair marked "LED-A" and
used to short the nearby pair of solder pads marked "1963-PWM". The PicoMite can then control the brightness
via the SSD1963 controller using the BACKLIGHT command.

Example SPI LCD Panel Configuration
The following is a summary of how a typical LCD panel using an ILI9341 controller can be connected. This
example supports the SD Card socket, the LCD display and the touch interface.
Typical panels can be found on ebay.com and similar sites by searching for the keyword “ILI9341”. Make sure
that the connections on the rear of the panel resemble that shown below:
The panel should be connected to the PicoMite as illustrated:
GP11
GP16
GP19
GP12
GP18
GP16
+5V
GP18
GP19
GP15
GP14
GP13
Ground
+5V

GP18
GP16
GP19
GP22

To match the above connections the following configuration commands should be entered, one by one at the
command prompt:

OPTION SYSTEM SPI GP18, GP19, GP16
OPTION SDCARD GP22
OPTION LCDPANEL ILI9341, L, GP15, GP14, GP13
OPTION TOUCH GP12, GP11


These commands will be remembered and automatically applied on power up. Note that after each command is
entered the PicoMite will restart, and the USB connection will be lost and must be reconnected.
Next the touch screen should be calibrated:

GUI CALIBRATE
You can then test the various components. The following will list the files on the SD Card, if it executes
without error you can be assured that the SD Card interface is good.

FILES
The following will draw multiple colourful overlapping circles on the LCD screen which will confirm that the
LCD is connected correctly:

GUI TEST LCDPANEL
Finally, the following will test the touch interface. When you touch the LCD screen a dot should appear on the
screen at the exact point of the touch.

GUI TEST TOUCH
If this is not accurate you may have to run the GUI CALIBRATE command a second time taking greater care.
If you run into trouble getting the display to work it is worth disconnecting everything and clear the options
with the command OPTION RESET so that you can start with a clean slate. Then reconnect it one stage at a
time and configure and test each new stage as you progress. First OPTION SYSTEM SPI, then the LCD
display, the touch interface and finally the SD Card.
Also note that the ILI9341 controller is sensitive to static discharge so, if the panel will not respond, it could be
damaged and it would be worth testing with another panel.



Touch Support
Many LCD panels are supplied with a resistive touch sensitive panel and associated controller chip. MMBasic
fully supports this interface on the PicoMite and this allows many of the physical knobs and switches used in a
project to be implemented as on-screen controls activated by touch.
Note that the maximum voltage on all the PicoMite I/O pins is 3.3V. Level shifting will be required if a display
uses 5V levels for signalling.

Configuring Touch
The touch controller on an LCD panel uses the SPI protocol for communications and this needs to be
specifically configured before the panel can be configured. This is the “system” SPI port which is the port that
will be used for system use (SD Card, LCD display and the touch controller on a LCD panel). This SPI port
will then not be available to BASIC programs (i.e., it is reserved)
There are a number of ports and pins that can be used but these are the same as the configuration used for the
example LCD panel interface previously in this manual. This command does not need to be repeated if the
system SPI has already been configured:

OPTION SYSTEM SPI GP18, GP19, GP16
To use the touch facility MMBasic must be told that it is available using the OPTION TOUCH command. This
should be done after the LCD display has been configured. This command tells MMBasic what pins are used for
the Chip Select and Interrupt signals. For example this sets Chip Select to the GP12 pin and Interrupt to GP11:

OPTION TOUCH GP12, GP11
These commands must be entered at the command prompt and will cause the PicoMite to restart. This has the
side effect of disconnecting the USB console interface which will need to be reconnected.
When the PicoMite is restarted MMBasic will automatically initialise the touch controller. To verify the
configuration, you can use the command OPTION LIST to list all options that have been set including the
configuration of the display panel and touch.
Note that you can use many different configurations using various pin allocations – this is just an example
based on the configuration commands listed above.
Care must be taken when the SPI port is shared between a number of devices (SD Card, touch, etc). In this case
all the Chip Select signals must configured in MMBasic or alternatively disabled.

Calibrating the Touch Screen
Before the touch facility can be used it must be calibrated using the GUI CALIBRATE command.
This command will present a target in the top left corner of the screen. Using a pointy but blunt object (such as
a toothpick) press exactly on the centre of the target and hold it down for at least a second. MMBasic will
record this location and then continue the calibration by sequentially displaying the target in the other three
corners of the screen for touch and calibration.
The calibration routine may warn that the calibration was not accurate. This is just a warning and you can still
use the touch feature if you wish but it would be better to repeat the calibration using more care.
Following calibration you can test the touch facility using the GUI TEST TOUCH command. This command
will blank the screen and wait for a touch. When the screen is touched a white dot will be placed on the display
marking the position on the screen. If the calibration was carried out successfully the dot should be displayed
exactly under the location of the stylus on the screen.
To exit the test routine you can press the space bar on the console’s keyboard.

Touch Functions
To detect if and where the screen is touched you can use the following functions in a BASIC program:


TOUCH(X)
Returns the X coordinate of the currently touched location or -1 if the screen is not being touched.



TOUCH(Y)
Returns the Y coordinate of the currently touched location or -1 if the screen is not being touched.





TOUCH(DOWN)
Returns true if the screen is currently being touched (this is much faster than TOUCH(X or Y)).



TOUCH(UP)
Returns true if the screen is currently NOT being touched (also faster than TOUCH(X or Y))



TOUCH(LASTX)
Returns the X coordinate of the last location that was touched.



TOUCH(LASTY)
Returns the Y coordinate of the last location that was touched.



TOUCH(REF)
Returns the reference number of the control that is currently being touched or zero if no control is being
touched. See the section Advanced Graphics for more details.



TOUCH(LASTREF)
Returns the reference number of the control that was last touched.

The GUI BEEP Command
The Piezo buzzer specified in the OPTION TOUCH command can also be driven by a BASIC program using
the command:
GUI BEEP msec

Where 'msec' is the number of milliseconds that the beeper should be driven. A time of 3ms produces a click
while 100ms produces a short beep.

Touch Interrupts with no Advanced GUI controls
An interrupt can be set on the IRQ pin number that was specified when the touch facility was configured. To
detect touch down the interrupt should be configured as INTL (i.e., high to low).
For example, if the command OPTION TOUCH 7, 15 was used to configure touch the following program will
print out the X and Y coordinates of any touch on the screen:
SETPIN 15, INTL, MyInt
DO : LOOP
SUB MyInt
PRINT TOUCH(X) TOUCH(Y)
END SUB
The interrupt can be cancelled with the command SETPIN pin, OFF.

Touch Interrupts with Advanced GUI controls
When the Advanced GUI controls are activated (by setting the number of GUI controls to a non-zero number
using OPTION GUI CONTROLS) the GUI INTERRUPT command is used instead to setup a touch interrupt.
The syntax is:
GUI INTERRUPT down [, up]

Where 'down' is the subroutine to call when a touch down has been detected. And optionally 'up' is the
subroutine to call when the touch has been lifted from the screen ('up' and 'down' can point to the same
subroutine if required).
As an example, the following program will print out the X and Y coordinates of any touch on the screen:
GUI INTERRUPT MyInt
DO : LOOP
SUB MyInt
PRINT TOUCH(X) TOUCH(Y)
END SUB
Specifying the number zero (single digit) as the argument will cancel both up and down interrupts. ie:
GUI INTERRUPT 0



Graphics Commands and Functions
Colours
Colour is specified as a true colour 24 bit number where the top eight bits represent the intensity of the red
colour, the middle eight bits the green intensity and the bottom eight bits the blue. The easiest way to generate
this number is with the RGB() function which has the form:
RGB(red, green, blue)

The RGB() function also supports a shortcut where you can specify common colours by naming them. For
example, RGB(red) or RGB(cyan). The colours that can be named using the shortcut form are white, black,
blue, green, cyan, red, magenta, yellow, brown, white, orange, pink, gold, salmon, beige, lightgrey and grey (or
USA spelling gray/lightgray).
MMBasic will automatically translate all colours to the format required by the individual display controller.
For example, in the case of the ILI9341 controller, is 64K colours in the 565 format.
The default for commands that require a colour parameter can be set with the COLOUR command (can also be
spelt COLOR). This is handy if your program uses a consistent colour scheme, you can then set the defaults
and use the short version of the drawing commands throughout your program.
The COLOUR command takes the format:
COLOUR foreground-colour, background-colour

Fonts
There are eight built in fonts. These are:
Font
Number

Size
(width x height)

Character
Set
All 95 ASCII characters
plus 7F to FF (hex)

1

8 x 12

2

12 x 20

All 95 ASCII characters

Medium sized font

3

16 x 24

All 95 ASCII characters

A larger font

4

10x16

All 95 ASCII characters
plus 7F to FF (hex)

A font with extended graphic characters. Suitable for
high resolution displays

5

24 x 32

All 95 ASCII characters

Extra large font, very clear

6

32 x 50

0 to 9 plus some
symbols

Numbers plus decimal point, positive, negative,
equals, degree and colon symbols. Very clear.

7

6x8

All 95 ASCII characters

A small font useful when low resolutions are used.

8

4x6

All 95 ASCII characters

An even smaller font.

Description
Standard font (default on start-up).

In all fonts (including font #6) the back quote character
(60 hex or 96 decimal) has been replaced with the degree
symbol (º).
Font #1 (the default font) and font #4 have an extended
character set covering all characters from CHR$(32) to
CHR$(255) or 20 to FF (hex) as illustrated on the right.
If required, additional fonts can be embedded in a
BASIC program. These fonts work exactly same as the
built in font (i.e. selected using the FONT command or
specified in the TEXT command).



The format of an embedded font is:
DefineFont #Nbr
hex [[ hex[…]
hex [[ hex[…]
END DefineFont
It must start with the keyword "DefineFont" followed by the font number (which may be preceded by an
optional # character). Any font number in the range of 2 to 5 and 8 to 16 can be specified and if it is the same
as a built in font it will replace that font. The body of the font is a sequence of 8-digit hex words with each
word separated by one or more spaces or a new line. The font definition is terminated by an "End DefineFont "
keyword. These can be placed anywhere in a program and MMBasic will skip over it. This format is the same
as that used by the Micromite.
Additional fonts and information can be found in the Embedded Fonts folder in the PicoMite firmware
download. These fonts cover a wide range of character sets including a symbol font (Dingbats) which is handy
for creating on screen icons, etc.

Read Only Variables
All coordinates and measurements on the screen are done in terms of pixels with the X coordinate being the
horizontal position and Y the vertical position. The top left corner of the screen has the coordinates X = 0 and
Y = 0 and the values increase as you move down and to the right of the screen.
There are four read only variables which provide useful information about the display currently connected:
 MM. HRES
Returns the width of the display (the X axis) in pixels.
 MM. VRES
Returns the height of the display (the Y axis) in pixels.
 MM.FONTHEIGHT
Returns the height of the current default font (in pixels). All characters in a font have the same height.
 MM.FONTWIDTH
Returns the width of a character in the current font (in pixels). All characters have the same width.

Drawing Commands
There are nine basic drawing commands that you can use within MMBasic programs on the PicoMite to
interact with an attached LCD display. There is also a series of more powerful GUI commands for drawing
switches, radio buttons, etc. See the next section Advanced Graphics for more details.
Most of the basic drawing commands have optional parameters. You can completely leave these off the end of
a command or you can use two commas in sequence to indicate a missing parameter. For example, the fifth
parameter of the LINE command is optional so you can use this format:
LINE 0, 0, 100, 100, , rgb(red)

Optional parameters are indicated below by italics, for example: font.
In the following commands C is the drawing colour and defaults to the current foreground colour. FILL is the
fill colour which defaults to -1 which indicates that no fill is to be used.
The drawing commands are:


CLS C
Clears the screen to the colour C. If C is not specified the current default background colour will be used.



PIXEL X, Y, C
Illuminates a pixel. If C is not specified the current default foreground colour will be used.



LINE X1, Y1, X2, Y2, LW, C
Draws a line starting at X1 and Y1 and ending at X2 and Y2.
LW is the line’s width and is only valid for horizontal or vertical lines. It defaults to 1 if not specified or if
the line is a diagonal.



BOX X, Y, W, H, LW, C, FILL
Draws a box starting at X and Y which is W pixels wide and H pixels high.
LW is the width of the sides of the box and can be zero. It defaults to 1.





RBOX X, Y, W, H, R, C, FILL
Draws a box with rounded corners starting at X and Y which is W pixels wide and H pixels high.
R is the radius of the corners of the box. It defaults to 10.



CIRCLE X, Y, R, LW, A, C, FILL
Draws a circle with X and Y as the centre and a radius R. LW is the width of the line used for the
circumference and can be zero (defaults to 1). A is the aspect ratio which is a floating point number and
defaults to 1. For example, an aspect of 0.5 will draw an oval where the width is half the height.



TEXT X, Y, STRING, ALIGNMENT, FONT, SCALE, C, BC
Displays a string starting at X and Y. ALIGNMENT is 0, 1 or 2 characters (a string expression or variable
is also allowed) where the first letter is the horizontal alignment around X and can be L, C or R for LEFT,
CENTER or RIGHT aligned text and the second letter is the vertical alignment around Y and can be T, M
or B for TOP, MIDDLE or BOTTOM aligned text. The default alignment is left/top. An additional code
letter can be used to rotate the text (see below for the details). FONT and SCALE are optional and default
to that set by the FONT command. C is the drawing colour and BC is the background colour. They are
optional and default to that set by the COLOUR command.



GUI BITMAP X, Y, BITS, WIDTH, HEIGHT, SCALE, C, BC
Displays the bits in a bitmap starting at X and Y. HEIGHT and WIDTH are the dimensions of the bitmap
as displayed on the LCD panel and default to 8x8. SCALE, C and BC are the same as for the TEXT
command. The bitmap can be an integer or a string variable or constant and is drawn using the first byte as
the first bits of the top line (bit 7 first, then bit 6, etc) followed by the next byte, etc. When the top line has
been filled the next line of the displayed bitmap will start with the next bit in the integer or string.



POLYGON n, xarray%(), yarray%() [, bordercolour] [, fillcolour]
Draws a filled or outline polygon with n xy-coordinate pairs in xarray%() and yarray%(). If ‘fillcolour’ is
omitted then just the polygon outline is drawn. If ‘bordercolour’ is omitted then it will default to the
current default foreground colour.



ARC x, y, r1, [r2], a1, a2 [, c]
Draws an arc of a circle with a given colour and width between two radials (defined in degrees). Parameters
for the ARC command are the x and y coordiantyes of the centre of the arc, the inner and outer radii, the
start and end angles of the arc and the colour of the arc. The zero degrees reference is at the 12 o’clock
posisition

Rotated Text
As described above the alignment of the text in the TEXT command can be specified by using one or two
characters in a string expression for the third parameter of the command. In this string you can also specify a
third character to indicate the rotation of the text. This character can be one of:
N for normal orientation
V for vertical text with each character under the previous running from top to bottom.
I the text will be inverted (i.e. upside down)
U the text will be rotated counter clockwise by 90º
D the text will be rotated clockwise by 90º
This extra feature applies in the TEXT and GUI CAPTION commands.
As an example, the following will display the text "LCD Display" vertically down the left hand margin of the
display panel and centred vertically:
TEXT 0, 250, "LCD Display", "LMV", 5
Positioning is relative to the top left corner of the character when viewed normally so inverted 100,100 will
have the top left pixel of the first character at 100,100 and the text will then be above y=101 and to the left of
x=101. Similarly “R” in the alignment string is viewed from the perspective of the character in whatever
orientation it is in (not the screen).

Transparent Text
If the display is capable of transparent text the TEXT command will allow the use of -1 for the background
colour. This means that the text is drawn over the background with the background image showing through the
gaps in the letters. Compatible displays use the SSD1963, ILI9341, ST7789_320, or ILI9488 with MISO
connected.


BLIT Command
If the display is capable of transparent text the BLIT command allows a portion of the image currently showing
on the display to be copied to a memory buffer and later copied back to the display. This is useful when
something needs to be drawn over the background and later removed without damaging the image in the
background. Examples include a game where a character is moving about in front of a landscape or the moving
needle of a photorealistic gauge.
The available commands are:
BLIT READ #b, x, y, w, h
BLIT WRITE #b, x, y, w, h
BLIT LOAD #b, f$, x, y, w, h
BLIT CLOSE #b
#b is the buffer number in the range of 1 to 32. x and y are the coordinates of the top left corner and w and h
are the width and height of the image. READ will copy the display image to the buffer, WRITE will copy the
buffer to the display and CLOSE will free up the buffer and reclaim the memory used. LOAD will load an
image file into the buffer.
BLIT LOAD and BLIT WRITE will work on any display while BLIT and BLIT READ will only work on
displays capable of transparent text (i.e. using the SSD1963, ILI9341, ST7789_320, or ILI9488 with MISO
connected).
These commands can be used to copy a portion of the display to another location (by copying to a buffer then
writing somewhere else) but a simpler method is to use an alternative version of the BLIT command as follows:
BLIT x1, y1, x2, y2, w, h
This will copy a portion of the image at x1/y1 to the location x2/y2. w and h specify the width and height of
the image to be copied. The source and destination areas can overlap and the BLIT command will perform the
copy correctly.
This form of the BLIT command is particularly useful for creating graphs that can scroll horizontally or
vertically as new data is added.

Load Image
The LOAD IMAGE and LOAD JPG commands can be used to load an image from the Flash Filesystem or SD
Card and display it on the LCD display. This can be used to draw a logo or add an ornate background to the
graphics drawn on the display.

Example
As an example the following program will draw a simple digital clock on an ILI9341 based LCD display. The
program will terminate and return to the command prompt if the display screen is touched.
First the display and touch options must be configured by entering the commands listed at the beginning of this
section. The exact format of these will depend on how you have connected the display panel.
Then enter and run the program:
CONST DBlue = RGB(0, 0, 128)
COLOUR RGB(GREEN), RGB(BLACK)
FONT 1, 3

' A dark blue colour
' Set the default colours
' Set the default font

BOX 0, 0, MM.HRes-1, MM.VRes/2, 3, RGB(RED), DBlue
DO
TEXT MM.HRes/2, MM.VRes/4, TIME$, "CM", 1, 4, RGB(CYAN), DBlue
TEXT MM.HRes/2, MM.VRes*3/4, DATE$, "CM"
IF TOUCH(X) <> -1 THEN END
LOOP
This program starts by defining a constant with a value corresponding to a dark blue colour and then sets the
defaults for the colours and the font. It then draws a box with red walls and a dark blue interior.



Following this the program enters a continuous loop where it performs three functions:
1. Displays the current time inside the previously drawn box. The string is drawn centred both horizontally
and vertically in the middle of the box. Note that the TEXT command overrides both the default font and
colours to set its own parameters.
2. Draws the date centred in the lower half of the screen. In this case the TEXT command uses the default
font and colours previously set.
3. Checks for a touch on the screen. This is indicated when the TOUCH(X) function returns something
other than -1. In that case the program will terminate.
The screen display should look like this (the font used in this illustration is different):



PicoMite Advanced Graphics
The PicoMite incorporates a suite of advanced graphic controls that respond to touch, these include on screen
switches, buttons, indicator lights, keyboard, etc. MMBasic will draw the control and animate it (i.e. a switch
will appear to depress when touched). All that the BASIC program needs to do is invoke a single command to
specify the basic details of the control.
To use the GUI controls in the PicoMite the memory required for the GUI controls must be allocated first by
using the command OPTION GUI CONTROLS. Typically you would use the command like this:
OPTION GUI CONTROLS 75
This will set the maximum number of controls that you can define to 75. This option is permanent (i.e. it will
be remembered on power down). By default the maximum number of controls is set to zero and in this case the
GUI features will not be available and no memory will be used.

Defining Controls
These are some of the advanced GUI controls that you can use:

Each control has a reference number called '#ref' in the description of the control. This can be any number
between 1 and the upper limit set by the OPTION CONTROL command. This reference number is used to
identify a control. For example, a check box can be created with a reference number of #10:
GUI CHECKBOX #10, "Test", 100, 100, 50, rgb(BLUE)
Once created the user can check and uncheck the box using the touch feature of the LCD panel without the
running BASIC program being involved. When needed the program can determine the check box value by
using its reference number in the CtrlVal() function:
IF CtrlVal(#10) THEN ..
The # character is optional but serves to remind the programmer that this is not an ordinary number.
In the following commands any arguments that are in italic font (e.g. Width, Height) are optional and if not
specified will take the value of the previous command that did specify them. This means for example, that a
number of radio buttons with the same size and colour can be specified with only the first button having to list
all the details. Note that with the colour specification this is different to the basic drawing commands which
default to the last COLOUR command.
All strings used in GUI controls and the MsgBox can display multiple lines by using the tilde character (~) to
separate each line in the string. For example, a push button's caption can be "ALARM~TEST" and this would
be displayed as two lines. For all controls the font used for the caption will be whatever is set with the FONT
command and the colours will be whatever was set by the last COLOUR command.
If the display is capable of transparent text these commands will allow the use of -1 for the background colour.
This means that the text is drawn over the background with the background image showing through the gaps in
the letters.


The advanced graphics controls are:

Frame
GUI FRAME #ref, caption$, StartX, StartY, Width, Height, Colour
This will draw a frame which is a box with round corners and a caption. A frame does not respond to touch but
is useful when a group of controls need to be visually brought together. It can also be used to surround a group
of radio buttons and MMBasic will arrange for the radio buttons surrounded by the frame to be exclusive – that
is, when one radio button is selected any other button that was selected and within the frame will be deselected.

LED
GUI LED #ref, caption$, CenterX, CenterY, Diameter, Colour
This will draw an indicator light (it looks like a panel mounted LED). When its value is set to one it will be
illuminated and when it is set to zero it will be off (a dull version of its colour attribute). The LED can be made
to flash by setting its value to the number of milliseconds that it should remain on before turning off.
The caption will be drawn to the right of the LED and will use the colours set by the COLOUR command. The
LED control is not animated when touched but its reference number can be found using TOUCH(REF) and
TOUCH(LASTREF) in the touch interrupts and any required animation can be done in MMBasic.

Check Box
GUI CHECKBOX #ref, caption$, StartX, StartY, Size, Colour
This will draw a check box which is a small box with a caption. Both the height and width are specified with
the 'Size' parameter. When touched an X will be drawn inside the box to indicate that this option has been
selected and the control's value will be set to 1. When touched a second time the check mark will be removed
and the control's value will be zero. The caption will be drawn to the right of the Check Box and will use the
colours set by the COLOUR command.

Push Button
GUI BUTTON #ref, caption$, StartX, StartY, Width, Height, FColour, BColour
This will draw a momentary button which is a square switch with the caption on its face. When touched the
visual image of the button will appear to be depressed and the control's value will be 1. When the touch is
removed the value will revert to zero. Caption can be a single string with two captions separated by a vertical
bar (|) character (e.g. "UP|DOWN"). When the button is up the first string will be used and when pressed the
second will be used.

Switch
GUI SWITCH #ref, caption$, StartX, StartY, Width, Height, FColour, BColour
This will draw a latching switch with the caption on its face. When touched the visual image of the button will
appear to be depressed and the control's value will be 1. When touched a second time the switch will be
released and the value will revert to zero. Caption can be a single string with two captions separated by a |
character (e.g. "ON|OFF"). When this is used the switch will appear to be a toggle switch with each half of the
caption used to label each half of the toggle switch.

Radio Button
GUI RADIO #ref, caption$, CenterX, CenterY, Radius, Colour
This will draw a radio button with a caption. When touched the centre of the button will be illuminated to
indicate that this option has been selected and the control's value will be 1. When another radio button is
selected the mark on this button will be removed and its value will be zero. Radio buttons are grouped together
when surrounded by a frame and when one button in the group is selected all others in the group will be
deselected. If a frame is not used all buttons on the screen will be grouped together.
The caption will be drawn to the right of the button and will use the colours set by the COLOUR command.

Display Box
GUI DISPLAYBOX #ref, StartX, StartY, Width, Height, FColour, BColour
This will draw a box with rounded corners. Any string can be displayed in the box by using the CtrlVal(r) =
command. This is useful for displaying text, numbers and messages. This control is not animated when
touched but its reference number can be found using TOUCH(REF) and TOUCH(LASTREF) in the touch
interrupts and any required animation can be done in MMBasic.



Text Box
GUI TEXTBOX #ref, StartX, StartY, Width, Height, FColour, BColour
This will draw a box with rounded corners. When
the box is touched a QWERTY keyboard will
appear on the screen as shown on the right. Using
this virtual keyboard any text can be entered into
the box including upper/lower case letters,
numbers and any other characters in the ASCII
character set. The new text will replace any text
previously in the box.
Ent is the enter key, Can is the cancel key and will
close the text box and return it to its original state,
the triangle is the shift key, the [ ] key will insert a
space and the &12 key will select an alternate key
selection with numbers and special characters
(there are two sets of special characters and the
shift key will switch between them).
The displayed string can be set by assigning a string to the box using the CtrlVal(r) = command. The value of
the control can also be set to a string starting with two hash characters (##) and in that case the string (without
the leading two hash characters) will be displayed in the box with reduced brightness. This can be used to give
the user a hint as to what should be entered (called "ghost text"). Reading the value of the control displaying
ghost text will return an empty string. When a key is pressed the ghost text will vanish and be replaced with the
entered text.
MMBasic will try to position the virtual keyboard on the screen to not obscure the text box that caused it to
appear. A pen down interrupt will be generated just before the keyboard is deployed and a key up interrupt will
be generated when the Enter or Cancel keys are touched and the keyboard is hidden.
If necessary the virtual keyboard can be dismissed by the program (same as touching the cancel button) with
the command: GUI TEXTBOX CANCEL.

Number Box
GUI NUMBERBOX #ref, StartX, StartY, Width, Height, FColour, BColour
This will draw a box with rounded corners. When
the box is touched a numeric keypad will appear
on the screen as shown on the right. Using this
virtual keypad any number can be entered into the
box including a floating point number in exponential format. The new number will replace the
number previously in the box.
The Alt key will select an alternative key selection
and the other special keys are the same as with the
text box.
The displayed number can also be set by assigning
a number (float or integer) to the box using the
CtrlVal(r) = command.
Similar to the Text Box, the value of the control can set to a literal string with two leading hash characters (e.g.
"##Hint") and in that case the string (without the leading two characters) will be displayed in the box with
reduced brightness. Reading this will return zero and when a key is pressed the ghost text will vanish.
MMBasic will try to position the virtual keypad on the screen to not obscure the number box that caused it to
appear. A pen down interrupt will be generated just before the keypad is deployed and a key up interrupt will
be generated when the Enter key is touched and the keypad is hidden. Also, when the Enter key is touched the
entered text will be evaluated as a number and the NUMBERBOX control redrawn to display this number.



Formatted Number Box
GUI FORMATBOX #ref, Format, StartX, StartY, Width, Height, FColour, BColour
This will draw a box with rounded corners. When the box is touched a numeric keypad will appear similar to a
Number Box. The difference is that the Formatted Number Box will require the user to enter numbers
according to a specific format for dates, time, etc. Invalid keys on the keypad will be disabled and the user will
guided in their entry with guide text. This means that the programmer can be assured that the entry made by
the user will always be in a fixed format.
The type of entry is controlled by the 'Format' argument as follows:
DATE1
Date in UK/Aust/NZ format (dd/mm/yy)
DATE2
Date in USA format (mm/dd/yy)
DATE3
Date in international format (yyyy/mm/dd)
TIME1
Time in 24 hour notation (hh:mm)
TIME2
Time in 24 hour notation with seconds (hh:mm:ss)
TIME3
Time in 12 hour notation (hh:mm AM/PM)
TIME4
Time in 12 hour notation with seconds (hh:mm:ss AM/PM)
DATETIME1 Both date (UK fmt) and time (12 hour) (dd/mm/yy hh:mm AM/PM)
DATETIME2 Both date (UK fmt) and time (24 hour) (dd/mm/yy hh:mm)
DATETIME3 Both date (USA fmt) and time (12 hour) (mm/dd/yy hh:mm AM/PM)
DATETIME4 Both date (USA fmt) and time (24 hour) (mm/dd/yy hh:mm)
LAT1
Latitude in degrees, minutes and seconds (d°` mm' ss" N/S)
LAT2
Latitude with seconds to one decimal place (dd° mm' ss.s" N/S)
LONG1
Longitude in degrees, minutes and seconds (ddd° mm' ss" E/W)
LONG2
Longitude with seconds to one decimal place (ddd° mm' ss.s" E/W)
ANGLE1
Angle in degrees and minutes (ddd° mm')
For example:
GUI FORMATBOX #1, DATE1, 300, 150, 200, 50
would create a data entry box and when it is touched a keypad will
appear as shown on the right . Note that:
 The display box is filled with a guide string to prompt the
user as to the data required.
 Because the day of the month can only start with a digit
from 0 to 3 all other keys are disabled. This also happens
with other numbers that have a limited range.
 The value of the control retrieved via CtrlVal(#1) is a string.
As an example, if the user entered the date for the 8th of
May 2020 the returned string would be "08/05/20" (i.e. the
UK/Aust/NZ format as specified by DATE1).
The value of the control can be pulled apart using the string functions or, in some cases, the string can be used
directly. For example, if using the above format box to get a date from the user the PicoMite’s internal clock
could then be directly set as follows:
DATE$ = CtrlVal(#1)

The RTC SETTIME command will accept a single string argument in the format of dd/mm/yy hh:mm so
similarly the RTC time could be set as follows if the formatted box used DATETIME2 for 'Format':
RTC SETTIME CtrlVal(#1)

You can use the USA style DATETIME4 to get the date/time. In that case you would use this to set the RTC:
RTC SETTIME MID$(CtrlVal(#1),4,3) + LEFT$(CtrlVal(#1),2) + RIGHT$((CtrlVal(#1),9)

MMBasic will try to position the virtual keypad on the screen so as to not obscure the format box that caused it
to appear. A pen down interrupt will be generated when the keypad is deployed and a key up interrupt will be
generated when all the required data has been entered and the keypad is hidden.



Spin Box
GUI SPINBOX #ref, StartX, StartY, Width, Height, FColour, BColour, Step,
Minimum, Maximum
This will draw a box with up/down icons on either end. When these icons are touched the number in the box
will be incremented or decremented by the 'StepValue', holding down the touch will repeat at a fast rate.
'Minimum' and 'Maximum' set a limit on the value that can be entered.
'StepValue', 'Minimum' and 'Maximum' are optional and if not specified 'StepValue' will be 1 and there will be
no limit on the number entered. A pen down interrupt will be generated every time up/down is touched or
when automatic repeat occurs.

Caption
GUI CAPTION #ref, text$, StartX, StartY, Alignment, FColour, BColour
This will draw a text string on the screen. It is similar to the basic drawing command TEXT, the difference
being that MMBasic will automatically dim this control if a keyboard or number pad is displayed.
'Alignment' is zero to three characters (a string expression or variable is also allowed) where the first letter is
the horizontal alignment around X and can be L, C or R for LEFT, CENTER, RIGHT and the second letter is
the vertical alignment around Y and can be T, M or B for TOP, MIDDLE, BOTTOM.
A third character can be used to indicate the rotation of the text. This can be 'N' for normal orientation, 'V' for
vertical text with each character under the previous running from top to bottom, 'I' the text will be inverted (i.e.
upside down), 'U' the text will be rotated counter clockwise by 90º and 'D' the text will be rotated clockwise by
90º. The default alignment is left/top with no rotation.
If the colours are not specified this control will use the colours set by the COLOUR command.

Circular Gauge
GUI GAUGE #ref, StartX, StartY, Radius, FColour, BColour, min, max,
nbrdec, units$, c1, ta, c2, tb, c3, tc, c4
This will define a graphical circular analog gauge with a digital display in the centre showing the value and
units. If specified the gauge will be coloured to provide a graphical indication of the signal level (e.g. green for
OK, yellow for warning, etc).
'StartX' and 'StartY' are the coordinates of the centre of the gauge while 'Radius' is
the distance from the centre to the outer edge.
'min' is the value associated with the minimum value of the gauge and 'max' is the
maximum value. When CtrlVal() is used to assign a value (floating point or
integer) to the gauge the analogue portion of the gauge will be drawn to a length
proportional to the range between 'min' and 'max'.
At the same time the digital value will be drawn in the centre of the gauge using the
current font settings (set with the FONT command). 'nbrdec' specifies the number
of decimal places to be used in this display. Under the digital value the 'units$' will
be displayed (this can be skipped or a zero length string used if not required).
Normally the analog graph is drawn using the colour specified in 'Fcolour' however
a multi colour gauge can be created using 'c1' to 'c4' for the colours and 'ta' to 'tc'
for the thresholds used to determine when the colour will change.
Specifically, 'c1' is the colour to be used for values up to 'ta'. 'c2' is the colour to be
used for values between 'ta' and 'tb', 'c3' is used for values between 'tb' and 'tc' and
c4 is used for values above 'tc'. Colours and thresholds not required can be left off
then list. For example, for a two colour gauge only 'c1', 'ta' and 'c2' need to be specified.
When colours and thresholds are specified the background of the gauge will be drawn with a dull version of the
gauge colour at that level ("ghost colouring") so that the user can appreciate how close to the various thresholds
the actual value is. Also the digital value displayed in the centre will also change to the colour specified by the
current value.
If only one colour is required for the whole analogue graph it can be specified by just using 'c1' and leaving all
the following parameters off.



Bar Gauge
GUI BARGAUGE #ref, StartX, StartY, width, height, FColour, BColour, min,
max, c1, ta, c2, tb, c3, tc, c4
This will define either a horizontal or vertical bar gauge. The gauge
can be coloured to provide a graphical indication of the signal level
(e.g. green for OK, yellow for warning, etc) and many bar graphs can
be packed close together so that a number of values can be displayed
simultaneously using a small amount of screen space (as shown in
the image which consists of ten bar gauges).
If the width is less that the height the bar gauge will be drawn
vertically with the analogue graph growing from the bottom towards
the top. Otherwise, if the width is more that the height, it will be
drawn horizontally with the analogue graph growing from the left
towards the right. In both cases 'StartX' and 'StartY' reference the
top left coordinate of the bar graph while 'width' is the horizontal
width and 'height' the vertical height.
The bar graph does not have a digital display of its value but other
than that the parameters are the same as for the circular gauge
(described above).
'min' and 'max' specify the range of values for the bar and, if specified, 'c1' to 'c4' and 'ta' to 'tc' specify the
colours and thresholds for the analogue bar image. Note that unlike the circular bar gauge a "ghost image" of
the colours is not shown in the background.
As with the circular gauge, if only one colour is required for the whole gauge it can be specified by just using
'c1' and leaving all the following parameters off.

Area
GUI AREA #ref, StartX, StartY, Width, Height
This will define an invisible area of the screen that is sensitive to touch and will set TOUCH(REF) and
TOUCH(LASTREF) accordingly when touched or released. It can be used as the basis for creating a custom
control which is defined and managed by the BASIC program.

Interacting with Controls
Using the following commands and functions the characteristics of the on screen controls can be changed and
their value retrieved.


= CTRLVAL(#ref)
This is a function that will return the current value of a control. For controls like check boxes or switches it
will be the number one (true) indicating that the control has been selected by the user or zero (false) if not.
For controls that hold a number (e.g. a SPINBOX) the value will be the number (normally a floating point
number). For controls that hold a string (e.g. TEXTBOX) the value will be a string. For example:
PRINT "The number in the spin box is: " CTRLVAL(#10)



CTRLVAL(#ref) =
This command will set the value of a control. For off/on controls like check boxes it will override any
touch input and can be used to depress/release switches, tick/untick check boxes, etc. A value of zero is off
or unchecked and non zero will turn the control on. For a LED it will cause the LED to be illuminated or
turned off. It can also be used to set the initial value of spin boxes, text boxes, etc. For example:
CTRLVAL(#10) = 12.4



GUI FCOLOUR colour, #ref1 [, #ref2, #ref3, etc]
This will change the foreground colour of the specified controls to 'colour'. This is especially handy for a
LED which can change colour.



GUI BCOLOUR colour, #ref1 [, #ref2, #ref3, etc]
This will change the background colour of the specified controls to 'colour'.



= TOUCH(REF)
This is a function that will return the reference number of the control currently being touched. If no control
is currently being touched it will return zero.





= TOUCH(LASTREF)
This is a function that will return the reference number of the control that was last touched.



GUI DISABLE #ref1 [, #ref2, #ref3, etc]
This will disable the controls in the list. Disabled controls do not respond to touch and will be displayed
dimmed. The keyword ALL can be used as the argument and that will disable all controls on the currently
displayed page. For example:
GUI DISABLE ALL



GUI ENABLE #ref1 [, #ref2, #ref3, etc]
This will undo the effects of GUI DISABLE and restore the controls in the list to normal operation. The
keyword ALL can be used as the argument for all controls on the currently displayed page.



GUI HIDE #ref1 [, #ref2, #ref3, etc]
This will hide the controls in the list. Hidden controls will not respond to touch and will be replaced on the
screen with the current background colour. The keyword ALL can be used as the argument.



GUI SHOW #ref1 [, #ref2, #ref3, etc]
This will undo the effects of GUI HIDE and restore the controls in the list to being visible and capable of
normal operation. The keyword ALL can be used as the argument for all controls.



GUI DELETE #ref1 [, #ref2, #ref3, etc]
This will delete the controls in the list. This includes removing the image of the control from the screen
using the current background colour and freeing the memory used by the control. The keyword ALL can
be used as the argument and that will cause all controls to be deleted.

MsgBox()
The MsgBox() function will display a message box on the screen and wait for user input. While the message
box is displayed all controls will be disabled so that the message box has the complete focus.
The syntax is:
r = MsgBox(message$, button1$ [, button2$ [, button3$ [, button4$]]])
All arguments are strings. 'message$' is the message to display. This can contain one or more tilde characters
(~) which indicate a line break. Up to 10 lines can be displayed inside the box. 'button1$' is the caption for the
first button, 'button2$' is the caption for the second button, etc. At least one button must be specified and four
is the maximum. Any buttons not included in the argument list will not be displayed.
The font used will be the default font set using the FONT command and the colours used will be the defaults
set by the COLOUR command. The box will be automatically sized taking into account the dimensions of the
default font, the number of lines to display and the number of buttons specified.
When the user touches a button the message box will erase itself, restore the display (e.g. re enable all controls)
and return the number of the button that was touched (the first button will return 1, the second 2, etc). Note
that, unlike all other GUI controls the BASIC program will stop running while the message box is displayed,
interrupts however will be honoured and acted upon.
To illustrate the usage of a message box will the following program fragment will attempt to open a file and if
an error occurs the program will display an error message using the MsgBox() function. The message has two
lines and the box has two buttons for retry and cancel.
Do
On Error Skip
Open "file.txt" For Input As #1
If MM.ErrNo <> 0 Then
if MsgBox("Error~Opening file.txt","RETRY","CANCEL") = 2 Then Exit Sub
EndIf
Loop While MM.ErrNo <> 0



This would be the result if the file "file.txt" did not exist:



Advanced Graphics Programming Techniques
When programming using the advanced GUI commands there are a number of hints and techniques to consider
that will make it easier to develop and maintain your program.

The User Should Be In Control
Traditional character based programs are normally in control of the interaction with the user. For example, the
program may display a menu and prompt the user to select an action. If the user selects an invalid option the
program would display an error message and display the menu options again.
However graphical based programs such as that created using the advanced GUI commands are different.
Usually the program just starts running doing what it normally does (e.g. control temperature, speed, etc) and it
is the user's job to select and change parameters without being prompted. This is a different way of
programming and is often hard for the traditional programmer to get used to this different technique.
As an example, consider a program that is to control a cutting device. The traditional program would prompt
the user for the speed and cutting time. When both have been entered the program would prompt to start the
cutting cycle. However, a graphical based program would display two number boxes where the user could
enter the speed and time along with a run button. The number boxes could be filled with default values and the
run button would be disabled if the user entered an invalid speed or time. When the run button is touched the
cutting cycle would start.
A good example of this type of graphical interface is the dialogue box used on a Windows/IOS/Android
computer to set the time and date. It displays a number of boxes where the user can enter the date/time along
with an OK button that tells the program to accept the data entered. At no time is the user forced to make a
selection from a menu. Also, the current time/date is already displayed in the entry boxes so the user can
accept them as the default if they wanted to do so.
If you need some inspiration as to how your graphical program should look and feel check your nearest GUI
based operating system to see how they operate.

Program Structure
Typically a program would start by defining the controls (which MMBasic will draw on the screen), then it
would set the defaults and finally it would drop into a continuous loop where it would do whatever job it was
design to do. For example, take the case of a simple controller for a motor where the user could select the
speed and cause the motor to run by pressing an on screen button.
To implement this function the program would look something like this:
GUI CAPTION #1, "Speed (rpm)", 200, 50
GUI NUMBERBOX #2, 200, 100, 150, 40
CtrlVal(#2) = 100
GUI BUTTON #3, "RUN", 200, 350, 0, RGB(red)

' label the number box
' define and draw the number box
' default value for the speed
' define and draw the RUN button

DO
IF CtrlVal(#3)<10 OR CtrlVal(#3)>200 THEN
GUI DISABLE #3
ELSE
GUI ENABLE #3
ENDIF

' this runs in a loop forever
' check the speed setting
' disable RUN if it is invalid
' otherwise
' enable the RUN button

IF CtrlVal(#3) = 1 THEN
SetMotorSpeed CtrlVal(#2)
ELSE
SetMotorSpeed 0
ENDIF
LOOP

' if the button is pressed
' make the motor run
' otherwise the button is up
' therefore set motor speed to zero

Note that the user is not prompted to do anything; the program just sits in a loop reacting to the changes that the
user has made to the controls (i.e. the user is in control).

Disable Invalid Controls
As in the above example, disabling a control will prevent a user from using it and MMBasic will redraw it in a
dull colour to indicate that it is not available. This is the equivalent of an error message in a traditional text



based program and is more user friendly than popping up a message box which must be dismissed before
anything else can be done.
There are many times that a control could be invalid, for example when an input is not ready or simply when an
option or action does not apply. Later, when the control becomes valid you can use the GUI ENABLE
command to return it to use. Another example is when a GUI NUMBERBOX keypad is displayed MMBasic
will automatically disable all other controls on the screen so that it is obvious to the user where their input is
required.
Disabling a control still leaves it on the screen, so that the user knows that it is there but it will be dimmed and
will not respond to touch. Not responding to touch also means that the user cannot change it and an interrupt
will not be generated when it is touched. This is handy for you the programmer because you do not have to
check if the control is valid before acting on it.

Use Constants for Control Reference Numbers
The advanced controls use a reference number to identify the control. To make it easy to read and maintain
your program you should define these numbers as constants with easy to recognise names.
For example, in the following program fragment MAIN_SWITCH is defined as a constant and this constant is
used wherever the reference number for that control is required:
CONST MAIN_SWITCH = 5
CONST ALARM_LED = 6
'…
GUI SWITCH MAIN_SWITCH, "ON|OFF", 330, 50, 140, 50, RGB(white), RGB(blue)
GUI LED ALARM_LED, 215, 220,30, RGB(red)
'…
IF CtrlVal(MAIN_SWITCH) = 0 THEN …
' for example turn the pump off
IF ALARM THEN CtrlVal(ALARM_LED) = 1

It is much easier to remember what MAIN_SWITCH does than remembering what control the number 5 refers
to. Also, when you have a lot of controls it is much easier to renumber the controls when all their numbers are
defined at the one place at the start of the program.
The reference number must be a number between 1 and the value set with the OPTION CONTROL command.
Increasing this number will consume more RAM and decreasing it will recover some RAM.

The Main Program Is Still Running
It is important to realise that your main BASIC program is still running while the user is interacting with the
GUI controls. For example, it will continue running even while a user holds down an on screen switch and it
will keep running while the virtual keyboard is displayed as a result of touching a TEXTBOX control.
For this reason your main program should not arbitrarily update touch sensitive screen controls, because they
might change the on screen image while the user is using them (with undefined results). Normally when a
BASIC program using GUI controls starts it will initialise controls such as a SPINBOX, NUMBERBOX and
TEXTBOX to some initial value but from then on the main program should just read the value of these
controls – it is the responsibility of the user to change these, not your program.
However, if you do want to change the value of such an on-screen control you need some mechanism to
prevent both the program and the user making a change at the same time. One method is to set a flag within the
key down interrupt to indicate that the control should not be updated during this time. This flag can then be
cleared in the key up interrupt to allow the main program to resume updating the control.
Note that this discussion only applies to controls that respond to touch. Controls such as CAPTION and LED
can be changed at any time by the main program and often are.

Use Interrupts and SELECT CASE Statements
Everything that happens on a screen using the advanced controls will be signalled by an interrupt, either touch
down or touch up. So, if you want to do something immediately when a control is changed, you should do it in
an interrupt. Mostly you will be interested in when the touch (or pen) is down but in some cases you might also
want to know when it is released.
Because the interrupt is triggered when the pen touches any control or part of the screen you need to discover
what control was being touched. This is best performed using the TOUCH(REF) function and the SELECT
CASE statement.
For example, in the following fragment the subroutine PenDown will be called when there is a touch and the
function TOUCH(REF) will return the reference number of the control being touched. Using the SELECT



CASE the alarm LED will be turned on or off depending on which button is touched. The action could be any
number of things like raising an I/O pin to turn on a physical siren or printing a message on the console.
CONST ALARM_ON = 15
CONST ALARM_OFF = 16
CONST ALARM_LED = 33
GUI INTERRUPT PenDown
'…
GUI BUTTON ALARM_ON, "ALARM ON ", 330, 50, 140, 50, RGB(white), RGB(blue)
GUI BUTTON ALARM_OFF, "ALARM OFF ", 330, 150, 140, 50, RGB(white), RGB(blue)
GUI LED ALARM_LED, 215, 220, 30, RGB(red)
'…
DO : LOOP
' the main program is doing something
' this sub is called when touch is detected
SUB PenDown
SELECT CASE TOUCH(REF)
CASE ALARM_ON
CtrlVal(ALARM_LED) = 1
CASE ALARM_OFF
CtrlVal(ALARM_LED) = 0
END SELECT
END SUB

The SELECT CASE can also test for other controls and perform whatever actions are required for them in their
own section of the CASE statement.
The important point is that the maintenance of the controls (e.g. responding to the buttons and turning the alarm
LED off or on) is done automatically without the main program being involved – it can continue doing
something useful like calculating some control response, etc.

Touch Up Interrupt
In most cases you can process all user input in the touch down interrupt. But there are exceptions and a typical
example is when you need to change the characteristics of the control that is being touched. For example, if
you wanted to change the foreground colour of a button from white to red when it is down. When it is returned
to the up state the colour should revert to white.
Setting the colour on the touch down is easy. Just define a touch down interrupt and change the colour in the
interrupt when that control is touched. However, to return the colour to white you need to detect when the
touch has been removed from the control (i.e. touch up). This can be done with a touch up interrupt.
To specify a touch up interrupt you add the name of the subroutine for this interrupt to the end of the GUI
INTERRUPT command. For example:
GUI INTERRUPT IntTouchDown, IntTouchUp

Within the touch up subroutine you can use the same structure as in the touch down sub but you need to find
the reference number of the last control that was touched. This is because the touch has already left the screen
and no control is currently being touched. To get the number of the last control touched you need to use the
function TOUCH(LASTREF)
The following example shows how you could meet the above requirement and implement both a touch down
and a touch up interrupt:
SUB IntTouchDown
SELECT CASE TOUCH(REF)
CASE ButtonRef
GUI FCOLOUR RGB(RED), ButtonRef
END SELECT
END SUB
SUB IntTouchUp
SELECT CASE TOUCH(LASTREF)
CASE ButtonRef
GUI FCOLOUR RGB(WHITE), ButtonRef
END SELECT
END SUB



Keep Interrupts Very Short
Because a touch interrupt indicates a request by the user it is tempting to do some extensive programming
within an interrupt. For example, if the touch indicates that the user wants to send a message to another
controller it sounds logical to put all that code within the interrupt. But this is not a good idea because
MMBasic cannot do anything else while your program is processing the interrupt and sending a message could
take many milliseconds.
Instead your program should update a global variable to indicate what is requested and leave the actual
execution to the main program. For example, if the user did touch the "send a message" button your program
could simply set a global variable to true. Then the main program can monitor this variable and if it changes
perform the logic and communications required to satisfy the request.
Remember the commandment "Thou shalt not hang around in an interrupt”.

Multiple Screens
Your program might need a number of screens with differing controls on each screen. This could be
implemented by deleting the old controls and creating new ones when the screen is switched. But another way
to do this is to use the GUI SETUP and GUI PAGE commands. These allow you to organise the controls onto
pages and with one simple command you can switch pages. All controls on the old page will be automatically
hidden and controls on the new page will be automatically shown.
To allocate controls to a page you use the GUI SETUP nn command where nn refers to the page in the range of
1 to 32. When you have used this command any newly created controls will be assigned to that page. You can
use GUI SETUP as many times that you want. For example, in the program fragment below the first two
controls will be assigned to page 1, the second to page 2, etc.
GUI SETUP 1
GUI Caption #1, "Flow Rate", 20, 170,, RGB(brown),0
GUI Displaybox #2, 20, 200, 150, 45
GUI SETUP 2
GUI Caption #3, "High:", 232, 260, LT, RGB(yellow)
GUI Numberbox #4, 318, 6,90, 12, RGB(yellow), RGB(64,64,64)
GUI SETUP 3
GUI Checkbox #5, "Alarms", 500, 285, 25
GUI Checkbox #6, "Warnings", 500, 325, 25

By default only the controls setup as page 1 will be displayed and the others will be hidden.
To switch the screen to page 3 all you need do is use the command GUI PAGE 3. This will cause controls #1
and #2 to be automatically hidden and controls #5 and #6 to be displayed. Similarly GUI PAGE 2 will hide all
except #3 and #4 which will be displayed.
You can specify multiple pages to display at the one time, for example, GUI PAGE 1,3 will display both pages 1
and 3 while hiding page 2. This can be useful if you have a set of controls that must be visible all the time. For
example, GUI PAGE 1,2 and GUI PAGE 1,3 will leave the controls on page 1 visible while the others are
switched on and off.
It is perfectly legal for a program to modify controls on other pages even though they are not displayed at the
time. This includes changing the value and colours as well as disabling or hiding them. When the display is
switched to their page the controls will be displayed with their new attributes.
It is possible to place the GUI PAGE commands in the touch down interrupt so that pressing a certain control or
part of the screen will switch to another page.
Note that when ALL is used for the list of controls in commands such as GUI ENABLE ALL this only refers to
the controls on the pages that are currently selected for display. Controls on other pages will be unaffected.
All programs start with the equivalent of the commands GUI SETUP 1 and GUI PAGE 1 in force. This means
that if the GUI SETUP and GUI PAGE commands are not used the program will run as you would expect with
all controls displayed.
A typical usage of the GUI PAGE command is shown below.



Two buttons (which are always displayed) allow the user to select between the first page and the second page.
The switch is done in the touch down interrupt.
GUI SETUP 1
GUI Button #10, "SELECT PAGE ONE", 50, 100, 150, 30, RGB(yellow), RGB(blue)
GUI Button #11, "SELECT PAGE TWO", 50, 140, 150, 30, RGB(yellow), RGB(blue)
GUI SETUP 2
GUI Caption #1, "Displaying First Page", 20, 20
GUI SETUP 3
GUI Caption #2, "Displaying Second Page", 20, 50
GUI INTERRUPT TouchDown
Do
' the main program loop
Loop
Sub TouchDown
If Touch(REF) = 10 Then GUI Page 1, 2
If Touch(REF) = 11 Then GUI Page 1, 3
End Sub

Multiple Interrupts
With many screen pages the interrupt subroutine could get long and complicated. To work around that it is
possible to have multiple interrupt subroutines and switch dynamically between them as you wish (normally
after switching pages). This is done by redefining the current interrupt routines using the GUI INTERRUPT
command.
For example, this program fragment uses different interrupt routines for pages 4 and 5 and they are specified
immediately after switching the pages.
GUI PAGE 4
GUI INTERRUPT P4keydown, P4keyup
..
GUI PAGE 5
GUI INTERRUPT P5keydown, P5keyup
..

Using Basic Drawing Commands
There are two types of objects that can be on the screen. These are the GUI controls and the basic drawing
objects (PIXEL, LINE, TEXT, etc). Mixing the two on the screen is not a good idea because MMBasic does
not track the position of the basic drawing objects and they can clash with the GUI controls.
As a result, unless you are prepared to do some extra programming, you should use either the GUI controls or
the basic drawing objects – but you should not use both. So, for example, do not use TEXT but use GUI
CAPTION instead. If you only use GUI controls MMBasic will manage the screen for you including erasing
and redrawing it as required, for example when a virtual keyboard is displayed.
Note that the CLS command (used to clear the screen) will automatically set any GUI controls on the screen to
hidden (i.e. it does a GUI HIDE ALL before clearing the screen).
The main problem with mixing basic graphics and GUI controls occurs with the Text Box, Formatted Box and
Number Box controls which display a virtual keyboard. This can erase any basic graphics and MMBasic will
not know to restore them when the keyboard is removed. If you want to mix basic graphics with GUI controls
you should:
 Intercept the touch down interrupt for the Text Box, Formatted Box and Number Box controls as that
indicates that a virtual keyboard is about to be displayed and that will give you the opportunity to redraw
your non GUI basic graphics in anticipation of this event (for example, draw them in a dimmed state to
appear as if they are disabled).
 Intercept the touch up interrupt for the same controls as that indicates that the virtual keyboard has been
removed and you could then redraw any non GUI graphics in their original state.



Overlapping Controls
Controls can be defined to overlap on the display, this mostly occurs with GUI AREA which, as an example,
you might want to capture a touch that was intended for (say) a GUI BUTTON. This will allow you to create
your own animation for the button rather than that provided by MMBasic. In this case the control that you wish
to respond to the touch (i.e. GUI AREA) should have a lower reference number (i.e. #ref) than the control that
it is covering (i.e. the GUI BUTTON). This is because when the screen is touched MMBasic will check the
current list of active controls starting with control number 1 and working upwards. When a match is made
MMBasic will take the appropriate action and terminate the search. This results in the lower numbered control
effectively masking out a higher numbered control covering the same screen area as the touched location.



MMBasic Characteristics
Naming Conventions
Command names, function names, labels, variable names, etc are not case sensitive, so that "Run" and "RUN"
are equivalent and "dOO" and "Doo" refer to the same variable.
The type of a variable can be specified in the DIM command or by adding a suffix to the end of the variable's
name. For example the suffix for an integer is '%' so if a variable called nbr% is automatically created it will be
an integer. There are three types of variables:
1. Floating point. These can store a number with a decimal point and fraction (e.g. 45.386) and also very
large numbers. However, they will lose accuracy when more than 14 significant digits are stored or
manipulated. The suffix is '!' and floating point is the default when a variable is created without a suffix
2. 64-bit integer. These can store numbers with up to 19 decimal digits without losing accuracy but they
cannot store fractions (i.e. the part following the decimal point). The suffix for an integer is '%'
3. Strings. These will store a string of characters (e.g. "Tom"). The suffix for a string is the '$' symbol
(e.g. name$, s$, etc) Strings can be up to 255 characters long.
Variable names and labels can start with an alphabetic character or underscore and can contain any alphabetic
or numeric character, the period (.) and the underscore (_). They may be up to 31 characters long. A variable
name or a label must not be the same as a command or a function or one of the following keywords: THEN,
ELSE, TO, STEP, FOR, WHILE, UNTIL, MOD, NOT, AND, OR, XOR, AS. E.g. step = 5 is illegal.
For file names see the section “MMBasic Support for Flash and SD Card Filesystems”

Constants
Numeric constants may begin with a numeric digit (0-9) for a decimal constant, &H for a hexadecimal
constant, &O for an octal constant or &B for a binary constant. For example &B1000 is the same as the
decimal constant 8. Constants that start with &H, &O or &B are always treated as 64-bit integer constants.
Decimal constants may be preceded with a minus (-) or plus (+) and may be terminated with 'E' followed by an
exponent number to denote exponential notation. For example 1.6E+4 is the same as 16000.
If the decimal constant contains a decimal point or an exponent, it will be treated as a floating point constant;
otherwise it will be treated as a 64-bit integer constant.
String constants are surrounded by double quote marks ("). E.g. "Hello World".

Implementation Characteristics
Maximum program size (as plain text) is 160KB. Note that MMBasic tokenises the program when it is stored
in flash so the final size in flash might vary from the plain text size.
Maximum length of a command line is 255 characters.
Maximum length of a variable name or a label is 31 characters.
Maximum number of dimensions to an array is 6.
Maximum number of arguments to commands that accept a variable number of arguments is 50.
Maximum number of nested FOR…NEXT loops is 20.
Maximum number of nested DO…LOOP commands is 20.
Maximum number of nested GOSUBs, subroutines and functions (combined) is 320.
Maximum number of nested multiline IF…ELSE…ENDIF commands is 20.
Maximum number of user defined labels, subroutines and functions (combined): 224
Maximum number of interrupt pins that can be configured: 10
Numbers are stored and manipulated as double precision floating point numbers or 64-bit signed integers. The
range of floating point numbers is 1.797693134862316e+308 to 2.225073858507201e-308.
The range of 64-bit integers (whole numbers) that can be manipulated is ± 9223372036854775807.
Maximum string length is 255 characters.
Maximum line number is 65000.
Maximum number of background pulses launched by the PULSE command is 5.
Maximum number of global variables and constants is 256
Maximum number of local variables is 256
The maximum number of files that can be listed by the FILES command is 1000



The maximum length filename supported is 63 characters

Compatibility
MMBasic implements a large subset of Microsoft’s GW-BASIC. There are numerous differences due to
physical and practical considerations but most standard BASIC commands and functions are essentially the
same. An online manual for GW-BASIC is available at http://www.antonis.de/qbebooks/gwbasman/index.html
and this provides a more detailed description of the commands and functions.
MMBasic also implements a number of modern programming structures documented in the ANSI Standard for
Full BASIC (X3.113-1987) or ISO/IEC 10279:1991. These include SUB/END SUB, the DO WHILE …
LOOP, the SELECT…CASE statements and structured IF . THEN … ELSE … ENDIF statements.



Predefined Read Only Variables
Detailed Listing
These variables are set by MMBasic and cannot be changed by the running program. Note that they do not do
anything on their own, they must be printed or assigned to a variable.
For example:
> PRINT MM.VER
5.0707
>
or, in a program:
If MM.VER < 5.0707 Then Error("Needs version 5.07.07 or greater")

MM.VER

The version number of the firmware as a floating point number in the form
aa.bbcc where aa is the major version number, bb is the minor version
number and cc is the revision number. For example version 5.03.00 will
return 5.03 and version 5.03.01 will return 5.0301.

MM.CMDLINE$

This constant variable containing any command line arguments passed to the
current program is automatically created when an MMBasic program runs;
see RUN and * commands for details.
•
Programs run from the Editor or using OPTION AUTORUN will set
MM.CMDLINE$ to the empty string.
•
If not required this constant variable may be removed from memory
using ERASE MM.CMDLINE$

MM.DEVICE$

A string representing the device or platform that MMBasic is running on.
Currently this variable will contain one of the following:
"Maximite" on the standard Maximite and compatibles.
"Colour Maximite" on the Colour Maximite and UBW32.
"Colour Maximite 2" on the Colour Maximite 2.
"DuinoMite" when running on one of the DuinoMite family.
"DOS" when running on Windows in a DOS box.
"Generic PIC32" for the generic version of MMBasic on a PIC32.
"Micromite" on the PIC32MX150/250
"Micromite MkII" on the PIC32MX170/270
"Micromite Plus" on the PIC32MX470
"Micromite Extreme" on the PIC32MZ series
"ARMmite H7" on the ArmmiteH7
"ARMmite F407" on the ArmmiteF4
"ARMmite L4" with chip no. and pin count appended on the ArmmiteL4
“PicoMite” on the Raspberry Pi Pico
“WebMite” on the Raspberry Pi Pico W
"PicoMiteVGA" on the Raspberry Pi Pico VGA Edition
“MMBasic for Windows” on the Windows version

MM.ERRNO
MM.ERRMSG$

If a statement caused an error which was ignored these variables will be set
accordingly. MM.ERRNO is a number where non zero means that there was
an error and MM.ERRMSG$ is a string representing the error message that
would have normally been displayed on the console. They are reset to zero
and an empty string by RUN, ON ERROR IGNORE or ON ERROR SKIP.

MM.INFO()
MM.INFO$()

These two versions can be used interchangeably but good programming
practice would require that you use the one corresponding to the returned
datatype.



MM.INFO$(AUTORUN)
MM.INFO(ADC)

Returns the setting of the OPTION AUTORUN command
Returns the number of the buffer currently ready to read when using ADC
RUN (1 or 2). Returns 0 if nothing ready.

MM.INFO(ADC DMA)

Returns true (1) if the ADC DMA is active.

MM.INFO(BOOT COUNT)

MM.INFO$(CPUSPEED)

Returns the number of times the Pico has been restarted since the flash drive
was last formatted
.
Returns the CPU speed as a string.

MM.INFO$(LCDPANEL)

Returns the name of the configured LCD panel or a blank string.

MM.INFO$(SDCARD)

Returns the status of the SD Card. Valid returns are:
DISABLED, NOT PRESENT, READY, and UNUSED

MM.INFO$(CURRENT)

Returns the name of the current program or NONE if called after a NEW or
EDIT Command.

MM.INFO(PATH)

Returns the path of the current program or NONE if called after a NEW or
EDIT Command.

MM.INFO(DISK SIZE)

Returns the capacity of the Flash Filesystem or SD Card, whichever is the
active drive, in bytes
.
Returns 1 if the file specified exists, returns -1 if fname$ is a directory,
otherwise returns 0.

MM.INFO(EXISTS FILE
fname$)
MM.INFO(EXISTS DIR
dirname$)

Returns a Boolean indicating whether the directory specified exits.

MM.INFO(FREE SPACE)

Returns the free space on the Flash Filesystem or SD Card whichever is the
active drive.

MM.INFO(FILESIZE file$)

Returns the size of file$ in bytes or -1 if not found, -2 if a directory.

MM.INFO$(MODIFIED file$)

Returns the date/time that file$ was modified, Empty string if not found.

MM.INFO(FCOLOUR)

Returns the current foreground colour.

MM.INFO(BCOLOUR)

Returns the current background colour.

MM.INFO(FONT)

Returns the number of the currently active font.

MM.INFO(FONT ADDRESS
n)

Returns the address of the memory location with the address of FONT n .

MM.INFO(FONT POINTER n)

Returns a POINTER to the start of FONT n in memory.

MM.INFO(FONTHEIGHT)
MM.INFO(FONTWIDTH)

Integers representing the height and width of the current font (in pixels).

MM.INFO(FLASH)

Reports which flash slot the program was loaded from if applicable.

MM.INFO(FLASH ADDRESS
n)

Returns the address of the flash slot n.

MM.INFO(HEAP)

Returns the amount of MMbasic Heap memory free. MMBasic heap is used
for strings, arrays and various other temporary and permanent buffers (e.g.



audio)
MM.INFO(HPOS)
MM.INFO(VPOS)

The current horizontal and vertical position (in pixels) following the last
graphics or print command.

MM.INFO(ID)

Returns the unique ID of the Pico.

MM.INFO(OPTION option)

Returns the current value of a range of options that affect how a program
will run. “option” can be one of AUTORUN, BASE, BREAK,
DEFAULT, EXPLICIT, KEYBOARD, ANGLE, HEIGHT, WIDTH,
FLASH SIZE

MM.INFO$(PIN pinno)

Returns the status of I/O pin 'pinno'. Valid returns are:
INVALID, RESERVED, IN USE, and UNUSED

MM.INFO(PINNO GPnn)

Returns the physical pin number for a given GP number. GPnn can be an
unquoted string (GP01), a string literal(“GP01”) or a string variable. Ie,
A$=”GP01”: MM.INFO(PINNO A$) .

MM.INFO$(PLATFORM)

Returns the string previously set with OPTION PLATFORM.

MM.INFO(PS2)

Reports the last raw message received on the PS2 interface if enabled.

MM.INFO$(SOUND)

Returns the current activity on the audio output (OFF, PAUSED, TONE,
WAV, FLAC, SOUND)

MM.INFO(STACK)

Returns the C stack pointer. Complex or recursive Basic code may result in
the error "Stack overflow, expression too complex at depth %" This will
occur when the stack is below &H 2003f800. Monitoring the stack will
allow the programmer to identify simplifications to the Basic code to avoid
the error.

MM.INFO(SYSTEM HEAP)

Returns the free space on the System Heap.

MM.INFO(TRACK)

Returns the name of the FLAC, MP3, WAV or MIDI file currently playing
on the audio output
.
Returns the status of the Touch controller. Valid returns are:
“Disabled”, “Not calibrated”, and “Ready”.

MM.INFO$(TOUCH)

MM.INFO(VARCNT)

Returns the number of variables in use in the MMBasic program.

MM.INFO$(LINE)

Returns the current line number as a string. LIBRARY returned if in the
Library and UNKNOWN if not in a program. Assists in diagnostics while
unit testing.

MM.INFO(UPTIME)

Returns the time in seconds since booted as a floating point number.

MM.INFO(VERSION)

Returns the version number as a floating point number.

MM.INFO(WRITEBUFF)

Returns the address in memory of the current buffer used for drawing
commands.



MM.HRES
MM.VRES

Integers representing the horizontal and vertical resolution of the LCD
display panel (if configured) in pixels.

MM.FONTHEIGHT
MM.FONTWIDTH

Integers representing the height and width of the current font (in pixels) kept
for compatibility. NB: these are automatically converted into
MM.INFO(FONTHEIGHT) and MM.INFO(FONTWIDTH) by MMBasic.

MM.ONEWIRE

Following a 1-Wire reset function this integer variable will be set to indicate
the result of the operation: 0 = Device not found, 1 = Device found.

MM.I2C

Following an I2C write or read command this integer variable will be set to
indicate the result of the operation as follows:
0 = The command completed without error.
1 = Received a NACK response
2 = Command timed out

MM.WATCHDOG

An integer which is true if MMBasic was restarted as the result of a
Watchdog timeout (see the WATCHDOG command) otherwise false.



Options
Detailed Listing
This table lists the various option commands which can be used to configure MMBasic and change the way it
operates. Options that are marked as permanent will be saved in non-volatile memory and automatically
restored when the PicoMite is restarted. Options that are not permanent will be reset on start-up.
Many OPTION commands will force a restart of the PicoMite and that will cause the USB console interface to be
reset. The program in memory will not be lost as it is held in non-volatile flash memory.
Permanent?
OPTION DISK SAVE fname$
OPTION DISK LOAD fname$

commands let the user save and restore the complete set of
 These
options defined to and from a disk file. The file could then be transferred
to a host computer using XMODEM allowing additional PicoMites to be
easily configured or options recovered after a firmware upgrade

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

OPTION AUTOREFRESH
OFF | ON


‘PWMnApin’ is the left audio channel, ‘PWMnBpin’ is the right. Both
pins must belong to the same audio channel.
Example, OPTION AUDIO GP18, GP19 would use PWM1A and
PWM1B on pins 24 and 25 respectively.
This option prevents use of these pins in the BASIC program.
The audio output is generated using PWM so a low pass filter is
necessary on the output. The audio output from the PicoMite is very
noisy. Using OPTION POWER and/or supplying power via a separate
3.3V linear regulator can reduce this.
This command must be run at the command prompt (not in a program).

connected to GND.

supported and also supports real-time MIDI output. See the PLAY
command for more details

Black and white displays can only be updated a full screen at a time. By
using OPTION AUTOREFRESH OFF/ON you can control whether a
write command immediately updates the display or not. If
AUTOREFRESH is OFF the REFRESH command can be used to
trigger the write. This applies to the following displays: N5110,
SSD1306I2C, SSD1306I2C32, SSD1306SPI, ST7920


OPTION AUTORUN ON
[,NORESET]
or
OPTION AUTORUN n
[,NORESET]
or
OPTION AUTORUN OFF

MMBasic to automatically run a program on power up or
 Instructs
restart.
ON will cause the the current program to be run.
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
The value of the break key is set to CTRL-C key at power up but it can be
changed to any keyboard key using this command (for example, OPTION
BREAK 4 will set the break key to the CTRL-D key). Setting this option
to zero will disable the break function entirely.

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

OPTION CPUSPEED speed

 Change the CPU clock.

The keyword COLORCODE (USA spelling) can also be used.
This requires a terminal emulator that can interpret the appropriate
escape codes (eg, Tera Term). This command must be run at the
command prompt (not in a program).

‘speed’ is the CPU clock in KHz in the range of 48000 to 378000. Speeds
above 133MHz are regarded as overclocking as that is the specified
maximum speed of the standard Raspberry Pi Pico.
With no option set the CPU speed will default to 133000. This command
must be run at the command prompt (not in a program).

OPTION COUNT pin1, pin2,
pin3, pin4

which pins are to be used as Count inputs. By default these are
 Specifies
GP6, GP7, GP8 and GP9. The SETPIN command defines the Counter
mode.
This command must be run at the command prompt (not in a program).



OPTION DEFAULT FLOAT |
INTEGER | STRING | NONE

OPTION DISPLAY lines
[,chars]

Used to set the default type for a variable which is not explicitly defined.
If OPTION DEFAULT NONE is used then all variables must have their
type explicitly defined or the error “Variable type not specified” will
occur.
When a program is run the default is set to FLOAT for compatibility with
Microsoft BASIC and previous versions of MMBasic.
Set the characteristics of the display terminal used for the console. Both

 the LIST and EDIT commands need to know this information to

correctly format the text for display.
'lines' is the number of lines on the display and 'chars' is the width of the
display in characters. The default is 24 lines x 80 chars and when
changed this option will be remembered even when the power is
removed. Maximum values are 100 lines and 240chars.
This command is not available if the display is being used as a
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
ON/OFFF

When using the PLAY SOUND command, changes to sounds, volumes,
or frequencies can cause audible clicks in the output. The firmware
attempts to mitigate this by ramping the volume down on the channel’s
previous output before changing the output and ramping it back up
again. This significantly improves the audio output but at the expense of
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
OPTION GUI CONTROLS
NbrOfGUIControls

 Specifies the maximum number of GUI controls that can be defined.

OPTION HEARTBEAT
ON/OFF

 Enables or disables the output of the heartbeat on GP25


Each control uses 52 bytes and the total memory used must be rounded up
to the next 2048 byte multiple. For example, specifying 70 controls will
use 4KB of RAM.
By default the number of GUI controls is set to zero so this option must
be used before any GUI controls are defined.


OPTION KEYBOARD nn
[,capslock] [,numlock]
[repeatstart] [repeatrate]

a PS2 keyboard. This can be used for console input and any
 Configure
characters typed will be available via any commands that read from the

OPTION KEYBOARD I2C

support for the Solderparty bbq20 mini I2C keyboard. Note:
 Configures
OPTION SYSTEM I2C must be set before executing this command

OPTION LCDPANEL
VIRTUAL_C
or
OPTION LCDPANEL
VIRTUAL_M

 Configures a virtual LCD panel without a physically connected panel.

OPTION LCDPANEL options
or
OPTION LCDPANEL
DISABLE

 Configures the PicoMite to work with an attached LCD panel.

OPTION LCDPANEL
CONSOLE [font [, fc [,bc ]]
or
OPTION LCDPANEL
NOCONSOLE

the LCD display panel for use as the console output. The LCD
 Configures
must support transparent text (i.e. the SSD1963_x, ILI9341 or


console (serial over USB).
‘nn is a two character code defining the keyboard layout. The choices are
US for the standard keyboard layout in the USA, Australia and New
Zealand and UK for the United Kingdom, GR for Germany, FR for
France, BR for Brazil and ES for Spain.
The keyboard must be connected as follows:
 Connect GP8 to PS2 socket CLOCK pin.
 Connect GP9 to PS2 socket DATA pin.
 Connect VBUS (5V) or 3V3 (3,3V) to PS2 socket +5V.
 Connect GND to PS2 socket GND.
Some keyboards will run on 3.3V and in that case the clock and data pins
can be directly connected. However, if the keyboard is powered by 5V,
level shifting must be used for these connections so that the PicoMite
I/O pins are not subjected to more than 3.6V
This command can only be run from the command line and will cause a
reboot. This setting can be reset with the command OPTION
KEYBOARD NO_KEYBOARD.
The optional parameters capslock and numlock set the initial state of the
keyboard (default 0, 1). The repeatstart defines how how long before a
character repeats the first time (valid 0-3 = 250mSec, 500mSec, 750mSec,
1S: default 1=500mSec). The repeat rate defines how fast a character
repeats after the first repeat (valid 0-31 = 33mSec to 500mSec: default
12=100mSec).

VIRTUAL _C = Colour, 4bit, 320 x 240
VIRTUAL _M = Monochrome, 640 x 480
Using this feature a program can draw graphical images on this virtual
panel and then save them as a BMP file. Useful for creating a graphic
image for export without an attached display

See the section LCD Displays for the details.
This command must be run at the command prompt (not in a program).

ST7789_320 controllers).
'font' is the default font, 'fc' is the default foreground colour, 'bc' is the
default background colour. These parameters are optional and default to
font 1, white, black and 100%. These settings are applied at power up.
Note that for displays other than the SSD1963 scrolling for any console
output is very slow so this feature is not recommended for general use.
This setting is saved in flash and will be automatically applied on startup.
To disable it use the OPTION LCDPANEL NOCONSOLE command.
This command must be run at the command prompt.


OPTION LCDPANEL USER
hres, vres

a user written display driver in MMBasic. See the file “User
 Configures
Display Driver.txt” in the PicoMite firmware distribution for a description
of how to write the driver.

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

OPTION MODBUFF
ENABLE/DISABLE [sizeinK]

or removes an area of flash memory used for loading an playing
 Creates
.MOD files. If enabled then a mod buffer is created with a size of
128Kbytes. This can be overridden with “sizeinK”.
The default is that no mod buffer is available

OPTION PICO ON/OFF

OPTION PIN nbr

OPTION PLATFORM name$

set to OFF pins GP23, GP24 and GP29 are not set up for normal
 When
Pico use and are immediately available to use. Default ON
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
command allows a user to identify a particular H/W configuration
 This
that can then be used to control a program. name$ can be up to 31
characters long. This is a permanent option.
MM.INFO$(PLATFORM) returns this string.

OPTION POWER PFM |
PWM

 Changes operation of the 3.3V supply switch mode power supply.

OPTION RESET

 Reset all saved options to their default values.

By default this runs in PFM mode. PWM gives better noise performance
but is less power-efficient. Note that under heavy load the system will
run in PWM mode regardless of this setting.

This command must be run at the command prompt (not in a program).



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

OPTION SERIAL CONSOLE
uartapin, uartbpin [,B]

that the console be accessed via a hardware serial port (instead
 Specify
of virtual serial over USB).

If the optional pins are not specified the SD Card will use the pins
specified by OPTION SYSTEM SPI.
Note: The pins specified by OPTION SYSTEM SPI must be a valid set
of hardware SPI pins (SPI or SPI2), however, the pins specified by
OPTION SDCARD can be any pins. The pins specified by OPTION
SYSTEM SPI and OPTION SDCARD cannot be the same.
This command must be run at the command prompt (not in a program).

‘uartapin’ and ‘uartbpin’ can be any valid pair of rx and tx pins for either
COM1 or COM2. The order that they are specified is not important.
The speed defaults to 115200 baud but can be changed with OPTION
BAUDRATE. Adding the "B" parameter means output will go to "B"oth
the serial port and the USB.
OPTION SERIAL CONSOLE
DISABLE

Revert to the normal the USB console.
These commands must be run at the command prompt (not in a program).

OPTION SYSTEM I2C sdapin,
sclpin [,SLOW/FAST]

the I2C port and pins for use by system devices (LCD panel, and
 Specify
RTC). The PicoMite uses a specific I2C port for system devices, leaving
the other for the programmer. This command specifies which pins are to
be used, and hence which of the I2C ports is to be used. The pins
allocated to the SYSTEM I2C will not be available for other MMBasic
SETPIN settings but can be used for additional I2C devices using the
standard I2C command. Note: I2C(2) OPEN and I2C(2) CLOSE are not
available in this case. By default the I2C port is opened at a speed of
400KHz and with a 100mSec timeout. The I2C frequency can be set
using the optional third parameter which can take the values FAST =
400KHz or SLOW = 100KHzThis command must be run at the command
prompt (not in a program).

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


The PicoMite uses a specific hardware SPI port for system devices,
leaving the other for the user. This command specifies which pins are to
be used, and hence which of the SPI ports is to be used. The pins
allocated to the SYSTEM SPI will not be available to other MMBasic
commands.
This command must be run at the command prompt (not in a program).


OPTION TOUCH T_CS pin,
T_IRQ pin [, Beep]
OPTION TOUCH DISABLE

OPTION VCC voltage


MMBasic for the touch sensitive feature of an attached LCD
 Configures
panel.
'T_CS pin' and 'T_IRQ pin' are the PicoMite I/O pins to be used for chip
select and touch interrupt respectively (any free pins can be used).
The remaining pins are connected to those specified using the OPTION
SYSTEM SPI command.
‘Beep’ is an optional pin which can be connected to a small
buzzer/beeper to generate a "click" or beep sound when an advanced
control is touched.
This command must be run at the command prompt (not in a program).
Specifies the voltage (Vcc) supplied to the PicoMite.
When using the ADC pins to measure voltage the PicoMite uses the
voltage on the pin marked VREF as its reference. This voltage can be
accurately measured using a DMM and set using this command for more
accurate measurement.
The parameter is not saved and should be initialised either on the
command line or in a program. The default if not set is 3.3.


Commands
Detailed Listing
Square brackets indicate that the parameter or characters are optional.
‘ (single quotation mark)

Starts a comment and any text following it will be ignored. Comments can be
placed anywhere on a line.

*file

The star/asterisk command is a shortcut for RUN that may only be used at the
MMBasic prompt. e.g.
*
RUN
*foo
RUN "foo"
*"foo bar"
RUN "foo bar"
*foo –wombat
RUN "foo", "--wombat"
*foo "wom"
RUN "foo", CHR$(34) + "wom" + CHR$(34)
*foo --wom="bat" RUN "foo","--wom=" + CHR$(34) + "bat" + CHR$(34)
String expressions are not supported/evaluated by this command; any
arguments provided are passed as a literal string to the RUN command.

? (question mark)

Shortcut for the PRINT command.
Start and end of multiline comments. /* and */ must be the first non-space
characters at the start of a line and have a space or end-of-line after them (i.e.
they are MMBasic commands). Multi-line comments cannot be used inside
subroutines and functions. Any characters after */ on a line are also treated as
a comment.
Shortcut for DRIVE “A:” and DRIVE “B:” at the command prompt

/*
*/

A: or B:
ADC OPEN freq, n_channels
[,interrupt]

This allocates up to 4 ADC channels for use GP26, GP27, GP28, and GP29
and sets them to be converted at the specified frequency. The maximum total
frequency is 500KHz (e.g. 125KHz if all four channels are to be sampled). If
the number of channels is one then it will always be GP26 used, if two then
GP26 and GP27 etc. Sampling of multiple channels is sequential (there is only
one ADC). The specified pins are locked to the function when ADC OPEN is
active
The optional interrupt parameter specifies an interrupt to call when the
conversion completes. If not specified then conversion will be blocking

ADC FREQUENCY freq

This changes the sampling frequency of the ADC conversion without having to
close and re-open

ADC CLOSE

Releases the pins to normal usage

ADC START array1!()
[,array2!()] [,array3!()]
[,array4!()] [,Chan4arr!()]
[,C1min] [,C1max] [,C2min]
[,C2max] [,C3min] [,C3max]
[,C4min] [,C4max]

This starts conversion into the specified arrays. The arrays must be floating
point and the same size. The size of the arrays defines the number of
conversions. Start can be called repeatedly once the ADC is OPEN
‘Cxmin’ and ‘Cxmax’ will scale the readings. For example, C1min=200 and
C1max=100 will create values ranging from 200 to 100 for equivalent voltages
of 0 - 3.3. If the scaling is not used the results are returned as a voltage
between 0 and OPTION VCC (defaults to 3.3V).

ADC RUN
array1%(),array2%()

Runs the ADC continuously in double buffered mode. The ADC first fills
array1% and then array2% and then back to array1% etc. If more than one
ADC channel is specified in the ADC OPEN command the data are
interleaved. The data is returned as packed 8-bit values (Use MEMORY
UNPACK to convert to a normal array). MM.INFO(ADC) will return the
number of the buffer currently available for reading (1 or 2)



ARC x, y, r1, [r2], a1, a2 [, c]

Draws an arc of a circle with a given colour and width between two radials
(defined in degrees). Parameters for the ARC command are:
x:
X coordinate of centre of arc
y:
Y coordinate of centre of arc
r1:
inner radius of arc
r2:
outer radius of arc - can be omitted if 1 pixel wide
a1:
start angle of arc in degrees
a2:
end angle of arc in degrees
c:
Colour of arc (if omitted it will default to the foreground colour)
Zero degrees is at the 12 o'clock position.

AUTOSAVE
or
AUTOSAVE CRUNCH
Or
AUTOSAVE APPEND

Enter automatic program entry mode. This command will take lines of text
from the console serial input and save them to program memory.
This mode is terminated by entering Control-Z or F1 which will then cause the
received data to be transferred into program memory overwriting the previous
program. Use F2 to exit and immediately run the program.
The CRUNCH option instructs MMBasic to remove all comments, blank lines
and unnecessary spaces from the program before saving. This can be used on
large programs to allow them to fit into limited memory. CRUNCH can be
abbreviated to the single letter C.
The APPEND option will leave the existing program intact and append the
new data from the serial input to the end of it.
At any time this command can be aborted by Control-C which will leave
program memory untouched.
This is one way of transferring a BASIC program into the PicoMite. The
program to be transferred can be pasted into a terminal emulator and this
command will capture the text stream and store it into program memory. It can
also be used for entering a small program directly at the console input.

BACKLIGHT n [,DEFAULT]

Sets the display backlight, valid values are 0 to 100. If DEFAULT is specified
then the firmware will automatically set the backlight to that level on powerup. This is particularly useful for battery operation where reducing the
backlight level can significantly increase battery life

BITBANG

Replaced by the command DEVICE. For compatibility BITBANG can still be
used in programs and will be automatically converted to DEVICE

BLIT

Copy one section of the display screen on LCD panel using the SSD19863,
ILI9341, ILI9488 (if MISO connected), or ST7789_320 controllers controllers
to or from a memory buffer.

BLIT READ [#]b, x, y, w, h

BLIT READ will copy a portion of the display to the memory buffer '#b'. The
source coordinate is 'x' and 'y' and the width of the display area to copy is 'w'
and the height is 'h'. When this command is used the memory buffer is
automatically created and sufficient memory allocated. This buffer can be
freed and the memory recovered with the BLIT CLOSE command.

BLIT WRITE [#]b, x, y
[,mode]

BLIT WRITE will copy the memory buffer '#b' to the display. The destination
coordinate is 'x' and 'y' and the width/height of the buffer to copy is 'w' and 'h'.
If omitted w,h will default to the width and height of the blit buffer.
The optional 'mode' parameter defaults to 0 and specifies how the stored image
data is changed as it is written out. It is the bitwise AND of the following
values:
&B001 = mirrored left to right
&B010 = mirrored top to bottom
&B100 = don't copy transparent pixels



BLIT LOAD[BMP] [#]b,
fname$ [,x] [,y] [,w] [,h]

BLIT LOAD will load a blit buffer from a 24-bit bmp image file. x,y define
the start position in the image to start loading and w,h specify the width and
height of the area to be loaded. This command will work on most display
panels (not just panels using the ILI9341 controller).
e.g.
BLIT LOAD #1,"image1", 50,50,100,100
will load an area of 100 pixels square with the top left had corner at 50,50 from
the image image1.bmp

BLIT CLOSE [#]b

BLIT CLOSE will close the memory buffer '#b' to allow it to be used for
another BLIT READ operation and recover the memory used.
Notes:
 32 buffers are available ranging from #1 to #32.
 When specifying the buffer number the # symbol is optional.
 All other arguments are in pixels.

BLIT MERGE colour, x, y, w, Copies an area of the framebuffer defined by the ‘x’ and ‘y’ pixel coordinates
h
of the top left and with a width of ‘w’ and height ‘h’ to the LCD display. As
part of the copy it will overlay the LCD display with pixels from the layer
buffer that aren’t set to the ‘colour’ specified. The colour is specified as a
number between 0 and 15 representing:
Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta,
rust, fuschia, brown, lilac, yellow and white
Requires both a framebuffer and a layer buffer to have been created to operate.
Will automatically wait for frame blanking before starting the copy on
ILI9341, ST7789_320 and ILI9488 displays
BLIT FRAMEBUFFER from,
to, xin, yin, xout, yout, width,
height [,colour]

Copies an area of a specific ‘from’ framebuffer N, F, or L to another different
‘to’ framebuffer N, F, or L. ‘xin’ and ‘yin’ define the top left of the area of
‘width’ and ‘height’ on the source framebuffer to be copied. ‘xout’ and ‘yout’
define the top left of the area on the target framebuffer to receive the copy. The
optional parameter colour defines a pixel colour on the source which will not
be copied. If omitted all pixels are copied. The colour is specified as a number
between 0 and 15 representing:
Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta,
rust, fuschia, brown, lilac, yellow and white

BLIT MEMORY address, x, y
[,col]

Copies an area of memory treated as a packed array of colour nibbles to the
current graphical output as specified by FRAMEBUFFER WRITE. The colour
is specified as a number between 0 and 15 representing:
Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta,
rust, fuschia, brown, lilac, yellow and white
The first word of the area of memory starting at ‘address%’ must contain the
width and height of the area to be copied as 16-bit integers with the width as
the bottom 16 bits. The address must be aligned to a word boundary (divisible
by 4).
If the optional parameter ‘col’ is specified then that specific colour is not
copied.
If the top bit of either the width or height is set to 1 then the colour data is
treated as compressed (the remaining 15 bits are used as the width and/or
height). The compression algorithm is simple, each byte contains a count in the
bottom nibble (1-15) and a colour in the top nibble (0-15). In the event that
more than 15 pixels are the same colour additional bytes are used for that
colour



BLIT COMPRESSED
address%, x, y [,col]

Acts the same as BLIT MEMORY but assumes the data is compressed and
ignores the top bit in the width and height

BLIT x1, y1, x2, y2, w, h

Copy one section of the display screen to another part of the display.
The source coordinate is 'x1' and 'y1'. The destination coordinate is 'x2' and
'y2'. The width of the screen area to copy is 'w' and the height is 'h'.
All arguments are in pixels. The display on a PicoMite must use the
SSD19863, ILI9341_8, ILI9341, ILI9488 (if MISO connected), or
ST7789_320 controllers.

BOX x, y, w, h [, lw] [,c]
[,fill]

Draws a box on the attached LCD panel with the top left hand corner at 'x' and
'y' with a width of 'w' pixels and a height of 'h' pixels.
'lw' is the width of the sides of the box and can be zero. It defaults to 1.
'c' specifies the colour and defaults to the default foreground colour if not
specified. 'fill' is the fill colour. It can be omitted or set to -1 in which case the
box will not be filled.
All parameters can be expressed as arrays and the software will plot the
number of boxes as determined by the dimensions of the smallest array. 'x',
'y', 'w', and 'h' must all be arrays or all be single variables /constants otherwise
an error will be generated. 'lw', 'c', and fill can be either arrays or single
variables/constants.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

CALL usersubname$
[,usersubparameters,..]

This is an efficient way of programmatically calling user defined subroutines
(see also the CALL() function). In many case it can allow you to get rid of
complex SELECT and IF THEN ELSEIF ENDIF clauses and is processed in a
much more efficient way.
The “usersubname$” can be any string or variable or function that resolves to
the name of a normal user subroutine (not an in-built command). The
“usersubparameters” are the same parameters that would be used to call the
subroutine directly. A typical use could be writing any sort of emulator where
one of a large number of subroutines should be called depending on some
variable. It also allows a way of passing a subroutine name to another
subroutine or function as a variable.

CAT S$, N$

Concatenates the strings by appending N$ to S$. This is functionally the same
a S$ = S$ + N$ but operates faster.

CHDIR dir$

Change the current working directory on the default drive to ‘dir$’
The special entry “.” represents the parent of the current directory and “.”
represents the current directory. "/" is the root directory.

CIRCLE x, y, r [,lw] [, a] [, Draw a circle on the video output centred at 'x' and 'y' with a radius of 'r' on the
c] [, fill]
attached LCD panel. ‘lw’ is optional and is the line width (defaults to 1).
'c' is the optional colour and defaults to the current foreground colour if not
specified. The optional 'a' is a floating point number which will define the
aspect ratio. If the aspect is not specified the default is 1.0 which gives a
standard circle. 'fill' is the fill colour. It can be omitted or set to -1 in which
case the box will not be filled.
All parameters can be expressed as arrays and the software will plot the
number of circles as determined by the dimensions of the smallest array. 'x',
'y' and 'r' must all be arrays or all be single variables/constants otherwise an
error will be generated. 'lw', 'a', 'c', and fill can be either arrays or single
variables/constants.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.



CLEAR

Delete all variables and recover the memory used by them.
See ERASE for deleting specific array variables.

CLOSE [#]fnbr [,[#]fnbr] …

Close the file(s) previously opened with the file number ‘#fnbr’. The # is
optional. Also see the OPEN command.

CLS [colour]

Clears the LCD panel's screen. Optionally 'colour' can be specified which will
be used for the background when clearing the screen.

COLOUR fore [, back]
or
COLOR fore [, back]

Sets the default colour for commands (PRINT, etc) that display on the on the
attached LCD panel. 'fore' is the foreground colour, 'back' is the background
colour. The background is optional and if not specified will default to black.

CONST id = expression
[, id = expression] … etc

Create a constant identifier which cannot be changed once created.
'id' is the identifier which follows the same rules as for variables. The
identifier can have a type suffix (!, %, or $) but it is not required. If it is
specified it must match the type of 'expression'. 'expression' is the value of the
identifier and it can be a normal expression (including user defined functions)
which will be evaluated when the constant is created.
A constant defined outside a sub or function is global and can be seen
throughout the program. A constant defined inside a sub or function is local to
that routine and will hide a global constant with the same name.

CONTINUE

Resume running a program that has been stopped by an END statement, an
error, or CTRL-C. The program will restart with the next statement following
the previous stopping point.
Note that it is not always possible to resume the program correctly – this
particularly applies to complex programs with graphics, nested loops and/or
nested subroutines and functions.

CONTINUE DO
or
CONTINUE FOR

Skip to the end of a DO/LOOP or a FOR/NEXT loop. The loop condition will
then be tested and if still valid the loop will continue with the next iteration.

COPY fname1$ TO fname2$

Copy a file from ‘fname1$’ to ‘fname2$’. Both are strings.
A directory path can be used in both 'fname$' and 'fname$'. If the paths differ
the file specified in 'fname$' will be copied to the path specified in 'fname2$'
with the file name as specified. The filenames can include the drive
specification in the case that you are copying to and or from the non-active
drive (see the DRIVE command)

COPY fname$ TO dirname$

Wildcard copy. the bulk copy is triggered if fname$ contains a '*' or a '?'
character. dirname$ must be a valid directory name and should NOT end in a
slash character

CPU RESTART

Will force a restart of the processor.
This will clear all variables and reset everything (e.g. timers, COM ports, I2C,
etc) similar to a power up situation but without the power up banner.
If OPTION AUTORUN has been set the program in the specified flash
location or program memory will restart.

CPU SLEEP n

Will cause the processor to sleep for ‘n’ seconds.
Note that the CPU does not have a true low power sleep so the power saving is
limited.



CSUB name [type [, type]
…]
hex [[ hex[…]
hex [[ hex[…]
END CSUB

Defines the binary code for an embedded machine code program module
written in C or ARM assembler. The module will appear in MMBasic as the
command 'name' and can be used in the same manner as a built-in command.
Multiple embedded routines can be used in a program with each defining a
different module with a different 'name'.
The first 'hex' word is a 32 bit word which is the offset in bytes from the start
of the CSUB to the entry point of the embedded routine (usually the function
main()). The following hex words are the compiled binary code for the
module. These are automatically programmed into MMBasic when the
program is saved. Each 'hex' must be exactly eight hex digits representing the
bits in a 32-bit word and be separated by one or more spaces or new lines. The
command must be terminated by a matching END CSUB. Any errors in the
data format will be reported when the program is run.
During execution MMBasic will skip over any CSUB commands so they can
be placed anywhere in the program.
The type of each parameter can be specified in the definition. For example:
CSUB MySub integer, integer, string
This specifies that there will be three parameters, the first two being integers
and the third a string.
Note:
 Up to ten arguments can be specified ('arg1', 'arg2', etc).
 If a variable or array is specified as an argument the C routine will
receive a pointer to the memory allocated to the variable or array and the
C routine can change this memory to return a value to the caller. In the
case of arrays, they should be passed with empty brackets e.g. arg(). In
the CSUB the argument will be supplied as a pointer to the first element
of the array.
 Constants and expressions will be passed to the embedded C routine as
pointers to a temporary memory space holding the value.

CTRLVAL(#ref) =

This command will set the value of an advanced control.
'#ref' is the control's reference number.
For off/on controls like check boxes it will override any touch input and can be
used to depress/release switches, tick/untick check boxes, etc. A value of zero
is off or unchecked and non-zero will turn the control on. For a LED it will
cause the LED to be illuminated or turned off. It can also be used to set the
initial value of spin boxes, text boxes, etc.
For example:
CTRLVAL(#10) = 12.4
All controls expect to be assigned a number (float or integer) except Frame,
Caption, Display Box, Text Box and Format Box which expect a string.

DATA constant[,constant]..

Stores numerical and string constants to be accessed by READ.
In general string constants should be surrounded by double quotes ("). An
exception is when the string consists of just alphanumeric characters that do
not represent MMBasic keywords (such as THEN, WHILE, etc). In that case
quotes are not needed.
Numerical constants can also be expressions such as 5 * 60.

DATE$ = "DD-MM-YY[YY]"
or
DATE$ = "DD/MM/YY[YY]"
or
DATE$ =”YYYY-MM-DD”
or
DATE$=”YYYY/MM/DD”

Set the date of the internal clock/calendar.
DD, MM and YY are numbers, for example: DATE$ = "28-7-2014"
With OPTION RTC AUTO ENABLE the picomite starts with the DATE$
programmed in RTC.
Without OPTION RTC AUTO ENABLE the picomite starts with the date set
to "01-01-2000" on power up.



DEFINEFONT #Nbr
hex [[ hex[…]
hex [[ hex[…]
END DEFINEFONT

This will define an embedded font which can be used alongside or to replace
the built in font(s) used on an attached LCD panel. These work exactly same
as the built in fonts (i.e. selected using the FONT command or specified in the
TEXT command).
See the Embedded Fonts folder in the PicoMite distribution zip file for a
selection of embedded fonts and a full description of how to create them.
'#Nbr' is the font's reference number (from 1 to 16). It can be the same number
as a built in font and in that case it will replace the built in font.
Each 'hex' must be exactly eight hex digits and be separated by spaces or new
lines from the next.
 Multiple lines of 'hex' words can be used with the command terminated by
a matching END DEFINEFONT.
 Multiple embedded fonts can be used in a program with each defining a
different font with a different font number.
 During execution MMBasic will skip over any DEFINEFONT commands
so they can be placed anywhere in the program.
 Any errors in the data format will be reported when the program is saved.

DEVICE BITSTREAM pinno,
n_transitions, array%()

DEVICE CAMERA OPEN
XLKpin, PLKpin, HSpin,
VSCpin, RETpin, D0pin

DEVICE CAMERA
CAPTURE [scale, [x , y]]


This command is used to generate an extremely accurate bit sequence on the
pin specified. The pin must have previously been set up as an output and set to
the required starting level.
Notes:
 The array contains the length of each level in the bitstream in
microseconds. The maximum period allowed is 65.5 mSec
 The first transition will occur immediately on executing the command.
 The last period in the array is ignored other than defining the time before
control returns to the program or command line.
 The pin is left in the starting state if the number of transitions is even
and the opposite state if the number of transitions is odd.
Command supporting the OV7670 camera module. This command initialises
the camera, It outputs a 12MHz clock on XLK (PWM) and checks that it is
correctly receiving signals on PLK, VS, and HS. The camera is set to a
resolution of 160x120 (QQVGA) which is the maximum achievable within the
limits of the RP2040 memory.
Enable OPTION SYSTEM I2C on the PicoMite and wire SCL and SDA to the
relevant pins (may be labelled SIOC and SIOD on the camera module). These
connections must have a pullup to 3.3V - 2K7 recommended)
Other pins are wired as per the OPEN command. (NB: VS may be labelled
VSYNC, HS may be labelled HREF, PLK may be labelled PCLK, RET may
be labelled RESET and XLK may be XCLK on your module)
D0pin defines the start of a range of 8 contiguous pins (e.g.GP0 - GP7).
This captures a picture from the camera (RGB565) and displays it on an LCD
screen. An SPI LCD must be connected and enabled in order for the command
to work. (ILI9341 and ST7789_320 recommended).
Scale defaults to 1 and x,y each to 0
By default a 160x120 image is output on the LCD with the top left at 0,0 on
the LCD. Setting scale to 2 will fill a 320x240 display with the image. Setting
the x and y parameters will offset the top left of the image on the LCD.
Update rate in a continuous loop is 7FPS onto the display at 1:1 scale and
5FPS scaled to 320x240.
Of course, assuming the display has MISO wired it is then possible to save the
image to disk using the SAVE IMAGE command as used to create the
example image above.


DEVICE CAMERA CLOSE

Closes the camera subsystem and frees up all the pins allocated in the OPEN
command

DEVICE CAMERA
CHANGE image%(),change!
[,scale [,x ,y]]

The camera firmware is also able to detect motion in the camera's field of view
using the command. It does this by operating the camera in YUV mode rather
than RGB. This has the advantage that the intensity information and colour
information are separated and just one byte is needed for a 256-level greyscale
image which is ideal fer detecting movement.
image% is an array of size 160x120 bytes (DIM image%(160,120/8-1)
On calling the command it holds a packed 8-bit greyscale image.
The change! variable returns the percentage the image has changed from the
previous time the command was called.
Optionally if "scale" is set then the image delta is output to the screen i.e. the
difference between the previous image and this one. As in the CAPTURE
command the delta image can be scaled and positioned as required. If the scale
parameter is omitted then the LCD is not updated by this command.

DEVICE CAMERA TEST
tnum

The command enables or disables a test signal from the camera. tnum=2
generates colourbars and tnum=0 sets back to the visual input. tnum = 1 and
tnum = 3 do something but what?

DEVICE CAMERA
REGISTER reg%, data%

Sets the register "reg%" in the camera to the value "data%". When used the
command will report to the console the previous value and automatically
confirms that the new value has been set as requested. The colour rendition of
the camera as initialised is reasonable but could probably be improved further
by tuning the various camera registers.

DEVICE HUMID pin, tvar,
hvar [,DHT11]

Returns the temperature and humidity using the DHT22 sensor. Alternative
versions of the DHT22 are the AM2303 or the RHT03 (all are compatible).
'pin' is the I/O pin connected to the sensor. Any I/O pin may be used.
'tvar' is the variable that will hold the measured temperature and 'hvar' is the
same for humidity. Both must be present and both must be floating point
variables.
For example: HUMID 3, TEMP!, HUMIDITY!
Temperature is measured in ºC and the humidity is percent relative humidity.
Both will be measured with a resolution of 0.1. If an error occurs (sensor not
connected or corrupt signal) both values will be 1000.0.
Normally the DHT22 should powered by 3.3V to keep its output below 3.6V
for the PicoMite and the signal pin of should be pulled up by a 1K to 10K
resistor (4.7K recommended) to 3.3V.
The optional DHT11 parameter modifies the timings to work with the DHT11.
Set to 1 for DHT11 and 0 or omit for DHT22.

DEVICE SERIALTX pinno,
baudrate, ostring$

Outputs ostring$ as a serial datastream on pinno. Baudrate can be between 110
and 230400 (230400 may need CPU to be overclocked). NB command is
blocking during transmission.

DEVICE SERIALRX pinno,
baudrate, istring$,
timeout_in_ms, status% [,nbr]
[,terminators$]

Inputs serial data on pinno. Baudrate can be between 110 and 230400 (230400
may need CPU to be overclocked). status% returns:
-1 = timeout (NB: use len(istring$) to see number received)
2 = number of characters requested satisfied
3 = terminating character satisfied
Nbr specifies the number of characters to be received before the command
returns. Terminators$ specifies one or more signle characters that can be used
to terminate reception. NB command is blocking during reception.



DEVICE WS2812 type, pin,
nbr, value%[()]

DEVICE WII OPEN
[,interrupt]

DEVICE WII CLOSE
DEVICE LCD INIT d4, d5,
d6, d7, rs, en
or
DEVICE LCD line, pos, text$
or
DEVICE LCD CLEAR
or
DEVICE LCD CLOSE

This command outputs the required signals to drive one or more WS2812 LED
chips connected to 'pin'. Note that the pin must be set to a digital output before
this command is used.
'type' is a single character specifying the type of chip being driven:
O = original WS2812
B = WS2812B
S = SK6812
W =SK6812W (RGBW)
‘nbr’ is the number of LEDs in the chain (1 to 256). The 'value%()' array
should be an integer array sized to have exactly the same number of elements
as the number of LEDs to be driven.
For the first three variants each element in the array should contain the colour
in the normal RGB888 format (i.e. 0 to &HFFFFFF).
For type W use a RGBW value (0-&HFFFFFFFF).
If only one LED is connected then a single integer should be used for value%
(ie, not an array).
Opens a WII Classic controller and implements background polling of the
device. The Wii Classic must be wired to the pins specified by OPTION
SYSTEM I2C which is a prerequisite. Open attempts to talk to the Wii Classic
and will return an error if not found. If found the firmware will sample the Wii
data in the background at a rate of 50Hz. If an optional user interrupt is
specified this will be triggered if any of the buttons changes (both on and off)
See the DEVICE function for how to read data from the Wii Classic.
CLOSE will stop the background polling and disable any interrupt specified
Display text on an LCD character display module. This command will work
with most 1-line, 2-line or 4-line LCD modules that use the KS0066, HD44780
or SPLC780 controller (however this is not guaranteed).
The LCD INIT command is used to initialise the LCD module for use. 'd4' to
'd7' are the I/O pins that connect to inputs D4 to D7 on the LCD module
(inputs D0 to D3 should be connected to ground). 'rs' is the pin connected to
the register select input on the module (sometimes called CMD). 'en' is the pin
connected to the enable or chip select input on the module. The R/W input on
the module should always be grounded. The above I/O pins are automatically
set to outputs by this command.
When the module has been initialised data can be written to it using the LCD
command. 'line' is the line on the display (1 to 4) and 'pos' is the character
location on the line (the first location is 1). 'text$' is a string containing the text
to write to the LCD display.
'pos' can also be C8, C16, C20 or C40 in which case the line will be cleared
and the text centred on a 8 or 16, 20 or 40 line display. For example:
LCD 1, C16, "Hello"
LCD CLEAR will erase all data displayed on the LCD and LCD CLOSE will
terminate the LCD function and return all I/O pins to the not configured state.
See the section Special Hardware Devices for more details.

DEVICE LCD CMD d1 [, d2
[, etc]]
or
DEVICE LCD DATA d1 [, d2
[, etc]]


These commands will send one or more bytes to an LCD display as either a
command (LCD CMD) or as data (LCD DATA). Each byte is a number
between 0 and 255 and must be separated by commas. The LCD must have
been previously initialised using the LCD INIT command (see above).
These commands can be used to drive a non standard LCD in "raw mode" or
they can be used to enable specialised features such as scrolling, cursors and
custom character sets. You will need to refer to the data sheet for your LCD to
find the necessary command and data values.


DIM [type] decl [,decl]..
where 'decl' is:
var [length] [type] [init]
'var' is a variable name with
optional dimensions
'length' is used to set the
maximum size of the string to
'n' as in LENGTH n
'type' is one of FLOAT or
INTEGER or STRING (the
type can be prefixed by the
keyword AS - as in AS
FLOAT)
'init' is the value to initialise
the variable and consists of:
= <expression>
For a simple variable one
expression is used, for an array
a list of comma separated
expressions surrounded by
brackets is used.

Examples:
DIM nbr(50)
DIM INTEGER nbr(50)
DIM name AS STRING
DIM a, b$, nbr(100), strn$(20)
DIM a(5,5,5), b(1000)
DIM strn$(200) LENGTH 20
DIM STRING strn(200)
LENGTH 20
DIM a = 1234, b = 345
DIM STRING strn = "text"
DIM x%(3) = (11, 22, 33, 44)


Declares one or more variables (i.e. makes the variable name and its
characteristics known to the interpreter).
When OPTION EXPLICIT is used (as recommended) the DIM, LOCAL or
STATIC commands are the only way that a variable can be created. If this
option is not used then using the DIM command is optional and if not used the
variable will be created automatically when first referenced.
The type of the variable (i.e. string, float or integer) can be specified in one of
three ways:
By using a type suffix (i.e. !, % or $ for float, integer or string). For example:
DIM nbr%, amount!, name$
By using one of the keywords FLOAT, INTEGER or STRING immediately
after the command DIM and before the variable(s) are listed. The specified
type then applies to all variables listed (i.e. it does not have to be repeated).
For example:
DIM STRING first_name, last_name, city
By using the Microsoft convention of using the keyword "AS" and the type
keyword (i.e. FLOAT, INTEGER or STRING) after each variable. If you use
this method the type must be specified for each variable and can be changed
from variable to variable.
For example:
DIM amount AS FLOAT, name AS STRING
Floating point or integer variables will be set to zero when created and strings
will be set to an empty string (i.e. ""). You can initialise the value of the
variable with something different by using an equals symbol (=) and an
expression following the variable definition. For example:
DIM STRING city = "Perth", house = "Brick"
The initialising value can be an expression (including other variables) and will
be evaluated when the DIM command is executed. See the section Defining
and Using Variables for more examples of the syntax.
As well as declaring simple variables the DIM command will also declare
arrayed variables (i.e. an indexed variable with a number of dimensions).
Following the variable's name the dimensions are specified by a list of numbers
separated by commas and enclosed in brackets. For example:
DIM array(10, 20)
Each number specifies the number of elements in each dimension. Normally
the numbering of each dimension starts at 0 but the OPTION BASE command
can be used to change this to 1.
The above example specifies a two dimensional array with 11 elements (0 to
10) in the first dimension and 21 (0 to 20) in the second dimension. The total
number of elements is 231 and because each floating point number on the
PicoMite requires 8 bytes a total of 1848 bytes of memory will be allocated.
Strings will default to allocating 255 bytes (i.e. characters) of memory for each
element and this can quickly use up memory when defining arrays of strings.
In that case the LENGTH keyword can be used to specify the amount of
memory to be allocated to each element and therefore the maximum length of
the string that can be stored. This allocation ('n') can be from 1 to 255
characters.
For example: DIM STRING s(5, 10) will declare a string array with 66
elements consuming 16,896 bytes of memory while:
DIM STRING s(5, 10) LENGTH 20
Will only consume 1,386 bytes of memory. Note that the amount of memory
allocated for each element is n + 1 as the extra byte is used to track the actual
length of the string stored in each element.
If a string longer than 'n' is assigned to an element of the array an error will be


produced. Other than this, string arrays created with the LENGTH keyword
act exactly the same as other string arrays. This keyword can also be used with
non-array string variables but it will not save any memory.
In the above example you can also use the Microsoft syntax of specifying the
type after the length qualifier. For example:
DIM s(5, 10) LENGTH 20 AS STRING
Arrays can also be initialised when they are declared by adding an equals
symbol (=) followed by a bracketed list of values at the end of the declaration.
For example:
DIM INTEGER nbr(4) = (22, 44, 55, 66, 88)
or
DIM s$(3) = ("foo", "boo", "doo", "zoo")
Note that the number of initialising values must match the number of elements
in the array including the base value set by OPTION BASE. If a multi
dimensioned array is initialised then the first dimension will be initialised first
followed by the second, etc.
Also note that the initialising values must be after the LENGTH qualifier (if
used) and after the type declaration (if used).
DO
<statements>
LOOP

This structure will loop forever; the EXIT DO command can be used to
terminate the loop or control must be explicitly transferred outside of the loop
by commands like GOTO or EXIT SUB (if in a subroutine).

DO WHILE expression
<statements>
LOOP

Loops while ‘expression’ is true (this is equivalent to the older WHILEWEND loop). If, at the start, the expression is false the statements in the loop
will not be executed, not even once.

DO
<statements>
LOOP UNTIL expression

Loops until the expression following UNTIL is true. Because the test is made
at the end of the loop the statements inside the loop will be executed at least
once, even if the expression is true.

DRAW3D

The 3D engine includes commands for manipulating 3D images including
setting the camera, creating, hiding, rotating, etc.
See the document “The CMM2 3D engine” in the PicoMite firmware
download for a full description.

DRIVE drive$

Sets the active disk drive as ‘drive$’. ‘drive$’ can be “A:” or “B:” where A is
the flash drive and B is the SD Card if configured

EDIT
or
EDIT fname$

Invoke the full screen editor.
If a filename is specified the editor will load the file from the current disk (A:
or B:) to allow editing and on exit with F1 or F2 save it to the disk. If the file
does not exist it is created on exit. The current program stored in flash memory
is not affected. If editing an existing file a backup with .bak appended to the
filename is also created on exit.
If fname$ includes an extension other than .bas then colour coding will be
temporarily turned off during the edit.
If no extension is specified the firmware will assume .bas
Editing a file from disk allows non-Basic files such as html or sprite files to be
edited without corruption during the tokenising process that happens when
stored to flash.
See the section Full Screen Editor for details of how to use the editor.

ELSE

Introduces an optional default condition in a multiline IF statement.
See the multiline IF statement for more details.

ELSEIF expression THEN
or
ELSE IF expression THEN

Introduces an optional secondary condition in a multiline IF statement.
See the multiline IF statement for more details.

END

End the running program and return to the command prompt.



END CSUB

Marks the end of a C subroutine. See the CSUB command.
Each CSUB must have one and only one matching END CSUB statement.

END FUNCTION

Marks the end of a user defined function. See the FUNCTION command.
Each function must have one and only one matching END FUNCTION
statement. Use EXIT FUNCTION if you need to return from a function from
within its body.

ENDIF
or
END IF

Terminates a multiline IF statement.
See the multiline IF statement for more details.

END SUB

Marks the end of a user defined subroutine. See the SUB command.
Each sub must have one and only one matching END SUB statement. Use
EXIT SUB if you need to return from a subroutine from within its body.

ERASE variable [,variable]..

Deletes variables and frees up the memory allocated to them. This will work
with arrayed variables and normal (non array) variables. Arrays can be
specified using empty brackets (e.g. dat()) or just by specifying the
variable's name (e.g. dat).
Use CLEAR to delete all variables at the same time (including arrays).

ERROR [error_msg$]

Forces an error and terminates the program. This is normally used in
debugging or to trap events that should not occur.

EXECUTE command$

This executes the Basic command "command$". Use should be limited to basic
commands that execute sequentially for example the GOTO statement will not
work properly
Things that are tested and work OK include GOSUB, Subroutine calls, other
simple statements (like PRINT and simple assignments)
Multiple statements separated by : are not allowed and will error
The command sets an internal watchdog before executing the requested
command and if control does not return to the command, like in a GOTO
statement, the timer will expire. In this case you will get the message
"Command timeout".
RUN is a special case and will cancel the timer allowing you to use the
command to chain programs if required.

EXIT DO
EXIT FOR
EXIT FUNCTION
EXIT SUB

EXIT DO provides an early exit from a DO..LOOP
EXIT FOR provides an early exit from a FOR..NEXT loop.
EXIT FUNCTION provides an early exit from a defined function.
EXIT SUB provides an early exit from a defined subroutine.
The old standard of EXIT on its own (exit a do loop) is also supported.

FILES [fspec$] [,sort]

Lists files in any directories on the default Flash Filesystem or SD Card.
'fspec$' (if specified) can contain a path and search wildcards in the filename.
Question marks (?) will match any character and an asterisk (*) will match
any number of characters. If omitted, all files will be listed.
For example:
* Find all entries
*.TXT Find all entries with an extension of TXT
E*.* Find all entries starting with E
X?X.* Find all three letter file names starting and ending with X
mydir/* Find all entries in directory mydir
NB: putting wildcards in the pathname will result in an error
'sort' specifies the sort order as follows:
size by ascending size
time by descending time/date
name by file name (default if not specified)
type by file extension



FLASH

Manages the storage of programs in the flash memory. Up to three programs
can be stored in the flash memory and retrieved as required. Note that these
saved programs will be erased with a firmware upgrade.
One of these flash memory locations can be automatically loaded and run
when power is applied using the OPTION AUTORUN n command. In the
following ‘n’ is a number 1 to 3.

FLASH LIST

Displays a list of all flash locations including the first line of the program.

FLASH LIST n [,all]

List the program saved to slot n. Use ALL to list without page breaks.

FLASH ERASE n

Erase a flash program location.

FLASH ERASE ALL

Erase all flash program locations.

FLASH SAVE n

Save the current program to the flash location specified.

FLASH LOAD n

Load a program from the specified flash location into program memory.

FLASH RUN n

Runs the program in flash location n, clear all variables. Does not change the
program memory.

FLASH CHAIN n

Runs the program in flash location n, leaving all variables intact (allows for a
program that is much bigger than the program memory). Does not change the
program memory.

FLASH OVERWRITE n

Erase a flash program location and then save the current program to the flash
location specified.

FLASH DISK LOAD n,
fname$ [,O[VERWRITE]]

Loads the contents of file fname$ into flash slot n as a binary image. If the
optional parameter OVERWRITE (or O) is specified the content of the flash
slot will be overwritten without an error being raised.
Causes any buffered writes to a file previously opened with the file number
‘#fnbr’ to be written to disk. The # is optional. Using this command ensures
that no data is lost if there is a power cut after a write command.

FLUSH [#]fnbr

FONT [#]font-number, scaling

This will set the default font for displaying text on an LCD panel.
Fonts are specified as a number. For example, #2 (the # is optional). See the
section Graphics Commands and Functions for details of the available fonts.
'scaling' can range from 1 to 15 and will multiply the size of the pixels making
the displayed character correspondingly wider and higher. E.g. a scale of 2
will double the height and width.

FOR counter = start TO finish
[STEP increment]

Initiates a FOR-NEXT loop with the 'counter' initially set to 'start' and
incrementing in 'increment' steps (default is 1) until 'counter' is greater than
'finish'.
The ‘increment’ can be an integer or a floating point number. Note that using
a floating point fractional number for 'increment' can accumulate rounding
errors in 'counter' which could cause the loop to terminate early or late.
'increment' can be negative in which case 'finish' should be less than 'start' and
the loop will count downwards.
See also the NEXT command.
FRAMEBUFFER command for colour SPI displays. This command can be used to
avoid screen artefacts when updating SPI displays with moving elements.

FRAMEBUFFER

FRAMEBUFFER CREATE


Creates a framebuffer “F” with a RGB121 colour space and resolution to
match the configured SPI colour display


FRAMEBUFFER LAYER

Creates a framebuffer “L” with a RGB121 colour space and resolution to
match the configured SPI colour display

FRAMEBUFFER WRITE
where/where

Specifies the target for subsequent graphics commands.
"where" can be N, F, or L where N is the actual display or a string variable can
be used

FRAMEBUFFER CLOSE
[which]

Closes a framebuffer and releases the memory. The optional parameter
"which" can be F or L. If omitted closes both.

FRAMEBUFFER COPY
from, to [,b]

Does a highly optimised full screen copy of one framebuffer to another.
"from" and "to" can be N, F, or L where N is the physical display.
You can only copy from N on displays that support BLIT and transparent text.
The firmware will automatically compress or expand the RGB resolution when
copying to and from unmatched framebuffers.
Of course copying from RGB565 to RGB121 loses information but for many
applications (e.g. games) 16 colour levels is more than enough.
When copying to an LCD display the optional parameter “b” can be used
(FRAMEBUFFER COPY F/L, N, B). This instructs the firmware to action the
copy using the second processor in the PicoMite and control returns
immediately to the Basic program

FRAMEBUFFER WAIT

Pauses processing until the LCD display enters frame blanking. Implemented
for ILI9341, ST7789_320 and ILI9488 displays. Used to reduce artefacts when
writing to the screen

FRAMEBUFFER MERGE
[colour] [,mode] [,updaterate]

Copies the contents of the Layer buffer and Framebuffer onto the LCD display
omitting all pixels of a particular colour. Preconditions for the command
are that FRAMEBUFFER and LAYERBUFFER are both created
FRAMEBUFFER MERGE - writes the contents of the framebuffer to the
physical display overwriting any pixels in the framebuffer that are set in the
layerbuffer (not zero)
FRAMEBUFER MERGE col - writes the contents of the framebuffer to the
physical display overwriting any pixels in the framebuffer that are in the
layerbuffer not set to the transparent colour "col". The colour is specified as a
number between 0 and 15 representing:
0:BLACK,1:BLUE,2:MYRTLE,3:COBALT,4:MIDGREEN,5:CERULEAN,6:
GREEN,7:CYAN,8:RED,9:MAGENTA,10:RUST,11:FUCHSIA,12:BROWN,
13:LILAC,14:YELLOW,15:WHITE
FRAMEBUFFER MERGE col,B - as above except that the transfer to the
physical display takes place on the second processor and control returns to
Basic immediately
FRAMEBUFFER MERGE col,R [,updaterate] - sets the second processor to
continuously update the physical display with the merger of the two buffers.
Automatically sets FRAMEBUFFER WRITE F if not F or L already set. By
default the screen will update as fast as possible (At 133MHz an ILI9341 in
SPI mode updates about 13 times a second, in 8-bit parallel mode the ILI9341
achieves 27 FPS)
If "updaterate" is set then the screen will update to the rate specified in
milliseconds (unless that is less than the fastest achievable on the display)
NB: FRAMEBUFFER WRITE cannot be set to N while continuous merged
update is active.
FRAMEBUFFER MERGE col,A - aborts the continuous updates
In addition deleting either the layerbuf or framebuffer, ctrl-C, or END will
abort the automatic update as well.
Waits for the latest update on the second processor to complete to allow
drawing without tearing

FRAMEBUFFER SYNC



FUNCTION xxx (arg1
[,arg2, …]) [AS <type>}
<statements>
<statements>
xxx = <return value>
END FUNCTION

Defines a callable function. This is the same as adding a new function to
MMBasic while it is running your program.
'xxx' is the function name and it must meet the specifications for naming a
variable. The type of the function can be specified by using a type suffix (i.e.
xxx$) or by specifying the type using AS <type> at the end of the functions
definition. For example:
FUNCTION xxx (arg1, arg2) AS STRING
'arg1', 'arg2', etc are the arguments or parameters to the function (the brackets
are always required, even if there are no arguments). An array is specified by
using empty brackets. i.e. arg3(). The type of the argument can be specified
by using a type suffix (i.e. arg1$) or by specifying the type using AS <type>
(i.e. arg1 AS STRING).
The argument can also be another defined function or the same function if
recursion is to be used (the recursion stack is limited to 50 nested calls).
To set the return value of the function you assign the value to the function's
name. For example:
FUNCTION SQUARE(a)
SQUARE = a * a
END FUNCTION
Every definition must have one END FUNCTION statement. When this is
reached the function will return its value to the expression from which it was
called. The command EXIT FUNCTION can be used for an early exit.
You use the function by using its name and arguments in a program just as you
would a normal MMBasic function. For example:
PRINT SQUARE(56.8)
When the function is called each argument in the caller is matched to the
argument in the function definition. These arguments are available only inside
the function.
Functions can be called with a variable number of arguments. Any omitted
arguments in the function's list will be set to zero or a null string.
Arguments in the caller's list that are a variable and have the correct type will
be passed by reference to the function. This means that any changes to the
corresponding argument in the function will also be copied to the caller's
variable and therefore may be accessed after the function has ended. Arrays
are passed by specifying the array name with empty brackets (e.g. arg()) and
are always passed by reference and must be the correct type.
You must not jump into or out of a function using commands like GOTO,
GOSUB, etc. Doing so will have undefined side effects including the
possibility of ruining your day.

GOTO target

Branches program execution to the target, which can be a line number or a
label.

GUI AREA #ref, startX,
startY, width, height

This will define an invisible area of the screen that is sensitive to touch and
will generate touch down and touch up interrupts. It can be used as the basis
for creating custom controls which are defined and managed by the program.
'#ref' is the control's reference number. 'startX' and 'startY' are the top left
coordinates while 'width' and 'height' set the dimensions.

GUI BCOLOUR colour, #ref1
[, #ref2, #ref3, etc]

This will change the background colour of the specified controls to 'colour'
which is an RGB value for the drawing colour.
'#ref' is the control's reference number.



GUI BARGAUGE #ref,
StartX, StartY, width, height,
FColour, BColour, min, max,
c1, ta, c2, tb, c3, tc, c4

Define either a horizontal or vertical analogue bar gauge.
'#ref' is the control's reference number.
'StartX' and 'StartY' are the top left coordinates of the bar while 'width' is the
horizontal width and 'height' the vertical height. If the width is less that the
height the bar gauge will be drawn vertically with the graph growing from the
bottom towards the top. Otherwise it will be drawn horizontally with the graph
growing from the left towards the right.
'Fcolour' is the colour used for the gauge while 'Bcolour' is the background
colour. 'min' is the minimum value of the gauge and 'max' is the maximum
value (both floating point).
A multi colour gauge can be created using 'c1' to 'c4' for the colours and 'ta' to
'tc' for the thresholds used to determine when the colour will change.
'width', 'height', 'FColour', 'BColour', 'min' and 'max' are optional and will
default to the values used in the previous definition of a GUI BARGAUGE.
'c1', 'ta', 'c2', 'tb', 'c3', 'tc' and 'c4' are optional and if not specified the gauge
will use less colours. If all are omitted the gauge will be drawn using 'Fcolour'.
The section Advanced Graphics has a more detailed description.

GUI BUTTON #ref, caption$,
startX, startY, width, height [,
FColour] [,BColour]

This will draw a momentary button which is a square switch with the caption
on its face. When touched the visual image of the button will appear to be
depressed and the control's value will be 1. When the touch is removed the
value will revert to zero.
#ref' is the control's reference number. 'caption$' is the string to display on the
face of the button. It can be a single string with two captions separated by a |
character (e.g. "UP|DOWN"). When the button is up the first string will be
used and when pressed the second will be used.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours.
'width', 'height', FColour and 'BColour' are optional and default to that used in
previous controls or set with the COLOUR command.

GUI CAPTION #ref, text$,
startX, startY [,align$]
[, FColour] [, BColour]

This will draw a text string on the screen.
'#ref' is the control's reference number.
'text$' is the string to display. 'startX' and 'startY' are the top left coordinates.
'align$' is zero to three characters (a string expression or variable is also
allowed) where the first letter is the horizontal alignment around X and can be
L, C or R for LEFT, CENTER, RIGHT and the second letter is the vertical
alignment around Y and can be T, M or B for TOP, MIDDLE, BOTTOM. A
third character can be used in the string to indicate the rotation of the text.
This can be 'N' for normal orientation, 'V' for vertical text with each character
under the previous running from top to bottom, 'I' the text will be inverted (i.e.
upside down), 'U' the text will be rotated counter clockwise by 90º and 'D' the
text will be rotated clockwise by 90º. The default alignment is left/top with no
rotation.
'FColour and 'BColour' are RGB values for the foreground and background
colours. On a display that supports transparent text BColour can be -1 which
means that the background will show through the gaps in the characters.
FColour and 'BColour' are optional and default to the colours set by the
COLOUR command.



GUI CHECKBOX #ref,
caption$, startX, startY [, size]
[, colour]

This will draw a check box which is a small box with a caption. When
touched an X will be drawn inside the box to indicate that this option has been
selected and the control's value will be set to 1. When touched a second time
the check mark will be removed and the control's value will be zero.
'#ref' is the control's reference number.
The string 'caption$' will be drawn to the right of the control using the colours
set by the COLOUR command.
'startX' and 'startY' are the top left coordinates while 'size' set the height and
width (the bix is square). 'colour' is an RGB value for the drawing colour.
'size' and 'colour' are optional and default to that used in previous controls.

GUI DELETE #ref1 [,#ref2,
#ref3, etc]
or
GUI DELETE ALL

This will delete the controls in the list. This includes removing the image of
the control from the screen using the current background colour and freeing the
memory used by the control.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will delete all controls.

GUI DISABLE #ref1 [,#ref2,
#ref3, etc]
or
GUI DISABLE ALL

This will disable the controls in the list. Disabled controls do not respond to
touch and will be displayed dimmed.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will disable all controls.
GUI ENABLE can be used to restore the controls.

GUI DISPLAYBOX #ref,
startX, startY, width, height,
FColour, BColour

This will draw a box with rounded corners that can be used to display a string
'#ref' is the control's reference number.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls.
Any text can be displayed in the box by using the CtrlVal(r) = command. This
is useful for displaying text, numbers and messages.
This control does not respond to touch.

GUI ENABLE #ref1 [,#ref2,
#ref3, etc]
or
GUI ENABLE ALL

This will undo the effects of GUI DISABLE and restore the control(s) to
normal operation.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will disable all controls.

GUI FCOLOUR colour, #ref1
[, #ref2, #ref3, etc]

This will change the foreground colour of the specified controls to 'colour'
which is an RGB value for the drawing colour.
'#ref' is the control's reference number.

GUI FORMATBOX #ref,
Format, startX, startY, width,
height, FColour, BColour

This will draw a box with rounded corners that can be used to create a virtual
keypad for entry of data using a specific format.
'#ref' is the control's reference number.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls.
The 'Format' argument specifies the format of the entry as follows:
DATE1
Date in UK/Aust/NZ format (dd/mm/yy)
DATE2
Date in USA format (mm/dd/yy)
DATE3
Date in international format (yyyy/mm/dd)
TIME1
Time in 24 hour notation (hh:mm)
TIME2
Time in 24 hour notation with seconds (hh:mm:ss)
TIME3
Time in 12 hour notation (hh:mm AM/PM)
TIME4
Time in 12 hour notation with seconds (hh:mm:ss AM/PM)



DATETIME1 Date (UK fmt) and time (12 hour) (dd/mm/yy hh:mm AM/PM)
DATETIME2 Date (UK fmt) and time (24 hour) (dd/mm/yy hh:mm)
DATETIME3 Date (USA fmt) and time (12 hour) (mm/dd/yy hh:mm AM/PM)
DATETIME4 Date (USA fmt) and time (24 hour) (mm/dd/yy hh:mm)
LAT1
Latitude in degrees, minutes and seconds (dd° mm' ss" N/S)
LAT2
Latitude with seconds to one decimal place (dd° mm' ss.s" N/S)
LONG1
Longitude in degrees, minutes and seconds (ddd° mm' ss" E/W)
LONG2
Longitude seconds to one decimal place (ddd° mm' ss.s" E/W)
ANGLE1
Angle in degrees and minutes (ddd° mm')
For example, this command:
GUI FORMATBOX #1, LAT1, 50, 50, 300, 50

would create a format box which would accept the entry of latitude in the
format of dd° mm' ss" N/S. The value of CtrlVal(#1) would be a string which
includes the numbers and separating characters. For example an entry of 17
degrees, 32 minutes and 1 second south would result in the string 17° 32' 01" S
MMBasic will try to position the virtual keypad on the screen so as to not
obscure the format box that caused it to appear. A pen down interrupt will be
generated just before the keypad is deployed and a key up interrupt will be
generated when the entry is complete and the keypad is hidden. .
GUI FORMATBOX
CANCEL

This will dismiss a virtual keypad if it is displayed on the screen. It is the same
as if the user touched the cancel key except that the touch up interrupt is not
generated. If a keypad is not displayed this command will do nothing.

GUI FRAME #ref, caption$,
startX, startY, width, height,
colour

This will draw a frame which is a box with round corners and a caption.
'#ref' is the control's reference number.
'caption$' is a string to display as the caption. 'startX' and 'startY' are the top
left coordinates while 'width' and 'height' set the dimensions. 'colour' is an
RGB value for the drawing colour. 'width', 'height' and 'colour' are optional and
default to that used in previous controls.
A frame is useful when a group of controls need to be visually brought
together. It is also used to surround a group of radio buttons and MMBasic
will arrange for the radio buttons surrounded by the frame to be exclusive. i.e.
when one radio button is selected any other button that was selected and within
the frame will be automatically deselected.
A frame does not respond to touch.

GUI GAUGE #ref, StartX,
StartY, Radius, FColour,
BColour, min, max, nbrdec,
units$, c1, ta, c2, tb, c3, tc, c4

Define a graphical circular analogue gauge with a digital display in the centre.
'#ref' is the control's reference number.
'StartX' and 'StartY' are the coordinates of the centre of the gauge, 'Radius' is
the distance from the centre to the outer edge.
'min' is the minimum value of the gauge and 'max' is the maximum value (both
floating point).
'nbrdec' specifies the number of decimal places to be used when drawing the
digital value in the centre of the gauge. Under this 'units$' will be displayed.
'Fcolour' is the colour used for the gauge while 'Bcolour' is the background
colour. A multi colour gauge can be created using 'c1' to 'c4' for the colours
and 'ta' to 'tc' for the thresholds used to determine when the colour will change.
When colours and thresholds are specified the background of the gauge will be
drawn with a dull version of the colour at that level. Also the digital value will
change to the colour specified by the current value.
'Radius', 'FColour', 'BColour', 'min', 'max', 'nbrdec' and 'units$' are optional and
will default to the values used in the previous definition of a GUI GAUGE.
'c1', 'ta', 'c2', 'tb', 'c3', 'tc' and 'c4' are optional and if not specified the gauge
will use less colours. If all are omitted the gauge will be drawn using 'Fcolour'.
The section Advanced Graphics has a more detailed description.



GUI HIDE #ref1 [,#ref2,
#ref3, etc]
or
GUI HIDE ALL

This will hide the controls in the list. Hidden controls do not respond to touch
and will not be visible.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will hide all controls.
GUI SHOW can be used to restore the controls.

GUI INTERRUPT down [, up]

This command will setup an interrupt that will be triggered on a touch on the
LCD panel and optionally if the touch is released.
'down' is the subroutine to call when a touch down has been detected. 'up' is
the subroutine to call when the touch has been lifted from the screen ('up' and
'down' can point to the same subroutine if required).
Specifying the number zero (single digit) as the argument will cancel both of
these interrupts. ie: GUI INTERRUPT 0.

GUI LED #ref, caption$,
centerX, centerY, radius,
colour

This will draw an indicator light which looks like a panel mounted LED. A
LED does not respond to touch.
'#ref' is the control's reference number.
The string 'caption$' will be drawn to the right of the control using the colours
set by the COLOUR command.
'centerX' and 'centerY' are the coordinates of the centre of the LED and 'radius'
is the radius of the LED. 'colour' is an RGB value for the drawing colour.
'radius' and 'colour' are optional and default to that used in previous controls.
When a LED's value is set to a value of one it will be illuminated and when it
is set to zero it will be off (a dull version of its colour attribute). The LED can
be made to flash on then off by setting the value of the LED to a number
greater than one which is the time in milliseconds that it should remain on.
The colour can be changed with the GUI FCOLOUR command.

GUI NUMBERBOX #ref,
startX, startY, width, height,
FColour, BColour

This will draw a box with rounded corners that can be used to create a virtual
numeric keypad for data entry.
'#ref' is the control's reference number.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls.
When the box is touched a numeric keypad will appear on the screen. Using
this virtual keypad any number can be entered into the box including a floating
point number in exponential format. The new number will replace the number
previously in the box.
The value of the control can set to a literal string (not an expression) starting
with two hash characters. For example: CtrlVal(nnn) = "##Enter Number"
and in that case the string (without the leading two hash characters) will be
displayed in the box with reduced brightness. This can be used to give the user
a hint as to what should be entered (called "ghost text"). Reading the value of
the control displaying ghost text will return zero. When the control is used
normally the ghost text will vanish.
MMBasic will try to position the virtual keypad on the screen so as to not
obscure the number box that caused it to appear. A pen down interrupt will be
generated just before the keypad is deployed and a key up interrupt will be
generated when the Enter key is touched and the keypad is hidden. Also, when
the Enter key is touched the entered number will be evaluated as a number and
the NUMBERBOX control redrawn to display this number.

GUI NUMBERBOX
CANCEL

This will dismiss a virtual keypad if it is displayed on the screen. It is the same
as if the user touched the cancel key except that the touch up interrupt is not
generated. If a keypad is not displayed this command will do nothing.

GUI PAGE #n [,#n2, #n3, etc]

This will switch the display to show controls that have been assigned (via the



GUI SETUP command) to the page numbers specified on the command line
(#n, #n2, etc). Any controls that were displayed but are not on the current list
of pages will be automatically hidden. Any controls on a page that was
displayed on the old screen and is also specified in the new PAGE command
will remain unaffected.
The default when a program starts running is PAGE 1 and GUI SETUP 1.
This means that if these commands are not used the program will run as
normal showing all GUI controls that have been defined.
See also the GUI SETUP command.
GUI RADIO #ref, caption$,
centerX, centerY, radius,
colour

This will draw a radio button with a caption.
'#ref' is the control's reference number.
The string 'caption$' will be drawn to the right of the control using the colours
set by the COLOUR command.
'centerX' and 'centerY' are the coordinates of the centre of the button and
'radius' is the radius of the button. 'colour' is an RGB value for the drawing
colour. 'radius' and 'colour' are optional and default to that used in previous
controls.
When touched the centre of the button will be illuminated to indicate that this
option has been selected and the control's value will be 1. When another radio
button is selected the mark on this button will be removed and its value will be
zero. Radio buttons are grouped together when surrounded by a frame and
when one button in the group is selected all others in the group will be
deselected. If a frame is not used all buttons on the screen will be grouped
together.

GUI REDRAW #ref1 [,#ref2,
#ref3, etc]
or
GUI REDRAW ALL

This will redraw the controls on the screen. It is useful if the screen image has
somehow been corrupted.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will first clear the screen then redraw all controls. This is
useful if the whole screen needs to be refreshed.

GUI SETUP #n

This will allocate any new controls created to the page '#n'.
This command can be used as many times as needed while GUI controls are
being defined. The default when a program starts running is GUI SETUP 1.
See also the GUI PAGE command.

GUI SHOW #ref1 [,#ref2,
#ref3, etc]
or
GUI SHOW ALL

This will undo the effects of GUI HIDE and restore the control(s) to being
visible and capable of normal operation.
'#ref' is the control's reference number. The keyword ALL can be used as the
argument and that will disable all controls.

GUI SPINBOX #ref, startX,
startY, width, height, FColour,
BColour, Step, Minimum,
Maximum

This will draw a box with up/down icons on either end. When these icons are
touched the number in the box will be incremented or decremented. Holding
down the up/down icons will repeat the step at a fast rate.
'#ref' is the control's reference number.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls.
'Step' sets the amount to increment/decrement the number with each touch.
'Minimum' and 'Maximum' set limits on the number that can be entered. All
three parameters can be floating point numbers and are optional. The default
for 'Step' is 1 and 'Minimum' and 'Maximum' if omitted will default to no limit.

GUI SWITCH #ref, caption$,
startX, startY, width, height,
FColour, BColour

This will draw a latching switch which is a square switch that latches when
touched.
'#ref' is the control's reference number.
'caption$' is a string to display as the caption on the face of the switch. 'startX'



and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls.
When touched the visual image of the button will appear to be depressed and
the control's value will be 1. When touched a second time the switch will be
released and the value will revert to zero. Caption can consist of two captions
separated by a | character (e.g. "ON|OFF"). When this is used the switch will
appear to be a toggle switch with each half of the caption used to label each
half of the toggle switch.
GUI TEXTBOX #ref, startX,
startY, width, height, FColour,
BColour

This will draw a box with rounded corners that can be used to create a virtual
keyboard for data entry
'#ref' is the control's reference number.
'startX' and 'startY' are the top left coordinates while 'width' and 'height' set the
dimensions. ' FColour and 'BColour' are RGB values for the foreground and
background colours. 'width', 'height', FColour and 'BColour' are optional and
default to that used in previous controls. On a display that supports transparent
text BColour can be -1 which means that the background will show through
the gaps in the characters.
When the box is touched a QWERTY keyboard will appear on the screen.
Using this virtual keyboard any text can be entered into the box including
upper/lower case letters, numbers and any other characters in the ASCII
character set. The new text will replace any text previously in the box.
The value of the control can set to a string starting with two hash characters.
For example: CtrlVal(nnn) = "##Enter Filename" and in that case the string
(without the leading two hash characters) will be displayed in the box with
reduced brightness. This can be used to give the user a hint as to what should
be entered (called "ghost text"). Reading the value of the control displaying
ghost text will return an empty string. When the control is used normally the
ghost text will vanish.
MMBasic will try to position the virtual keyboard on the screen so as to not
obscure the text box that caused it to appear. A pen down interrupt will be
generated just before the keyboard is deployed and a key up interrupt will be
generated when the Enter key is touched and the keyboard is hidden. .

GUI TEXTBOX CANCEL

This will dismiss a virtual keyboard if it is displayed on the screen. It is the
same as if the user touched the cancel key except that the touch up interrupt is
not generated. If a keyboard is not displayed this command will do nothing.

GUI BITMAP x, y, bits [,
width] [, height] [, scale] [,
c] [, bc]

Displays the bits in a bitmap on an LCD panel starting at 'x' and 'y' on an
attached LCD panel.
'height' and 'width' are the dimensions of the bitmap as displayed on the LCD
panel and default to 8x8.
'scale' is optional and defaults to that set by the FONT command.
'c' is the drawing colour and 'bc' is the background colour. They are optional
and default to the current foreground and background colours.
The bitmap can be an integer or a string variable or constant and is drawn
using the first byte as the first bits of the top line (bit 7 first, then bit 6, etc)
followed by the next byte, etc. When the top line has been filled the next line
of the displayed bitmap will start with the next bit in the integer or string.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

GUI CALIBRATE

This command is used to calibrate the touch feature on an LCD panel. It will
display a series of targets on the screen and wait for each one to be precisely
touched.
The command can also be used with five arguments which specify the
calibration values and in this case the calibration will be done without

or
GUI CALIBRATE a,b,c,d,d



displaying any targets or requiring an input from the user. To discover the
values use the OPTION LIST after calibrating the display normally. Note that
these values are specific to that display and can vary considerably.
GUI RESET LCDPANEL

Will reinitialise the configured LCD panel. Initialisation is automatically done
when the PicoMite starts up but in some circumstances it may be necessary to
interrupt power to the LCD panel (e.g. to save battery power) and this
command can then be used to reinitialise the display.

GUI TEST LCDPANEL
or
GUI TEST TOUCH

Will test the display or touch feature on an LCD panel.
With GUI TEST LCDPANEL an animated display of colour circles will be
rapidly drawn on top of each other.
With GUI TEST TOUCH the screen will blank and wait for a touch which will
cause a white dot to be placed on the display marking the touch position on the
screen.
Any character entered at the console will terminate the test.

I2C OPEN speed, timeout

Enables the first I2C module in master mode. ‘speed’ is the clock speed (in
KHz) to use and must be one of 100, 400 or 1000.
‘timeout’ is a value in milliseconds after which the master send and receive
commands will be interrupted if they have not completed. The minimum value
is 100. A value of zero will disable the timeout (though this is not
recommended).

I2C WRITE addr, option,
sendlen, senddata [,sendata ..]

Send data to the I2C slave device. ‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘sendlen’ is the number of bytes to send. ‘senddata’ is the data to be sent - this
can be specified in various ways (all values sent will be between 0 and 255).
Notes:
 The data can be supplied as individual bytes on the command line.
Example: I2C WRITE &H6F, 0, 3, &H23, &H43, &H25
 The data can be in a one dimensional array specified with empty brackets
(i.e. no dimensions). ‘sendlen’ bytes of the array will be sent starting with
the first element.
Example: I2C WRITE &H6F, 0, 3, ARRAY()
The data can be a string variable (not a constant).
Example: I2C WRITE &H6F, 0, 3, STRING$

I2C READ addr, option,
rcvlen, rcvbuf

I2C CLOSE

I2C SLAVE
I2C2


Get data from the I2C slave device. ‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘rcvlen’ is the number of bytes to receive.
‘rcvbuf’ is the variable or array used to save the received data - this can be:
 A string variable. Bytes will be stored as sequential characters.
 A one dimensional array of numbers specified with empty brackets.
Received bytes will be stored in sequential elements of the array starting
with the first.
Example: I2C READ &H6F, 0, 3, ARRAY()
A normal numeric variable (in this case rcvlen must be 1).
Disables the master I2C module. This command will also send a stop if the bus
is still held.
See Appendix B
The same set of commands as for I2C (above) but applying to the second I2C
channel.


IF expr THEN stmt [: stmt]
or
IF expr THEN stmt ELSE stmt

Evaluates the expression ‘expr' and performs the statement following the
THEN keyword if it is true or skips to the next line if false. If there are more
statements on the line (separated by colons (:) they will also be executed if true
or skipped if false. The ELSE keyword is optional and if present the
statement(s) following it will be executed if 'expr' resolved to be false.
The ‘THEN statement’ construct can be also replaced with:
GOTO linenumber | label’.
This type of IF statement is all on one line.

IF expression THEN
<statements>
[ELSEIF expression THEN
<statements>]
[ELSE
<statements>]
ENDIF

Multiline IF statement with optional ELSE and ELSEIF cases and ending with
ENDIF. Each component is on a separate line.
Evaluates 'expression' and performs the statement(s) following THEN if the
expression is true or optionally the statement(s) following the ELSE statement
if false. The ELSEIF statement (if present) is executed if the previous
condition is false and it starts a new IF chain with further ELSE and/or
ELSEIF statements as required.
One ENDIF is used to terminate the multiline IF.

INC var [,increment]

Increments the variable “var” by either 1 or, if specified, the value in
increment. “increment” can have a negative. This is functionally the same as
var = var + increment
but is processed much faster

INPUT ["prompt$";] var1
[,var2 [, var3 [, etc]]]

Will take a list of values separated by commas (,) entered at the console and
will assign them to a sequential list of variables.
For example, if the command is: INPUT a, b, c
And the following is typed on the keyboard: 23, 87, 66
Then a = 23 and b = 87 and c = 66
The list of variables can be a mix of float, integer or string variables. The
values entered at the console must correspond to the type of variable.
If a single value is entered a comma is not required (however that value cannot
contain a comma).
‘prompt$’ is a string constant (not a variable or expression) and if specified it
will be printed first. Normally the prompt is terminated with a semicolon (;)
and in that case a question mark will be printed following the prompt. If the
prompt is terminated with a comma (,) rather than the semicolon (;) the
question mark will be suppressed.

INPUT #nbr,
list of variables

Same as above except that the input is read from a serial port or file previously
opened for INPUT as ‘nbr’. See the OPEN command.

INTERRUPT [myint]

This command triggers a software interrupt. The interrupt is set up using
INTERRUPT ‘myint’ where ‘myint’ is the name of a subroutine that will be
executed when the interrupt is triggered.
Use INTERRUPT 0 to disable the interrupt
Use INTERRUPT without parameters to trigger the interrupt.
NB: the interrupt can also be triggered from within a CSUB

IR dev, key , int
or
IR CLOSE

Decodes NEC or Sony infrared remote control signals.
An IR Receiver Module is used to sense the IR light and demodulate the
signal. It can be connected to any pin however this pin must be configured in
advanced using the command: SETPIN n, IR
The IR signal decode is done in the background and the program will continue
after this command without interruption. 'dev' and 'key' should be numeric
variables and their values will be updated whenever a new signal is received
('dev' is the device code transmitted by the remote and 'key' is the key pressed).
'int' is a user defined subroutine that will be called when a new key press is
received or when the existing key is held down for auto repeat. In the interrupt



subroutine the program can examine the variables 'dev' and 'key' and take
appropriate action.
The IR CLOSE command will terminate the IR decoder.
Note that for the NEC protocol the bits in 'dev' and 'key' are reversed. For
example, in 'key' bit 0 should be bit 7, bit 1 should be bit 6, etc. This does not
affect normal use but if you are looking for a specific numerical code provided
by a manufacturer you should reverse the bits. This describes how to do it:
http://www.thebackshed.com/forum/forum_posts.asp?TID=8367
See the section Special Hardware Devices for more details.
IR SEND pin, dev, key

Generate a 12-bit Sony Remote Control protocol infrared signal.
'pin' is the I/O pin to use. This can be any I/O pin which will be automatically
configured as an output and should be connected to an infrared LED. Idle is
low with high levels indicating when the LED should be turned on.
'dev' is the device being controlled and is a number from 0 to 31, 'key' is the
simulated key press and is a number from 0 to 127.
The IR signal is modulated at about 38KHz and sending the signal takes about
25mS during which program execution is paused.

KEYPAD var, int, r1, r2, r3,
r4, c1, c2, c3 [, c4]
or
KEYPAD CLOSE

Monitor and decode key presses on a 4x3 or 4x4 keypad.
Monitoring of the keypad is done in the background and the program will
continue after this command without interruption. 'var' should be a numeric
variable and its value will be updated whenever a key press is detected.
'int' is a user defined subroutine that will be called when a new key press is
received. In the interrupt subroutine the program can examine the variable 'var'
and take appropriate action.
r1, r2, r3 and r4 are pin numbers used for the four row connections to the
keypad and c1, c2, c3 and c4 are the column connections. c4 is optional and is
only used with 4x4 keypads. This command will automatically configure these
pins as required.
On a key press the value assigned to 'var' is the number of a numeric key (e.g.
'6' will return 6) or 10 for the * key and 11 for the # key. On 4x4 keypads the
number 20 will be returned for A, 21 for B, 22 for C and 23 for D.
The KEYPAD CLOSE command will terminate the keypad function and
return the I/O pin to a not configured state.
See the section Special Hardware Devices for more details.

KILL file$ [,all]

Deletes the file specified by ‘file$’. Any extension must be specified.
Bulk erase is triggered if fname$ contains a '*' or a '?' character
If the optional 'all' parameter is used then you will be prompted for a single
confirmation. If 'all' is not specified you will be prompted on each file.

LET variable = expression

Assigns the value of 'expression' to the variable. LET is automatically
assumed if a statement does not start with a command. For example:
Var = 56

LIBRARY SAVE
or
LIBRARY DELETE
or
LIBRARY LIST
Or
LIBRARY LIST ALL
Or
LIBRARY DISK SAVE
fname$

The library is a special segment of program memory that can contain program
code such as subroutines, functions and CFunctions. These routines are not
visible to the programmer but are available to any program running on the
Micromite and act the same as built in commands and functions in MMBasic.
Any code in the library that is not contained within a subroutine or function
will be executed immediately before a program is run. This can be used to
initialise constants, set options, etc. See the heading "The Library" in this
manual for a full explanation.
The library is stored in program memory Flash Slot 3 which will then not be
available for saving a program (slots 1 to 2 will still be available).
LIBRARY SAVE will take whatever is in normal program memory, compress
it (remove redundant data such as comments) and append it to the library area



Or
LIBRARY DISK LOAD
fname$

(main program memory is then empty). The code in the library will not show
in LIST or EDIT and will not be deleted when a new program is loaded or
NEW is used.
LIBRARY DELETE will remove the library and return Flash Slot 3 for normal
use (OPTION RESET will do the same).
LIBRARY LIST will list the contents of the library. Use ALL to list without
page confirmations.
LIBRARY DISK SAVE fname$ will save the current library as a binary file
allowing a subsequent call to LIBRARY DISK LOAD fname$ to restore the
library. Together, these allow libraries specific for individual programs to be
stored and restored easily and distributed. Other than using version specific
functionality in the library (WEB, VGA, GUI) libraries can be shared between
versions.

LINE x1, y1, x2, y2 [, LW [,
C]]

On an attached LCD display this command will draw a line starting at the
coordinates ‘x1’ and ‘y1’ and ending at ‘x2’ and ‘y2’.
‘LW’ is the line’s width and is only valid for horizontal or vertical lines. It
defaults to 1 if not specified or if the line is a diagonal. ‘C’ is an integer
representing the colour and defaults to the current foreground colour.
All parameters can be expressed as arrays and the software will plot the
number of lines as determined by the dimensions of the smallest array. 'x1',
'y1', 'x2', and 'y2' must all be arrays or all be single variables /constants
otherwise an error will be generated. 'lw' and 'c' can be either arrays or single
variables/constants.

LINE AA x1, y1, x2, y2 [,
LW [, C]]

Draws a line with anti-aliasing . The parameters are as per the LINE command
above. However this version will use variable intensity values of the specified
colour to reduce the “staggered” quality of diagonal lines. In addition this
version can draw diagonal lines of any width. Note that it does not accept
arrays as parameters.

LINE GRAPH x(),y(),colour

This command generates a line graph of the coordinate pairs specified in “x()”
and “y()”. The graph will have n-1 segments where there a n elements in the x
and y arrays.

LINE INPUT [prompt$,]
string-variable$

Reads an entire line from the console input into ‘string-variable$’.
‘prompt$’ is a string constant (not a variable or expression) and if specified it
will be printed first. A question mark is not printed unless it is part of
‘prompt$’. Unlike INPUT, this command will read a whole line, not stopping
for comma delimited data items.

LINE INPUT #nbr,
string-variable$

Same as above except that the input is read from a serial communications port
or a file previously opened for INPUT as ‘nbr’. See the OPEN command.

LINE PLOT ydata() [,nbr]
[,xstart] [,xinc] [,ystart] [,yinc]
[,colour]

Plots a line graph from an array of y-axis data points.
‘ydata’ is an array of floats or integers to be plotted
‘nbr ‘is the number of line segments to be plotted - defaults to the lesser of the
array size and MM.HRES-2 if omitted
‘xstart’ is the x-coordinate to start plotting - defaults to 0
‘xinc’ is the increment along the x-axis to plot each coordinate - defaults to 1
‘ystart’ is the location in ydata to start the plot - defaults to the array start
‘yinc’ is the increment in ydata to add for each point to be plotted
‘colour’ is the colour to draw the line

LIST [fname$]
or
LIST ALL [fname$]

List a program on the console.
LIST on its own will list the program with a pause at every screen full.
LIST ALL will list the program without pauses. This is useful if you wish to
transfer the program to a terminal emulator on a PC that has the ability to
capture its input stream to a file. If the optional ‘fname$’ is specified then that



file on the Flash Filesystem or SD Card will be listed.
LIST COMMANDS
or
LIST FUNCTIONS

Lists all valid commands or functions

LOAD file$ [,R]

Loads a program called ‘file$’ from the Flash Filesystem or SD Card into program
memory. If the optional suffix ,R is added the program will be immediately run
without prompting (in this case ‘file$’ must be a string constant).
If an extension is not specified “.BAS” will be added to the file name.

LOAD IMAGE file$ [, x] [, y]

Load a bitmapped image from the Flash Filesystem or SD Card and display it
on the LCD panel. ''file$' is the name of the file and 'x' and 'y' are the screen
coordinates for the top left hand corner of the image. If the coordinates are not
specified the image will be drawn at the top left hand position on the screen.
If an extension is not specified “.BMP” will be added to the file name.
All types of the BMP format are supported including black and white and true
colour 24-bit images.

LOAD JPG file$ [, x] [, y]

Load a jpg image from the Flash Filesystem or SD Card and display it on the
LCD panel. ''file$' is the name of the file and 'x' and 'y' are the screen
coordinates for the top left hand corner of the image. If the coordinates are not
specified the image will be drawn at the top left hand position on the screen.
If an extension is not specified “.JPG” will be added to the file name.
Progressive jpg images are not supported.

LOCAL variable [, variables]
See DIM for the full syntax.

Defines a list of variable names as local to the subroutine or function. This
command uses exactly the same syntax as DIM and will create variables that
will only be visible within the subroutine or function. They will be
automatically discarded when the subroutine or function exits.

LONGSTRING

The LONGSTRING commands allow for the manipulation of strings longer
than the normal MMBasic limit of 255 characters.
Variables for holding long strings must be defined as single dimensioned
integer arrays with the number of elements set to the number of characters
required for the maximum string length divided by eight. The reason for
dividing by eight is that each integer in an MMBasic array occupies eight
bytes. Note that the long string routines do not check for overflow in the
length of the strings. If an attempt is made to create a string longer than a long
string variable's size the outcome will be undefined.

LONGSTRING APPEND
array%(), string$

Append a normal MMBasic string to a long string variable. array%() is a long
string variable while string$ is a normal MMBasic string expression.

LONGSTRING CLEAR
array%()

Will clear the long string variable array%(). i.e. it will be set to an empty
string.

LONGSTRING COPY
dest%(), src%()

Copy one long string to another. dest%() is the destination variable and src%()
is the source variable. Whatever was in dest%() will be overwritten.

LONGSTRING CONCAT
dest%(), src%()

Concatenate one long string to another. dest%() is the destination variable and
src%() is the source variable. src%() will the added to the end of dest%() (the
destination will not be overwritten).

LONGSTRING LCASE
array%()

Will convert any uppercase characters in array%() to lowercase. array%() must
be long string variable.

LONGSTRING LEFT
dest%(), src%(), nbr

Will copy the left hand 'nbr' characters from src%() to dest%() overwriting
whatever was in dest%(). i.e. copy from the beginning of src%(). src%() and
dest%() must be long string variables. 'nbr' must be an integer constant or
expression.

LONGSTRING LOAD
array%(), nbr, string$

Will copy 'nbr' characters from string$ to the long string variable array%()
overwriting whatever was in array%().



LONGSTRING MID dest%(),
src%(), start, nbr

Will copy 'nbr' characters from src%() to dest%() starting at character position
'start' overwriting whatever was in dest%(). i.e. copy from the middle of
src%(). 'nbr' is optional and if omitted the characters from 'start' to the end of
the string will be copied src%() and dest%() must be long string variables.
'start' and 'nbr' must be an integer constants or expressions.

LONGSTRING PRINT [#n,]
src%()

Prints the longstring stored in ‘src%()’ to the file or COM port opened as ‘#n’.
If ‘#n’ is not specified the output will be sent to the console.

LONGSTRING REPLACE
array%() , string$, start

Will substitute characters in the normal MMBasic string string$ into an
existing long string array%() starting at position ‘start’ in the long string.

LONGSTRING RESIZE
addr%(), nbr

Sets the size of the longstring to nbr. This overrides the size set by other
longstring commands so should be used with caution. Typical use would be in
using a longstring as a byte array.
Will copy the right hand 'nbr' characters from src%() to dest%() overwriting
whatever was in dest%(). i.e. copy from the end of src%(). src%() and dest%()
must be long string variables. 'nbr' must be an integer constant or expression.
Sets byte nbr to the value “data”, nbr respects OPTION BASE

LONGSTRING RIGHT
dest%(), src%(), nbr
LONGSTRING SETBYTE
addr%(), nbr, data
LONGSTRING TRIM
array%(), nbr

Will trim ‘nbr’ characters from the left of a long string. array%() must be a
long string variables. 'nbr' must be an integer constant or expression.

LONGSTRING UCASE
array%()

Will convert any lowercase characters in array%() to uppercase. array%() must
be long string variable.

LOOP [UNTIL expression]
MATH

Terminates a program loop: see DO.
The math command performs many simple mathematical calculations that can
be programmed in BASIC but there are speed advantages to coding looping
structures in the firmware and there is the advantage that once debugged they
are there for everyone without re-inventing the wheel. Note: 2 dimensional
maths matrices are always specified DIM matrix(n_columns, n_rows) and of
course the dimensions respect OPTION BASE. Quaternions are stored as a 5
element array w, x, y, z, magnitude.

MATH RANDOMIZE [n]

Seeds the Mersenne Twister algorithm.
If n is not specified the seed is the time in microseconds since boot
The Mersenne Twister algorithm gives a much better random number than the
C-library inbuilt function

Simple array arithmetic
MATH SET nbr, array()

Sets all elements in array() to the value nbr. Note this is the fastest way of
clearing an array by setting it to zero.

MATH SCALE in(), scale
,out()

This scales the matrix in() by the scalar scale and puts the answer in out().
Works for arrays of any dimensionality of both integer and float and can
convert between. Setting b to 1 is optimised and is the fastest way of copying
an entire array.

MATH ADD in(), num ,out()

This adds the value 'num' to every element of the matrix in() and puts the
answer in out(). Works for arrays of any dimensionality of both integer and
float and can convert between. Setting num to 0 is optimised and is a fast way
of copying an entire array. in() and out() can be the same array.

MATH INTERPOLATE in1(),
in2(), ratio, out()

This command implements the following equation on every array element:
out = (in2 - in1) * ratio + in1
Arrays can have any number of dimensions and must be distinct and have the



same number of total elements. The command works with both integer and
floating point arrays in any mixture

MATH WINDOW in(),
minout, maxout, out() [,minin,
maxin]

This command takes the “in” array and scales it between “minout” and
“maxout” returning the answer in “out”. Optionally, it can also return the
minimum and maximum values found in the original data (“minin” and
“minout”).
Note: “minout” can be greater than “maxout” and in this case the data will be
both scaled and inverted.
e.g
DIM IN(2)=(1,2,3)
DIM OUT(2)
MATH WINDOW IN(),7,3,OUT(),LOW,HIGH
Will return OUT(0)=7, OUT(1)=5,OUT(2)=3,LOW=1,HIGH=3
This command can massively simplify scaling data for plotting etc.

MATH SLICE sourcearray(),
[d1] [,d2] [,d3] [,d4] [,d5] ,
destinationarray()

This command copies a specified set of values from a multi-dimensional array
into a single dimensional array. It is much faster than using a FOR loop. The
slice is specified by giving a value for all but one of the source array indices
and there should be as many indices in the command, including the blank one,
as there are dimensions in the source array
e.g.
OPTION BASE 1
DIM a(3,4,5)
DIM b(4)
MATH SLICE a(), 2, , 3, b()
Will copy the elements 2,1,3 and 2,2,3 and 2,3,3 and 2,4,3 into array b()

MATH INSERT targetarray(),
[d1] [,d2] [,d3] [,d4] [,d5] ,
sourcearray()

This is the opposite of MATH SLICE, has a very similar syntax, and allows
you, for example, to substitute a single vector into an array of vectors with a
single instruction
e.g.
OPTION BASE 1
DIM targetarray(3,4,5)
DIM sourcearray(4)=(1,2,3,4)
MATH INSERT targetarray(), 2, , 3, sourcearray()
Will set elements 2,1,3 = 1 and 2,2,3 = 2 and 2,3,3 = 3 and 2,4,3 = 4

MATH SHIFT inarray%(),
nbr, outarray%() [,U]

This command does a bit shift on all elements of inarray%() and places the
result in outarray%() (may be the same as inarray%()). nbr can be between -63
and 63. Positive numbers are a left shift (multiply by power of 2). Negative
number are a right shift. The optional parameter ,U will force an unsigned
shift.

Matrix arithmetic
MATH M_INVERSE array!(),
inversearray!()

This returns the inverse of array!() in inversearray!(). The array must be square
and you will get an error if the array cannot be inverted (determinant=0).
array!() and inversearray!() cannot be the same.

MATH M_PRINT array()

Quick mechanism to print a 2D matrix one row per line.

MATH M_TRANSPOSE in(),
out()

Transpose matrix in() and put the answer in matrix out(), both arrays must be
2D but need not be square. If not square then the arrays must be dimensioned
in(m,n) out(n,m)



MATH M_MULT in1(), in2(),
out()

Multiply the arrays in1() and in2() and put the answer in out()c. All arrays
must be 2D but need not be square. If not square then the arrays must be
dimensioned in1(m,n) in2(p,m) ,out(p,n)

Vector arithmetic

MATH V_PRINT array()

Quick mechanism to print a small array on a single line

MATH V_NORMALISE
inV(), outV()

Converts a vector inV() to unit scale and puts the answer in outV()
(sqr(x*x + y*y +....)=1
There is no limit on number of elements in the vector

MATH V_MULT matrix(),
inV(), outV()

Multiplies matrix() and vector inV() returning vector outV(). The vectors and
the 2D matrix can be any size but must have the same cardinality.

MATH V_CROSS inV1(),
inV2(), outV()

Calculates the cross product of two three element vectors inV1() and inV2()
and puts the answer in outV()

MATH V_ROTATE x, y, a,
xin(), yin(), xout(), yout()

This command rotates the coordinate pairs in “xin()” and “yin()” around the
centre point defined by “x” and “y” by the angle “a” and puts the results in
“xout()” and “yout()”. NB: the input and output arrays can be the same and the
rotation angle is, by default, in radians but this can be changed using the
OPTION ANGLE command.

Quaternion arithmetic
MATH Q_INVERT inQ(),
outQ()

Invert the quaternion in inQ() and put the answer in outQ()

MATH Q_VECTOR x, y, z,
outVQ()

Converts a vector specified by x , y, and z to a normalised quaternion vector
outVQ() with the original magnitude stored

MATH Q_CREATE theta, x,
y, z, outRQ()

Generates a normalised rotation quaternion outRQ() to rotate quaternion
vectors around axis x,y,z by an angle of theta. Theta is specified in radians.

MATH Q_EULER yaw, pitch,
roll, outRQ()

Generates a normalised rotation quaternion outRQ() to rotate quaternion
vectors as defined by the yaw, pitch and roll angles
With the vector in front of the “viewer” yaw is looking from the top of the
ector and rotates clockwise, pitch rotates the top away from the camera and roll
rotates around the z-axis clockwise.
The yaw, pitch and roll angles default to radians but respect the setting of
OPTION ANGLE

MATH Q_MULT inQ1(),
inQ2(), outQ()

Multiplies two quaternions inQ1() and inQ2() and puts the answer in outQ()

MATH Q_ROTATE , RQ(),
inVQ(), outVQ()

Rotates the source quaternion vector inVQ() by the rotate quaternion RQ() and
puts the answer in outVQ()

MATH C_ADD array1%(), array2%(), array3%()
MATH C_SUB array1%(), array2%(), array3%()
MATH C_MUL array1%(), array2%(), array3%()
MATH C_DIV array1%(), array2%(), array3%()
MATH C_ADD array1!(), array2!(), array3!()
MATH C_SUB array1!(), array2!(), array3!()
MATH C_MUL array1!(), array2!(), array3!()
MATH C_DIV array1!(), array2!(), array3!()


These commands do cell by cell operations (hence C_) on
identically sized arrays. There are no restrictions on the
number of dimensions and no restrictions on using the
same array twice or even three times in the parameters.
The datatype must be the same for all the arrays.
e.g.
MATH C_MULT a%(),a%(),a%()
will square all the values in the array a%()


MATH FFT signalarray!(),
FFTarray!()

Performs a fast fourier transform of the data in “signalarray!”. "signalarray"
must be floating point and the size must be a power of 2 (e.g. s(1023)
assuming OPTION BASE is zero)
"FFTarray" must be floating point and have dimension 2*N where N is the
same as the signal array (e.g. f(1,1023) assuming OPTION BASE is zero)
The command will return the FFT as complex numbers with the real part in
f(0,n) and the imaginary part in f(1,n)

MATH FFT INVERSE
FFTarray!(), signalarray!()

Performs an inverse fast fourier transform of the data in “FFTarray!”.
"FFTarray" must be floating point and have dimension 2*N where N must be a
power of 2 (e.g. f(1,1023) assuming OPTION BASE is zero) with the real part
in f(0,n) and the imaginary part in f(1,n).
"signalarray" must be floating point and the single dimension must be the same
as the FFT array.
The command will return the real part of the inverse transform in
"signalarray".

MATH FFT MAGNITUDE
signalarray!(),magnitudearray!
()

Generates magnitudes for frequencies for the data in “signalarray!”
"signalarray" must be floating point and the size must be a power of 2 (e.g.
s(1023) assuming OPTION BASE is zero)
"magnitudearray" must be floating point and the size must be the same as the
signal array
The command will return the magnitude of the signal at various frequencies
according to the formula:
frequency at array position N = N * sample_frequency / number_of_samples

MATH FFT PHASE
signalarray!(), phasearray!()

Generates phases for frequencies for the data in “signalarray!”.
"signalarray" must be floating point and the size must be a power of 2 (e.g.
s(1023) assuming OPTION BASE is zero). "phasearray" must be floating
point and the size must be the same as the signal array
The command will return the phase angle of the signal at various frequencies
according to the formula above.

MATH SENSORFUSION
type ax, ay, az, gx, gy, gz, mx,
my, mz, pitch, roll, yaw [,p1]
[,p2]

Type can be MAHONY or MADGWICK
Ax, ay, and az are the accelerations in the three directions and should be
specified in units of standard gravitational acceleration.
Gx, gy, and gz are the instantaneous values of rotational speed which should
be specified in radians per second.
Mx, my, and mz are the magnetic fields in the three directions and should be
specified in nano-Tesla (nT)
Care must be taken to ensure that the x, y and z components are consistent
between the three inputs. So , for example, using the MPU-9250 the correct
input will be ax, ay,az, gx, gy, gz, my, mx, -mz based on the reading from the
sensor.
Pitch, roll and yaw should be floating point variables and will contain the
outputs from the sensor fusion.
The SENSORFUSION routine will automatically measure the time between
consecutive calls and will use this in its internal calculations.
The Madwick algorithm takes an optional parameter p1. This is used as beta in
the calculation. It defaults to 0.5 if not specified
The Mahony algorithm takes two optional parameters p1, and p2. These are
used as Kp and Ki in the calculation. If not specified these default to 10.0 and
0.0 respectively.
A fully worked example of using the code is given on the BackShed forum at:
https://www.thebackshed.com/forum/ViewTopic.php?TID=13459&PID=1669
62#166962



MEMORY

List the amount of memory currently in use. For example:
Program:
0K ( 0%) Program (0 lines)
160K (100%) Free
RAM:
0K ( 0%) 0 Variables
0K ( 0%) General
112K (100%) Free
Notes:
 Memory usage is rounded to the nearest 1K byte.
 General memory is used by serial I/O buffers, etc.

MEMORY SET address, byte,
numberofbytes
MEMORY SET BYTE
address, byte, numberofbytes
MEMORY SET SHORT
address, short, numberofshorts

This command will set a region of memory to a value.
BYTE = One byte per memory address.
SHORT = Two bytes per memory address.
WORD = Four bytes per memory address.
FLOAT = Eight bytes per memory address.
‘increment’ is optional and controls the increment of the ‘address’ pointer as
the operation is executed. For example, if increment=3 then only every third
element of the target is set. The default is 1.

MEMORY SET WORD
address, word, numberofwords
MEMORY SET INTEGER
address, integervalue
,numberofintegers [,increment]
MEMORY SET FLOAT
address, floatingvalue
,numberofloats [,increment]
MEMORY COPY
sourceaddress,
destinationaddres,
numberofbytes
MEMORY COPY INTEGER
sourceaddress,
destinationaddress,
numberofintegers
[,sourceincrement][,destination
increment]

This command will copy one region of memory to another.
COPY INTEGER and FLOAT will copy eight bytes per operation.
‘sourceincrement’ is optional and controls the increment of the ‘sourceaddress’
pointer as the operation is executed. For example, if sourceincrement=3 then
only every third element of the source will be copied. The default is 1.
‘destinationincrement’ is similar and operates on the ‘destinationaddress’
pointer.

MEMORY COPY FLOAT
sourceaddress,
destinationaddress,
numberoffloats
[,sourceincrement][,destination
increment]



MEMORY PRINT #]fnbr ,
nbr, address%/array()
MEMORY INPUT [#]fnbr ,
nbr, address%/array()
MEMORY PACK
source%()/sourceaddress%,
dest%()/destaddress%,
number, size
MEMORY UNPACK
source%()/sourceaddress%,
dest%()/destaddress%,
number, size

These commands save or read ‘nbr’ of data bytes from or to memory from or
to an open disk file.
The memory to be saved can be specified as an integer array in which case the
nbr of bytes to be saved or read is checked against the array size. Alternatively,
a memory address can be used in which case no checking can take place and
user errors could result in a crash of the firmware..
Memory pack and unpack allow integer values from one array to be
compressed into another or uncompressed from one to the other.
The two arrays are always normal integer arrays but the packed array can have
2, 4, 8, 16 or 64 values “packed into them. Thus a single integer array element
could store 2 off 32-bit words, 4 off 16 bit values, 8 bytes, 16 nibbles, or 64
booleans (bits).
“number specifies the number of values to be packed or unpacked and “size”
specifies the number of bits (1,4,8,16,or 32)
Alternatively, memory address(es) can be used in which case no checking can
take place and user errors could result in a crash of the firmware.

MKDIR dir$

Make, or create, the directory ‘dir$’ on the default Flash Filesystem or SD
Card.

MID$( str$, start, num) = str2$

The ‘num’ characters in 'str$', beginning at position 'start', are replaced by the
characters in 'str2$'.

NEW

Clears the the program memory and all variables including saved variables.
This command also clears the backup copy of the program which is held in
flash memory.

NEXT [counter-variable] [,
counter-variable], etc

NEXT comes at the end of a FOR-NEXT loop; see FOR.
The ‘counter-variable’ specifies exactly which loop is being operated on. If no
‘counter-variable’ is specified the NEXT will default to the innermost loop. It
is also possible to specify multiple counter-variables as in:
NEXT x, y, z

ON ERROR ABORT
or
ON ERROR IGNORE
or
ON ERROR SKIP [nn]
or
ON ERROR CLEAR

This controls the action taken if an error occurs while running a program and
applies to all errors discovered by MMBasic including syntax errors, wrong data,
missing hardware, etc.
ON ERROR ABORT will cause MMBasic to display an error message, abort the
program and return to the command prompt. This is the normal behaviour and is
the default when a program starts running.
ON ERROR IGNORE will cause any error to be ignored.
ON ERROR SKIP will ignore an error in a number of commands (specified by
the number 'nn') executed following this command. 'nn' is optional, the default if
not specified is one. After the number of commands has completed (with an
error or not) the behaviour of MMBasic will revert to ON ERROR ABORT.
If an error occurs and is ignored/skipped the read only variable MM.ERRNO
will be set to non zero and MM.ERRMSG$ will be set to the error message that
would normally be generated. These are reset to zero and an empty string by
ON ERROR CLEAR. They are also cleared when the program is run and when
ON ERROR IGNORE and ON ERROR SKIP are used.
ON ERROR IGNORE can make it very difficult to debug a program so it is
strongly recommended that only ON ERROR SKIP be used.

ON KEY target
or
ON KEY ASCIIcode, target

The first version of the command sets an interrupt which will call 'target' user
defined subroutine whenever there is one or more characters waiting in the serial
console input buffer.
Note that all characters waiting in the input buffer should be read in the interrupt
subroutine otherwise another interrupt will be automatically generated as soon as
the program returns from the interrupt.



The second version allows you to associate an interrupt routine with a specific
key press. This operates at a low level for the serial console and if activated the
key does not get put into the input buffer but merely triggers the interrupt. It uses
a separate interrupt from the simple ON KEY command so can be used at the
same time if required.
In both variants, to disable the interrupt use numeric zero for the target, i.e.:
ON KEY 0. or ON KEY ASCIIcode, 0
ON PS2 target

This triggers an interrupt whenever the PicoMite sees a message from the PS2
interface.
Use MM.info(PS2) to report the raw message received. This allows the
programmer to trap both keypress and release.
See https://wiki.osdev.org/PS/2_Keyboard for the scan codes (Set 2).

ONEWIRE RESET pin
or
ONEWIRE WRITE pin, flag,
length, data [, data…]
or
ONEWIRE READ pin, flag,
length, data [, data…]

Commands for communicating with 1-Wire devices.
ONEWIRE RESET will reset the 1-Wire bus
ONEWIRE WRITE will send a number of bytes
ONEWIRE READ will read a number of bytes
'pin' is the I/O pin (located in the rear connector) to use. It can be any pin
capable of digital I/O.
'flag' is a combination of the following options:
1 - Send reset before command
2 - Send reset after command
4 - Only send/recv a bit instead of a byte of data
8 - Invoke a strong pullup after the command (the pin will be set high and open
drain disabled)
'length' is the length of data to send or receive
'data' is the data to send or variable to receive. The number of data items must
agree with the length parameter.
See also Appendix C.

OPEN fname$ FOR mode AS
[#]fnbr

Opens a file for reading or writing.
‘fname’ is the filename with an optional extension separated by a dot (.).
Long file names with upper and lower case characters are supported.
A directory path can be specified with the backslash as directory separators.
The parent of the current directory can be specified by using a directory name
of “..” (two dots) and the current directory with “.” (a single dot).
For example OPEN ".\dir1\dir2\filename.txt" FOR INPUT AS #1
‘mode’ is INPUT, OUTPUT, APPEND or RANDOM.
INPUT will open the file for reading and throw an error if the file does not
exist. OUTPUT will open the file for writing and will automatically overwrite
any existing file with the same name.
APPEND will also open the file for writing but it will not overwrite an existing
file; instead any writes will be appended to the end of the file. If there is no
existing file the APPEND mode will act the same as the OUTPUT mode (i.e.
the file is created then opened for writing).
RANDOM will open the file for both read and write and will allow random
access using the SEEK command. When opened the read/write pointer is
positioned at the end of the file.
‘fnbr’ is the file number (1 to 10). The # is optional. Up to 10 files can be
open simultaneously. The INPUT, LINE INPUT, PRINT, WRITE and
CLOSE commands as well as the EOF() and INPUT$() functions all use ‘fnbr’
to identify the file being operated on.
See also ON ERROR and MM.ERRNO for error handling.



OPEN comspec$ AS [#]fnbr

Will open a serial communications port for reading and writing. Two ports are
available (COM1: and COM2:) and both can be open simultaneously. For a
full description with examples see Appendix A.
Using ‘fnbr’ the port can be written to and read from using any command or
function that uses a file number.

OPEN comspec$ AS GPS
[,timezone_offset] [,monitor]

Will open a serial communications port for reading from a GPS receiver. See
the GPS function for details. The sentences interpreted are GPRMC, GNRMC,
GPGGA and GNGGA.
The timezone_offset parameter is used to convert UTC as received from the
GPS to the local timezone. If omitted the timezone will default to UTC. The
timezone_offset can be a any number between -12 and 14 allowing the time to
be set correctly even for the Chatham Islands in New Zealand (UTC +12:45).
If the monitor parameter is set to 1 then all GPS input is directed to the
console. This can be stopped by closing the GPS channel.

OPTION

See the section Options earlier in this manual.

PAUSE delay

Halt execution of the running program for ‘delay’ ms. This can be a fraction.
For example, 0.2 is equal to 200 µs. The maximum delay is 2147483647 ms
(about 24 days).
Note that interrupts will be recognised and processed during a pause.

PIN( pin ) = value

For a ‘pin’ configured as digital output this will set the output to low (‘value’
is zero) or high (‘value’ non-zero). You can set an output high or low before it
is configured as an output and that setting will be the default output when the
SETPIN command takes effect.
See the function PIN() for reading from a pin and the command SETPIN for
configuring it. Refer to the section Using the I/O pins for a general description
of the PicoMite's input/output capabilities.

PIO

The RP2040 chip used in the PicoMite contains a programmable I/O system
with two identical PIO devices (pio%=0 or pio%=1) acting like specialised
CPU cores. See the Appendix for a more detailed description.

PIO assemble pio,linedata$

This command will assemble and load text based PIO assembler code
including labels for jumps
Use: PIO assemble pio,".program anything" to initialise the assembler
Use: PIO assemble pio,".side_set n [opt] [pindirs]" if using side set. This is
mandatory in order to correctly construct the op-codes if one or more side set
pins are used.
It does not load the pinctrl register as this is specific to the state-machine.
Also note the "opt" parameter changes the op-code on instructions that have a
side parameter
Use: PIO assemble pio,".line n" to assemble starting from a line other than 1 this is optional
Use: PIO assemble pio,".end program [list]" to terminate the assembly and
program the pio. The optional parameter LIST causes a hex dump of the opcodes to the terminal.
Use: PIO assemble pio,"label:" to define a label. This must appear as a separate
command.
Use: PIO assemble “’wrap target” to specify where the program will wrap to.
See PIO(.wrap target) for how to use this.
Use: PIO assemble “.wrap” to specify where the program should wrap back to
from “.wrap target” . See PIO(.wrap) for how to use this.
Use: PIO assemble pio "instruction [parameters]" to define the actual PIO
instructions that will be converted to machine code



PIO DMA RX pio, sm, nbr,
data%() [,completioninterrupt]
[,transfersize]
[,loopbackcount]
PIO DMA TX pio, sm, nbr,
data%() [,completioninterrupt]
[,transfersize]
[,loopbackcount]

Sets up DMA transfers from PIO to MMBasic memory
pio specifies which of the two pio instances to use (0 or 1
sm specifies which of the state machine to use (0-3)
nbr specifies how many 32-bit words to transfer. See below for the special case
of setting nbr to zero.
data%() is the array that will either supply or receive the PIO data
The optional parameter completioninterrupt is the name of a MMBasic
subroutine rthat will be called when the DMA completes and in the case of
DMA_OUT the FIFO has been emptied.
If the optional interrupt is not used then the status of the DMA can be checked
using the functions
MM.INFO(PIO RX DMA)
MM.INFO(PIO TX DMA)
The optional parameter transfersize allows the user to override the normal 32bit transfers and select 8, 16, or 32.
The optional parameter loopbackcount specifies how many data items are to be
read or written before the DMA starts again at the beginning of the buffer
The parameter must be a power of 2 between 2 and 32768
Due to a limitation in the RP2040 if loopbackcount is used the MMBasic array
must be aligned in memory to the number of bytes in the loop
Thus if the array is 64 integers long which is 512 bytes then the array must be
aligned to a 512byte boundary in memory
All MMBasic arrays are aligned to a 256 byte boundary but to create an array
which is guaranteed to be aligned to a 512 byte boundary or greater the PIO
MAKE RING BUFFER command must be used
If loopbackcount is set then “nbr” can be set to 0. In this case the transfer will
run continuously repeatedly filling the buffer until explicitly stopped

PIO DMA RX OFF
PIO DMA TX OFF

Aborts a running DMA

PIO INTERRUPT pio, sm
[,RXinterrupt] [,TXinterrupt]

Sets Basic interrupts for PIO activity.
Use the value 0 for RXinterrupt or TXinterrupt to disable an interrupt
Omit values not needed
The RX interrupt triggers whenever a word has been "pushed" by the PIO code
into the specified FIFO. The data MUST be read in the interrupt to clear it.
The TX interrupt triggers whenever the specified FIFO has been FULL and the
PIO code has now "pulled" it

PIO INIT MACHINE pio%,
statemachine%, clockspeed
[,pinctrl] [,execctrl] [,shiftctrl]
[,startinstruction]

PIO interrupts have priority have keyboard interrupts but before anything else.
As with all interrupts interrupt conditions are processed one at a time.
Initialises PIO 'pio%' with state machine 'statemachine%'. 'clockspeed' is the
clock speed of the state machine in kHz. The four optional arguments are
variables holding initialising values of the state machine registers and the
address of the first instruction to execute (defaults to zero). These decide how
the PIO will operate.
It is anticipated that eventually the PIO assembler will be able to generate the
register values for the user along with the program array based on the defined
assembler directives.

PIO EXECUTE pio,
state_machine, instruction%

Immediately executes the instruction on the pio and state machine specified.



PIO WRITE pio,
state_machine, count, data0
[,data1..]

Writes the data elements to the pio and state machine specified. The write is
blocking so the state machine needs to be able to take the data supplied
NB: this command will probably need additional capability in future releases

PIO READ pio,
state_machine, count,
data%[()]

Reads the data elements from the pio and state machine specified. The read is
non-blocking so the state machine needs to be able to supply the data
requested. When count is one then an integer can be used to receive the data,
otherwise and integer array should be specified.
NB: this command will probably need additional capability in future releases

PIO START pio, statemachine

Start a given state machine on pio

PIO STOP pio, statemachine

Stop a given state machine on pio

PIO CLEAR pio

This stops the pio specified on all statemachines and clears the control registers
for the statemachines PINCTRL, EXECTRL, and SHIFTCTRL to defaults

PIO PROGRAM LINE pio,
line, instruction

Programs just the specified line in a PIO program

PIXEL x, y [,c]

Set a pixel on an attached LCD panel to a colour. 'x' is the horizontal
coordinate and 'y' is the vertical coordinate of the pixel. 'c' is a 24 bit number
specifying the colour. 'c' is optional and if omitted the current foreground
colour will be used. All parameters can be expressed as arrays and the software
will plot the number of pixels as determined by the dimensions of the smallest
array. 'x' and 'y' must both be arrays or both be single variables /constants
otherwise an error will be generated. 'c' can be either an array or a single
variable or constant.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

PLAY

This command will generate a variety of audio outputs.
See the OPTION AUDIO command for setting the I/O pins to be used for the
output. The audio is a pulse width modulated signal so a low pass filter is
required to remove the carrier frequency.

PLAY TONE left [, right [,
dur] [,interrupt]]]

Generates two separate sine waves on the sound output left and right channels.
'left' and 'right' are the frequencies in Hz to use for the left and right channels.
The tone plays in the background (the program will continue running after this
command) and 'dur' specifies the number of milliseconds that the tone will
sound for. If the duration is not specified the tone will continue until explicitly
stopped or the program terminates.
'interrupt' is an optional subroutine which will be called when the play
terminates.
The frequency can be from 1Hz to 20KHz and is very accurate (it is based on a
crystal oscillator). The frequency can be changed at any time by issuing a new
PLAY TONE command.

PLAY FLAC file$ [, interrupt]

Will play a FLAC file on the sound output.
'file$' is the FLAC file to play (the extension of .flac will be appended if
missing). The sample rate can be up to 48kHz in stereo (96kHz if the Pico is
overclocked)
The FLAC file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY WAV file$ [, interrupt]

Will play a WAV file on the sound output.
'file$' is the WAV file to play (the extension of .wav will be appended if



missing). The WAV file must be PCM encoded in mono or stereo with 8 or
16-bit sampling. The sample rate can be up to 48kHz in stereo (96kHz if the
Pico is overclocked).
The WAV file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
PLAY MODFILE file$
[,interrupt]

Will play a MOD file on the sound output.
'file$' is the MOD file to play (the extension of .mod will be appended if
missing).
The MOD file is played in the background and will play continuously in a
loop. If the optional 'interrupt' is specified This will be called when the file has
played once through the sequence and playback will then be terminated.

PLAY MODSAMPLE
Samplenum, channel
[,volume]

Plays a specific sample in the mod file on the channel specified. The volume is
optional and can be between 0 and 64. This command can only be used when
there is a mod file already playing and allows sound effects to be output whilst
the background music is still playing.

PLAY LOAD SOUND
array%()

Loads a 1024 element array comprising 4096 16-bit values between 0 and
4095. This provides the data for any arbitrary waveform that can be played by
the PLAY SOUND command. You can use the MEMORY PACK command to
create the arrays from a normal 40956 element integer array.

PLAY SOUND soundno,
channelno, type [,frequency]
[,volume]

Play a series of sounds simultaneously on the audio output.
'soundno' is the sound number and can be from 1 to 4 allowing for four
simultaneous sounds on each channel.
'channelno' specifies the output channel. It can be L (left speaker), R (right
speaker), B (both speakers) or M (mono output with the right channel inverted
compared to the left).
type' specifies the wave form It can be S (Sine wave), Q (square wave) ,T
(triangular wave) ,W (saw tooth) , O (Null output), P (periodic noise), N
(random noise) or U (user defined using the PLAY LOAD sound command).to
be used.
'frequency' is the frequency from 1 to 20000 (Hz) and it must be specified
except when type is O.
'volume' is optional and must be between 1 and 25. It defaults to 25
The first time PLAY SOUND is called all other audio usage will be blocked
and will remain blocked until PLAY STOP is called. Output can be stopped
temporarily using PLAY PAUSE and PLAY RESUME.
Calling SOUND on an already running 'soundno' will immediately replace the
previous output. Individual sounds are turned off using type “O”
Running 4 sounds simultaneously on both channels of the audio output
consumes about 23% of the CPU.

PLAY PAUSE
PLAY RESUME
PLAY STOP

PLAY PAUSE will temporarily halt the currently playing file or tone.
PLAY RESUME will resume playing a sound that was paused.
PLAY STOP will terminate the playing of the file or tone. When the program
terminates for whatever reason the sound output will also be automatically
stopped.

PLAY VOLUME left, right

Will adjust the volume of the audio output.
'left' and 'right' are the levels to use for the left and right channels and can be
between 0 and 100 with 100 being the maximum volume. There is a linear
relationship between the specified level and the output. The volume defaults
to maximum when a program is run.

PLAY NEXT
Stops playback of the current audio file and starts the next one in the directory


PLAY PREVIOUS

Stops playback of the current audio file and starts the previous one in the
directory

VS1053 specific PLAY commands
PLAY MP3 file$ [, interrupt]

Will play a MP3 file on the sound output.
'file$' is the MP3 file to play (the extension of .mp3 will be appended if
missing). The sample rate should be 44100Hz stereo.
The MP3 file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY HALT

This command works when a MP3 file is playing. It stops playback and
records the current file position to allow playback to be resumed from the same
point. This command is specifically designed to support for mp3 audio books

PLAY CONTINUE track$

Resumes playback of the MP3 track specified. "track$" will be the name of the
file that was playing when halted with all file attributes removed
e.g.
PLAY MP3 "B:/mp3/mymp3.mp3"
sometime later
PLAY HALT
later again
PLAY CONTINUE "mymp3"

PLAY MIDIFILE file$ [,
interrupt]

Will play a MIDI file on the sound output.
'file$' is the MIDI file to play (the extension of .mid will be appended if
missing).
The MIDI file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY MIDI

Initiates the real-time midi mode. In this mode midi instructions can be sent to
the VS1053 to select which instruments to play on which channels, turn notes
on, and turn them off in real timer

PLAY MIDI CMD cmd%,
data1%, data2%

Sends a midi command when in real time midi mode. An example would be to
allocate an instrument to a channel. E.g.
PLAY MIDI CMD &B11000001,4 ‘set channel 1 to instrument 4

PLAY MIDI TEST n

Plays a MIDI test sequence, n=0 to 3, 0 = normal realtime, the others play note
and instrument samples

PLAY NOTE ON channel%,
note%, velocity%
PLAY NOTE OFF channel%,
note% [,velocity%]
PLAY STREAM buffer%(),
readpointer%, writepointer%
POKE BYTE addr%, byte
or
POKE SHORT addr%, short%
Or


Turns on the note on the channel specified when in real time MIDI mode

Turns off the note on the channel specified when in real time MIDI mode

Sends data to the VS1053 CODEC from the circular buffer “buffer%”. This
command initiates a background output stream where the VS1053 is sent
anything in the buffer between the readpointer and the write pointer, updating
the readpointer as it goes. Can be used for arbitrary waveform output.
Will set a byte or a word within the virtual memory space.
POKE BYTE will set the byte (i.e. 8 bits) at the memory location 'addr%' to
'byte'. 'addr%' should be an integer.
POKE SHORT will set the short integer (i.e. 16 bits) at the memory location
'addr%' to 'word%'. 'addr%' and short%' should be integers.

POKE WORD addr%, word%
or
POKE INTEGER addr%, int%
or
POKE FLOAT addr%, float!
or
POKE VAR var, offset, byte
or
POKE VARTBL, offset, byte
or
POKE DISPLAY command
[,data1] [,data2] [,datan]

POKE WORD will set the word (i.e. 32 bits) at the memory location 'addr%' to
'word%'. 'addr%' and 'word%' should be integers.
POKE INTEGER will set the MMBasic integer (i.e. 64 bits) at the memory
location 'addr%' to int%'. 'addr%' and int%' should be integers.
POKE FLOAT will set the word (i.e. 32 bits) at the memory location 'addr%'
to 'float!'. 'addr%' should be an integer and 'float!' a floating point number.
POKE VAR will set a byte in the memory address of 'var'. 'offset' is the
±offset from the address of the variable. An array is specified as var().
POKE VARTBL will set a byte in MMBasic's variable table. 'offset' is the
±offset from the start of the variable table. Note that a comma is required after
the keyword VARTBL.
This command sends commands and associated data to the display controller
for a connected display. This allows the programmer to change parameters of
how the display is configured. e.g. POKE DISPLAY &H28 will turn off an
SSD1963 display and POKE DISPLAY &H29 will turn it back on again.
Works for all displays except the ST7790.

POKE DISPLAY HRES n
POKE DISPLAY VRES n

These commands change the stored value of MM.HRES and MM.VRES
allowing the programmer to configure non-standard displays.

POLYGON n, xarray%(),
yarray%() [, bordercolour] [,
fillcolour]

Draws a filled or outline polygon with n xy-coordinate pairs in xarray%() and
yarray%(). If ‘fillcolour’ is omitted then just the polygon outline is drawn. If
‘bordercolour’ is omitted then it will default to the current default foreground
colour.
If the last xy-coordinate pair is not the same as the first the firmware will
automatically create an additional xy-coordinate pair to complete the polygon.
The size of the arrays should be at least as big as the number of x,y coordinate
pairs.
'n' can be an array and the colours can also optionally be arrays as follows:
POLYGON n(), xarray%(), yarray%() [, bordercolour()] [, fillcolour()]
POLYGON n(), xarray%(), yarray%() [, bordercolour] [, fillcolour]
The elements of array n() define the number of xy-coordinate pairs in each of
the polygons. e.g. DIM n(1)=(3,3) would define that 2 polygons are to be
drawn with three vertices each. The size of the n array determines the number
of polygons that will be drawn unless an element is found with the value zero
in which case the firmware only processes polygons up to that point. The x,ycoordinate pairs for all the polygons are stored in xarray%() and yarray%().
The xarray%() and yarray%() parameters must have at least as many elements
as the total of the values in the n array.
Each polygon can be closed with the first and last elements the same. If the last
element is not the same as the first the firmware will automatically create an
additional x,y-coordinate pair to complete the polygon. If fill colour is omitted
then just the polygon outlines are drawn.
The colour parameters can be a single value in which case all polygons are
drawn in the same colour or they can be arrays with the same cardinality as n.
In this case each polygon drawn can have a different colour of both border
and/or fill. For example, this will draw 3 triangles in yellow, green and red:
DIM c%(2)=(3,3,3)
DIM x%(8)=(100,50,150,100,50,150,100,50,150)
DIM y%(8)=(50,100,100,150,200,200,250,300,300)
DIM fc%(2)=(rgb(yellow),rgb(green),rgb(red))
POLYGON c%(),x%(),y%(),fc%(),fc%()

POLYGON n(), xarray%(),
yarray%() [, bordercolour()] [,
fillcolour()]
POLYGON n(), xarray%(),
yarray%() [, bordercolour] [,
fillcolour]



PORT(start, nbr [,start, nbr]…) Set a number of I/O pins simultaneously (i.e. with one command).
= value
'start' is an I/O pin number and the lowest bit in 'value' (bit 0) will be used to
set that pin. Bit 1 will be used to set the pin 'start' plus 1, bit 2 will set pin
'start'+2 and so on for 'nbr' number of bits. I/O pins used must be numbered
consecutively and any I/O pin that is invalid or not configured as an output will
cause an error. The start/nbr pair can be repeated if an additional group of
output pins needed to be added.
For example; PORT(15, 4, 23, 4) = &B10000011
Will set eight I/O pins. Pins 15 and 16 will be set high while 17, 18, 23, 24
and 25 will be set to a low and finally 26 will be set high.
This command can be used to conveniently communicate with parallel devices
like LCD displays. Any number of I/O pins (and therefore bits) can be used
from 1 to the number of I/O pins on the chip.
See the PORT function to simultaneously read from a number of pins.
PRINT expression
[[,; ]expression] … etc

Outputs text to the serial console followed by a carriage return/newline pair.
Multiple expressions can be used and must be separated by either a:
 Comma (,) which will output the tab character
 Semicolon (;) which will not output anything (it is just used to separate
expressions).
 Nothing or a space which will act the same as a semicolon.
A semicolon (;) or a comma (,) at the end of the expression list will suppress
the output of the carriage return/newline pair at the end of a print statement.
When printed, a number is preceded with a space if positive or a minus (-) if
negative but is not followed by a space. Integers (whole numbers) are printed
without a decimal point while fractions are printed with the decimal point and
the significant decimal digits. Large or small floating point numbers are
automatically printed in scientific number format.
The function TAB() can be used to space to a certain column and the STR$()
function can be used to justify or otherwise format strings.

PRINT #nbr, expression
[[,; ]expression] … etc

Same as above except that the output is directed to a serial communications
port or a file opened for OUTPUT or APPEND with a file number of ‘nbr’.
See the OPEN command.

PRINT #GPS, expression
[[,; ]expression] … etc

Outputs a NMEA string to an opened GPS device. The string must start with a
$ character and end with a * character. The checksum is automatically
calculated and appended to the string together with the CR/LF characters.

PRINT @(x [, y]) expression
Or
PRINT @(x, [y], m)
expression

Works on terminal console on an attached computer or the display if OPTION
LCDPANEL CONSOLE is enabled.
Same as the standard PRINT command except that the cursor is positioned at
the coordinates x, y expressed in pixels. If y is omitted the cursor will be
positioned at “x” on the current line.
Example: PRINT @(150, 45) "Hello World"
The @ function can be used anywhere in a print command.
Example: PRINT @(150, 45) "Hello" @(150, 55) "World"
The @(x,y) function can be used to position the cursor anywhere on or off the
screen. For example, PRINT @(-10, 0) "Hello" will only show "llo" as the
first two characters could not be shown because they were off the screen.
The @(x,y) function will automatically suppress the automatic line wrap
normally performed when the cursor goes beyond the right screen margin.
If 'm' is specified the mode of the video operation will be as follows:
m = 0 Normal text (white letters, black background)
m = 1 The background will not be drawn (ie, transparent)
m = 2 The video will be inverted (black letters, white background)
m = 5 Current pixels will be inverted (transparent background)



PULSE pin, width

Will generate a pulse on 'pin' with duration of 'width' ms. 'width' can be a
fraction. For example, 0.01 is equal to 10µs and this enables the generation of
very narrow pulses.
The generated pulse is of the opposite polarity to the state of the I/O pin when
the command is executed. For example, if the output is set high the PULSE
command will generate a negative going pulse. Notes:
 'pin' must be configured as an output.
 For a pulse of less than 3 ms the accuracy is ± 1 µs.
 For a pulse of 3 ms or more the accuracy is ± 0.5 ms.
 A pulse of 3 ms or more will run in the background. Up to five different
and concurrent pulses can be running in the background and each can have
its time changed by issuing a new PULSE command or it can be
terminated by issuing a PULSE command with zero for 'width'.

PWM channel, frequency,
[dutyA]
[,dutyB][,phase][,defer]

PWM SYNC s0
[,s1][,s2][,s3][,s4][,s5][,s6][,s7
]

There are 8 separate PWM frequencies available (channels 0 to 7) and up to 16
outputs with individually controlled duty cycle. You can output on either
PWMnA or PWMnB or both for each channel - no restriction. Duty cycles
are specified as a percentage and you can use a negative value to invert the
output (-100.0 <= duty <=100.0).
Minimum frequency = (cpuspeed + 1) / (2^24) Hz. Maximum speed is
OPTION CPUSPEED/4. At very fast speeds the duty cycles will be
increasingly limited.
Phase is a parameter that causes the waveforms to be centred such that a wave
form with a shorter duty cycle starts and ends equal times from a longer one.
Use 1 to enable this mode and 0 (or omit) to run as normal
The parameter "deferredstart" when set to 1 configures the PWM channels as
but does not start the output running. They can the be started uing the PWM
SYNC command. This can be used to avoid any undesirable startup artefacts
The PWM command is also capable of driving servos as follows:
PWM 1,50,(position_as_a_percentage * 0.05 + 5)
This initiates the PWM on channels where a deferred start was defined or just
syncs existing running channels. However, the power comes in the ability to
offset the channels one to another (defined as a percentage of the time period
as per the duty cycle - can be a float)
You can use an offset of -1 to omit a channel from the synch
Stop output on ‘channel

PWM channel, OFF
RANDOMIZE nbr

Seed the random number generator with ‘nbr’.
On power up the random number generator is seeded with zero and will
generate the same sequence of random numbers each time. To generate a
different random sequence each time you must use a different value for ‘nbr’
(the TIMER function is handy for that).

REFRESH

Initiates an update of the screen for certain black and white displays.
These can only be updated a full screen at a time and if OPTION
AUTOREFRESH is OFF this command can be used to trigger the write. This
applies to the following displays: N5110, SSD1306I2C, SSD1306I2C32,
SSD1306SPI, ST7920.



RBOX x, y, w, h [, r] [,c]
[,fill]

Draws a box with rounded corners on an attached LCD panel starting at 'x' and
'y' which is 'w' pixels wide and 'h' pixels high.
'r' is the radius of the corners of the box. It defaults to 10.
'c' specifies the colour and defaults to the default foreground colour if not
specified. 'fill' is the fill colour. It can be omitted or set to -1 in which case the
box will not be filled.
All parameters can be expressed as arrays and the software will plot the
number of boxes as determined by the dimensions of the smallest array. 'x', 'y',
'w', and 'h' must all be arrays or all be single variables /constants otherwise an
error will be generated. 'r', 'c', and 'fill' can be either arrays or single
variables/constants.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

READ variable[, variable]..

Reads values from DATA statements and assigns these values to the named
variables. Variable types in a READ statement must match the data types in
DATA statements as they are read.
Arrays can be used as variables (specified with empty brackets, e.g. a()) and in
that case the size of the array is used to determine how many elements are to
be read. If the array is multidimensional then the leftmost dimension will be
the fastest moving.
See also DATA and RESTORE.

READ SAVE
or
READ RESTORE

READ SAVE will save the virtual pointer used by the READ command to
point to the next DATA to be read. READ RESTORE will restore the pointer
that was previously saved.
This enables subroutines to READ data and then restore the read pointer so as
not to disturb other parts of the program that may be reading the same data
statements. These commands can be nested.

REM string

REM allows remarks to be included in a program.
Note the Microsoft style use of the single quotation mark (‘) to denote remarks
is also supported and is preferred.

RENAME old$ AS new$

Rename a file or a directory from ‘old$’ to ‘new$’. Both are strings.
A directory path can be used in both 'old$' and 'new$'. If the paths differ the
file specified in 'old$' will be moved to the path specified in 'new$' with the
file name as specified.

RESTORE [line]

Resets the line and position counters for the READ statement.
If ‘line’ is specified the counters will be reset to the beginning of the specified
line. ‘line’ can be a line number or label or a variable with these values.
If ‘line’ is not specified the counters will be reset to the start of the program.

RMDIR dir$

Remove, or delete, the directory ‘dir$’ on the default Flash Filesystem or SD
Card.

RTC GETTIME

RTC GETTIME will get the current date/time from a PCF8563, DS1307 or
DS3231 real time clock and set the internal MMBasic clock accordingly. The
date/time can then be retrieved with the DATE$ and TIME$ functions.

RTC SETTIME year, month,
day, hour, minute, second

RTC SETTIME will set the time in the clock chip. 'hour' must use 24 hour
notation. ‘year’ can be two or four digits. The RTC SETTIME command will
also accept a single string argument in the format of dd/mm/yy hh:mm. This
means the date/time could be entered by the user using a GUI FORMATBOX
with the DATETIME2 format.

RTC SETREG reg, value
RTC GETREG reg, var

The RTC SETREG and GETREG commands can be used to set or read the
contents of registers within the chip. 'reg' is the register's number, 'value' is the
number to store in the register and 'var' is a variable that will receive the
number read from the register. These commands are not necessary for normal



operation but they can be used to manipulate special features of the chip
(alarms, output signals, etc). They are also useful for storing temporary
information in the chip's battery backed RAM.
These chips are I2C devices and must be connected to the two I2C pins as
specified by OPTION SYSTEM I2C with appropriate pullup resistors.
Also see the command OPTION RTC AUTO ENABLE.
RUN
or
RUN [file$] [, cmdline$]

Run a program.
If file$ is not supplied then run the program currently held in program
memory.
If file$ is supplied then run the named file from the Flash or SD Card
filesystem; if file$ does not contain a '.BAS' extension then one will be
automatically added.
If cmdline$ is supplied then pass its value to the MM.CMDLINE$ constant of
the program when it runs.
If cmdline$ is not supplied then an empty string value is passed to
MM.CMDLINE$.
•
Both file$ and cmdline$ may be supplied as string expressions.
•
Use FLASH RUN n to run a program stored in a Flash Slot.
.Use
FLASH RUN n to run a program stored in a Flash Slot.

SAVE file$

Saves the program in the current working directory of the Flash Filesystem or
SD Card as ‘file$’. Example: SAVE “TEST.BAS”
If an extension is not specified “.BAS” will be added to the file name.
See also FLASH SAVE n

SAVE IMAGE file$ [,x, y, w,
h]
or
SAVE COMPRESSED
IMAGE file$ [,x, y, w, h]

Save the current image on the current LCD panel as a BMP file. The panel
must be capable of being read, for example, a ILI9341 based panel or a
VIRTUAL_M or VIRTUAL_ panel.
'file$' is the name of the file. If an extension is not specified “.BMP” will be
added to the file name. The image is saved as a true colour 24-bit image.
‘x’, ‘y’, ‘w’ and ‘h’ are optional and are the coordinates (x and y are the top
left coordinate) and dimensions (width and height) of the area to be saved. If
not specified the whole screen will be saved.
SAVE COMPRESSED IMAGE will work the same except that RLE
compression will be used to reduce the file size..

SEEK [#]fnbr, pos

Will position the read/write pointer in a file that has been opened on the Flash
Filesystem or SD Card for RANDOM access to the 'pos' byte.
The first byte in a file is numbered one so SEEK #5,1 will position the
read/write pointer to the start of the file.

SELECT CASE value
CASE testexp [[, testexp]
…]
<statements>
<statements>
CASE ELSE
<statements>
<statements>
END SELECT

Executes one of several groups of statements, depending on the value of an
expression. 'value' is the expression to be tested. It can be a number or string
variable or a complex expression.
'testexp' is the value that is to be compared against. It can be:
 A single expression (i.e. 34, "string" or PIN(4)*5) to which it may equal
 A range of values in the form of two single expressions separated by the
keyword "TO" (i.e. 5 TO 9 or "aa" TO "cc")
 A comparison starting with the keyword "IS" (which is optional). For
example: IS > 5, IS <= 10.
When a number of test expressions (separated by commas) are used the CASE
statement will be true if any one of these tests evaluates to true.
If 'value' cannot be matched with a 'testexp' it will be automatically matched to
the CASE ELSE. If CASE ELSE is not present the program will not execute
any <statements> and continue with the code following the END SELECT.
When a match is made the <statements> following the CASE statement will be



executed until END SELECT or another CASE is encountered when the
program will then continue with the code following the END SELECT.
An unlimited number of CASE statements can be used but there must be only
one CASE ELSE and that should be the last before the END SELECT.
Example:
SELECT CASE nbr%
CASE 4, 9, 22, 33 TO 88
statements
CASE IS < 4, IS > 88, 5 TO 8
statements
CASE ELSE
statements
END SELECT
Each SELECT CASE must have one and one only matching END SELECT
statement. Any number of SELECT…CASE statements can be nested inside
the CASE statements of other SELECT…CASE statements.
SETPIN pin, cfg [, option]

Will configure an external I/O pin. Refer to the section Using the I/O pins for
a general description of the PicoMite's input/output capabilities.
'pin' is the I/O pin to configure, ‘cfg’ is the mode that the pin is to be set to and
'option' is an optional parameter. 'cfg' is a keyword and can be any one of the
following:
OFF
Not configured or inactive
AIN
Analog input (i.e. measure the voltage on the input).
DIN
Digital input
If 'option' is omitted the input will be high impedance
If 'option' is the keyword "PULLUP" a simulated resistor will be
used to pull up the input pin to 3.3V If the keyword
"PULLDOWN" is used the pin will be pulled down to zero
volts. The pull up/down is a constant current of about 50µA.
FIN
Frequency input
'option' can be used to specify the gate time (the length of time
used to count the input cycles). It can be any number between
10 ms and 100000 ms. Note that the PIN() function will always
return the frequency correctly scaled in Hz regardless of the gate
time used. If 'option' is omitted the gate time will be 1 second.
The pins can be GP6, GP7, GP8 or GP9 (can be changed with
OPTION COUNT).
PIN
Period input
'option' can be used to specify the number of input cycles to
average the period measurement over. It can be any number
between 1 and 10000. Note that the PIN() function will always
return the average period of one cycle correctly scaled in ms
regardless of the number of cycles used for the average. If
'option' is omitted the period of just one cycle will be used.
The pins can be GP6, GP7, GP8 or GP9 (can be changed with
OPTION COUNT).
CIN


Counting input
‘option’ can be used to specify which edge triggers the count
and if any pullup or pulldown is enabled
1 specifies a rising edge with pulldown,
2 specifies a falling edge with pullup,
3 specifies that both a falling and rising edge will trigger a
count with no pullup or pulldown applied,
4 specifies both edges but with a pulldown and
5 specifies both edges but with a pullup applied.


If ‘option’ is omitted a rising edge will trigger the count and a
pulldown is enabled. The pins can be GP6, GP7, GP8 or GP9
(can be changed with OPTION COUNT).
DOUT

Digital output
'option' is not used in this mode.
The functions PIN() and PORT() can also be used to return the value on one or
more output pins. See the function PIN() for reading inputs and the statement
PIN()= for setting an output. See the command below if an interrupt is
configured.
SETPIN pin, cfg, target [,
option]

Will configure ‘pin’ to generate an interrupt according to ‘cfg’. Any I/O pin
capable of digital input can be configured to generate an interrupt with a
maximum of ten interrupts configured at any one time.
'cfg' is a keyword and can be any one of the following:
OFF
Not configured or inactive
INTH
Interrupt on low to high input
INTL
Interrupt on high to low input
INTB
Interrupt on both (i.e. any change to the input)
‘target' is a user defined subroutine which will be called when the event
happens. Return from the interrupt is via the END SUB or EXIT SUB
commands. 'option' can be the keywords "PULLUP" or "PULLDOWN" as
specified for a normal input pin (SETPIN pin DIN). If 'option' is omitted the
input will be high impedance.
This mode also configures the pin as a digital input so the value of the pin can
always be retrieved using the function PIN().
Refer to the section Using the I/O pins for a general description of the
PicoMite's input/output capabilities.

SETPIN GP25, DOUT |
HEARTBEAT

This version of SETPIN controls the on-board LED.
If it is configured as DOUT then it can be switched on and off under program
control.
If configured as HEARTBEAT then it will flash 1s on, 1s off continually while
powered. This is the default state and will be restored to this when the user
program stops running.

SETPIN p1[, p2 [, p3]], device

These commands are used for the pin allocation for special devices.
Pins must be chosen from the pin designation diagram and must be allocated
before the devices can be used. Note that the pins (e.g. rx, tx, etc) can be
declared in any order and that the pins can be referred to by using their pin
number (e.g. 1, 2) or GP number (e.g. GP0, GP1).

SETPIN rx, tx, COM1

Allocate the pins to be used for serial port COM1.
Valid pins are
RX:
GP1, GP13 or GP17
TX:
GP0, GP12, GP16 or GP28

SETPIN rx, tx, COM2

Allocate the pins to be used for serial port COM2.
Valid pins are
RX:
GP5, GP9 or GP21
TX:
GP4, GP8 or GP20

SETPIN rx, tx, clk, SPI

Allocate the pins to be used for SPI port SPI.
Valid pins are
RX:
GP0, GP4, GP16 or GP20
TX:
GP3, GP7 or GP19
CLK: GP2, GP6 or GP18

SETPIN rx, tx, clk, SPI2

Allocate the pins to be used for SPI port SPI2.
Valid pins are
RX:
GP8, GP12 or GP28
TX:
GP11, GP15 or GP27



CLK:

GP10, GP14 or GP26

SETPIN sda, scl, I2C

Allocate the pins to be used for the I2C port I2C.
Valid pins are
SDA: GP0, GP4, GP8, GP12, GP16, GP20 or GP28
SCL: GP1, GP5, GP9, GP13, GP17 or GP21

SETPIN sda, scl, I2C2

Allocate the pins to be used for the I2C port I2C2.
Valid pins are
SDA: GP2, GP6, GP10, GP14, GP18, GP22 or GP26
SCL: GP3, GP7, GP11, GP15, GP19 or GP27

SETPIN pin, PWM[nx]

Allocate pin to PWMnx
'n' is the PWM number (0 to 7) and 'x' and is the channel (A or B). n and x are
optional.
The setpin can be changed until the PWM command is issued. At that point the
pin becomes locked to PWM until PWMn,OFF is issued.

SETPIN pin, IR

Allocate pins for InfraRed (IR) communications (can be any pin).

SETPIN pin, PIOn

Reserve pin for use by a PIO0 or PIO1 (see Appendix F for PIO details).

SETTICK period, target [, nbr]

This will setup a periodic interrupt (or "tick").
Four tick timers are available ('nbr' = 1, 2, 3 or 4). 'nbr' is optional and if not
specified timer number 1 will be used.
The time between interrupts is ‘period’ milliseconds and ‘target' is the interrupt
subroutine which will be called when the timed event occurs.
The period can range from 1 to 2147483647 ms (about 24 days).
These interrupts can be disabled by setting ‘period’ to zero
(i.e. SETTICK 0, 0, 3 will disable tick timer number 3).

SETTICK PAUSE, target
[, nbr]
or
SETTICK RESUME, target
[, nbr]

Pause or resume the specified timer. When paused the interrupt is delayed but
the current count is maintained.

SORT array() [,indexarray()]
[,flags] [,startposition]
[,elementstosort]

This command takes an array of any type (integer, float or string) and sorts it
into ascending order in place.
It has an optional parameter ‘indexarray%()’. If used this must be an integer
array of the same size as the array to be sorted. After the sort this array will
contain the original index position of each element in the array being sorted
before it was sorted. Any data in the array will be overwritten. This allows
connected arrays to be sorted. See the section Sorting Data in the tutorial
Programming with the Colour Maximite 2 for an example.
The ‘flag’ parameter is optional and valid flag values are:
bit0: 0 (default if omitted) normal sort - 1 reverse sort
bit1: 0 (default) case dependent - 1 sort is case independent (strings only).
The optional ‘startposition’ defines which element in the array to start the sort.
Default is 0 (OPTION BASE 0) or 1 (OPTION BASE 1)
The optional ‘elementstosort’ defines how many elements in the array should
be sorted. The default is all elements after the startposition.
Any of the optional parameters may be omitted so, for example, to sort just the
first 50 elements of an array you could use:
SORT array(), , , ,50

SPI OPEN speed, mode, bits
or
SPI READ nbr, array()
or
SPI WRITE nbr, data1, data2,

Communications via an SPI channel. See Appendix D for the details.
'nbr' is the number of data items to send or receive
'data1', 'data2', etc can be float or integer and in the case of WRITE can be a
constant or expression.
If 'string$' is used 'nbr' characters will be sent.



data3, … etc
or
SPI WRITE nbr, string$
or
SPI WRITE nbr, array()
or
SPI CLOSE

'array' must be a single dimension float or integer array and 'nbr' elements will
be sent or received.

SPI2

The same set of commands as for SPI (above) but applying to the second SPI
channel.

STATIC variable [, variables]
See DIM for the full syntax.

Defines a list of variable names which are local to the subroutine or function.
These variables will retain their value between calls to the subroutine or
function (unlike variables created using the LOCAL command).
This command uses exactly the same syntax as DIM. The only difference is
that the length of the variable name created by STATIC and the length of the
subroutine or function name added together cannot exceed 31 characters.
Static variables can be initialised to a value. This initialisation will take effect
only on the first call to the subroutine (not on subsequent calls).

SUB xxx (arg1 [,arg2, …])
<statements>
<statements>
END SUB

Defines a callable subroutine. This is the same as adding a new command to
MMBasic while it is running your program.
'xxx' is the subroutine name and it must meet the specifications for naming a
variable.
'arg1', 'arg2', etc are the arguments or parameters to the subroutine. An array is
specified by using empty brackets. i.e. arg3(). The type of the argument can
be specified by using a type suffix (i.e. arg1$) or by specifying the type using
AS <type> (i.e. arg1 AS STRING).
Every definition must have one END SUB statement. When this is reached the
program will return to the next statement after the call to the subroutine. The
command EXIT SUB can be used for an early exit.
You use the subroutine by using its name and arguments in a program just as
you would a normal command. For example: MySub a1, a2
When the subroutine is called each argument in the caller is matched to the
argument in the subroutine definition. These arguments are available only
inside the subroutine. Subroutines can be called with a variable number of
arguments. Any omitted arguments in the subroutine's list will be set to zero
or a null string.
Arguments in the caller's list that are a variable and have the correct type will
be passed by reference to the subroutine. This means that any changes to the
corresponding argument in the subroutine will also be copied to the caller's
variable and therefore may be accessed after the subroutine has ended. Arrays
are passed by specifying the array name with empty brackets (e.g. arg()) and
are always passed by reference. Brackets around the argument list in both the
caller and the definition are optional.

SYNC time% [,period]
or
SYNC

The SYNC command allows the user to implement very precisely timed
repeated actions (1-2 microseconds accuracy).
To enable this the command is first called with the parameter time%. This sets
up a repeating clock for time% microseconds. The optional parameter ‘period’
modifies the time and can be “U” for microseconds, “M” for milliseconds or
“S” for seconds.
Once the clock is set up the programis synchronised to it using the SYNC
command without parameters. This waits for the clock period to expire. For
periods below 2milliseconds this is non-interruptible. Above two milliseconds
the program will respond to Ctrl-C but not any MMBasic interrupts.
Typical use is to set the clock outside of a loop and then at the top of the loop



call the SYNC command without parameters. This means the contents of the
loop will be executed exactly once for each clock period set.
For example, the following would drive a servo with the required precise 50Hz
timing:
SYNC 20, M
DO
SYNC
PULSE GP0,n
LOOP
TEMPR START pin [,
precision]

This command can be used to start a conversion running on a DS18B20
temperature sensor connected to 'pin'.
Normally the TEMPR() function alone is sufficient to make a temperature
measurement so usage of this command is optional.
This command will start the measurement on the temperature sensor. The
program can then attend to other duties while the measurement is running and
later use the TEMPR() function to get the reading. If the TEMPR() function is
used before the conversion time has completed the function will wait for the
remaining conversion time before returning the value.
Any number of these conversions (on different pins) can be started and be
running simultaneously.
'precision' is the resolution of the measurement and is optional. It is a number
between 0 and 3 meaning:
0 = 0.5ºC resolution, 100 ms conversion time.
1 = 0.25ºC resolution, 200 ms conversion time (this is the default).
2 = 0.125ºC resolution, 400 ms conversion time.
3 = 0.0625ºC resolution, 800 ms conversion time.

TEXT x, y, string$
[,alignment$] [, font] [, scale]
[, c] [, bc]

Displays a string on an attached LCD panel starting at 'x' and 'y'.
‘string$’ is the string to be displayed. Numeric data should be converted to a
string and formatted using the Str$() function.
' alignment$' is a string expression or string variable consisting of 0, 1 or 2
letters where the first letter is the horizontal alignment around 'x' and can be L,
C or R for LEFT, CENTER, RIGHT and the second letter is the vertical
alignment around 'y' and can be T, M or B for TOP, MIDDLE, BOTTOM.
The default alignment is left/top.
For example. “CM” will centre the text vertically and horizontally.
The 'alignment$' string can be a constant (e.g. “CM”) or it can be a string
variable. For backwards compatibility with earlier versions of MMBasic the
string can also be unquoted (e.g. CM).
In the PicoMite a third letter can be used in the alignment string to indicate the
rotation of the text. This can be 'N' for normal orientation, 'V' for vertical text
with each character under the previous running from top to bottom, 'I' the text
will be inverted (i.e. upside down), 'U' the text will be rotated counter
clockwise by 90º and 'D' the text will be rotated clockwise by 90º
'font' and 'scale' are optional and default to that set by the FONT command.
'c' is the drawing colour and 'bc' is the background colour. They are optional
and default to the current foreground and background colours.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.



TIME$ = "HH:MM:SS"
or
TIME$ = "HH:MM"
or
TIME$ = "HH"

Sets the time of the internal clock. MM and SS are optional and will default to
zero if not specified. For example TIME$ = "14:30" will set the clock to 14:30
with zero seconds.
With OPTION RTC AUTO ENABLE the picomite starts with the TIME$
programmed in RTC.
Without OPTION RTC AUTO ENABLE the picomite starts with
TIME$="00:00:00"

TIMER = msec

Resets the timer to a number of milliseconds. Normally this is just used to
reset the timer to zero but you can set it to any positive number.
See the TIMER function for more details.

TRACE ON
or
TRACE OFF
or
TRACE LIST nn

TRACE ON/OFF will turn on/off the trace facility. This facility will print the
number of each line (counting from the beginning of the program) in square
brackets as the program is executed. This is useful in debugging programs.
TRACE LIST will list the last 'nn' lines executed in the format described
above. MMBasic is always logging the lines executed so this facility is always
available (i.e. it does not have to be turned on).

TRIANGLE X1, Y1, X2, Y2,
X3, Y3 [, C [, FILL]]

Draws a triangle on the LCD display panel with the corners at X1, Y1 and X2,
Y2 and X3, Y3. 'C' is the colour of the triangle and defaults to the current
foreground colour. 'FILL' is the fill colour and defaults to no fill (it can also be
set to -1 for no fill).
All parameters can be expressed as arrays and the software will plot the
number of triangles as determined by the dimensions of the smallest array
unless X1 = Y1 = X2 = Y2 = X3 = Y3 = -1 in which case processing will stop
at that point 'x1', 'y1', 'x2', 'y2', 'x3',and 'y3' must all be arrays or all be single
variables /constants otherwise an error will be generated 'c' and 'fill' can be
either arrays or single variables/constants.

TRIANGLE SAVE [#]n,
x1,y1,x2,y2,x3,y3

Saves a triangular area of the screen to buffer #n.

TRIANGLE RESTORE [#]n

Restores a saved triangular region of the screen and deletes the saved buffer.

UPDATE FIRMWARE

Causes the PicoMite to enter the firmware update mode (the same as applying
power while holding down the BOOTSEL button).
Loading the PicoMite firmware will erase the flash memory including the
current program, any programs saved in flash memory slots and all saved
variables. So make sure that you backup this data before you upgrade the
firmware. A firmware load will also reset all options to their defaults.

VAR SAVE var [, var]…
or
VAR RESTORE
or
VAR CLEAR

VAR SAVE will save one or more variables to non-volatile flash memory
where they can be restored later (normally after a power interruption).
'var' can be any number of numeric or string variables and/or arrays. Arrays
are specified by using empty brackets. For example: var()
VAR RESTORE will retrieve the previously saved variables and insert them
(and their values) into the variable table.
The VAR SAVE command can be used repeatedly. Variables that had been
previously saved will be updated with their new value and any new variables
(not previously saved) will be added to the saved list for later restoration.
VAR CLEAR will erase all saved variables. Also, the saved variables will be
automatically cleared by a firmware upgrade, by the NEW command or when
a new program is loaded via AUTOSAVE, XMODEM, etc.
This command is normally used to save calibration data, options, and other
data which does not change often but needs to be retained across a power
interruption. Normally the VAR RESTORE command is placed at the start of
the program so that previously saved variables are restored and immediately



available to the program when it starts. Notes:
 The storage space available to this command is 16KB.
 Using VAR RESTORE without a previous save will have no effect and
will not generate an error.
 If, when using RESTORE, a variable with the same name already exists its
value will be overwritten.
 Saved arrays must be declared (using DIM) before they can be restored.
 Be aware that string arrays can rapidly use up all the memory allocated to
this command. The LENGTH qualifier can be used when a string array is
declared to reduce the size of the array (see the DIM command). This is
not needed for ordinary string variables.
WATCHDOG timeout
or
WATCHDOG OFF
Or
WATCHDOG HW timeout
Or
WATCHDOG HW OFF

Starts the watchdog timer which will automatically restart the processor when
it has timed out. This can be used to recover from some event that disabled the
running program (such as an endless loop or a programming or other error that
halts a running program). This can be important in an unattended control
situation. The timeout can either be processed in the system timer interrupt or
as a true H/W watchdog.
'timeout' is the time in milliseconds (ms) before a restart is forced. This
command should be placed in strategic locations in the running BASIC
program to constantly reset the watchdog timer (to ‘timeout’) and therefore
prevent it from counting down to zero. If the H/W watchdog is used the timer
has a maximum of 8.3 seconds. No such limitation exists for the software
watchdog.
If the timer count does reach zero (perhaps because the BASIC program has
stopped running) the PicoMite will be automatically restarted and the
automatic variable MM.WATCHDOG will be set to true (i.e. 1) indicating that
an error occurred. On a normal startup MM.WATCHDOG will be set to false
(i.e. 0). Note that OPTION AUTORUN must be specified for the program to
restart.
WATCHDOG OFF can be used to disable the watchdog timer (this is the
default on a reset or power up). The timer is also turned off when the break
character (CTRL-C) is used on the console to interrupt a running program.

XMODEM SEND
or
XMODEM SEND file$
or
XMODEM RECEIVE
or
XMODEM RECEIVE file$
or
XMODEM CRUNCH

Transfers a BASIC program to or from a remote computer using the XModem
protocol. The transfer is done over the USB console connection.
XMODEM SEND will send the current program held in the PicoMite's
program memory to the remote device.
XMODEM RECEIVE will accept a program sent by the remote device and
save it into the PicoMite's the program memory overwriting the program
currently held there.
In both cases you can also specify 'file$' which will transfer the data to/from a
file on the Flash Filesystem or SD Card. If the file already exists it will be
overwritten when receiving a file.
Note that the data is buffered in RAM which limits the maximum transfer size.
This command also creates a backup of the program in flash memory which will
be automatically retrieved if the CPU is reset of the power is lost.
The CRUNCH option works like RECEIVE but will remove all comments,
blank lines and unnecessary spaces from the program before saving. This can
be used on large programs to allow them to fit into limited memory.
SEND, RECEIVE and CRUNCH can be abbreviated to S, R and C.
The XModem protocol requires a cooperating software program running on the
remote computer and connected to its serial port. It has been tested on Tera
Term running on Windows and it is recommended that this be used.
After running the XMODEM command in MMBasic select:
File -> Transfer -> XMODEM -> Receive/Send



from the Tera Term menu to start the transfer.
The transfer can take up to 15 seconds to start and if the XMODEM command
fails to establish communications it will return to the MMBasic prompt after
60 seconds and leave the program memory untouched.
Download Tera Term from http://ttssh2.sourceforge.jp/



Functions
Detailed Listing
Note that the functions related to communications functions (I2C, 1-Wire, and SPI) are not listed here but are
described in the appendices at the end of this document.
Square brackets indicate that the parameter or characters are optional.
ABS( number )

Returns the absolute value of the argument 'number' (i.e. any negative sign is
removed and a positive number is returned).

ACOS( number )

Returns the inverse cosine of the argument 'number' in radians.

ASC( string$ )

Returns the ASCII code (i.e. byte value) for the first letter in ‘string$’.

ASIN( number )

Returns the inverse sine value of the argument 'number' in radians.

ATN( number )

Returns the arctangent of the argument 'number' in radians.

ATAN2( y, x )

Returns the arc tangent of the two numbers x and y as an angle expressed in
radians.
It is similar to calculating the arc tangent of y / x, except that the signs of
both arguments are used to determine the quadrant of the result.

BIN$( number [, chars])

Returns a string giving the binary (base 2) value for the 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

BIN2STR$(type, value
[,BIG])

Returns a string containing the binary representation of 'value'.
'type' can be:
INT64
signed 64-bit integer converted to an 8 byte string
UINT64
unsigned 64-bit integer converted to an 8 byte string
INT32
signed 32-bit integer converted to a 4 byte string
UINT32
unsigned 32-bit integer converted to a 4 byte string
INT16
signed 16-bit integer converted to a 2 byte string
UINT16
unsigned 16-bit integer converted to a 2 byte string
INT8
signed 8-bit integer converted to a 1 byte string
UINT8
unsigned 8-bit integer converted to a 1 byte string
SINGLE
single precision floating point number converted to a 4 byte
string
DOUBLE double precision floating point number converted to a 8 byte
string
By default the string contains the number in little-endian format (i.e. the least
significant byte is the first one in the string). Setting the third parameter to
‘BIG’ will return the string in big-endian format (i.e. the most significant byte
is the first one in the string) In the case of the integer conversions, an error will
be generated if the ‘value’ cannot fit into the ‘type’ (e.g. an attempt to store the
value 400 in a INT8).
This function makes it easy to prepare data for efficient binary file I/O or for
preparing numbers for output to sensors and saving to flash memory.
See also the function STR2BIN



BOUND(array() [,dimension]

This returns the upper limit of the array for the dimension requested.
The dimension defaults to one if not specified. Specifying a dimension value of
0 will return the current value of OPTION BASE.
Unused dimensions will return a value of zero.
For example:
DIM myarray(44,45)
BOUND(myarray(),2) will return 45

CALL(userfunname$,
[,userfunparameters,..])

This is an efficient way of programmatically calling user defined functions.
(See also the CALL command). In many cases it can be used to eliminate
complex SELECT and IF THEN ELSEIF ENDIF clauses and is processed in a
much more efficient manner.
‘userfunname$’ can be any string or variable or function that resolves to the
name of a normal user function (not an in-built command).
‘userfunparameters’ are the same parameters that would be used to call the
function directly.
A typical use for this command could be writing any sort of emulator where
one of a large number of functions should be called depending on a some
variable. It also provides a method of passing a function name to another
subroutine or function as a variable.

CHOICE(condition,
ExpressionIfTrue,
ExpressionIfFalse)

This function allows you to do simple either/or selections more efficiently and
faster than using IF THEN ELSE ENDIF clauses.
The condition is anything that will resolve to nonzero (true) or zero (false).
The expressions are anything that you could normally assign to a variable or
use in a command and can be integers, floats or strings.
Examples:
PRINT CHOICE(1, "hello","bye") will print "Hello"
PRINT CHOICE (0, "hello","bye") will print "Bye"
a=1 : b=1 : PRINT CHOICE (a=b, 4, 5) will print 4

CHR$( number )

Returns a one-character string consisting of the character corresponding to the
ASCII code (i.e. byte value) indicated by argument 'number'.

CINT( number )

Round numbers with fractional portions up or down to the next whole number
or integer.
For example, 45.47 will round to 45
45.57 will round to 46
-34.45 will round to -34
-34.55 will round to -35
See also INT() and FIX().

COS( number )

Returns the cosine of the argument 'number' in radians.

CTRLVAL(#ref)

Returns the current value of an advanced control.
'#ref' is the control's reference. For controls like check boxes or switches it will
be the number one (true) indicating that the control has been selected by the
user or zero (false) if not. For controls that hold a number (e.g. a SPINBOX)
the value will be the number (normally a floating point number). For controls
that hold a string (e.g. TEXTBOX) the value will be a string.



CWD$

The current working directory on the Flash Filesystem or SD Card. Invalid for
exFAT format.
The format is: A:/dir1/dir2.

DATE$

Returns the current date based on MMBasic’s internal clock as a string in the
form "DD-MM-YYYY". For example, "28-07-2012".
The internal clock/calendar will keep track of the time and date including leap
years. To set the date use the command DATE$ =.

DATETIME$(n)

Returns the date and time corresponding to the epoch number n (number of
seconds that have elapsed since midnight GMT on January 1, 1970). The
format of the returned string is “dd-mm-yyyy hh:mm:ss”. Use the text NOW to
get the current datetime string, i.e. ? DATETIME$(NOW)

DAY$(date$)

Returns the day of the week for a given date as a string “Monday”, “Tuesday”
etc. The format for date$ is "DD-MM-YY", "DD-MM-YYYY", or "YYYYMM-DD". Use NOW to get the day for the current date, e.g. PRINT
DAY$(NOW)

DEG( radians )

Converts 'radians' to degrees.

DEVICE(WII funct)

Returns data from a Wii Classic controller.
'funct' is a 1 or 2 letter code indicating the information to return as follows:
LX returns the position of the analog left joystick x axis
LY returns the position of the analog left joystick y axis
RX returns the position of the analog right joystick x axis
RY returns the position of the analog right joystick y axis
L returns the position of the analog left button
R returns the position of the analog right button
B returns a bitmap of the state of all the buttons. A bit will be set to 1 if the
button is pressed.
T returns the ID code of the controller - should be hex &HA4200101
The button bitmap is as follows:
BIT 0: Button R
BIT 1: Button start
BIT 2: Button home
BIT 3: Button select
BIT 4: Button L
BIT 5: Button down cursor
BIT 6: Button right cursor
BIT 7: Button up cursor
BIT 8: Button left cursor
BIT 9: Button ZR
BIT 10: Button x
BIT 11: Button a
BIT 12: Button y
BIT 13: Button b
BIT 14: Button ZL



DIR$( fspec, type )
or
DIR$( fspec )
or
DIR$( )

Will search the default Flash Filesystem or SD Card for files and return the
names of entries found.
'fspec' is a file specification using wildcards the same as used by the FILES
command. E.g. "*.*" will return all entries, "*.TXT" will return text files.
Note that the wildcard *.* does not find files or folders without an extension.
'type' is the type of entry to return and can be one of:
VOL
Search for the volume label only
DIR
Search for directories only
FILE
Search for files only (the default if 'type' is not specified)
The function will return the first entry found. To retrieve subsequent entries
use the function with no arguments. i.e. DIR$( ). The return of an empty
string indicates that there are no more entries to retrieve.
This example will print all the files in a directory:
f$ = DIR$("*.*", FILE)
DO WHILE f$ <> ""
PRINT f$
f$ = DIR$()
LOOP
You must change to the required directory before invoking this command.

DISTANCE( trigger, echo )
or
DISTANCE( trig-echo )

Measure the distance to a target using the HC-SR04 ultrasonic distance sensor.
Four pin sensors have separate trigger and echo connections. 'trigger' is the I/O
pin connected to the "trig" input of the sensor and 'echo' is the pin connected to
the "echo" output of the sensor.
Three pin sensors have a combined trigger and echo connection and in that case
you only need to specify one I/O pin to interface to the sensor.
Note that any I/O pins used with the HC-SR04 should be 5V capable as the
HC-SR04 is a 5V device. The I/O pins are automatically configured by this
function and multiple sensors can be used on different I/O pins.
The value returned is the distance in centimetres to the target or -1 if no target
was detected or -2 if there was an error (i.e. sensor not connected).

EOF( [#]fnbr )

Will return true if the file previously opened on the Flash Filesystem or SD
Card for INPUT with the file number ‘#fnbr’ is positioned at the end of the file.
The # is optional. Also see the OPEN, INPUT and LINE INPUT commands
and the INPUT$ function.

EPOCH(DATETIME$)

Returns the epoch number (number of seconds that have elapsed since midnight
GMT on January 1, 1970) for the supplied DATETIME$ string.
The format for DATETIME$ is “dd-mm-yyyy hh:mm:ss”, “dd-mm-yy
hh:mm:ss”, or “yyyy-mm-dd hh:mm:ss”,. Use NOW to get the epoch number
for the current date and time, i.e. PRINT EPOCH(NOW)

EVAL( string$ )

Will evaluate 'string$' as if it is a BASIC expression and return the result.
'string$' can be a constant, a variable or a string expression. The expression can
use any operators, functions, variables, subroutines, etc that are known at the
time of execution. The returned value will be an integer, float or string
depending on the result of the evaluation.
For example: S$ = "COS(RAD(30)) * 100" : PRINT EVAL(S$)
Will display: 86.6025

EXP( number )

Returns the exponential value of 'number', i.e. e^x where x is 'number'.



FIELD$( string1, nbr, string2
[, string3] )

Returns a particular field in a string with the fields separated by delimiters.
'nbr' is the field to return (the first is nbr 1). 'string1' is the string to search and
'string2' is a string holding the delimiters (more than one can be used).
'string3' is optional and if specified will include characters that are used to
quote text in 'string1' (ie, quoted text will not be searched for a delimiter).
For example:
S$ = "foo, boo, zoo, doo"
r$ = FIELD$(s$, 2, ",")
will result in r$ = "boo". While:
s$ = "foo, 'boo, zoo', doo"
r$ = FIELD$(s$, 2, ",", "'")
will result in r$ = "boo, zoo".

FIX( number )

Truncate a number to a whole number by eliminating the decimal point and all
characters to the right of the decimal point.
For example 9.89 will return 9 and -2.11 will return -2.
The major difference between FIX() and INT() is that FIX() provides a true
integer function (i.e. does not return the next lower number for negative
numbers as INT() does). This behaviour is for Microsoft compatibility.
See also CINT() .

FORMAT$( nbr [, fmt$] )

Will return a string representing ‘nbr’ formatted according to the specifications
in the string ‘fmt$’.
The format specification starts with a % character and ends with a letter.
Anything outside of this construct is copied to the output as is.
The structure of a format specification is:
% [flags] [width] [.precision] type
Where ‘flags’ can be:
Left justify the value within a given field width
0
Use 0 for the pad character instead of space
+
Forces the + sign to be shown for positive numbers
space Causes a positive value to display a space for the sign. Negative
values still show the – sign
‘width’ is the minimum number of characters to output, less than this the
number will be padded, more than this the width will be expanded.
‘precision’ specifies the number of fraction digits to generate with an e, or f
type or the maximum number of significant digits to generate with a g type and
defaults to 4 digits. If specified, the precision must be preceded by a dot (.).
‘type’ can be one of:
g
Automatically format the number for the best presentation.
f
Format the number with the decimal point and following digits
e
Format the number in exponential format
If uppercase G or F is used the exponential output will use an uppercase E. If
the format specification is not specified “%g” is assumed.
Examples:
format$(45) will return 45
format$(45, “%g”) will return 45



GPS()

The GPS functions are used to return data from a serial communications
channel opened as GPS.
The function GPS(VALID) should be checked before any of these functions are
used to ensure that the returned value is valid.

GPS(ALTITUDE)

Returns current altitude (if sentence GGA is enabled).

GPS(DATE)

Returns the normal date string corrected for local time e.g. “12-01-2020”.

GPS(DOP)

Returns DOP (dilution of precision) value (if sentence GGA is enabled).

GPS(FIX)

Returns non zero (true) if the GPS has a fix on sufficient satellites and is
producing valid data.

GPS(GEOID)

Returns the geoid-ellipsoid separation (if sentence GGA is enabled).

GPS(LATITUDE)

Returns the latitude in degrees as a floating point number, values are negative
for South of equator

GPS(LONGITUDE)

Returns the longitude in degrees as a floating point number, values are
negative for West of the meridian.

GPS(SATELLITES)

Returns number of satellites in view (if sentence GGA is enabled).

GPS(SPEED)

Returns the ground speed in knots as a floating point number.

GPS(TIME)

Returns the normal time string corrected for local time e.g. “12:09:33”.

GPS(TRACK)

Returns the track over the ground (degrees true) as a floating point number.

GPS(VALID)

Returns: 0=invalid data, 1=valid data

HEX$( number [, chars])

Returns a string giving the hexadecimal (base 16) value for the 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

INKEY$

Checks the console input buffer and, if there is one or more characters waiting
in the queue, will remove the first character and return it as a single character in
a string.
If the input buffer is empty this function will immediately return with an empty
string (i.e. "").

INPUT$(nbr, [#]fnbr)

Will return a string composed of ‘nbr’ characters read from a serial
communications port opened as 'fnbr'. This function will return as many
characters as are waiting in the receive buffer up to ‘nbr’. If there are no
characters waiting it will immediately return with an empty string.
#0 can be used which refers to the console's input buffer.
The # is optional. Also see the OPEN command.



INSTR( [start-position,]
string-searched$, stringpattern$ [,size] )

Returns the position at which 'string-pattern$' occurs in 'string-searched$',
beginning at 'start-position'. If 'start-position' is not provided it will default to
1.
Both the position returned and 'start-position' use 1 for the first character, 2 for
the second, etc.
The function returns zero if 'string-pattern$' is not found.
If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.

INT( number )

Truncate an expression to the next whole number less than or equal to the
argument. For example 9.89 will return 9 and -2.11 will return -3.
This behaviour is for Microsoft compatibility, the FIX() function provides a
true integer function. See also CINT() .

LCASE$( string$ )

Returns ‘string$’ converted to lowercase characters.

LCOMPARE(array1%(),
array2%())

Compare the contents of two long string variables array1%() and array2%().
The returned is an integer and will be -1 if array1%() is less than array2%(). It
will be zero if they are equal in length and content and +1 if array1%() is
greater than array2%(). The comparison uses the ASCII character set and is
case sensitive.

LEFT$( string$, nbr )

Returns a substring of ‘string$’ with ‘nbr' of characters from the left
(beginning) of the string.

LEN( string$ )

Returns the number of characters in 'string$'.

LGETBYTE(array%(), n)

Returns the numerical value of the 'n'th byte in the LONGSTRING held in
'array%()'. This function respects the setting of OPTION BASE in determining
which byte to return.

LGETSTR$(array%(), start,
length)

Returns part of a long string stored in array%() as a normal MMBasic string.
The parameters start and length define the part of the string to be returned.

LINSTR(array%(), search$
[,start] [,size]))

Returns the position of a search string in a long string. The returned value is an
integer and will be zero if the substring cannot be found. array%() is the string
to be searched and must be a long string variable. Search$ is the substring to
look for and it must be a normal MMBasic string or expression (not a long
string). The search is case sensitive.
Normally the search will start at the first character in 'str' but the optional third
parameter allows the start position of the search to be specified.
If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.

LLEN(array%())

Returns the length of a long string stored in array%()

LOC( [#]fnbr )

For a serial communications port opened as 'fnbr' this function will return the
number of bytes received and waiting in the receive buffer to be read.
#0 can be used which refers to the console's input buffer.
The # is optional.



LOF( [#]fnbr )

For a serial communications port opened as 'fnbr' this function will return the
space (in characters) remaining in the transmit buffer.
Note that when the buffer is full MMBasic will pause when adding a new
character and wait for some space to become available.
The # is optional.

LOG( number )

Returns the natural logarithm of the argument 'number'.

MATH

The math function performs many simple mathematical calculations that can be
programmed in Basic but there are speed advantages to coding looping
structures in C and there is the advantage that once debugged they are there for
everyone without re-inventing the wheel.

Simple functions
MATH(ATAN3 x,y)

Returns ATAN3 of x and y

MATH(COSH a)

Returns the hyperbolic cosine of a

MATH(LOG10 a)

Returns the base 10 logarithm of a

MATH(SINH a)

Returns the hyperbolic sine of a

MATH(TANH a)

Returns the hyperbolic tan of a

MATH(CRCn data [,length]
[,polynome] [,startmask]
[,endmask] [,reverseIn]
[,reverseOut]

Calculates the CRC to n bits (8, 12, 16, 32) of “data”. “data” can be an integer
or floating point array or a string variable. “Length” is optional and if not
specified the size of the array or string length is used. The defaults for
startmask, endmask reverseIn, and reversOut are all zero. reverseIn, and
reversOut are both Booleans and take the value 1 or 0. The defaults for
polynomes are CRC8=&H07, CRC12=&H80D, CRC16=&H1021,
crc32=&H04C11DB7
e.g. for crc16_CCITT use MATH(CRC16 array(), n,, &HFFFF)

MATH(RAND)

Returns a random number 0.0 <= n < 1.0 using the "Mersenne Twister
algorithm. If not seeded with MATH RANDOMIZE the first usage seeds with
the time in microseconds since boot

Simple Statistics
Returns the Pearson's chi-squared value of the two dimensional array a())
MATH(CHI a())
MATH(CHI_p a())

MATH(CROSSING array()
[,level] [,direction]

MATH(CORREL a(), a())
MATH(MAX a() [,index%])


Returns the associated probability in % of the Pearson's chi-squared value of
the two dimensional array a())

This returns the array index at which the values in the array pass the "level" in
the direction specified. level defaults to 0. Direction defaults to 1 ( valid values
are -1 or 1)
Returns the Pearson’s correlation coefficient between arrays a() and b()
Returns the maximum of all values in the a() array, a() can have any number of


dimensions. If the integer variable is specified then it will be updated with the
index of the maximum value in the array. This is only available on onedimensional arrays
MATH(MEAN a())

Returns the average of all values in the a() array, a() can have any number of
dimensions

MATH(MEDIAN a())

Returns the median of all values in the a() array, a() can have any number of
dimensions

MATH(MIN a(), [index%])

Returns the minimum of all values in the a() array, a() can have any number of
dimensions. If the integer variable is specified then it will be updated with the
index of the maximum value in the array. This is only available on onedimensional arrays.

MATH(SD a())

Returns the standard deviation of all values in the a() array, a() can have any
number of dimensions

MATH(SUM a())

Returns the sum of all values in the a() array, a() can have any number of
dimensions

Vector Arithmetic
MATH(MAGNITUDE v())

Returns the magnitude of the vector v(). The vector can have any number of
elements

MATH(DOTPRODUCT
v1(), v2())

Returns the dot product of two vectors v1() and v2(). The vectors can have any
number of elements but must have the same cardinality

Matrix Arithmetic
MATH(M_DETERMINANT
array!())

Returns the determinant of the array. The array must be square.

Creation
complex% = MATH(C_CPLX r!, i!)
complex% = MATH(C_POLAR radius!, angle!)
Floating returns
real! = MATH(C_REAL complex%)
imag! = MATH(C_IMAG complex%)
arg! = MATH(C_ARG complex%)
mod! = MATH(C_MOD complex%)
phase! = MATH(C_PHASE complex%)
Unary functions
complex1% = MATH(C_CONJ complex2%)
complex1% = MATH(C_SIN complex2%)
complex1% = MATH(C_COS complex2%)
complex1% = MATH(C_TAN complex2%)


MMBasic supports a full range of functions to
allow the manipulation of complex numbers. In
this implementation complex numbers have a 32bit real and 32-bit imaginary part and to make
this work in MMBasic, it uses integers (64-bit) to
hold these.


complex1% = MATH(C_ASIN complex2%)
complex1% = MATH(C_ACOS complex2%)
complex1% = MATH(C_ATAN complex2%)
complex1% = MATH(C_SINH complex2%)
complex1% = MATH(C_COSH complex2%)
complex1% = MATH(C_TANH complex2%)
complex1% = MATH(C_ASINH complex2%)
complex1% = MATH(C_ACOSH complex2%)
complex1% = MATH(C_ATANH complex2%)
complex1% = MATH(C_PROJ complex2%)
Basic Arithmetic
complex1% = MATH(C_ADD complex2%,complex3%)
complex1% = MATH(C_SUB complex2%,complex3%)
complex1% = MATH(C_MUL complex2%,complex3%)
complex1% = MATH(C_DIV complex2%,complex3%)
complex1% = MATH(C_POW complex2%,complex3%)
complex1% = MATH(C_AND complex2%,complex3%)
complex1% = MATH(C_OR complex2%,complex3%)
complex1% = MATH(C_XOR complex2%,complex3%)
MAX( arg1 [, arg2 [, …]] )
or
MIN( arg1 [, arg2 [, …]] )

Returns the maximum or minimum number in the argument list.
Note that the comparison is a floating point comparison (integer arguments are
converted to floats) and a float is returned.

MID$( string$, start )
or
MID$( string$, start, nbr )

Returns a substring of ‘string$’ beginning at ‘start’ and continuing for ‘nbr’
characters. The first character in the string is number 1.
If ‘nbr’ is omitted the returned string will extend to the end of ‘string$’

MSGBOX (msg$, b1$ [,b2$
… b4$])

This function will display a message box on the screen with one to four touch
sensitive buttons. All other controls will be disabled until the user touches one
of the buttons. The message box will then be erased, the previous controls will
be restored and the function will return the number of the button touched (the
first button is number one)
'msg$' is the message to display. This can contain one or more tilde characters
(~) which indicate a line break. Up to 10 lines can be displayed inside the box.
'b1$' is the caption for the first button, 'b2$' is the caption for the second button,
etc. At least one button must be specified and four is the maximum. Any
buttons not included in the argument list will not be displayed.

OCT$( number [, chars])

Returns a string giving the octal (base 8) representation of 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

PEEK(BYTE addr%)
or
PEEK(SHORT addr%)
or
PEEK(WORD addr%)
or
PEEK(INTEGER addr%)
or
PEEK(FLOAT addr%)

Will return a byte or a word within the PIC32 virtual memory space.
BYTE will return the byte (8-bits) located at 'addr%'
SHORT will return the short integer (16-bits) located at 'addr%'


WORD will return the word (32-bits) located at 'addr%'
INTEGER will return the integer (64-bits) located at 'addr%'
FLOAT will return the floating point number (32-bits) located at 'addr%'


or
PEEK(VARADDR var)
or
PEEK(CFUNADDR cfun)
or
PEEK(VAR var, ±offset)
or
PEEK( VARTBL, ±offset)
or
PEEK( PROGMEM, ±offset)

VARADDR will return the address (32-bits) of the variable 'var' in memory.
An array is specified as var().
CFUNADDR will return the address (32-bits) of the CFunction 'cfun' in
memory. This address can be passed to another CFunction which can then call
it to perform some common process.
VAR, will return a byte in the memory allocated to 'var'. An array is specified
as var().
VARTBL, will return a byte in the memory allocated to the variable table
maintained by MMBasic. Note that there is a comma after the keyword
VARTBL.
PROGMEM, will return a byte in the memory allocated to the program. Note
that there is a comma after the keyword PROGMEM.
Note that 'addr%' should be an integer.

PEEK(WP,n%)

peek(bp n%) ' returns the byte at address n% and increments n% to point to the
next byte
peek(sp n%) ' returns the short at address n% and increments n% to point to the
next short
peek(wp n%) ' returns the word at address n% and increments n% to point to
the next word

PI

Returns the value of pi.

PIN( pin )

Returns the value on the external I/O ‘pin’. Zero means digital low, 1 means
digital high and for analogue inputs it will return the measured voltage as a
floating point number.
Frequency inputs will return the frequency in Hz. A period input will return
the period in milliseconds while a count input will return the count since reset
(counting is done on the positive rising edge). The count input can be reset to
zero by resetting the pin to counting input (even if it is already so configured).
This function will also return the state of a pin configured as an output or a PIO
pin.
Also see the SETPIN and PIN() = commands. Refer to the section Using the
I/O pins for a general description of the PicoMite's input/output capabilities.

PIN( TEMP )

Returns the temperature of the RP2040 chip (see the RP2040 data sheet for the
details)

PIO(DMA RX POINTER)
PIO(DMA TX POINTER)

Returns the current data item being written or read by the PIO

PIO (SHIFTCTRL
push_threshold
[,pull_threshold] [,autopush]
[,autopull] [,in_shiftdir]
[,out_shiftdir] [,fjoin_rx]
[,fjoin_tx])

helper function to calculate the value of shiftctrl for the INIT MACHINE
command

PEEK(BP, n%)
PEEK(SP,n%)



PIO (PINCTRL
no_side_set_pins
[,no_set_pins] [,no_out_pins]
[,IN base]
[,side_set_base] [,set_base][,
out_base])

helper function to calculate the value of pinctrl for the INIT MACHINE
command. Note: The pin parameters must be formatted as GPn.

PIO (EXECCTRL jmp_pin
,wrap_target, wrap
[,side_pindir] [,side_en])

helper function to calculate the value of execctrl for the INIT MACHINE
command

PIO (FDEBUG pio)

returns the value of the FSDEBUG register for the pio specified

PIO (FSTAT pio)

returns the value of the FSTAT register for the pio specified

PIO (FLEVEL pio)

returns the value of the FLEVEL register for the pio specified
PIO(FLEVEL pio)

PIO(FLEVEL pio ,sm, DIR)

dir can be RX or TX. Returns the level of the specific fifo

PIO(.WRAP)
PIO(.WRAP TARGET)

returns the location of the .wrap directive in PIO ASSEMBLE
returns the location of the .wrap target directive in PIO ASSEMBLE.
These can be used in the PIO(EXECCTRL function as follows:
PIO (EXECCTRL jmp_pin PIO(.WRAP TARGET), PIO(.WRAP)
[,side_pindir] [,side_en])

PORT(start, nbr [,start,
nbr]…)

Returns the value of a number of I/O pins in one operation.
'start' is an I/O pin number and its value will be returned as bit 0. 'start'+1 will be
returned as bit 1, 'start'+2 will be returned as bit 2, and so on for 'nbr' number of
bits. I/O pins used must be numbered consecutively and any I/O pin that is
invalid or not configured as an input will cause an error. The start/nbr pair can be
repeated up to 25 times if additional groups of input pins need to be added.
This function will also return the state of a pin configured as an output. It can
be used to conveniently communicate with parallel devices like memory chips.
Any number of I/O pins (and therefore bits) can be used from 1 to the number
of I/O pins on the chip.
See the PORT command to simultaneously output to a number of pins.

PIXEL( x, y)

Returns the colour of a pixel on an LCD display. 'x' is the horizontal
coordinate and 'y' is the vertical coordinate of the pixel. The display must use
one of the SSD1963, ILI9341, ILI9488, or ST7789_320 controllers.

PULSIN( pin, polarity )
or
PULSIN( pin, polarity, t1 )
or
PULSIN( pin, polarity, t1, t2
)

Measures the width of an input pulse from 1µs to 1 second with 0.1µs
resolution.
'pin' is the I/O pin to use for the measurement, it must be previously configured
as a digital input. 'polarity' is the type of pulse to measure, if zero the function
will return the width of the next negative pulse, if non zero it will measure the
next positive pulse.
't1' is the timeout applied while waiting for the pulse to arrive, 't2' is the timeout
used while measuring the pulse. Both are in microseconds (µs) and are
optional. If 't2' is omitted the value of 't1' will be used for both timeouts. If
both 't1' and 't2' are omitted then the timeouts will be set at 100000 (i.e.



100ms).
This function returns the width of the pulse in microseconds (µs) or -1 if a
timeout has occurred. The measurement is accurate to ±0.5% and ±0.5µsNote
that this function will cause the running program to pause while the
measurement is made and interrupts will be ignored during this period.
RAD( degrees )

Converts 'degrees' to radians.

RGB(red, green, blue)
or
RGB(shortcut)

Generates an RGB true colour value.
'red', 'blue' and 'green' represent the intensity of each colour. A value of zero
represents black and 255 represents full intensity.
'shortcut' allows common colours to be specified by naming them. The colours
that can be named are white, black, blue, green, cyan, red, magenta, yellow,
brown, white, orange, pink, gold, salmon, beige, lightgrey and grey (or USA
spelling gray/lightgray). For example, RGB(red) or RGB(cyan).
Note that the value returned is an integer and, if it is to be saved, the variable
should be declared as an integer to retain the accuracy of the number.

RIGHT$( string$, number-ofchars )

Returns a substring of ‘string$’ with ‘number-of-chars’ from the right (end) of
the string.

RND( number )
or
RND

Returns a pseudo-random number in the range of 0 to 0.999999. The 'number'
value is ignored if supplied. The RANDOMIZE command reseeds the random
number generator.

SGN( number )

Returns the sign of the argument 'number', +1 for positive numbers, 0 for 0, and
-1 for negative numbers.

SIN( number )

Returns the sine of the argument 'number' in radians.

SPACE$( number )

Returns a string of blank spaces 'number' characters long.

SPI ( data )
or
SPI2 ( data )

Send and receive data using an SPI channel.
A single SPI transaction will send data while simultaneously receiving data
from the slave. ‘data’ is the data to send and the function will return the data
received during the transaction. ‘data’ can be an integer or a floating point
variable or a constant.

SQR( number )

Returns the square root of the argument 'number'.

STR$( number )
or
STR$( number, m )
or
STR$( number, m, n )
or
STR$( number, m, n, c$ )

Returns a string in the decimal (base 10) representation of 'number'.
If 'm' is specified sufficient spaces will be added to the start of the number to
ensure that the number of characters before the decimal point (including the
negative or positive sign) will be at least 'm' characters. If 'm' is zero or the
number has more than 'm' significant digits no padding spaces will be added.
If 'm' is negative, positive numbers will be prefixed with the plus symbol and
negative numbers with the negative symbol. If 'm' is positive then only the
negative symbol will be used.
'n' is the number of digits required to follow the decimal place. If it is zero the
string will be returned without the decimal point. If it is negative the output
will always use the exponential format with 'n' digits resolution. If 'n' is not
specified the number of decimal places and output format will vary



automatically according to the number.
'c$' is a string and if specified the first character of this string will be used as
the padding character instead of a space (see the 'm' argument).
Examples:
STR$(123.456)
will return "123.456"
STR$(-123.456)
will return "-123.456"
STR$(123.456, 1)
will return "123.456"
STR$(123.456, -1)
will return "+123.456"
STR$(123.456, 6)
will return "
123.456"
STR$(123.456, -6)
will return " +123.456"
STR$(-123.456, 6)
will return " -123.456"
STR$(-123.456, 6, 5) will return " -123.45600"
STR$(-123.456, 6, -5) will return "
-1.23456e+02"
STR$(53, 6)
will return "
53"
STR$(53, 6, 2)
will return "
53.00"
STR$(53, 6, 2, "*")
will return "****53.00"
STR2BIN(type, string$
[,BIG])

Returns a number equal to the binary representation in ‘string$’.
‘type’ can be:
INT64 converts 8 byte string representing a signed 64-bit integer to an integer
UINT64 converts 8 byte string representing an unsigned 64-bit integer to an
integer
INT32 converts 4 byte string representing a signed 32-bit integer to an integer
UINT32 converts 4 byte string representing an unsigned 32-bit integer to an
integer
INT16 converts 2 byte string representing a signed 16-bit integer to an integer
UINT16 converts 2 byte string representing an unsigned 16-bit integer to an
integer
INT8 converts 1 byte string representing a signed 8-bit integer to an integer
UINT8 converts 1 byte string representing an unsigned 8-bit integer to an
integer
SINGLE converts 4 byte string representing single precision float to a float
DOUBLE converts 8 byte string representing single precision float to a float
By default the string must contain the number in little-endian format (i.e. the
least significant byte is the first one in the string). Setting the third parameter
to ‘BIG’ will interpret the string in big-endian format (i.e. the most
significant byte is the first one in the string).
This function makes it easy to read data from binary data files, interpret
numbers from sensors or efficiently read binary data from flash memory
chips.
An error will be generated if the string is the incorrect length for the
conversion requested
See also the function BIN2STR$

STRING$( nbr, ascii )
or
STRING$( nbr, string$ )

Returns a string 'nbr' bytes long consisting of either the first character of string$
or the character representing the ASCII value 'ascii' which is an integer or float
number in the range of 0 to 255.

TAB( number )

Outputs spaces until the column indicated by 'number' has been reached on the
console output.



TAN( number )

Returns the tangent of the argument 'number' in radians.

TEMPR( pin )

Return the temperature measured by a DS18B20 temperature sensor connected
to 'pin' (which does not have to be configured).
The returned value is degrees C with a default resolution of 0.25ºC. If there is
an error during the measurement the returned value will be 1000.
The time required for the overall measurement is 200ms and interrupts will be
ignored during this period. Alternatively the TEMPR START command can be
used to start the measurement and your program can do other things while the
conversion is progressing. When this function is called the value will then be
returned instantly assuming the conversion period has expired. If it has not,
this function will wait out the remainder of the conversion time before
returning the value.
The DS18B20 can be powered separately by a 3V to 5V supply or it can
operate on parasitic power from the PicoMite.
See the section Special Hardware Devices for more details.

TIME$

Returns the current time based on MMBasic's internal clock as a string in the
form "HH:MM:SS" in 24 hour notation. For example, "14:30:00".
To set the current time use the command TIME$ = .

TIMER

Returns the elapsed time in milliseconds (e.g. 1/1000 of a second) since reset.
The timer is reset to zero on power up or a CPU restart and you can also reset it
by using TIMER as a command. If not specifically reset it will continue to
count up forever (it is a 64 bit number and therefore will only roll over to zero
after 200 million years).

TOUCH(X)
or
TOUCH(Y)

Will return the X or Y coordinate of the location currently touched on an LCD
panel.
If the screen is not being touched the function will return -1.

UCASE$( string$ )

Returns ‘string$’ converted to uppercase characters.

VAL( string$ )

Returns the numerical value of the ‘string$’. If 'string$' is an invalid number
the function will return zero.
This function will recognise the &H prefix for a hexadecimal number, &O for
octal and &B for binary.



Obsolete Commands and Functions
Detailed Listing
These commands and functions are mostly included to assist in converting programs written for Microsoft
BASIC. For new programs the corresponding modern commands in MMBasic should be used.
Note that these commands may be removed in the future to recover memory for other features.
BITBANG

Replaced by the command DEVICE. For compatibility BITBANG can still be
used in programs and will be automatically converted to DEVICE

GOSUB target

Initiates a subroutine call to the target, which can be a line number or a label.
The subroutine must end with RETURN.
New programs should use defined subroutines (i.e. SUB…END SUB).

IF condition THEN linenbr

For Microsoft compatibility a GOTO is assumed if the THEN statement is
followed by a number. A label is invalid in this construct.
New programs should use: IF condition THEN GOTO linenbr | label

IRETURN

Returns from an interrupt when the interrupt destination was a line number or a
label.
New programs should use a user defined subroutine as an interrupt destination.
In that case END SUB or EXIT SUB will cause a return from the interrupt.

ON nbr GOTO | GOSUB
target[,target, target,..]

ON either branches (GOTO) or calls a subroutine (GOSUB) based on the
rounded value of 'nbr'; if it is 1, the first target is called, if 2, the second target
is called, etc. Target can be a line number or a label.
New programs should use SELECT CASE.

POS

For the console, returns the current cursor position in the line in characters.

PAGE

Replaced with “GUI PAGE”

RETURN

RETURN concludes a subroutine called by GOSUB and returns to the
statement after the GOSUB.



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
TX is data from the PicoMite and RX is data to it.
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
 ‘n’ is the serial port number for either COM1: or COM2:.
 ‘baud’ is the baud rate. This can be any number from 1200 to 921600. Default is 9600.
 ‘buf’ is the receive buffer size in bytes (default size is 256). The transmit buffer is fixed at 256 bytes.
 ‘int’ is interrupt subroutine to be called when the serial port has received some data.
 ‘int-trigger’ is the number of characters received which will trigger an interrupt.
All parameters except the serial port name (COMn:) are optional. If any one parameter is left out then all the
following parameters must also be left out and the defaults will be used.
Five options can be added to the end of 'comspec$'. These are:
 'S2' specifies that two stop bits will be sent following each character transmitted.
 EVEN specifies that an even parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set.
 ODD specifies that an odd parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set
 7BIT specifies that there a 7bits of data. This is normally used with EVEN or ODD
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
the section Using the I/O pins for a description).
When using interrupts you need to be aware that it will take some time for MMBasic to respond to the interrupt
and more characters could have arrived in the meantime, especially at high baud rates. For example, if you
have specified the interrupt level as 200 characters and a buffer of 256 characters then quite easily the buffer
will have overflowed by the time the interrupt subroutine can read the data. In this case the buffer should be
increased to 512 characters or more.



Appendix B – I2C Communications
I2C Communications
There are two I2C channels. They can operate in master or slave mode.

I/O Pins
Before the I2C interface can be used the I/O pins must be defined using the following command for the first
channel (referred as I2C):
SETPIN sda, scl, I2C
Valid pins are
SDA: GP0, GP4, GP8, GP12, GP16, GP20 or GP28
SCL: GP1, GP5, GP9, GP13, GP17 or GP21
And the following command for the second channel (referred to as I2C2):
SETPIN sda, scl, I2C2
Valid pins are
SDA: GP2, GP6, GP10, GP14, GP18, GP22 or GP26
SCL: GP3, GP7, GP11, GP15, GP19 or GP27
2
When running the I C bus at above 100 kHz the cabling between the devices becomes important. Ideally the
cables should be as short as possible (to reduce capacitance) and the data and clock lines should not run next to
each other but have a ground wire between them (to reduce crosstalk).
If the data line is not stable when the clock is high, or the clock line is jittery, the I2C peripherals can get
"confused" and end up locking the bus (normally by holding the clock line low). If you do not need the higher
speeds then operating at 100 kHz is the safest choice.

I2C Master Commands
There are four commands that can be used for the first channel (I2C) in master mode as follows.
The commands for the second channel (I2C2) are identical except that the command is I2C2
I2C OPEN speed,
timeout

Enables the I2C module in master mode. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
‘speed’ is the clock speed (in KHz) to use and must be either 100 or 400.
‘timeout’ is a value in milliseconds after which the master send and receive
commands will be interrupted if they have not completed. The minimum value is
100. A value of zero will disable the timeout (though this is not recommended).

I2C WRITE addr,
option, sendlen,
senddata [,sendata ..]

Send data to the I2C slave device. The I2C command refers to channel 1 while the
command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘sendlen’ is the number of bytes to send.
‘senddata’ is the data to be sent - this can be specified in various ways (all data
sent will be sent as bytes with a value between 0 and 255):
 The data can be supplied as individual bytes on the command line.
Example: I2C WRITE &H6F, 0, 3, &H23, &H43, &H25
 The data can be in a one dimensional array specified with empty brackets (i.e.
no dimensions). ‘sendlen’ bytes of the array will be sent starting with the first
element. Example: I2C WRITE &H6F, 0, 3, ARRAY()
 The data can be a string variable (not a constant).
Example: I2C WRITE &H6F, 0, 3, STRING$



I2C READ addr,
option, rcvlen, rcvbuf

Get data from the I2C slave device. The I2C command refers to channel 1 while
the command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘rcvlen’ is the number of bytes to receive.
‘rcvbuf’ is the variable or array used to save the received data - this can be:
 A string variable. Bytes will be stored as sequential characters in the string.
 A one dimensional array of numbers specified with empty brackets. Received
bytes will be stored in sequential elements of the array starting with the first.
Example: I2C READ &H6F, 0, 3, ARRAY()
 A normal numeric variable (in this case rcvlen must be 1).

I2C CLOSE

Disables the master I2C module and returns the I/O pins to a "not configured" state.
This command will also send a stop if the bus is still held.

I2C Slave Commands
I2C SLAVE OPEN
addr, send_int,
rcv_int

Enables the I2C module in slave mode. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave I2C address.
‘send_int’ is the subroutine to be invoked when the module has detected that the
master is expecting data.
‘rcv_int is the subroutine to be called when the module has received data from the
master. Note that this is triggered on the first byte received so your program might
need to wait until all the data is received.

I2C SLAVE WRITE
sendlen, senddata
[,sendata ..]

Send the data to the I2C master. The I2C command refers to channel 1 while the
command I2C2 refers to channel 2 using the same syntax.
This command should be used in the send interrupt (ie in the 'send_int' subroutine
when the master has requested data). Alternatively, a flag can be set in the
interrupt subroutine and the command invoked from the main program loop when
the flag is set.
‘sendlen is the number of bytes to send.
‘senddata’ is the data to be sent. This can be specified in various ways, see the I2C
WRITE commands for details.

I2C SLAVE READ
rcvlen, rcvbuf, rcvd

Receive data from the I2C master device. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
This command should be used in the receive interrupt (ie in the 'rcv_int' subroutine
when the master has sent some data). Alternatively a flag can be set in the receive
interrupt subroutine and the command invoked from the main program loop when
the flag is set.
‘rcvlen’ is the maximum number of bytes to receive.
‘rcvbuf’ is the variable to receive the data. This can be specified in various ways,
see the I2C READ commands for details.
‘rcvd’ is a variable that, at the completion of the command, will contain the actual
number of bytes received (which might differ from ‘rcvlen’).

I2C SLAVE CLOSE

Disables the slave I2C module and returns the external I/O pins to a "not
configured" state. They can then be configured using SETPIN.



Errors
Following an I2C write or read the automatic variable MM.I2C will be set to indicate the result as follows:
0 = The command completed without error.
1 = Received a NACK response
2 = Command timed out

7-Bit Addressing
The standard addresses used in these commands are 7-bit addresses (without the read/write bit). MMBasic will
add the read/write bit and manipulate it accordingly during transfers.
Some vendors provide 8-bit addresses which include the read/write bit. You can determine if this is the case
because they will provide one address for writing to the slave device and another for reading from the slave. In
these situations you should only use the top seven bits of the address. For example: If the read address is 9B
(hex) and the write address is 9A (hex) then using only the top seven bits will give you an address of 4D (hex).
Another indicator that a vendor is using 8-bit addresses instead of 7-bit addresses is to check the address range.
All 7-bit addresses should be in the range of 08 to 77 (hex). If your slave address is greater than this range then
probably your vendor has provided an 8-bit address.

Examples
As an example of a simple communications where the PicoMite is the master, the following program
will read and display the current time (hours and minutes) maintained by a PCF8563 real time clock
chip connected to the second I2C channel:
DIM AS INTEGER RData(2)
' this will hold received data
SETPIN GP6, GP5, I2C2
' assign the I/O pins for I2C2
I2C2 OPEN 100, 1000
' open the I2C channel
I2C2 WRITE &H51, 0, 1, 3
' set the first register to 3
I2C2 READ &H51, 0, 2, RData()
' read two registers
I2C2 CLOSE
' close the I2C channel
PRINT "Time is " RData(1) ":" RData(0)

This is an example of communications between two PicoMites where one is the master and the other
is the slave.
First the master:
SETPIN GP2, GP3, I2C2
I2C2 OPEN 100, 1000
i = 10
DO
i = i + 1
a$ = STR$(i)
I2C2 WRITE &H50, 0, LEN(a$), a$
PAUSE 200
I2C2 READ &H50, 0, 8, a$
PRINT a$
PAUSE 200
LOOP

Then the slave:
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



Appendix C – 1-Wire Communications
1-Wire Communications
The 1-Wire protocol was developed by Dallas Semiconductor to communicate with chips using a single
signalling line. This implementation was written for MMBasic by Gerard Sexton.
There are three commands that you can use:
ONEWIRE RESET pin
ONEWIRE WRITE pin, flag, length, data [, data…]
ONEWIRE READ pin, flag, length, data [, data…]

Reset the 1-Wire bus
Send a number of bytes
Get a number of bytes

Where:
pin - The PicoMite I/O pin to use. It can be any pin capable of digital I/O.
flag - A combination of the following options:
1 - Send reset before command
2 - Send reset after command
4 - Only send/recv a bit instead of a byte of data
8 - Invoke a strong pullup after the command (the pin will be set high and open drain disabled)
length - Length of data to send or receive
data - Data to send or variable to receive.
The number of data items must agree with the length parameter.
The automatic variable MM.ONEWIRE returns true if a device was found
After the command is executed, the I/O pin will be set to the not configured state unless flag option 8 is used.
When a reset is requested the automatic variable MM.ONEWIRE will return true if a device was found. This
will occur with the ONEWIRE RESET command and the ONEWIRE READ and ONEWIRE WRITE
commands if a reset was requested (flag = 1 or 2).
The 1-Wire protocol is often used in communicating with the DS18B20 temperature measuring sensor and to
help in that regard MMBasic includes the TEMPR() function which provides a convenient method of directly
reading the temperature of a DS18B20 without using these functions.



Appendix D – SPI Communications
SPI Communications
The Serial Peripheral Interface (SPI) communications protocol is used to send and receive data between
integrated circuits. The PicoMite acts as the master (i.e. it generates the clock).

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
TX is data from the PicoMite and RX is data to it.

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
If you do not want to send any data (i.e. you wish to receive only) any number (e.g. zero) can be used for the
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


Appendix E – Regex Syntax
Regex Syntax
The alternate forms of the INSTR() and LINSTR() functions can take a regular expression as the search pattern.
The alternate form of the commands are:
INSTR([start],text$, search$ [,size])
LINSTR(text%(),search$ [,start] [,size]
In both cases specifying the size parameter causes the firmware to interpret the search string as a regular
expression. The size parameter is a floating point variable that is used by the firmware to return the size of a
matching string. If the variable doesn't exist it is created. As implemented in MMBasic you need to apply the
returned start and size values to the MID$ function to extract the matched string. e.g.
IF start THEN match$=MID$(text$,start,size) ELSE match$=”” ENDIF
The library used for the regular expressions “implements POSIX draft P1003.2/D11.2, except for some of the
internationalization features”. See http://mirror.math.princeton.edu/pub/oldlinux/Linux.old/Refdocs/POSIX/all.pdf section 2.8 for details of constructing Regular Expressions or other online tutorials if you
are not familiar with them.
The syntax of regular expressions can vary slightly with the various implementations. This document is a
summary of the syntax and supported operations used in the MMBasic implementation.
Anchors
^ Start of string
$ End of string
\b Word Boundary
\B Not a word boundary
\< Start of word
\> End of word
Qualifiers
*
0 or more (not escaped)
\+
1 or more
\?
0 or 1
\{3\} Exactly 3
\{3,\} 3 or more
\{3,5\} 3,4 or 5
Groups and Ranges
(a\|b)
a or b
\(…\) group
[abc]
Range (a or b or c)
[^abc] Not (a or b or c]
[a-q]
lower case letters a to q
[A-Q] upper case letters A to Q
[0-7]
Digits from 0 to 7
Escapes Required to Match Normal Characters
\^ to match ^ (caret)
\.
to match . (dot)
\* to match * (asterix)
\$ to match $ (dollar)
\[ to match [ (left bracket)
\\
to match \ (backslash)



Escapes with Special Functions
\+ See Quantifiers
\? See Quantifiers
\{ See Quantifiers
\} See Quantifiers
\| See Groups and Ranges
\( See Groups and Ranges
\) See Groups and Ranges
\w See Character Classes
Character Classes
\w
digits,letters and _
[:word:] digits,letters and _
[:upper:] Upper case letters_
[:lower:] Lower case letters_
[:alpha:] All letters
[:alnum:] Digits and letters
[:digit:] Digits
[:xdigit:] Hexidecimal digits
[:punct:] Puntuation
[:blank:] Space and tab
[:space:] Blank charaters
[:cntrl:] Control charaters
[:graph:] Printed characters
[:print:] Printed chars and spaces
Example expression to match an IP Address which is contained within a word boundary.
"\<[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\>"



Appendix F – The PIO Programming Package
The PIO Programming Package
Introduction to the PIO
The RP2040 has many built in peripherals like PWM, UART, ADC, SPI. In addition the RP2040 chip contains
two PIO blocks, rather like cut-down, highly specialised CPU cores. MMBasic refers to them as PIO0 and
PIO1 in line with the Raspberry Pi documentation. They are capable of running completely independently of
the main system and of each other. They can be used to create such things as very high accuracy serial data
interfaces and bit streams, although they are by no means restricted to this sort of thing. They can be made to
run extremely fast, with a throughput of up to 32 bits during every clock cycle.
Before a state machine can execute it's program, the program needs to be written to PIO memory, and the state
machine needs to be configured.
This appendix describes the support MMBasic can give in using PIO. It does not contain an explanation how to
write PIO state machine programs. For better understanding how the PIO state machines work look at
following thread "PIO explained PICOMITE" on the thebackshed.com forum:
https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=15385

Overview of PIO
A single PIO block has four independent state machines. All four state machines share a single 32 instruction
program area of flash memory. This memory has write-only access from the main system, but has four read
ports, one for each state machine, so that each can access it independently at its own speed. Each state machine
has its own program counter.
Each state machine also has two 32-bit "scratchpad" registers, X and Y, which can be used as temporary data
stores.
I/O pins are accessed via an input/output mapping module that can access 32 pins (but limited to 30 for the
RP2040). All state machines can access all the pins independently and simultaneously.
The system can write data into the input end of a 4-word 32-bit wide TX FIFO buffer. The state machine can
then use pull to move the output word of the FIFO into the OSR (Output Shift Register). It can also use out to
shift 1-32 bits at a time from the OSR into the output mapping module or other destinations. AUTOPULL can
be used to automatically pull data until the TX FIFO is empty or reaches a preset level.
The system can read data from the output end of a 4-word 32-bit wide RX FIFO buffer. The state machine can
then use in to shift 1-32 bits of data at a time from the input mapping module into the ISR (Input Shift
Register). It can also use push to move the contents of the ISR into the FIFO. AUTOPUSH can be used to
automatically push data until the RX FIFO is full or reaches a preset level.
The FIFO buffers can be reconfigured to form a single direction 8-word 32-bit FIFO in a single direction. The
buffers allow data to be passed to and from the state machines without either the system or the state machine
having to wait for the other.
Each of the four state machines in the PIO has four registers associated with it:
• CLKDIV is the clock divider, which has a 16-bit integer divider and an 8-bit fractional divider. This
sets how fast the state machine runs. It divides down from the main system clock.
• EXECCTRL holds information controlling the translation and execution of the program memory
• SHIFTCTRL controls the arrangement and usage of the shift registers
• PINCTRL controls which and how the GPIO pins are used.
The four state machines of a PIO have shared access to its block of 8 interrupt flags. Any state machine can use
any flag. They can set, reset or wait for them to change. In this way they can be made to run synchronously if
required. The lower four flags are also accessible to and from the main system, so the PIO can be controlled or
pass interrupts back.
DMA can be used to pass information to and from the PIO block via its FIFO from the RP2040's memory
A PIO has nine possible programming instructions, but there can be many variations on each one. For example,
Mov can have up to 8 sources, 8 destinations, 3 process operations during the copy, with optional delay and/or
side set operations!
• Jmp Jump to an absolute address in program memory if a condition is true (or instantly).
• Wait Stall operation of the state machine until a condition is true.
• In
Shift a number of bits from a source into the ISR.


• Out
Shift a number of bits out of the OSR to a destination.
• Push Push the contents of the ISR into the RX FIFO as a single 32-bit word.
• Pull
Load a 32-bit word from the TX FIFO into the OSR.
• Mov Copy date from a source to a destination.
• Irq
Set or clear an interrupt flag.
• Set
Immediately write data to a destination.
Instructions are all 16-bit and contain both the instruction and all data associated with it. All instructions
operate in 1 clock cycle, but it is possible to introduce a delay of several idle clock cycles between an
instruction and the next.
Additionally, there is a facility called "side-set" which allows a value to be written to some pre-defined output
pins while an instruction is being read from memory. This is transparent to the program.

Programming PIO
PicoMite programs the PIO statemachine memory using one of the following commands. Each option will be
explained with an example of the exact same program that toggles one of the GPIO lines of the PicoMite.
Which GPIO line is toggled, is determined in the configuration.

PIO ASSEMBLE
This command is used to use the build in assembler to generate the program from mnemonics, then write it
directly into PIO memory.
PIO ASSEMBLE 1,".program test"
PIO ASSEMBLE 1,".line 0"
PIO ASSEMBLE 1,"SET PINDIRS 1"
PIO ASSEMBLE 1,"label:"
PIO ASSEMBLE 1,"SET PIN 1"
PIO ASSEMBLE 1,"SET PIN 0"
PIO ASSEMBLE 1,"JMP label"
PIO ASSEMBLE 1,".end program list"

'a program has to have a name
'start the program at line 0
'SET the GPIO line to output
'define a label called "label"
'SET the GPIO pin high
'SET the GPIO pin low
'JuMP to "label" in an endless loop
'end program, list=show result

PIO PROGRAM LINE
This command can be used to program 16bit values to indidual lines in the PIO memory.
pio program line 1,0,&hE081
pio program line 1,1,&hE001
pio program line 1,2,&hE000
pio program line 1,3,&h0001

'SET pin output
'SET pin high
'SET pin low
'JMP to line 1

PIO PROGRAM
This command writes all 32 lines in one PIO from an array. This is useful once a PIO program is debugged. It
is extremely compact.
Dim a%(7)=(&h0001E0000E001E081,0,0,0,0,0,0,0)
PIO program 1,a%()

Configuring PIO
The PicoMite can configure each state machine individually. Configuration allows 2 state machines to run the
exact same program lines (e.g. an SPI interface) but operate with different GPIO pins and at different speeds.
There are several configuration fields.

FREQUENCY
PicoMite contains a default configuration for each configuration field, except for the frequency. The frequency
is set by a 16 bit divider from the ARM clock. Example: when OPTION CPUSPEED 126000 is set the PIO can
run at speeds between 126MHz and 1.922kHz (126000000 / 65536). Be aware that higher CPU speeds
(overclocking) directly impact the state machine frequency.

PIN CONTROL
PicoMite defaults the GPIO pins for use by MMBasic. For the PIO to take ownership of a GPIO pin MMBasic
needs to assign it to PIO as below.
SETPIN GPxx,PIOx
(e.g. SETPIN gp0,pio1)


A state machine can SET the state of a pin (SET is a state machine instruction), but can also output serial data
to one or more GPIO pins using the OUT instruction. Or read serial data using the IN instruction. And GPIO
pins can be set as a side effect of any state machine instruction (SIDE SET). For each method of interfacing,
different pins can be mapped to the state machine.
It is important to understand is that these instructions work on consecutive pins. This means that there is a range
of pins that can be controlled, starting at the lowest GPx pin number (e.g. GP0), and pins next to it can be
included (up to 5 pins in total). So GP0,GP1,GP2 is a valid set of IO pins. GP0,GP1,GP6 is not. Consider this
when designing a PIO application.
Assigning GPIO pins to a state machine uses the PIO helper function:
PIO(PINCTRL a,b,c,d,e,f,g)
a/ the number of SIDE SET pins (0...5), SIDE SET can write 5 pins at once
b/ the number of SET pins
(0...5), SET can write 5 pins at once
c/ the number of OUT pins
(0...31), OUT can write 32 pins at once
d/ the lowest pin for IN pins (GP0.....GP31) IN can read up to 32 pins at once
e/ the lowest pin for SIDE SET (GP0.....GP31)
f/ the lowest pin for SET
(GP0.....GP31)
g/ the lowest pin for OUT
(GP0.....GP31)

Ranges for the different functions can overlap, be identical, or adjacent.

EXECUTE CONTROL
The execute control register EXECCTRL configures the program flow. There is a field that connects a GPIO
pin to a conditional jump (JMP instruction), and fields that hold the line address of the main program loop
begin (.WRAP TARGET) and end (.WRAP).
If we want the program flow to change in response of a GPIO pin state, a JMP PIN is used. The JMP pin is
assigned in the execute control configuration (there can only be 1 pin per state machine) and the JMP happens
only when the pin is high).
The state machine program starts at the beginning and runs until it reaches the end. In above demo program, the
program loops from the end to beginning using a (unconditional) JMP instruction. An alternative way to using
the JMP instruction is defining the beginning of the loop (WRAP TARGET = line 1) and end of the loop
(WRAP = line 2) and configure the state machine to only execute these instructions in between. The JMP
instruction in line 3 is obsolete when WRAP/WRAP TARGET is used.
PIO(EXECCTRL a,b,c)
a/ the GPIO pin for conditional JMP (e.g. GP0)
b/ the WRAP TARGET line number
(e.g. 1)
c/ the WRAP line number
(e.g. 2)

SHIFT CONTROL
The IN and OUT instructions shift data from the FIFO register to the GPIO pins. In between MMBasic and the
PIO, 32bit words can be communicated. Since both the ARM cores and the PIO processors operate
independently, the data is exchanged through FIFO's. The ARM (MMBasic) puts data in the FIFO, PIO reads
it. This uses the TX FIFO. The other way around uses the RX FIFO. The FIFO's are normally 4 words deep but
can be configured to a single 8 word deep RX or TX FIFO.
The PIO can "shift" data IN the RX FIFO from the MSB side, or from the LSB side. That is set with the IN
SHIFTDIR bit. Similar the OUT SHIFTDIR bit for OUT data. The autopull and autopush flags in combination
with the pull and push thresholds determine when FIFO is replenished.
PIO(SHIFTCTRL a,b,c,d,e,f,g,h)
a/ push threshold
b/ pull threshold
c/ autopush
d/ autopull
e/ IN-shiftdir
f/ OUT-shiftdir
g/ fjoin_rx
h/ fjoin_tx


(leave 0 for now)
(leave 0 for now)
(leave 0 for now)
(leave 0 for now)
(1 = shift MSB, 0 = shift LSB)
(1 = shift MSB, 0 = shift LSB)
(join TX and RX fifo to 1 RX fifo)
(join TX and RX fifo to 1 TX fifo)


WRITING THE STATE MACHINE CONFIGURATION
A state machine configuration is written using the command:
PIO INIT MACHINE a,b,c,d,e,f,g
a/ the PIO
(0 or 1)
b/ the state machine number
(0...3)
c/ frequency
(CPUSPEED/65536...CPUSPEED in Hz)
d/ pincontrol value
(PIO(PINCTRL ......))
e/ execture control value
(PIO(EXECCTRL......))
f/ shiftcontrol value
(PIO(SHIFCTRL......))
g/ start address
(0....31, the line at which the state machine starts executing)

STARTING AND STOPPING A STATE MACHINES
Once the PIO is configured, you can start and stop the state machine using:
PIO START a,b
PIO STOP a,b
a/ the PIO number
b/ the state machine

(0 or 1)
(0...3)

Note that when stopping a state machine, it stops right where it is. To restart the state machine it is advisable to
PIO INIT MACHINE first.

EXAMPLE PROGRAM 1
A complete PIO implementation that toggles a GPIO pins can be implemented in MMBasic as shown below.
Connect a buzzer to GP0, and hear the audio tone generated by the PIO.
'disconnect ARM from GP0
setpin gp0,pio1

'use GP0 as output pin for PIO 1

'pio program used
'0 E081
'SET pin output
'1 E001
'SET pin high
'2 E000
'SET pin low
'3 0001
'jmp 1
'program pio 1 using an array to write the program in PIO memory, and start
Dim a%(7)=(&h0001E000E001E081,0,0,0,0,0,0,0)
PIO program 1,a%()
'configure pio 1 statemachine 0
p=Pio(pinctrl 0,1,,,,gp0,)
f=2029
133000
PIO init machine 1,0,f,p
address(=0)

'define SET uses 1 pin, and that is GP0
'2029 Hz is lowest frequency for CPUSPEED
'use default for execctrl, shiftctrl, start

'start the PIO 1 state machine 0
PIO start 1,0

Note that the MMBasic program ends, but the sound on the buzzer continues. PIO is independent of the ARM
processor, and continues until it is stopped. Entering the MMBasic editor stops the PIO.

FIFO's
MMBasic and the PIO exchange information using FIFO's. The PIO's PUSH data into the RX FIFO (MMBasic
is the receiver), or PULL data from the TX FIFO (MMBasic is the transmitter).
When PIO is fetching data from the FIFO the data is transferred to the OSR (Output Shift Register), from there
is can be processed. The PIO can push the data from the ISR (Input shift register) into the FIFO. Additionally,
the PIO has 2 registers X and Y that can be used for storage, or counting. PIO cannot add or subtract or
compare.
Data flow:
MMBasic -> FIFO -> OSR -> PIO (or pins)
PIO (or pins) -> ISR -> FIFO -> MMBasic
MMBasic can write data into the TX FIFO and read data from the RX FIFO using:


PIO READ a,b,c,d
PIO WRITE a,b,c,d
a/ PIO number
(0 or 1)
b/ state machine number
(0...3)
c/ number of 32 bit words
(1...4)
d/ integer variable name (i.e. variable% or array%())

PIO CLEAR clears all the PIO FIFO's, as does PIO START and PIO INIT MACHINE.
The MMBAsic program doesn't need to wait for data in the FIFO to appear since the RX FIFO can be assigned
an interrupt. The MMBasic interrupt routine can fetch the data from the FIFO.
Similar for TX interrupt in which case MMBasic gets an interrupt when data is needed for the TX FIFO.
PIO INTERRUPT a,b,c,d
a/ PIO
(0 or 1)
b/ state machine
(0...3)
c/ Name of RX interrupt handler (i.e. "myRX_Interrupt" or 0 to disable)
d/ Name of TX interrupt handler (i.e. "myTX_Interrupt" or 0 to disable)

EXAMPLE PROGRAM 2
Below program explains many of the above presented MMbasic functions and commands. The program reads a
NES controller (SPI) connected to the PicoMite. The NES controller consists of a HEF4021 shift register
connected to 8 push button switches.
Program uses: wrap and wrap target, IN, side set and delay, PUSH, PIO READ. GP0 and GP1 are in SET for
pin direction, and in side set for compact code.
The wiring is as defined in the code:
'disconnect ARM from GP0/1/2
setpin gp0,pio1
setpin gp1,pio1
setpin gp2,pio1

'clock out
'load out
'data in

'PIO program
PIO assemble 1,".program NES"
PIO assemble 1,".side_set 2"
PIO assemble 1,".line 0"
PIO assemble 1,"SET pindirs,&b11"
PIO assemble 1,".wrap target"
PIO assemble 1,"IN null,32 side 2"
PIO assemble 1,"SET X,7 side 0"
PIO assemble 1,"loop:"
PIO assemble 1,"IN pins,1 side 0"
PIO assemble 1,"JMP X-- loop side 1"
PIO assemble 1,"PUSH side 0 [7]"
PIO assemble 1,".wrap"
PIO assemble 1,".end program list"

'a program needs a name
'use 2 bits for side set, 3 for delay
'start code at line 0
'set GP0,GP1 output, side GP0,GP1 low
'wrap target = top of the loop
'set ISR to 0, GP1 high (load), GP0 low
'set X counter to 7, GP0,GP1 low
'inner loop label
'shift 1 databit in, keep GP0,GP1 low
'jmp to loop, dec. X, GP0 high(clock)
'now X=0, PUSH result into FIFO, delay 7
'end outer loop, repeat
'end of program, list result

'configure pio1
p=Pio(pinctrl 2,2,,gp2,gp0,gp0,)
'GP0,GP1 out (SET and SIDE SET), GP2
IN
f=1e5
'100kHz
s=PIO(shiftctrl 0,0,0,0,0,0)
'shift in from LSB for IN (and OUT)
e=PIO(execctrl gp0,PIO(.wrap target),PIO(.wrap)
'wrap and wrap target
'write the configuration
PIO init machine 1,0,f,p,e,s,0
'start the pio1 code
PIO start 1,0

'Check the the read data in MMBasic and print
dim d%
do
pio read 1,0,1,d%
print bin$(d%)



pause 200
loop
END

DMA To and From the FIFOS
The way that DMA works is as follows:
When reading from the FIFO the DMA controller waits on data being in the FIFO and when it appears transfers
that data into processor memory. Each time it reads it increments the pointer into the processor memory so that
it can, for example, incrementally fill an array as each and every data item is made available.
When writing to the FIFO the DMA controller writes data from processor memory to the FIFO automatically
waiting whenever the FIFO is full. Thus, data can be prepared in an array and the DMA controller will stream
that data to the PIO FIFO as fast as the PIO program requires it.
DMA can transfer a 32-bit word, a 16-bit short, or an 8-bit byte and when setting up DMA you need to tell it
the size of the tranfer and how many transfers to make. Because each transfer will increment the memory
pointer by 1,2, or 4 bytes MMBasic must deal with the data packed into memory rather than the 64-bits used for
MMbasic integers and floats. Luckily MMBasic implements two commands MEMORY PACK and MEMORY
UNPACK to do this very efficiently but it could equally be done using standard BASIC arithmetic.
The DMA can be configured to repeatedly loop data into or out of a section of memory (a ring buffer)
The commands are:
PIO DMA_IN a,b,c,d,e,f,g
PIO DMA_OUT a,b,c,d,e,f,g
a/ pio
b/ state machine
c/ nbr
d/ data%()
e/ completioninterrupt
f/ transfersize
g/ loopbackcount

(0 or 1)
(0...3)
(number of words to be transferred)
(interger array name)
(where to go when done, optional)
(8/16/32, optional)
(used data%() as a ring buffer, optional, loopbackcount = 2^n)

The DMA will start the state machine automatically and there is no need for a PIO START command. But,
before starting the transfer make sure a fresh PIO INIT MACHINE is done, so the state machine starts at the
required start address.
When a ring buffer is used, it requires special preparation:
PIO MAKE RING BUFFER a,b
a/ name of integer buffer
b/ size of the array in bytes

Example :
DIM packed%
PIO MAKE RING BUFFER packed%,4096

packed% will then be an integer array holding 4096/8=512 integers
This can then be used by the DMA for a loopbackcounter with DMA of 1024 32-bit words, 2048 16-bit shorts
or 4096 8-bit bytes

EXAMPLE PROGRAM 3
This program brings everything together and uses DMA to read 128 samples from the PIO RX FIFO. For the
demonstration, GP0 to GP5 are outputs of 3 PWMS, and are ,at the same time, sampled by the PIO as a 6
channel logic analyser or oscilloscope. The 128 samples are sent to the serial port as waveforms.
This program also demonstrates PIO DMA RX, MEMORY UNPACK, the use of buffers.
'generate a 50Hz 3 phase test signal to demonstrate the DMA on 6 GPIO pins.
SetPin gp0,pwm 'CH 0a
SetPin gp1,pwm 'CH 0b
SetPin gp2,pwm 'CH 1a
SetPin gp3,pwm 'CH 1b
SetPin gp4,pwm 'CH 2a
SetPin gp5,pwm 'CH 2b
Fpwm = 50: PW = 100 / 3
PWM 0, Fpwm, PW, PW - 100, 1, 1
PWM 1, Fpwm, PW, PW - 100, 1, 1



PWM 2, Fpwm, PW, PW - 100, 1, 1
PWM sync 0, 100/3, 200/3
'----------------------------------- LA code PIO -------------------------'PIO code to sample GP0..GP6 as elementary logic analyser
PIO clear 1
'in this program the PIO reads GP0..GP5 brute force
'and pushes data into FIFO. The clock speed determines the
'sampling rate. There are 2 instructions per cycle
'taking 10000/2 / 50 = 100 samples per 50Hz cycle.
PIO assemble 1,".program push"
PIO assemble 1,".line 0"
PIO assemble 1,".wrap target"
PIO assemble 1,"IN pins,6"
PIO assemble 1,"PUSH block"

‘'get 6 bits from GPIO pins (GP0..GP5)
'only push data when FIFO has room

PIO assemble 1,".wrap"
PIO assemble 1,".end program list"
'configuration
f=1e4
'PIO run at 10kHz
p=Pio(pinctrl 0,0,0,gp0,,,)
'IN base = GP0
e=Pio(execctrl gp0,PIO(.wrap target),PIO(.wrap)) 'wrap 1 to 0, gp0 is default
s=Pio(shiftctrl 0,0,0,0,0,0)
'shift in through LSB, out is not used
'write the configuration, running 10kHz (data in FIFO 10us after edge GP0)
PIO init machine 1,0,f,p,e,s,0
'start address = 0
'---------------------------- LA code MMBasic -------------------------------'define memory buffers
Dim a$(1)=("_","-")
'characters for the printout
length%=64
'size of the packed array
Dim data%(2*length%-1)
'array to put the 32 bit samples FIFO
format
Dim packed%(length%-1)
'DMA array to pack 32 bit samples in 64
bit integers
'let the DMA machine run, and repeat at will
Do
PIO DMA RX 1,0,2*length%,packed%(),ReadyInt
print "press any key to restart sampling"
do:loop while inkey$=""
Loop
End
'-----------------------------------SUBS MMBasic ----------------------------Sub ReadyInt
'stop the PIO and re-init for next run
PIO stop 1,0
PIO init machine 1,0,f,p,e,s,0
'start address = 0
'get the data from the packed DMA buffer and unpack to original 32 bit format
Memory unpack packed%(),data%(),2*length%,32
'Serial output as if logic analyzer traces
For j=0 To 5
mask%=2^j
For i=0 To 2*length%-1
If i<106 Then Print a$(((data%(i) And mask%)=mask%));
Next i
Print : Print
Next j
End Sub



Appendix G – Programming in BASIC - A Tutorial
Programming in BASIC - A Tutorial
The PicoMite is programmed using the BASIC programming language. The PicoMite version of
BASIC is called MMBasic which loosely emulates the Microsoft BASIC interpreter that was popular
years ago.
The BASIC language was introduced in 1964 by Dartmouth College in the USA as a computer
language for teaching programming and accordingly it is easy to use and learn. At the same time, it
has proved to be a competent and powerful programming language and as a result it became very
popular in the late 70s and early 80s. Even today some large commercial data systems are still written
in the BASIC language (primarily Pick Basic).
For the PicoMite the greatest advantage of BASIC is its ease of use. Some more modern languages
such as C and C++ can be truly mind bending but with BASIC you can start with a one line program
and get something sensible out of it. MMBasic is also powerful in that you can draw sophisticated
graphics, manipulate the external I/O pins to control other devices and communicate with other
devices using a range of built-in communications protocols.
Command Prompt
Interaction with MMBasic is done via the console at the command prompt (ie, the greater than symbol
(>) on the console). On startup MMBasic will issue the command prompt and wait for some
command to be entered. It will also return to the command prompt if your program ends or if it
generated an error message.
When the command prompt is displayed you have a wide range of commands that you can enter and
execute. Typically they would list the program held in memory (LIST) or edit it (EDIT) or perhaps
set some options (the OPTION command). Most times the command is just RUN which instructs
MMBasic to run the program held in program memory.
Almost any command can be entered at the command prompt and this is often used to test a command
to see how it works. A simple example is the PRINT command (more on this later), which you can
test by entering the following at the command prompt:
PRINT 2 + 2
and not surprisingly MMBasic will print out the number 4 before returning to the command prompt.
This ability to test a command at the command prompt is useful when you are learning to program in
BASIC, so it would be worthwhile having the PicoMite handy for the occasional test while you are
working through this tutorial.
Structure of a BASIC Program
A BASIC program starts at the first line and continues until it runs off the end or hits an END
command - at which point MMBasic will display the command prompt (>) on the console and wait for
something to be entered.
A program consists of a number of statements or commands, each of which will cause the BASIC
interpreter to do something (the words statement and command generally mean the same and are used
interchangeable in this tutorial).
Normally each statement is on its own line but you can have multiple statements in the one line
separated by the colon character (:).
For example;
A = 24.6 : PRINT A



Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters
however modern implementations (such as MMBasic) do not need them. You can still use them if
you wish but they have no benefit and generally just clutter up your programs.
This is an example of a program that uses line numbers:
50 A = 24.6
60 PRINT A
A line can also start with a label which can be used as the target for a program jump using the GOTO
command. This will be explained in more detail when we cover the GOTO command but this is an
example (the label name is JmpBack):
JmpBack: A = A + 1
PRINT A
GOTO JmpBack
Comments
A comment is any text that follows the single quote character ('). A comment can be placed anywhere
and extends to the end of the line. If MMBasic runs into a comment it will just skip to the end of it
(ie, it does not take any action regarding a comment).
Comments should be used to explain non obvious parts of the program and generally inform someone
who is not familiar with the program how it works and what it is trying to do. Remember that after
only a few months a program that you have written will have faded from your mind and will look
strange when you pick it up again. For this reason you will thank yourself later if you use plenty of
comments.
The following are some examples of comments:
' calculate the hypotenuse
PRINT SQR(a * a + b * b)
or
INPUT var

' get the temperature

Older BASIC programs used the command REM to start a comment and you can also use that if you
wish but the single quote character is easier to use and more convenient.
The PRINT Command
There are a number of common commands that are fundamental and we will cover them in this
tutorial but arguably the most useful is the PRINT command. Its job is simple; to print something on
the console. This is mostly used to output data for you to see (like the result of calculations) or
provide informative messages.
PRINT is also useful when you are tracing a fault in your program; you can use it to print out the
values of variables and display messages at key stages in the execution of the program.
In its simplest form the command will just print whatever is on its command line. So, for example:
PRINT 54
will display on the console the number 54 followed by a new line.
The data to be printed can be something simple like this or an expression, which means something to
be calculated. We will cover expressions in more detail later but as an example the following:
> PRINT 3/21
0.1428571429
>
would calculate the result of three divided by twenty one and display it. Note that the greater than
symbol (>) is the command prompt produced by MMBasic – you do not type that in.


Other examples of the PRINT command include:
> PRINT "Wonderful World"
Wonderful World
> PRINT (999 + 1) / 5
200
>
You can try these out at the command prompt.
The PRINT command will also work with multiple values at the same time, for example:
> PRINT "The amount is" 345 " and the second amount is" 456
The amount is 345 and the second amount is 456
>
Normally each value is separated by a space character as shown in the previous example but you can
also separate values with a comma (,). The comma will cause a tab to be inserted between the two
values. In MMBasic tabs in the PRINT command are eight characters apart.
To illustrate tabbing, the following command prints a tabbed list of numbers:
> PRINT 12, 34, 9.4, 1000
12
34
9.4
1000
>
Note that there is a space printed before each number. This space is a place holder for the minus
symbol (-) in case the value is negative. You can see the difference with the number 12 in this
example:
> PRINT -12, 34, -9.4, 1000
-12
34
-9.4
1000
>
The print statement can be terminated with a semicolon (;). This will prevent the PRINT command
from moving to a new line when it has printed all the text. For example:
PRINT "This will be";
PRINT " printed on a single line."
Will result in this output:
This will be printed on a single line.
The message would be look like this without the semicolon at the end of the first line:
This will be
printed on a single line.
Variables
Before we go much further we need to define what a "variable" is as they are fundamental to the
operation of the BASIC language (in fact, most programming languages). A variable is simply a
place to store an item of data (ie, its "value"). This value can be changed as the program runs which
why it is called a "variable".
Variables in MMBasic can be one of three types. The most common is floating point and this is
automatically assumed if the type of the variable is not specified. The other two types are integer and
string and we will cover them later. A floating point number is an ordinary number which can contain
a decimal point. For example 3.45 or -0.023 or 100.00 are all floating point numbers.
A variable can be used to store a number and it can then be used in the same manner as the number
itself, in which case it will represent the value of the last number assigned to it.



As a simple example:
A = 3
B = 4
PRINT A + B
will display the number 7. In this case both A and B are variables and MMBasic used their current
values in the PRINT statement. MMBasic will automatically create a variable when it first encounters
it so the statement A = 3 both created a floating point variable (the default type) with the name of A
and then it assigned the value of 3 to it.
The name of a variable must start with a letter while the remainder of the name can use letters,
numbers, the underscore or the full stop (or period) characters. The name can be up to 31 characters
long and the case (ie, capitals or not) is not important. Here are some examples:
Total_Count
ForeColour
temp3
count
x
ThisIsALongVariableName
increment.value
You can change the value of a variable anywhere in your program by using the assignment command,
ie:
variable = expression
For example:
temp3 = 24.6
count = 5
CTemp = (FTemp – 32) * 0.5556
In the last example both CTemp and FTemp are variables and this line converts the value of FTemp
(in degrees Fahrenheit) to degrees Celsius and stores the result in the variable CTemp.
Expressions
We have met the term ‘expression’ before in this tutorial and in programming it has a specific
meaning. It is a formula which can be resolved by the BASIC interpreter to a single number or value.
MMBasic will evaluate numeric expressions using the same rules that we learnt at school. For
example, multiplication and division are performed first followed by addition and subtraction. These
are called the rules of precedence and are fully spelt out in this manual.
This means that MMBasic will resolve 2 + 3 * 6 by first multiplying 3 by 6 giving 18 then adding 2
resulting in a final value of 20. Similarly, both 5 * 4 and 10 + 4 * 3 – 2 will also resolve to 20.
If you want to force the interpreter to evaluate parts of the expression first you can surround that part
of the expression with brackets. For example, (10 + 4) * (3 – 2) will resolve to 14 not 20 as would
have been the case if the brackets were not used. Using brackets does not appreciably slow down the
program so you should use them liberally if there is a chance that MMBasic will misinterpret your
intention.
As pointed out earlier, you can use variables in an expression exactly the same as straight numbers.
For example, this will increment the value of the variable temp by one:
temp = temp + 1
You can also use functions in expressions. These are special operations provided by MMBasic, for
example to calculate trigonometric values.



As an example, the following will print the length of the hypotenuse of a right angled triangle using
the SQR() function which returns the square root of a number (a and b are variables holding the
lengths of the other sides):
PRINT SQR(a * a + b * b)
MMBasic will first evaluate this expression by multiplying a by a, then multiplying b by b, then
adding the results together. The resulting number is then passed to the SQR() function which will
calculate the square root of that number (ie, the hypotenuse) and return it for the PRINT command to
display.
Some other mathematical functions provided by MMBasic include:
SIN(r) – the sine of r
COS(r) – the cosine of r
TAN(r) – the tangent of r
There are many more functions available to you and they are all listed earlier in this manual.
Note that in the above trigonometric functions the value passed to the function (ie, 'r') is the angle in
radians. In MMBasic you can use the function RAD(d) to convert an angle from degrees to radians
('d' is the angle in degrees).
Another feature of most programming languages including BASIC is that you can nest function calls
within each other. For example, given the angle in degrees (ie, 'd') the sine of that angle can be found
with this expression:
PRINT SIN(RAD(d))
In this case MMBasic will first take the value of d and convert it to radians using the RAD() function.
The output of this function then becomes the input to the SIN() function.
The IF Statement
Making decisions is at the core of most computer programs and in BASIC this is usually done with
the IF statement. This is written almost like an English sentence:
IF condition THEN action
The condition is usually a comparison such as equals, less than, more than, etc.
For example:
IF Temp < 25 THEN PRINT "Cold"
Temp would be a variable holding the current temperature (in ºC) and PRINT "Cold" the action to
be done.
There are a range of tests that you can make:
=
<
>

equals
less than
greater than

<>
<=
>=

not equal
less than or equals
greater than or equals

You can also add an ELSE clause which will be executed if the initial condition tested false:
IF condition THEN true-action ELSE false-action
For example, this will execute different actions when the temperature is under 25 or 25 or more:
IF Temp < 25 THEN PRINT "Cold" ELSE PRINT "Hot"
The previous examples all used single line IF statements but you can also have multiline IF
statements.



They look like this:
IF condition THEN
true-action
true-action
ENDIF
or
IF condition THEN
true-action
true-action
ELSE
false-action
false-action
ENDIF
Unlike the single line IF statement you can have many true actions with each on their own line and
similarly many false actions. Generally the single line IF statement is handy if you have a simple
action that needs to be taken while the multiline version is much easier to understand if the actions are
numerous and more complicated.
An example of a multiline IF statement with more than one action is:
IF Amount < 100 THEN
PRINT "Too low"
PRINT “Minimum value is 100”
ELSE
PRINT "Input accepted"
SaveToSDCard
PRINT "Enter second amount"
ENDIF
Note that in the above example each action is indented to show what part of the IF structure it belongs
to. Indenting is not mandatory but it makes a program much easier to understand for someone who is
not familiar with it and therefore it is highly recommended.
In a multiline IF statement you can make additional tests using the ELSE IF command. This is best
explained by using an example (the temperatures are all in ºC):
IF Temp < 0 THEN
PRINT “Freezing”
ELSE IF Temp < 20 THEN
PRINT “Cold”
ELSE IF Temp < 35 THEN
PRINT “Warm”
ELSE
PRINT “Hot”
ENDIF
The ELSE IF can use the same tests as an ordinary IF (ie, <, <=, etc) but that test will only be made if
the preceding test was false. So, for example, you will only get the message Warm if Temp < 0
failed, and Temp < 20 failed but Temp < 35 was true. The final ELSE will catch the case where
all the tests were false.
An expression like Temp < 20 is evaluated by MMBasic as either true or false with true having a
value of one and false zero. You can see this if you entered the following at the console:
PRINT 30 > 20
MMBasic will print 1 meaning that the value of the expression is true.



Similarly the following will print 0 meaning that the expression evaluated to false.
PRINT 30 < 20
The IF statement does not really care about what the condition actually is, it just evaluates the
condition and if the result is zero it will take that as false and if non zero it will take it as true. This
allows for some handy shortcuts. For example, if BalanceCorrect is a variable that is true (non
zero) when some feature of the program is correct then the following can be used to make a decision
based on that value:
IF BalanceCorrect THEN …do something…
FOR Loops
Another common requirement in programming is repeating a set of actions. For instance, you might
want to step through all seven days in the week and perform the same function for each day. BASIC
provides the FOR loop construct for this type of job and it works like this:
FOR day = 1 TO 7
Do something based on the value of ‘day’
NEXT day
This starts by creating the variable day and assigning the value of 1 to it. The program will then
execute the following statements until it comes to the NEXT statement. This tells the BASIC
interpreter to increment the value of day, go back to the previous FOR statement and re-execute the
following statements a second time. This will continue looping around until the value of day exceeds
7 and the program will then exit the loop and continue with the statements following the NEXT
statement.
As a simple example, you can print the numbers from one to ten like this:
FOR nbr = 1 TO 10
PRINT nbr,;
NEXT nbr
The comma at the end of the PRINT statement tells the interpreter to tab to the next tab column after
printing the number and the semicolon will leave the cursor on this line rather than automatically
moving to the next line. As a result, the numbers will be printed in neat columns across the page.
This is what you would see:
1

2

3

4

5

6

7

8

9

10

The FOR loop also has a couple of extra tricks up it sleeves. You can change the amount that the
variable is incremented by using the STEP keyword. So, for example, the following will print just the
odd numbers:
FOR nbr = 1 TO 10 STEP 2
PRINT nbr,;
NEXT nbr
The value of the step (or increment value) defaults to one if the STEP keyword is not used but you can
set it to whatever number you want.
When MMBasic is incrementing the variable it will check to see if the variable has exceeded the TO
value and, if it has, it will exit from the loop. So, in the above example, the value of nbr will reach
nine and it will be printed but on the next loop nbr will be eleven and at that point execution will
leave the loop. This test is also applied at the start of the loop (ie, if in the beginning the value of the
variable exceeds the TO value (and STEP is positive) the loop will never be executed, not even once).
By setting the STEP value to a negative number you can use the FOR loop to step down from a high
number to low. In that case the starting number must be greater than the TO number.



For example, the following will print the numbers from 1 to 10 in reverse:
FOR nbr = 10 TO 1 STEP -1
PRINT nbr,;
NEXT nbr
Multiplication Table
To further illustrate how loops work and how useful they can be, the following short program will use
two FOR loops to print out the multiplication table that we all learnt at school. The program for this is
not complicated:
FOR nbr1 = 1 to 10
FOR nbr2 = 1 to 10
PRINT nbr1 * nbr2,;
NEXT nbr2
PRINT
NEXT nbr1

The output is shown in the following screen grab, which also shows a listing of the program.

You need to work through the logic of this example line by line to understand what it is doing.
Essentially it consists of one loop inside another. The inner loop, which increments the variable
nbr2 prints one horizontal line of the table. When this loop has finished it will execute the following
PRINT command which has nothing to print - so it will simply output a new line (ie, terminate the
line printed by the inner loop).
The program will then execute another iteration of the outer loop by incrementing nbr1 and
re-executing the inner loop again. Finally, when the outer loop is exhausted (when nbr1 exceeds 10)
the program will reach the end and terminate.
One last point, you can omit the variable name from the NEXT statement and MMBasic will guess
which variable you are referring to. However, it is good practice to include the name to make it easier
for someone else who is reading the program to understand it. You can also terminate multiple loops
using a comma separated list of variables in the NEXT statement. For example:
FOR var1 = 1 TO 5
FOR var2 = 10 to 13
PRINT var1 * var2
NEXT var1, var2



DO Loops
Another method of looping is the DO…LOOP structure which looks like this:
DO WHILE condition
statement
statement
LOOP
This will start by testing the condition and if it is true the statements will be executed until the LOOP
command is reached, at which point the condition will be tested again and if it is still true the loop will
execute again. The ‘condition’ is the same as in the IF command (ie, X < Y).
For example, the following will keep printing the word "Hello" on the console for 4 seconds then stop:
Timer = 0
DO WHILE Timer < 4000
PRINT "Hello"
LOOP
Note that Timer is a function within MMBasic which will return the time in milliseconds since the
timer was reset. A reset is done by assigning zero to Timer (as done above) or when powering up
the PicoMite .
A variation on the DO-LOOP structure is the following:
DO
statement
statement
LOOP UNTIL condition
In this arrangement the loop is first executed once, the condition is then tested and if the condition is
false, the loop will be repeatedly executed until the condition becomes true. Note that the test in
LOOP UNTIL is the inverse of DO WHILE.
For example, similar to the previous example, the following will also print "Hello" for four seconds:
Timer = 0
DO
PRINT "Hello"
LOOP UNTIL Timer >= 4000
Both forms of the DO-LOOP essentially do the same thing, so you can use whatever structure fits
with the logic that you wish to implement.
Finally, it is possible to have a DO Loop that has no conditions at all - ie,
DO
statement
statement
LOOP
This construct will continue looping forever and you, as the programmer, will need to provide a way
to explicitly exit the loop (the EXIT DO command will do this). For example:
Timer = 0
DO
PRINT "Hello"
IF Timer >= 4000 THEN EXIT DO
LOOP



Console Input
As well as printing data for the user to see your programs will also want to get input from the user.
For that to work you need to capture keystrokes from the console and this can be done with the
INPUT command. In its simplest form the command is:
INPUT var
This command will print a question mark on the console's screen and wait for a number to be entered
followed by the Enter key. That number will then be assigned to the variable var.
For example, the following program extends the expression for finding the hypotenuse of a triangle by
allowing the user to enter the lengths of the other sides from the console.
PRINT "Length of side 1"
INPUT a
PRINT "Length of side 2"
INPUT b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
This is a screen capture of a typical session:

The INPUT command can also print your prompt for you, so that you do not need a separate PRINT
command. For example, this will work the same as the above program:
INPUT "Length of side 1"; a
INPUT "Length of side 2"; b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
Finally, the INPUT command will allow you to input a series of numbers separated by commas with
each number being saved in different variables.
For example:
INPUT "Enter the length of the two sides: ", a, b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
If the user entered 12,15 the number 12 would be saved in the variable a and 15 in b.
Another method of getting input from the console is the LINE INPUT command. This will get the
whole line as typed by the user and allocate it to a string variable. Like the INPUT command you can
also specify a prompt. This is a simple example:
LINE INPUT "What is your name? ", s$
PRINT "Hello " s$
We will cover string variables later in this tutorial but for the moment you can think of them as a
variable that holds a sequence of characters. If you ran the above program and typed in John when
prompted the program would respond with Hello John.


Sometimes you do not want to wait for the user to hit the enter key, you want to get each character as
it is typed in. This can be done with the INKEY$ function which will return the value of the character
as a string consisting of just one character or an empty string (ie, contains no characters) if nothing has
been entered.
GOTO and Labels
One method of controlling the flow of the program is the GOTO command. This essentially tells
MMBasic to jump to another part of the program and continue executing from there. The target of the
GOTO is a label and this needs to be explained first.
A label is an identifier that marks part of the program. It must be the first thing on the line and it must
be terminated with the colon (:) character. The name that you use can be up to 31 characters long and
must follow the same rules as for a variable's name. For example, in the following program line
LoopBack is a label:
LoopBack:

a = a + 1

When you use the GOTO command to jump to that particular part of the program you would use the
command like this:
GOTO LoopBack
To put all this into context the following program will print out all the numbers from 1 to 10:
z = 0
LoopBack: z = z + 1
PRINT z
IF z < 10 THEN GOTO LoopBack
The program starts by setting the variable z to zero then incrementing it to 1 in the next line. The
value of z is printed and then tested to see if it is less than 10. If it is less than 10 the program
execution will jump back to the label LoopBack where the process will repeat. Eventually the value
of z will be more than 10 and the program will run off the end and terminate.
Note that a FOR loop can do the same thing (and is simpler) so this example is purely designed to
illustrate what the GOTO command can do.
In the past the GOTO command gained a bad reputation. This is because using GOTOs it is possible
to create a program that continuously jumps from one point to another (often referred to as "spaghetti
code") and that type of program is almost impossible for another programmer to understand. With
constructs like the multiline IF statements the need for the GOTO statement has been reduced and it
should be used only when there is no other way of changing the program's flow.
Testing for Prime Numbers
The following is a simple program which brings together many of the programming features
previously discussed.
DO
InpErr:
PRINT
INPUT "Enter a number: "; a
IF a < 2 THEN
PRINT "Number must be equal or greater than 2"
GOTO InpErr
ENDIF
Divs = 0
FOR x = 2 TO SQR(a)
r = a/x


IF r = FIX(r) THEN Divs = Divs + 1
NEXT x
PRINT a " is ";
IF Divs > 0 THEN PRINT "not ";
PRINT "a prime number."
LOOP

This will first prompt (on the console) for a number and, when it has been entered, it will test if that
number is a prime number or not and display a suitable message.
It starts with a DO Loop that does not have a condition – so it will continue looping forever. This is
what we want. It means that when the user has entered a number, it will report if it is a prime number
or not and then loop around and ask for another number. The way that the user can exit the program
(if they wanted to) is by typing the break character (normally CTRL-C).
The program then prints a prompt for the user which is terminated with a semicolon character. This
means that the cursor is left at the end of the prompt for the INPUT command which will get the
number and store it in the variable a.
Following this the number is tested. If it is less than 2 an error message will be printed and the
program will jump backwards and ask for the number again.
We are now ready to test if the number is a prime number. The program uses a FOR loop to step
through the possible divisors testing if each one can divide evenly into the entered number. Each time
it does the program will increment the variable Divs.
Note that the test is done with the function FIX(r) which simply strips off any digits after the decimal
point. So, the condition r = FIX(r) will be true if r is an integer (ie, has no digits after the
decimal point).
Finally, the program will construct the message for the user. The key part is that if the variable Divs
is greater than zero it means that one or more numbers were found that could divide evenly into the
test number. In that case the IF statement inserts the word "not" into the output message.
For example, if the entered number was 21 the user will see this response:
21 is not a prime number.
This is the result of running the program and some of the output:

You can test this program by using the editor (the EDIT command) to enter it.


Using your newly learnt skills you could then have a shot at making it more efficient. For example,
because the program counts how many times a number can be divided into the test number it takes a
lot longer than it should to detect a non prime number. The program would run much more efficiently
if it jumped out of the FOR loop at the first number that divided evenly. You could use the GOTO
command to do this or you could use the command EXIT FOR – that would cause the FOR loop to
terminate immediately.
Other efficiencies include only testing the division with odd numbers (by using an initial test for an
even number then starting the FOR loop at 3 and using STEP 2) or by only using prime numbers for
the test (that would be much more complicated).
Arrays
Arrays are something which you will probably not think of as
useful at first glance but when you do need to use them you will
find them very handy indeed.
An array is best thought of as a row of letterboxes for a block of
units or condos as shown on the right. The letterboxes are all
located at the same address and each box represents a unit or
condo at that address. You can place a letter in the box for unit
one, or unit two, etc.
Similarly an array in BASIC is a single variable with multiple
sub units (called elements in BASIC) which are numbered. You
can place data in element one, or element two, etc. In BASIC an
array is created by the DIM command, for example:
DIM numarr(300)
This creates an array with the name of numarr containing 301 elements (think of them as
letterboxes) ranging from 0 to 300. By default an array will start from zero so this is why there is an
extra element making the total 301. To specify a specific element in the array (ie, a specific letterbox)
you use an index which is simply the number of the array element that you wish to access. For
example, if you want to set element number 100 in this array to (say) the number 876, you would do it
this way:
numarr(100) = 876
Normally the index to an array is not a constant number as in this example (ie, 100) but a variable
which can be changed to access different array elements.
As an example of how you might use an array, consider the case where you would like to record the
maximum temperature for each day of the year and, at the end of the year, calculate the overall
average. You could use ordinary variables to record the temperature for each day but you would need
365 of them and that would make your program unwieldy indeed. Instead, you could define an array
to hold the values like this:
DIM days(365)
Every day you would need to save the temperature in the correct location in the array. If the number of
the day in the year was held in the variable doy and the maximum temperature was held in the
variable maxtemp you would save the reading like this:
days(doy) = maxtemp
At the end of the year it would be simple to calculate the average for the year:
total = 0
FOR i = 1 to 365
total = total + days(i)
NEXT i
PRINT "Average is:" total / 365


This is much easier than adding up and averaging 365 individual variables.
The above array was single dimensioned but you can have multiple
dimensions. Reverting to our analogy of letterboxes, an array with
two dimensions could be thought of as a block of flats with multiple
floors. A block could have a row of four letter boxes for level one,
another row of four boxes for level two, and so on. To place a letter
in a letterbox you need to specify the floor number and the unit
number on that floor.
In BASIC such an array is specified using two indices separated by a
comma. For example:
LetterBox(floor, unit)
As a practical example, assume that you needed to record the maximum temperature for each day over
five years. To do this you could dimension the array as follows:
DIM days(365, 5)
The first index is the day in the year and the second is a number representing the year. If you wanted
to set day 100 in year 3 to 24 degrees you would do it like this:
days(100, 3) = 24
In MMBasic for the PicoMite you can have up to five dimensions (this is different from some other
versions of MMBasic which support eight dimensions). The maximum size of an array is only limited
by the amount of free RAM that is available.
Integers
So far all the numbers and variables that we have been using have been floating point. As explained
before, floating point is handy because it will track digits after the decimal point and when you use
division it will return a sensible result. So, if you just want to get things done and are not concerned
with the details you should stick to floating point.
However, the limitation of floating point is that it stores numbers as an approximation with an
accuracy of 14 digits on the PicoMite . Most times this characteristic of floating point numbers is not
a problem but there are some cases where you need to accurately store larger numbers.
As an example, let us say that you want to manipulate time accurately down to the microsecond so
that you can compare two different date/times to work out which one is earlier. The easy way to do
this is to convert the date/time to the number of microseconds since some date (say 1st Jan in year
zero) - then finding the earliest of the two is just a matter of using an arithmetic compare in an IF
statement.
The problem is that the number of microseconds since that date will exceed the accuracy range of
floating point variables and this is where integer variables come in. An integer variable can accurately
hold very large numbers up to nine million million million (or ±9223372036854775807 to be precise).
The downside of using an integer is that it cannot store fractions (ie, numbers after the decimal point).
Any calculation that produces a fractional result will be rounded up or down to the nearest whole
number when assigned to an integer. However this characteristic can be handy when dealing with
money – for example, you don’t want to send someone a bill for $100.13333333333.
It is easy to create an integer variable, just add the percent symbol (%) as a suffix to a variable name.
For example, sec% is an integer variable. Within a program you can mix integers and floating point
and MMBasic will make the necessary conversions but if you want to maintain the full accuracy of
integers you should avoid mixing the two.
Just like floating point you can have arrays of integers with up to five dimensions, all you need to do
is add the percent character as a suffix to the array name. For example: days%(365, 5).



Beginners often get confused as to when they should use floating point or integers and the answer is
simple… always use floating point unless you need an extremely high level of accuracy in the
resulting number. This does not happen often but when you need them you will find that integers are
a lifesaver.
Strings
Strings are another variable type (like floating point and integers). Strings are used to hold a sequence
of characters. For example, in the command:
PRINT "Hello"
The string "Hello" is a string constant. Note that a constant is something that does not change (as
against a variable, which can) and that string constants are always surrounded by double quotes.
String variables names use the dollar symbol ($) as a suffix to identify them as a string instead of a
normal floating point variable and you can use ordinary assignment to set their value. The following
are examples (note that the second example uses an array of strings):
Car$ = "Holden"
Country$(12) = "India"
Name$ = "Fred"
You can also join strings using the plus operator:
Word1$ = "Hello"
Word2$ = "World"
Greeting$ = Word1$ + " " + Word2$
In which case the value of Greeting$ will be "Hello World".
Strings can also be compared using operators such as = (equals), <> (not equals), < (less than), etc.
For example:
IF Car$ = "Holden" THEN PRINT "Was an Aussie made car"
The comparison is made using the full ASCII character set so a space will come before a printable
character. Also the comparison is case sensitive so 'holden' will not equal "Holden". Using the
function UCASE() to convert the string to upper case you can then have a case insensitive
comparison. For example:
IF UCASE$(Car$) = "HOLDEN" THEN PRINT "Was an Aussie made car"
You can have arrays of strings but you need to be careful when you declare them as you can rapidly
run out of RAM (general memory used for storing variables, etc). This is because MMBasic will by
default allocate 255 bytes of RAM for each element of the array. For example, a string array with 100
elements will by default use 25K of RAM. To alleviate this you can use the LENGTH qualifier to
limit the maximum size of each element. For instance, if you know that the maximum length of any
string that will be stored in the array will be less than 20 characters you can use the following
declaration to allocate just 20 bytes for each element:
DIM MyArray$(100) LENGTH 20
The resultant array will only use 2K of RAM.
Manipulating Strings
String handling is one of MMBasic's strengths and using a few simple functions you can pull apart
and generally manipulate strings. The basic string functions are:
LEFT$(string$, nbr )

Returns a substring of string$ with nbr of characters from the left
(beginning) of the string.

RIGHT$(string$, nbr )

Same as the above but return nbr of characters from the right (end) of
the string.



MID$(string$, pos, nbr )

Returns a substring of string$ with nbr of characters starting from the
character pos in the string (ie, the middle of the string).

For example if S$ = "This is a string"
then:
R$ = LEFT$(S$, 7)
would result in the value of R$ being set to: "This is"
and:
R$ = RIGHT$(S$, 8) would result in the value of R$ being set to: "a string"
finally: R$ = MID$(S$, 6, 2) would result in the value of R$ being set to: "is"
Note that in MID$() the first character position in a string is number 1, the second is number 2 and so
on. So, counting the first character as one, the sixth position is the start of the word "is".
Another useful function is:
INSTR(string$, pattern$ )

Returns a number representing the position at which pattern$ occurs in
string$.

This can be used to search for a string inside another string. The number returned is the position of
the substring inside the main string. Like with MID$() the start of the string is position 1.
For example if S$ = "This is a string"
Then: pos = INSTR(S$, " ")
would result in pos being set to the position of the first space in S$ (ie, 5).
INSTR() can be combined with other functions so this would return the first word in S$:
R$ = LEFT$(S$, INSTR(S$, " ") - 1)
There is also an extended version of INSTR():
INSTR(pos, string$, pattern$ )

Returns a number representing the position at which pattern$
occurs in string$ when starting the search at the character position
pos.

So we can find the second word in S$ using the following:
pos = INSTR(S$, " ")
R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
This last example is rather complicated so it might be worth working through it in detail so that you
can understand how it works.
Note that INSTR() will return the number zero if the sub string is not found and that any string
function will throw an error (and halt the program) if that is used as a character position. So, in a
practical program you would first check for zero being returned by INSTR() before using that value.
For example:
pos = INSTR(S$, " ")
if pos > 0 THEN R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
Scientific Notation
Before we finish discussing data types we need to cover off the subject of floating point numbers and
scientific notation.
Most numbers can be written normally, for example 11 or 24.5, but very large or small numbers are
more difficult. For example, it has been estimated that the number of grains of sand on planet Earth is
7500000000000000000. The problem with this number is that you can easily lose track of how many
zeros there are in the number and consequently it is difficult to compare this with a similar sized
number.
A scientist would write this number as 7.5 x 1018 which is called scientific notation and is much easier
to comprehend.
MMBasic will automatically shift to scientific notation when dealing with very large or small floating
point numbers. For example, if the above number was stored in a floating point variable the PRINT



command would display it as 7.5E+18 (this is BASIC’s way of representing 7.5 x 1018). As another
example, the number 0.0000000456 would display as 4.56E-8 which is the same as 4.56 x 10-8.
You can also use scientific notation when entering constant numbers in MMBasic. For example:
SandGrains = 7.5E+18
MMBasic only uses scientific notation for displaying floating point numbers (not integers). For
instance, if you assigned the number of grains of sand to an integer variable it would print out as a
normal number (with lots of zeros).
DIM Command
We have used the DIM command before for defining arrays but it can also be used to create ordinary
variables. For example, you can simultaneously create four string variables like this:
DIM STRING Car, Name, Street, City
Note that because these variables have been defined as strings using the DIM command we do not
need the $ suffix, the definition alone is enough for MMBasic to identify their type. Similarly, when
you use these variables in an expression you do not need the type suffix: For example:
City = "Sydney"
You can also use the keyword INTEGER to define a number of integer variables and FLOAT to do
the same for floating point variables. This type of notation can similarly be used to define arrays.
For example:
DIM INTEGER seconds(200)
Another method of defining the variables type is to use the keyword AS. For example:
DIM Car AS STRING, Name AS STRING, Street AS STRING
This is the method used by Microsoft (MMBasic tries to maintain Microsoft compatibility) and it is
useful if the variables have different types. For example:
DIM Car AS STRING, Age AS INTEGER, Value AS FLOAT
You can use any of these methods of defining a variable's type, they all act the same.
The advantage of defining variables using the DIM command is that they are clearly defined
(preferably at the start of the program) and their type (float, integer or string) is not subject to
misinterpretation.
You can strengthen this by using the following commands at the very top of your program:
OPTION EXPLICIT
OPTION DEFAULT NONE
The first specifies to MMBasic that all variables must be explicitly defined using DIM before they can
be used. The second specifies that the type of all variables must be specified when they are created.
Why are these two commands important?
The first can help avoid a common programming error which is where you accidently misspell a
variable's name. For example, your program might have the current temperature saved in a variable
called Temp but at one point you accidently misspell it as Tmp. This will cause MMBasic to
automatically create a variable called Tmp and set its value to zero.
This is obviously not what you want and it will introduce a subtle error which could be hard to find,
even if you were aware that something was not right. On the other hand, if you used the OPTION
EXPLICIT command at the start of your program MMBasic would refuse to automatically create the
variable and instead would display an error thereby saving you from a probable headache.
The command OPTION DEFAULT NONE further helps because it tells MMBasic that the
programmer must specifically specify the type of every variable when they are declared. It is easy to


forget to specify the type and allowing MMBasic to automatically assume the type can lead to
unexpected consequences.
For small, quick and dirty programs, it is fine to allow MMBasic to automatically create variables but
in larger programs you should always disable this feature with OPTION EXPLICIT and strengthen it
with OPTION DEFAULT NONE.
When a variable is created it is set to zero for float and integers and an empty string (ie, contains no
characters) for a string variable. You can set its initial value to something else when it is created using
DIM. For example:
DIM FLOAT nbr = 12.56
DIM STRING Car = "Ford", City = "Perth"
You can also initialise arrays by placing the initialising values inside brackets like this:
DIM s$(2) = ("zero", "one", "two")
Note that because arrays start from zero by default this array actually has three elements with the
index numbers of 0, 1 and 2. This is why we needed three string constants to initialise it.
Constants
A common requirement in programming is to define an identifier that represents a value without the
risk of the value being accidently changed - which can happen if variables were used for this purpose.
These are called constants and they can represent I/O pin numbers, signal limits, mathematical
constants and so on.
You can create a constant using the CONST command. This defines an identifier that acts like a
variable but is set to a value that cannot be changed.
For example, if you wanted to check the voltage of a battery connected to pin 31 you could define the
relevant values thus:
CONST BatteryVoltagePin = 31
CONST BatteryMinimum = 1.5
These constants can then be used in the program where they make more sense to the casual reader
than simple numbers.
For example:
SETPIN BatteryVoltagePin, AIN
IF PIN(BatteryVoltagePin) < BatteryMinimum THEN SoundAlarm
It is good programming practice to use constants for any fixed number that represents an important
value. Normally they are defined at the start of a program where they are easy to see and conveniently
located for another programmer to adjust (if necessary).
Subroutines
A subroutine is a block of programming code which is self contained (like a module) and can be
called from anywhere within your program. To your program it looks like a built in MMBasic
command and can be used the same. For example, assume that you need a command that would
signal an error by printing a message on the console. You could define the subroutine like this:
SUB ErrMsg
PRINT "Error detected"
END SUB
With this subroutine embedded in your program all you have to do is use the command ErrMsg
whenever you want to display the message. For example:
IF A < B THEN ErrMsg



The definition of a subroutine can be anywhere in the program but typically it is at the end. If
MMBasic runs into the definition while running your program it will simply skip over it.
The above example is fine enough but it would be better if a more useful message could be displayed,
one that could be customised every time the subroutine was called. This can be done by passing a
string to the subroutine as an argument (sometimes called a parameter).
In this case the definition of the subroutine would look like this:
SUB ErrMsg Msg$
PRINT "Error: " + Msg$
END SUB
Then, when you call the subroutine, you can supply the string to be printed on the command line of
the subroutine.
For example:
IF A < B THEN ErrMsg "Number too small"
When the subroutine is called like this the message "Error: Number too small" will be
printed on the console. Inside the subroutine Msg$ will have the value of "Number too small" when
called like this and it will be concatenated in the PRINT statement to make the full error message.
A subroutine can have any number of arguments which can be float, integer or string with each
argument separated by a comma.
Within the subroutine the arguments act like ordinary variables but they exist only within the
subroutine and will vanish when the subroutine ends. You can have variables with the same name in
the main program and they will be hidden within the subroutine and be different from arguments
defined for the subroutine.
The type of the argument to be supplied can be specified with a type suffix (ie, $, % or ! for string,
integer and float). For example, in the following the first argument must be a string and the second an
integer:
SUB MySub Msg$, Nbr%
…
END SUB
MMBasic will convert the supplied values if it can, so if your program supplied a floating point value
as the second argument MMBasic will convert it to an integer. If MMBasic cannot convert the value
it will display an error and return to the command prompt. For example, if you supplied a string for
the second argument your program will stop with an error.
You do not have to use the type suffixes, you can instead define the type of the arguments using the
AS keyword similar to the way it is used in the DIM command.
For example, the following is identical to the above example:
SUB MySub Msg AS STRING, Nbr AS INTEGER
…
END SUB
Of course, if you used only one variable type throughout the program and used OPTION DEFAULT
to set that type you could ignore the question of variable types completely.
When a subroutine is called with an argument that is a variable (ie, not a constant or expression)
MMBasic will create a corresponding variable within the subroutine that points back to this variable.
Any changes to the variable representing the argument inside the subroutine will also change the
variable used in the call. This is called passing arguments by reference.



This is best explained by example:
DIM MyNumber = 5
CalcSquare MyNumber
PRINT MyNumber
END
SUB CalcSquare nbr
nbr = nbr * nbr
END SUB

‘ set the variable to 5
‘ the subroutine will square its value
‘ this will print the number 25

‘ square the argument and pass it back

The subroutine CalcSquare will take its argument, square it and write it back to the variable
representing the argument (nbr). Because the subroutine was called with a variable (MyNumber) the
variable nbr will point back to MyNumber and any change to nbr will also change MyNumber
accordingly. As a result the PRINT statement will output 25.
Passing arguments by reference is handy because it allows a subroutine to pass values back to the
code that called it. However it could lead to trouble if a subroutine used the variable representing an
argument as a general purpose variable and changed its value. Then, if it were called with a variable as
an argument, that variable would be inadvertently changed. For this reason you should avoid
manipulating variables representing arguments inside a subroutine, instead assign the value to a
local variable (see below) and manipulate that instead.
When you call a subroutine you can omit some (or all) of the parameters and they will take the value
of zero (for floats or integers) or an empty string. This is handy as your subroutine can tell if a
parameter is missing and act accordingly.
For example, here is our subroutine to generate an error message but this version can be used without
specifying an error message as a parameter:
SUB ErrMsg Msg$
IF Msg$ = "" THEN
PRINT "Error detected"
ELSE
PRINT "Error: " + Msg$
ENDIF
END SUB
Within a subroutine you can use most features of MMBasic including calling other subroutines,
IF…THEN commands, FOR…NEXT loops and so on. However, one thing that you cannot do is
jump out of a subroutine using GOTO (if you do the result will be undefined and may cause your hair
to turn grey).
Normally the subroutine will exit when the END SUB command is reached but you can also terminate
the subroutine early by using the EXIT SUB command.
Functions
Functions are similar to subroutines with the main difference being that a function is used to return a
value in an expression. For example, if you wanted a function to convert a temperature from degrees
Celsius to Fahrenheit you could define:
FUNCTION Fahrenheit(C)
Fahrenheit = C * 1.8 + 32
END FUNCTION
Then you could use it in an expression:
Input "Enter a temperature in Celsius: ", t
PRINT "That is the same as" Fahrenheit(t) "F"



Or as another example:
IF Fahrenheit(temp) <= 32 THEN PRINT "Freezing"
You could also define the reverse:
FUNCTION Celsius(F)
Celsius = (F - 32) * 0.5556
END FUNCTION
As you can see, the function name is used as an ordinary local variable inside the subroutine. It is
only when the function returns that the value is made available to the expression that called it.
The rules for the argument list in a function are similar to subroutines. The only difference is that
parentheses are always required around the argument list when you are calling a function, even if
there are no arguments (parentheses are optional when calling a subroutine).
To return a value from the function you assign a value to the function's name within the function. If
the function's name is terminated with a type suffix (ie, $, a % or a !) the function will return that type
(string, integer or float), otherwise it will return whatever the OPTION DEFAULT is set to. For
example, the following function will return a string:
FUNCTION LVal$(nbr)
IF nbr = 0 THEN LVal$ = "False" ELSE LVal$ = "True"
END FUNCTION
You can explicitly specify the type of the function by using the AS keyword and then you do not need
to use a type suffix (similar to defining a variable using DIM).
This is the above example rewritten to take advantage of this feature:
FUNCTION LVal(nbr) AS STRING
IF nbr = 0 THEN LVal = "False" ELSE LVal = "True"
END FUNCTION
In this case the type returned by the function LVal will be a string.
As for subroutines you can use most features of MMBasic within functions. This includes
FOR…NEXT loops, calling other functions and subroutines, etc. Also, the function will return to the
expression that called it when the END FUNCTION command is reached but you can also return early
by using the EXIT FUNCTION command.
Local Variables
Variables that are created using DIM or that are just automatically created are called global variables.
This means that they can be seen and used anywhere in the program including within subroutines and
functions. However, inside a subroutine or function you will often need to use variables for various
tasks that are internal to the subroutine/function. In portable code you do not want the name you
chose for such a variable to clash with a global variable of the same name. To this end you can define
a variable using the LOCAL command within the subroutine/function.
The syntax for LOCAL is identical to the DIM command, this means that the variable can be an array,
you can set the type of the variable and you can initialise it to some value.
For example, this is our ErrMsg subroutine but this time it has been extended to use a local variable
for joining the error message strings.
SUB ErrMsg Msg$
LOCAL STRING tstr
tstr = "Error: " + Msg$
PRINT tstr
END SUB
The variable tstr is declared as LOCAL within the subroutine, which means that (like the argument
list) it will only exist within the subroutine and will vanish when the subroutine exits. You can have a


global variable called tstr in your main program and it will be different from the variable tstr in
the subroutine (in this case the global tstr will be hidden within the subroutine).
You should always use local variables for operations within your subroutine or function because they
help make the module much more self contained and portable.
Static Variables
LOCAL variables are reset to their initial values (normally zero or an empty string) every time the
subroutine or function starts, however there are times when you would like the variable to retain its
value between calls. This type of variable is defined with the STATIC command.
We can demonstrate how STATIC variables are useful by extending the ErrMsg subroutine to prevent
duplicated calls to the subroutine repeatedly displaying the same message. For example, our program
might call this subroutine from multiple places but if the message is the same in a number of
subsequent calls we would like to see the message just once. This is our new subroutine:
SUB ErrMsg Msg$
STATIC STRING lastmsg
LOCAL STRING tstr
IF Msg$ <> lastmsg THEN
tstr = "Error: " + Msg$
PRINT tstr
lastmsg = Msg$
ENDIF
END SUB
To keep track of the last message displayed we use a static variable called lastmsg. This will hold
the text of the last message and we can compare it to the current message text to determine if it is
different and therefore should be printed. This would give just one message every time a call is made
with a duplicate message text.
The STATIC command uses exactly the same syntax as DIM. This means that you can define
different types of static variables including arrays and you can also initialise them to some value.
The static variable is created on the first time the STATIC command is encountered and it is
automatically set to zero (if a float or integer) or an empty string. On subsequent calls to the
subroutine or function MMBasic will recognise that the variable has already been created and it will
leave its value untouched (ie, whatever it was in the previous call). As with DIM you can also
initialise a static variable to some value. For example:
STATIC INTEGER var = 123
On the first call (when the variable is created) it will be initialised to 123 but on subsequent calls it
will keep whatever its value was previously set to.
Mostly static variables are used to keep track of the state of something while inside a subroutine or
function. A state is a record of something that has happened previously.
Examples include:




Has the COM port already been opened?
What steps in a sequence have we completed?
What text has already been displayed?

Normally you will use global variables (created using DIM) to track a state but sometimes you want
this to be contained within a module and this is where static variables are valuable. Just like LOCAL
the use of STATIC helps to make your subroutines and functions more self contained and portable.



Calculate Days
We have covered a lot of programming commands and techniques so far in this tutorial and before we
finish it would be worth giving an example of how they work together. The following is an example
that uses many features of the BASIC language to calculate the number of days between two dates:
' Example program to calculate the number of days between two dates
OPTION EXPLICIT
OPTION DEFAULT NONE
DIM STRING s
DIM FLOAT d1, d2
DO
‘ main program loop
PRINT : PRINT "Enter the date as dd mmm yyyy"
PRINT " First date";
INPUT s
d1 = GetDays(s)
IF d1 = 0 THEN PRINT "Invalid date!" : CONTINUE DO
PRINT "Second date";
INPUT s
d2 = GetDays(s)
IF d2 = 0 THEN PRINT "Invalid date!" : CONTINUE DO
PRINT "Difference is" ABS(d2 - d1) " days"
LOOP
' Calculate the number of days since 1/1/1900
FUNCTION GetDays(d$) AS FLOAT
LOCAL STRING Month(11) =
("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
LOCAL FLOAT Days(11) = (0,31,59,90,120,151,181,212,243,273,304,334)
LOCAL FLOAT day, mth, yr, s1, s2
' Find the separating space character within a date
s1 = INSTR(d$, " ")
IF s1 = 0 THEN EXIT FUNCTION
s2 = INSTR(s1 + 1, d$, " ")
IF s2 = 0 THEN EXIT FUNCTION
' Get the day, month and year as numbers
day = VAL(MID$(d$, 1, s2 - 1)) - 1
IF day < 0 OR day > 30 THEN EXIT FUNCTION
FOR mth = 0 TO 11
IF LCASE$(MID$(d$, s1 + 1, 3)) = Month(mth) THEN EXIT FOR
NEXT mth
IF mth > 11 THEN EXIT FUNCTION
yr = VAL(MID$(d$, s2 + 1)) - 1900
IF yr < 1 OR yr >= 200 THEN EXIT FUNCTION
' Calculate the number of days including adjustment for leap years
GetDays = (yr * 365) + FIX((yr - 1) / 4)
IF yr MOD 4 = 0 AND mth >= 2 THEN GetDays = GetDays + 1
GetDays = GetDays + Days(mth) + day
END FUNCTION

Note that the line starting LOCAL STRING Month(11) has been wrapped around because of the
limited page width – it is one line as follows:
LOCAL STRING Month(11) = ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")

This program works by getting two dates from the user at the console and then converting them to
integers representing the number of days since 1900. With these two numbers a simple subtraction
will give the number of days between them.



When this program is run it will ask for the two dates to be entered and you need to use the form of:
dd mmm yyyy.
This screen capture shows what the
running program will look like.
The main feature of the program is the
defined function GetDays() which
takes a string entered at the console,
splits it into its day, month and year
components then calculates the number
of days since 1st January 1900.
This function is called twice, once for
the first date and then again for the
second date. It is then just a matter of
subtracting one date (in days) from the
other to get the difference in days.
We will not go into the detail of how the calculations are made (ie, handling leap years) as that can be
left as an exercise for the reader. However, it is appropriate to point out some features of MMBasic
that are used by the program.
It demonstrates how local variables can be used and how they can be initialised. In the function
GetDays() two arrays are declared and initialised at the same time. These are just a convenient
method of looking up the names of the months and the cumulative number of days for each month.
Later in the function (the FOR loop) you can see how they make dealing with twelve different months
quite efficient.
Another feature highlighted by this program is the string handling features of MMBasic. The
INSTR() function is used to locate the two space characters in the date string and then later the
MID$() function uses these to extract the day, month and year components of the date. The VAL()
function is used to turn a string of digits (like the year) into a number that can be stored in a numeric
variable.
Note that the value of a function is initialised to zero every time the function is run and unless it is set
to some value it will return a zero value. This makes error handling easy because we can just exit the
function if an error is discovered. It is then the responsibility of the calling program code to check for
a return value of zero which signifies an error.
This program illustrates one of the benefits of using subroutines and functions which is that when
written and fully tested they can be treated as a trusted "black box" that does not have to be opened.
For this reason functions like this should be the properly tested and then, if possible, left untouched (in
case you add some error).
There are a few features of this program that we have not covered before. The first is the MOD
operator which will calculate the remainder of dividing one number into another. For example, if you
divided 4 into 15 you would have a remainder of 3 which is exactly what the expression 15 MOD 4
will return. The ABS() function is also new and will return its argument as a positive number (eg,
ABS(-15) will return +15 as will ABS(15)).
The EXIT FOR command will exit a FOR loop even though it has not reached the end of its looping,
EXIT FUNCTION will immediately exit a function even though execution has not reached the end of
the function and CONTINUE DO will immediately cause the program to jump to the end of a DO
loop and execute it again.
Why would this program be useful? Well some people like to count their age in days, that way every
day is a birthday! You can calculate your age in days, just enter the date that you were born and
today's date. That is not particularly useful but the program itself is valuable as it demonstrates many
of the characteristics of programming in MMBasic. So, work your way through the program and
review each section until you understand it – it should be a rewarding experience.




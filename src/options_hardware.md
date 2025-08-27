# Hardware

These function change settings in the Picocalc's own hardware.

For input/output devices see the chapters [Mouse], [Keyboard](keyboard.md), [Display](display.md), [Audio](audio.md)

## OPTION BAUDRATE nn

Set the baudrate of the serial console (if it is configured).


## OPTION COUNT pin1, pin2, pin3, pin4

Specifies which pins are to be used as Count inputs. By default these are `GP6`, `GP7`, `GP8` and `GP9`. The `SETPIN` command defines the Counter mode.

*This command must be run at the command prompt (not in a program).*


## OPTION CPUSPEED speed

*NOT ON HDMI OR VGA VERSIONS*

Change the CPU clock speed. `speed` is the CPU clock in KHz in the range of 48000 to 378000. Speeds above 200MHz (150MHz for the RP2350) are regarded as overclocking as that is the specified maximum speed of the standard Raspberry Pi Pico.

Pico | Default speed 
:-: | -:
RP2040 | 200000
RP2350 | 150000

*This command must be run at the command prompt (not in a program).*


## OPTION HEARTBEAT ON/OFF [HEARTBEATpin]

Enables or disables the output of the heartbeat LED.

In the case of the Pico-W the heartbeat is on a pin controlled by the CWY43 chip.

*NOT WEBMITE VERSION*

By default, for RP2350A chips the heartbeat is enabled on GP25. If it is disabled the program can control the LED via GP25.

For RP2350B chips the heartbeat is not enabled.

If the heartbeat is disabled then the command can be used both to enable it and optionally specify the pin to use (default GP25)


## OPTION PICO ON/OFF

*ALL VERSIONS EXCEPT WEBMITE*

When set to OFF pins GP23, GP24 and GP29 are not set up for normal Pico use and are immediately available to use. 

Default ON for RP2350A and RP2040, OFF for RP2350B


## OPTION POWER PFM | PWM

Changes operation of the 3.3V supply switch mode power supply.

By default this runs in PFM mode. PWM gives better noise performance but is less power-efficient. Note that under heavy load the system will run in PWM mode regardless of this setting.


## OPTION PSRAM PIN n <br> OPTION PSRAM PIN DISABLE

Enable/disable PSRAM support. 

`n` is the PSRAM chip select (CS) pin and can be GP0, GP8, GP19, or
GP47.

Typically GP47 is used for Pimoroni boards. Default is disabled.


## OPTION SYSTEM I2C sdapin, sclpin [,SLOW]<br>OPTION SYSTEM I2C sdapin, sclpin [,FAST]

Specify the I²C port and pins for use by system devices (LCD panel, and RTC).

The PicoMite firmware uses a specific I2C port for system devices, leaving the other for the programmer. This command specifies which pins are to be used, and hence which of the I2C ports is to be used.

The pins allocated to the SYSTEM I2C will not be available for other MMBasic SETPIN settings but can be used for additional I2C devices using the standard I2C command. Note: I2C(2) OPEN and I2C(2) CLOSE are not available in this case.

By default the I2C port is opened at a speed of 400KHz and with a 100mSec timeout. The I2C frequency can be set using the optional third parameter which can take the values FAST = 400KHz or SLOW = 100KHz.

*This command must be run at the command prompt (not in a program).*


## OPTION SYSTEM SPI CLKpin, MOSIpin, MISOpin <br> OPTION SYSTEM SPI DISABLE

Specify or disable the SPI port and pins for use by system devices (SD Card, LCD panel, etc).

The PicoMite firmware uses a specific hardware SPI port for system devices, leaving the other for the user. This command specifies which pins are to be used, and hence which of the SPI ports is to be used. The pins allocated to the `SYSTEM SPI` will not be available to other MMBasic commands.

*This command must be run at the command prompt (not in a program).*


## OPTION VCC voltage

Specifies the voltage (Vcc) supplied to the Raspberry Pi Pico.

When using the ADC pins to measure voltage the PicoMite firmware uses the voltage on the pin marked VREF as its reference. This voltage can be accurately measured using a DMM and set using this command for more accurate measurement.

The parameter is not saved and should be initialised either on the command line or in a program. The default if not set is `3.3`.


## OPTION RTC AUTO ENABLE | DISABLE

Enable auto-load time$ & date$ from RTC on boot & every hour. If enabled and the RTC does not respond then any running program will abort with an error. At the command prompt an information message will be output.

*This command must be run at the command prompt (not in a program).*

## OPTION SERIAL CONSOLE uartapin, uartbpin [,B]

Specify that the console be accessed via a hardware serial port (instead
of virtual serial over USB).

`uartapin` and `uartbpin` can be any valid pair of rx and tx pins for either
COM1 or COM2. The order that they are specified is not important.

The speed defaults to 115200 baud but can be changed with OPTION
BAUDRATE. Adding the "B" parameter means output will go to "B"oth
the serial port and the USB.


## OPTION SERIAL CONSOLE DISABLE

Revert to the normal the USB console.

These commands must be run at the command prompt (not in a program).
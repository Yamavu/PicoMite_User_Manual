# Display

Various settings for VGA, HDMI, I2C or SPI displays, also touch sensitive displays.


## OPTION AUTOREFRESH OFF | ON

Black and white displays can only be updated a full screen at a time. By using OPTION AUTOREFRESH OFF/ON you can control whether a write command immediately updates the display or not. 

If `AUTOREFRESH` is `OFF` the `REFRESH` command can be used to
trigger the write. This applies to the following displays: N5110, SSD1306I2C, SSD1306I2C32, SSD1306SPI and ST7920


## OPTION DISPLAY lines [,chars]

Set the characteristics of the display terminal used for the console. Both the `LIST` and `EDIT` commands need to know this information to correctly format the text for display.

`lines` is the number of lines on the display and `chars` is the width of the display in characters. The default is 24 lines x 80 chars and when changed this option will be remembered even when the power is removed. Maximum values are 100 lines and 240 chars.

This will send an ESC sequence to set the VT100 terminal to the matching size. TerraTerm, Putty and MMCC respond to this sequence
and set the terminal width (if the option is enabled in the terminal setup).

This option is not available if an LCD display is being used as the console.


## OPTION HDMI PINS clockpositivepin, d0positivepin, d1positivepin, d2positivepin

*HDMI VERSION ONLY*

Set the I/O pins used for the HDMI video output. This is only required to suit nonstandard PCB layouts.

The positive HDMI signal pins are set according to `nbr` below. Valid values are 0-7 and the pins must not overlap for each channel. If `nbr` is an even number the negative output is on physical pin+1, if `nbr` is odd it will be on physical pin-1.

nbr | HSTX Nbr | Physical Pin
:-: | :-: | :-:
0 | HSTX0 | GP12
1 | HSTX1 | GP13
2 | HSTX2 | GP14
3 | HSTX3 | GP15
4 | HSTX4 | GP16
5 | HSTX5 | GP17
6 | HSTX6 | GP18
7 | HSTX7 | GP19

The default is: `OPTION HDMI PINS 2, 0, 6, 4`

Which means that:

- CK+ and CK- are allocated to GP14 and GP15
- D0+ and D0- are allocated to GP12 and GP13
- D1+ and D1- are allocated to GP18 and GP19
- D2+ and D2- are allocated to GP16 and GP17


## OPTION LCD320 ON/OFF

*not VGA or HDMI versions*

This enables or disables 16-bit LCD displays in 320x240 mode allowing things like games on these larger LCD displays. In the case of 800x480 displays the 320x240 image is scaled by 2 and occupies the screen area 80,0 to 719,479 .

In the case of 480x272 displays the 320x240 image is windowed and occupies the screen area 80,16 to 399,255


## OPTION LCDPANEL VIRTUAL_C <br> OPTION LCDPANEL VIRTUAL_M

*not VGA or HDMI versions*

Configures a virtual LCD panel without a physically connected panel.

* `VIRTUAL_C` = Colour, 4bit, 320 x 240
* `VIRTUAL_M` = Monochrome, 640 x 480

Using this feature a program can draw graphical images on this virtual panel and then save them as a BMP file. Useful for creating a graphic image for export without an attached display.


## OPTION LCDPANEL options <br> OPTION LCDPANEL DISABLE

*not VGA or HDMI versions*

Configures the PicoMite firmware to work with an attached LCD panel.

See the chapter [LCD Displays](../display_panels.md) for the details.

*This command must be run at the command prompt (not in a program).*


## OPTION LCDPANEL CONSOLE [font [, fc [, bc [, blight]]] [,NOSCROLL] <br> OPTION LCDPANEL NOCONSOLE

*not VGA or HDMI versions*

Configures the LCD display panel for use as the console output. The LCD must support transparent text (i.e. the SSD1963_x, ILI9341 or ST7789_320 controllers).

`font` is the default font, `fc` is the default foreground colour, `bc` is the default background colour. 

These parameters are optional and default to font 1, white, black and 100%. These settings are applied at power up.

The optional `NOSCROLL` command changes the firmware such that when outputting to the last line of the display rather than the display scrolling it is cleared and output continues at the top of the display. This allows displays that don’t support reading to be used as a console device.

Note that for displays other than the SSD1963 scrolling for any console output is very slow so it is recommended to use the NOSCROLL option for these displays. This setting is saved in flash and will be automatically applied on startup. To disable it use the `OPTION LCDPANEL NOCONSOLE` command.

*This command must be run at the command prompt (not in a program).*


## OPTION LCDPANEL CONSOLE [font [, fc [,bc]]] <br> OPTION LCDPANEL NOCONSOLE

*VGA and HDMI versions only*

Changes the default font used on the VGA or HDMI display. 

`fc` is the foreground colour and `bc` is the background colour.

Disables the console output to the VGA/HDMI display.

This option is permanent, both print output and console output will be disabled and only graphics commands will output to the VGA screen.

If output is required to be temporarily disabled in a program use the `OPTION CONSOLE` command.

For SSD1963 based displays in landscape and SPI displays in portrait the firmware uses H/W scrolling to improve display console performance.


## OPTION LCDPANEL USER hres, vres

*not VGA or HDMI versions*

Configures a user written display driver in MMBasic. See the file “User Display Driver.txt” in the PicoMite firmware distribution for a description of how to write the driver.


## OPTION RESOLUTION nn [,cpuspeedinKhz]

*HDMI and VGA VERSIONS ONLY*
For firmware with HDMI video set the video resolution to `nn`.

Where `nn` is:

- `640x480` or `640`
- `720x400` or `720`
- `800x600` or `800` (RP2350 only)
- `848x480` or `848` (RP2350 only)
- `1280x720` or `1280` (HDMI only)
- `1024x768` or `1024` (HDMI only)

For `640x480` the display frequency can be set to 60Hz (252Mhz or 378MHz) or 75Hz (315MHz) by appending cpuspeedinKHz to the command (ie, `252000`, `378000` or `315000`).

Each VGA and HDMI resolution can operate in a number of modes which are set using the MODE command.

Note that `800x600` and `848x480` resolutions reduce both the maximum program size and the variable space available to the Basic programs


## OPTION TOUCH T_CS pin <br> T_IRQ pin [, Beep] <br> OPTION TOUCH DISABLE

*NOT VGA OR HDMI VERSIONS*

Configures MMBasic for the touch sensitive feature of an attached LCD
panel.

`T_CS pin` and `T_IRQ pin` are the I/O pins to be used for chip select and
touch interrupt respectively (any free pins can be used). The remaining
pins are connected to those specified using the OPTION SYSTEM SPI
command.

`Beep` is an optional pin which can be connected to a small
buzzer/beeper to generate a "click" or beep sound when an Advanced
Graphics control is touched (ie, radio button, switch, etc). This is
described in Advanced Graphics Functions.pdf.

*This command must be run at the command prompt (not in a program).*


## OPTION TOUCH FT6336 IRQpin, RESETpin [,BEEPpin] [,sensitivity]

*NOT VGA OR HDMI VERSIONS*

Enables touch support for FT6336 capacitive touch chip. Sensitivity is a number between `0` and `255` - defaults to `50`, lower is more sensitive.

`SDA` and `SCK` should be connected to valid I2C pins and set up with `OPTION SYSTEM I2C`. See also the `TOUCH` function.


## OPTION VGA PINS HSYNCpin, BLUEpin

*VGA VERSION ONLY*

Changes the pins used for VGA display output allowing more flexibility in PCB design or wiring. `HSYNCpin` defines the start of a pair of contiguous GP numbered pins that are connected to `HSYNC` and `VSYNC`.

“BLUEpin” defines the start of four contiguous GP numbered pins that are connected to `BLUE`, `GREEN_LSB`, `GREEN_MSB`, and `RED`.

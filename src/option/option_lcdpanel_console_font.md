## OPTION LCDPANEL CONSOLE [font [, fc [, bc [, blight]]] [,NOSCROLL] <br> OPTION LCDPANEL NOCONSOLE

*not VGA or HDMI versions*

Configures the LCD display panel for use as the console output. The LCD must support transparent text (i.e. the SSD1963_x, ILI9341 or ST7789_320 controllers).

`font` is the default font, `fc` is the default foreground colour, `bc` is the default background colour. 

These parameters are optional and default to font 1, white, black and 100%. These settings are applied at power up.

The optional `NOSCROLL` command changes the firmware such that when outputting to the last line of the display rather than the display scrolling it is cleared and output continues at the top of the display. This allows displays that don’t support reading to be used as a console device.

Note that for displays other than the SSD1963 scrolling for any console output is very slow so it is recommended to use the NOSCROLL option for these displays. This setting is saved in flash and will be automatically applied on startup. To disable it use the `OPTION LCDPANEL NOCONSOLE` command.

*This command must be run at the command prompt (not in a program).*


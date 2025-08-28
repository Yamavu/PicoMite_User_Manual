# OPTION LCDPANEL CONSOLE [font [, fc [,bc]]] <br> OPTION LCDPANEL NOCONSOLE

*VGA and HDMI versions only*

Changes the default font used on the VGA or HDMI display. 

`fc` is the foreground colour and `bc` is the background colour.

Disables the console output to the VGA/HDMI display.

This option is permanent, both print output and console output will be disabled and only graphics commands will output to the VGA screen.

If output is required to be temporarily disabled in a program use the `OPTION CONSOLE` command.

For SSD1963 based displays in landscape and SPI displays in portrait the firmware uses H/W scrolling to improve display console performance.


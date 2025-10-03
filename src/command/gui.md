.wip


### GUI BITMAP x, y, bits [, width] [, height] [, scale] [, c] [, bc]

Displays the bits in a bitmap on a VGA/HDMI monitor or LCD panel starting at 'x' and 'y' on an attached device. 'height' and 'width' are the dimensions of the bitmap as displayed on the device and default to 8x8. 'scale' is optional and defaults to that set by the FONT command. 'c' is the drawing colour and 'bc' is the background colour. They are optional and default to the current foreground and background colours. The bitmap can be an integer or a string variable or constant and is drawn using the first byte as the first bits of the top line (bit 7 first, then bit 6, etc) followed by the next byte, etc. When the top line has been filled the next line of the displayed bitmap will start with the next bit in the integer or string. See the chapter Graphics Commands and Functions for a definition of the colours and graphics coordinates. NOT VGA AND HDMI VERSIONS

### GUI CALIBRATE or

This command is used to calibrate the touch feature on an LCD panel. It will display a series of targets on the screen and wait for each one to be precisely touched.

### GUI CALIBRATE a,b,c,d,d

The command can also be used with five arguments which specify the calibration values and in this case the calibration will be done without displaying any targets or requiring an input from the user. To discover the values use the OPTION LIST after calibrating the display normally. Note that these values are specific to that display and can vary considerably.

### GUI TEST LCDPANEL

Will test a display device (LCD, VGA, etc). It will continuously draw an animated display of colour circles on the display. NOT VGA AND HDMI VERSIONS

### GUI RESET LCDPANEL

Will reinitialise the configured LCD panel. Initialisation is automatically done when the PicoMite firmware starts up but in some circumstances it may be necessary to interrupt power to the LCD panel (eg, to save battery power) and this command can then be used to reinitialise the display.

### GUI TEST TOUCH

Will test the display touch feature on an LCD panel. The screen will be cleared and MMBasic will wait for a touch which will cause a white dot to be placed on the display marking the exact touch position on the screen. Any character entered at the console will terminate the test.
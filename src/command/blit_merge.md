### BLIT MERGE colour, x, y, w, h

*not VGA or HDMI versions*

Copies an area of the framebuffer defined by the `x` and `y` pixel coordinates of the top left and with a width of `w` and height `h` to the LCD display.

As part of the copy it will overlay the LCD display with pixels from the layer buffer that aren't set to the `colour` specified. The colour is specified as a number between `0` and `15` representing: 

black, blue, myrtle, cobalt, midgreen, cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white

Requires both a framebuffer and a layer buffer to have been created to operate. 

Will automatically wait for frame blanking before starting the copy on ILI9341, ST7789_320 and ILI9488 displays.

### CAMERA CAPTURE [scale, [x , y]]

This captures a picture from the camera (RGB565) and displays it on an LCD screen.

An SPI LCD must be connected and enabled in order for the command to work. (ILI9341 and ST7789_320 recommended). 

Scale defaults to 1 and x,y each to 0 By default a 160x120 image is output on the LCD with the top left at `0,0` on the LCD. Setting scale to `2` will fill a 320x240 display with the image.

Setting the `x` and `y` parameters will offset the top left of the image on the LCD. Update rate in a continuous loop is 7FPS onto the display at 1:1 scale and 5FPS scaled to 320x240. 

Assuming the display has MISO wired it is then possible to save the image to disk using the `SAVE IMAGE` command.

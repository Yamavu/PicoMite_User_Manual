

### BLIT

BLIT is a simple memory operation copying to and from a display or memory to a display or memory. Notes:  32 buffers are available ranging from #1 to #32.  When specifying the buffer number the # symbol is optional.  All other arguments are in pixels.

### BLIT READ [#]b, x, y, w, h

BLIT READ will copy a portion of the display to the memory buffer '#b'. The source coordinate is 'x' and 'y' and the width of the display area to copy is 'w' and the height is 'h'. When this command is used the memory buffer is automatically created and sufficient memory allocated. This buffer can be freed and the memory recovered with the BLIT CLOSE command.

### BLIT WRITE [#]b, x, y [,mode]

BLIT WRITE will copy the memory buffer '#b' to the display. The destination coordinate is 'x' and 'y'. The optional 'mode' parameter defaults to 0 and specifies how the stored image data is changed as it is written out. It is the bitwise AND of the following values: &B001 = mirrored left to right &B010 = mirrored top to bottom &B100 = don't copy transparent pixels

### BLIT LOAD[BMP] [#]b, fname$ [,x] [,y] [,w] [,h]

BLIT LOAD will load a blit buffer from a 24-bit bmp image file. x,y define the start position in the image to start loading and w,h specify the width and height of the area to be loaded. This command will work on most display panels (not just panels using the ILI9341 controller). eg, BLIT LOAD #1,"image1", 50,50,100,100 will load an area of 100 pixels square with the top left had corner at 50,50 from the image image1.bmp

### BLIT CLOSE [#]b

BLIT CLOSE will close the memory buffer '#b' to allow it to be used for another BLIT READ operation and recover the memory used. NOT VGA OR HDMI VERSIONS

### BLIT MERGE colour, x, y, w, h

Copies an area of the framebuffer defined by the ‘x’ and ‘y’ pixel coordinates of the top left and with a width of ‘w’ and height ‘h’ to the LCD display. As part of the copy it will overlay the LCD display with pixels from the layer buffer that aren’t set to the ‘colour’ specified. The colour is specified as a number between 0 and 15 representing: Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white Requires both a framebuffer and a layer buffer to have been created to operate. Will automatically wait for frame blanking before starting the copy on ILI9341, ST7789_320 and ILI9488 displays

### BLIT FRAMEBUFFER from, to, xin, yin, xout, yout, width, height [,colour]

Copies an area of a specific ‘from’ framebuffer N, F, or L to another different ‘to’ framebuffer N, F, or L. ‘xin’ and ‘yin’ define the top left of the area of ‘width’ and ‘height’ on the source framebuffer to be copied. ‘xout’ and ‘yout’ define the top left of the area on the target framebuffer to receive the copy. The optional parameter colour defines a pixel colour on the source which will not be copied. If omitted all pixels are copied. The colour is specified as a number between 0 and 15 representing: Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white Requires both a framebuffer and a layer buffer to have been created to operate. Will automatically wait for frame blanking before starting the copy on ILI9341, ST7789_320 and ILI9488 displays

### BLIT MEMORY address, x, y [,col]

Copies an area of memory treated as a packed array of colour nibbles to the current graphical output as specified by FRAMEBUFFER WRITE. The colour is specified as a number between 0 and 15 representing: Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white The first word of the area of memory starting at ‘address%’ must contain the width and height of the area to be copied as 16-bit integers with the width as the bottom 16 bits. The address must be aligned to a word boundary (divisible by 4). If the optional parameter ‘col’ is specified then that specific colour is not copied. If the top bit of either the width or height is set to 1 then the colour data is treated as compressed (the remaining 15 bits are used as the width and/or height). The compression algorithm is simple, each byte contains a count in the bottom nibble (1-15) and a colour in the top nibble (0-15). In the event that more than 15 pixels are the same colour additional bytes are used for that colour.

### BLIT COMPRESSED address%, x, y [,col]

Acts the same as BLIT MEMORY but assumes the data is compressed and ignores the top bit in the width and height

### BLIT x1, y1, x2, y2, w, h

Copy one section of the display screen to another part of the display. The source coordinate is 'x1' and 'y1'. The destination coordinate is 'x2' and 'y2'. The width of the screen area to copy is 'w' and the height is 'h'. All arguments are in pixels. If the output is to an LCD panel it must be either the SSD19863, ILI9341_8, ILI9341, ILI9488 (if MISO connected), or ST7789_320 controllers.
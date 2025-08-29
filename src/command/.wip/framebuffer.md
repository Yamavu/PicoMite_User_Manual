

### FRAMEBUFFER

 The Framebuffer command allow you to allocate some of the variable memory to either a framebuffer, a second display layer, or both and then use these in interesting ways to both avoid tearing artefacts and/or play graphics objects over the background display.

### FRAMEBUFFER CREATE

 Creates a framebuffer “F” with a RGB121 colour space and resolution to match the configured SPI colour display

### FRAMEBUFFER LAYER

 Creates a framebuffer “L” with a RGB121 colour space and resolution to match the configured SPI colour display

### FRAMEBUFFER WRITE where/where$

 Specifies the target for subsequent graphics commands. "where" can be N, F, or L where N is the actual display. AA string variable can be used or a literal

### FRAMEBUFFER CLOSE [which]

 Closes a framebuffer and releases the memory. The optional parameter "which" can be F or L. If omitted closes both.

### FRAMEBUFFER COPY from, to [,b]

 Does a highly optimised full screen copy of one framebuffer to another. "from" and "to" can be N, F, or L where N is the physical display. You can only copy from N on displays that support BLIT and transparent text. The firmware will automatically compress or expand the RGB resolution when copying to and from unmatched framebuffers. Of course copying from RGB565 to RGB121 loses information but for many applications (eg, games) 16 colour levels is more than enough. When copying to an LCD display the optional parameter “b” can be used (FRAMEBUFFER COPY F/L, N, B). This instructs the firmware to action the copy using the second CPU in the Raspberry Pi Pico and control returns immediately to the Basic program

### FRAMEBUFFER WAIT

 Pauses processing until the LCD display enters frame blanking. Implemented for ILI9341, ST7789_320 and ILI9488 displays. Used to reduce artefacts when writing to the screen

### FRAMEBUFFER MERGE [colour] [,mode] [,updaterate]

 Copies the contents of the Layer buffer and Framebuffer onto the LCD display omitting all pixels of a particular colour. Preconditions for the command are that FRAMEBUFFER and LAYERBUFFER are both created FRAMEBUFFER MERGE - writes the contents of the framebuffer to the physical display overwriting any pixels in the framebuffer that are set in the layerbuffer (not zero) FRAMEBUFER MERGE col - writes the contents of the framebuffer to the physical display overwriting any pixels in the framebuffer that are in the layerbuffer not set to the transparent colour "col". The colour is specified as a number between 0 and 15 representing: 0:BLACK,1:BLUE,2:MYRTLE,3:COBALT,4:MIDGREEN,5:CERULEAN,6: GREEN,7:CYAN,8:RED,9:MAGENTA,10:RUST,11:FUCHSIA,12:BROWN, 13:LILAC,14:YELLOW,15:WHITE FRAMEBUFFER MERGE col,B - as above except that the transfer to the physical display takes place on the second CPU and control returns to Basic immediately FRAMEBUFFER MERGE col,R [,updaterate] - sets the second CPU to continuously update the physical display with the merger of the two buffers. Automatically sets FRAMEBUFFER WRITE F if not F or L already set. By default the screen will update as fast as possible (At 200MHz an ILI9341 in SPI mode updates about 13 times a second, in 8-bit parallel mode the ILI9341 achieves 27 FPS) If "updaterate" is set then the screen will update to the rate specified in milliseconds (unless that is less than the fastest achievable on the display) NB: FRAMEBUFFER WRITE cannot be set to N while continuous merged update is active. FRAMEBUFFER MERGE col,A - aborts the continuous updates In addition deleting either the layerbuf or framebuffer, ctrl-C, or END will abort the automatic update as well.

### FRAMEBUFFER SYNC

 Waits for the latest update on the second CPU to complete to allow drawing without tearing HDMI AND VGA VERSIONS ONLY

### FRAMEBUFFER

 The Framebuffer command allow you to allocate some of the variable memory to framebuffers, layer buffers, or both and then use these in interesting ways to both avoid tearing artefacts and/or play graphics objects over the background display.

### FRAMEBUFFER CREATE

 Creates a framebuffer “F” with a colour space and resolution to match the current display mode

### FRAMEBUFFER CREATE 2

 RP2350 only: Creates a second framebuffer “2” with a colour space and resolution to match the current display mode

### FRAMEBUFFER LAYER [colour]

 Creates a layer buffer “L” with a colour space and resolution to match the current display mode. The optional parameter colour is specified as a number 0-15 (modes 2 and 3), RGB888 colour (mode 4) or 0-255 (mode 5) and specifies a colour which is ignored when the layer is applied to the display. In display modes where automatic layer application is not supported a layer buffer acts as another framebuffer.

### FRAMEBUFFER LAYER

 RP2350 only: Creates a second layer buffer “T” with a colour space and

### FRAMEBUFFER WRITE where/where$

 Specifies the target for subsequent graphics commands. "where" can be N, F, 2, T, or L where N is the actual display. A string variable can be used

### FRAMEBUFFER CLOSE [which]

 Closes a framebuffer and releases the memory. The optional parameter "which" can be F, 2, T or L. If omitted closes all.

### FRAMEBUFFER COPY from, to [,b]

 Does a highly optimised full screen copy of one framebuffer to another. "from" and "to" can be N, F, 2, T, or L where N is the physical display. If the optional parameter ‘b’ is specified pauses processing until the Monitor enters frame blanking.

### FRAMEBUFFER WAIT

 Pauses processing until the next frame blanking starts
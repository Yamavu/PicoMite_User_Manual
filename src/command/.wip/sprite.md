

### SPRITE

The SPRITE commands are used to manipulate small graphic images on the VGA or HDMI screen and are useful when writing games. Sprites operate in framebuffers in MODEs 2 and 3 only. Sprites are always stored as RGB121 'nibbles' for efficiency The maximum size of a sprite is MM.HRES-1 and MM.VRES-1. See also the BLIT command and SPRITE() functions.

### SPRITE CLOSE [#]n

Closes sprite “n” and releases its memory resources allowing the sprite number to be re-used. The command will give an error if other sprites are copied from this one unless they are closed first.

### SPRITE CLOSE ALL

Closes all sprites and releases all sprite memory. The screen is not changed

### SPRITE COPY [#]n, [#]m, nbr

Makes a copy of sprite “n” to “nbr” of new sprites starting a number “m”. Copied sprites share the same loaded image as the original to save memory

### SPRITE HIDE [#]n

Removes sprite n from the display and replaces the stored background. To restore a screen to a previous state sprites should be hidden in the opposite order to which they were written "LIFO"

### SPRITE HIDE ALL

Hides all the sprites allowing the background to be manipulated. The following commands cannot be used when all sprites are hidden: SPRITE SHOW (SAFE) SPRITE HIDE (SAFE, ALL) SPRITE SWAP SPRITE MOVE SPRITE SCROLLR SPRITE SCROLL

### SPRITE RESTORE

Restores the sprites that were previously hidden with SPRITE HIDE ALL.

### SPRITE HIDE SAFE [#]n

Removes sprite n from the display and replaces the stored background. Automatically hides all more recent sprites as well as the requested one and then replaces them afterwards. This ensures that sprites that are covered by other sprites can be removed without the user tracking the write order. Of course this version is less performant than the simple version and should only be used it there is a risk of the sprite being partially covered.

### SPRITE INTERRUPT sub

Specifies the name of the subroutine that will be called when a sprite collision occurs. See Appendix H for how to use the function SPRITE to interrogate details of what has collided.

### SPRITE READ [#]b, x, y, w, h

This will copy a portion of the display to the memory buffer '#b'. The source coordinate is 'x' and 'y' and the width of the display area to copy is 'w' and the height is 'h'. When this command is used the memory buffer is automatically created and sufficient memory allocated. This buffer can be freed and the memory recovered with the SPRITE CLOSE command.

### SPRITE WRITE [#]b, x, y [,mode]

Will copy sprite '#b' to the display. The destination coordinate is 'x' and 'y'. The optional 'mode' parameter defaults to 4 and specifies how the stored image data is changed as it is written out. It is the bitwise AND of the following values: &B001 = mirrored left to right &B010 = mirrored top to bottom &B100 = don't copy transparent pixels

### SPRITE LOAD fname$ [,start_sprite_number] [,mode]

Loads the file ‘fname$’ which must be formatted as an original Colour Maximite sprite file. See the original Colour Maximite MMBasic Language Manual for the file format. Multiple sprite files can be loaded by specifying a different ‘start_sprite_number’ for each file. The programmer is responsible for making sure that the sprites do not overlap. Mode defaults to zero in which case the CMM1/CMM2 colour codes are used (Black, Blue, Green, Cyan, Red, Magenta, Yellow, White, Myrtle, Cobalt, Midgreen, Cerulean, Rust, Fuchsia, Brown, Lilac); If mode is specified as 1 then the RGB121 colour codes are used: (Black, Blue, Myrtle, Cobalt, Midgreen, Cerulean, Green, Cyan, Red, Magenta, Rust, Fuchsia, Brown, Lilac, Yellow, White).

### SPRITE LOADARRAY [#]n, w, h, array%()

Creates the sprite 'n' with width 'w' and height 'h' by reading w*h RGB888 values from 'array%()'. The RGB888 values must be stored in order of columns across and then rows down starting at the top left. This allows the programmer to create simple sprites in a program without needing to load them from disk or read them from the display. The firmware will generate an error if 'array%()' is not big enough to hold the number of values required.

### SPRITE LOADBMP [#]b, fname$ [,x] [,y] [,w] [,h]

Will load a blit buffer from a 24-bit bmp image file. 'x' and 'y' define the start position in the image to start loading and 'w' and 'h' specify the width and height of the area to be loaded. eg, SPRITE LOAD #1,"image1", 50,50,100,100 will load an area of 100 pixels square with the top left had corner at 50, 50 from the image image1.bmp

### SPRITE LOADPNG [#]b, fname$ [,transparent] [,alphacut]

Loads SPRITE number ‘b’ from the png file ‘fname$’. If no extension is specified .png will be automatically added to the filename. The file must be in RGBA8888 format which is the normal default. The optional parameter 'transparent' (defaults to 0) specifies one of the colour codes (0-15) which will be allocated to pixels in the png file with an alpha value less than 'alphacut' (defaults to 20). The variable transparency can then used with the command SPRITE SET TRANSPARENT n or FRAMEBUFFER LAYER n to display the sprite with the transparent region hidden.

### SPRITE MOVE

Actions a single atomic transaction that re-locates all sprites which have previously had a location change set up using the SPRITE NEXT command. Collisions are detected once all sprites are moved and reported in the same way as from a scroll

### SPRITE NEXT [#]n, x, y

Sets the X and Y coordinate of the sprite to be used when the screen is next scrolled or the SPRITE MOVE command is executed. Using SPRITE NEXT rather than SPRITE SHOW allows multiple sprites to be moved as part of the same atomic transaction.

### SPRITE SCROLL x, y [,col]

Scrolls the background and any sprites on the active framebuffer (L or N) 'x' pixels to the right and 'y' pixels up. 'x' can be any number between - MM.HRES-1 and MM.HRES-1, 'y' can be any number between -MM.VRES-1 and MM.VRES-1. Sprites on any layer other than zero will remain fixed in position on the screen. By default the scroll wraps the image round. If 'col' is specified the colour will replace the area behind the scrolled image. If 'col' is set to -1 the scrolled area will be left untouched.

### SPRITE SET

Sets the colour code (0-15) which will be used as transparent when sprites are

### SPRITE SHOW [#]n, x,y, layer [,options]

Displays sprite ‘n’ on the screen with the top left at coordinates ‘x’, ‘y’. Sprites will only collide with other sprites on the same layer, layer zero, or with the screen edge. If a sprite is already displayed on the screen, then the SPRITE SHOW command acts to move the sprite to the new location. The display background is stored as part of the command and will be replaced when the sprite is hidden or moved further. The parameter ‘options’ is optional and can be set as follows: bit 0 set - mirrored left to right bit 1 set - mirrored top to bottom bit 2 set - black pixels not treated as transparent default is 0

### SPRITE SHOW SAFE [#]n, x,y, layer [,orientation] [,ontop]

Shows a sprite and automatically compensates for any other sprites that overlap it. If the sprite is not already being displayed the command acts exactly the same as SPRITE SHOW. If the sprite is already shown it is moved and remains in its position relative to other sprites based on the original order of writing. i.e. if sprite 1 was written before sprite 2 and it is moved to overlap sprite 2 it will display under sprite 2. If the optional "ontop" parameter is set to 1 then the sprite moved will become the newest sprite and will sit on top of any other sprite it overlaps. Refer to SPRITE SHOW for details of the orientation parameter.

### SPRITE SWAP [#]n1, [#]n2 [,orientation]

Replaces the sprite ‘n1’ with the sprite ‘n2’. The sprites must have the same width and height and ‘n1’ must be displayed or an error will be generated. Refer to SPRITE SHOW for details of the orientation parameter. The replacement sprite inherits the background from the original as well as its position in the list of order drawn.
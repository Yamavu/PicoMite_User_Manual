### BLIT MEMORY address, x, y [,col]

Copies an area of memory treated as a packed array of colour nibbles to the current graphical output as specified by `FRAMEBUFFER WRITE`. 

The colour is specified as a number between 0 and 15 representing:

black, blue, myrtle, cobalt, midgreen, cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white

The first word of the area of memory starting at `address%` must contain the width and height of the area to be copied as 16-bit integers with the width as the bottom 16 bits. The address must be aligned to a word boundary (divisible by 4).

If the optional parameter `col` is specified then that specific colour is not copied.

If the top bit of either the width or height is set to 1 then the colour data is treated as compressed (the remaining 15 bits are used as the width and/or height). The compression algorithm is simple, each byte contains a count in the bottom nibble (`1`-`15`) and a colour in the top nibble (`0`-`15`). In the event that more than 15 pixels are the same colour additional bytes are used for that colour.

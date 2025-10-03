### TILE x, y [,foreground] [,background] [,nbr_tiles_wide] [,nbr_tiles_high]

*VGA OR HDMI VERSIONS MODE 1 ONLY*

Sets the colour for one or more tiles on the screen. When in monochrome mode by default the video screen is split up into 80x40 tiles each 8x12 pixels. This matches font 1 and allows full colour coding in the editor in monochrome mode. Each tile can have a different foreground and background named colour assigned to it from the following: white, yellow, lilac, brown, fuchsia, rust, magenta, red, cyan, green, cerulean, midgreen, cobalt, myrtle, blue and black. 'x' and 'y' are the coordinates of the start block (0-79, 0-39) 'foreground ' and 'background' are the new colours selected. 'nbr_tiles_wide' and 'nbr_tiles_high' are the number of tiles to change. The change is instant and does not affect the text or graphics currently displayed in the tiles (just the colours).

### TILE HEIGHT n

Sets the height of the tiles. ‘n’ can be between 12 and 480 (RP2040) or between 8 and 480 (RP2350)
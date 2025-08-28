## BLIT WRITE [#]b, x, y [,mode]

BLIT WRITE will copy the memory buffer '#b' to the display. The destinationcoordinate is 'x' and 'y'.The optional 'mode' parameter defaults to 0 and specifies how the stored imagedata is changed as it is written out. It is the bitwise AND of the followingvalues: &B001 = mirrored left to right &B010 = mirrored top to bottom &B100 = don't copy transparent pixels
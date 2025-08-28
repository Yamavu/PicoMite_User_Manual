## SPRITE WRITE [#]b, x, y [,mode]

Will copy sprite '#b' to the display. The destination coordinate is 'x' and 'y'.The optional 'mode' parameter defaults to 4 and specifies how the stored imagedata is changed as it is written out. It is the bitwise AND of the followingvalues: &B001 = mirrored left to right &B010 = mirrored top to bottom &B100 = don't copy transparent pixels
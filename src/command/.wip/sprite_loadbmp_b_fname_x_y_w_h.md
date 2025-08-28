## SPRITE LOADBMP [#]b, fname$ [,x] [,y] [,w] [,h]

Will load a blit buffer from a 24-bit bmp image file. 'x' and 'y' define the startposition in the image to start loading and 'w' and 'h' specify the width andheight of the area to be loaded.eg, SPRITE LOAD #1,"image1", 50,50,100,100 will load anarea of 100 pixels square with the top left had corner at 50, 50 from the imageimage1.bmp
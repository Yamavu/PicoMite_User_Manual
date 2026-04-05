### SPRITE LOADBMP [#]b, fname$ [,x] [,y] [,w] [,h]

Will load a blit buffer from a 24-bit bmp image file. `x` and `y` define the start position in the image to start loading and `w` and `h` specify the width and height of the area to be loaded. eg, SPRITE LOAD #1,"image1", 50,50,100,100 will load an area of 100 pixels square with the top left had corner at 50, 50 from the image image1.bmp

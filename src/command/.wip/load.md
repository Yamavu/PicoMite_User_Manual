

### LOAD file$ [,R]

Loads a program called ‘file$’ from the Flash Filesystem or SD Card into program memory. If the optional suffix ,R is added the program will be immediately run without prompting (in this case ‘file$’ must be a string constant). The RUN command does the same thing and allows a string variable to be used. If an extension is not specified “.BAS” will be added to the file name.

### LOAD CONTEXT [KEEP]

Restores the variable space to the previously saved state and optionally preserves the stored variables to allow a second LOAD if required. See also SAVE CONTEXT

### LOAD IMAGE file$ [, x] [, y]

Load a bitmapped image (BMP) from the Flash Filesystem or SD Card and display it on the display. ''file$' is the name of the file and 'x' and 'y' are the screen coordinates for the top left hand corner of the image. If the coordinates are not specified the image will be drawn at the top left hand position on the screen. If an extension is not specified “.BMP” will be added to the file name. All types of the BMP format are supported including black and white and true colour 24-bit images.

### LOAD JPG file$ [, x] [, y]

Load a jpg image from the Flash Filesystem or SD Card and display it on the display. ''file$' is the name of the file and 'x' and 'y' are the screen coordinates for the top left hand corner of the image. If the coordinates are not specified the image will be drawn at the top left hand position on the screen. If an extension is not specified “.JPG” will be added to the file name. Progressive jpg images are not supported.

### LOAD PNG fname$ [, x] [, y] [,transparent] [,alphacut]

Loads and displays a png file 'fname' If no extension is specified .png will be automatically added to the filename. The file must be in RGBA8888 format which is the normal default. If specified 'x' and 'y' indicate where on the display or framebuffer the image will appear. The optional parameter 'transparent' (defaults to 0) specifies one of the colour codes (0-15) which will be allocated to pixels in the png file with an alpha value less than 'alphacut' (defaults to 20). If 'transparent' is set to -1 the png image is written with pixels with an alpha value less than 'alphacut' missed completely.
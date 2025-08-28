## LOAD file$ [,R]

Loads a program called ‘file$’ from the Flash Filesystem or SD Card into programmemory.If the optional suffix ,R is added the program will be immediately run withoutprompting (in this case ‘file$’ must be a string constant). The RUN commanddoes the same thing and allows a string variable to be used.If an extension is not specified “.BAS” will be added to the file name.
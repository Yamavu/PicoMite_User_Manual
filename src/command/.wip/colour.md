

### COLOUR fore [, back] or

Sets the default colour for commands (PRINT, etc) that display on the on the attached LCD panel. 'fore' is the foreground colour, 'back' is the background

### COLOUR MAP inarray%(), outarray%() [,colourmap%()]

This command generates RGB888 colours in outarray% from colour codes (0- 15) in inarray%. If the optional colourmap% parameter is used this must be 16 elements long). In this case the values in inarray% are mapped to the colours for that index value in colourmap%
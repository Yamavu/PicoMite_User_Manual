

### MOUSE

For all variants of the command. In the case of USB firmware ‘channel’ is the USB port that the mouse is connected to (1-4). See MM.INFO(USB n) for more information. For PS2 firmware ‘channel’ is fixed at the value 2

### MOUSE INTERRUPT

'int' is a user defined subroutine that will be called when the left mouse button

### MOUSE INTERRUPT

Disables an interrupt on the left mouse button

### MOUSE SET channel, y- coord, y-coord [, wheel-count]

Sets the current position that will be returned by the mouse x, y and optionally wheel positions NON USB VERSIONS - ONLY FOR A PS2 MOUSE

### MOUSE OPEN channel,

Opens a connection to a PS2 mouse connected to the two specified pins. This

### MOUSE CLOSE channel

will error if OPTION MOUSE has been set.
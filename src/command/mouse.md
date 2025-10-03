## MOUSE

For all variants of the command. 

In the case of USB firmware `channel` is the USB port that the mouse is connected to (1-4). See M[M.INFO(USB n)](../predefined_read_only_variables.md#mminfousb-n) for more information. 

For PS2 firmware `channel` is fixed at the value `2`.

### MOUSE INTERRUPT ENABLE channel, int

`int` is a user defined subroutine that will be called when the left mouse button

### MOUSE INTERRUPT DISABLE channel

Disables an interrupt on the left mouse button

### MOUSE SET channel, x-coord, y-coord [, wheel-count]

Sets the current position that will be returned by the mouse x, y and optionally wheel positions.

### MOUSE OPEN channel, CLKpin, DATApin

*NON USB VERSIONS - ONLY FOR A PS2 MOUSE*

Opens a connection to a PS2 mouse connected to the two specified pins. This command can be used in a program to configure the mouse while the program is running as against OPTION MOUSE which permanently configures the mouse.

The `channel` parameter is included for compatibility with USB mouse functionality and must be set to 2. If a mouse is not connected you will get an error and the command can be called again once the mouse is connected


### MOUSE CLOSE channel

Closes access to the mouse and restores the pins to normal use. The command will error if [OPTION MOUSE](../option/mouse.md) has been set.

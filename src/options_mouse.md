# Mouse

## OPTION MOUSE CLKpin,
DATApin

*non USB firmware only*
Set the pins to be used to connect a PS2 mouse.

Using this command the mouse is automatically configured on boot and you can set up interrupts and read values with no additional commands. This is different from the `MOUSE OPEN` which only connects to a mouse while the program is running. The PS2 mouse *must* be is disabled.


## OPTION MOUSE DISABLE

Disables the automatic connection to a PS2 mouse and frees up the pins for normal usage.


## OPTION NOCHECK ON/OFF

This command, when set **ON**, disables the standard checking for interrupts and **ctrl-C** at the end of every command. Setting it to `ON` allows time critical processing to take place without risk of interruption.

However, the command should be used carefully or the program may only be stopped with a H/W reset.



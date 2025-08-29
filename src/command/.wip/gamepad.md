

### GAMEPAD COLOUR channel, colour

Changes the colour of the display panel on a PS4 controller on USB channel ‘channel’. ‘colour’ is set as a standard RGB888 value e.g. RGB(RED)

### GAMEPAD HAPTIC channel left, right

Causes the left and right vibration motors to operate on a PS4 controller on USB channel ‘channel’. ’left’ and ‘right’ must be a number between 0 (off) and 255 (maximum).

### GAMEPAD INTERRUPT

Enables interrupts on the button presses on a USB game controller. The

### GAMEPAD INTERRUPT

Disables interrupts from the gamepad on the channel specified

### GAMEPAD MONITOR

Use GAMEPAD MONITOR before plugging in a gamepad and when plugged in it will show the before and after report with each change of buttons

### GAMEPAD CONFIGURE vid,pid,i0,c0,i1,c1,i2,c2,i3,c3,i 4,c4,i5,c5,i6,c6,i7,c7,i8,c8,i9,c 9,i10,c10,i11,c11,i12,c12,i13,c 13,i14,c14,i15,c15

Use to configure a gamepad that isn’t supported by the firmware. Run the command before plugging in the gamepad. All 34 parameters are mandatory. In each case the i/c parameters define the index into the report and the bit number at that index for the data that corresponds to the relevant bit. See DEVICE(GAMEPAD n,B) for more information on bit usage (0-15)
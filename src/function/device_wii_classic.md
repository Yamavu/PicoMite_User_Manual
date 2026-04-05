### DEVICE(WII [CLASSIC] funct)

Returns data from a Wii Classic controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    LX the position of the analog left joystick x axis
    LY the position of the analog left joystick y axis
    RX the position of the analog right joystick x axis
    RY the position of the analog right joystick y axis
    L        the position of the analog left button
    R        the position of the analog right button
    B        a bitmap of the state of all the buttons. A bit will be set to 1 if the
             button is pressed.

    T        the ID code of the controller - should be hex &HA4200101
The button bitmap is as follows:
    BIT 0        Button R
    BIT 1        Button start
    BIT 2        Button home
    BIT 3        Button select
    BIT 4        Button L
    BIT 5        Button down cursor
    BIT 6        Button right cursor
    BIT 7        Button up cursor
    BIT 8        Button left cursor
    BIT 9        Button ZR
    BIT 10 Button x
    BIT 11 Button a
    BIT 12 Button y
    BIT 13 Button b
    BIT 14 Button ZL
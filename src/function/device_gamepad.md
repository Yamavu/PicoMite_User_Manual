### DEVICE(GAMEPAD channel, funct)

Returns data from a USB PS3 or PS4 controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    LX the position of the analog left joystick x axis
    LY the position of the analog left joystick y axis
    RX the position of the analog right joystick x axis
    RY the position of the analog right joystick y axis
    GX the reading from the X axis gyro (where supported)
    GY the reading from the Y axis gyro (where supported)
    GZ the reading from the Z axis gyro (where supported)
    AX the reading from the X axis accelerometer (where supported)
    AY the reading from the Y axis accelerometer (where supported)
    AZ the reading from the Z axis accelerometer (where supported)
    L        the position of the analog left button
    R        the position of the analog right button
    B        a bitmap of the state of all the buttons. A bit will be set to 1 if the
             button is pressed.

    T        the ID code of the controller
The button bitmap is as follows:
    BIT 0 Button R/R1
    BIT 1 Button start/options
    BIT 2 Button home
    BIT 3 Button select/share
    BIT 4 Button L/L1
    BIT 5 Button down cursor
    BIT 6 Button right cursor
    BIT 7 Button up cursor
    BIT 8 Button left cursor
    BIT 9 Right shoulder button 2/R2
    BIT 10 Button x/triangle
    BIT 11 Button a/circle
    BIT 12 Button y/square
    BIT 13 Button b/cross
    BIT 14 Left should button 2/L2
    BIT 15 Touchpad
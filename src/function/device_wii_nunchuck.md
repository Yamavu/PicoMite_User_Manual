### DEVICE(WII NUNCHUCK funct)

Returns data from a Wii Nunchuck controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    AX the x axis acceleration
    AY the y axis acceleration
    AZ the z axis acceleration
    JX the position of the joystick x axis
    JY the position of joystick y axis
    C       the state of the C button
    Z       the state of the Z button
    T       the ID code of the controller - should be hex &HA4200000
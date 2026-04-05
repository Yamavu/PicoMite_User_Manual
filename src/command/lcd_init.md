### LCD INIT d4, d5, d6, d7, rs, en

Initialise an LCD character display module for use. This command will work with most 1-line, 2-line or 4-line LCD modules that use the KS0066, HD44780 or SPLC780 controller (however this is not guaranteed).

'd4' to 'd7' are the I/O pins that connect to inputs D4 to D7 on the LCD module (inputs D0 to D3 should be connected to ground). 'rs' is the pin connected to the register select input on the module (sometimes called CMD). 'en' is the pin connected to the enable or chip select input on the module. The R/W input on the module should always be grounded.

The above I/O pins are automatically set to outputs by this command. When the module has been initialised data can be written to it using the LCD command.
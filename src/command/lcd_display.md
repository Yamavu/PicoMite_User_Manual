### LCD line, pos, text$

Display text on an LCD character display module that has been previously initialised with LCD INIT.

'line' is the line on the display (1 to 4) and 'pos' is the character location on the line (the first location is 1). 'text$' is a string containing the text to write to the LCD display.

'pos' can also be C8, C16, C20 or C40 in which case the line will be cleared and the text centred on a 8, 16, 20 or 40 character display. For example: LCD 1, C16, "Hello"
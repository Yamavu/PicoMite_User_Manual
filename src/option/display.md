## OPTION DISPLAY lines [,chars]

Set the characteristics of the display terminal used for the console. Both the `LIST` and `EDIT` commands need to know this information to correctly format the text for display.

`lines` is the number of lines on the display and `chars` is the width of the display in characters. The default is 24 lines x 80 chars and when changed this option will be remembered even when the power is removed. Maximum values are 100 lines and 240 chars.

This will send an ESC sequence to set the VT100 terminal to the matching size. TerraTerm, Putty and MMCC respond to this sequence
and set the terminal width (if the option is enabled in the terminal setup).

This option is not available if an LCD display is being used as the console.


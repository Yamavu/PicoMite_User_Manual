## OPTION KEYBOARD nn [,capslock] [,numlock] [,repeatstart] [,repeatrate]

Configure a keyboard. This can be used for console input and any characters typed will be available via any commands that read from the console (serial over USB).

`nn` is a two character code defining the keyboard layout. The choices are `US` for the standard keyboard layout in the USA, Australia and New Zealand and `UK` for the United Kingdom, `GR` for Germany, `FR` for France, `BR` for Brazil and `ES` for Spain.

The optional parameters `capslock` and `numlock` are true/false integers that set the initial state of the keyboard (default is 0 and 1).

The optional parameters `repeatstart` and `repeatrate` set the time for the first repeat of a key that is held down and subsequent repeats.

For a USB keyboard they are `100` to 2000mSec and `25` to 2000mSec. 

For a PS2 keyboard they are `0` to `3` indicating 250mSec, 500mSec, 750mSec and 1000mSec (default is `1`) and `0` to `31` indicating 33mSec to 500mSec as per the PS2 keyboard specification (default is `12` or 100mSec).

*This command must be entered at the command line and will cause a reboot.*
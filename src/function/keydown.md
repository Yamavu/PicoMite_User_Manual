### KEYDOWN(n)

Return the decimal ASCII value of the USB keyboard key that is currently held
down or zero if no key is down. The decimal values for the function and arrow
keys are listed in Appendix F.

This function will report multiple simultaneous key presses and the parameter
`n` is the number of the keypress to report. KEYDOWN(0) will return the
number of keys being pressed
For example, if "c", "g" and "p" are pressed simultaneously KEYDOWN(0)
will return 3, KEYDOWN(1) will return 99, KEYDOWN(2) will return 103,
etc. The keys do not need to be pressed simultaneously and will report in the
order pressed. Taking a finger off a key will promote the next key pressed to
#1.

The first key (`n` = 1) is entered in the keyboard buffer (accessible using
INKEY$) while keys 2 to 6 can only be accessed via this function. Using this
function will clear the console input buffer.

KEYDOWN(7) will give any modifier keys that are pressed. These keys do not
add to the count in keydown(0)
The return value is a bitmask as follows:
lalt = 1, lctrl = 2, lgui = 4, lshift = 8, ralt = 16, rctrl = 32, rgui = 64, rshift = 128
KEYDOWN(8) will give the current status of the lock keys. These keys do not
add to the count in keydown(0)
The return value is a bitmask as follows:
caps_lock = 1, num_lock = 2, scroll_lock = 4
Note that some keyboards will limit the number of active keys that they can
report on.

### PIN( pin )

Returns the value on the external I/O `pin`. Zero means digital low, 1 means
digital high and for analogue inputs it will return the measured voltage as a
floating point number.

Frequency inputs will return the frequency in Hz. A period input will return
the period in milliseconds while a count input will return the count since reset
(counting is done on the positive rising edge). The count input can be reset to
zero by resetting the pin to counting input (even if it is already so configured).

When a pin is configured as an output this function will return the value of the
output setting (ie, high or low). Also see the SETPIN and PIN() = commands.

Refer to the chapter Using the I/O pins for a general description of the
PicoMite's input/output capabilities.


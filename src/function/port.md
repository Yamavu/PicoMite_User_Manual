### PORT(start, nbr [,start, nbr]…)

Returns the value of a number of I/O pins in one operation.

`start` is an I/O pin number and its value will be returned as bit 0. `start`+1 will be
returned as bit 1, `start`+2 will be returned as bit 2, and so on for `nbr` number of
bits. I/O pins used must be numbered consecutively and any I/O pin that is
invalid or not configured as an input will cause an error. The start/nbr pair can be
repeated up to 25 times if additional groups of input pins need to be added.

This function will also return the output state of a pin configured as an output.

This can be used to conveniently communicate with parallel devices like
memory chips. Any number of I/O pins (and therefore bits) can be used from 1
to the number of I/O pins on the chip.

See the PORT command to simultaneously output to a number of pins.


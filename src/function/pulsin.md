### PULSIN( pin, polarity ) or PULSIN( pin, polarity, t1 ) or PULSIN( pin, polarity, t1, t2 )

Measures the width of an input pulse from 1µs to 1 second with 0.1µs
resolution.

`pin` is the I/O pin to use for the measurement, it must be previously configured as a digital input.

`polarity` is the type of pulse to measure, if zero the function will return the width of the next negative pulse, if non zero it will measure the next positive pulse.

`t1` is the timeout applied while waiting for the pulse to arrive, `t2` is the timeout used while measuring the pulse. Both are in microseconds (µs) and are optional. 

If `t2` is omitted the value of `t1` will be used for both timeouts. If both `t1` and `t2` are omitted then the timeouts will be set at 100000 (i.e. 100ms).

This function returns the width of the pulse in microseconds (µs) or -1 if a
timeout has occurred. The measurement is accurate to ±0.5% and ±0.5µs.

Note that this function will cause the running program to pause while the
measurement is made and interrupts will be ignored during this period.


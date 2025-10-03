.wip


### SETTICK period, target [, nbr]

This will setup a periodic interrupt (or "tick"). Four tick timers are available ('nbr' is 1, 2, 3 or 4). 'nbr' is optional and if not specified timer number 1 will be used. The time between interrupts is ‘period’ milliseconds and ‘target' is the interrupt subroutine which will be called when the timed event occurs. The period can range from 1 to 2147483647 ms (about 24 days). These interrupts can be disabled by setting ‘period’ to zero (i.e. SETTICK 0, 0, 3 will disable tick timer number 3).

### SETTICK PAUSE, target [, nbr] or

Pause or resume the specified timer. When paused the interrupt is delayed but the current count is maintained.

### SETTICK RESUME, target [, nbr]


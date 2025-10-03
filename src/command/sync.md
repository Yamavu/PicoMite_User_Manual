.wip


### SYNC time% [,period] or

The SYNC command allows the user to implement very precisely timed repeated actions (1-2 microseconds accuracy).

### SYNC

To enable this the command is first called with the parameter time%. This sets up a repeating clock for time% microseconds. The optional parameter ‘period’ modifies the time and can be “U” for microseconds, “M” for milliseconds or “S” for seconds. Once the clock is set up the program is synchronised to it using the SYNC command without parameters. This waits for the clock period to expire. For periods below 2 ms this is non-interruptible. Above 2 ms the program will respond to Ctrl-C but not any MMBasic interrupts. Typical use is to set the clock outside of a loop and then at the top of the loop call the SYNC command without parameters. This means the contents of the loop will be executed exactly once for each clock period set. For example, the following would drive a servo with the required precise 50Hz timing: SYNC 20, M DO SYNC PULSE GP0,n LOOP
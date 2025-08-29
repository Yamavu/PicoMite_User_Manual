

### PIN( pin ) = value

For a ‘pin’ configured as digital output this will set the output to low (‘value’ is zero) or high (‘value’ non-zero). You can set an output high or low before it is configured as an output and that setting will be the default output when the SETPIN command takes effect. See the function PIN() for reading from a pin and the command SETPIN for configuring it. Refer to the chapter Using the I/O pins for a general description of the PicoMite firmware's input/output capabilities.

### PIN

Period input 'option' can be used to specify the number of input cycles to average the period measurement over. It can be any number between 1 and 10000. The PIN() function will always return the average period of one cycle correctly scaled in ms regardless of the number of cycles used for the average. If 'option' is omitted the period of just one cycle will be used. The pins can be GP6, GP7, GP8 or GP9 (can be changed with OPTION COUNT).
## ON ERROR

This controls the action taken if an error occurs while running a program and applies to all errors discovered by MMBasic including syntax errors, wrong data, missing hardware, etc.


### ON ERROR ABORT or

Display an error message, abort the program and return to the command prompt. 

*This is the normal behaviour and is the default when a program starts running.*


### ON ERROR IGNORE or

ON ERROR IGNORE will cause any error to be ignored.

*ON ERROR IGNORE can make it very difficult to debug a program so it is strongly recommended that only ON ERROR SKIP be used.*

### ON ERROR SKIP [nn] or

ON ERROR SKIP will ignore an error in a number of commands (specified by the number `nn`) executed following this command. 

`nn` is optional, the default if not specified is one. After the number of commands has completed (with an error or not) the behaviour of MMBasic will revert to ON ERROR ABORT. 

If an error occurs and is ignored/skipped the read only variable [MM.ERRNO](predefined_read_only_variables.md#mmerrno) will be set to non zero and [MM.ERRMSG$](predefined_read_only_variables.md#mmerrmsg) will be set to the error message that would normally be generated.


### ON ERROR CLEAR

[MM.ERRNO](predefined_read_only_variables.md#mmerrno) is reset to zero. [MM.ERRMSG$](predefined_read_only_variables.md#mmerrmsg) is reset to an empty string. 
 
They are also cleared when the program is run and when ON ERROR IGNORE and ON ERROR SKIP are used. 

## ON KEY

### ON KEY target or

The first version of the command sets an interrupt which will call 'target' user defined subroutine whenever there is one or more characters waiting in the serial console input buffer.

### ON KEY ASCIIcode, target

Note that all characters waiting in the input buffer should be read in the interrupt subroutine otherwise another interrupt will be automatically generated as soon as the program returns from the interrupt. The second version allows you to associate an interrupt routine with a specific key press. This operates at a low level for the serial console and if activated the key does not get put into the input buffer but merely triggers the interrupt. It uses a separate interrupt from the simple ON KEY command so can be used at the same time if required. In both variants, to disable the interrupt use numeric zero for the target, i.e.: ON KEY 0. or ON KEY ASCIIcode, 0

## ON PS2

This triggers an interrupt whenever the PicoMite firmware sees a message from the PS2 interface.

### ON PS2 target

Use MM.info(PS2) to report the raw message received. This allows the programmer to trap both keypress and release. See https://wiki.osdev.org/PS/2_Keyboard for the scan codes (Set 2).

### ON ERROR ABORT

This controls the action taken if an error occurs while running a program and applies to all errors discovered by MMBasic including syntax errors, wrong data, missing hardware, etc.

Display an error message, abort the program and return to the command prompt. 

*This is the normal behaviour and is the default when a program starts running.*


### ON ERROR IGNORE

ON ERROR IGNORE will cause any error to be ignored.

*ON ERROR IGNORE can make it very difficult to debug a program so it is strongly recommended that only ON ERROR SKIP be used.*


### ON ERROR SKIP [nn]

ON ERROR SKIP will ignore an error in a number of commands (specified by the number `nn`) executed following this command. 

`nn` is optional, the default if not specified is one. After the number of commands has completed (with an error or not) the behaviour of MMBasic will revert to ON ERROR ABORT. 

If an error occurs and is ignored/skipped the read only variable [MM.ERRNO](predefined_read_only_variables.md#mmerrno) will be set to non zero and [MM.ERRMSG$](predefined_read_only_variables.md#mmerrmsg) will be set to the error message that would normally be generated.


### ON ERROR CLEAR

[MM.ERRNO](predefined_read_only_variables.md#mmerrno) is reset to zero. [MM.ERRMSG$](predefined_read_only_variables.md#mmerrmsg) is reset to an empty string. 
 
They are also cleared when the program is run and when ON ERROR IGNORE and ON ERROR SKIP are used. 


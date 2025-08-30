

### VAR SAVE var [, var]…

`VAR SAVE` will save one or more variables to non-volatile flash memory where they can be restored later (normally after a power interruption).

`var` can be any number of numeric or string variables and/or arrays. Arrays are specified by using empty brackets. For example: var() The `VAR SAVE` command can be used repeatedly. Variables that had been
previously saved will be updated with their new value and any new variables (not previously saved) will be added to the saved list for later restoration.

The storage space available to this command is 16KB.

Be aware that string arrays can rapidly use up all the memory allocated to this command. The `LENGTH` qualifier can be used when a string array is declared to reduce the size of the array (see the [`DIM` command](dim.md)). This is not needed for ordinary string variables. 

The saved variables will be automatically cleared by a firmware upgrade, by the `NEW` command or when a new program is loaded via `AUTOSAVE`, `XMODEM`, etc.

### VAR RESTORE


`VAR RESTORE` will retrieve the previously saved variables and insert them (and their values) into the variable table. 

Normally the `VAR RESTORE` command is placed at the start of the program so that previously saved variables are restored and immediately available to the program when it starts.

Using `VAR RESTORE` without a previous save will have no effect and will not generate an error. 

If, when using `RESTORE`, a variable with the same name already exists its value will be overwritten. 

Saved arrays must be declared (using `DIM`) before they can be restored. 


### VAR CLEAR

`VAR CLEAR` will erase all saved variables. 

This command is normally used to save calibration data, options, and other data which does not change often but needs to be retained across a power interruption.

The saved variables will be automatically cleared by a firmware upgrade, by the `NEW` command or when a new program is loaded via `AUTOSAVE`, `XMODEM`, etc.


### CALL usersubname$ [,usersubparameters,..]

This is an efficient way of programmatically calling user defined subroutines.
 
In many cases it can allow you to get rid of complex `SELECT` and `IF THEN ELSEIF ENDIF` clauses and is processed in a much more efficient way.

The `usersubname$` can be any string or variable or function that resolves to the name of a normal user subroutine (not an in-built command).

The `usersubparameters` are the same parameters that would be used to call the
subroutine directly.

A typical use could be writing any sort of emulator where one of a large number of subroutines should be called depending on some variable. It also allows a way of passing a subroutine name to another subroutine or function as a variable.

See also the [CALL() function](../function/call.md).
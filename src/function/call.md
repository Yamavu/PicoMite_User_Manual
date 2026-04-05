### CALL(userfunname$, [,userfunparameters,..])

This is an efficient way of programmatically calling user defined functions.

(See also the CALL command). In many cases it can be used to eliminate
complex SELECT and IF THEN ELSEIF ENDIF clauses and is processed in a
much more efficient manner.

`userfunname$` can be any string or variable or function that resolves to the
name of a normal user function (not an in-built command).

`userfunparameters` are the same parameters that would be used to call the
function directly.

A typical use for this command could be writing any sort of emulator where
one of a large number of functions should be called depending on a some
variable. It also provides a method of passing a function name to another
subroutine or function as a variable.




### BYTE(var$, byteno)=value

 Sets a specific byte in a string to an integer value. `value` can be in the range `0`-`255`.
 
 The `byteno` can be between `1` and the current length of the string variable.
 
 This is the equivalent of `MID$(var$,byteno,1)=CHR$(value)` but executes much faster. 
 
 See also the [BYTE function](../function/byte.md).
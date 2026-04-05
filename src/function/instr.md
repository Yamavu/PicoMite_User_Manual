### INSTR( [start-position,] string-searched$, string- pattern$ [,size] )

Returns the position at which `string-pattern$` occurs in `string-searched$`,
beginning at `start-position`. If `start-position` is not provided it will default to 1.

Both the position returned and `start-position` use 1 for the first character, 2 for
the second, etc.

The function returns zero if `string-pattern$` is not found.

If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.


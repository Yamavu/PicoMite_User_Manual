### EVAL( string$ )

Will evaluate `string$` as if it is a BASIC expression and return the result.

`string$` can be a constant, a variable or a string expression. The expression can
use any operators, functions, variables, subroutines, etc that are known at the
time of execution. The returned value will be an integer, float or string
depending on the result of the evaluation.

For example: S$ = "COS(RAD(30)) * 100" : PRINT EVAL(S$)
Will display: 86.6025

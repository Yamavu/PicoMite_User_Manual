### CHOICE(condition, ExpressionIfTrue, ExpressionIfFalse)

This function allows you to do simple either/or selections more efficiently and
faster than using IF THEN ELSE ENDIF clauses.

The condition is anything that will resolve to nonzero (true) or zero (false).

The expressions are anything that you could normally assign to a variable or
use in a command and can be integers, floats or strings.

Examples:
- `PRINT CHOICE(1, "hello","bye")` will print `"Hello"`
- `PRINT CHOICE (0, "hello","bye")` will print `"Bye"`
- `a=1 : b=1 : PRINT CHOICE (a=b, 4, 5)` will print `4`


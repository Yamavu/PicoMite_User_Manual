### STATIC variable [, variables]

Defines a list of variable names which are local to the subroutine or function.

These variables will retain their value between calls to the subroutine or function (unlike variables created using the [LOCAL](./local.md) command).

This command uses exactly the same syntax as [DIM](./dim.md). The only difference is
that the length of the variable name created by `STATIC` and the length of the
subroutine or function name added together cannot exceed 31 characters.

Static variables can be initialised to a value. This initialisation will take effect
only on the first call to the subroutine (not on subsequent calls).

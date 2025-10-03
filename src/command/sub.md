### SUB xxx (arg1 [,arg2, …]) <br>&lt;statements> <br>&lt;statements> <br>END SUB

Defines a callable subroutine. 

This is the same as adding a new command to MMBasic while it is running your program. 

`xxx` is the subroutine name and it must meet the specifications for naming a variable.

`arg1`, `arg2`, etc are the arguments or parameters to the subroutine. An array is
specified by using empty brackets. i.e. arg3(). 

The type of the argument can be specified by using a type suffix (i.e. arg1$) or by specifying the type using `AS` &lt;type> (i.e. `arg1 AS STRING`).

Arguments in the caller's list that are a variable and have the correct type will be passed by reference to the subroutine. This means that any changes to the corresponding argument in the subroutine will also be copied to the caller's variable and therefore may be accessed after the subroutine has ended. 

The argument can be prefixed with `BYVAL` which will prevent this mechanism and cause only the value to be used. Alternatively, the prefix `BYREF` instructs MMBasic that a reference is required and an error will be generated if that cannot be done.

Arrays are passed by specifying the array name with empty brackets (eg, arg()) and are always passed by reference and must be the correct type.

Every definition must have one `END SUB` statement. When this is reached the program will return to the next statement after the call to the subroutine. The command `EXIT SUB` can be used for an early exit.

You use the subroutine by using its name and arguments in a program just as you would a normal command. For example: `MySub a1, a2`

When the subroutine is called each argument in the caller is matched to the argument in the subroutine definition. These arguments are available only inside the subroutine. Subroutines can be called with a variable number of arguments. Any omitted arguments in the subroutine's list will be set to zero or a null string.

Arguments in the caller's list that are a variable and have the correct type will be passed by reference to the subroutine. This means that any changes to the corresponding argument in the subroutine will also be copied to the caller's variable and therefore may be accessed after the subroutine has ended. The argument can be prefixed with `BYVAL` which will prevent this mechanism and cause only the value to be used. Alternatively, the prefix `BYREF` instructs MMBasic that a reference must be used and an error will occur if that cannot be done.

Arrays are passed by specifying the array name with empty brackets (eg, arg()) and are always passed by reference.

Brackets around the argument list in both the caller and the definition are optional.
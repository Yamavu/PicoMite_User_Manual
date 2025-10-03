.wip


### END CSUB

The first 'hex' word is a 32 bit word which is the offset in bytes from the start of the CSUB to the entry point of the embedded routine (usually the function main()). The following hex words are the compiled binary code for the module. These are automatically programmed into MMBasic when the program is saved. Each 'hex' must be exactly eight hex digits representing the bits in a 32-bit word and be separated by one or more spaces or new lines. The command must be terminated by a matching END CSUB. Any errors in the data format will be reported when the program is run. During execution MMBasic will skip over any CSUB commands so they can be placed anywhere in the program. The type of each parameter can be specified in the definition. For example: CSUB MySub integer, integer, string This specifies that there will be three parameters, the first two being integers and the third a string. Note:  Up to ten arguments can be specified ('arg1', 'arg2', etc).  If a variable or array is specified as an argument the C routine will receive a pointer to the memory allocated to the variable or array and the C routine can change this memory to return a value to the caller. In the case of arrays, they should be passed with empty brackets eg, arg(). In the CSUB the argument will be supplied as a pointer to the first element of the array.  Constants and expressions will be passed to the embedded C routine as pointers to a temporary memory space holding the value.

### END DEFINEFONT

See the Embedded Fonts folder in the PicoMite firmware distribution zip file for a selection of embedded fonts and a full description of how to create them. '#Nbr' is the font's reference number (from 1 to 16). It can be the same number as a built in font and in that case it will replace the built in font. Each 'hex' must be exactly eight hex digits and be separated by spaces or new lines from the next.  Multiple lines of 'hex' words can be used with the command terminated by a matching END DEFINEFONT.  Multiple embedded fonts can be used in a program with each defining a different font with a different font number.  During execution MMBasic will skip over any DEFINEFONT commands so they can be placed anywhere in the program.  Any errors in the data format will be reported when the program is saved.

### END [noend] or

End the running program and return to the command prompt. If a subroutine named MM.END exists in the program it will be executed whenever the program ends with an actual or implied END command. It is not executed if

### END cmd$

the program ends with the break character (ie, Ctrl-C). The optional parameter ‘noend’ can be used to block execution of the MM.END subroutine eg, “END noend” if 'cmd$' is specified then it will be executed as though at the command prompt after the program finishes. Note: if "END cmd$" is used but a subroutine MM.END exists it will be executed and cmd$ ignored.

### END CSUB

Marks the end of a C subroutine. See the CSUB command. Each CSUB must have one and only one matching END CSUB statement.

### END FUNCTION

Marks the end of a user defined function. See the FUNCTION command. Each function must have one and only one matching END FUNCTION statement. Use EXIT FUNCTION if you need to return from a function from within its body.

### END IF

### END FUNCTION

definition. For example: FUNCTION xxx (arg1, arg2) AS STRING 'arg1', 'arg2', etc are the arguments or parameters to the function (the brackets are always required, even if there are no arguments). An array is specified by using empty brackets. i.e. arg3(). The type of the argument can be specified by using a type suffix (i.e. arg1$) or by specifying the type using AS <type> (i.e. arg1 AS STRING). The argument can also be another defined function or the same function if recursion is to be used (the recursion stack is limited). To set the return value of the function you assign the value to the function's name. For example: FUNCTION SQUARE(a) SQUARE = a * a END FUNCTION Every definition must have one END FUNCTION statement. When this is reached the function will return its value to the expression from which it was called. The command EXIT FUNCTION can be used for an early exit. You use the function by using its name and arguments in a program just as you would a normal MMBasic function. For example: PRINT SQUARE(56.8) When the function is called each argument in the caller is matched to the argument in the function definition. These arguments are available only inside the function. Functions can be called with a variable number of arguments. Any omitted arguments in the function's list will be set to zero or a null string. Arguments in the caller's list that are a variable and have the correct type will be passed by reference to the function. This means that any changes to the corresponding argument in the function will also be copied to the caller's variable and therefore may be accessed after the function has ended. The argument can be prefixed with BYVAL which will prevent this mechanism and cause only the value to be used. Alternatively, the prefix BYREF instructs MMBasic that a reference is required and an error will be generated if that cannot be done. Arrays are passed by specifying the array name with empty brackets (eg, arg()) and are always passed by reference and must be the correct type. You must not jump into or out of a function using commands like GOTO. Doing so will have undefined side effects including ruining your day.

### END SELECT

If 'value' cannot be matched with a 'testexp' it will be automatically matched to the CASE ELSE. If CASE ELSE is not present the program will not execute any <statements> and continue with the code following the END SELECT. When a match is made the <statements> following the CASE statement will be executed until END SELECT or another CASE is encountered when the program will then continue with the code following the END SELECT.

### END SELEC

T

### END SUB

variable. 'arg1', 'arg2', etc are the arguments or parameters to the subroutine. An array is specified by using empty brackets. i.e. arg3(). The type of the argument can be specified by using a type suffix (i.e. arg1$) or by specifying the type using AS <type> (i.e. arg1 AS STRING). Arguments in the caller's list that are a variable and have the correct type will be passed by reference to the subroutine. This means that any changes to the corresponding argument in the subroutine will also be copied to the caller's
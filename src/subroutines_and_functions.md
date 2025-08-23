# Subroutines and Functions

## Subroutines and Functions

A program defined subroutine or function is simply a block of programming code that is contained within a
module and can be called from anywhere within your program. It is the same as if you have added your own
command or function to the language.

### Subroutines

A subroutine acts like a command and it can have arguments (sometimes called a parameter list). In the
definition of the subroutine they look like this:

```basic
SUB MYSUB arg1, arg2$, arg3
<statements>
<statements>
END SUB
```
And when you call the subroutine you can assign values to the arguments. For example:

```basic
MYSUB 23, "Cat", 55
```
Inside the subroutine `arg1` will have the value `23`, `arg2$` the value of `"Cat"`, and so on. The arguments act
like ordinary variables but they exist only within the subroutine and will vanish when the subroutine ends. You
can have variables with the same name in the main program and they will be hidden by the arguments defined
for the subroutine.

When calling a subroutine you can supply less than the required number of values and in that case the missing
values will be assumed to be either zero or an empty string. You can also leave out a value in the middle of the
list and the same will happen. For example:

```basic
MYSUB 23, , 55
```

Will result in `arg2$` being set to the empty string `""`.
Rather than using the type suffix (eg, the `$` in `arg2$`) you can use the suffix `AS <type>` in the definition of the
subroutine argument and then the argument will be known as the specified type, even when the suffix is not
used. For example:

```basic
SUB MYSUB arg1, arg2 AS STRING, arg3
IF arg2 = "Cat" THEN …
END SUB
```

Inside a subroutine you can define a variable using `LOCAL` (which has the same syntax as `DIM`). This variable
will only exist within the subroutine and will vanish when the subroutine exits.


### Functions

Functions are similar to subroutines with the main difference being that the function is used to return a value in
an expression. The rules for the argument list in a function are similar to subroutines. The only difference is
that brackets are required around the argument list when you are calling a function, even if there are no
arguments (brackets are optional when calling a subroutine).

To return a value from the function you assign a value to the function's name within the function. If the function's name is terminated with a $, a % or a ! the function will return that type, otherwise it will return whatever the `OPTION DEFAULT` is set to. You can also specify the type of the function by adding `AS <type>` to the end of the function definition.

For example:

```basic
FUNCTION Fahrenheit(C) AS FLOAT
Fahrenheit = C * 1.8 + 32
END FUNCTION
```

### Passing Arguments by Reference

If you use an ordinary variable (i.e., not an expression) as the value when calling a subroutine or a function, the
argument within the subroutine/function will point back to the variable used in the call and any changes to the
argument will also be made to the supplied variable. This is called passing arguments by reference.

For example, you might define a subroutine to swap two values, as follows:

```basic
SUB Swap a, b
LOCAL t
t = a
a = b
b = t
END SUB
```

In your calling program you would use variables for both arguments:

```basic
Swap nbr1, nbr2
```

And the result will be that the values of `nbr1` and `nbr2` will be swapped.

For this to work the type of the variable passed (eg, `nbr1`) and the defined argument (eg, a) must be the same (in the above example both default to float).

If you want to use an argument as a general purpose variable inside a subroutine or function (ie, change its value) you should prefix its definition with the keyword `BYVAL`. This instructs MMBasic to always use the value of the argument, even if it is a variable, and to never point back to the variable used in the call. This is because another user of your routine may unwittingly use a variable in their call and that variable could be "magically" changed by your routine if you did not use `BYVAL`.

### Passing Arrays

Single elements of an array can be passed to a subroutine or function and they will be treated the same as a normal variable. For example, this is a valid way of calling the Swap subroutine (discussed above):

```basic
Swap dat(i), dat(i + 1)
```

This type of construct is often used in sorting arrays.

You can also pass one or more complete arrays to a subroutine or function by specifying the array with empty brackets instead of the normal dimensions. For example, `a()`. In the subroutine or function definition the associated parameter must also be specified with empty brackets. The type (i.e., float, integer or string) of the argument supplied and the parameter in the definition must be the same.

In the subroutine or function the array will inherit the dimensions of the array passed and these must be respected when indexing into the array. If required the dimensions of the array could be passed as additional arguments to the subroutine or function or it could find these via the `BOUND()` function. The array is passed by reference which means that any changes made to the array within the subroutine or function will also apply to the supplied array.

For example, when the following is run the words `Hello World` will be printed out:

```basic
DIM MyStr$(5, 5)
MyStr$(4, 4) = "Hello" : MyStr$(4, 5) = "World"
Concat MyStr$()
PRINT MyStr$(0, 0)
SUB Concat arg$()
arg$(0,0) = arg$(4, 4) + " " + arg$(4, 5)
END SUB
```

### Early Exit

There can be only one `END SUB` or `END FUNCTION` for each definition of a subroutine or function. To exit
early from a subroutine (i.e., before the `END SUB` command has been reached) you can use the `EXIT SUB`
command. This has the same effect as if the program reached the `END SUB` statement. Similarly you can use
`EXIT FUNCTION` to exit early from a function.

### Recursion

Recursion is where a subroutine or function calls itself. You can do recursion in MMBasic but there are a
number of issues (these are a direct consequence of the limitations of microcontrollers and the BASIC
language):
* There is a fixed limit to the depth of recursion. In the PicoMite firmware this is 50 levels.
* If you have many arguments to the subroutine or function and many `LOCAL` variables (especially strings)
you could easily run out of memory before reaching the 50 level limit.
* Any `FOR…NEXT` loops and `DO…LOOP`s will be corrupted if the subroutine or function is recursively
called from within these loops.

### Examples

There is often the need for a special command or function to be implemented in MMBasic but in many cases
these can be constructed using an ordinary subroutine or function which will then act exactly the same as a built
in command or function.

For example, sometimes there is a requirement for a `TRIM` function which will trim specified characters from
the start and end of a string. The following provides an example of how to construct such a simple function in
MMBasic.

The first argument to the function is the string to be trimmed and the second is a string containing the
characters to trim from the first string. `RTrim$()` will trim the specified characters from the end of the string,
`LTrim$()` from the beginning and `Trim$()` from both ends.

* trim any characters in c$ from the start and end of s$

```basic
Function Trim$(s$, c$)
Trim$ = RTrim$(LTrim$(s$, c$), c$)
End Function
```

* trim any characters in c$ from the end of s$

```basic
Function RTrim$(s$, c$)
RTrim$ = s$
Do While Instr(c$, Right$(RTrim$, 1))
RTrim$ = Mid$(RTrim$, 1, Len(RTrim$) - 1)
Loop
End Function
```

* trim any characters in c$ from the start of s$

```basic
Function LTrim$(s$, c$)
LTrim$ = s$
Do While Instr(c$, Left$(LTrim$, 1))
LTrim$ = Mid$(LTrim$, 2)
Loop
End Function
```

As an example of using these functions:

```basic
S$ = "
****23.56700
PRINT Trim$(s$, " ")

"
```

Will give `"****23.56700"`

```basic
PRINT Trim$(s$, " *0")
```

Will give `"23.567"`

```basic
PRINT LTrim$(s$, " *0")
```

Will give `"23.56700"`

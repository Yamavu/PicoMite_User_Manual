## Functions

Functions are similar to subroutines with the main difference being that a function is used to return a
value in an expression. For example, if you wanted a function to convert a temperature from degrees
Celsius to Fahrenheit you could define:

```basic
FUNCTION Fahrenheit(C)
Fahrenheit = C * 1.8 + 32
END FUNCTION
```

Then you could use it in an expression:

```basic
Input "Enter a temperature in Celsius: ", t
PRINT "That is the same as" Fahrenheit(t) "F"
```

Or as another example:

```basic
IF Fahrenheit(temp) <= 32 THEN PRINT "Freezing"
```

You could also define the reverse:

```basic
FUNCTION Celsius(F)
Celsius = (F - 32) * 0.5556
END FUNCTION
```

As you can see, the function name is used as an ordinary local variable inside the subroutine. It is
only when the function returns that the value is made available to the expression that called it.

The rules for the argument list in a function are similar to subroutines. The only difference is that
parentheses are always required around the argument list when you are calling a function, even if
there are no arguments (parentheses are optional when calling a subroutine).

To return a value from the function you assign a value to the function's name within the function. If
the function's name is terminated with a type suffix (ie, $, a % or a !) the function will return that type

(string, integer or float), otherwise it will return whatever the `OPTION DEFAULT` is set to. For
example, the following function will return a string:

```basic
FUNCTION LVal$(nbr)
IF nbr = 0 THEN LVal$ = "False" ELSE LVal$ = "True"
END FUNCTION
```

You can explicitly specify the type of the function by using the AS keyword and then you do not need
to use a type suffix (similar to defining a variable using `DIM` ).

This is the above example rewritten to take advantage of this feature:

```basic
FUNCTION LVal(nbr) AS STRING
IF nbr = 0 THEN LVal = "False" ELSE LVal = "True"
END FUNCTION
```

In this case the type returned by the function LVal will be a string.

As for subroutines you can use most features of MMBasic within functions. This includes
`FOR…NEXT` loops, calling other functions and subroutines, etc. Also, the function will return to the
expression that called it when the `END FUNCTION` command is reached but you can also return early
by using the `EXIT FUNCTION` command.

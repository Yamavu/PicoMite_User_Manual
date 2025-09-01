## Subroutines

A subroutine is a block of programming code which is self contained (like a module) and can be
called from anywhere within your program. To your program it looks like a built in MMBasic
command and can be used the same. For example, assume that you need a command that would
signal an error by printing a message on the console. You could define the subroutine like this:

```basic
SUB ErrMsg
PRINT "Error detected"
END SUB
```

With this subroutine embedded in your program all you have to do is use the command ErrMsg
whenever you want to display the message. For example:

```basic
IF A < B THEN ErrMsg
```

The definition of a subroutine can be anywhere in the program but typically it is at the end. If
MMBasic runs into the definition while running your program it will simply skip over it.

The above example is fine enough but it would be better if a more useful message could be displayed,
one that could be customised every time the subroutine was called. This can be done by passing a
string to the subroutine as an argument (sometimes called a parameter).

In this case the definition of the subroutine would look like this:

```basic
SUB ErrMsg Msg$
PRINT "Error: " + Msg$
END SUB
```

Then, when you call the subroutine, you can supply the string to be printed on the command line of
the subroutine.

For example:

```basic
IF A < B THEN ErrMsg "Number too small"
```

When the subroutine is called like this the message "Error: Number too small" will be
printed on the console. Inside the subroutine Msg$ will have the value of "Number too small" when
called like this and it will be concatenated in the `PRINT` statement to make the full error message.

A subroutine can have any number of arguments which can be float, integer or string with each
argument separated by a comma.

Within the subroutine the arguments act like ordinary variables but they exist only within the
subroutine and will vanish when the subroutine ends. You can have variables with the same name in
the main program and they will be hidden within the subroutine and be different from arguments
defined for the subroutine.

The type of the argument to be supplied can be specified with a type suffix (ie, $, % or ! for string,
integer and float). For example, in the following the first argument must be a string and the second an
integer:

```basic
SUB MySub Msg$, Nbr%
…
END SUB
```

MMBasic will convert the supplied values if it can, so if your program supplied a floating point value
as the second argument MMBasic will convert it to an integer. If MMBasic cannot convert the value
it will display an error and return to the command prompt. For example, if you supplied a string for
the second argument your program will stop with an error.

You do not have to use the type suffixes, you can instead define the type of the arguments using the
`AS` keyword similar to the way it is used in the `DIM` command.

For example, the following is identical to the above example:

```basic
SUB MySub Msg AS STRING, Nbr AS INTEGER
…
END SUB
```

Of course, if you used only one variable type throughout the program and used `OPTION DEFAULT` 
to set that type you could ignore the question of variable types completely.

When a subroutine is called with an argument that is a variable (ie, not a constant or expression)
MMBasic will create a corresponding variable within the subroutine that points back to this variable.

Any changes to the variable representing the argument inside the subroutine will also change the
variable used in the call. This is called passing arguments by reference.

This is best explained by example:

```basic
DIM MyNumber = 5      ‘ set the variable to 5
CalcSquare MyNumber   ‘ the subroutine will square its value
PRINT MyNumber
END
SUB CalcSquare nbr    ‘ this will print the number 25
nbr = nbr * nbr       ‘ square the argument and pass it back
END SUB
```

The subroutine CalcSquare will take its argument, square it and write it back to the variable
representing the argument (nbr). Because the subroutine was called with a variable (MyNumber) the
variable nbr will point back to MyNumber and any change to nbr will also change MyNumber
accordingly. As a result the `PRINT` statement will output 25.

Passing arguments by reference is handy because it allows a subroutine to pass values back to the
code that called it. However, it could lead to trouble if a subroutine used the variable representing an
argument as a general purpose variable and changed its value. Then, if it were called with a variable as
an argument, that variable would be inadvertently changed. To avoid this, you should prefix its
definition with the keyword `BYVAL` . This instructs MMBasic to always use the value of the
argument, even if it is a variable, and to never point back to the variable used in the call.

When you call a subroutine you can omit some (or all) of the parameters and they will take the value
of zero (for floats or integers) or an empty string. This is handy as your subroutine can tell if a
parameter is missing and act accordingly.

For example, here is our subroutine to generate an error message but this version can be used without
specifying an error message as a parameter:

```basic
SUB ErrMsg Msg$
IF Msg$ = "" THEN
PRINT "Error detected"
ELSE
PRINT "Error: " + Msg$
ENDIF
END SUB
```

Within a subroutine you can use most features of MMBasic including calling other subroutines,
`IF … THEN` commands, `FOR…NEXT` loops and so on. However, one thing that you cannot do is
jump out of a subroutine using `GOTO` (if you do the result will be undefined and may cause your hair
to turn grey).

Normally the subroutine will exit when the `END SUB` command is reached but you can also terminate
the subroutine early by using the `EXIT SUB` command.



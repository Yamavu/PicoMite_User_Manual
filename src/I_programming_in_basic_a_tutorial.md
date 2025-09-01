# Programming in BASIC - A Tutorial

The BASIC language was introduced in 1964 by Dartmouth College in the USA as a computer
language for teaching programming and accordingly it is easy to use and learn. At the same time, it
has proved to be a competent and powerful programming language and as a result it became very
popular in the late 70s and early 80s. Even today some large commercial data systems are still written
in the BASIC language (primarily Pick Basic).

The BASIC interpreter used in the PicoMite firmware’s is called MMBasic and is a modern version of
the BASIC language which loosely emulates the Microsoft BASIC interpreter that was popular years
ago.

For a programmer the greatest advantage of BASIC is its ease of use. Some more modern languages
such as C and C++ can be truly mind bending but with BASIC you can start with a one line program
and get something sensible out of it. MMBasic is also powerful in that you can draw sophisticated
graphics, manipulate the external I/O pins to control other devices and communicate with other
devices using a range of built-in communications protocols.


{{#include programming_in_basic_a_tutorial/command_prompt.md}}
{{#include programming_in_basic_a_tutorial/if.md}}
{{#include programming_in_basic_a_tutorial/for.md}}
{{#include programming_in_basic_a_tutorial/multiplication_table.md}}
{{#include programming_in_basic_a_tutorial/do_loops.md}}
{{#include programming_in_basic_a_tutorial/console_input.md}}
{{#include programming_in_basic_a_tutorial/testing_prime_numbers.md}}
{{#include programming_in_basic_a_tutorial/arrays.md}}
{{#include programming_in_basic_a_tutorial/integer.md}}
{{#include programming_in_basic_a_tutorial/string.md}}
{{#include programming_in_basic_a_tutorial/dim.md}}
{{#include programming_in_basic_a_tutorial/const.md}}
{{#include programming_in_basic_a_tutorial/sub.md}}
{{#include programming_in_basic_a_tutorial/function.md}}
{{#include programming_in_basic_a_tutorial/local.md}}
{{#include programming_in_basic_a_tutorial/static.md}}
{{#include programming_in_basic_a_tutorial/calculate_days.md}}


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


## Local Variables

Variables that are created using `DIM` or that are just automatically created are called global variables.

This means that they can be seen and used anywhere in the program including within subroutines and
functions. However, inside a subroutine or function you will often need to use variables for various
tasks that are internal to the subroutine/function. In portable code you do not want the name you
chose for such a variable to clash with a global variable of the same name. To this end you can define
a variable using the `LOCAL` command within the subroutine/function.

The syntax for `LOCAL` is identical to the `DIM` command, this means that the variable can be an array,
you can set the type of the variable and you can initialise it to some value.

For example, this is our ErrMsg subroutine but this time it has been extended to use a local variable
for joining the error message strings.


```basic
SUB ErrMsg Msg$
LOCAL STRING tstr
tstr = "Error: " + Msg$
PRINT tstr
END SUB
```

The variable `tstr` is declared as `LOCAL` within the subroutine, which means that (like the argument
list) it will only exist within the subroutine and will vanish when the subroutine exits. You can have a
global variable called `tstr` in your main program and it will be different from the variable `tstr` in
the subroutine (in this case the global `tstr` will be hidden within the subroutine).

You should always use local variables for operations within your subroutine or function because they
help make the module much more self contained and portable.

## Static Variables
 `LOCAL` variables are reset to their initial values (normally zero `0` or an empty string `""`) every time the
subroutine or function starts, however there are times when you would like the variable to retain its
value between calls. This type of variable is defined with the `STATIC` command.

We can demonstrate how `STATIC` variables are useful by extending the ErrMsg subroutine to prevent
duplicated calls to the subroutine repeatedly displaying the same message. For example, our program
might call this subroutine from multiple places but if the message is the same in a number of
subsequent calls we would like to see the message just once.

This is our new subroutine:

```basic
SUB ErrMsg Msg$
STATIC STRING lastmsg
LOCAL STRING tstr
IF Msg$ <> lastmsg THEN
tstr = "Error: " + Msg$
PRINT tstr
lastmsg = Msg$
ENDIF
END SUB
```

To keep track of the last message displayed we use a static variable called lastmsg. This will hold
the text of the last message and we can compare it to the current message text to determine if it is
different and therefore should be printed. This would give just one message every time a call is made
with a duplicate message text.

The `STATIC` command uses exactly the same syntax as `DIM` . This means that you can define
different types of static variables including arrays and you can also initialise them to some value.

The static variable is created on the first time the `STATIC` command is encountered and it is
automatically set to zero (if a float or integer) or an empty string. On subsequent calls to the
subroutine or function MMBasic will recognise that the variable has already been created and it will
leave its value untouched (ie, whatever it was in the previous call). As with DIM you can also
initialise a static variable to some value. For example:

```basic
STATIC INTEGER var = 123
```

On the first call (when the variable is created) it will be initialised to 123 but on subsequent calls it
will keep whatever its value was previously set to.

Mostly static variables are used to keep track of the state of something while inside a subroutine or
function. A state is a record of something that has happened previously.

Examples include:

- Has the COM port already been opened?
- What steps in a sequence have we completed?
- What text has already been displayed?

Normally you will use global variables (created using `DIM` ) to track a state but sometimes you want
this to be contained within a module and this is where static variables are valuable. Just like `LOCAL` 
the use of `STATIC` helps to make your subroutines and functions more self contained and portable.

Calculate Days
We have covered a lot of programming commands and techniques so far in this tutorial and before we
finish it would be worth giving an example of how they work together. The following is an example
that uses many features of the BASIC language to calculate the number of days between two dates:

```basic
' Example program to calculate the number of days between two dates
OPTION EXPLICIT
OPTION DEFAULT NONE
DIM STRING s
DIM FLOAT d1, d2
DO
' main program loop
PRINT : PRINT "Enter the date as dd mmm yyyy"
PRINT " First date";
INPUT s
d1 = GetDays(s)
IF d1 = 0 THEN PRINT "Invalid date!" : CONTINUE DO
PRINT "Second date";
INPUT s
d2 = GetDays(s)
IF d2 = 0 THEN PRINT "Invalid date!" : CONTINUE DO
PRINT "Difference is" ABS(d2 - d1) " days"
LOOP
' Calculate the number of days since 1/1/1900
FUNCTION GetDays(d$) AS FLOAT
LOCAL STRING Month(11) =
("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
LOCAL FLOAT Days(11) = (0,31,59,90,120,151,181,212,243,273,304,334)
LOCAL FLOAT day, mth, yr, s1, s2
' Find the separating space character within a date
s1 = INSTR(d$, " ")
IF s1 = 0 THEN EXIT FUNCTION
s2 = INSTR(s1 + 1, d$, " ")
IF s2 = 0 THEN EXIT FUNCTION
' Get the day, month and year as numbers
day = VAL(MID$(d$, 1, s2 - 1)) - 1
IF day < 0 OR day > 30 THEN EXIT FUNCTION
FOR mth = 0 TO 11
IF LCASE$(MID$(d$, s1 + 1, 3)) = Month(mth) THEN EXIT FOR
NEXT mth
IF mth > 11 THEN EXIT FUNCTION
yr = VAL(MID$(d$, s2 + 1)) - 1900
IF yr < 1 OR yr >= 200 THEN EXIT FUNCTION
' Calculate the number of days including adjustment for leap years
GetDays = (yr * 365) + FIX((yr - 1) / 4)
IF yr MOD 4 = 0 AND mth >= 2 THEN GetDays = GetDays + 1
GetDays = GetDays + Days(mth) + day
END FUNCTION

```

Note that the line starting LOCAL STRING Month(11) has been wrapped around because of the
limited page width – it is one line as follows:

```basic
LOCAL STRING Month(11) = ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
```

This program works by getting two dates from the user at the console and then converting them to
integers representing the number of days since 1900. With these two numbers a simple subtraction
will give the number of days between them.

When this program is run it will ask for the two dates to be entered and you need to use the form of: `dd mmm yyyy`.

This screen capture shows what the running program will look like.

The main feature of the program is the defined function `GetDays()` which takes a string entered at the console, splits it into its day, month and year components then calculates the number of days since 1st January 1900.

This function is called twice, once for the first date and then again for the second date. It is then just a matter of subtracting one date (in days) from the other to get the difference in days.

We will not go into the detail of how the calculations are made (ie, handling leap years) as that can be left as an exercise for the reader. However, it is appropriate to point out some features of MMBasic
that are used by the program.

It demonstrates how local variables can be used and how they can be initialised. In the function `GetDays()` two arrays are declared and initialised at the same time. These are just a convenient method of looking up the names of the months and the cumulative number of days for each month.

Later in the function (the FOR loop) you can see how they make dealing with twelve different months quite efficient.

Another feature highlighted by this program is the string handling features of MMBasic. The `INSTR()` function is used to locate the two space characters in the date string and then later the MID$() function uses these to extract the day, month and year components of the date. The `VAL()` function is used to turn a string of digits (like the year) into a number that can be stored in a numeric variable.

Note that the value of a function is initialised to zero every time the function is called and unless it is set to some value it will return a zero value. This makes error handling easy because we can just exit the function if an error is discovered. It is then the responsibility of the calling program code to check for a return value of zero which signifies an error.

This program illustrates one of the benefits of using subroutines and functions which is that when written and fully tested they can be treated as a trusted "black box" that does not have to be opened.

For this reason functions like this should be the properly tested and then, if possible, left untouched (in case you add some error).

There are a few features of this program that we have not covered before. The first is the MOD operator which will calculate the remainder of dividing one number into another. For example, if you divided 4 into 15 you would have a remainder of 3 which is exactly what the expression 15 MOD 4 will return. The `ABS()` function is also new and will return its argument as a positive number (eg, ABS(-15) will return +15 as will ABS(15)).

The EXIT FOR command will exit a FOR loop even though it has not reached the end of its looping, EXIT FUNCTION will immediately exit a function even though execution has not reached the end of the function and CONTINUE DO will immediately cause the program to jump to the end of a DO loop and execute it again.

Why would this program be useful? Well some people like to count their age in days, that way every day is a birthday! You can calculate your age in days, just enter the date that you were born and today's date. That is not particularly useful but the program itself is valuable as it demonstrates many of the characteristics of programming in MMBasic. So, work your way through the program and review each section until you understand it – it should be a rewarding experience.

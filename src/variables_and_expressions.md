# Variables and Expressions

In MMBasic command names, function names, labels, variable names, file names, etc are not case sensitive, so
that "Run" and "RUN" are equivalent and "dOO" and "Doo" refer to the same variable.

## Variables

Variables can start with an alphabetic character or underscore and can contain any alphabetic or numeric
character, the period (.) and the underscore (_). They may be up to 31 characters long.
A variable name or a label must not be the same as a command, function or one of the following keywords:

```basic
THEN, ELSE, GOTO, GOSUB, TO, STEP, FOR, WHILE, UNTIL, LOAD, MOD, NOT, AND, OR, XOR, AS.
```

Eg, `step = 5` is illegal as `STEP` is a keyword.

MMBasic supports three types of variables:

1. Double Precision Floating Point.

   These can store a number with a decimal point and fraction (eg, `45.386`) however they will lose accuracy
   when more than 14 digits of precision are used. Floating point variables are specified by adding the
   suffix `!` to a variable's name (eg, `i!`, `nbr!`, etc). They are also the default when a variable is created
   without a suffix (eg, `i`, `nbr`, etc).

2. 64-bit Signed Integer.
   
   These can store positive or negative numbers with up to 19 decimal digits without losing accuracy but
   they cannot store fractions (i.e. the part following the decimal point). These are specified by adding the
   suffix `%` to a variable's name. For example, `i%`, `nbr%`, etc.

3. A String.

   A string will store a sequence of characters (eg, `"Tom"`). Each character in the string is stored as an eight
   bit number and can therefore have a decimal value of `0` to `255`. String variable names are terminated with
   a `$` symbol (eg, `name$`, `s$`, etc). Strings can be up to 255 characters long.

Note that it is illegal to use the same variable name with different types. Eg, using `nbr!` and `nbr%` in the
same program would cause an error.

Most programs use floating point variables for arithmetic as these can deal with the numbers used in typical
situations and are more intuitive than integers when dealing with division and fractions. So, if you are not
bothered with the details, always use floating point.


## Constants

Numeric constants may begin with a numeric digit (`0`-`9`) for a decimal constant, `&H` for a hexadecimal
constant, `&O` for an octal constant or `&B` for a binary constant. For example `&B1000` is the same as the
decimal constant `8`. Constants that start with `&H`, `&O` or `&B` are always treated as 64-bit unsigned integer
constants.
Decimal constants may be preceded with a minus (`-`) or plus (`+`) and may be terminated with `E` followed by an
exponent number to denote exponential notation. For example `1.6E+4` is the same as `16000`.
When a constant number is used it will be assumed that it is an integer if a decimal point or exponent is not
used. For example, `1234` will be interpreted as an integer while `1234.0` will be interpreted as a floating point
number.

String constants must be surrounded by double quote marks (`"`). Eg, `"Hello World"`.


## OPTION DEFAULT

A variable can be used without a suffix (i.e. `!`, `%` or `$`) and in that case MMBasic will use the default type of
floating point. For example, the following will create a floating point variable:

```basic
Nbr = 1234`
```

However. the default can be changed with the OPTION DEFAULT command. For example, `OPTION DEFAULT INTEGER` will specify that all variables without a specific type will be integer. So, the following
will create an integer variable:

```basic
OPTION DEFAULT INTEGER
Nbr = 1234
```

The default can be set to `FLOAT` (which is the default when a program is run), `INTEGER`, `STRING` or `NONE`. In the latter all variables must be specifically typed otherwise an error will occur.

The `OPTION DEFAULT` command can be placed anywhere in the program and changed at any time but good
practice dictates that if it is used it should be placed at the start of the program and left unchanged.


## OPTION EXPLICIT

By default MMBasic will automatically create a variable when it is first referenced. So, Nbr = 1234 will
create the variable and set it to the number 1234 at the same time. This is convenient for short and quick
programs but it can lead to subtle and difficult to find bugs in large programs. For example, in the third line of
this fragment the variable Nbr has been misspelt as Nbrs. As a consequence the variable Nbrs would be
created with a value of zero and the value of Total would be wrong.

```basic
Nbr = 1234
Incr = 2
Total = Nbrs + Incr
```

The `OPTION EXPLICIT` command tells MMBasic to not automatically create variables. Instead they must be
explicitly defined using the `DIM`, `LOCAL` or `STATIC` commands (see below) before they are used. The use of
this command is recommended to support good programming practice. If it is used it should be placed at the
start of the program before any variables are used.


## DIM and LOCAL

The `DIM` and `LOCAL` commands can be used to define a variable and set its type and are mandatory when the
`OPTION EXPLICIT` command is used.
The `DIM` command will create a global variable that can be seen and used throughout the program including
inside subroutines and functions. However, if you require the definition to be visible only within a subroutine
or function, you should use the `LOCAL` command at the start of the subroutine or function. `LOCAL` has
exactly the same syntax as `DIM`.
If `LOCAL` is used to specify a variable with the same name as a global variable then the global variable will be
hidden to the subroutine or function and any references to the variable will only refer to the variable defined by
the `LOCAL` command. Any variable created by `LOCAL` will vanish when the program leaves the subroutine.
At its simplest level `DIM` and `LOCAL` can be used to define one or more variables based on their type suffix or
the OPTION DEFAULT in force at the time. For example:

```basic
DIM nbr%, s$
```

But it can also be used to define one or more variables with a specific type when the type suffix is not used:
`DIM INTEGER nbr, nbr2, nbr3, etc`
In this case `nbr, nbr2, nbr3, etc` are all created as integers. When you use the variable within a program you do
not need to specify the type suffix. For example, `MyStr` in the following works perfectly as a string variable:

```basic
DIM STRING MyStr
MyStr = "Hello"
```

The `DIM` and `LOCAL` commands will also accept the Microsoft practice of specifying the variable's type after
the variable with the keyword "AS". For example:

```basic
DIM nbr AS INTEGER, s AS STRING
```

In this case the type of each variable is set individually (not as a group as when the type is placed before the list
of variables).

The variables can also be initialised while being defined. For example:

```basic
DIM INTEGER a = 5, b = 4, c = 3
DIM s$ = "World", i% = &H8FF8F
DIM msg AS STRING = "Hello" + " " + s$
```

The value used to initialise the variable can be an expression including user defined functions.
The `DIM` or `LOCAL` commands are also used to define an array and all the rules listed above apply when
defining an array. For example, you can use:

```basic
DIM INTEGER nbr(10), nbr2, nbr3(5,8)
```

When initialising an array the values are listed as comma separated values with the whole list surrounded by
brackets. For example:

```basic
DIM INTEGER nbr(5) = (11, 12, 13, 14, 15, 16)
```
or
```basic
DIM days(7) AS STRING = ("","Sun","Mon","Tue","Wed","Thu","Fri","Sat")
```

## STATIC
Inside a subroutine or function it is sometimes useful to create a variable which is only visible within the
subroutine or function (like a `LOCAL` variable) but retains its value between calls to the subroutine or function.
You can do this by using the `STATIC` command. `STATIC` can only be used inside a subroutine or function and
uses the same syntax as `LOCAL` and `DIM`. The difference is that its value will be retained between calls to the
subroutine or function (i.e. it will not be initialised on the second and subsequent calls).

For example, if you had the following subroutine and repeatedly called it, the first call would print 5, the
second 6, the third 7 and so on.

```basic
SUB Foo
    STATIC var = 5
    PRINT var
    var = var + 1
END SUB
```

Note that the initialisation of the static variable to `5` (as in the above example) will only take effect on the first
call to the subroutine. On subsequent calls the initialisation will be ignored as the variable had already been
created on the first call.

As with `DIM` and `LOCAL` the variables created with `STATIC` can be float, integers or strings and arrays of
these with or without initialisation. The length of the variable name created by `STATIC` and the length of the
subroutine or function name added together cannot exceed 31 characters.


## CONST
Often it is useful to define an identifier that represents a value without the risk of the value being accidently
changed - which can happen if variables were used for this purpose (this practice encourages another class of
difficult to find bugs).
Using the CONST command you can create an identifier that acts like a variable but is set to a value that cannot
be changed. For example:

```basic
CONST InputVoltagePin = 31
CONST MaxValue = 2.4
```

The identifiers can then be used in a program where they make more sense to the casual reader than simple
numbers. For example:

```basic
IF PIN(InputVoltagePin) > MaxValue THEN SoundAlarm
```

A number of constants can be created on the one line:

```basic
CONST InputVoltagePin = 31, MaxValue = 2.4, MinValue = 1.5
```

The value used to initialise the constant is evaluated when the constant is created and can be an expression
including user defined functions.

The type of the constant is derived from the value assigned to it; so for example, MaxValue above will be a
floating point constant because `2.4` is a floating point number. The type of a constant can also be explicitly set
by using a type suffix (i.e. `!`, `%` or `$`) but it must agree with its assigned value.


## Special Characters in Strings

Special, non-printable characters can be inserted in string constants using the backslash (ie, `\`) as an escape
symbol. To enable this facility the command `OPTION ESCAPE` must be placed at the start of the program.
These are the valid escape sequences:

| | Hex Value | Description |
| :-: |  :-: |  :- | 
| `\a` | 07 | Alert (Beep, Bell) |
| `\b` | 08 | Backspace |
| `\e` | 1B | Escape character |
| `\f` | 0C | Formfeed Page Break |
| `\n` | 0A | Newline (Line Feed) |
| `\r` | 0D | Carriage Return |
| `\q` | 22 | Quote symbol |
| `\t` | 09 | Horizontal Tab |
| `\v` | 0B | Vertical Tab |
| `\\` | 5C | Backslash |
| `\nnn` | any | The byte whose value is given by nnn interpreted as a decimal number |
| `\&hh` | any | The byte whose value is given by hh… interpreted as a hexadecimal number |

For example, the following will print the words Hello and World on separate lines:

```basic
OPTION ESCAPE
PRINT "Hello\r\nWorld"
```

## Expressions and Operators

MMBasic will evaluate a mathematical expression using the standard mathematical rules. For example,
multiplication and division are performed first followed by addition and subtraction. These are called the rules
of precedence and are detailed below.

This means that `2 + 3 * 6` will resolve to `20`, so will `5 * 4` and also `10 + 4 * 3 – 2`.

If you want to force the interpreter to evaluate parts of the expression first you can surround that part of the
expression with brackets. For example, `(10 + 4) * (3 – 2)` will resolve to `14` not `20` as would have been the case
if the brackets were not used. Using brackets does not appreciably slow down the program so you should use
them liberally if there is a chance that MMBasic will misinterpret your intention.

The following operators, in order of precedence, are implemented in MMBasic. Operators that are on the same
level (for example `+` and `-`) are processed with a left to right precedence as they occur on the program line.

| Arithmetic operators | |
|  :-: |  :- |
| `^` | Exponentiation (eg, b^n means bn) | 
| `*` `/` `\` `MOD` | Multiplication, division, integer division and modulus (remainder) |
| `+` `-` | Addition and subtraction | 

| Shift operators | |
|  :-: |  :- |
| `x << y` <br> `x >> y` |  These operate in a special way.<br> `<<` means that the value returned will be the value of x shifted by y bits to the left while <br>`>>` means the same only right shifted.<br> They are integer functions and any bits shifted off are discarded and any bits introduced are set to zero. |

| Logical operators | |
|  :-: |  :- |
| `NOT` `INV` | invert the logical value on the right (eg, `NOT(a=b)` is `a<>b`) or bitwise inversion of the value on the right (eg, `a = INV b`) |
| `<>` `<` `>` `<=` `=<` `>=`  `=>` | Inequality, less than, greater than, less than or equal to, less than or equal to (alternative version), greater than or equal to, greater than or equal to (alternative version) |
| `=` | equality |
| `AND` `OR` `XOR` | Conjunction, disjunction, exclusive or |

For Microsoft compatibility the operators `AND`, `OR` and `XOR` are integer bitwise operators. For example:

```basic
> PRINT (3 AND 6)
2
``` 

Because these operators can act as both logical operators (for example, `IF a=5 AND b=8 THEN …`) and as bitwise operators (eg, `y% = x% AND &B1010`) the interpreter will be confused if they are mixed in the same expression. So, always evaluate logical and bitwise expressions
in separate expressions.

The other logical operations result in the integer 0 (zero) for false and 1 for true. For example `PRINT 4 >= 5` will print  the number `0` on the output and the expression `A = 3 > 2` will store `+1` in `A`.

The `NOT` operator will invert the logical value on its right (it is not a bitwise invert) while the `INV` operator
will perform a bitwise invert. Both of these have the highest precedence so they will bind tightly to the next
value. For normal use of `NOT` or `INV` the expression to be operated on should be placed in brackets. Eg:

```basic
IF NOT (A = 3 OR A = 8) THEN …
```

| String operators | |
| :-: | :- |
| `+` | Join two strings |
| `<>` `<` `>` `<=` `=<` `>=` `=>` | Inequality, less than, greater than, less than or equal to, less than or equal to (alternative version), greater than or equal to, greater than or equal to (alternative version) in order of ascii value. |
| `=` | Equality |

String comparisons respect case. For example `"A"` is greater than `"a"`.


## Mixing Floating Point and Integers

MMBasic automatically handles conversion of numbers between floating point and integers. If an operation
mixes both floating point and integers (eg, `PRINT A% + B!`) the integer will be converted to a floating point
number first, then the operation performed and a floating point number returned. If both sides of the operator
are integers then an integer operation will be performed and an integer returned.

The one exception is the normal division (`/`) which will always convert both sides of the expression to a
floating point number and then returns a floating point number. For integer division you should use the integer
division operator `\`.

MMBasic functions will return a float or integer depending on their characteristics. For example, `PIN()` will
return an integer when the pin is configured as a digital input but a float when configured as an analog input.
If necessary you can convert a float to an integer with the `INT()` function. It is not necessary to specifically
convert an integer to a float but if it was needed the integer value could be assigned to a floating point variable
and it will be automatically converted in the assignment.


## 64-bit Unsigned Integers

MMBasic supports 64-bit signed integers. This means that there are 63 bits for holding the number and one bit
(the most significant bit) which is used to indicate the sign (positive or negative). However it is possible to use
full 64-bit unsigned numbers as long as you do not do any arithmetic on the numbers.

64-bit unsigned numbers can be created using the `&H`, `&O` or `&B` prefixes to a number and these numbers can
be stored in an integer variable. You then have a limited range of operations that you can perform on these.

They are `<<` (shift left), `>>` (shift right), `AND` (bitwise and), `OR` (bitwise or), `XOR` (bitwise exclusive or), `INV`
(bitwise inversion), `=` (equal to) and `<>` (not equal to). Arithmetic operators such as division or addition may
be confused by a 64-bit unsigned number and could return nonsense results.

To display 64-bit unsigned numbers you should use the `HEX$()`, `OCT$()` or `BIN$()` functions.

For example, the following 64-bit unsigned operation will return the expected results:

```basic
> X% = &HFFFF0000FFFF0044
> Y% = &H800FFFFFFFFFFFFF
> X% = X% AND Y%
> PRINT HEX$(X%, 16)
800F0000FFFF0044
```

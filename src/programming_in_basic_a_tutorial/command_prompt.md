## Command Prompt

Interaction with MMBasic is done via the console at the command prompt (ie, the greater than symbol
 `>` on the console). On startup MMBasic will issue the command prompt and wait for some
command to be entered. It will also return to the command prompt if your program ends or if it
generated an error message.

When the command prompt is displayed you have a wide range of commands that you can enter and
execute. Typically they would list the program held in memory ( `LIST` ) or edit it ( `EDIT` ) or perhaps
set some options (the `OPTION` command). Most times the command is just `RUN` which instructs
MMBasic to run the program held in program memory.

Almost any command can be entered at the command prompt and this is often used to test a command
to see how it works. A simple example is the `PRINT` command (more on this later), which you can
test by entering the following at the command prompt:

```basic
PRINT 2 + 2
```

and not surprisingly MMBasic will print out the number 4 before returning to the command prompt.

This ability to test a command at the command prompt is useful when you are learning to program in
BASIC, so it would be worthwhile having a Raspberry Pi Pico loaded with the PicoMite firmware
handy for the occasional test while you are working through this tutorial.

Structure of a BASIC Program
A BASIC program starts at the first line and continues until it runs off the end or hits an `END` 
command - at which point MMBasic will display the command prompt `>` on the console and wait for
something to be entered.

A program consists of a number of statements or commands, each of which will cause the BASIC
interpreter to do something (the words statement and command generally mean the same and are used
interchangeable in this tutorial).

Normally each statement is on its own line but you can have multiple statements in the one line
separated by the colon character `:`.

For example:
```
A = 24.6 : PRINT A
```

Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters
however modern implementations (such as MMBasic) do not need them. You can still use them if
you wish but they have no benefit and generally just clutter up your programs.

This is an example of a program that uses line numbers:

```basic
50 A = 24.6
60 PRINT A
```

A line can also start with a label which can be used as the target for a program jump using the `GOTO`
command. This will be explained in more detail when we cover the `GOTO` command but this is an
example (the label name is `JmpBack`):

```basic
JmpBack: A = A + 1
PRINT A
GOTO JmpBack
```


## Comments

A comment is any text that follows the single quote character ('). A comment can be placed anywhere
and extends to the end of the line. If MMBasic runs into a comment it will just skip to the end of it
(ie, it does not take any action regarding a comment).

Comments should be used to explain non obvious parts of the program and generally inform someone
who is not familiar with the program how it works and what it is trying to do. Remember that after
only a few months a program that you have written will have faded from your mind and will look
strange when you pick it up again. For this reason you will thank yourself later if you use plenty of
comments.

The following are some examples of comments:

```basic
' calculate the hypotenuse
PRINT SQR(a * a + b * b)
```

or

```basic
INPUT var ' get the temperature
```

Older BASIC programs used the command `REM` to start a comment and you can also use that if you
wish but the single quote character is easier to use and more convenient.


## The PRINT Command

There are a number of common commands that are fundamental and we will cover them in this
tutorial but arguably the most useful is the PRINT command. Its job is simple; to print something on
the console. This is mostly used to output data for you to see (like the result of calculations) or
provide informative messages.

`PRINT` is also useful when you are tracing a fault in your program; you can use it to print out the
values of variables and display messages at key stages in the execution of the program.

In its simplest form the command will just print whatever is on its command line. So, for example:

```basic
PRINT 54
```

will display on the console the number 54 followed by a new line.

The data to be printed can be something simple like this or an expression, which means something to
be calculated. We will cover expressions in more detail later but as an example the following:

```basic
> PRINT 3/21
0.1428571429
>
```

would calculate the result of three divided by twenty one and display it. Note that the greater than
symbol `>` is the command prompt produced by MMBasic – you do not type that in.

Other examples of the PRINT command include:

```basic
> PRINT "Wonderful World"
Wonderful World
> PRINT (999 + 1) / 5
200
>
```

You can try these out at the command prompt.

The PRINT command will also work with multiple values at the same time, for example:

```basic
> PRINT "The first number is" 20+25 " and the second is" 18/3
The first number is 45 and the second is 6
>
```

Normally each value is separated by a space character as shown in the previous example but you can also separate values with a comma `,`. The comma will cause a tab to be inserted between the two values. In MMBasic tabs in the `PRINT` command are eight characters apart.

To illustrate tabbing, the following command prints a tabbed list of numbers:

```basic
> PRINT 12, 34, 9.4, 1000
12
34
9.4
1000
>
```

Note that there is a space printed before each number. This space is a place holder for the minus
symbol `-` in case the value is negative. You can see the difference with the numbers 12 and 9.4 in
this example:

```basic
> PRINT -12, 34, -9.4, 1000
-12
34
-9.4
1000
>
```

The print statement can be terminated with a semicolon (;). This will prevent the PRINT command
from moving to a new line when it has printed all the text. For example:

```basic
PRINT "This will be";
PRINT " printed on a single line."
```

Will result in this output:

```basic
This will be printed on a single line.
```

The message would be look like this without the semicolon at the end of the first line:

```basic
This will be
printed on a single line.
```


## Variables

Before we go much further we need to define what a "variable" is as they are fundamental to the
operation of the BASIC language (in fact, most programming languages). A variable is simply a
place to store an item of data (ie, its "value"). This value can be changed as the program runs which
why it is called a "variable".

Variables in MMBasic can be one of three types. The most common is floating point and this is
automatically assumed if the type of the variable is not specified. The other two types are integer and
string and we will cover them later. A floating point number is an ordinary number which can contain
a decimal point. For example 3.45 or -0.023 or 100.00 are all floating point numbers.

A variable can be used to store a number and it can then be used in the same manner as the number
itself, in which case it will represent the value of the last number assigned to it.

As a simple example:

```basic
A = 3
B = 4
PRINT A + B
```

will display the number 7. In this case both A and B are variables and MMBasic used their current
values in the PRINT statement. MMBasic will automatically create a variable when it first encounters
it, so the statement A = 3 both created a floating point variable (the default type) with the name of A
and then it assigned the value of 3 to it.

The name of a variable must start with a letter while the remainder of the name can use letters,
numbers, the underscore or the full stop (or period) characters. The name can be up to 31 characters
long and the case (ie, capitals or not) is not important. Here are some examples:

* `Total_Count`
* `ForeColour`
* `temp3`
* `count`
* `x`
* `ThisIsAVeryLongVariableName`
* `increment.value`

You can change the value of a variable anywhere in your program by using the assignment command, ie:

```basic
variable = expression
```

For example:

```basic
temp3 = 24.6
count = 5
CTemp = (FTemp – 32) * 0.5556
```

In the last example both `CTemp` and `FTemp` are variables and this line converts the value of `FTemp`
(in degrees Fahrenheit) to degrees Celsius and stores the result in the variable `CTemp`.


## Expressions

We have met the term ‘expression’ before in this tutorial and in programming it has a specific
meaning. It is a formula which can be resolved by the BASIC interpreter to a single number or value.

MMBasic will evaluate numeric expressions using the same rules that we learnt at school. For
example, multiplication and division are performed first followed by addition and subtraction. These
are called the rules of precedence and are fully described previously in this manual (see the chapter
Expressions and Operators).

This means that MMBasic will resolve `2 + 3 * 6` by first multiplying 3 by 6 giving 18 then adding 2
resulting in a final value of `20`. Similarly, both `5 * 4` and `10 + 4 * 3 – 2` will also resolve to `20`.

If you want to force the interpreter to evaluate parts of the expression first you can surround that part
of the expression with brackets. For example, `(10 + 4) * (3 – 2)` will resolve to `14` not `20` as would
have been the case if the brackets were not used. Using brackets does not appreciably slow down the
program so you should use them liberally if there is a chance that MMBasic will misinterpret your
intention.

As pointed out earlier, you can use variables in an expression exactly the same as straight numbers.

For example, this will increment the value of the variable temp by one:

```basic
temp = temp + 1
```

You can also use functions in expressions. These are special operations provided by MMBasic, for
example to calculate trigonometric values.

An example of using a function is the following which will print the length of the hypotenuse of a
right angled triangle. This uses the `SQR()` function which returns the square root of a number (a and
b are variables holding the lengths of the other sides):

```basic
PRINT SQR(a * a + b * b)
```

MMBasic will first evaluate this expression by multiplying a by a, then multiplying b by b, then
adding the results together. The resulting number is then passed to the `SQR()` function which will
calculate the square root of that number (ie, the hypotenuse) and return it for the PRINT command to
display.

Some other mathematical functions provided by MMBasic include:

* `SIN(r)` – the sine of r
* `COS(r)` – the cosine of r
* `TAN(r)` – the tangent of r

There are many more functions available to you and they are all listed earlier in this manual.

Note that in the above trigonometric functions the value passed to the function (ie, 'r') is the angle in
radians. In MMBasic you can use the function RAD(d) to convert an angle from degrees to radians
('d' is the angle in degrees).

Another feature of most programming languages (including BASIC) is that you can nest function calls
within each other. For example, given the angle in degrees (ie, 'd') the sine of that angle can be found
with this expression:

```basic
PRINT SIN(RAD(d))
```

In this case MMBasic will first take the value of d and convert it to radians using the `RAD()` function.

The output of this function then becomes the input to the `SIN()` function.

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


## Command Prompt

Interaction with MMBasic is done via the console at the command prompt (ie, the greater than symbol
(>) on the console). On startup MMBasic will issue the command prompt and wait for some
command to be entered. It will also return to the command prompt if your program ends or if it
generated an error message.

When the command prompt is displayed you have a wide range of commands that you can enter and
execute. Typically they would list the program held in memory (LIST) or edit it (EDIT) or perhaps
set some options (the OPTION command). Most times the command is just RUN which instructs
MMBasic to run the program held in program memory.

Almost any command can be entered at the command prompt and this is often used to test a command
to see how it works. A simple example is the PRINT command (more on this later), which you can
test by entering the following at the command prompt:

```basic
PRINT 2 + 2
```

and not surprisingly MMBasic will print out the number 4 before returning to the command prompt.

This ability to test a command at the command prompt is useful when you are learning to program in
BASIC, so it would be worthwhile having a Raspberry Pi Pico loaded with the PicoMite firmware
handy for the occasional test while you are working through this tutorial.

Structure of a BASIC Program
A BASIC program starts at the first line and continues until it runs off the end or hits an END
command - at which point MMBasic will display the command prompt (>) on the console and wait for
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

A line can also start with a label which can be used as the target for a program jump using the GOTO
command. This will be explained in more detail when we cover the GOTO command but this is an
example (the label name is JmpBack):

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

Older BASIC programs used the command REM to start a comment and you can also use that if you
wish but the single quote character is easier to use and more convenient.


## The PRINT Command
There are a number of common commands that are fundamental and we will cover them in this
tutorial but arguably the most useful is the PRINT command. Its job is simple; to print something on
the console. This is mostly used to output data for you to see (like the result of calculations) or
provide informative messages.

PRINT is also useful when you are tracing a fault in your program; you can use it to print out the
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
symbol (>) is the command prompt produced by MMBasic – you do not type that in.

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
symbol (-) in case the value is negative. You can see the difference with the numbers 12 and 9.4 in
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
right angled triangle. This uses the SQR() function which returns the square root of a number (a and
b are variables holding the lengths of the other sides):

```basic
PRINT SQR(a * a + b * b)
```

MMBasic will first evaluate this expression by multiplying a by a, then multiplying b by b, then
adding the results together. The resulting number is then passed to the SQR() function which will
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

In this case MMBasic will first take the value of d and convert it to radians using the RAD() function.

The output of this function then becomes the input to the SIN() function.

The IF Statement
Making decisions is at the core of most computer programs and in BASIC this is usually done with
the IF statement. This is written almost like an English sentence:

```basic
IF condition THEN action
```

The condition is usually a comparison such as equals, less than, more than, etc.

For example:

```basic
IF Temp < 25 THEN PRINT "Cold"
```

Temp would be a variable holding the current temperature (in ºC) and PRINT "Cold" the action to
be done.

There are a range of tests that you can make:

Symbol | Meaning
:-: | :-
= | equals
\< | less than
\> | greater than
\<\> | not equal
\<= | less than or equals
\>= |  greater than or equals

You can also add an ELSE clause which will be executed if the initial condition tested false:

```basic
IF condition THEN true-action ELSE false-action
```

For example, this will execute different actions when the temperature is under 25 or 25 or more:

```basic
IF Temp < 25 THEN PRINT "Cold" ELSE PRINT "Hot"
```

The previous examples all used single line IF statements but you can also use a multiline IF statement.

They look like this:

```basic
IF condition THEN
true-action
true-action
ENDIF
```

or

```basic
IF condition THEN
true-action
true-action
ELSE
false-action
false-action
ENDIF
```

Unlike the single line IF statement you can have many true actions with each on their own line and
similarly many false actions. Generally the single line IF statement is handy if you have a simple
action that needs to be taken while the multiline version is much easier to understand if the actions are
numerous and more complicated.

An example of a multiline IF statement with more than one action is:

```basic
IF Amount < 100 THEN
PRINT "Too low"
PRINT “Minimum value is 100”
ELSE
PRINT "Input accepted"
SaveToSDCard
PRINT "Enter second amount"
ENDIF
```

Note that in the above example each action is indented to show what part of the IF structure it belongs
to. Indenting is not mandatory but it makes a program much easier to understand for someone who is
not familiar with it and therefore it is highly recommended.

In a multiline IF statement you can make additional tests using the ELSE IF command. This is best
explained by using an example (the temperatures are all in ºC):

```basic
IF Temp < 0 THEN
PRINT “Freezing”
ELSE IF Temp < 20 THEN
PRINT “Cold”
ELSE IF Temp < 35 THEN
PRINT “Warm”
ELSE
PRINT “Hot”
ENDIF
```

The ELSE IF uses the same tests as an ordinary IF (ie, <, <=, etc) but that test will only be made if the
preceding test was false. So, for example, you will only get the message Warm if Temp < 0 failed,
and Temp < 20 failed but Temp < 35 was true. The final ELSE will catch the case where all the
tests were false.

An expression like Temp < 20 is evaluated by MMBasic as either true or false with true having a
value of one and false zero. You can see this if you entered the following at the console:

```basic
PRINT 30 > 20
```

MMBasic will print 1 meaning that the value of the expression is true.

Similarly the following will print 0 meaning that the expression evaluated to false.


```basic
PRINT 30 < 20
```

The IF statement does not really care about what the condition actually is, it just evaluates the
condition and if the result is zero it will take that as false and if non zero it will take it as true.

This allows for some handy shortcuts. For example, if BalanceCorrect is a variable that is true
(non zero) when some feature of the program is correct then the following can be used to make a
decision based on that value:

```basic
IF BalanceCorrect THEN …do something…
```

## FOR Loops
Another common requirement in programming is repeating a set of actions. For instance, you might
want to step through all seven days in the week and perform the same function for each day. BASIC
provides the FOR loop construct for this type of job and it works like this:

```basic
FOR day = 1 TO 7
Do something based on the value of ‘day’
NEXT day
```

This starts by creating the variable day and assigning the value of 1 to it. The program will then
execute the following statements until it comes to the NEXT statement. This tells the BASIC
interpreter to increment the value of day, go back to the previous FOR statement and re-execute the
following statements a second time. This will continue looping around until the value of day exceeds
7 and the program will then exit the loop and continue with the statements following the NEXT
statement.

As a simple example, you can print the numbers from one to ten like this:

```basic
FOR nbr = 1 TO 10
PRINT nbr,;
NEXT nbr
```

The comma at the end of the PRINT statement tells the interpreter to tab to the next tab column after
printing the number and the semicolon will leave the cursor on this line rather than automatically
moving to the next line. As a result, the numbers will be printed in neat columns across the page.

This is what you would see:

```basic
1    2    3    4    5    6    7    8    9    10
```


The FOR loop also has a couple of extra tricks up it sleeves. You can change the amount that the
variable is incremented by using the STEP keyword. So, for example, the following will print just the
odd numbers:

```basic
FOR nbr = 1 TO 10 STEP 2
PRINT nbr,;
NEXT nbr
```

The value of the step (or increment value) defaults to one if the STEP keyword is not used but you can
set it to whatever number you want.

When MMBasic is incrementing the variable it will check to see if the variable has exceeded the TO
value and, if it has, it will exit from the loop. So, in the above example, the value of nbr will reach
nine and it will be printed but on the next loop nbr will be eleven and at that point execution will
leave the loop. This test is also applied at the start of the loop. For example, if in the beginning the
value of the variable exceeds the TO value, the loop will never be executed, not even once.

By setting the STEP value to a negative number you can use the FOR loop to step down from a high
number to low. In that case the starting number must be greater than the TO number.

For example, the following will print the numbers from 1 to 10 in reverse:

```basic
FOR nbr = 10 TO 1 STEP -1
PRINT nbr,;
NEXT nbr
```

## Multiplication Table
To further illustrate how loops work and how useful they can be, the following short program uses
two FOR loops to print out the multiplication table that we all learnt at school. The program for this is
not complicated:

```basic
FOR nbr1 = 1 to 10
FOR nbr2 = 1 to 10
PRINT nbr1 * nbr2,;
NEXT nbr2
PRINT
NEXT nbr1
```

The output is shown in the following screen grab, which also shows a listing of the program.

You need to work through the logic of this example line by line to understand what it is doing.

Essentially it consists of one loop inside another. The inner loop, which increments the variable
nbr2 prints one horizontal line of the table. When this loop has finished it will execute the following
PRINT command which has nothing to print - so it will simply output a new line (ie, terminate the
line printed by the inner loop).

The program will then execute another iteration of the outer loop by incrementing nbr1 and
re-executing the inner loop again. Finally, when the outer loop is exhausted (when nbr1 exceeds 10)
the program will reach the end and terminate.

One last point, you can omit the variable name from the NEXT statement and MMBasic will guess
which variable you are referring to. However, it is good practice to include the name to make it easier
for someone else who is reading the program to understand it. You can also terminate multiple loops
using a comma separated list of variables in the NEXT statement. For example:

```basic
FOR var1 = 1 TO 5
FOR var2 = 10 to 13
PRINT var1 * var2
NEXT var1, var2
DO Loops
```

Another method of looping is the DO…LOOP structure which looks like this:

```basic
DO WHILE condition
<statement>
<statement>
LOOP
```

This will start by testing the condition and if it is true the statements will be executed until the LOOP
command is reached, at which point the program will return to DO statement and the condition will be
tested again, and if it is still true the loop will execute again. The condition is the same as in the IF
command (ie, X < Y).

For example, the following will keep printing the word "Hello" on the console for 4 seconds then stop:

```basic
Timer = 0
DO WHILE Timer < 4000
PRINT "Hello"
LOOP
```

Note that Timer is a function within MMBasic which will return the time in milliseconds since the
timer was reset. A reset is done by assigning zero to Timer (as done above) or when powering up
the PicoMite .

A variation on the DO-LOOP structure is the following:

```basic
DO
<statement>
<statement>
LOOP UNTIL condition
```

In this arrangement the loop is first executed once, the condition is then tested and if the condition is
false, the loop will be repeatedly executed until the condition becomes true. Note that the test in
LOOP UNTIL is the inverse of DO WHILE.

For example, similar to the previous example, the following will also print "Hello" for four seconds:

```basic
Timer = 0
DO
PRINT "Hello"
LOOP UNTIL Timer >= 4000
```

Both forms of the DO-LOOP essentially do the same thing, so you can use whatever structure fits
with the logic that you wish to implement.

Finally, it is possible to have a DO Loop that has no conditions at all - ie,

```basic
DO
<statement>
<statement>
LOOP
```


This construct will continue looping forever and you, as the programmer, will need to provide a way
to explicitly exit the loop (the EXIT DO command will do this). For example:

```basic
Timer = 0
DO
PRINT "Hello"
IF Timer >= 4000 THEN EXIT DO
LOOP
```


## Console Input

As well as printing data for the user to see your programs will also want to get input from the user.

For that to work you need to capture keystrokes from the console and this can be done with the
INPUT command. In its simplest form the command is:

```basic
INPUT var
```


This command will print a question mark on the console's screen and wait for a number to be entered
followed by the Enter key. That number will then be assigned to the variable var.



For example, the following program extends the expression for finding the hypotenuse of a triangle by
allowing the user to enter the lengths of the other sides from the console.

```basic
PRINT "Length of side 1"
INPUT a
PRINT "Length of side 2"
INPUT b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
```

This is a screen capture of a typical session:

The INPUT command can also print your prompt for you, so that you do not need a separate PRINT
command. For example, this will work the same as the above program:

```basic
INPUT "Length of side 1"; a
INPUT "Length of side 2"; b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
```

Finally, the INPUT command will allow you to input a series of numbers separated by commas with
each number being saved in different variables.

For example:

```basic
INPUT "Enter the length of the two sides: ", a, b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
```

If the user entered 12,15 the number 12 would be saved in the variable a and 15 in b.

Another method of getting input from the console is the LINE INPUT command. This will get the
whole line as typed by the user and allocate it to a string variable. Like the INPUT command you can
also specify a prompt. This is a simple example:

```basic
LINE INPUT "What is your name? ", s$
PRINT "Hello " s$
```

We will cover string variables later in this tutorial but for the moment you can think of them as a
variable that holds a sequence of characters. If you ran the above program and typed in John when
prompted the program would respond with Hello John.

Sometimes you do not want to wait for the user to hit the enter key, you want to get each character as
it is typed in. This can be done with the INKEY$ function which will return the value of the character
as a string consisting of just one character or an empty string (ie, contains no characters) if nothing has
been entered.

## GOTO and Labels
One method of controlling the flow of the program is the GOTO command. This essentially tells
MMBasic to jump to another part of the program and continue executing from there. The target of the
GOTO is a label and this needs to be explained first.

A label is an identifier that marks part of the program. It must be the first thing on the line and it must
be terminated with the colon (:) character. The name that you use can be up to 31 characters long and
must follow the same rules as for a variable's name. For example, in the following program line
LoopBack is a label:

```basic
LoopBack: a = a + 1
```

When you use the GOTO command to jump to that particular part of the program you would use the
command like this:

```basic
GOTO LoopBack
```

To put all this into context the following program will print out all the numbers from 1 to 10:

```basic
z = 0
LoopBack: z = z + 1
PRINT z
IF z < 10 THEN GOTO LoopBack
```

The program starts by setting the variable z to zero then incrementing it to 1 in the next line. The
value of z is printed and then tested to see if it is less than 10. If it is less than 10 the program
execution will jump back to the label LoopBack where the process will repeat. Eventually the value
of z will reach 10 and the program will run off the end and terminate.

Note that a FOR loop can do the same thing (and is simpler), so this example is purely designed to
illustrate what the GOTO command can do.

In the past the GOTO command gained a bad reputation. This is because using GOTOs it is possible
to create a program that continuously jumps from one point to another (often referred to as "spaghetti
code") and that type of program is almost impossible for another programmer to understand. With
constructs like the multiline IF statements the need for the GOTO statement has been reduced and it
should be used only when there is no other way of changing the program's flow.

Testing for Prime Numbers
The following is a simple program which brings together many of the programming features
previously discussed.

```basic
DO
InpErr:
PRINT
INPUT "Enter a number: "; a
IF a < 2 THEN
PRINT "Number must be equal or greater than 2"
GOTO InpErr
ENDIF
Divs = 0
FOR x = 2 TO SQR(a)
r = a/x
IF r = FIX(r) THEN Divs = Divs + 1
NEXT x
PRINT a " is ";
IF Divs > 0 THEN PRINT "not ";
PRINT "a prime number."
LOOP
```

This will first prompt (on the console) for a number and, when it has been entered, it will test if that
number is a prime number or not and display a suitable message.

It starts with a DO Loop that does not have a condition – so it will continue looping forever. This is
what we want. It means that when the user has entered a number, it will report if it is a prime number
or not and then loop around and ask for another number. The way that the user can exit the program
(if they wanted to) is by typing the break character (normally CTRL-C).

The program then prints a prompt for the user which is terminated with a semicolon character. This
means that the cursor is left at the end of the prompt for the INPUT command which will get the
number and store it in the variable a.

Following this the number is tested. If it is less than 2 an error message will be printed and the
program will jump backwards and ask for the number again.

We are now ready to test if the number is a prime number. The program uses a FOR loop to step
through the possible divisors testing if each one can divide evenly into the entered number. Each time
it does the program will increment the variable Divs.

Note that the test is done with the function FIX(r) which simply strips off any digits after the decimal
point. So, the condition r = FIX(r) will be true if r is an integer (ie, has no digits after the
decimal point).

Finally, the program will construct the message for the user. The key part is that if the variable Divs
is greater than zero it means that one or more numbers were found that could divide evenly into the
test number. In that case the IF statement inserts the word "not" into the output message.

For example, if the entered number was 21 the user will see this response:

```basic
21 is not a prime number.
```

This is the result of running the program and some of the output:

You can test this program by using the editor (the EDIT command) to enter it.

Using your newly learnt skills you could then have a shot at making it more efficient. For example,
because the program counts how many times a number can be divided into the test number it takes a
lot longer than it should to detect a non prime number. The program would run much more efficiently
if it jumped out of the FOR loop at the first number that divided evenly. You could use the GOTO
command to do this or you could use the command EXIT FOR – that would cause the FOR loop to
terminate immediately.

Other efficiencies include only testing the division with odd numbers (by using an initial test for an
even number then starting the FOR loop at 3 and using STEP 2) or by only using prime numbers for
the test (that would be much more complicated).

## Arrays

Arrays are something which you will probably not think of as
useful at first glance but when you do need to use them you will
find them very handy indeed.

An array is best thought of as a row of letterboxes for a block of
units or condos as shown on the right. The letterboxes are all
located at the same address and each box represents a unit or
condo at that address. You can place a letter in the box for unit
one, or unit two, etc.

Similarly an array in BASIC is a single variable with multiple
sub units (called elements in BASIC) which are numbered. You
can place data in element one, or element two, etc. In BASIC an
array is created by the DIM command, for example:

```basic
DIM numarr(300)
```

This creates an array with the name of numarr containing 301 elements (think of them as
letterboxes) ranging from 0 to 300. By default an array will start from zero so this is why there is an
extra element making the total 301. To specify a specific element in the array (ie, a specific letterbox)
you use an index which is simply the number of the array element that you wish to access. For
example, if you want to set element number 100 in this array to (say) the number 876, you would do it
this way:

```basic
numarr(100) = 876
```

Normally the index to an array is not a constant number as in this example (ie, 100) but a variable
which can be changed to access different array elements.

As an example of how you might use an array, consider the case where you would like to record the
maximum temperature for each day of the year and, at the end of the year, calculate the overall
average. You could use ordinary variables to record the temperature for each day but you would need
365 of them and that would make your program quite unwieldy. Instead, you could define an array to
hold the values like this:

```basic
DIM days(365)
```

Every day you would need to save the temperature in the correct location in the array. If the number of
the day in the year was held in the variable doy and the maximum temperature was held in the
variable maxtemp you would save the reading like this:

```basic
days(doy) = maxtemp
```

At the end of the year it would be simple to calculate the average for the year.

For example:

```basic
total = 0
FOR i = 1 to 365
total = total + days(i)
NEXT i
PRINT "Average is:" total / 365
```

This is much easier than adding up and averaging 365 individual variables.

The above array was single dimensioned but you can have multiple
dimensions. Reverting to our analogy of letterboxes, an array with two
dimensions could be thought of as a block of flats with multiple floors. A
block could have a row of four letter boxes for level one, another row of
four boxes for level two, and so on. To place a letter in a letterbox you
need to specify the floor number and the unit number on that floor.



In BASIC such an array is specified using two indices separated by a comma. For example:

```basic
LetterBox(floor, unit)
```

As a practical example, assume that you needed to record the maximum temperature for each day over
five years. To do this you could dimension the array as follows:

```basic
DIM days(365, 5)
```

The first index is the day in the year and the second is a number representing the year. If you wanted
to set day 100 in year 3 to 24 degrees you would do it like this:

```basic
days(100, 3) = 24
```

In MMBasic for the PicoMite firmware, you can have up to six dimensions with the RP2040
processor or five dimensions with the RP2350 processor. The size of an array is limited only by the
amount of free RAM that is available.


## Integers
So far all the numbers and variables that we have been using have been floating point. As explained
before, floating point is handy because it will track digits after the decimal point and when you use
division it will return a sensible result. So, if you just want to get things done and are not concerned
with the details you should stick to floating point.

However, the limitation of floating point is that it stores numbers as an approximation with an
accuracy of 14 digits in the PicoMite firmware . Most times this characteristic of floating point
numbers is not a problem but there are some cases where you need to accurately store larger numbers.

As an example, let us say that you want to manipulate time accurately down to the microsecond so
that you can compare two different date/times to work out which one is earlier. The easy way to do
this is to convert the date/time to the number of microseconds since some date (say 1st Jan in year
zero) - then finding the earliest of the two is just a matter of using an arithmetic compare in an IF
statement.

The problem is that the number of microseconds since that date will exceed the accuracy range of
floating point variables and this is where integer variables come in. An integer variable can accurately
hold very large numbers up to nine million million million (or ±9223372036854775807 to be precise).

The downside of using an integer is that it cannot store fractions (ie, numbers after the decimal point).

Any calculation that produces a fractional result will be rounded up or down to the nearest whole
number when assigned to an integer. However this characteristic can be handy when dealing with
money – for example, you don’t want to send someone a bill for $100.13333333333.

It is easy to create an integer variable, just add the percent symbol (%) as a suffix to a variable name.

For example, sec% is an integer variable. Within a program you can mix integers and floating point
and MMBasic will make the necessary conversions but if you want to maintain the full accuracy of
integers you should avoid mixing the two.

Just like floating point you can have arrays of integers, all you need to do is add the percent character
as a suffix to the array name. For example: days%(365, 5).

Beginners often get confused as to when they should use floating point or integers and the answer is
simple… always use floating point unless you need an extremely high level of accuracy. This does
not happen often but when you need them you will find that integers are quite useful.


## Strings

Strings are another variable type (like floating point and integers). Strings are used to hold a sequence
of characters. For example, in the command:

```basic
PRINT "Hello"
```

The string "Hello" is a string constant. Note that a constant is something that does not change (as
against a variable, which can) and that string constants are always surrounded by double quotes.

String variables names use the dollar symbol ($) as a suffix to identify them as a string instead of a
normal floating point variable and you can use ordinary assignment to set their value. The following
are examples (note that the second example uses an array of strings):

```basic
Car$ = "Holden"
Country$(12) = "India"
Name$ = "Fred"
```

You can also join strings using the plus operator:

```basic
Word1$ = "Hello"
Word2$ = "World"
Greeting$ = Word1$ + " " + Word2$
```

In which case the value of Greeting$ will be "Hello World".

Strings can also be compared using operators such as = (equals), <> (not equals), < (less than), etc.

For example:

```basic
IF Car$ = "Holden" THEN PRINT "Was an Aussie made car"
```

The comparison is made using the full ASCII character set so a space will come before a printable
character. Also the comparison is case sensitive so 'holden' will not equal "Holden". Using the
function UCASE() to convert the string to upper case you can then have a case insensitive
comparison. For example:

```basic
IF UCASE$(Car$) = "HOLDEN" THEN PRINT "Was an Aussie made car"
```

You can have arrays of strings but you need to be careful when you declare them as you can rapidly
run out of RAM (general memory used for storing variables, etc). This is because MMBasic will by
default allocate 255 bytes of RAM for each element of the array. For example, a string array with 100
elements will by default use 25K of RAM. To alleviate this you can use the LENGTH qualifier to
limit the maximum size of each element. For instance, if you know that the maximum length of any
string that will be stored in the array will be less than 20 characters you can use the following
declaration to allocate just 20 bytes for each element:

```basic
DIM MyArray$(100) LENGTH 20
```

The resultant array will only use 2K of RAM.

Note that sometimes people think that by using the LENGTH qualifier when declaring a normal (non
array) string variable they will save some RAM. This is not correct; they always occupy 256 bytes.

## Manipulating Strings
String handling is one of MMBasic's strengths and using a few simple functions you can pull apart
and generally manipulate strings. The basic string functions are:

Command | Description 
:-: | :-
`LEFT$(string$, nbr )` | Returns a substring of string$ with nbr of characters from the left (beginning) of the string.
`RIGHT$(string$, nbr )` | Same as the above but return nbr of characters from the right (end) of the string.
`MID$(string$, pos, nbr )` | Returns a substring of string$ with nbr of characters starting from the character pos in the string (ie, the middle of the string).

For example if S$ = "This is a string"
- then: `R$ = LEFT$(S$, 7)` would result in the value of R$ being set to: "This is"
- and: `R$ = RIGHT$(S$, 8)` would result in the value of R$ being set to: "a string"
- finally: `R$ = MID$(S$, 6, 2)` would result in the value of R$ being set to: "is"

Note that in MID$() the first character position in a string is number 1, the second is number 2 and so
on. So, counting the first character as one, the sixth position is the start of the word "is".

Another useful function is:

Command | Description 
:-: | :-
`INSTR(string$, pattern$ )` | Returns a number representing the position at which pattern$ occurs in string$.

This can be used to search for a string inside another string. The number returned is the position of
the substring inside the main string. Like with MID$() the start of the string is position 1.

For example if `S$ = "This is a string"` Then: `pos = INSTR(S$, " ")` would result in pos being set to the position of the first space in S$ (ie, 5).

`INSTR()` can be combined with other functions so this would return the first word in S$:

```basic
R$ = LEFT$(S$, INSTR(S$, " ") - 1)
```

There is also an extended version of INSTR():

```basic
INSTR(pos, string$, pattern$ )
```

Returns a number representing the position at which pattern$
occurs in string$ when starting the search at the character position
pos.


So we can find the second word in S$ using the following:

```basic
pos = INSTR(S$, " ")
R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
```

This last example is rather complicated so it might be worth working through it in detail so that you
can understand how it works.

Note that `INSTR()` will return the number zero if the sub string is not found and that any string
function will throw an error (and halt the program) if that is used as a character position. So, in a
practical program you would first check for zero being returned by `INSTR()` before using that value.

For example:

```basic
pos = INSTR(S$, " ")
if pos > 0 THEN R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
```

## Scientific Notation

Before we finish discussing data types we need to cover off the subject of floating point numbers and
scientific notation.

Most numbers can be written normally, for example 11 or 24.5, but very large or small numbers are
more difficult. For example, it has been estimated that the number of grains of sand on planet Earth is
7500000000000000000. The problem with this number is that you can easily lose track of how many
zeros there are in the number and consequently it is difficult to compare this with a similar sized
number.

A scientist would write this number as 7.5 x 1018 which is called scientific notation and is much easier
to comprehend.

MMBasic will automatically shift to scientific notation when dealing with very large or small floating
point numbers. For example, if the above number was stored in a floating point variable the PRINT
command would display it as 7.5E+18 (this is BASIC’s way of representing 7.5 x 1018). As another
example, the number 0.0000000456 would display as 4.56E-8 which is the same as 4.56 x 10-8.

You can also use scientific notation when entering constant numbers in MMBasic. For example:

```basic
SandGrains = 7.5E+18
```

MMBasic only uses scientific notation for displaying floating point numbers (not integers). For
instance, if you assigned the number of grains of sand to an integer variable it would print out as a
normal number (with lots of zeros).


## DIM Command
We have used the DIM command before for defining arrays but it can also be used to create ordinary
variables. For example, you can simultaneously create four string variables like this:

```basic
DIM STRING Car, Name, Street, City
```

Note that because these variables have been defined as strings using the DIM command we do not
need the $ suffix, the definition alone is enough for MMBasic to identify their type. Similarly, when
you use these variables in an expression you do not need the type suffix: For example:

```basic
City = "Sydney"
```

You can also use the keyword INTEGER to define a number of integer variables and FLOAT to do
the same for floating point variables. This type of notation can similarly be used to define arrays.

For example:

```basic
DIM INTEGER seconds(200)
```

Another method of defining the variables type is to use the keyword AS. For example:

```basic
DIM Car AS STRING, Name AS STRING, Street AS STRING
```

This is the method used by Microsoft (MMBasic tries to maintain Microsoft compatibility) and it is
useful if the variables have different types. For example:

```basic
DIM Car AS STRING, Age AS INTEGER, Value AS FLOAT
```

You can use any of these methods of defining a variable's type, they all act the same.

The advantage of defining variables using the DIM command is that they are clearly defined
(preferably at the start of the program) and their type (float, integer or string) is not subject to
misinterpretation.

You can strengthen this by using the following commands at the very top of your program:

```basic
OPTION EXPLICIT
OPTION DEFAULT NONE
```

The first specifies to MMBasic that all variables must be explicitly defined using DIM before they can
be used. The second specifies that the type of all variables must be specified when they are created.


### Why are these two commands important?

The first can help avoid a common programming error which is where you accidently misspell a
variable's name. For example, your program might have the current temperature saved in a variable
called Temp but at one point you accidently misspell it as Tmp. This will cause MMBasic to
automatically create a variable called Tmp and set its value to zero.

This is obviously not what you want and it will introduce a subtle error which could be hard to find,
even if you were aware that something was not right. On the other hand, if you used the OPTION
EXPLICIT command at the start of your program MMBasic would refuse to automatically create the
variable and instead would display an error thereby saving you from a probable headache.

The command OPTION DEFAULT NONE further helps because it tells MMBasic that the
programmer must specifically specify the type of every variable when they are declared. It is easy to
forget to specify the type and allowing MMBasic to automatically assume the type can lead to
unexpected consequences.

For small, quick and dirty programs, it is fine to allow MMBasic to automatically create variables but
in larger programs you should always disable this feature with OPTION EXPLICIT and strengthen it
with OPTION DEFAULT NONE.

When a variable is created it is set to zero for float and integers and an empty string (ie, contains no
characters) for a string variable. You can set its initial value to something else when it is created using
DIM.


For example:

```basic
DIM FLOAT nbr = 12.56
DIM STRING Car = "Ford", City = "Perth"
```

You can also initialise arrays by placing the initialising values inside brackets like this:

```basic
DIM s$(2) = ("zero", "one", "two")
```

Note that because arrays start from zero by default this array actually has three elements with the
index numbers of 0, 1 and 2. This is why we needed three string constants to initialise it.


## Constants

A common requirement in programming is to define an identifier that represents a value without the
risk of the value being accidently changed - which can happen if variables were used for this purpose.

These are called constants and they can represent I/O pin numbers, signal limits, mathematical
constants and so on.

You can create a constant using the CONST command. This defines an identifier that acts like a
variable but is set to a value that cannot be changed.

For example, if you wanted to check the voltage of a battery connected to pin 31 you could define the
relevant values thus:

```basic
CONST BatteryVoltagePin = 31
CONST BatteryMinimum = 1.5
```

These constants can then be used in the program where they make more sense to the casual reader
than simple numbers. For example:

```basic
SETPIN BatteryVoltagePin, AIN
IF PIN(BatteryVoltagePin) < BatteryMinimum THEN SoundAlarm
```

It is good programming practice to use constants for any fixed number that represents an important
value. Normally they are defined at the start of a program where they are easy to see and conveniently
located for another programmer to adjust (if necessary).


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
called like this and it will be concatenated in the PRINT statement to make the full error message.

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
AS keyword similar to the way it is used in the DIM command.

For example, the following is identical to the above example:

```basic
SUB MySub Msg AS STRING, Nbr AS INTEGER
…
END SUB
```

Of course, if you used only one variable type throughout the program and used OPTION DEFAULT
to set that type you could ignore the question of variable types completely.

When a subroutine is called with an argument that is a variable (ie, not a constant or expression)
MMBasic will create a corresponding variable within the subroutine that points back to this variable.

Any changes to the variable representing the argument inside the subroutine will also change the
variable used in the call. This is called passing arguments by reference.

This is best explained by example:

```basic
DIM MyNumber = 5     ‘ set the variable to 5
CalcSquare MyNumber  ‘ the subroutine will square its value
PRINT MyNumber
END
SUB CalcSquare nbr   ‘ this will print the number 25
nbr = nbr * nbr      ‘ square the argument and pass it back
END SUB
```

The subroutine CalcSquare will take its argument, square it and write it back to the variable
representing the argument (nbr). Because the subroutine was called with a variable (MyNumber) the
variable nbr will point back to MyNumber and any change to nbr will also change MyNumber
accordingly. As a result the PRINT statement will output 25.

Passing arguments by reference is handy because it allows a subroutine to pass values back to the
code that called it. However, it could lead to trouble if a subroutine used the variable representing an
argument as a general purpose variable and changed its value. Then, if it were called with a variable as
an argument, that variable would be inadvertently changed. To avoid this, you should prefix its
definition with the keyword BYVAL. This instructs MMBasic to always use the value of the
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
IF…THEN commands, FOR…NEXT loops and so on. However, one thing that you cannot do is
jump out of a subroutine using GOTO (if you do the result will be undefined and may cause your hair
to turn grey).

Normally the subroutine will exit when the END SUB command is reached but you can also terminate
the subroutine early by using the EXIT SUB command.

Functions
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

(string, integer or float), otherwise it will return whatever the OPTION DEFAULT is set to. For
example, the following function will return a string:

```basic
FUNCTION LVal$(nbr)
IF nbr = 0 THEN LVal$ = "False" ELSE LVal$ = "True"
END FUNCTION
```

You can explicitly specify the type of the function by using the AS keyword and then you do not need
to use a type suffix (similar to defining a variable using DIM).

This is the above example rewritten to take advantage of this feature:

```basic
FUNCTION LVal(nbr) AS STRING
IF nbr = 0 THEN LVal = "False" ELSE LVal = "True"
END FUNCTION
```

In this case the type returned by the function LVal will be a string.

As for subroutines you can use most features of MMBasic within functions. This includes
FOR…NEXT loops, calling other functions and subroutines, etc. Also, the function will return to the
expression that called it when the END FUNCTION command is reached but you can also return early
by using the EXIT FUNCTION command.


## Local Variables

Variables that are created using DIM or that are just automatically created are called global variables.

This means that they can be seen and used anywhere in the program including within subroutines and
functions. However, inside a subroutine or function you will often need to use variables for various
tasks that are internal to the subroutine/function. In portable code you do not want the name you
chose for such a variable to clash with a global variable of the same name. To this end you can define
a variable using the LOCAL command within the subroutine/function.

The syntax for LOCAL is identical to the DIM command, this means that the variable can be an array,
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

The variable tstr is declared as LOCAL within the subroutine, which means that (like the argument
list) it will only exist within the subroutine and will vanish when the subroutine exits. You can have a
global variable called tstr in your main program and it will be different from the variable tstr in
the subroutine (in this case the global tstr will be hidden within the subroutine).

You should always use local variables for operations within your subroutine or function because they
help make the module much more self contained and portable.

## Static Variables
LOCAL variables are reset to their initial values (normally zero or an empty string) every time the
subroutine or function starts, however there are times when you would like the variable to retain its
value between calls. This type of variable is defined with the STATIC command.

We can demonstrate how STATIC variables are useful by extending the ErrMsg subroutine to prevent
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

The STATIC command uses exactly the same syntax as DIM. This means that you can define
different types of static variables including arrays and you can also initialise them to some value.

The static variable is created on the first time the STATIC command is encountered and it is
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

Normally you will use global variables (created using DIM) to track a state but sometimes you want
this to be contained within a module and this is where static variables are valuable. Just like LOCAL
the use of STATIC helps to make your subroutines and functions more self contained and portable.

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

The main feature of the program is the defined function GetDays() which takes a string entered at the console, splits it into its day, month and year components then calculates the number of days since 1st January 1900.

This function is called twice, once for the first date and then again for the second date. It is then just a matter of subtracting one date (in days) from the other to get the difference in days.

We will not go into the detail of how the calculations are made (ie, handling leap years) as that can be left as an exercise for the reader. However, it is appropriate to point out some features of MMBasic
that are used by the program.

It demonstrates how local variables can be used and how they can be initialised. In the function GetDays() two arrays are declared and initialised at the same time. These are just a convenient method of looking up the names of the months and the cumulative number of days for each month.

Later in the function (the FOR loop) you can see how they make dealing with twelve different months quite efficient.

Another feature highlighted by this program is the string handling features of MMBasic. The INSTR() function is used to locate the two space characters in the date string and then later the MID$() function uses these to extract the day, month and year components of the date. The VAL() function is used to turn a string of digits (like the year) into a number that can be stored in a numeric variable.

Note that the value of a function is initialised to zero every time the function is called and unless it is set to some value it will return a zero value. This makes error handling easy because we can just exit the function if an error is discovered. It is then the responsibility of the calling program code to check for a return value of zero which signifies an error.

This program illustrates one of the benefits of using subroutines and functions which is that when written and fully tested they can be treated as a trusted "black box" that does not have to be opened.

For this reason functions like this should be the properly tested and then, if possible, left untouched (in case you add some error).

There are a few features of this program that we have not covered before. The first is the MOD operator which will calculate the remainder of dividing one number into another. For example, if you divided 4 into 15 you would have a remainder of 3 which is exactly what the expression 15 MOD 4 will return. The ABS() function is also new and will return its argument as a positive number (eg, ABS(-15) will return +15 as will ABS(15)).

The EXIT FOR command will exit a FOR loop even though it has not reached the end of its looping, EXIT FUNCTION will immediately exit a function even though execution has not reached the end of the function and CONTINUE DO will immediately cause the program to jump to the end of a DO loop and execute it again.

Why would this program be useful? Well some people like to count their age in days, that way every day is a birthday! You can calculate your age in days, just enter the date that you were born and today's date. That is not particularly useful but the program itself is valuable as it demonstrates many of the characteristics of programming in MMBasic. So, work your way through the program and review each section until you understand it – it should be a rewarding experience.

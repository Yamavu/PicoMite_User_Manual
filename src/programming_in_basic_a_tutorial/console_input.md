## Console Input

As well as printing data for the user to see your programs will also want to get input from the user.

For that to work you need to capture keystrokes from the console and this can be done with the
[INPUT command](../command/input.md). In its simplest form the command is:

```basic
INPUT var
```

This command will print a question mark on the console's screen and wait for a number to be entered
followed by the Enter key. That number will then be assigned to the variable `var`.

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
it is typed in. This can be done with the [INKEY$ function](../function/inkey$.md) which will return the value of the character
as a string consisting of just one character or an empty string (ie, contains no characters) if nothing has
been entered.


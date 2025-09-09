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


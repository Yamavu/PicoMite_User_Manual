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
```


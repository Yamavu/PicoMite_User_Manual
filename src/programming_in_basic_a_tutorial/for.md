## FOR Loops

Another common requirement in programming is repeating a set of actions. For instance, you might
want to step through all seven days in the week and perform the same function for each day. BASIC
provides the `FOR` loop construct for this type of job and it works like this:

```basic
FOR day = 1 TO 7
' Do something based on the value of ‘day’
NEXT day
```

This starts by creating the variable `day` and assigning the value of `1` to it. The program will then
execute the following statements until it comes to the `NEXT` statement. This tells the BASIC
interpreter to increment the value of day, go back to the previous `FOR` statement and re-execute the
following statements a second time. This will continue looping around until the value of day exceeds
7 and the program will then exit the loop and continue with the statements following the `NEXT`
statement.

As a simple example, you can print the numbers from one to ten like this:

```basic
FOR nbr = 1 TO 10
  PRINT nbr,;
NEXT nbr
```

Alternatively MMbasic allows you to place multiple statements on a single line by separating them with a colon `:`.

```basic
FOR nbr = 1 TO 10 : PRINT nbr,; : NEXT nbr
```

The comma at the end of the `PRINT` statement tells the interpreter to tab to the next tab column after
printing the number and the semicolon will leave the cursor on this line rather than automatically
moving to the next line. As a result, the numbers will be printed in neat columns across the page.

This is what you would see the output:

```basic
1  2  3  4  5  6  7  8  9  10
```


The `FOR` loop also has a couple of extra tricks up it sleeves. You can change the amount that the
variable is incremented by using the `STEP` keyword. So, for example, the following will print just the
odd numbers:

```basic
FOR nbr = 1 TO 10 STEP 2
PRINT nbr,;
NEXT nbr
```

The value of the step (or increment value) defaults to one if the `STEP` keyword is not used but you can
set it to whatever number you want.

When MMBasic is incrementing the variable it will check to see if the variable has exceeded the TO
value and, if it has, it will exit from the loop. So, in the above example, the value of nbr will reach
nine and it will be printed but on the next loop nbr will be eleven and at that point execution will
leave the loop. This test is also applied at the start of the loop. For example, if in the beginning the
value of the variable exceeds the TO value, the loop will never be executed, not even once.

By setting the `STEP` value to a negative number you can use the FOR loop to step down from a high
number to low. In that case the starting number must be greater than the TO number.

For example, the following will print the numbers from 1 to 10 in reverse:

```basic
FOR nbr = 10 TO 1 STEP -1
PRINT nbr,;
NEXT nbr
```

### Multiplication Table

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


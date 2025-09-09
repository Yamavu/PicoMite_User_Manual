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


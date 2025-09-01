## DO Loops

Another method of looping is the `DO … LOOP` structure which looks like this:

```basic
DO WHILE condition
<statement>
<statement>
LOOP
```

This will start by testing the condition and if it is true the statements will be executed until the `LOOP`
command is reached, at which point the program will return to DO statement and the condition will be
tested again, and if it is still true the loop will execute again. The condition is the same as in the `IF`
command (ie, `X < Y`).

For example, the following will keep printing the word "Hello" on the console for 4 seconds then stop:

```basic
Timer = 0
DO WHILE Timer < 4000
PRINT "Hello"
LOOP
```

Note that Timer is a function within MMBasic which will return the time in milliseconds since the
timer was reset. A reset is done by assigning zero to Timer (as done above) or when powering up
the PicoMite.

A variation on the `DO … LOOP` structure is the following:

```basic
DO
<statement>
<statement>
LOOP UNTIL condition
```

In this arrangement the loop is first executed once, the condition is then tested and if the condition is
false, the loop will be repeatedly executed until the condition becomes true. Note that the test in
`LOOP UNTIL` is the inverse of `DO WHILE`.

For example, similar to the previous example, the following will also print "Hello" for four seconds:

```basic
Timer = 0
DO
PRINT "Hello"
LOOP UNTIL Timer >= 4000
```

Both forms of the `DO … LOOP` essentially do the same thing, so you can use whatever structure fits
with the logic that you wish to implement.

Finally, it is possible to have a `DO` Loop that has no conditions at all.

```basic
DO
<statement>
<statement>
LOOP
```


This construct will continue looping forever and you, as the programmer, will need to provide a way
to explicitly exit the loop (the `EXIT DO` command will do this). 

For example:

```basic
Timer = 0
DO
PRINT "Hello"
IF Timer >= 4000 THEN EXIT DO
LOOP
```
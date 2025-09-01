## The IF Statement

Making decisions is at the core of most computer programs and in BASIC this is usually done with
the `IF` statement. This is written almost like an English sentence:

```basic
IF condition THEN action
```

The condition is usually a comparison such as equals, less than, more than, etc.

For example:

```basic
IF Temp < 25 THEN PRINT "Cold"
```

Temp would be a variable holding the current temperature (in ºC) and `PRINT` "Cold" the action to
be done.

There are a range of tests that you can make:

Symbol | Meaning
:-: | :-
= | equals
\< | less than
\> | greater than
\<\> | not equal
\<= | less than or equals
\>= | greater than or equals

You can also add an ELSE clause which will be executed if the initial condition tested false:

```basic
IF condition THEN true-action ELSE false-action
```

For example, this will execute different actions when the temperature is under 25 or 25 or more:

```basic
IF Temp < 25 THEN PRINT "Cold" ELSE PRINT "Hot"
```

The previous examples all used single line `IF` statements but you can also use a multiline `IF` statement.

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

Unlike the single line `IF` statement you can have many true actions with each on their own line and
similarly many false actions. Generally the single line `IF` statement is handy if you have a simple
action that needs to be taken while the multiline version is much easier to understand if the actions are
numerous and more complicated.

An example of a multiline `IF` statement with more than one action is:

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

Note that in the above example each action is indented to show what part of the `IF` structure it belongs
to. Indenting is not mandatory but it makes a program much easier to understand for someone who is
not familiar with it and therefore it is highly recommended.

In a multiline `IF` statement you can make additional tests using the `ELSE IF` command. This is best
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

The ELSE `IF` uses the same tests as an ordinary `IF` (ie, `<`, `<=`, etc) but that test will only be made if the
preceding test was false. So, for example, you will only get the message Warm if `Temp < 0` failed,
and `Temp < 20` failed but `Temp < 35` was true. The final `ELSE` will catch the case where all the
tests were false.

An expression like `Temp < 20` is evaluated by MMBasic as either true or false with true having a
value of one and false zero. You can see this if you entered the following at the console:

```basic
PRINT 30 > 20
```

MMBasic will print `1` meaning that the value of the expression is true.

Similarly the following will print `0` meaning that the expression evaluated to false.


```basic
PRINT 30 < 20
```

The IF statement does not really care about what the condition actually is, it just evaluates the
condition and if the result is zero it will take that as false and if non zero it will take it as true.

This allows for some handy shortcuts. For example, if `BalanceCorrect` is a variable that is true
(non zero) when some feature of the program is correct then the following can be used to make a
decision based on that value:

```basic
IF BalanceCorrect THEN …do something…
```

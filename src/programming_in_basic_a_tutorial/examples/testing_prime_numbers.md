## Testing for Prime Numbers

The following is a simple program which brings together many of the programming features
previously discussed.

```basic
DO
  InpErr:
  PRINT
  INPUT "Enter a number: "; a
  IF a < 2 THEN
    PRINT "Number must be 2 or greater"
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

It starts with a [DO-Loop](./do_loops.md) that does not have a condition – so it will continue looping forever. This is
what we want. It means that when the user has entered a number, it will report if it is a prime number
or not and then loop around and ask for another number. The way that the user can exit the program
(if they wanted to) is by typing the break character (normally **CTRL-C**).

The program then prints a prompt for the user which is terminated with a semicolon character. This
means that the cursor is left at the end of the prompt for the [INPUT command](../command/input.md) which will get the
number and store it in the variable `a`.

Following this the number is tested. If it is less than 2 an error message will be printed and the
program will jump backwards and ask for the number again.

We are now ready to test if the number is a prime number. The program uses a [FOR loop](./for.md) to step
through the possible divisors testing if each one can divide evenly into the entered number. Each time
it does the program will increment the variable `Divs`.

Note that the test is done with the function [FIX(r)](../function/fix.md) which simply strips off any digits after the decimal point. So, the condition `r = FIX(r)` will be true if `r` is an integer (ie, has no digits after the
decimal point).

Finally, the program will construct the message for the user. The key part is that if the variable `Divs`
is greater than zero it means that one or more numbers were found that could divide evenly into the
test number. In that case the `IF` statement inserts the word `"not"` into the output message.

For example, if the entered number was `21` the user will see this response:

```basic
21 is not a prime number.
```

This is the result of running the program and some of the output:

You can test this program by using the editor (the `EDIT` command) to enter it.

Using your newly learnt skills you could then have a shot at making it more efficient. For example,
because the program counts how many times a number can be divided into the test number it takes a
lot longer than it should to detect a non prime number. The program would run much more efficiently
if it jumped out of the `FOR` loop at the first number that divided evenly. You could use the `GOTO`
command to do this or you could use the command `EXIT FOR` – that would cause the `FOR` loop to
terminate immediately.

Other efficiencies include only testing the division with odd numbers (by using an initial test for an
even number then starting the `FOR` loop at `3` and using `STEP 2`) or by only using prime numbers for
the test (that would be much more complicated).

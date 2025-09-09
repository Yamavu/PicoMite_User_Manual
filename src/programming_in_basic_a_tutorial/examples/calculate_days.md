
### Calculate Days

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

The main feature of the program is the defined function `GetDays()` which takes a string entered at the console, splits it into its day, month and year components then calculates the number of days since 1st January 1900.

This function is called twice, once for the first date and then again for the second date. It is then just a matter of subtracting one date (in days) from the other to get the difference in days.

We will not go into the detail of how the calculations are made (ie, handling leap years) as that can be left as an exercise for the reader. However, it is appropriate to point out some features of MMBasic
that are used by the program.

It demonstrates how local variables can be used and how they can be initialised. In the function `GetDays()` two arrays are declared and initialised at the same time. These are just a convenient method of looking up the names of the months and the cumulative number of days for each month.

Later in the function (the FOR loop) you can see how they make dealing with twelve different months quite efficient.

Another feature highlighted by this program is the string handling features of MMBasic. The `INSTR()` function is used to locate the two space characters in the date string and then later the MID$() function uses these to extract the day, month and year components of the date. The `VAL()` function is used to turn a string of digits (like the year) into a number that can be stored in a numeric variable.

Note that the value of a function is initialised to zero every time the function is called and unless it is set to some value it will return a zero value. This makes error handling easy because we can just exit the function if an error is discovered. It is then the responsibility of the calling program code to check for a return value of zero which signifies an error.

This program illustrates one of the benefits of using subroutines and functions which is that when written and fully tested they can be treated as a trusted "black box" that does not have to be opened.

For this reason functions like this should be the properly tested and then, if possible, left untouched (in case you add some error).

There are a few features of this program that we have not covered before. The first is the MOD operator which will calculate the remainder of dividing one number into another. For example, if you divided 4 into 15 you would have a remainder of 3 which is exactly what the expression 15 MOD 4 will return. The `ABS()` function is also new and will return its argument as a positive number (eg, ABS(-15) will return +15 as will ABS(15)).

The EXIT FOR command will exit a FOR loop even though it has not reached the end of its looping, EXIT FUNCTION will immediately exit a function even though execution has not reached the end of the function and CONTINUE DO will immediately cause the program to jump to the end of a DO loop and execute it again.

Why would this program be useful? Well some people like to count their age in days, that way every day is a birthday! You can calculate your age in days, just enter the date that you were born and today's date. That is not particularly useful but the program itself is valuable as it demonstrates many of the characteristics of programming in MMBasic. So, work your way through the program and review each section until you understand it – it should be a rewarding experience.

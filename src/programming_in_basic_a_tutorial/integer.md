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
zero) - then finding the earliest of the two is just a matter of using an arithmetic compare in an `IF`
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



### Scientific Notation

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
point numbers. For example, if the above number was stored in a floating point variable the `PRINT`
command would display it as 7.5E+18 (this is BASIC’s way of representing 7.5 x 1018). As another
example, the number 0.0000000456 would display as 4.56E-8 which is the same as 4.56 x 10-8.

You can also use scientific notation when entering constant numbers in MMBasic. For example:

```basic
SandGrains = 7.5E+18
```

MMBasic only uses scientific notation for displaying floating point numbers (not integers). For
instance, if you assigned the number of grains of sand to an integer variable it would print out as a
normal number (with lots of zeros).

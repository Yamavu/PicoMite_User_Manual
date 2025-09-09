
## Variables

Before we go much further we need to define what a "variable" is as they are fundamental to the
operation of the BASIC language (in fact, most programming languages). A variable is simply a
place to store an item of data (ie, its "value"). This value can be changed as the program runs which
why it is called a "variable".

Variables in MMBasic can be one of three types. The most common is floating point and this is
automatically assumed if the type of the variable is not specified. The other two types are integer and
string and we will cover them later. A floating point number is an ordinary number which can contain
a decimal point. For example 3.45 or -0.023 or 100.00 are all floating point numbers.

A variable can be used to store a number and it can then be used in the same manner as the number
itself, in which case it will represent the value of the last number assigned to it.

As a simple example:

```basic
A = 3
B = 4
PRINT A + B
```

will display the number 7. In this case both A and B are variables and MMBasic used their current
values in the PRINT statement. MMBasic will automatically create a variable when it first encounters
it, so the statement A = 3 both created a floating point variable (the default type) with the name of A
and then it assigned the value of 3 to it.

The name of a variable must start with a letter while the remainder of the name can use letters,
numbers, the underscore or the full stop (or period) characters. The name can be up to 31 characters
long and the case (ie, capitals or not) is not important. Here are some examples:

* `Total_Count`
* `ForeColour`
* `temp3`
* `count`
* `x`
* `ThisIsAVeryLongVariableName`
* `increment.value`

You can change the value of a variable anywhere in your program by using the assignment command, ie:

```basic
variable = expression
```

For example:

```basic
temp3 = 24.6
count = 5
CTemp = (FTemp – 32) * 0.5556
```

In the last example both `CTemp` and `FTemp` are variables and this line converts the value of `FTemp`
(in degrees Fahrenheit) to degrees Celsius and stores the result in the variable `CTemp`.


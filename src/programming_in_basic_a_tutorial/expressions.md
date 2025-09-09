## Expressions

We have met the term ‘expression’ before in this tutorial and in programming it has a specific
meaning. It is a formula which can be resolved by the BASIC interpreter to a single number or value.

MMBasic will evaluate numeric expressions using the same rules that we learnt at school. For
example, multiplication and division are performed first followed by addition and subtraction. These
are called the rules of precedence and are fully described previously in this manual (see the chapter
Expressions and Operators).

This means that MMBasic will resolve `2 + 3 * 6` by first multiplying 3 by 6 giving 18 then adding 2
resulting in a final value of `20`. Similarly, both `5 * 4` and `10 + 4 * 3 – 2` will also resolve to `20`.

If you want to force the interpreter to evaluate parts of the expression first you can surround that part
of the expression with brackets. For example, `(10 + 4) * (3 – 2)` will resolve to `14` not `20` as would
have been the case if the brackets were not used. Using brackets does not appreciably slow down the
program so you should use them liberally if there is a chance that MMBasic will misinterpret your
intention.

As pointed out earlier, you can use variables in an expression exactly the same as straight numbers.

For example, this will increment the value of the variable temp by one:

```basic
temp = temp + 1
```

You can also use functions in expressions. These are special operations provided by MMBasic, for
example to calculate trigonometric values.

An example of using a function is the following which will print the length of the hypotenuse of a
right angled triangle. This uses the `SQR()` function which returns the square root of a number (a and
b are variables holding the lengths of the other sides):

```basic
PRINT SQR(a * a + b * b)
```

MMBasic will first evaluate this expression by multiplying a by a, then multiplying b by b, then
adding the results together. The resulting number is then passed to the `SQR()` function which will
calculate the square root of that number (ie, the hypotenuse) and return it for the PRINT command to
display.

Some other mathematical functions provided by MMBasic include:

* `SIN(r)` – the sine of r
* `COS(r)` – the cosine of r
* `TAN(r)` – the tangent of r

There are many more functions available to you and they are all listed earlier in this manual.

Note that in the above trigonometric functions the value passed to the function (ie, 'r') is the angle in
radians. In MMBasic you can use the function RAD(d) to convert an angle from degrees to radians
('d' is the angle in degrees).

Another feature of most programming languages (including BASIC) is that you can nest function calls
within each other. For example, given the angle in degrees (ie, 'd') the sine of that angle can be found
with this expression:

```basic
PRINT SIN(RAD(d))
```

In this case MMBasic will first take the value of d and convert it to radians using the `RAD()` function.

The output of this function then becomes the input to the `SIN()` function.


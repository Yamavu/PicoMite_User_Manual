## DIM Command

We have used the `DIM` command before for defining arrays but it can also be used to create ordinary
variables. For example, you can simultaneously create four string variables like this:

```basic
DIM STRING Car, Name, Street, City
```

Note that because these variables have been defined as strings using the `DIM` command we do not
need the $ suffix, the definition alone is enough for MMBasic to identify their type. Similarly, when
you use these variables in an expression you do not need the type suffix: For example:

```basic
City = "Sydney"
```

You can also use the keyword `INTEGER` to define a number of integer variables and `FLOAT` to do
the same for floating point variables. This type of notation can similarly be used to define arrays.

For example:

```basic
DIM INTEGER seconds(200)
```

Another method of defining the variables type is to use the keyword `AS`. For example:

```basic
DIM Car AS STRING, Name AS STRING, Street AS STRING
```

This is the method used by Microsoft (MMBasic tries to maintain Microsoft compatibility) and it is
useful if the variables have different types. For example:

```basic
DIM Car AS STRING, Age AS INTEGER, Value AS FLOAT
```

You can use any of these methods of defining a variable's type, they all act the same.


### Require explicit definitions

The advantage of defining variables using the `DIM` command is that they are clearly defined
(preferably at the start of the program) and their type (float, integer or string) is not subject to
misinterpretation.

You can strengthen this by using the following commands at the very top of your program:

```basic
OPTION EXPLICIT
OPTION DEFAULT NONE
```

The first specifies to MMBasic that all variables must be explicitly defined using `DIM` before they can
be used. The second specifies that the type of all variables must be specified when they are created.

Why are these two commands important?

The first can help avoid a common programming error which is where you accidently misspell a
variable's name. For example, your program might have the current temperature saved in a variable
called Temp but at one point you accidently misspell it as Tmp. This will cause MMBasic to
automatically create a variable called Tmp and set its value to zero.

This is obviously not what you want and it will introduce a subtle error which could be hard to find,
even if you were aware that something was not right. On the other hand, if you used the `OPTION EXPLICIT` command at the start of your program MMBasic would refuse to automatically create the
variable and instead would display an error thereby saving you from a probable headache.

The command `OPTION DEFAULT NONE` further helps because it tells MMBasic that the
programmer must specifically specify the type of every variable when they are declared. It is easy to
forget to specify the type and allowing MMBasic to automatically assume the type can lead to
unexpected consequences.

For small, quick and dirty programs, it is fine to allow MMBasic to automatically create variables but
in larger programs you should always disable this feature with `OPTION EXPLICIT` and strengthen it
with `OPTION DEFAULT NONE` .

When a variable is created it is set to zero for float and integers and an empty string (ie, contains no
characters) for a string variable. You can set its initial value to something else when it is created using
 `DIM` .


For example:

```basic
DIM FLOAT nbr = 12.56
DIM STRING Car = "Ford", City = "Perth"
```

You can also initialise arrays by placing the initialising values inside brackets like this:

```basic
DIM s$(2) = ("zero", "one", "two")
```

Note that because arrays start from zero by default this array actually has three elements with the
index numbers of 0, 1 and 2. This is why we needed three string constants to initialise it.

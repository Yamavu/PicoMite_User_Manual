

### DIM [type] decl [,decl].. 

Declares one or more variables (i.e. makes the variable name and its characteristics known to the interpreter).

where 'decl' is:

`var [length] [type] [init]`

'var' is a variable name with optional dimensions 

'length' is used to set the maximum size of the string to 

'n' as in LENGTH n

'type' is one of FLOAT or INTEGER or STRING (the type can be prefixed by the keyword AS - as in AS FLOAT)

'init' is the value to initialise the variable and consists of: 
`= <expression>`

For a simple variable one expression is used, for an array a list of comma separated expressions surrounded by brackets is used.

Examples:
```basic
DIM nbr(50)
DIM INTEGER nbr(50)
DIM name AS STRING
DIM a, b$, nbr(100), strn$(20)
DIM a(5,5,5), b(1000)
DIM strn$(200) LENGTH 20
DIM STRING strn(200)
LENGTH 20
DIM a = 1234, b = 345
DIM STRING strn = "text"
DIM x%(3) = (11, 22, 33, 44)
```

When [OPTION EXPLICIT](../option/explicit.md) is used (as recommended) the DIM, LOCAL or STATIC commands are the only way that a variable can be created. If this option is not used then using the DIM command is optional and if not used the
variable will be created automatically when first referenced.

The type of the variable (i.e. string, float or integer) can be specified in one of three ways:

* By using a type suffix (i.e. !, % or $ for float, integer or string). 
  * For example: `DIM nbr%, amount!, name$`
* By using one of the keywords FLOAT, INTEGER or STRING immediately after the command DIM and before the variable(s) are listed. The specified type then applies to all variables listed (i.e. it does not have to be repeated).
  * For example: `DIM STRING first_name, last_name, city`
* By using the Microsoft convention of using the keyword `AS` and the type keyword (i.e. FLOAT, INTEGER or STRING) after each variable. If you use this method the type must be specified for each variable and can be changed from variable to variable.
  * For example: `DIM amount AS FLOAT, name AS STRING`
  
Floating point or integer variables will be set to zero when created and strings will be set to an empty string (i.e. ""). 

You can initialise the value of the variable by using an equals symbol (=) and an expression following the variable definition. For example:

```basic
DIM STRING city = "Perth", house = "Brick"
```

The initialising value can be an expression (including other variables) and will be evaluated when the DIM command is executed. See the chapter Defining and Using Variables for more examples of the syntax. As well as declaring simple variables the DIM command will also declare arrayed variables (i.e. an indexed variable with a number of dimensions).

Following the variable's name the dimensions are specified by a list of numbers separated by commas and enclosed in brackets. For example:

```basic
DIM array(10, 20)
```

Each number specifies the index range in each dimension. Normally the indexing of each dimension starts at 0 but the OPTION BASE command can be used to change this to 1.

The above example specifies a two dimensional array with 11 elements (0 to 10) in the first dimension and 21 (0 to 20) in the second dimension. The total number of elements is 231 and because each floating point number requires 8 bytes a total of 1848 bytes of memory will be allocated.

Strings will default to allocating 255 bytes (i.e. characters) of memory for each element and this can quickly use up memory when defining arrays of strings.

In that case the LENGTH keyword can be used to specify the amount of memory to be allocated to each element and therefore the maximum length of the string that can be stored. This allocation ('n') can be from 1 to 255 characters.

For example: `DIM STRING s(5, 10)` will declare a string array with 66 elements consuming 16,896 bytes of memory while: `DIM STRING s(5, 10) LENGTH 20` Will only consume 1,386 bytes of memory.

Note that the amount of memory allocated for each element is n + 1 as the extra byte is used to track the actual length of the string stored in each element.

If a string longer than 'n' is assigned to an element of the array an error will be produced. Other than this, string arrays created with the LENGTH keyword act exactly the same as other string arrays. This keyword can also be used with non-array string variables but it will not save any memory.

In the above example you can also use the Microsoft syntax of specifying the type after the length qualifier. For example:

```basic
DIM s(5, 10) LENGTH 20 AS STRING
```

Arrays can also be initialised when they are declared by adding an equals symbol (=) followed by a bracketed list of values at the end of the declaration.

For example:
```basic
DIM INTEGER nbr(4) = (22, 44, 55, 66, 88)
```
or
```basic
DIM s$(3) = ("foo", "boo", "doo", "zoo")
```

Note that the number of initialising values must match the number of elements in the array including the base value set by OPTION BASE. If a multi dimensioned array is initialised then the first dimension will be initialised first followed by the second, etc.

Also note that the initialising values must be after the LENGTH qualifier (if used) and after the type declaration (if used).

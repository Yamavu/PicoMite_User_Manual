

### DIM [type] decl [,decl].. where 'decl' is: var [length] [type] [init] 'var' is a variable name with optional dimensions 'length' is used to set the maximum size of the string to 'n' as in LENGTH n 'type' is one of FLOAT or

 Declares one or more variables (i.e. makes the variable name and its characteristics known to the interpreter). When OPTION EXPLICIT is used (as recommended) the DIM, LOCAL or STATIC commands are the only way that a variable can be created. If this option is not used then using the DIM command is optional and if not used the variable will be created automatically when first referenced. The type of the variable (i.e. string, float or integer) can be specified in one of three ways: By using a type suffix (i.e. !, % or $ for float, integer or string). For example:

### DIM nbr(50)

 variable definition. For example: DIM STRING city = "Perth", house = "Brick"

### DIM INTEGER nbr(50)

 The initialising value can be an expression (including other variables) and will

### DIM name AS STRING

 be evaluated when the DIM command is executed. See the chapter Defining

### DIM a, b$, nbr(100), strn$(20)

 and Using Variables for more examples of the syntax.

### DIM a(5,5,5), b(1000)

 As well as declaring simple variables the DIM command will also declare

### DIM strn$(200) LENGTH 20

 arrayed variables (i.e. an indexed variable with a number of dimensions).

### DIM STRING strn(200)

 Following the variable's name the dimensions are specified by a list of numbers

### DIM a = 1234, b = 345

 DIM array(10, 20)

### DIM STRING strn = "text"

 Each number specifies the index range in each dimension. Normally the indexing of each dimension starts at 0 but the OPTION BASE command can

### DIM x%(3) = (11, 22, 33, 44)

 be used to change this to 1. The above example specifies a two dimensional array with 11 elements (0 to 10) in the first dimension and 21 (0 to 20) in the second dimension. The total
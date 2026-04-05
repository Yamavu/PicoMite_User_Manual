### STR$( number ) or STR$( number, m ) or STR$( number, m, n ) or STR$( number, m, n, c$ )

Returns a string in the decimal (base 10) representation of `number`.

If `m` is specified sufficient spaces will be added to the start of the number to
ensure that the number of characters before the decimal point (including the
negative or positive sign) will be at least `m` characters. If `m` is zero or the

number has more than `m` significant digits no padding spaces will be added.


If `m` is negative, positive numbers will be prefixed with the plus symbol and
negative numbers with the negative symbol. If `m` is positive then only the
negative symbol will be used.

`n` is the number of digits required to follow the decimal place. If it is zero the
string will be returned without the decimal point. If it is negative the output
will always use the exponential format with `n` digits resolution. If `n` is not
specified the number of decimal places and output format will vary
automatically according to the number.

`c$` is a string and if specified the first character of this string will be used as
the padding character instead of a space (see the `m` argument). 

Examples:

Command                    | result
:-:vvvv                    | :-:
STR$(123.456)              | "123.456"
STR$(-123.456)             | "-123.456"
STR$(123.456, 1)           | "123.456"
STR$(123.456, -1)          | "+123.456"
STR$(123.456, 6)           | "   123.456"
STR$(123.456, -6)          | " +123.456"
STR$(-123.456, 6)          | " -123.456"
STR$(-123.456, 6, 5)       | " -123.45600"
STR$(-123.456, 6, -5)      | "    -1.23456e+02"
STR$(53, 6)                | "    53"
STR$(53, 6, 2)             | "    53.00"
STR$(53, 6, 2, "*")        | "****53.00"


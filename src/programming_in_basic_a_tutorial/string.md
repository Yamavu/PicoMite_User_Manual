## String

Strings are another variable type (like floating point and integers). Strings are used to hold a sequence of characters.

For example, in the command:

```basic
PRINT "Hello"
```

The string "Hello" is a string constant. Note that a constant is something that does not change (as
against a variable, which can) and that string constants are always surrounded by double quotes.

String variables names use the dollar symbol ($) as a suffix to identify them as a string instead of a normal floating point variable and you can use ordinary assignment to set their value. The following are examples (note that the second example uses an array of strings):

```basic
Car$ = "Holden"
Country$(12) = "India"
Name$ = "Fred"
```

You can also join strings using the plus operator:

```basic
Word1$ = "Hello"
Word2$ = "World"
Greeting$ = Word1$ + " " + Word2$
```

In which case the value of Greeting$ will be "Hello World".

Strings can also be compared using operators such as = (equals), <> (not equals), < (less than), etc.

For example:

```basic
IF Car$ = "Holden" THEN PRINT "Was an Aussie made car"
```

The comparison is made using the full ASCII character set so a space will come before a printable
character. Also the comparison is case sensitive so 'holden' will not equal "Holden". Using the
function `UCASE()` to convert the string to upper case you can then have a case insensitive
comparison. For example:

```basic
IF UCASE$(Car$) = "HOLDEN" THEN PRINT "Was an Aussie made car"
```

## Long Strings

The maximum length of a standard string is 255, longer character sequences can be declared as [long strings](../long_strings.md).

## Arrays of Strings

You can have arrays of strings but you need to be careful when you declare them as you can rapidly
run out of RAM (general memory used for storing variables, etc). This is because MMBasic will by
default allocate 255 bytes of RAM for each element of the array. 

For example, a string array with 100 elements will by default use 25K of RAM.

To alleviate this you can use the `LENGTH` qualifier to limit the maximum size of each element. For instance, if you know that the maximum length of any string that will be stored in the array will be less than 20 characters you can use the following declaration to allocate just 20 bytes for each element:

```basic
DIM MyArray$(100) LENGTH 20
```

The resultant array will only use 2K of RAM.

Note that sometimes people think that by using the `LENGTH` qualifier when declaring a normal (non
array) string variable they will save some RAM. This is not correct; they always occupy 256 bytes.

### Manipulating Strings

String handling is one of MMBasic's strengths and using a few simple functions you can pull apart
and generally manipulate strings. The basic string functions are:

Command | Description 
:- | :-
`LEFT$(string$, nbr )` | Returns a substring of string$ with nbr of characters from the left (beginning) of the string.
`RIGHT$(string$, nbr )` | Same as the above but return nbr of characters from the right (end) of the string.
`MID$(string$, pos, nbr )` | Returns a substring of string$ with nbr of characters starting from the character pos in the string (ie, the middle of the string).

For example if S$ = "This is a string"
- then: `R$ = LEFT$(S$, 7)` would result in the value of R$ being set to: "This is"
- and: `R$ = RIGHT$(S$, 8)` would result in the value of R$ being set to: "a string"
- finally: `R$ = MID$(S$, 6, 2)` would result in the value of R$ being set to: "is"

Note that in `MID$()` the first character position in a string is number 1, the second is number 2 and so
on. So, counting the first character as one, the sixth position is the start of the word "is".


## Searching Strings

Another useful function is: `INSTR(string$, pattern$ )` , which returns a number representing the position at which `pattern$` occurs in `string$`.

This can be used to search for a string inside another string. The number returned is the position of
the substring inside the main string. Like with `MID$()` the start of the string is position 1.

For example if `S$ = "This is a string"` Then: `pos = INSTR(S$, " ")` would result in pos being set to the position of the first space in S$ (ie, 5).

`INSTR()` can be combined with other functions so this would return the first word in S$:

```basic
R$ = LEFT$(S$, INSTR(S$, " ") - 1)
```

### Searching from a starting point

There is also an extended version of `INSTR()`:

```basic
INSTR(pos, string$, pattern$ )
```

Returns a number representing the position at which pattern$ occurs in string$ when starting the search at the character position pos.


So we can find the second word in S$ using the following:

```basic
pos = INSTR(S$, " ")
R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
```

This last example is rather complicated so it might be worth working through it in detail so that you
can understand how it works.

Note that `INSTR()` will return the number zero if the sub string is not found and that any string
function will throw an error (and halt the program) if that is used as a character position. So, in a
practical program you would first check for zero being returned by `INSTR()` before using that value.

For example:

```basic
pos = INSTR(S$, " ")
if pos > 0 THEN R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
```

### Searching using Regular expressions

see [Appendix E – Regex Syntax](../E_regex_syntax.md)

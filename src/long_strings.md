# Long Strings

Long Strings are a set of commands and functions that allow MMBasic to manipulate strings of unlimited
length and are particularly useful when dealing with data sent via WiFi and the Internet. Standard strings in
MMBasic are limited to a maximum length of 255 characters. Long strings duplicate these functions but will
work with strings of any length limited only by the amount of available RAM.

Long String Variables
Variables for holding long strings must be defined as integer arrays. The long string routines do not keep
numbers in these arrays but just use them as blocks of memory for holding long strings.
When creating these arrays they should be defined as single dimensioned integer arrays with the number of
elements set to the number of characters required for the maximum string length divided by eight. The reason
for dividing by eight is that each integer in an MMBasic array occupies eight bytes.
The following is an example of declaring three long string variables which will be used to hold up to 2048
characters in each:
CONST MaxLen = 2048
DIM INTEGER Str1(MaxLen/8), Str2(MaxLen/8), Str3(MaxLen/8)

These will contain empty strings when created (ie, their length will be zero). When these variables are passed
to the long string functions they should be entered as the variable name followed by empty brackets. For
example:
LONGSTRING COPY Str1(), Str2()

Long string variables can be passed as arguments to user defined subroutines and functions. For example:
Sub MySub longarg() AS INTEGER
PRINT "Long string length is" LLEN(longarg())
END SUB

And it could be called like this:
MySub str1()

Summary of the Commands and Functions
These are documented in detail in the Commands and Functions sections of this manual. The commands are:
LONGSTRING AES128 ENCRYPT/DECRYPT
Encrypts or decrypts a long string
LONGSTRING APPEND array%(), string$
Append an ordinary string to a long string
LONGSTRING BASE64 ENCODE/DECODE
Encodes or decodes a long string using base 64
LONGSTRING CLEAR array%()
Clear (ie, set to empty) a long string
LONGSTRING COPY dest%(), src%()
Copy a long string
LONGSTRING CONCAT dest%(), src%()
Concatenate two long strings
LONGSTRING LCASE array%()
Convert a long string to lowercase
LONGSTRING LEFT dest%(), src%(), nbr
Get the left nbr characters from a long string
LONGSTRING LOAD array%(), nbr, string$
Copy characters to a long string
LONGSTRING MID dest%(), src%(), start, nbr
Get characters from the middle of a long string
LONGSTRING PRINT [#n,] src%() [;]
Print a long string
LONGSTRING REPLACE array%() , string$, start
Replace characters in a long string
LONGSTRING RESIZE addr%(), nbr
Set the length of a long string
LONGSTRING RIGHT dest%(), src%(), nbr
Get the right nbr characters from a long string
LONGSTRING SETBYTE addr%(), nbr, data
Set a byte in a long string
LONGSTRING TRIM array%(), nbr
Trim characters from the left of a long string
LONGSTRING UCASE array%()
Convert a long string to uppercase
The functions are:
r = LGETBYTE(array%(), n)
Return the value of a byte in a long string
r$ = LGETSTR$(array%(), start, length)
Returns part of a long string as a normal string.
r = LINSTR(array%(), search$ [,start] [,size])
Returns the position of a string in a long string
r = LLEN(array%())
Returns the length of a long string
MATH(BASE64 ENCODE/DECODE)
Encodes or decodes data using base 64
PicoMite User Manual
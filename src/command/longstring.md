### LONGSTRING

The LONGSTRING commands allow for the manipulation of strings longer than the normal MMBasic limit of 255 characters. Variables for holding long strings must be defined as single dimensioned integer arrays with the number of elements set to the number of characters required for the maximum string length divided by eight. The reason for dividing by eight is that each integer in an MMBasic array occupies eight bytes. Note that the long string routines do not check for overflow in the length of the strings. If an attempt is made to create a string longer than a long string variable's size the outcome will be undefined.

#### Basic Operations
{{#include longstring_clear.md}}
{{#include longstring_copy.md}}
{{#include longstring_concat.md}}
{{#include longstring_append.md}}
{{#include longstring_load.md}}

#### String Manipulation
{{#include longstring_left.md}}
{{#include longstring_mid.md}}
{{#include longstring_right.md}}
{{#include longstring_trim.md}}

#### Case Conversion
{{#include longstring_lcase.md}}
{{#include longstring_ucase.md}}

#### Encoding and Encryption
{{#include longstring_aes128.md}}
{{#include longstring_base64.md}}

#### Output
{{#include longstring_print.md}}

#### Advanced Operations
{{#include longstring_replace.md}}
{{#include longstring_resize.md}}
{{#include longstring_setbyte.md}} 

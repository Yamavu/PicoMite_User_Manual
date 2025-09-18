## Trigonometric Functions

### ACOS( number )

Returns the inverse cosine of the argument `number` in radians.


### SIN( number )

Returns the sine of the argument `number` in radians.


### ASIN( number )

Returns the inverse sine value of the argument `number` in radians.


### TAN( number )

Returns the tangent of the argument `number` in radians.


### ATN( number )

Returns the arctangent of the argument `number` in radians.


### ATAN2( y, x )

Returns the arc tangent of the two numbers x and y as an angle expressed in
radians.

It is similar to calculating the arc tangent of y / x, except that the signs of
both arguments are used to determine the quadrant of the result.


### COS( number )

Returns the cosine of the argument `number` in radians.


### DEG( radians )

Converts `radians` to degrees.


### RAD( degrees )

Converts `degrees` to radians.


## String Functions


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
the padding character instead of a space (see the `m` argument). Examples:
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


### UCASE$( string$ )

Returns `string$` converted to uppercase characters.


### LCASE$( string$ )

Returns `string$` converted to lowercase characters.


### ASC( string$ )

Returns the ASCII code (i.e. byte value) for the first letter in `string$`.


### CHR$( number )

Returns a one-character string consisting of the character corresponding to the
ASCII code (i.e. byte value) indicated by argument `number`.


### VAL( string$ )

Returns the numerical value of the `string$`. If `string$` is an invalid number
the function will return zero.

This function will recognise the &H prefix for a hexadecimal number, &O for
octal and &B for binary.


### STRING$( nbr, ascii ) or STRING$( nbr, string$ )

Returns a string `nbr` bytes long consisting of either the first character of string$
or the character representing the ASCII value `ascii` which is an integer or float
number in the range of 0 to 255.


### LEFT$( string$, nbr )

Returns a substring of `string$` with `nbr` of characters from the left
(beginning) of the string.


### MID$( string$, start ) or MID$( string$, start, nbr )

Returns a substring of `string$` beginning at `start` and continuing for `nbr`
characters. The first character in the string is number 1.

If `nbr` is omitted the returned string will extend to the end of `string$`


### RIGHT$( string$, number-of- chars )

Returns a substring of `string$` with `number-of-chars` from the right (end) of
the string.


### LEN( string$ )

Returns the number of characters in `string$`.


### SPACE$( number )

Returns a string of blank spaces `number` characters long.


### TAB( number )

Outputs spaces until the column indicated by `number` has been reached on the
console output.


### JSON$(array%(), string$)

Returns a string representing a specific item out of the JSON input stored in the
longstring array%(). Note that many JSON data sets are quite large and may be
too big to parse with the memory available.

Examples (taken from api.openweathermap.org):

```basic
JSON$(a%(), “name”)
JSON$(a%(), “coord.lat”)
JSON$(a%(), “weather[0].description”)
JSON$(a%(),”list[4].weather[0].description
```


## Binary Functions

### BIT(var%, bitno)

'returns the value of a specific bit (0-63) in an integer variable (0 or 1).

See also the [BIT command](../command/bit.md)

### BIN$( number [, chars])

Returns a string giving the binary (base 2) value for the `number`.

`chars` is optional and specifies the number of characters in the string with zero
as the leading padding character(s).


### BIN2STR$(type, value [,BIG])

Returns a string containing the binary representation of `value`.

`type` | description
:-: | :-
INT64 | signed 64-bit integer converted to an 8 byte string
UINT64 | unsigned 64-bit integer converted to an 8 byte string
INT32 | signed 32-bit integer converted to a 4 byte string
UINT32 | unsigned 32-bit integer converted to a 4 byte string
INT16 | signed 16-bit integer converted to a 2 byte string
UINT16 | unsigned 16-bit integer converted to a 2 byte string
INT8 | signed 8-bit integer converted to a 1 byte string
UINT8 | unsigned 8-bit integer converted to a 1 byte string
SINGLE | single precision floating point number converted to a 4 byte string
DOUBLE | double precision floating point number converted to a 8 byte string

By default the string contains the number in little-endian format (i.e. the least
significant byte is the first one in the string). Setting the third parameter to
`BIG` will return the string in big-endian format (i.e. the most significant byte
is the first one in the string). In the case of the integer conversions, an error
will be generated if the `value` cannot fit into the `type` (eg, an attempt to store
the value 400 in a INT8).

This function makes it easy to prepare data for efficient binary file I/O or for
preparing numbers for output to sensors and saving to flash memory.

See also the function STR2BIN


### STR2BIN(type, string$ [,BIG])

Returns a number equal to the binary representation in `string$`.

`type` can be:
* INT64 converts 8 byte string representing a signed 64-bit integer to an integer
* UINT64 converts 8 byte string representing an unsigned 64-bit integer to an integer
* INT32 converts 4 byte string representing a signed 32-bit integer to an integer
* UINT32 converts 4 byte string representing an unsigned 32-bit integer to an integer
* INT16 converts 2 byte string representing a signed 16-bit integer to an integer
* UINT16 converts 2 byte string representing an unsigned 16-bit integer to an integer
* INT8 converts 1 byte string representing a signed 8-bit integer to an integer
* UINT8 converts 1 byte string representing an unsigned 8-bit integer to an integer
* SINGLE converts 4 byte string representing single precision float to a float
* DOUBLE converts 8 byte string representing single precision float to a float

By default the string must contain the number in little-endian format (i.e. the
least significant byte is the first one in the string). Setting the third parameter
to `BIG` will interpret the string in big-endian format (i.e. the most
significant byte is the first one in the string).

This function makes it easy to read data from binary data files, interpret
numbers from sensors or efficiently read binary data from flash memory
chips.

An error will be generated if the string is the incorrect length for the
conversion requested

See also the function BIN2STR$


### BYTE(var$, byteno)

Returns the integer value of a specific byte in a string (0-255). This is the
equivalent of ASC(MID$(var$,byteno,1)) but operates much faster.

See also the [BYTE command](../command/byte.md)


### HEX$( number [, chars])

Returns a string giving the hexadecimal (base 16) value for the `number`.

`chars` is optional and specifies the number of characters in the string with zero
as the leading padding character(s).


### OCT$( number [, chars])

Returns a string giving the octal (base 8) representation of `number`.

`chars` is optional and specifies the number of characters in the string with zero
as the leading padding character(s).


## MMBasic Functions

### CALL(userfunname$, [,userfunparameters,..])

This is an efficient way of programmatically calling user defined functions.

(See also the CALL command). In many cases it can be used to eliminate
complex SELECT and IF THEN ELSEIF ENDIF clauses and is processed in a
much more efficient manner.

`userfunname$` can be any string or variable or function that resolves to the
name of a normal user function (not an in-built command).

`userfunparameters` are the same parameters that would be used to call the
function directly.

A typical use for this command could be writing any sort of emulator where
one of a large number of functions should be called depending on a some
variable. It also provides a method of passing a function name to another
subroutine or function as a variable.


### CHOICE(condition, ExpressionIfTrue, ExpressionIfFalse)

This function allows you to do simple either/or selections more efficiently and
faster than using IF THEN ELSE ENDIF clauses.

The condition is anything that will resolve to nonzero (true) or zero (false).

The expressions are anything that you could normally assign to a variable or
use in a command and can be integers, floats or strings.

Examples:
- `PRINT CHOICE(1, "hello","bye")` will print `"Hello"`
- `PRINT CHOICE (0, "hello","bye")` will print `"Bye"`
- `a=1 : b=1 : PRINT CHOICE (a=b, 4, 5)` will print `4`


### EVAL( string$ )

Will evaluate `string$` as if it is a BASIC expression and return the result.

`string$` can be a constant, a variable or a string expression. The expression can
use any operators, functions, variables, subroutines, etc that are known at the
time of execution. The returned value will be an integer, float or string
depending on the result of the evaluation.

For example: S$ = "COS(RAD(30)) * 100" : PRINT EVAL(S$)
Will display: 86.6025


## Time and Date Functions

### DATE$

Returns the current date based on MMBasic’s internal clock as a string in the
form "DD-MM-YYYY". For example, "28-07-2012".


### DATETIME$(n)

Returns the date and time corresponding to the epoch number `n` (number of
seconds that have elapsed since midnight GMT on January 1, 1970).

The format of the returned string is “dd-mm-yyyy hh:mm:ss”. Use the text
NOW to get the current datetime string, ie, DATETIME$(NOW)


### DAY$(date$)

Returns the day of the week for a given date as a string.

For example, “Monday”, “Tuesday” etc.

`date$` is a string and its format can be DD-MM-YY or DD-MM-YYYY or
YYYY-MM-DD. You can also use NOW to get the day for the current date,
eg, PRINT DAY$(NOW)


### EPOCH(DATETIME$)

Returns the epoch number (number of seconds that have elapsed since midnight
GMT on January 1, 1970) for the supplied DATETIME$ string.

The format for DATETIME$ is “dd-mm-yyyy hh:mm:ss”, “dd-mm-yy
hh:mm:ss”, or “yyyy-mm-dd hh:mm:ss”,. Use NOW to get the epoch number
for the current date and time, i.e. PRINT EPOCH(NOW)


### TIME$

Returns the current time based on MMBasic's internal clock as a string in the
form "HH:MM:SS" in 24 hour notation. For example, "14:30:00".

To set the current time use the command TIME$ = .


### TIMER

Returns the elapsed time in milliseconds (eg, 1/1000 of a second) since reset.

The timer is reset to zero on power up or a CPU restart and you can also reset it
by using TIMER as a command. If not specifically reset it will continue to
count up forever (it is a 64 bit number and therefore will only roll over to zero
after 200 million years).


## DEVICE functions

### DEVICE(GAMEPAD channel, funct)

Returns data from a USB PS3 or PS4 controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    LX the position of the analog left joystick x axis
    LY the position of the analog left joystick y axis
    RX the position of the analog right joystick x axis
    RY the position of the analog right joystick y axis
    GX the reading from the X axis gyro (where supported)
    GY the reading from the Y axis gyro (where supported)
    GZ the reading from the Z axis gyro (where supported)
    AX the reading from the X axis accelerometer (where supported)
    AY the reading from the Y axis accelerometer (where supported)
    AZ the reading from the Z axis accelerometer (where supported)
    L        the position of the analog left button
    R        the position of the analog right button
    B        a bitmap of the state of all the buttons. A bit will be set to 1 if the
             button is pressed.

    T        the ID code of the controller
The button bitmap is as follows:
    BIT 0 Button R/R1
    BIT 1 Button start/options
    BIT 2 Button home
    BIT 3 Button select/share
    BIT 4 Button L/L1
    BIT 5 Button down cursor
    BIT 6 Button right cursor
    BIT 7 Button up cursor
    BIT 8 Button left cursor
    BIT 9 Right shoulder button 2/R2
    BIT 10 Button x/triangle
    BIT 11 Button a/circle
    BIT 12 Button y/square
    BIT 13 Button b/cross
    BIT 14 Left should button 2/L2
    BIT 15 Touchpad


### DEVICE(MOUSE channel, funct)

Returns data from a mouse connected via `channel`.

A PS2 mouse is always allocated channel 2. Normally a USB mouse is also
allocated to channel 2 but this can vary. See MM.INFO(USB n) for more
information.


### DEVICE(WII [CLASSIC] funct)

Returns data from a Wii Classic controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    LX the position of the analog left joystick x axis
    LY the position of the analog left joystick y axis
    RX the position of the analog right joystick x axis
    RY the position of the analog right joystick y axis
    L        the position of the analog left button
    R        the position of the analog right button
    B        a bitmap of the state of all the buttons. A bit will be set to 1 if the
             button is pressed.

    T        the ID code of the controller - should be hex &HA4200101
The button bitmap is as follows:
    BIT 0        Button R
    BIT 1        Button start
    BIT 2        Button home
    BIT 3        Button select
    BIT 4        Button L
    BIT 5        Button down cursor
    BIT 6        Button right cursor
    BIT 7        Button up cursor
    BIT 8        Button left cursor
    BIT 9        Button ZR
    BIT 10 Button x
    BIT 11 Button a
    BIT 12 Button y
    BIT 13 Button b
    BIT 14 Button ZL


### DEVICE(WII NUNCHUCK funct)

Returns data from a Wii Nunchuck controller.

`funct` is a 1 or 2 letter code indicating the information to return as follows:
    AX the x axis acceleration
    AY the y axis acceleration
    AZ the z axis acceleration
    JX the position of the joystick x axis
    JY the position of joystick y axis
    C       the state of the C button
    Z       the state of the Z button
    T       the ID code of the controller - should be hex &HA4200000



### FIELD$( string1, nbr, string2 [, string3] )

Returns a particular field in a string with the fields separated by delimiters.

Note that a space character cannot be used as a delimeter.

`nbr` is the field to return (the first is nbr 1). `string1` is the string to search and
`string2` is a string holding the delimiters (more than one can be used). The
space character may not be used as a delimiter.

`string3` is optional and if specified will include characters that are used to
quote text in `string1` (ie, quoted text will not be searched for a delimiter).

For example:
S$ = "foo, boo, zoo, doo"
r$ = FIELD$(s$, 2, ",")
will result in r$ = "boo". While:
s$ = "foo, 'boo, zoo', doo"
r$ = FIELD$(s$, 2, ",", "'")
will result in r$ = "boo, zoo".


### FLAG(n%)

Returns the value (0 or 1) of the bit n% (0-63) in the system flag register.

See also MM.FLAGS and the FLAG and FLAGS commands


### FORMAT$( nbr [, fmt$] )

Will return a string representing `nbr` formatted according to the specifications
in the string `fmt$`.

The format specification starts with a % character and ends with a letter.

Anything outside of this construct is copied to the output as is.

The structure of a format specification is:
              % [flags] [width] [.precision] type
Where `flags` can be:
     -         Left justify the value within a given field width
     0         Use 0 for the pad character instead of space
     +         Forces the + sign to be shown for positive numbers
     space Causes a positive value to display a space for the sign. Negative
               values still show the – sign
`width` is the minimum number of characters to output, less than this the
number will be padded, more than this the width will be expanded.

`precision` specifies the number of fraction digits to generate with an e, or f
type or the maximum number of significant digits to generate with a g type and
defaults to 4 digits. If specified, the precision must be preceded by a dot (.).


### GETSCANLINE

This will report on the line that is currently being drawn on the VGA monitor
in the range of 0 to 525. This is irrespective of the current MODE.

Using this to time updates to the screen can avoid timing effects caused by
updates while the screen is being updated.

The first visible line will return a value of 0. Any line number above 479 is in
the frame blanking period.

## GPS functions

The GPS functions are used to return data from a serial communications
channel opened as GPS.

The function GPS(VALID) should be checked before any of these functions are
used to ensure that the returned value is valid.


### GPS(ALTITUDE)

Returns current altitude (if sentence GGA is enabled).


### GPS(DATE)

Returns the normal date string corrected for local time eg, “12-01-2020”.


### GPS(DOP)

Returns DOP (dilution of precision) value (if sentence GGA is enabled).


### GPS(FIX) GPS(GEOID)

Returns non zero (true) if the GPS has a fix on sufficient satellites and is
producing valid data.

Returns the geoid-ellipsoid separation (if sentence GGA is enabled).


### GPS(LATITUDE)

Returns the latitude in degrees as a floating point number, values are negative
for South of equator


### GPS(LONGITUDE)

Returns the longitude in degrees as a floating point number, values are
negative for West of the meridian.


### GPS(SATELLITES)

Returns number of satellites in view (if sentence GGA is enabled).


### GPS(SPEED)

Returns the ground speed in knots as a floating point number.


### GPS(TIME)

Returns the normal time string corrected for local time eg, “12:09:33”.


### GPS(TRACK)

Returns the track over the ground (degrees true) as a floating point number.


### GPS(VALID)

Returns: 0=invalid data, 1=valid data



### INKEY$

Checks the console input buffer and, if there is one or more characters waiting
in the queue, will remove the first character and return it as a single character in
a string.

If the input buffer is empty this function will immediately return with an empty
string (i.e. "").


### INPUT$(nbr, [#]fnbr)

Will return a string composed of `nbr` characters read from a file or serial
communications port opened as `fnbr`. This function will return as many
characters as are in the file or receive buffer up to `nbr`. If there are no
characters available it will immediately return with an empty string.

#0 can be used which refers to the console's input buffer.

The # is optional. Also see the OPEN command.


### INSTR( [start-position,] string-searched$, string- pattern$ [,size] )

Returns the position at which `string-pattern$` occurs in `string-searched$`,
beginning at `start-position`. If `start-position` is not provided it will default to 1.

Both the position returned and `start-position` use 1 for the first character, 2 for
the second, etc.

The function returns zero if `string-pattern$` is not found.

If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.


### KEYDOWN(n)

Return the decimal ASCII value of the USB keyboard key that is currently held
down or zero if no key is down. The decimal values for the function and arrow
keys are listed in Appendix F.

This function will report multiple simultaneous key presses and the parameter
`n` is the number of the keypress to report. KEYDOWN(0) will return the
number of keys being pressed
For example, if "c", "g" and "p" are pressed simultaneously KEYDOWN(0)
will return 3, KEYDOWN(1) will return 99, KEYDOWN(2) will return 103,
etc. The keys do not need to be pressed simultaneously and will report in the
order pressed. Taking a finger off a key will promote the next key pressed to
#1.

The first key (`n` = 1) is entered in the keyboard buffer (accessible using
INKEY$) while keys 2 to 6 can only be accessed via this function. Using this
function will clear the console input buffer.

KEYDOWN(7) will give any modifier keys that are pressed. These keys do not
add to the count in keydown(0)
The return value is a bitmask as follows:
lalt = 1, lctrl = 2, lgui = 4, lshift = 8, ralt = 16, rctrl = 32, rgui = 64, rshift = 128
KEYDOWN(8) will give the current status of the lock keys. These keys do not
add to the count in keydown(0)
The return value is a bitmask as follows:
caps_lock = 1, num_lock = 2, scroll_lock = 4
Note that some keyboards will limit the number of active keys that they can
report on.


## Longstring functions

### LCOMPARE(array1%(), array2%())

Compare the contents of two long string variables `array1%()` and `array2%()`.

The returned is an integer and will be -1 if `array1%()` is less than `array2%()`.

It will be zero if they are equal in length and content and +1 if `array1%()` is
greater than `array2%()`. The comparison uses the ASCII character set and is
case sensitive.


### LGETBYTE(array%(), n)

Returns the numerical value of the `n`th byte in the LONGSTRING held in
`array%()`. This function respects the setting of OPTION BASE in determining
which byte to return.


### LGETSTR$(array%(), start, length)

Returns part of a long string stored in `array%()` as a normal MMBasic string.

The parameters start and length define the part of the string to be returned.


### LINSTR(array%(), search$ [,start] [,size]))

Returns the position of a search string in a long string.

The returned value is an integer and will be zero if the substring cannot be
found. `array%()` is the string to be searched and must be a long string
variable. `search$` is the substring to look for and it must be a normal
MMBasic string or expression (not a long string). The search is case sensitive.

Normally the search will start at the first character in ' array%()' but the
optional third parameter allows the start position of the search to be specified.

If the optional parameter `size` is specified the `search$` is treated as a regular
expression. See Appendix E for the details.


### LLEN(array%())

Returns the length of a long string stored in `array%()`.


## File and Memory Functions

### CWD$

Returns the current working directory on the Flash Filesystem or SD Card.

Invalid for exFAT format.

The format is: A:/dir1/dir2.


### DIR$( fspec, type ) or DIR$( fspec ) or DIR$( )

Will search the default Flash Filesystem or SD Card for files and return the
names of entries found.

`fspec` is a file specification using wildcards the same as used by the FILES
command. Eg, "*.*" will return all entries, "*.TXT" will return text files. Note
that the wildcard *.* does not find files or folders without an extension.

`type` is the type of entry to return and can be one of:
      ALL          Search for all files and directories
      DIR          Search for directories only
      FILE         Search for files only (the default if `type` is not specified)
The function will return the first entry found. To retrieve subsequent entries
use the function with no arguments. i.e. DIR$( ). The return of an empty
string indicates that there are no more entries to retrieve.

This example will print all the files in a directory:
       f$ = DIR$("*.*", FILE)
       DO WHILE f$ <> ""
           PRINT f$
           f$ = DIR$()
       LOOP
You must change to the required directory before invoking this command.


### EOF( [#]fnbr )

Will return true if the file previously opened on the Flash Filesystem or SD
Card for INPUT with the file number `#fnbr` is positioned at the end of the file.

The # is optional. Also see the OPEN, INPUT and LINE INPUT commands
and the INPUT$ function.


### LOC( [#]fnbr )

For a file on the Flash Filesystem or SD Card opened as `fnbr` this will return
the current position of the read/write pointer in the file. Note that the first byte
in a file is numbered 1.

For a serial communications port opened as `fnbr` this function will return the
number of bytes received and waiting in the receive buffer to be read. #0 can
be used which refers to the console's input buffer.

The # is optional.


### LOF( [#]fnbr )

For a file on the Flash Filesystem or SD Card opened as `fnbr` this will return
the current length of the file in bytes.

For a serial communications port opened as `fnbr` this function will return the
space (in characters) remaining in the transmit buffer. Note that when the
buffer is full MMBasic will pause when adding a new character and wait for
some space to become available so this function can be used to avoid this.

The # is optional.


### PEEK(BYTE addr%) or PEEK(SHORT addr%) or PEEK(WORD addr%) or PEEK(INTEGER addr%) or PEEK(FLOAT addr%) or PEEK(VARADDR var) or PEEK(CFUNADDR cfun) or PEEK(VAR var, ±offset) or PEEK( VARTBL, ±offset) or PEEK( PROGMEM, ±offset)

PEEK(SHORT or give a error if not aligned e.g PEEK(SP
Will return a byte or a word within the processor’s virtual memory space.

BYTE will return the byte (8-bits) located at `addr%`
SHORT will return the short integer (16-bits) located at `addr%`
  
WORD will return the word (32-bits) located at `addr%`
  
INTEGER will return the integer (64-bits) located at `addr%`
  
FLOAT will return the floating point number (64-bits) located at `addr%`
  
VARADDR will return the address (32-bits) of the variable `var` in memory.

An array is specified as var().

CFUNADDR will return the address (32-bits) of the CFunction `cfun` in
memory. This address can be passed to another CFunction which can then call
it to perform some common process.

VAR, will return a byte in the memory allocated to `var`. An array is specified
as var().

VARTBL, will return a byte in the memory allocated to the variable table
maintained by MMBasic. Note that there is a comma after the keyword
VARTBL.

PROGMEM, will return a byte in the memory allocated to the program. Note
that there is a comma after the keyword PROGMEM.

Note that `addr%` should be an integer.


### PEEK(BP, n%) PEEK(SP,n%) PEEK(WP,n%) PI

PEEK(bp n%) ' returns the byte at address n% and increments n% to point to
the next byte.

       
PEEK(sp n%) ' returns the short at address n% and increments n% to point to
the next short.

       
PEEK(wp n%) ' returns the word at address n% and increments n% to point to
the next word.


## Numeric Functions


### CINT( number )

Round numbers with fractional portions up or down to the next whole number
or integer.

For example, 45.47 will round to 45
                45.57 will round to 46
                -34.45 will round to -34
                -34.55 will round to -35
See also INT() and FIX().


### EXP( number )

Returns the exponential value of `number`, i.e. e^x where x is `number`.


### LOG( number )

Returns the natural logarithm of the argument `number`.


### INT( number )

Truncate an expression to the next whole number less than or equal to the
argument. For example 9.89 will return 9 and -2.11 will return -3.

This behaviour is for Microsoft compatibility, the FIX() function provides a
true integer function. See also CINT() .


### MAX( arg1 [, arg2 [, …]] ) or MIN( arg1 [, arg2 [, …]] )

Returns the maximum or minimum number in the argument list.

Note that the comparison is a floating point comparison (integer arguments are
converted to floats) and a float is returned.


### PI ()

Returns the value of pi.


### RND( number ) or RND

Returns a random (RP2350) or pseudo-random (RP2040) number in the range
of 0 to 0.999999. The `number` value is ignored if supplied.

See also the RANDOMIZE command (RP2040 only).


### SGN( number )

Returns the sign of the argument `number`, +1 for positive numbers, 0 for 0, and
-1 for negative numbers.


### SQR( number )

Returns the square root of the argument `number`.


## MATH functions

The math function performs many simple mathematical calculations that can be
programmed in Basic but there are speed advantages to coding looping
structures in C and there is the advantage that once debugged they are there for
everyone without re-inventing the wheel.


### MATH(ATAN3 x,y)

Returns ATAN3 of x and y


### MATH(COSH a)

Returns the hyperbolic cosine of a


### MATH(LOG10 a)

Returns the base 10 logarithm of a


### MATH(SINH a)

Returns the hyperbolic sine of a


### MATH(TANH a)

Returns the hyperbolic tan of a


### MATH(CRCn data [,length] [,polynome] [,startmask] [,endmask] [,reverseIn] [,reverseOut]

Calculates the CRC to n bits (8, 12, 16, 32) of “data”. “data” can be an integer
or floating point array or a string variable. “Length” is optional and if not
specified the size of the array or string length is used. The defaults for

startmask, endmask reverseIn, and reversOut are all zero. reverseIn, and
reversOut are both Booleans and take the value 1 or 0. The defaults for
polynomes are CRC8=&H07, CRC12=&H80D, CRC16=&H1021,
crc32=&H04C11DB7
eg, for crc16_CCITT use MATH(CRC16 array(), n,, &HFFFF)


### MATH(RAND)

Returns a random number 0.0 <= n < 1.0 using the "Mersenne Twister
algorithm. If not seeded with MATH RANDOMIZE the first usage seeds with
the time in microseconds since boot


## Array functions


### BOUND(array() [,dimension]

This returns the upper limit of the array for the dimension requested.

The dimension defaults to one if not specified. Specifying a dimension value of
0 will return the current value of OPTION BASE.

Unused dimensions will return a value of zero.

For example:
DIM myarray(44,45)
BOUND(myarray(),2) will return 45


### MATH(CHI a()) 

Returns the Pearson's chi-squared value of the two dimensional array a())


### MATH(CHI_p a())

Returns the associated probability in % of the Pearson's chi-squared value of
the two dimensional array a())


### MATH(CROSSING array() [,level] [,direction]

This returns the array index at which the values in the array pass the "level" in
the direction specified. level defaults to 0. Direction defaults to 1 ( valid values
are -1 or 1)
 

### MATH(CORREL a(), a()) 

Returns the Pearson’s correlation coefficient between arrays a() and b()

### MATH(MAX a() [,index%])

Returns the maximum of all values in the a() array, a() can have any number of
dimensions. If the integer variable is specified then it will be updated with the
index of the maximum value in the array. This is only available on one-
dimensional arrays


### MATH(MEAN a()) 

Returns the average of all values in the a() array, a() can have any number of
dimensions

### MATH(MEDIAN a()) 

Returns the median of all values in the a() array, a() can have any number of
dimensions 
 
### MATH(MIN a(), [index%])
 
Returns the minimum of all values in the a() array, a() can have any number of
dimensions. If the integer variable is specified then it will be updated with the
index of the minimum value in the array. This is only available on one-
dimensional arrays.


### MATH(SD a())

Returns the sample standard deviation of all values in the a() array, a() can have
any number of dimensions
 
### MATH(SUM a())

Returns the sum of all values in the a() array, a() can have any number of
dimensions


### Vector Arithmetic

### MATH(MAGNITUDE v())
Returns the magnitude of the vector v(). The vector can have any number of
elements 

### MATH(DOTPRODUCT v1(), v2())

Returns the dot product of two vectors v1() and v2(). The vectors can have any
number of elements but must have the same cardinality


### MATH(M_DETERMINANT array!())

Returns the determinant of the array. The array must be square.


### MATH(PID channel, setpoint!, measurement))

This function must be called in the PID callback subroutine for the `channel`
specified and returns the output of the controller function.

The `setpoint` value is the desired state that the controller is trying to achieve.

The `measurement` is the current value of the real world.

https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=17263
For an example of setting up and running a PID controller


### MATH(BASE64 ENCODE/DECODE in$/in(), out$/out())

Returns the length of out$/out(). This base64 encodes or decodes the data in `in`
and puts the result in `out`. 

Where arrays are used as the output they must be big enough relative to the input and the direction. Encryption increases length by 4/3 and decryption decreases it by 3/4.


## Graphics functions

### MAP( n )

Returns the 24-bit RGB value for the index `n` in the colour map table.

See the MAP command. This allows the Basic programmer to use a colour
specified by the MAP command
e.g
MAP(8) = RGB(100,100,100)
MAP SET
Pixel x,y,map(8)


### PIXEL( x, y)

Returns the colour of a pixel on the video output or LCD display. `x` is the
horizontal coordinate and `y` is the vertical coordinate of the pixel.

If an LCD display is used it must use one of the SSD1963, ILI9341, ILI9488,
or ST7789_320 controllers.


### RGB(red, green, blue) or RGB(shortcut)

Generates an RGB true colour value.

`red`, `blue` and `green` represent the intensity of each colour. A value of zero
represents black and 255 represents full intensity.

`shortcut` allows common colours to be specified by naming them. The colours
that can be named are white, black, blue, green, cyan, red, magenta, yellow,
brown, white, orange, pink, gold, salmon, beige, lightgrey and grey (or USA
spelling gray/lightgray). For example, RGB(red) or RGB(cyan).


## I/O Funcitons


### PORT(start, nbr [,start, nbr]…)

Returns the value of a number of I/O pins in one operation.

`start` is an I/O pin number and its value will be returned as bit 0. `start`+1 will be
returned as bit 1, `start`+2 will be returned as bit 2, and so on for `nbr` number of
bits. I/O pins used must be numbered consecutively and any I/O pin that is
invalid or not configured as an input will cause an error. The start/nbr pair can be
repeated up to 25 times if additional groups of input pins need to be added.

This function will also return the output state of a pin configured as an output.

This can be used to conveniently communicate with parallel devices like
memory chips. Any number of I/O pins (and therefore bits) can be used from 1
to the number of I/O pins on the chip.

See the PORT command to simultaneously output to a number of pins.


### PULSIN( pin, polarity ) or PULSIN( pin, polarity, t1 ) or PULSIN( pin, polarity, t1, t2 )

Measures the width of an input pulse from 1µs to 1 second with 0.1µs
resolution.

`pin` is the I/O pin to use for the measurement, it must be previously configured as a digital input.

`polarity` is the type of pulse to measure, if zero the function will return the width of the next negative pulse, if non zero it will measure the next positive pulse.

`t1` is the timeout applied while waiting for the pulse to arrive, `t2` is the timeout used while measuring the pulse. Both are in microseconds (µs) and are optional. 

If `t2` is omitted the value of `t1` will be used for both timeouts. If both `t1` and `t2` are omitted then the timeouts will be set at 100000 (i.e. 100ms).

This function returns the width of the pulse in microseconds (µs) or -1 if a
timeout has occurred. The measurement is accurate to ±0.5% and ±0.5µs.

Note that this function will cause the running program to pause while the
measurement is made and interrupts will be ignored during this period.


### SPI ( data ) or SPI2 ( data )

Send and receive data using an SPI channel.

A single SPI transaction will send data while simultaneously receiving data
from the slave. `data` is the data to send and the function will return the data
received during the transaction. `data` can be an integer or a floating point
variable or a constant.

See [SPI Communications](../D_spi_communications.md)

### PIN( pin )

Returns the value on the external I/O `pin`. Zero means digital low, 1 means
digital high and for analogue inputs it will return the measured voltage as a
floating point number.

Frequency inputs will return the frequency in Hz. A period input will return
the period in milliseconds while a count input will return the count since reset
(counting is done on the positive rising edge). The count input can be reset to
zero by resetting the pin to counting input (even if it is already so configured).

When a pin is configured as an output this function will return the value of the
output setting (ie, high or low). Also see the SETPIN and PIN() = commands.

Refer to the chapter Using the I/O pins for a general description of the
PicoMite's input/output capabilities.


### PIN( BOOTSEL )

Returns the state of the boot select switch allowing it to be used as a user input
in a program.


### PIN( TEMP )

Returns the temperature of the RP2040/RP2350 chip (see the data sheet for the
details).


## PIO Functions

see also [Appendix F – The PIO Programming Package](../F_the_pio_programming_package.md)


### PIO(DMA RX POINTER) PIO(DMA TX POINTER)

Returns the current data item being written or read by the PIO.


### PIO (SHIFTCTRL push_threshold [,pull_threshold] [,autopush] [,autopull] [,in_shiftdir] [,out_shiftdir] [,fjoin_tx] [,fjoin_rx])

helper function to calculate the value of shiftctrl for the INIT MACHINE command .


### PIO (PINCTRL no_side_set_pins [,no_set_pins] [,no_out_pins] [,IN base] [,side_set_base] [,set_base][, out_base])

helper function to calculate the value of pinctrl for the INIT MACHINE
command. Note: The pin parameters must be formatted as GPn.


### PIO (EXECCTRL jmp_pin ,wrap_target, wrap [,side_pindir] [,side_en])

helper function to calculate the value of execctrl for the INIT MACHINE
command


### PIO(READFIFO a, b, c)

Read from a PIO FIFO `a` is the pio (0 or 1), `b` id the state machine (0...3), `c` is the FIFO register *0…3)


### PIO (FDEBUG pio)

returns the value of the FSDEBUG register for the pio specified


### PIO (FSTAT pio)

returns the value of the FSTAT register for the pio specified


### PIO (FLEVEL pio)

returns the value of the FLEVEL register for the pio specified PIO(FLEVEL pio)


### PIO(FLEVEL pio ,sm, DIR)

dir can be RX or TX. Returns the level of the specific fifo


### PIO(.WRAP) PIO(.WRAP TARGET)

returns the location of the .wrap directive in PIO ASSEMBLE
returns the location of the .wrap target directive in PIO ASSEMBLE.

These can be used in the PIO(EXECCTRL function as follows:
PIO (EXECCTRL jmp_pin PIO(.WRAP TARGET), PIO(.WRAP)
[,side_pindir] [,side_en])


### PIO(NEXT LINE)

Returns the next unused PIO instruction slot after a block of PIO instructions
terminated by END PROGRAM


## SPRITE funcitons

*VGA AND HDMI VERSIONS ONLY*

The SPRITE functions return information regarding sprites which are small
graphic images on the VGA/HDMI screen. These are useful when writing
games. See also the [SPRITE commands](../command/sprite.md).


### SPRITE(C, [#]n )

Returns the number of currently active collisions for sprite n. If n=0 then
returns the number of sprites that have a currently active collision following a
SPRITE SCROLL command


### SPRITE(C, [#]n, m) SPRITE(D ,[#]s1, [#]s2)

Returns the number of the sprite which caused the “m”th collision of sprite n.

If n=0 then returns the sprite number of “m”th sprite that has a currently active
collision following a SPRITE SCROLL command.

If the collision was with the edge of the screen then the return value will be:

          &HF1       collision with left of screen
          &HF2       collision with top of screen
          &HF4       collision with right of screen
          &HF8       collision with bottom of screen

Returns the distance between the centres of sprites `s1` and `s2` (returns -1 if
either sprite is not active)


### SPRITE(E, [#]n)

Returns a bitmap indicating any edges of the screen the sprite is in contact with:
- 1=left of screen
- 2=top of screen
- 4=right of screen
- 8=bottom of screen


### SPRITE(H,[#]n)

Returns the height of sprite n. This function is active whether or not the sprite is
currently displayed (active).


### SPRITE(L, [#]n)

Returns the layer number of active sprites number `n`


### SPRITE(N)

Returns the number of displayed (active) sprites


### SPRITE(N,n)

Returns the number of displayed (active) sprites on layer `n`


### SPRITE(S)

Returns the number of the sprite which last caused a collision. NB if the
number returned is Zero then the collision is the result of a SPRITE SCROLL
command and the SPRITE(C…) function should be used to find how many and
which sprites collided.


### SPRITE(T, [#]n)

Returns a bitmap showing all the sprites currently touching the requested sprite `n`
Bits 0-63 in the returned integer represent a current collision with sprites 1 to
64 respectively


### SPRITE(V,[#]s1, [#]s2)

Returns the vector from sprite `s1` to `s2` in radians.

The angle is based on the clock so if `s2` is above `s1` on the screen then the
answer will be zero. This can be used on any pair of sprites that are visible. If
either sprite is not visible the function will return -1.

This is particularly useful after a collision if the programmer wants to make
some differential decision based on where the collision occurred. The angle is
calculated between the centre of each of the sprites which may of course be
different sizes.


### SPRITE(W, [#]n) SPRITE(X, [#]n)

Returns the width of sprite n. This function is active whether or not the sprite is
currently displayed (active).


Returns the X-coordinate of sprite n. This function is only active when the
sprite is currently displayed (active). Returns 10000 otherwise.


### SPRITE(Y, [#]n)

Returns the Y-coordinate of sprite n. This function is only active when the
sprite is currently displayed (active). Returns 10000 otherwise.


## Misc functions

Handling optional devices

### DISTANCE( trigger, echo ) or DISTANCE( trig-echo )

Measure the distance to a target using the HC-SR04 ultrasonic distance sensor.

Four pin sensors have separate trigger and echo connections. `trigger` is the I/O
pin connected to the "trig" input of the sensor and `echo` is the pin connected to
the "echo" output of the sensor.

Three pin sensors have a combined trigger and echo connection and in that case
you only need to specify one I/O pin to interface to the sensor.

Note that the HC-SR04 is a 5V device so level shifting will be required on Pico
(RP2040) processors but not on Pico 2 (RP2350) processors.

The I/O pins are automatically configured by this function and multiple sensors
can be used on different I/O pins.

The value returned is the distance in centimetres to the target or -1 if no target
was detected or -2 if there was an error (i.e. sensor not connected).


### TEMPR( pin [,timeout])

Return the temperature measured by a DS18B20 temperature sensor connected
to `pin` (which does not have to be configured).

The returned value is degrees C with a default resolution of 0.25ºC. If there is
an error during the measurement the returned value will be 1000.

The time required for the overall measurement is 200ms and interrupts will be
ignored during this period.

The optional parameter timeout can be used to override the default (200mSec)
to allow for slow devices.

Alternatively the TEMPR START command can be used to start the
measurement and your program can do other things while the conversion is
progressing. When this function is called the value will then be returned
instantly assuming the conversion period has expired. If it has not, this
function will wait out the remainder of the conversion time before returning the
value.

The DS18B20 can be powered separately by a 3V to 5V supply or it can
operate on parasitic power from the Raspberry Pi Pico.

See the chapter Special Hardware Devices for more details.


### TOUCH(X) or TOUCH(Y) or FT6336 only TOUCH(X2) or TOUCH(Y2)

Will return the X or Y coordinate of the location currently touched on an LCD
panel.

If the screen is not being touched the function will return -1.

For the FT6336 TOUCH(X2) and TOUCH(Y2) returns the position of a second
touch location or -1 if no second location is touched.





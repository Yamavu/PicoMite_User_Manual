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


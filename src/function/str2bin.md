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


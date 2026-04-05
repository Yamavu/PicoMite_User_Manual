### LOF( [#]fnbr )

For a file on the Flash Filesystem or SD Card opened as `fnbr` this will return
the current length of the file in bytes.

For a serial communications port opened as `fnbr` this function will return the
space (in characters) remaining in the transmit buffer. Note that when the
buffer is full MMBasic will pause when adding a new character and wait for
some space to become available so this function can be used to avoid this.

The # is optional.


### LOC( [#]fnbr )

For a file on the Flash Filesystem or SD Card opened as `fnbr` this will return
the current position of the read/write pointer in the file. Note that the first byte
in a file is numbered 1.

For a serial communications port opened as `fnbr` this function will return the
number of bytes received and waiting in the receive buffer to be read. #0 can
be used which refers to the console's input buffer.

The # is optional.


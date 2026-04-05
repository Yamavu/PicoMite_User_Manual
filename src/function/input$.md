### INPUT$(nbr, [#]fnbr)

Will return a string composed of `nbr` characters read from a file or serial
communications port opened as `fnbr`. This function will return as many
characters as are in the file or receive buffer up to `nbr`. If there are no
characters available it will immediately return with an empty string.

#0 can be used which refers to the console's input buffer.

The # is optional. Also see the OPEN command.


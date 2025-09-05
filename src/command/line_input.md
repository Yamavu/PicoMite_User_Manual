### LINE INPUT [prompt$,] string-variable$

Reads an entire line from the console input into `string-variable$`.

`prompt$` is a string constant (not a variable or expression) and if specified it will be printed first. A question mark `?` is not printed unless it is part of `prompt$`.

Unlike [INPUT](./input.md), this command will read a whole line, not stopping for comma delimited data items.


### LINE INPUT #nbr, string-variable$

Same as above except that the input is read from a serial communications port or a file previously opened for INPUT as `nbr`.

See the [OPEN command](./open.md).

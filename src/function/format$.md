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


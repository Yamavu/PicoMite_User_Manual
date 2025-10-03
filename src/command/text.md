### TEXT x, y, string$ [,alignment$] [, font] [, scale] [, c] [, bc]

Displays a string on the video output or attached LCD panel starting at `x` and `y`.

`string$` is the string to be displayed. Numeric data should be converted to a string and formatted using the [Str$() function](../function/str$.md). 

`alignment$` is a string expression or string variable consisting of 0, 1 or 2 letters. The default alignment is left/top. The `alignment$` string can be a constant (eg, `"CM"`) or it can be a string variable. For backwards compatibility with earlier versions of MMBasic the string can also be unquoted (eg, `TEXT 1,1,"HELO",CM`).

The first letter is the horizontal alignment around `x` and can be:
| 1st | Alignment |
|:-:  |:-     |
| `L` | left   | 
| `C` | center |
| `R` | right  | 

The second letter is the vertical alignment around `y` and can be 
| 2st | Alignment |
|:-:|:-     |
| `T` | top    |
| `M` | middle |
| `B` | bottom |

For example. `"CM"` will centre the text vertically and horizontally. 

A third letter can be used in the alignment string to indicate the rotation of the text.
This can be:
| 3rd | Alignment |
|:-:|:-     |
| `N` | for normal orientation |
| `V` | for vertical text with each character under the previous running from top to bottom |
| `I` | the text will be inverted (i.e. upside down) |
| `U` | the text will be rotated counter clockwise by 90º  |
| `D` | the text will be rotated clockwise by 90º |

`font` and `scale` are optional and default to that set by the `FONT` command.

`c` is the drawing colour and `bc` is the background colour. They are optional and default to the current foreground and background colours. See the chapter [Graphics Commands and Functions](../graphics_functions.md) for a definition of the colours and graphics coordinates. 


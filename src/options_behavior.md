# Behavior

These options change the behavior of the  BASIC code.

## OPTION ANGLE RADIANS | DEGREES

This command switches trig functions between degrees and radians.

Acts on SIN, COS, TAN, ATN, ATAN2, MATH ATAN3, ACOS, ASIN


## OPTION BASE 0 | 1

Set the lowest value for array subscripts to either 0 or 1.
This must be used before any arrays are declared and is reset to the
default of 0 on power up.


## OPTION DEFAULT FLOAT | INTEGER | STRING | NONE

Used to set the default type for a variable which is not explicitly defined.

If `OPTION DEFAULT NONE` is used then all variables must have their type explicitly defined or the error `Variable type not specified` will occur.

When a program is run the default is set to `FLOAT` for compatibility with Microsoft BASIC and previous versions of MMBasic.


## OPTION DEFAULT COLOURS foreground [,background]

#permanent

Set the default foreground and background colours for both the monochrome and colour modes. The colour must be one of the following:

* white
* yellow
* lilac
* brown
* fuchsia
* rust
* magenta
* red
* cyan
* green,
* cerulean
* midgreen
* cobalt
* myrtle
* blue
* black. 

A numeric value cannot be used. The default is `white, black`. If background is omitted it defaults to `black`.


## OPTION DEFAULT MODE n

#permanent

This sets the default display mode on boot.

*This command must be run at the command prompt (not in a program).*


## OPTION ESCAPE

Enables the ability to insert escape sequences into string constants. See the section Special Characters in Strings.


## OPTION EXPLICIT

Placing this command at the start of a program will require that every variable be explicitly declared using the `DIM`, `LOCAL` or `STATIC` commands before it can be used in the program.

This option is disabled by default when a program is run. If it is used it must be specified before any variables are used.


## OPTION LEGACY ON <br> OPTION LEGACY OFF

This will turn on or off compatibility mode with the graphic commands used in the original Colour Maximite. The commands `COLOUR`, `LINE`, `CIRCLE` and `PIXEL` use the legacy syntax and all drawing commands will accept colours in the range of 0 to 7.

Notes:
* Keywords such as RED, BLUE, etc are not implemented so they should be defined as constants if needed.
* Refer to the Colour Maximite MMBasic Language Manual for the syntax of the legacy commands. This can be downloaded from https://geoffg.net/OriginalColourMaximite.html .


## OPTION MILLISECONDS ON|OFF

This enables or disables a millisecond output in the `TIME$` function .i.e, `HH:MM:SS.mmm`.

The milliseconds counter is set to zero whenever the time is updated using the `TIME` command, `WEB NTP` command or `RTC GETTIME`
command. Default is `OFF`.


## OPTION PLATFORM name$

Allows a user to identify a particular hardware configuration that can
then be used in programs to control the program's operation.

`name$` can be up to 31 characters long. This is a permanent option.

`MM.INFO$(PLATFORM)` returns this string.

For example, this can be used on a particular hardware configuration:

```basic
OPTION PLATFORM "GameMite"
```

Then programs that might run on this or other platforms can use:

```basic
IF MM.INFO$(PLATFORM) = "GameMite" THEN …
```
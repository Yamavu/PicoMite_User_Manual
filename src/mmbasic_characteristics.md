# MMBasic Characteristics

## Naming Conventions

Command names, function names, labels, variable names, etc are not case sensitive, so that `Run` and `RUN` are equivalent and `dOO` and `Doo` refer to the same variable.

The type of a variable can be specified in the DIM command or by adding a suffix to the end of the variable's name. For example the suffix for an integer is '%' so if a variable called nbr% is automatically created it will be an integer. There are three types of variables:

Name | Suffix |  Description
:-: | :-: |  :-
Floating point | `!` | These can store a number with a decimal point and fraction (eg, 45.386) and also very large numbers. However, they will lose accuracy when more than 14 significant digits are stored or manipulated. Floating point is the default when a variable is created without a suffix.
64-bit integer | `%` | These can store numbers with up to 19 decimal digits without losing accuracy but they cannot store fractions (i.e. the part following the decimal point). The suffix for an integer is '%'
Strings | `$` | These will store a string of characters (eg, "Tom"). Strings can be up to 255 characters long.

Variable names and labels can start with an alphabetic character or underscore and can contain any alphabetic or numeric character, the period (.) and the underscore (_). They may be up to 31 characters long. A variable name or a label must not be the same as a command or a function or one of the following keywords:

`THEN`, `ELSE`, `TO`, `STEP`, `FOR`, `WHILE`, `UNTIL`, `MOD`, `NOT`, `AND`, `OR`, `XOR`, `AS`. 

Eg, `step = 5` is illegal.

For file names see the section MMBasic Support for Flash and SD Card Filesystems.

## Constants

Numeric constants may begin with a numeric digit (`0-9`) for a decimal constant, &H for a hexadecimal
constant, &O for an octal constant or &B for a binary constant. For example &B1000 is the same as the
decimal constant 8. Constants that start with &H, &O or &B are always treated as 64-bit integer constants.

Decimal constants may be preceded with a minus (`-`) or plus (`+`) and may be terminated with `E` followed by an exponent number to denote exponential notation. For example `1.6E+4` is the same as `16000`. If the decimal constant contains a decimal point or an exponent, it will be treated as a floating point constant; otherwise it will be treated as a 64-bit integer constant.

String constants are surrounded by double quote marks (`"`). Eg, "Hello World".

## Implementation Characteristics

Maximum program - see table. Note that MMBasic tokenises the program when it is stored in flash so the final size in flash might vary from the plain text size.

- Maximum length of a command line is 255 characters.
- Maximum length of a variable name or a label is 31 characters.

- Maximum number of dimensions - see table.
- Maximum number of arguments to commands that accept a variable number of arguments is 50.
- Maximum number of nested FOR…NEXT loops is 20.
- Maximum number of nested DO…LOOP commands is 20.
- Maximum number of nested GOSUBs is 50.
- Maximum number of nested multiline IF…ELSE…ENDIF commands is 20.
- Maximum number of user defined labels, subroutines and functions (combined) – see table.
- Maximum number of interrupt pins that can be configured: 10

- Numbers are stored and manipulated as double precision floating point numbers or 64-bit signed integers. The range of floating point numbers is 1.797693134862316e+308 to 2.225073858507201e-308.
The range of 64-bit integers (whole numbers) that can be manipulated is ± 9223372036854775807.

- Maximum string length is 255 characters.
- Maximum line number is 65000.
- Maximum number of background pulses launched by the [PULSE](command/pulse.md) command is 5.
- Maximum number of global variables/constants and the number of local variables are the same for current implementations.

  for example: PicoMite RP2040 allows for 256 global **and** 256 local variables
- The maximum number of files that can be listed by the [FILES](command/files.md) command is 1000.
- The maximum length of a filename/path is 63 characters.

### Characteristics vs firmware features

The following chart lists the maximum for various firmwares

Program size | frequency | numbers of subroutines or functions | Array Dimensions | number of number of variables
 :- | :-: | :-: | :-: | :-: 
PicoMite RP2040 | 128Kb | 420MHz | 256 | 6 | 256 | 256
PicoMiteUSB RP2040 | 128Kb | 420MHz | 256 | 6 | 256 | 256
PicoMiteVGA RP2040 | 100Kb | 378MHz | 256 | 6 | 256 | 256
PicoMiteVGAUSB RP2040 | 100Kb | 378MHz | 256 | 6 | 256 | 256
PebMite RP2040 | 88Kb | 252MHz | 256 | 6 | 240 | 240
PicoMite RP2350 | 288Kb | 396MHz | 512 | 5 | 384 | 384
PicoMiteUSB RP2350 | 288Kb | 396MHz | 512 | 5 | 384 | 384
PicoMiteVGA RP2350 | 184Kb | 378MHz | 512 | 5 | 384 | 384
PicoMiteVGAUSB RP2350 | 184Kb | 378MHz | 512 | 5 | 384 | 384
PicoMiteHDMI RP2350 | 184Kb | 372MHz | 512 | 5 | 384 | 384
PicoMiteHDMIUSB RP2350 | 184Kb | 372MHz | 512 | 5 | 384 | 384
WebMite RP2350 | 208Kb | 252MHz | 512 | 5 | 384 | 384

## Compatibility

MMBasic implements a large subset of Microsoft’s GW-BASIC. There are numerous differences due to
physical and practical considerations but most standard BASIC commands and functions are essentially the
same. An online manual for GW-BASIC is available at http://www.antonis.de/qbebooks/gwbasman/index.html
and this provides a more detailed description of the commands and functions.

MMBasic also implements a number of modern programming structures documented in the ANSI Standard for
Full BASIC (X3.113-1987) or ISO/IEC 10279:1991.

These include the statements below.
- `SUB`/`END SUB`
- `DO WHILE … LOOP`
- `SELECT … CASE `
- `IF . THEN … ELSE … ENDIF`

# Obsolete Commands and Functions

Detailed Listing

These commands and functions are mostly included to assist in converting programs written for Microsoft
BASIC. For new programs the corresponding modern commands in MMBasic should be used.
Note that these commands/functions may be removed in the future to recover memory for other features.

## BITBANG

Replaced by the command DEVICE. For compatibility BITBANG can still be
used in programs and will be automatically converted to DEVICE

## DEVICE CAMERA

Changed to the CAMERA command

## DEVICE GAMEPAD

Changed to the GAMEPAD command

## DEVICE HUMID

Changed to the HUMID command

## DEVICE KEYPAD

Changed to the KEYPAD command

## DEVICE MOUSE

Changed to the MOUSE command

## DEVICE LCD

Changed to the LCD command

## DEVICE WII

Changed to the WII command

## DEVICE WS2812

Changed to the WS2812 command

## GOSUB target

Initiates a subroutine call to the target, which can be a line number or a label.
The subroutine must end with RETURN.

New programs should use defined subroutines (i.e. SUB…END SUB).

## IF condition THEN linenbr

For Microsoft compatibility a GOTO is assumed if the THEN statement is
followed by a number. A label is invalid in this construct.
New programs should use: IF condition THEN GOTO linenbr | label

## IRETURN

Returns from an interrupt when the interrupt destination was a line number or a
label.
New programs should use a user defined subroutine as an interrupt destination.
In that case END SUB or EXIT SUB will cause a return from the interrupt.

## ON nbr GOTO | GOSUB target[,target, target,..]

ON either branches (GOTO) or calls a subroutine (GOSUB) based on the
rounded value of 'nbr'; if it is 1, the first target is called, if 2, the second target
is called, etc. Target can be a line number or a label.
New programs should use SELECT CASE.

## POS

For the console, returns the current cursor position in the line in characters.

## RETURN

`RETURN` concludes a subroutine called by GOSUB and returns to the
statement after the GOSUB.

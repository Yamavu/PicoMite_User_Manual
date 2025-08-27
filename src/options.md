# Options

This table lists the various option commands which can be used to configure MMBasic and change the way it
operates. Options that are marked as permanent will be saved in non-volatile memory and automatically
restored when the PicoMite firmware is restarted. Options that are not permanent will be reset on start-up, reset
and in many cases when a program is run and/or exited.

Many OPTION commands will force a restart of the PicoMite firmware and that will cause the USB console
interface to be reset. The program in memory will not be lost as it is held in non-volatile flash memory.


## Command Prompt

Instructs MMBasic to automatically run a program on power up or restart.

Entering the break key (default CTRL-C) at the console will interrupt the running program and return to the command prompt.


### OPTION AUTORUN ON [,NORESET] 

`ON` will cause the current program in program memory to be run.

Specifying the optional parameter “NORESET” will maintain AUTORUN even if the program causes a system error (by default this
will cause the firmware to cancel any OPTION AUTORUN setting).


### OPTION AUTORUN n [,NORESET] 

Specifying `n` will cause that location in flash memory to be run. `n` must be in the range 1 to 3.

Specifying the optional parameter “NORESET” will maintain AUTORUN even if the program causes a system error (by default this
will cause the firmware to cancel any OPTION AUTORUN setting).


### OPTION AUTORUN OFF

OFF will disable the autorun option and is the default for a new program.


### OPTION BREAK nn

Set the value of the break key to the ASCII value `nn`. This key is used to
interrupt a running program.

The value of the break key is set to **CTRL-C** key at power upand when a
program is run but it can be changed to any keyboard key using this
command in a program (for example, `OPTION BREAK 4` will set the break
key to the **CTRL-D** key). Setting this option to zero `0` will disable the break
function entirely.


### OPTION CASE LOWER | UPPER | TITLE

Change the case used for listing command and function names when using the `LIST` command. The default is `TITLE` but the old standard of MMBasic can be restored using `OPTION CASE UPPER`.


### OPTION COLOURCODE ON <br> OPTION COLOURCODE OFF

#permanent

Turn on or off colour coding for the editor's output. Keywords will be in cyan, comments in yellow, etc. The default is OFF.

The keyword `COLORCODE` (USA spelling) can also be used.

This will work on VGA/HDMI video and the serial console using a terminal emulator with VT100 emulation (eg, Tera Term). This
command must be run at the command prompt (not in a program).


### OPTION CONSOLE output

Specifies where print statements will output. Valid settings are `BOTH` (SCREEN and SERIAL), `SERIAL`, `SCREEN`, `NONE`. This is a temporary option that is reset when a program exits.


### OPTION CONTINUATION<br>LINES ON/OFF

Enables or disables the use of continuation lines in the editor and with the `LIST` command. Line continuation is indicated by a space followed by an underscore character at the end of a line.

When enabled the editor will automatically split lines as it reads them from file and add the continuation characters required. When exiting the editor, the continuation characters are removed before saving. While in the editor the user can create long lines by adding their own continuation characters. This makes using a small screen as a console much easier.


### OPTION FNKey string$

Define the string that will be generated when a function key is pressed at
the command prompt. `FNKey` can be *F1*, and *F5* thru to *F9*.

Example:

```basic
OPTION F8 “RUN “+chr$(34)+”myprog” +chr$(34)+chr$(13)+chr$(10).
```

This command must be run at the command prompt (not in a program).


### OPTION LIST

This will list the settings of any options that have been changed from their default setting and are the permanent type. OPTION LIST also shows the version number and which firmware is loaded.

This command must be run at the command prompt (not in a program).


### OPTION PIN nbr

Set `nbr` as the PIN (Personal Identification Number) for access to the
console prompt. `nbr` can be any non zero number of up to eight digits.

Whenever a running program tries to exit to the command prompt for
whatever reason MMBasic will request this number before the prompt is
presented. This is a security feature as without access to the command
prompt an intruder cannot list or change the program in memory or
modify the operation of MMBasic in any way. To disable this feature
enter zero for the PIN number (i.e. OPTION PIN 0).

A permanent lock can be applied by using 99999999 for the PIN
number. If a permanent lock is applied or the PIN number is lost the
only way to recover is to reload the PicoMite firmware.

This command must be run at the command prompt (not in a program).


### OPTION PLATFORM name$

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


### OPTION SERIAL CONSOLE uartapin, uartbpin [,B]

Specify that the console be accessed via a hardware serial port (instead
of virtual serial over USB).

`uartapin` and `uartbpin` can be any valid pair of rx and tx pins for either
COM1 or COM2. The order that they are specified is not important.

The speed defaults to 115200 baud but can be changed with OPTION
BAUDRATE. Adding the "B" parameter means output will go to "B"oth
the serial port and the USB.


### OPTION SERIAL CONSOLE DISABLE

Revert to the normal the USB console.

These commands must be run at the command prompt (not in a program).


### OPTION TAB 2 | 3 | 4 | 8

Set the spacing for the tab key. Default is `2`.


### OPTION DISK SAVE fname$<br>OPTION DISK LOAD fname$

These commands let the user save and restore the complete set of options defined to and from a disk file. The file could then be transferred to a host computer using `XMODEM` allowing additional devices to be easily configured or options recovered after a firmware upgrade.


## OPTION RESET

Reset all saved options to their default values.

This command must be run at the command prompt (not in a program).


### OPTION RESET cfg <br> OPTION RESET LIST

Reset all options to default values for the configuration `cfg`.

`OPTION RESET LIST` will list all available configurations.

This command must be run at the command prompt (not in a program).
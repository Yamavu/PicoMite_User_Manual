# Command Prompt


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


### OPTION TAB 2 | 3 | 4 | 8

Set the spacing for the tab key. Default is `2`.



# Commands

At the command prompt you can enter a command and it will be immediately run. Most of the time you will
do this to tell the PicoMite to do something like run a program or set an option. But this feature also allows you
to test out commands at the command prompt.
To enter a program the easiest method is to use the EDIT command. This will invoke the full screen program
editor which is built into the PicoMite and is described later in this manual. It includes advanced features such
as search and copy, cut and paste to and from a clipboard.
You could also compose the program on your desktop computer using something like Notepad and then
transfer it to the PicoMite via the XModem protocol (see the XMODEM command) or by streaming it up the
console serial link (see the AUTOSAVE command).
A third and convenient method of writing and debugging a program is to use MMEdit. This is a program
running on your Windows computer which allows you to edit your program on your computer then transfer it to
the PicoMite with a single click of the mouse. MMEdit was written by Jim Hiley and can be downloaded for
free from https://www.c-com.com.au/MMedit.htm.
One thing that you cannot do is use the old BASIC way of entering a program which was to prefix each line
with a line number. Line numbers are optional in MMBasic so you can still use them if you wish but if you
enter a line with a line number at the prompt MMBasic will simply execute it immediately.

Program Structure
A BASIC program starts at the first line and continues until it runs off the end of the program or hits an END
command - at which point MMBasic will display the command prompt (>) on the console and wait for
something to be entered.
A program consists of a number of statements or commands, each of which will cause the BASIC interpreter to
do something (the words statement and command generally mean the same and are used interchangeably).
Normally each statement is on its own line but you can have multiple statements in the one line separated by
the colon character (:). For example.
A = 24.6 : PRINT A
Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters however
modern implementations (such as MMBasic) do not need them. You can still use them if you wish but they
have no benefit and generally just clutter up your programs. This is an example of a program that uses line
numbers:
50 A = 24.6
60 PRINT A
A line can also start with a label which can be used as the target for a program jump using the GOTO
command. For example (the label name is JmpBack):
JmpBack: A = A + 1
PRINT A
GOTO JmpBack

A label has the same specifications (length, character set, etc) as a variable name but it cannot be the
same as a command name. When used to label a line the label must appear at the beginning of a line
but after a line number (if used) and be terminated with a colon character (:).
Editing the Command Line
When entering a line at the command prompt the line can be edited using the left and right arrow keys to move
along the line, the Delete key to delete a character and the Insert key to switch between insert and overwrite.
At any point the Enter key will send the line to MMBasic which will execute it.
The up and down arrow keys will move through a history of previously entered command lines which can be
edited and reused.



Shortcut Keys
The function keys on the keyboard or the serial console can be used at the command prompt to automatically
enter common commands. These function keys will insert the text followed by the Enter key so that the
command is immediately executed:
F2
RUN
F3
LIST
F4
EDIT
F10
AUTOSAVE
F11
XMODEM RECEIVE
F12
XMODEM SEND
Function keys F1, and F5 to F9 can be programmed with custom text. See the OPTION FNKey command.

Interrupting A Running Program
A program is set running by the RUN command. You can interrupt MMBasic and the running program at any
time by typing CTRL-C on the console input and MMBasic will return to the command prompt.

Setting Options
Many options can be set by using commands that start with the keyword OPTION. They are listed in their own
section of this manual. For example, you can change the CPU clock speed with the command:
OPTION CPUSPEED speed

Saved Variables
Because the PicoMite does not necessarily have a normal storage system it needs to save data that can be
recovered when power is restored. This can be done with the VAR SAVE command which will save the
variables listed on its command line in non-volatile flash memory. The space reserved for saved variables is
16KB.
These variables can be restored with the VAR RESTORE command which will add all the saved variables to
the variable table of the running program. Normally this command is placed near the start of a program so that
the variables are ready for use by the program.
This facility is intended for saving calibration data, user selected options and other items which change
infrequently. It should not be used for high-speed saves as you may wear out the flash memory. The flash used
for the Raspberry Pi Pico has a high endurance but this can be exceeded by a program that repeatedly saves
variables. If you do want to save data often you should add a real time clock chip. The RTC commands can
then be used to store and retrieve data from the RTC's battery backed memory. See the RTC command for
more details.

Watchdog Timer
The main use for the PicoMite is as an embedded controller. It can be programmed in MMBasic and when the
program is debugged and ready for "prime time" the OPTION AUTORUN configuration setting can be turned
on. The module will then automatically run its program when power is applied and act as a custom circuit
performing some special task. The user need not know anything about what is running inside it.
However, there is the possibility that a fault in the program could cause MMBasic to generate an error and
return to the command prompt. This would be of little use in an embedded situation as the PicoMite would not
have anything connected to the console. Another possibility is that the BASIC program could get itself stuck in
an endless loop for some reason. In both cases the visible effect would be the same… the program would stop
running until the power was cycled.
To guard against this the watchdog timer can be used. This is a timer that counts down to zero and when it
reaches zero the processor will be automatically restarted (the same as when power was first applied), this will
occur even if MMBasic was sitting at the command prompt. Following the restart the automatic variable
MM.WATCHDOG will be set to true to indicate that the restart was caused by a watchdog timeout.
The WATCHDOG command should be placed in strategic locations in the program to keep resetting the timer
and therefore preventing it from counting down to zero. Then, if a fault occurs, the timer will not be reset, it
will count down to zero and the program will be restarted (assuming the AUTORUN option is set).



PIN Security
Sometimes it is important to keep the data and program in an embedded controller confidential. In the
PicoMite this can be done by using the OPTION PIN command. This command will set a pin number (which
is stored in flash) and whenever the PicoMite returns to the command prompt (for whatever reason) the user at
the console will be prompted to enter the PIN number. Without the correct PIN the user cannot get to the
command prompt and their only option is to enter the correct PIN or reboot the PicoMite. When it is rebooted
the user will still need the correct PIN to access the command prompt.
Because an intruder cannot reach the command prompt they cannot list or copy a program, they cannot change
the program or change any aspect of MMBasic or the PicoMite. Once set the PIN can only be removed by
providing the correct PIN as set in the first place. If the number is lost the only method of recovery is to reload
the PicoMite firmware (which will erase the program and all options).
There are other time consuming ways of accessing the data (such as using a programmer to examine the flash
memory) so this should not be regarded as the ultimate security but it does act as a significant deterrent.

The Library
Using the LIBRARY feature it is possible to create BASIC functions, subroutines and embedded fonts and add
them to MMBasic to make them permanent and part of the language. For example, you might have written a
series of subroutines and functions that perform sophisticated bit manipulation; these could be stored as a
library and become part of MMBasic and perform the same as other built-in functions that are already part of
the language. An embedded font can also be added the same way and used just like a normal font.
To install components into the library you need to write and test the routines as you would with any normal
BASIC routines. When they are working correctly you can use the LIBRARY SAVE command. This will
transfer the routines (as many as you like) to a non-visible part of flash memory where they will be available to
any BASIC program but will not show when the LIST command is used and will not be deleted when a new
program is loaded or NEW is used. However, the saved subroutines and functions can be called from within
the main program and can even be run at the command prompt (just like a built-in command or function).
Some points to note:
 Library routines act exactly like normal BASIC code and can consist of any number of subroutines,
functions, embedded C routines and fonts. The only difference is that they do not show when a program
is listed and are not deleted when a new program is loaded.


Library routines can create and access global variables and are subject to the same rules as the main
program – for example, respecting OPTION EXPLICIT if it is set.



When the routines are transferred to the library MMBasic will compress them by removing comments,
extra spaces, blank lines and the hex codes in embedded C routines and fonts. This makes the library
space efficient, especially when loading large fonts. Following the save the program area is cleared.



You can use the LIBRARY SAVE command multiple times. With each save the new contents of the
program space are appended to the already existing code in the library.



You can use line numbers in the library but you cannot use a line number on an otherwise empty line as
the target for a GOTO, etc. This is because the LIBRARY SAVE command will remove any blank lines.



You can use READ commands in the library but they will default to reading DATA statements in the
main program memory. If you want to read from DATA statements in the library you must use the
RESTORE command before the first READ command. This will reset the pointer to the library space.



The library is saved to program flash memory Slot 3 and this will not be available for storing a program if
LIBRARY SAVE is used.



You can see what is in the library by using the LIBRARY LIST command which will list the contents of
the library space.



The LIBRARY contents can be saved to disk using LIBRARY DISK SAVE fname$ and restored using
LIBRARY DISK LOAD fname$

To delete the routines in the library space you use the LIBRARY DELETE command. This will clear the space
and return the Flash Slot 3 used by the library back to being available for storage for normal programs. The
only other way to delete a library is to use OPTION RESET.



Program Initialisation
The library can also include code that is not contained within a subroutine or function. This code (if it exists)
will be run automatically before a program starts running (ie, via the RUN command). This feature can be used
to initialise constants or setup MMBasic in some way. For example, if you wanted to set some constants you
could include the following lines in the library code:
CONST TRUE = 1
CONST FALSE = 0
For all intents and purposes, the identifiers TRUE and FALSE have been added to the language and will be
available to any program that is run on the PicoMite.

MM.STARTUP
There may be a need to execute some code on initial power up, perhaps to initialise some hardware, set some
options or print a custom start-up banner. This can be accomplished by creating a subroutine with the name
MM.STARTUP. When the PicoMite is first powered up or reset it will search for this subroutine and, if found,
it will be run once.
For example, if the PicoMite has a real time clock attached, the program could contain the following code:
SUB MM.STARTUP
RTC GETTIME
END SUB
This would cause the internal clock within MMBasic to be set to the current time on every power up or reset.
After the code in MM.STARTUP has been run MMBasic will continue with running the rest of the program in
program memory. If there is no other code MMBasic will return to the command prompt.
Note that you should not use MM.STARTUP for general setup of MMBasic (like dimensioning arrays, opening
communication channels, etc) before running a program. The reason is that when you use the RUN command
MMBasic will clear the interpreter's state ready for a fresh start.

MM.PROMPT
If a subroutine with this name exists it will be automatically executed by MMBasic instead of displaying the
command prompt. This can be used to display a custom prompt, set colours, define variables, etc all of which
will be active at the command prompt.
Note that MMBasic will clear all variables and I/O pin settings when a program is run so anything set in this
subroutine will only be valid for commands typed at the command prompt (i.e. in immediate mode).
As an example the following will display a custom prompt:
SUB MM.PROMPT
PRINT TIME$ "> ";
END SUB
Note that while constants can be defined, they will not be visible because a constant defined inside a subroutine
is local to a subroutine. However, DIM will create variables that are global that that should be used instead.



Full Screen Editor
An important productivity feature is the built-in full screen editor. When running it looks like this:

When the editor starts up the cursor will be automatically positioned at the last place that you were editing or, if
your program had just been stopped by an error, the cursor will be positioned at the line that caused the error.
At the bottom of the screen the status line lists details such as the current cursor position and the common
functions supported by the editor.
If you have previously used an editor like Windows Notepad you will find that the operation of this editor is
familiar. The arrow keys will move the cursor around in the text, home and end will take you to the beginning
or end of the line. Page up and page down will do what their titles suggest. The delete key will delete the
character at the cursor and backspace will delete the character before the cursor. The insert key will toggle
between insert and overtype modes. About the only unusual key combination is that two home key presses will
take you to the start of the program and two end key presses will take you to the end.
At the bottom of the screen the status line will list the various function keys used by the editor and their action.
In more details these are:
ESC

F1: SAVE
F2: RUN
F3: FIND
SHIFT-F3
F4: MARK
F5: PASTE

This will cause the editor to abandon all changes and return to the command prompt with the
program memory unchanged. If you have changed the text you will be asked if you really what
want to abandon your changes.
This will save the program to program memory and return to the command prompt.
This will save the program to program memory and immediately run it.
This will prompt for the text that you want to search for. When you press enter the cursor will
be placed at the start of the first entry found.
Once you have used the search function you can repeat the search by pressing SHIFT-F3.
This is described in detail below.
This will insert (at the current cursor position) the text that had been previously cut or copied
(see below).

If you pressed the mark key (F4) the editor will change to the mark mode. In this mode you can use the arrow
keys to mark a section of text which will be highlighted in reverse video. You can then delete, cut or copy the
marked text. In this mode the status line will change to show the functions of the function keys in the mark
mode. These keys are:
ESC
F4: CUT
F5: COPY
DELETE

Will exit mark mode without changing anything.
Will copy the marked text to the clipboard and remove it from the program.
Will just copy the marked text to the clipboard.
Will delete the marked text leaving the clipboard unchanged.



You can also use control keys instead of the function keys listed above. These control keystrokes are:

LEFT
HOME
DEL
F3

Ctrl-S
Ctrl-U
Ctrl-]
Ctrl-R

RIGHT
END
INSERT
ShiftF3

Ctrl-D
Ctrl-K
Ctrl-N
Ctrl-G

UP
PageUp
F1
F4

Ctrl-E
Ctrl-P
Ctrl-Q
Ctrl-T

DOWN
PageDn
F2
F5

Ctrl-X
Ctrl-L
Ctrl-W
Ctrl-Y

If you are using Tera Term, Putty, MMEdit or GFXterm as the terminal emulator it is also possible to position
the cursor by left clicking the PC's mouse in the terminal emulator's window.
The best way to learn how to use the editor is to simply fire it up and experiment.
The editor is a very productive method of writing a program. With the command EDIT you can enter your
program then, by pressing the F2 key, you can save and run the program. If your program stops with an error
pressing the function key F4 at the command prompt will run the command EDIT and place you back in the
editor with the cursor positioned at the line that caused the error. This edit/run/edit cycle is very fast.

Colour Coded Editor Display
The editor can colour code the edited program with keywords, numbers and comments displayed in different
colours. This feature can be turned on or off with the command:
OPTION COLOURCODE ON or OPTION COLOURCODE OFF
This setting requires a compatible terminal emulator like Tera Term and is saved in non-volatile memory and
automatically applied on start-up.



Program and Data Storage
The BASIC program is held in flash memory and is run from there. When a program is edited via EDIT or
loaded via the console it will be saved there. Flash memory is non-volatile so the program will not be lost if the
power is lost or the processor is reset. The maximum program size is 160KB.
In addition to this program memory there are three other locations where programs can be saved. These are
described in detail below and are Flash Slots, the Flash Filesystem and an attached SD Card

Flash Slots
There are four of these which can be used to save completely different programs or previous versions of the
program you are working on (in case you need to revert to an earlier version). In addition, MMBasic will allow
a BASIC program to load and run another program saved to a numbered flash location while retaining all the
variables and settings of the original program – this is called chaining and allows for a much larger program to
be run than the amount of program memory would normally allow.
To manage these numbered locations in flash you can use the following commands (note that in the following n
is a number from 1 to 3):
FLASH SAVE n
Save the program in the program memory to the flash location n.
FLASH LOAD n
Load a program from flash location n into the program memory.
FLASH RUN n
Run a program from flash location n, clears all variables but does not erase
or change the program held in the main program memory.
FLASH LIST
Display a list of all flash locations including the first line of the program.
FLASH LIST n [,ALL]
Lists the program held in location n. Use FLASH LIST n,ALL to list
without page breaks
FLASH ERASE n
Erase flash location n.
FLASH ERASE ALL
Erase all flash locations.
FLASH CHAIN n
Load and run a program from flash location n, leaving all variables intact.
As with FLASH RUN this command but does not erase or change the
program held in the main program memory.
FLASH OVERWRITE n
Erase flash location n and then save the program in the program memory to
that location.
FLASH DISK LOAD f$ [,O] Loads a flash slot from the binary file specified. Overwrites the slot if the
optional “O” is specified.
In addition, the command OPTION AUTORUN can be used to specify a flash program location to be set
running when power is applied or the CPU restarted. This option can also used without specifying a flash
location and in that case MMBasic will automatically load and run the program that is in the program memory.
Notes:
 It is recommended that you include a comment describing the program as the first line of the program. This
will then be displayed by the FLASH LIST command and will help identify the program.
 All BASIC programs saved to flash may be erased if you upgrade (or downgrade) the PicoMite firmware.
So make sure that you backup these first.
 The LIBRARY command uses Slot 3 for saving library data therefore only 2 slots will be available if the
library feature is used.

Flash Filesystem
This is an area of the Raspberry Pi Pico’s flash memory which is automatically created by the firmware and
will look like a normal disk drive to MMBasic. It is called drive A: and data and programs can be read/written
using the normal BASIC file commands (SAVE, RUN, OPEN, etc). In addition, sub directories can be created
and deleted and long filenames used.
For example, to run a program:
RUN "A:/MyProgram.bas"
Open a text file for random access:
OPEN "A:/data/database.dat" FOR RANDOM as #4



Nothing needs to be done to create this drive so it will always be available to the BASIC program.
The system will create and maintain the file "BOOTCOUNT" on the Flash Filesystem. This keeps a count of
the number of times the PicoMite has been restarted and can be read with the function MM.INFO(boot count).

SD Cards
An SD Card socket can be connected to the PicoMite and accessed as drive B:. Like the Flash Filesystem the
normal BASIC file commands can be used to save/load programs as well as opening data files for read/write.
Cards up to 32 GB formatted in FAT16 or FAT32 are supported and the files created can also be read/written
on personal computers running Windows, Linux or the Mac operating system. The PicoMite uses the SPI
protocol to talk to the card and this is not influenced by the card type, so all types (Class 4, 10, UHS-1 etc) are
supported
The SPI protocol needs to be specifically configured before it can be used. First the “system” SPI port needs to
be configured. This is a port that will be used for system use (SD Card, LCD display and the touch controller
on an LCD panel).
There are a number of ports and pins that can be used (see the section PicoMite Hardware) but this example
uses SPI on pins GP18, GP19 and GP16 for Clock, MOSI and MISO.

OPTION SYSTEM SPI GP18, GP19, GP16
Then MMBasic must be told that there is an SD Card attached and what pin is used for the Chip Select signal:

OPTION SDCARD GP22
These commands must be entered at the command prompt (not in a program) and will cause the PicoMite to
restart. This has the side effect of disconnecting the USB console interface which will need to be reconnected.
When the PicoMite is restarted MMBasic will automatically initialise the SD Card interface. This SPI port will
then not be available to BASIC programs (i.e. it is reserved). To verify the configuration, you can use the
command OPTION LIST to list all options that have been set including the configuration of the SD Card.
The basic circuit diagram for connecting the SD Card connector using these pin allocations is illustrated below.

PicoMite
GP22
GP19
GP18
GP16

Note that you can use many different configurations using various pin allocations – this is just an example
based on the configuration commands listed above.
Care must be taken when the SPI port is shared between a number of devices (SD Card, touch, etc). In this case all
the Chip Select signals must configured in MMBasic or alternatively disabled by a permanent connection to 3.3V.
If this is not done any floating Chip Select signal lines will cause the wrong controller to respond to commands on
the SPI bus.
Where no other devices share the SPI bus the SD Card can be set up with:
OPTION SDCARD CSpin, CLKpin, MOSIpin, MISOpin
In this case the pins can be assigned completely flexibly and do not need to be capable of SPI operation.

MMBasic Support for Flash and SD Card Filesystems
The MMBasic support for the Flash Filesystem and SD Cards is almost identical. This allows programs to use
either filesystem with minimal modification. The Flash Filesystem is referred to as drive A: while the SD Card
(when connected) is drive B:. The default drive can be set with the DRIVE command and then the drive prefix is
not needed.
In the following note that:
 On startup the active drive (ie, the default) is A: (the Flash Filesystem).







Any file path that uses the drive letter must be a full path from the root (ie, “A:/mypath/myfile.txt”).
Long file/directory names are supported in addition to the old 8.3 format.
The maximum file/path length is 63 characters.
Upper/lowercase characters and spaces are allowed. The file system on the SD Card is NOT case
sensitive however the Flash Filesystem IS case sensitive.
 Directory paths are allowed in file/directory strings. (i.e., OPEN "A:\dir1\dir2\file.txt" FOR …).
 Either forward or back slashes can be used in paths. E.g. \dir\file.txt is the same as /dir/file.txt.
 The current PicoMite time is used for file create and last access times.
 Up to ten files can be simultaneously open and they can be on both the A: drive and the B: drive.
 Except for INPUT, LINE INPUT and PRINT the # in #fnbr is optional and may be omitted.
Programs can be loaded from or saved to the Flash Filesystem and SD Cards using these commands.


LOAD fname$ [, R]
Load a BASIC program. The optional suffix ",R" will cause the program to be run after it has been loaded
(in this case fname$ must be a string constant).



RUN fname$
Load a BASIC program and run it. fname$ must be a string constant.



SAVE fname$
Save the current program to the Flash Filesystem or SD Card.

These are the basic commands for reading and writing data.


OPEN fname$ FOR mode AS #fnbr
Opens a file for reading or writing. 'fname$' is the file name in 8.3 format. 'mode' can be INPUT,
OUTPUT, APPEND or RANDOM. ‘#fnbr’ is the file number (1 to 10).



PRINT #fnbr, expression [[,; ]expression] … etc
Outputs text to the file opened as #fnbr.



INPUT #fnbr, list of variables
Read a list of comma separated data into the variables specified from the file previously opened as #fnbr.



LINE INPUT #fnbr, variable$
Read a complete line into the string variable specified from the file previously opened as #fnbr.



FLUSH #fnbr
Forces any buffered writes to be written to the Flash Filesystem or SD Card. It is recommended that this
command be used regularly where data loss could occur in the event of power loss.



CLOSE #fnbr [,#fnbr] …
Close the file(s) previously opened with the file number ‘#fnbr’.

Basic file and directory manipulation. Most can be done at the command prompt or from within a BASIC
program.


DRIVE drive$
Sets the active disk drive as ‘drive$’. ‘drive$’ can be “A:” or “B:” where A is the flash drive and B is the
SD Card (if configured).



DRIVE "A:/FORMAT"
Reformat the Flash Filesystem (drive A:) to its initial state.



FILES [wildcard]
Search the current directory and list the files/directories found. Note: Can only be used at the command
prompt, not within a program.



LIST fname$
List the contents of a program or text file on the console.





KILL fname$
Delete a file in the current directory on the current drive. See the command reference for more details on
wildcard deletes.



MKDIR dname$
Creates a sub directory in the current directory on the current drive.



CHDIR dname$
Change into to the directory $dname. $dname can also be "." (dot dot) for up one directory or "\" for the
root directory. The starting point is the current directory on the current drive.



RMDIR dir$
Remove, or delete, the directory ‘dir$’ in the current directory on the current drive.



SEEK #fnbr, pos
Will position the read/write pointer in a file that has been opened for RANDOM access to the 'pos' byte.



RENAME fromname$ AS toname$
Will rename the file fromname$ to have the name toname$ in the current directory on the current drive



COPY [mode] fromname$ TO toname$
Will copy the file fromname$ to have the file toname$. See the command reference for more details on the
optional mode and wildcard copies.

Also there are a number of functions that support the above commands.


INPUT$(nbr, #fnbr)
Will return a string composed of ‘nbr’ characters read from a file previously opened for INPUT with the
file number ‘#fnbr’. If less than ‘nbr’ characters are available the function will return with what it has
(including an empty string if no characters are available).



DIR$( fspec, type )
Will search for files and return the names of entries found.



CWD$
Will return the current working directory.



EOF( #fnbr )
Will return true if the file previously opened for INPUT with the file number ‘#fnbr’ is positioned at the
end of the file.



LOC( #fnbr )
For a file opened as RANDOM this will return the current position of the read/write pointer in the file.



LOF( #fnbr )
Will return the current length of the file in bytes.



MM.INFO(drive)
Will return the current active drive – ie, "A:" or "B:"



MM.INFO(free space)
Will return how much space is left on the active drive



MM.INFO(disk size)
Will return the size of the active drive



MM.INFO(exists file fname$)
Will return true if the file exists



MM.INFO(exists dir dirname$)
Will return true if the directory exists



XModem Transfer
In addition to the standard method of XModem transfer which copies to or from the program memory the
PicoMite can also copy to and from a file on the Flash Filesystem or SD Card. The syntax is:
XMODEM SEND filename$
or
XMODEM RECEIVE filename$
Where ‘filename$’ is the file to save or send. ‘filename$’ can be a string expression, variable or constant. If it
is a constant the string must be quoted (e.g., XMODEM SEND "prbas.bas"). In the case of receiving a file, any
file with the same name will be overwritten.

Load and Save Image
An image can be loaded from the Flash Filesystem or SD Card for display on an attached LCD display panel.
This can be used to draw a logo or add a background on the display. The syntax is:
LOAD IMAGE filename$ [, StartX, StartY]
or
LOAD JPG filename$ [, StartX, StartY]
Where ‘filename$’ is the image to load and ‘StartX’/’StartY’ are the coordinates of the top left corner of the
image (these are optional and will default to the top left corner of the display if not specified).
The image must be in the BMP format (for LOAD IMAGE) or JPG format (for LOAD JPG) and MMBasic will
add “.BMP” or “.JPG” to the file name if an extension is not specified. All types of the BMP or JPG formats
are supported including black and white and true colour 24-bit images.
The current image on a ILI9341 based LCD screen can be saved to a file using the following command:
SAVE IMAGE filename$ [,StartX, StartY, width, height]
This will save the image, or part of the image, as a 24-bit true colour BMP file (the extension .BMP) will be
added if an extension is not supplied.

Example of Sequential I/O
In the example below a file is created and two lines are written to the file (using the PRINT command). The
file is then closed.
OPEN "fox.txt" FOR OUTPUT AS #1
PRINT #1, "The quick brown fox"
PRINT #1, "jumps over the lazy dog"
CLOSE #1
You can read the contents of the file using the LINE INPUT command. For example:
OPEN "fox.txt" FOR INPUT AS #1
LINE INPUT #1,a$
LINE INPUT #1,b$
CLOSE #1
LINE INPUT reads one line at a time so the variable a$ will contain the text "The quick brown fox" and b$
will contain "jumps over the lazy dog".
Another way of reading from a file is to use the INPUT$() function. This will read a specified number of
characters. For example:
OPEN "fox.txt" FOR INPUT AS #1
ta$ = INPUT$(12, #1)
tb$ = INPUT$(3, #1)
CLOSE #1



The first INPUT$() will read 12 characters and the second three characters. So the variable ta$ will contain
"The quick br" and the variable tb$ will contain "own".
Files normally contain just text and the print command will convert numbers to text. So in the following
example the first line will contain the line "123" and the second "56789".
nbr1 = 123 : nbr2 = 56789
OPEN "numbers.txt" FOR OUTPUT AS #1
PRINT #1, nbr1
PRINT #1, nbr2
CLOSE #1
Again you can read the contents of the file using the LINE INPUT command but then you would need to
convert the text to a number using VAL().
For example:
OPEN "numbers.txt" FOR INPUT AS #1
LINE INPUT #1, a$
LINE INPUT #1, b$
CLOSE #1
x = VAL(a$) : y = VAL(b$)
Following this the variable x would have the value 123 and y the value 56789.

Random File I/O
For random access the file should be opened with the keyword RANDOM. For example:
OPEN "filename" FOR RANDOM AS #1
To seek to a record within the file you would use the SEEK command which will position the read/write
pointer to a specific byte. The first byte in a file is numbered one so, for example, the fifth record in a file that
uses 64 byte records would start at byte 257. In that case you would use the following to point to it:
SEEK #1, 257
When reading from a random access file the INPUT$() function should be used as this will read a fixed number
of bytes (i.e. a complete record) from the file. For example, to read a record of 64 bytes you would use:
dat$ = INPUT$(64, #1)
When writing to the file a fixed record size should be used and this can be easily accomplished by adding
sufficient padding characters (normally spaces) to the data to be written. For example:
PRINT #1, dat$ + SPACE$(64 – LEN(dat$);
The SPACE$() function is used to add enough spaces to ensure that the data written is an exact length (64 bytes
in this example). The semicolon at the end of the print command suppresses the addition of the carriage return
and line feed characters which would make the record longer than intended.
Two other functions can help when using random file access. The LOC() function will return the current byte
position of the read/write pointer and the LOF() function will return the total length of the file in bytes.
The following program demonstrates random file access. Using it you can append to the file (to add some data
in the first place) then read/write records using random record numbers. The first record in the file is record
number 1, the second is 2, etc.
RecLen = 64
OPEN "test.dat" FOR RANDOM AS #1
DO
abort: PRINT
PRINT "Number of records in the file =" LOF(#1)/RecLen
INPUT "Command (r = read, w = write, a = append, q = quit): ", cmd$
IF cmd$ = "q" THEN CLOSE #1 : END
IF cmd$ = "a" THEN



SEEK #1, LOF(#1) + 1
ELSE
INPUT "Record Number: ", nbr
IF nbr < 1 or nbr > LOF(#1)/RecLen THEN PRINT "Invalid record" : GOTO abort
SEEK #1, RecLen * (nbr - 1) + 1
ENDIF
IF cmd$ = "r" THEN
PRINT "The record = " INPUT$(RecLen, #1)
ELSE
LINE INPUT "Enter the data to be written: ", dat$
PRINT #1,dat$ + SPACE$(RecLen - LEN(dat$));
ENDIF
LOOP

Random access can also be used on a normal text file. For example, this will print out a file backwards:
OPEN "file.txt" FOR RANDOM AS #1
FOR i = LOF(#1) TO 1 STEP -1
SEEK #1, i
PRINT INPUT$(1, #1);
NEXT i
CLOSE #1



Variables and Expressions
In MMBasic command names, function names, labels, variable names, file names, etc are not case sensitive, so
that "Run" and "RUN" are equivalent and "dOO" and "Doo" refer to the same variable.

Variables
Variables can start with an alphabetic character or underscore and can contain any alphabetic or numeric
character, the period (.) and the underscore (_). They may be up to 31 characters long.
A variable name or a label must not be the same as a function or one of the following keywords: THEN, ELSE,
GOTO, GOSUB, TO, STEP, FOR, WHILE, UNTIL, LOAD, MOD, NOT, AND, OR, XOR, AS.
E.g. step = 5 is illegal as STEP is a keyword.
MMBasic supports three types of variables:
1. Double Precision Floating Point.
These can store a number with a decimal point and fraction (e.g. 45.386) however they will lose accuracy
when more than 14 digits of precision are used. Floating point variables are specified by adding the
suffix '!' to a variable's name (e.g. i!, nbr!, etc). They are also the default when a variable is created
without a suffix (e.g. i, nbr, etc).
2. 64-bit Signed Integer.
These can store positive or negative numbers with up to 19 decimal digits without losing accuracy but
they cannot store fractions (i.e. the part following the decimal point). These are specified by adding the
suffix '%' to a variable's name. For example, i%, nbr%, etc.
3. A String.
A string will store a sequence of characters (e.g. "Tom"). Each character in the string is stored as an
eight bit number and can therefore have a decimal value of 0 to 255. String variable names are
terminated with a '$' symbol (e.g. name$, s$, etc). Strings can be up to 255 characters long.
Note that it is illegal to use the same variable name with different types. E.g. using nbr! and nbr% in the
same program would cause an error.
Most programs use floating point variables for arithmetic as these can deal with the numbers used in typical
situations and are more intuitive than integers when dealing with division and fractions. So, if you are not
bothered with the details, always use floating point.

Constants
Numeric constants may begin with a numeric digit (0-9) for a decimal constant, &H for a hexadecimal
constant, &O for an octal constant or &B for a binary constant. For example &B1000 is the same as the
decimal constant 8. Constants that start with &H, &O or &B are always treated as 64-bit unsigned integer
constants.
Decimal constants may be preceded with a minus (-) or plus (+) and may be terminated with 'E' followed by an
exponent number to denote exponential notation. For example 1.6E+4 is the same as 16000.
When a constant number is used it will be assumed that it is an integer if a decimal point or exponent is not
used. For example, 1234 will be interpreted as an integer while 1234.0 will be interpreted as a floating point
number.
String constants must be surrounded by double quote marks ("). E.g. "Hello World".

OPTION DEFAULT
A variable can be used without a suffix (i.e. !, % or $) and in that case MMBasic will use the default type of
floating point. For example, the following will create a floating point variable:
Nbr = 1234
However. the default can be changed with the OPTION DEFAULT command. For example, OPTION
DEFAULT INTEGER will specify that all variables without a specific type will be integer. So, the following
will create an integer variable:
OPTION DEFAULT INTEGER
Nbr = 1234



The default can be set to FLOAT (which is the default when a program is run), INTEGER, STRING or NONE.
In the latter all variables must be specifically typed otherwise an error will occur.
The OPTION DEFAULT command can be placed anywhere in the program and changed at any time but good
practice dictates that if it is used it should be placed at the start of the program and left unchanged.

OPTION EXPLICIT
By default MMBasic will automatically create a variable when it is first referenced. So, Nbr = 1234 will
create the variable and set it to the number 1234 at the same time. This is convenient for short and quick
programs but it can lead to subtle and difficult to find bugs in large programs. For example, in the third line of
this fragment the variable Nbr has been misspelt as Nbrs. As a consequence the variable Nbrs would be
created with a value of zero and the value of Total would be wrong.
Nbr = 1234
Incr = 2
Total = Nbrs + Incr
The OPTION EXPLICIT command tells MMBasic to not automatically create variables. Instead they must be
explicitly defined using the DIM, LOCAL or STATIC commands (see below) before they are used. The use of
this command is recommended to support good programming practice. If it is used it should be placed at the
start of the program before any variables are used.

DIM and LOCAL
The DIM and LOCAL commands can be used to define a variable and set its type and are mandatory when the
OPTION EXPLICIT command is used.
The DIM command will create a global variable that can be seen and used throughout the program including
inside subroutines and functions. However, if you require the definition to be visible only within a subroutine
or function, you should use the LOCAL command at the start of the subroutine or function. LOCAL has
exactly the same syntax as DIM.
If LOCAL is used to specify a variable with the same name as a global variable then the global variable will be
hidden to the subroutine or function and any references to the variable will only refer to the variable defined by
the LOCAL command. Any variable created by LOCAL will vanish when the program leaves the subroutine.
At its simplest level DIM and LOCAL can be used to define one or more variables based on their type suffix or
the OPTION DEFAULT in force at the time. For example:
DIM nbr%, s$
But it can also be used to define one or more variables with a specific type when the type suffix is not used:
DIM INTEGER nbr, nbr2, nbr3, etc
In this case nbr, nbr2, nbr3, etc are all created as integers. When you use the variable within a program you do
not need to specify the type suffix. For example, MyStr in the following works perfectly as a string variable:
DIM STRING MyStr
MyStr = "Hello"
The DIM and LOCAL commands will also accept the Microsoft practice of specifying the variable's type after
the variable with the keyword "AS". For example:
DIM nbr AS INTEGER, s AS STRING
In this case the type of each variable is set individually (not as a group as when the type is placed before the list
of variables).
The variables can also be initialised while being defined. For example:
DIM INTEGER a = 5, b = 4, c = 3
DIM s$ = "World", i% = &H8FF8F
DIM msg AS STRING = "Hello" + " " + s$
The value used to initialise the variable can be an expression including user defined functions.
The DIM or LOCAL commands are also used to define an array and all the rules listed above apply when
defining an array. For example, you can use:
DIM INTEGER nbr(10), nbr2, nbr3(5,8)



When initialising an array the values are listed as comma separated values with the whole list surrounded by
brackets. For example:
DIM INTEGER nbr(5) = (11, 12, 13, 14, 15, 16)
or
DIM days(7) AS STRING = ("","Sun","Mon","Tue","Wed","Thu","Fri","Sat")

STATIC
Inside a subroutine or function it is sometimes useful to create a variable which is only visible within the
subroutine or function (like a LOCAL variable) but retains its value between calls to the subroutine or function.
You can do this by using the STATIC command. STATIC can only be used inside a subroutine or function and
uses the same syntax as LOCAL and DIM. The difference is that its value will be retained between calls to the
subroutine or function (i.e. it will not be initialised on the second and subsequent calls).
For example, if you had the following subroutine and repeatedly called it, the first call would print 5, the
second 6, the third 7 and so on.
SUB Foo
STATIC var = 5
PRINT var
var = var + 1
END SUB
Note that the initialisation of the static variable to 5 (as in the above example) will only take effect on the first
call to the subroutine. On subsequent calls the initialisation will be ignored as the variable had already been
created on the first call.
As with DIM and LOCAL the variables created with STATIC can be float, integers or strings and arrays of
these with or without initialisation. The length of the variable name created by STATIC and the length of the
subroutine or function name added together cannot exceed 31 characters.

CONST
Often it is useful to define an identifier that represents a value without the risk of the value being accidently
changed - which can happen if variables were used for this purpose (this practice encourages another class of
difficult to find bugs).
Using the CONST command you can create an identifier that acts like a variable but is set to a value that cannot
be changed. For example:
CONST InputVoltagePin = 31
CONST MaxValue = 2.4
The identifiers can then be used in a program where they make more sense to the casual reader than simple
numbers. For example:
IF PIN(InputVoltagePin) > MaxValue THEN SoundAlarm
A number of constants can be created on the one line:
CONST InputVoltagePin = 31, MaxValue = 2.4, MinValue = 1.5
The value used to initialise the constant is evaluated when the constant is created and can be an expression
including user defined functions.
The type of the constant is derived from the value assigned to it; so for example, MaxValue above will be a
floating point constant because 2.4 is a floating point number. The type of a constant can also be explicitly set
by using a type suffix (i.e. !, % or $) but it must agree with its assigned value.

Special Characters in Strings
Special, non-printable characters can be inserted in string constants using the backslash (ie, \) as an escape
symbol. To enable this facility the command OPTION ESCAPE must be placed at the start of the program.
These are the valid escape sequences:
Hex Value
\a
\b
\e


07
08
1B

Description
Alert (Beep, Bell)
Backspace
Escape character


\f
\n
\r
\q
\t
\v
\\
\nnn
\&hh

0C
0A
0D
22
09
0B
5C
any
any

Formfeed Page Break
Newline (Line Feed)
Carriage Return
Quote symbol
Horizontal Tab
Vertical Tab
Backslash
The byte whose value is given by nnn interpreted as a decimal number
The byte whose value is given by hh… interpreted as a hexadecimal number

For example, the following will print the words Hello and World on separate lines:
OPTION ESCAPE
PRINT "Hello\r\nWorld"

Expressions and Operators
MMBasic will evaluate a mathematical expression using the standard mathematical rules. For example,
multiplication and division are performed first followed by addition and subtraction. These are called the rules
of precedence and are detailed below.
This means that 2 + 3 * 6 will resolve to 20, so will 5 * 4 and also 10 + 4 * 3 – 2.
If you want to force the interpreter to evaluate parts of the expression first you can surround that part of the
expression with brackets. For example, (10 + 4) * (3 – 2) will resolve to 14 not 20 as would have been the case
if the brackets were not used. Using brackets does not appreciably slow down the program so you should use
them liberally if there is a chance that MMBasic will misinterpret your intention.
The following operators, in order of precedence, are implemented in MMBasic. Operators that are on the same
level (for example + and -) are processed with a left to right precedence as they occur on the program line.
Arithmetic operators:
Exponentiation (e.g. b^n means bn)

^
*

/ \ MOD

+ -

Multiplication, division, integer division and modulus (remainder)
Addition and subtraction

Shift operators:
x << y

x >> y

These operate in a special way. << means that the value returned
will be the value of x shifted by y bits to the left while >> means the
same only right shifted. They are integer functions and any bits
shifted off are discarded and any bits introduced are set to zero.

Logical operators:
NOT INV

invert the logical value on the right (e.g. NOT a=b is a<>b)
or bitwise inversion of the value on the right (e.g. a = INV b)

<>
>=

Inequality, less than, greater than, less than or equal to, less than or
equal to (alternative version), greater than or equal to, greater than or
equal to (alternative version)

< > <= =<
=>

=
AND

equality
OR

XOR

Conjunction, disjunction, exclusive or

For Microsoft compatibility the operators AND, OR and XOR are integer bitwise operators. For example,
PRINT (3 AND 6) will output the number 2. Because these operators can act as both logical operators (for
example, IF a=5 AND b=8 THEN …) and as bitwise operators (e.g. y% = x% AND &B1010) the interpreter
will be confused if they are mixed in the same expression. So, always evaluate logical and bitwise expressions
in separate expressions.
The other logical operations result in the integer 0 (zero) for false and 1 for true. For example the statement
PRINT 4 >= 5 will print the number zero on the output and the expression A = 3 > 2 will store +1 in A.


The NOT operator will invert the logical value on its right (it is not a bitwise invert) while the INV operator
will perform a bitwise invert. Both of these have the highest precedence so they will bind tightly to the next
value. For normal use of NOT or INV the expression to be operated on should be placed in brackets. Eg:
IF NOT (A = 3 OR A = 8) THEN …
String operators:
+
<>
>=

Join two strings
< > <= =<
=>

=

Inequality, less than, greater than, less than or equal to, less than or
equal to (alternative version), greater than or equal to, greater than or
equal to (alternative version)
Equality

String comparisons respect case. For example "A" is greater than "a".

Mixing Floating Point and Integers
MMBasic automatically handles conversion of numbers between floating point and integers. If an operation
mixes both floating point and integers (e.g. PRINT A% + B!) the integer will be converted to a floating point
number first, then the operation performed and a floating point number returned. If both sides of the operator
are integers then an integer operation will be performed and an integer returned.
The one exception is the normal division ("/") which will always convert both sides of the expression to a
floating point number and then returns a floating point number. For integer division you should use the integer
division operator "\".
MMBasic functions will return a float or integer depending on their characteristics. For example, PIN() will
return an integer when the pin is configured as a digital input but a float when configured as an analog input.
If necessary you can convert a float to an integer with the INT() function. It is not necessary to specifically
convert an integer to a float but if it was needed the integer value could be assigned to a floating point variable
and it will be automatically converted in the assignment.

64-bit Unsigned Integers
MMBasic on the PicoMite supports 64-bit signed integers. This means that there are 63 bits for holding the
number and one bit (the most significant bit) which is used to indicate the sign (positive or negative). However
it is possible to use full 64-bit unsigned numbers as long as you do not do any arithmetic on the numbers.
64-bit unsigned numbers can be created using the &H, &O or &B prefixes to a number and these numbers can
be stored in an integer variable. You then have a limited range of operations that you can perform on these.
They are << (shift left), >> (shift right), AND (bitwise and), OR (bitwise or), XOR (bitwise exclusive or), INV
(bitwise inversion), = (equal to) and <> (not equal to). Arithmetic operators such as division or addition may
be confused by a 64-bit unsigned number and could return nonsense results.
To display 64-bit unsigned numbers you should use the HEX$(), OCT$() or BIN$() functions.
For example, the following 64-bit unsigned operation will return the expected results:
X% = &HFFFF0000FFFF0044
Y% = &H800FFFFFFFFFFFFF
X% = X% AND Y%
PRINT HEX$(X%, 16)
Will display "800F0000FFFF0044"



Subroutines and Functions
A program defined subroutine or function is simply a block of programming code that is contained within a
module and can be called from anywhere within your program. It is the same as if you have added your own
command or function to the language.

Subroutines
A subroutine acts like a command and it can have arguments (sometimes called a parameter list). In the
definition of the subroutine they look like this:
SUB MYSUB arg1, arg2$, arg3
<statements>
<statements>
END SUB
And when you call the subroutine you can assign values to the arguments. For example:
MYSUB 23, "Cat", 55
Inside the subroutine arg1 will have the value 23, arg2$ the value of "Cat", and so on. The arguments act
like ordinary variables but they exist only within the subroutine and will vanish when the subroutine ends. You
can have variables with the same name in the main program and they will be hidden by the arguments defined
for the subroutine.
When calling a subroutine you can supply less than the required number of values and in that case the missing
values will be assumed to be either zero or an empty string. You can also leave out a value in the middle of the
list and the same will happen. For example:
MYSUB

23, , 55

Will result in arg2$ being set to the empty string "".
Rather than using the type suffix (e.g. the $ in arg2$) you can use the suffix AS <type> in the definition of the
subroutine argument and then the argument will be known as the specified type, even when the suffix is not
used. For example:
SUB MYSUB arg1, arg2 AS STRING, arg3
IF arg2 = "Cat" THEN …
END SUB
Inside a subroutine you can define a variable using LOCAL (which has the same syntax as DIM). This variable
will only exist within the subroutine and will vanish when the subroutine exits.

ONEWIRE RESET will reset the 1-Wire bus
ONEWIRE WRITE will send a number of bytes
ONEWIRE READ will read a number of bytes
'pin' is the I/O pin (located in the rear connector) to use. It can be any pin
capable of digital I/O.
'flag' is a combination of the following options:
1 - Send reset before command
2 - Send reset after command
4 - Only send/recv a bit instead of a byte of data
8 - Invoke a strong pullup after the command (the pin will be set high and open
drain disabled)
'length' is the length of data to send or receive
'data' is the data to send or variable to receive. The number of data items must
agree with the length parameter.
See also Appendix C.

OPEN fname$ FOR mode AS
[#]fnbr

Opens a file for reading or writing.
‘fname’ is the filename with an optional extension separated by a dot (.).
Long file names with upper and lower case characters are supported.
A directory path can be specified with the backslash as directory separators.
The parent of the current directory can be specified by using a directory name
of “..” (two dots) and the current directory with “.” (a single dot).
For example OPEN ".\dir1\dir2\filename.txt" FOR INPUT AS #1
‘mode’ is INPUT, OUTPUT, APPEND or RANDOM.
INPUT will open the file for reading and throw an error if the file does not
exist. OUTPUT will open the file for writing and will automatically overwrite
any existing file with the same name.
APPEND will also open the file for writing but it will not overwrite an existing
file; instead any writes will be appended to the end of the file. If there is no
existing file the APPEND mode will act the same as the OUTPUT mode (i.e.
the file is created then opened for writing).
RANDOM will open the file for both read and write and will allow random
access using the SEEK command. When opened the read/write pointer is
positioned at the end of the file.
‘fnbr’ is the file number (1 to 10). The # is optional. Up to 10 files can be
open simultaneously. The INPUT, LINE INPUT, PRINT, WRITE and
CLOSE commands as well as the EOF() and INPUT$() functions all use ‘fnbr’
to identify the file being operated on.
See also ON ERROR and MM.ERRNO for error handling.



OPEN comspec$ AS [#]fnbr

Will open a serial communications port for reading and writing. Two ports are
available (COM1: and COM2:) and both can be open simultaneously. For a
full description with examples see Appendix A.
Using ‘fnbr’ the port can be written to and read from using any command or
function that uses a file number.

OPEN comspec$ AS GPS
[,timezone_offset] [,monitor]

Will open a serial communications port for reading from a GPS receiver. See
the GPS function for details. The sentences interpreted are GPRMC, GNRMC,
GPGGA and GNGGA.
The timezone_offset parameter is used to convert UTC as received from the
GPS to the local timezone. If omitted the timezone will default to UTC. The
timezone_offset can be a any number between -12 and 14 allowing the time to
be set correctly even for the Chatham Islands in New Zealand (UTC +12:45).
If the monitor parameter is set to 1 then all GPS input is directed to the
console. This can be stopped by closing the GPS channel.

OPTION

See the section Options earlier in this manual.

PAUSE delay

Halt execution of the running program for ‘delay’ ms. This can be a fraction.
For example, 0.2 is equal to 200 µs. The maximum delay is 2147483647 ms
(about 24 days).
Note that interrupts will be recognised and processed during a pause.

PIN( pin ) = value

For a ‘pin’ configured as digital output this will set the output to low (‘value’
is zero) or high (‘value’ non-zero). You can set an output high or low before it
is configured as an output and that setting will be the default output when the
SETPIN command takes effect.
See the function PIN() for reading from a pin and the command SETPIN for
configuring it. Refer to the section Using the I/O pins for a general description
of the PicoMite's input/output capabilities.

PIO

The RP2040 chip used in the PicoMite contains a programmable I/O system
with two identical PIO devices (pio%=0 or pio%=1) acting like specialised
CPU cores. See the Appendix for a more detailed description.

PIO assemble pio,linedata$

This command will assemble and load text based PIO assembler code
including labels for jumps
Use: PIO assemble pio,".program anything" to initialise the assembler
Use: PIO assemble pio,".side_set n [opt] [pindirs]" if using side set. This is
mandatory in order to correctly construct the op-codes if one or more side set
pins are used.
It does not load the pinctrl register as this is specific to the state-machine.
Also note the "opt" parameter changes the op-code on instructions that have a
side parameter
Use: PIO assemble pio,".line n" to assemble starting from a line other than 1 this is optional
Use: PIO assemble pio,".end program [list]" to terminate the assembly and
program the pio. The optional parameter LIST causes a hex dump of the opcodes to the terminal.
Use: PIO assemble pio,"label:" to define a label. This must appear as a separate
command.
Use: PIO assemble “’wrap target” to specify where the program will wrap to.
See PIO(.wrap target) for how to use this.
Use: PIO assemble “.wrap” to specify where the program should wrap back to
from “.wrap target” . See PIO(.wrap) for how to use this.
Use: PIO assemble pio "instruction [parameters]" to define the actual PIO
instructions that will be converted to machine code



PIO DMA RX pio, sm, nbr,
data%() [,completioninterrupt]
[,transfersize]
[,loopbackcount]
PIO DMA TX pio, sm, nbr,
data%() [,completioninterrupt]
[,transfersize]
[,loopbackcount]

Sets up DMA transfers from PIO to MMBasic memory
pio specifies which of the two pio instances to use (0 or 1
sm specifies which of the state machine to use (0-3)
nbr specifies how many 32-bit words to transfer. See below for the special case
of setting nbr to zero.
data%() is the array that will either supply or receive the PIO data
The optional parameter completioninterrupt is the name of a MMBasic
subroutine rthat will be called when the DMA completes and in the case of
DMA_OUT the FIFO has been emptied.
If the optional interrupt is not used then the status of the DMA can be checked
using the functions
MM.INFO(PIO RX DMA)
MM.INFO(PIO TX DMA)
The optional parameter transfersize allows the user to override the normal 32bit transfers and select 8, 16, or 32.
The optional parameter loopbackcount specifies how many data items are to be
read or written before the DMA starts again at the beginning of the buffer
The parameter must be a power of 2 between 2 and 32768
Due to a limitation in the RP2040 if loopbackcount is used the MMBasic array
must be aligned in memory to the number of bytes in the loop
Thus if the array is 64 integers long which is 512 bytes then the array must be
aligned to a 512byte boundary in memory
All MMBasic arrays are aligned to a 256 byte boundary but to create an array
which is guaranteed to be aligned to a 512 byte boundary or greater the PIO
MAKE RING BUFFER command must be used
If loopbackcount is set then “nbr” can be set to 0. In this case the transfer will
run continuously repeatedly filling the buffer until explicitly stopped

PIO DMA RX OFF
PIO DMA TX OFF

Aborts a running DMA

PIO INTERRUPT pio, sm
[,RXinterrupt] [,TXinterrupt]

Sets Basic interrupts for PIO activity.
Use the value 0 for RXinterrupt or TXinterrupt to disable an interrupt
Omit values not needed
The RX interrupt triggers whenever a word has been "pushed" by the PIO code
into the specified FIFO. The data MUST be read in the interrupt to clear it.
The TX interrupt triggers whenever the specified FIFO has been FULL and the
PIO code has now "pulled" it

PIO INIT MACHINE pio%,
statemachine%, clockspeed
[,pinctrl] [,execctrl] [,shiftctrl]
[,startinstruction]

PIO interrupts have priority have keyboard interrupts but before anything else.
As with all interrupts interrupt conditions are processed one at a time.
Initialises PIO 'pio%' with state machine 'statemachine%'. 'clockspeed' is the
clock speed of the state machine in kHz. The four optional arguments are
variables holding initialising values of the state machine registers and the
address of the first instruction to execute (defaults to zero). These decide how
the PIO will operate.
It is anticipated that eventually the PIO assembler will be able to generate the
register values for the user along with the program array based on the defined
assembler directives.

PIO EXECUTE pio,
state_machine, instruction%

Immediately executes the instruction on the pio and state machine specified.



PIO WRITE pio,
state_machine, count, data0
[,data1..]

Writes the data elements to the pio and state machine specified. The write is
blocking so the state machine needs to be able to take the data supplied
NB: this command will probably need additional capability in future releases

PIO READ pio,
state_machine, count,
data%[()]

Reads the data elements from the pio and state machine specified. The read is
non-blocking so the state machine needs to be able to supply the data
requested. When count is one then an integer can be used to receive the data,
otherwise and integer array should be specified.
NB: this command will probably need additional capability in future releases

PIO START pio, statemachine

Start a given state machine on pio

PIO STOP pio, statemachine

Stop a given state machine on pio

PIO CLEAR pio

This stops the pio specified on all statemachines and clears the control registers
for the statemachines PINCTRL, EXECTRL, and SHIFTCTRL to defaults

PIO PROGRAM LINE pio,
line, instruction

Programs just the specified line in a PIO program

PIXEL x, y [,c]

Set a pixel on an attached LCD panel to a colour. 'x' is the horizontal
coordinate and 'y' is the vertical coordinate of the pixel. 'c' is a 24 bit number
specifying the colour. 'c' is optional and if omitted the current foreground
colour will be used. All parameters can be expressed as arrays and the software
will plot the number of pixels as determined by the dimensions of the smallest
array. 'x' and 'y' must both be arrays or both be single variables /constants
otherwise an error will be generated. 'c' can be either an array or a single
variable or constant.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

PLAY

This command will generate a variety of audio outputs.
See the OPTION AUDIO command for setting the I/O pins to be used for the
output. The audio is a pulse width modulated signal so a low pass filter is
required to remove the carrier frequency.

PLAY TONE left [, right [,
dur] [,interrupt]]]

Generates two separate sine waves on the sound output left and right channels.
'left' and 'right' are the frequencies in Hz to use for the left and right channels.
The tone plays in the background (the program will continue running after this
command) and 'dur' specifies the number of milliseconds that the tone will
sound for. If the duration is not specified the tone will continue until explicitly
stopped or the program terminates.
'interrupt' is an optional subroutine which will be called when the play
terminates.
The frequency can be from 1Hz to 20KHz and is very accurate (it is based on a
crystal oscillator). The frequency can be changed at any time by issuing a new
PLAY TONE command.

PLAY FLAC file$ [, interrupt]

Will play a FLAC file on the sound output.
'file$' is the FLAC file to play (the extension of .flac will be appended if
missing). The sample rate can be up to 48kHz in stereo (96kHz if the Pico is
overclocked)
The FLAC file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY WAV file$ [, interrupt]

Will play a WAV file on the sound output.
'file$' is the WAV file to play (the extension of .wav will be appended if



missing). The WAV file must be PCM encoded in mono or stereo with 8 or
16-bit sampling. The sample rate can be up to 48kHz in stereo (96kHz if the
Pico is overclocked).
The WAV file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
PLAY MODFILE file$
[,interrupt]

Will play a MOD file on the sound output.
'file$' is the MOD file to play (the extension of .mod will be appended if
missing).
The MOD file is played in the background and will play continuously in a
loop. If the optional 'interrupt' is specified This will be called when the file has
played once through the sequence and playback will then be terminated.

PLAY MODSAMPLE
Samplenum, channel
[,volume]

Plays a specific sample in the mod file on the channel specified. The volume is
optional and can be between 0 and 64. This command can only be used when
there is a mod file already playing and allows sound effects to be output whilst
the background music is still playing.

PLAY LOAD SOUND
array%()

Loads a 1024 element array comprising 4096 16-bit values between 0 and
4095. This provides the data for any arbitrary waveform that can be played by
the PLAY SOUND command. You can use the MEMORY PACK command to
create the arrays from a normal 40956 element integer array.

PLAY SOUND soundno,
channelno, type [,frequency]
[,volume]

Play a series of sounds simultaneously on the audio output.
'soundno' is the sound number and can be from 1 to 4 allowing for four
simultaneous sounds on each channel.
'channelno' specifies the output channel. It can be L (left speaker), R (right
speaker), B (both speakers) or M (mono output with the right channel inverted
compared to the left).
type' specifies the wave form It can be S (Sine wave), Q (square wave) ,T
(triangular wave) ,W (saw tooth) , O (Null output), P (periodic noise), N
(random noise) or U (user defined using the PLAY LOAD sound command).to
be used.
'frequency' is the frequency from 1 to 20000 (Hz) and it must be specified
except when type is O.
'volume' is optional and must be between 1 and 25. It defaults to 25
The first time PLAY SOUND is called all other audio usage will be blocked
and will remain blocked until PLAY STOP is called. Output can be stopped
temporarily using PLAY PAUSE and PLAY RESUME.
Calling SOUND on an already running 'soundno' will immediately replace the
previous output. Individual sounds are turned off using type “O”
Running 4 sounds simultaneously on both channels of the audio output
consumes about 23% of the CPU.

PLAY PAUSE
PLAY RESUME
PLAY STOP

PLAY PAUSE will temporarily halt the currently playing file or tone.
PLAY RESUME will resume playing a sound that was paused.
PLAY STOP will terminate the playing of the file or tone. When the program
terminates for whatever reason the sound output will also be automatically
stopped.

PLAY VOLUME left, right

Will adjust the volume of the audio output.
'left' and 'right' are the levels to use for the left and right channels and can be
between 0 and 100 with 100 being the maximum volume. There is a linear
relationship between the specified level and the output. The volume defaults
to maximum when a program is run.

PLAY NEXT
Stops playback of the current audio file and starts the next one in the directory


PLAY PREVIOUS

Stops playback of the current audio file and starts the previous one in the
directory

VS1053 specific PLAY commands
PLAY MP3 file$ [, interrupt]

Will play a MP3 file on the sound output.
'file$' is the MP3 file to play (the extension of .mp3 will be appended if
missing). The sample rate should be 44100Hz stereo.
The MP3 file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY HALT

This command works when a MP3 file is playing. It stops playback and
records the current file position to allow playback to be resumed from the same
point. This command is specifically designed to support for mp3 audio books

PLAY CONTINUE track$

Resumes playback of the MP3 track specified. "track$" will be the name of the
file that was playing when halted with all file attributes removed
e.g.
PLAY MP3 "B:/mp3/mymp3.mp3"
sometime later
PLAY HALT
later again
PLAY CONTINUE "mymp3"

PLAY MIDIFILE file$ [,
interrupt]

Will play a MIDI file on the sound output.
'file$' is the MIDI file to play (the extension of .mid will be appended if
missing).
The MIDI file is played in the background. 'interrupt' is optional and is the
name of a subroutine which will be called when the file has finished playing.
If file$ is a directory the Pico will play all of the files in that directory in turn.

PLAY MIDI

Initiates the real-time midi mode. In this mode midi instructions can be sent to
the VS1053 to select which instruments to play on which channels, turn notes
on, and turn them off in real timer

PLAY MIDI CMD cmd%,
data1%, data2%

Sends a midi command when in real time midi mode. An example would be to
allocate an instrument to a channel. E.g.
PLAY MIDI CMD &B11000001,4 ‘set channel 1 to instrument 4

PLAY MIDI TEST n

Plays a MIDI test sequence, n=0 to 3, 0 = normal realtime, the others play note
and instrument samples

PLAY NOTE ON channel%,
note%, velocity%
PLAY NOTE OFF channel%,
note% [,velocity%]
PLAY STREAM buffer%(),
readpointer%, writepointer%
POKE BYTE addr%, byte
or
POKE SHORT addr%, short%
Or


Turns on the note on the channel specified when in real time MIDI mode

Turns off the note on the channel specified when in real time MIDI mode

Sends data to the VS1053 CODEC from the circular buffer “buffer%”. This
command initiates a background output stream where the VS1053 is sent
anything in the buffer between the readpointer and the write pointer, updating
the readpointer as it goes. Can be used for arbitrary waveform output.
Will set a byte or a word within the virtual memory space.
POKE BYTE will set the byte (i.e. 8 bits) at the memory location 'addr%' to
'byte'. 'addr%' should be an integer.
POKE SHORT will set the short integer (i.e. 16 bits) at the memory location
'addr%' to 'word%'. 'addr%' and short%' should be integers.

POKE WORD addr%, word%
or
POKE INTEGER addr%, int%
or
POKE FLOAT addr%, float!
or
POKE VAR var, offset, byte
or
POKE VARTBL, offset, byte
or
POKE DISPLAY command
[,data1] [,data2] [,datan]

POKE WORD will set the word (i.e. 32 bits) at the memory location 'addr%' to
'word%'. 'addr%' and 'word%' should be integers.
POKE INTEGER will set the MMBasic integer (i.e. 64 bits) at the memory
location 'addr%' to int%'. 'addr%' and int%' should be integers.
POKE FLOAT will set the word (i.e. 32 bits) at the memory location 'addr%'
to 'float!'. 'addr%' should be an integer and 'float!' a floating point number.
POKE VAR will set a byte in the memory address of 'var'. 'offset' is the
±offset from the address of the variable. An array is specified as var().
POKE VARTBL will set a byte in MMBasic's variable table. 'offset' is the
±offset from the start of the variable table. Note that a comma is required after
the keyword VARTBL.
This command sends commands and associated data to the display controller
for a connected display. This allows the programmer to change parameters of
how the display is configured. e.g. POKE DISPLAY &H28 will turn off an
SSD1963 display and POKE DISPLAY &H29 will turn it back on again.
Works for all displays except the ST7790.

POKE DISPLAY HRES n
POKE DISPLAY VRES n

These commands change the stored value of MM.HRES and MM.VRES
allowing the programmer to configure non-standard displays.

POLYGON n, xarray%(),
yarray%() [, bordercolour] [,
fillcolour]

Draws a filled or outline polygon with n xy-coordinate pairs in xarray%() and
yarray%(). If ‘fillcolour’ is omitted then just the polygon outline is drawn. If
‘bordercolour’ is omitted then it will default to the current default foreground
colour.
If the last xy-coordinate pair is not the same as the first the firmware will
automatically create an additional xy-coordinate pair to complete the polygon.
The size of the arrays should be at least as big as the number of x,y coordinate
pairs.
'n' can be an array and the colours can also optionally be arrays as follows:
POLYGON n(), xarray%(), yarray%() [, bordercolour()] [, fillcolour()]
POLYGON n(), xarray%(), yarray%() [, bordercolour] [, fillcolour]
The elements of array n() define the number of xy-coordinate pairs in each of
the polygons. e.g. DIM n(1)=(3,3) would define that 2 polygons are to be
drawn with three vertices each. The size of the n array determines the number
of polygons that will be drawn unless an element is found with the value zero
in which case the firmware only processes polygons up to that point. The x,ycoordinate pairs for all the polygons are stored in xarray%() and yarray%().
The xarray%() and yarray%() parameters must have at least as many elements
as the total of the values in the n array.
Each polygon can be closed with the first and last elements the same. If the last
element is not the same as the first the firmware will automatically create an
additional x,y-coordinate pair to complete the polygon. If fill colour is omitted
then just the polygon outlines are drawn.
The colour parameters can be a single value in which case all polygons are
drawn in the same colour or they can be arrays with the same cardinality as n.
In this case each polygon drawn can have a different colour of both border
and/or fill. For example, this will draw 3 triangles in yellow, green and red:
DIM c%(2)=(3,3,3)
DIM x%(8)=(100,50,150,100,50,150,100,50,150)
DIM y%(8)=(50,100,100,150,200,200,250,300,300)
DIM fc%(2)=(rgb(yellow),rgb(green),rgb(red))
POLYGON c%(),x%(),y%(),fc%(),fc%()

POLYGON n(), xarray%(),
yarray%() [, bordercolour()] [,
fillcolour()]
POLYGON n(), xarray%(),
yarray%() [, bordercolour] [,
fillcolour]



PORT(start, nbr [,start, nbr]…) Set a number of I/O pins simultaneously (i.e. with one command).
= value
'start' is an I/O pin number and the lowest bit in 'value' (bit 0) will be used to
set that pin. Bit 1 will be used to set the pin 'start' plus 1, bit 2 will set pin
'start'+2 and so on for 'nbr' number of bits. I/O pins used must be numbered
consecutively and any I/O pin that is invalid or not configured as an output will
cause an error. The start/nbr pair can be repeated if an additional group of
output pins needed to be added.
For example; PORT(15, 4, 23, 4) = &B10000011
Will set eight I/O pins. Pins 15 and 16 will be set high while 17, 18, 23, 24
and 25 will be set to a low and finally 26 will be set high.
This command can be used to conveniently communicate with parallel devices
like LCD displays. Any number of I/O pins (and therefore bits) can be used
from 1 to the number of I/O pins on the chip.
See the PORT function to simultaneously read from a number of pins.
PRINT expression
[[,; ]expression] … etc

Outputs text to the serial console followed by a carriage return/newline pair.
Multiple expressions can be used and must be separated by either a:
 Comma (,) which will output the tab character
 Semicolon (;) which will not output anything (it is just used to separate
expressions).
 Nothing or a space which will act the same as a semicolon.
A semicolon (;) or a comma (,) at the end of the expression list will suppress
the output of the carriage return/newline pair at the end of a print statement.
When printed, a number is preceded with a space if positive or a minus (-) if
negative but is not followed by a space. Integers (whole numbers) are printed
without a decimal point while fractions are printed with the decimal point and
the significant decimal digits. Large or small floating point numbers are
automatically printed in scientific number format.
The function TAB() can be used to space to a certain column and the STR$()
function can be used to justify or otherwise format strings.

PRINT #nbr, expression
[[,; ]expression] … etc

Same as above except that the output is directed to a serial communications
port or a file opened for OUTPUT or APPEND with a file number of ‘nbr’.
See the OPEN command.

PRINT #GPS, expression
[[,; ]expression] … etc

Outputs a NMEA string to an opened GPS device. The string must start with a
$ character and end with a * character. The checksum is automatically
calculated and appended to the string together with the CR/LF characters.

PRINT @(x [, y]) expression
Or
PRINT @(x, [y], m)
expression

Works on terminal console on an attached computer or the display if OPTION
LCDPANEL CONSOLE is enabled.
Same as the standard PRINT command except that the cursor is positioned at
the coordinates x, y expressed in pixels. If y is omitted the cursor will be
positioned at “x” on the current line.
Example: PRINT @(150, 45) "Hello World"
The @ function can be used anywhere in a print command.
Example: PRINT @(150, 45) "Hello" @(150, 55) "World"
The @(x,y) function can be used to position the cursor anywhere on or off the
screen. For example, PRINT @(-10, 0) "Hello" will only show "llo" as the
first two characters could not be shown because they were off the screen.
The @(x,y) function will automatically suppress the automatic line wrap
normally performed when the cursor goes beyond the right screen margin.
If 'm' is specified the mode of the video operation will be as follows:
m = 0 Normal text (white letters, black background)
m = 1 The background will not be drawn (ie, transparent)
m = 2 The video will be inverted (black letters, white background)
m = 5 Current pixels will be inverted (transparent background)



PULSE pin, width

Will generate a pulse on 'pin' with duration of 'width' ms. 'width' can be a
fraction. For example, 0.01 is equal to 10µs and this enables the generation of
very narrow pulses.
The generated pulse is of the opposite polarity to the state of the I/O pin when
the command is executed. For example, if the output is set high the PULSE
command will generate a negative going pulse. Notes:
 'pin' must be configured as an output.
 For a pulse of less than 3 ms the accuracy is ± 1 µs.
 For a pulse of 3 ms or more the accuracy is ± 0.5 ms.
 A pulse of 3 ms or more will run in the background. Up to five different
and concurrent pulses can be running in the background and each can have
its time changed by issuing a new PULSE command or it can be
terminated by issuing a PULSE command with zero for 'width'.

PWM channel, frequency,
[dutyA]
[,dutyB][,phase][,defer]

PWM SYNC s0
[,s1][,s2][,s3][,s4][,s5][,s6][,s7
]

There are 8 separate PWM frequencies available (channels 0 to 7) and up to 16
outputs with individually controlled duty cycle. You can output on either
PWMnA or PWMnB or both for each channel - no restriction. Duty cycles
are specified as a percentage and you can use a negative value to invert the
output (-100.0 <= duty <=100.0).
Minimum frequency = (cpuspeed + 1) / (2^24) Hz. Maximum speed is
OPTION CPUSPEED/4. At very fast speeds the duty cycles will be
increasingly limited.
Phase is a parameter that causes the waveforms to be centred such that a wave
form with a shorter duty cycle starts and ends equal times from a longer one.
Use 1 to enable this mode and 0 (or omit) to run as normal
The parameter "deferredstart" when set to 1 configures the PWM channels as
but does not start the output running. They can the be started uing the PWM
SYNC command. This can be used to avoid any undesirable startup artefacts
The PWM command is also capable of driving servos as follows:
PWM 1,50,(position_as_a_percentage * 0.05 + 5)
This initiates the PWM on channels where a deferred start was defined or just
syncs existing running channels. However, the power comes in the ability to
offset the channels one to another (defined as a percentage of the time period
as per the duty cycle - can be a float)
You can use an offset of -1 to omit a channel from the synch
Stop output on ‘channel

PWM channel, OFF
RANDOMIZE nbr

Seed the random number generator with ‘nbr’.
On power up the random number generator is seeded with zero and will
generate the same sequence of random numbers each time. To generate a
different random sequence each time you must use a different value for ‘nbr’
(the TIMER function is handy for that).

REFRESH

Initiates an update of the screen for certain black and white displays.
These can only be updated a full screen at a time and if OPTION
AUTOREFRESH is OFF this command can be used to trigger the write. This
applies to the following displays: N5110, SSD1306I2C, SSD1306I2C32,
SSD1306SPI, ST7920.



RBOX x, y, w, h [, r] [,c]
[,fill]

Draws a box with rounded corners on an attached LCD panel starting at 'x' and
'y' which is 'w' pixels wide and 'h' pixels high.
'r' is the radius of the corners of the box. It defaults to 10.
'c' specifies the colour and defaults to the default foreground colour if not
specified. 'fill' is the fill colour. It can be omitted or set to -1 in which case the
box will not be filled.
All parameters can be expressed as arrays and the software will plot the
number of boxes as determined by the dimensions of the smallest array. 'x', 'y',
'w', and 'h' must all be arrays or all be single variables /constants otherwise an
error will be generated. 'r', 'c', and 'fill' can be either arrays or single
variables/constants.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.

READ variable[, variable]..

Reads values from DATA statements and assigns these values to the named
variables. Variable types in a READ statement must match the data types in
DATA statements as they are read.
Arrays can be used as variables (specified with empty brackets, e.g. a()) and in
that case the size of the array is used to determine how many elements are to
be read. If the array is multidimensional then the leftmost dimension will be
the fastest moving.
See also DATA and RESTORE.

READ SAVE
or
READ RESTORE

READ SAVE will save the virtual pointer used by the READ command to
point to the next DATA to be read. READ RESTORE will restore the pointer
that was previously saved.
This enables subroutines to READ data and then restore the read pointer so as
not to disturb other parts of the program that may be reading the same data
statements. These commands can be nested.

REM string

REM allows remarks to be included in a program.
Note the Microsoft style use of the single quotation mark (‘) to denote remarks
is also supported and is preferred.

RENAME old$ AS new$

Rename a file or a directory from ‘old$’ to ‘new$’. Both are strings.
A directory path can be used in both 'old$' and 'new$'. If the paths differ the
file specified in 'old$' will be moved to the path specified in 'new$' with the
file name as specified.

RESTORE [line]

Resets the line and position counters for the READ statement.
If ‘line’ is specified the counters will be reset to the beginning of the specified
line. ‘line’ can be a line number or label or a variable with these values.
If ‘line’ is not specified the counters will be reset to the start of the program.

RMDIR dir$

Remove, or delete, the directory ‘dir$’ on the default Flash Filesystem or SD
Card.

RTC GETTIME

RTC GETTIME will get the current date/time from a PCF8563, DS1307 or
DS3231 real time clock and set the internal MMBasic clock accordingly. The
date/time can then be retrieved with the DATE$ and TIME$ functions.

RTC SETTIME year, month,
day, hour, minute, second

RTC SETTIME will set the time in the clock chip. 'hour' must use 24 hour
notation. ‘year’ can be two or four digits. The RTC SETTIME command will
also accept a single string argument in the format of dd/mm/yy hh:mm. This
means the date/time could be entered by the user using a GUI FORMATBOX
with the DATETIME2 format.

RTC SETREG reg, value
RTC GETREG reg, var

The RTC SETREG and GETREG commands can be used to set or read the
contents of registers within the chip. 'reg' is the register's number, 'value' is the
number to store in the register and 'var' is a variable that will receive the
number read from the register. These commands are not necessary for normal



operation but they can be used to manipulate special features of the chip
(alarms, output signals, etc). They are also useful for storing temporary
information in the chip's battery backed RAM.
These chips are I2C devices and must be connected to the two I2C pins as
specified by OPTION SYSTEM I2C with appropriate pullup resistors.
Also see the command OPTION RTC AUTO ENABLE.
RUN
or
RUN [file$] [, cmdline$]

Run a program.
If file$ is not supplied then run the program currently held in program
memory.
If file$ is supplied then run the named file from the Flash or SD Card
filesystem; if file$ does not contain a '.BAS' extension then one will be
automatically added.
If cmdline$ is supplied then pass its value to the MM.CMDLINE$ constant of
the program when it runs.
If cmdline$ is not supplied then an empty string value is passed to
MM.CMDLINE$.
•
Both file$ and cmdline$ may be supplied as string expressions.
•
Use FLASH RUN n to run a program stored in a Flash Slot.
.Use
FLASH RUN n to run a program stored in a Flash Slot.

SAVE file$

Saves the program in the current working directory of the Flash Filesystem or
SD Card as ‘file$’. Example: SAVE “TEST.BAS”
If an extension is not specified “.BAS” will be added to the file name.
See also FLASH SAVE n

SAVE IMAGE file$ [,x, y, w,
h]
or
SAVE COMPRESSED
IMAGE file$ [,x, y, w, h]

Save the current image on the current LCD panel as a BMP file. The panel
must be capable of being read, for example, a ILI9341 based panel or a
VIRTUAL_M or VIRTUAL_ panel.
'file$' is the name of the file. If an extension is not specified “.BMP” will be
added to the file name. The image is saved as a true colour 24-bit image.
‘x’, ‘y’, ‘w’ and ‘h’ are optional and are the coordinates (x and y are the top
left coordinate) and dimensions (width and height) of the area to be saved. If
not specified the whole screen will be saved.
SAVE COMPRESSED IMAGE will work the same except that RLE
compression will be used to reduce the file size..

SEEK [#]fnbr, pos

Will position the read/write pointer in a file that has been opened on the Flash
Filesystem or SD Card for RANDOM access to the 'pos' byte.
The first byte in a file is numbered one so SEEK #5,1 will position the
read/write pointer to the start of the file.

SELECT CASE value
CASE testexp [[, testexp]
…]
<statements>
<statements>
CASE ELSE
<statements>
<statements>
END SELECT

Executes one of several groups of statements, depending on the value of an
expression. 'value' is the expression to be tested. It can be a number or string
variable or a complex expression.
'testexp' is the value that is to be compared against. It can be:
 A single expression (i.e. 34, "string" or PIN(4)*5) to which it may equal
 A range of values in the form of two single expressions separated by the
keyword "TO" (i.e. 5 TO 9 or "aa" TO "cc")
 A comparison starting with the keyword "IS" (which is optional). For
example: IS > 5, IS <= 10.
When a number of test expressions (separated by commas) are used the CASE
statement will be true if any one of these tests evaluates to true.
If 'value' cannot be matched with a 'testexp' it will be automatically matched to
the CASE ELSE. If CASE ELSE is not present the program will not execute
any <statements> and continue with the code following the END SELECT.
When a match is made the <statements> following the CASE statement will be



executed until END SELECT or another CASE is encountered when the
program will then continue with the code following the END SELECT.
An unlimited number of CASE statements can be used but there must be only
one CASE ELSE and that should be the last before the END SELECT.
Example:
SELECT CASE nbr%
CASE 4, 9, 22, 33 TO 88
statements
CASE IS < 4, IS > 88, 5 TO 8
statements
CASE ELSE
statements
END SELECT
Each SELECT CASE must have one and one only matching END SELECT
statement. Any number of SELECT…CASE statements can be nested inside
the CASE statements of other SELECT…CASE statements.
SETPIN pin, cfg [, option]

Will configure an external I/O pin. Refer to the section Using the I/O pins for
a general description of the PicoMite's input/output capabilities.
'pin' is the I/O pin to configure, ‘cfg’ is the mode that the pin is to be set to and
'option' is an optional parameter. 'cfg' is a keyword and can be any one of the
following:
OFF
Not configured or inactive
AIN
Analog input (i.e. measure the voltage on the input).
DIN
Digital input
If 'option' is omitted the input will be high impedance
If 'option' is the keyword "PULLUP" a simulated resistor will be
used to pull up the input pin to 3.3V If the keyword
"PULLDOWN" is used the pin will be pulled down to zero
volts. The pull up/down is a constant current of about 50µA.
FIN
Frequency input
'option' can be used to specify the gate time (the length of time
used to count the input cycles). It can be any number between
10 ms and 100000 ms. Note that the PIN() function will always
return the frequency correctly scaled in Hz regardless of the gate
time used. If 'option' is omitted the gate time will be 1 second.
The pins can be GP6, GP7, GP8 or GP9 (can be changed with
OPTION COUNT).
PIN
Period input
'option' can be used to specify the number of input cycles to
average the period measurement over. It can be any number
between 1 and 10000. Note that the PIN() function will always
return the average period of one cycle correctly scaled in ms
regardless of the number of cycles used for the average. If
'option' is omitted the period of just one cycle will be used.
The pins can be GP6, GP7, GP8 or GP9 (can be changed with
OPTION COUNT).
CIN


Counting input
‘option’ can be used to specify which edge triggers the count
and if any pullup or pulldown is enabled
1 specifies a rising edge with pulldown,
2 specifies a falling edge with pullup,
3 specifies that both a falling and rising edge will trigger a
count with no pullup or pulldown applied,
4 specifies both edges but with a pulldown and
5 specifies both edges but with a pullup applied.


If ‘option’ is omitted a rising edge will trigger the count and a
pulldown is enabled. The pins can be GP6, GP7, GP8 or GP9
(can be changed with OPTION COUNT).
DOUT

Digital output
'option' is not used in this mode.
The functions PIN() and PORT() can also be used to return the value on one or
more output pins. See the function PIN() for reading inputs and the statement
PIN()= for setting an output. See the command below if an interrupt is
configured.
SETPIN pin, cfg, target [,
option]

Will configure ‘pin’ to generate an interrupt according to ‘cfg’. Any I/O pin
capable of digital input can be configured to generate an interrupt with a
maximum of ten interrupts configured at any one time.
'cfg' is a keyword and can be any one of the following:
OFF
Not configured or inactive
INTH
Interrupt on low to high input
INTL
Interrupt on high to low input
INTB
Interrupt on both (i.e. any change to the input)
‘target' is a user defined subroutine which will be called when the event
happens. Return from the interrupt is via the END SUB or EXIT SUB
commands. 'option' can be the keywords "PULLUP" or "PULLDOWN" as
specified for a normal input pin (SETPIN pin DIN). If 'option' is omitted the
input will be high impedance.
This mode also configures the pin as a digital input so the value of the pin can
always be retrieved using the function PIN().
Refer to the section Using the I/O pins for a general description of the
PicoMite's input/output capabilities.

SETPIN GP25, DOUT |
HEARTBEAT

This version of SETPIN controls the on-board LED.
If it is configured as DOUT then it can be switched on and off under program
control.
If configured as HEARTBEAT then it will flash 1s on, 1s off continually while
powered. This is the default state and will be restored to this when the user
program stops running.

SETPIN p1[, p2 [, p3]], device

These commands are used for the pin allocation for special devices.
Pins must be chosen from the pin designation diagram and must be allocated
before the devices can be used. Note that the pins (e.g. rx, tx, etc) can be
declared in any order and that the pins can be referred to by using their pin
number (e.g. 1, 2) or GP number (e.g. GP0, GP1).

SETPIN rx, tx, COM1

Allocate the pins to be used for serial port COM1.
Valid pins are
RX:
GP1, GP13 or GP17
TX:
GP0, GP12, GP16 or GP28

SETPIN rx, tx, COM2

Allocate the pins to be used for serial port COM2.
Valid pins are
RX:
GP5, GP9 or GP21
TX:
GP4, GP8 or GP20

SETPIN rx, tx, clk, SPI

Allocate the pins to be used for SPI port SPI.
Valid pins are
RX:
GP0, GP4, GP16 or GP20
TX:
GP3, GP7 or GP19
CLK: GP2, GP6 or GP18

SETPIN rx, tx, clk, SPI2

Allocate the pins to be used for SPI port SPI2.
Valid pins are
RX:
GP8, GP12 or GP28
TX:
GP11, GP15 or GP27



CLK:

GP10, GP14 or GP26

SETPIN sda, scl, I2C

Allocate the pins to be used for the I2C port I2C.
Valid pins are
SDA: GP0, GP4, GP8, GP12, GP16, GP20 or GP28
SCL: GP1, GP5, GP9, GP13, GP17 or GP21

SETPIN sda, scl, I2C2

Allocate the pins to be used for the I2C port I2C2.
Valid pins are
SDA: GP2, GP6, GP10, GP14, GP18, GP22 or GP26
SCL: GP3, GP7, GP11, GP15, GP19 or GP27

SETPIN pin, PWM[nx]

Allocate pin to PWMnx
'n' is the PWM number (0 to 7) and 'x' and is the channel (A or B). n and x are
optional.
The setpin can be changed until the PWM command is issued. At that point the
pin becomes locked to PWM until PWMn,OFF is issued.

SETPIN pin, IR

Allocate pins for InfraRed (IR) communications (can be any pin).

SETPIN pin, PIOn

Reserve pin for use by a PIO0 or PIO1 (see Appendix F for PIO details).

SETTICK period, target [, nbr]

This will setup a periodic interrupt (or "tick").
Four tick timers are available ('nbr' = 1, 2, 3 or 4). 'nbr' is optional and if not
specified timer number 1 will be used.
The time between interrupts is ‘period’ milliseconds and ‘target' is the interrupt
subroutine which will be called when the timed event occurs.
The period can range from 1 to 2147483647 ms (about 24 days).
These interrupts can be disabled by setting ‘period’ to zero
(i.e. SETTICK 0, 0, 3 will disable tick timer number 3).

SETTICK PAUSE, target
[, nbr]
or
SETTICK RESUME, target
[, nbr]

Pause or resume the specified timer. When paused the interrupt is delayed but
the current count is maintained.

SORT array() [,indexarray()]
[,flags] [,startposition]
[,elementstosort]

This command takes an array of any type (integer, float or string) and sorts it
into ascending order in place.
It has an optional parameter ‘indexarray%()’. If used this must be an integer
array of the same size as the array to be sorted. After the sort this array will
contain the original index position of each element in the array being sorted
before it was sorted. Any data in the array will be overwritten. This allows
connected arrays to be sorted. See the section Sorting Data in the tutorial
Programming with the Colour Maximite 2 for an example.
The ‘flag’ parameter is optional and valid flag values are:
bit0: 0 (default if omitted) normal sort - 1 reverse sort
bit1: 0 (default) case dependent - 1 sort is case independent (strings only).
The optional ‘startposition’ defines which element in the array to start the sort.
Default is 0 (OPTION BASE 0) or 1 (OPTION BASE 1)
The optional ‘elementstosort’ defines how many elements in the array should
be sorted. The default is all elements after the startposition.
Any of the optional parameters may be omitted so, for example, to sort just the
first 50 elements of an array you could use:
SORT array(), , , ,50

SPI OPEN speed, mode, bits
or
SPI READ nbr, array()
or
SPI WRITE nbr, data1, data2,

Communications via an SPI channel. See Appendix D for the details.
'nbr' is the number of data items to send or receive
'data1', 'data2', etc can be float or integer and in the case of WRITE can be a
constant or expression.
If 'string$' is used 'nbr' characters will be sent.



data3, … etc
or
SPI WRITE nbr, string$
or
SPI WRITE nbr, array()
or
SPI CLOSE

'array' must be a single dimension float or integer array and 'nbr' elements will
be sent or received.

SPI2

The same set of commands as for SPI (above) but applying to the second SPI
channel.

STATIC variable [, variables]
See DIM for the full syntax.

Defines a list of variable names which are local to the subroutine or function.
These variables will retain their value between calls to the subroutine or
function (unlike variables created using the LOCAL command).
This command uses exactly the same syntax as DIM. The only difference is
that the length of the variable name created by STATIC and the length of the
subroutine or function name added together cannot exceed 31 characters.
Static variables can be initialised to a value. This initialisation will take effect
only on the first call to the subroutine (not on subsequent calls).

SUB xxx (arg1 [,arg2, …])
<statements>
<statements>
END SUB

Defines a callable subroutine. This is the same as adding a new command to
MMBasic while it is running your program.
'xxx' is the subroutine name and it must meet the specifications for naming a
variable.
'arg1', 'arg2', etc are the arguments or parameters to the subroutine. An array is
specified by using empty brackets. i.e. arg3(). The type of the argument can
be specified by using a type suffix (i.e. arg1$) or by specifying the type using
AS <type> (i.e. arg1 AS STRING).
Every definition must have one END SUB statement. When this is reached the
program will return to the next statement after the call to the subroutine. The
command EXIT SUB can be used for an early exit.
You use the subroutine by using its name and arguments in a program just as
you would a normal command. For example: MySub a1, a2
When the subroutine is called each argument in the caller is matched to the
argument in the subroutine definition. These arguments are available only
inside the subroutine. Subroutines can be called with a variable number of
arguments. Any omitted arguments in the subroutine's list will be set to zero
or a null string.
Arguments in the caller's list that are a variable and have the correct type will
be passed by reference to the subroutine. This means that any changes to the
corresponding argument in the subroutine will also be copied to the caller's
variable and therefore may be accessed after the subroutine has ended. Arrays
are passed by specifying the array name with empty brackets (e.g. arg()) and
are always passed by reference. Brackets around the argument list in both the
caller and the definition are optional.

SYNC time% [,period]
or
SYNC

The SYNC command allows the user to implement very precisely timed
repeated actions (1-2 microseconds accuracy).
To enable this the command is first called with the parameter time%. This sets
up a repeating clock for time% microseconds. The optional parameter ‘period’
modifies the time and can be “U” for microseconds, “M” for milliseconds or
“S” for seconds.
Once the clock is set up the programis synchronised to it using the SYNC
command without parameters. This waits for the clock period to expire. For
periods below 2milliseconds this is non-interruptible. Above two milliseconds
the program will respond to Ctrl-C but not any MMBasic interrupts.
Typical use is to set the clock outside of a loop and then at the top of the loop



call the SYNC command without parameters. This means the contents of the
loop will be executed exactly once for each clock period set.
For example, the following would drive a servo with the required precise 50Hz
timing:
SYNC 20, M
DO
SYNC
PULSE GP0,n
LOOP
TEMPR START pin [,
precision]

This command can be used to start a conversion running on a DS18B20
temperature sensor connected to 'pin'.
Normally the TEMPR() function alone is sufficient to make a temperature
measurement so usage of this command is optional.
This command will start the measurement on the temperature sensor. The
program can then attend to other duties while the measurement is running and
later use the TEMPR() function to get the reading. If the TEMPR() function is
used before the conversion time has completed the function will wait for the
remaining conversion time before returning the value.
Any number of these conversions (on different pins) can be started and be
running simultaneously.
'precision' is the resolution of the measurement and is optional. It is a number
between 0 and 3 meaning:
0 = 0.5ºC resolution, 100 ms conversion time.
1 = 0.25ºC resolution, 200 ms conversion time (this is the default).
2 = 0.125ºC resolution, 400 ms conversion time.
3 = 0.0625ºC resolution, 800 ms conversion time.

TEXT x, y, string$
[,alignment$] [, font] [, scale]
[, c] [, bc]

Displays a string on an attached LCD panel starting at 'x' and 'y'.
‘string$’ is the string to be displayed. Numeric data should be converted to a
string and formatted using the Str$() function.
' alignment$' is a string expression or string variable consisting of 0, 1 or 2
letters where the first letter is the horizontal alignment around 'x' and can be L,
C or R for LEFT, CENTER, RIGHT and the second letter is the vertical
alignment around 'y' and can be T, M or B for TOP, MIDDLE, BOTTOM.
The default alignment is left/top.
For example. “CM” will centre the text vertically and horizontally.
The 'alignment$' string can be a constant (e.g. “CM”) or it can be a string
variable. For backwards compatibility with earlier versions of MMBasic the
string can also be unquoted (e.g. CM).
In the PicoMite a third letter can be used in the alignment string to indicate the
rotation of the text. This can be 'N' for normal orientation, 'V' for vertical text
with each character under the previous running from top to bottom, 'I' the text
will be inverted (i.e. upside down), 'U' the text will be rotated counter
clockwise by 90º and 'D' the text will be rotated clockwise by 90º
'font' and 'scale' are optional and default to that set by the FONT command.
'c' is the drawing colour and 'bc' is the background colour. They are optional
and default to the current foreground and background colours.
See the section Graphics Commands and Functions for a definition of the
colours and graphics coordinates.



TIME$ = "HH:MM:SS"
or
TIME$ = "HH:MM"
or
TIME$ = "HH"

Sets the time of the internal clock. MM and SS are optional and will default to
zero if not specified. For example TIME$ = "14:30" will set the clock to 14:30
with zero seconds.
With OPTION RTC AUTO ENABLE the picomite starts with the TIME$
programmed in RTC.
Without OPTION RTC AUTO ENABLE the picomite starts with
TIME$="00:00:00"

TIMER = msec

Resets the timer to a number of milliseconds. Normally this is just used to
reset the timer to zero but you can set it to any positive number.
See the TIMER function for more details.

TRACE ON
or
TRACE OFF
or
TRACE LIST nn

TRACE ON/OFF will turn on/off the trace facility. This facility will print the
number of each line (counting from the beginning of the program) in square
brackets as the program is executed. This is useful in debugging programs.
TRACE LIST will list the last 'nn' lines executed in the format described
above. MMBasic is always logging the lines executed so this facility is always
available (i.e. it does not have to be turned on).

TRIANGLE X1, Y1, X2, Y2,
X3, Y3 [, C [, FILL]]

Draws a triangle on the LCD display panel with the corners at X1, Y1 and X2,
Y2 and X3, Y3. 'C' is the colour of the triangle and defaults to the current
foreground colour. 'FILL' is the fill colour and defaults to no fill (it can also be
set to -1 for no fill).
All parameters can be expressed as arrays and the software will plot the
number of triangles as determined by the dimensions of the smallest array
unless X1 = Y1 = X2 = Y2 = X3 = Y3 = -1 in which case processing will stop
at that point 'x1', 'y1', 'x2', 'y2', 'x3',and 'y3' must all be arrays or all be single
variables /constants otherwise an error will be generated 'c' and 'fill' can be
either arrays or single variables/constants.

TRIANGLE SAVE [#]n,
x1,y1,x2,y2,x3,y3

Saves a triangular area of the screen to buffer #n.

TRIANGLE RESTORE [#]n

Restores a saved triangular region of the screen and deletes the saved buffer.

UPDATE FIRMWARE

Causes the PicoMite to enter the firmware update mode (the same as applying
power while holding down the BOOTSEL button).
Loading the PicoMite firmware will erase the flash memory including the
current program, any programs saved in flash memory slots and all saved
variables. So make sure that you backup this data before you upgrade the
firmware. A firmware load will also reset all options to their defaults.

VAR SAVE var [, var]…
or
VAR RESTORE
or
VAR CLEAR

VAR SAVE will save one or more variables to non-volatile flash memory
where they can be restored later (normally after a power interruption).
'var' can be any number of numeric or string variables and/or arrays. Arrays
are specified by using empty brackets. For example: var()
VAR RESTORE will retrieve the previously saved variables and insert them
(and their values) into the variable table.
The VAR SAVE command can be used repeatedly. Variables that had been
previously saved will be updated with their new value and any new variables
(not previously saved) will be added to the saved list for later restoration.
VAR CLEAR will erase all saved variables. Also, the saved variables will be
automatically cleared by a firmware upgrade, by the NEW command or when
a new program is loaded via AUTOSAVE, XMODEM, etc.
This command is normally used to save calibration data, options, and other
data which does not change often but needs to be retained across a power
interruption. Normally the VAR RESTORE command is placed at the start of
the program so that previously saved variables are restored and immediately



available to the program when it starts. Notes:
 The storage space available to this command is 16KB.
 Using VAR RESTORE without a previous save will have no effect and
will not generate an error.
 If, when using RESTORE, a variable with the same name already exists its
value will be overwritten.
 Saved arrays must be declared (using DIM) before they can be restored.
 Be aware that string arrays can rapidly use up all the memory allocated to
this command. The LENGTH qualifier can be used when a string array is
declared to reduce the size of the array (see the DIM command). This is
not needed for ordinary string variables.
WATCHDOG timeout
or
WATCHDOG OFF
Or
WATCHDOG HW timeout
Or
WATCHDOG HW OFF

Starts the watchdog timer which will automatically restart the processor when
it has timed out. This can be used to recover from some event that disabled the
running program (such as an endless loop or a programming or other error that
halts a running program). This can be important in an unattended control
situation. The timeout can either be processed in the system timer interrupt or
as a true H/W watchdog.
'timeout' is the time in milliseconds (ms) before a restart is forced. This
command should be placed in strategic locations in the running BASIC
program to constantly reset the watchdog timer (to ‘timeout’) and therefore
prevent it from counting down to zero. If the H/W watchdog is used the timer
has a maximum of 8.3 seconds. No such limitation exists for the software
watchdog.
If the timer count does reach zero (perhaps because the BASIC program has
stopped running) the PicoMite will be automatically restarted and the
automatic variable MM.WATCHDOG will be set to true (i.e. 1) indicating that
an error occurred. On a normal startup MM.WATCHDOG will be set to false
(i.e. 0). Note that OPTION AUTORUN must be specified for the program to
restart.
WATCHDOG OFF can be used to disable the watchdog timer (this is the
default on a reset or power up). The timer is also turned off when the break
character (CTRL-C) is used on the console to interrupt a running program.

XMODEM SEND
or
XMODEM SEND file$
or
XMODEM RECEIVE
or
XMODEM RECEIVE file$
or
XMODEM CRUNCH

Transfers a BASIC program to or from a remote computer using the XModem
protocol. The transfer is done over the USB console connection.
XMODEM SEND will send the current program held in the PicoMite's
program memory to the remote device.
XMODEM RECEIVE will accept a program sent by the remote device and
save it into the PicoMite's the program memory overwriting the program
currently held there.
In both cases you can also specify 'file$' which will transfer the data to/from a
file on the Flash Filesystem or SD Card. If the file already exists it will be
overwritten when receiving a file.
Note that the data is buffered in RAM which limits the maximum transfer size.
This command also creates a backup of the program in flash memory which will
be automatically retrieved if the CPU is reset of the power is lost.
The CRUNCH option works like RECEIVE but will remove all comments,
blank lines and unnecessary spaces from the program before saving. This can
be used on large programs to allow them to fit into limited memory.
SEND, RECEIVE and CRUNCH can be abbreviated to S, R and C.
The XModem protocol requires a cooperating software program running on the
remote computer and connected to its serial port. It has been tested on Tera
Term running on Windows and it is recommended that this be used.
After running the XMODEM command in MMBasic select:
File -> Transfer -> XMODEM -> Receive/Send



from the Tera Term menu to start the transfer.
The transfer can take up to 15 seconds to start and if the XMODEM command
fails to establish communications it will return to the MMBasic prompt after
60 seconds and leave the program memory untouched.
Download Tera Term from http://ttssh2.sourceforge.jp/



Functions
Detailed Listing
Note that the functions related to communications functions (I2C, 1-Wire, and SPI) are not listed here but are
described in the appendices at the end of this document.
Square brackets indicate that the parameter or characters are optional.
ABS( number )

Returns the absolute value of the argument 'number' (i.e. any negative sign is
removed and a positive number is returned).

ACOS( number )

Returns the inverse cosine of the argument 'number' in radians.

ASC( string$ )

Returns the ASCII code (i.e. byte value) for the first letter in ‘string$’.

ASIN( number )

Returns the inverse sine value of the argument 'number' in radians.

ATN( number )

Returns the arctangent of the argument 'number' in radians.

ATAN2( y, x )

Returns the arc tangent of the two numbers x and y as an angle expressed in
radians.
It is similar to calculating the arc tangent of y / x, except that the signs of
both arguments are used to determine the quadrant of the result.

BIN$( number [, chars])

Returns a string giving the binary (base 2) value for the 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

BIN2STR$(type, value
[,BIG])

Returns a string containing the binary representation of 'value'.
'type' can be:
INT64
signed 64-bit integer converted to an 8 byte string
UINT64
unsigned 64-bit integer converted to an 8 byte string
INT32
signed 32-bit integer converted to a 4 byte string
UINT32
unsigned 32-bit integer converted to a 4 byte string
INT16
signed 16-bit integer converted to a 2 byte string
UINT16
unsigned 16-bit integer converted to a 2 byte string
INT8
signed 8-bit integer converted to a 1 byte string
UINT8
unsigned 8-bit integer converted to a 1 byte string
SINGLE
single precision floating point number converted to a 4 byte
string
DOUBLE double precision floating point number converted to a 8 byte
string
By default the string contains the number in little-endian format (i.e. the least
significant byte is the first one in the string). Setting the third parameter to
‘BIG’ will return the string in big-endian format (i.e. the most significant byte
is the first one in the string) In the case of the integer conversions, an error will
be generated if the ‘value’ cannot fit into the ‘type’ (e.g. an attempt to store the
value 400 in a INT8).
This function makes it easy to prepare data for efficient binary file I/O or for
preparing numbers for output to sensors and saving to flash memory.
See also the function STR2BIN



BOUND(array() [,dimension]

This returns the upper limit of the array for the dimension requested.
The dimension defaults to one if not specified. Specifying a dimension value of
0 will return the current value of OPTION BASE.
Unused dimensions will return a value of zero.
For example:
DIM myarray(44,45)
BOUND(myarray(),2) will return 45

CALL(userfunname$,
[,userfunparameters,..])

This is an efficient way of programmatically calling user defined functions.
(See also the CALL command). In many cases it can be used to eliminate
complex SELECT and IF THEN ELSEIF ENDIF clauses and is processed in a
much more efficient manner.
‘userfunname$’ can be any string or variable or function that resolves to the
name of a normal user function (not an in-built command).
‘userfunparameters’ are the same parameters that would be used to call the
function directly.
A typical use for this command could be writing any sort of emulator where
one of a large number of functions should be called depending on a some
variable. It also provides a method of passing a function name to another
subroutine or function as a variable.

CHOICE(condition,
ExpressionIfTrue,
ExpressionIfFalse)

This function allows you to do simple either/or selections more efficiently and
faster than using IF THEN ELSE ENDIF clauses.
The condition is anything that will resolve to nonzero (true) or zero (false).
The expressions are anything that you could normally assign to a variable or
use in a command and can be integers, floats or strings.
Examples:
PRINT CHOICE(1, "hello","bye") will print "Hello"
PRINT CHOICE (0, "hello","bye") will print "Bye"
a=1 : b=1 : PRINT CHOICE (a=b, 4, 5) will print 4

CHR$( number )

Returns a one-character string consisting of the character corresponding to the
ASCII code (i.e. byte value) indicated by argument 'number'.

CINT( number )

Round numbers with fractional portions up or down to the next whole number
or integer.
For example, 45.47 will round to 45
45.57 will round to 46
-34.45 will round to -34
-34.55 will round to -35
See also INT() and FIX().

COS( number )

Returns the cosine of the argument 'number' in radians.

CTRLVAL(#ref)

Returns the current value of an advanced control.
'#ref' is the control's reference. For controls like check boxes or switches it will
be the number one (true) indicating that the control has been selected by the
user or zero (false) if not. For controls that hold a number (e.g. a SPINBOX)
the value will be the number (normally a floating point number). For controls
that hold a string (e.g. TEXTBOX) the value will be a string.



CWD$

The current working directory on the Flash Filesystem or SD Card. Invalid for
exFAT format.
The format is: A:/dir1/dir2.

DATE$

Returns the current date based on MMBasic’s internal clock as a string in the
form "DD-MM-YYYY". For example, "28-07-2012".
The internal clock/calendar will keep track of the time and date including leap
years. To set the date use the command DATE$ =.

DATETIME$(n)

Returns the date and time corresponding to the epoch number n (number of
seconds that have elapsed since midnight GMT on January 1, 1970). The
format of the returned string is “dd-mm-yyyy hh:mm:ss”. Use the text NOW to
get the current datetime string, i.e. ? DATETIME$(NOW)

DAY$(date$)

Returns the day of the week for a given date as a string “Monday”, “Tuesday”
etc. The format for date$ is "DD-MM-YY", "DD-MM-YYYY", or "YYYYMM-DD". Use NOW to get the day for the current date, e.g. PRINT
DAY$(NOW)

DEG( radians )

Converts 'radians' to degrees.

DEVICE(WII funct)

Returns data from a Wii Classic controller.
'funct' is a 1 or 2 letter code indicating the information to return as follows:
LX returns the position of the analog left joystick x axis
LY returns the position of the analog left joystick y axis
RX returns the position of the analog right joystick x axis
RY returns the position of the analog right joystick y axis
L returns the position of the analog left button
R returns the position of the analog right button
B returns a bitmap of the state of all the buttons. A bit will be set to 1 if the
button is pressed.
T returns the ID code of the controller - should be hex &HA4200101
The button bitmap is as follows:
BIT 0: Button R
BIT 1: Button start
BIT 2: Button home
BIT 3: Button select
BIT 4: Button L
BIT 5: Button down cursor
BIT 6: Button right cursor
BIT 7: Button up cursor
BIT 8: Button left cursor
BIT 9: Button ZR
BIT 10: Button x
BIT 11: Button a
BIT 12: Button y
BIT 13: Button b
BIT 14: Button ZL



DIR$( fspec, type )
or
DIR$( fspec )
or
DIR$( )

Will search the default Flash Filesystem or SD Card for files and return the
names of entries found.
'fspec' is a file specification using wildcards the same as used by the FILES
command. E.g. "*.*" will return all entries, "*.TXT" will return text files.
Note that the wildcard *.* does not find files or folders without an extension.
'type' is the type of entry to return and can be one of:
VOL
Search for the volume label only
DIR
Search for directories only
FILE
Search for files only (the default if 'type' is not specified)
The function will return the first entry found. To retrieve subsequent entries
use the function with no arguments. i.e. DIR$( ). The return of an empty
string indicates that there are no more entries to retrieve.
This example will print all the files in a directory:
f$ = DIR$("*.*", FILE)
DO WHILE f$ <> ""
PRINT f$
f$ = DIR$()
LOOP
You must change to the required directory before invoking this command.

DISTANCE( trigger, echo )
or
DISTANCE( trig-echo )

Measure the distance to a target using the HC-SR04 ultrasonic distance sensor.
Four pin sensors have separate trigger and echo connections. 'trigger' is the I/O
pin connected to the "trig" input of the sensor and 'echo' is the pin connected to
the "echo" output of the sensor.
Three pin sensors have a combined trigger and echo connection and in that case
you only need to specify one I/O pin to interface to the sensor.
Note that any I/O pins used with the HC-SR04 should be 5V capable as the
HC-SR04 is a 5V device. The I/O pins are automatically configured by this
function and multiple sensors can be used on different I/O pins.
The value returned is the distance in centimetres to the target or -1 if no target
was detected or -2 if there was an error (i.e. sensor not connected).

EOF( [#]fnbr )

Will return true if the file previously opened on the Flash Filesystem or SD
Card for INPUT with the file number ‘#fnbr’ is positioned at the end of the file.
The # is optional. Also see the OPEN, INPUT and LINE INPUT commands
and the INPUT$ function.

EPOCH(DATETIME$)

Returns the epoch number (number of seconds that have elapsed since midnight
GMT on January 1, 1970) for the supplied DATETIME$ string.
The format for DATETIME$ is “dd-mm-yyyy hh:mm:ss”, “dd-mm-yy
hh:mm:ss”, or “yyyy-mm-dd hh:mm:ss”,. Use NOW to get the epoch number
for the current date and time, i.e. PRINT EPOCH(NOW)

EVAL( string$ )

Will evaluate 'string$' as if it is a BASIC expression and return the result.
'string$' can be a constant, a variable or a string expression. The expression can
use any operators, functions, variables, subroutines, etc that are known at the
time of execution. The returned value will be an integer, float or string
depending on the result of the evaluation.
For example: S$ = "COS(RAD(30)) * 100" : PRINT EVAL(S$)
Will display: 86.6025

EXP( number )

Returns the exponential value of 'number', i.e. e^x where x is 'number'.



FIELD$( string1, nbr, string2
[, string3] )

Returns a particular field in a string with the fields separated by delimiters.
'nbr' is the field to return (the first is nbr 1). 'string1' is the string to search and
'string2' is a string holding the delimiters (more than one can be used).
'string3' is optional and if specified will include characters that are used to
quote text in 'string1' (ie, quoted text will not be searched for a delimiter).
For example:
S$ = "foo, boo, zoo, doo"
r$ = FIELD$(s$, 2, ",")
will result in r$ = "boo". While:
s$ = "foo, 'boo, zoo', doo"
r$ = FIELD$(s$, 2, ",", "'")
will result in r$ = "boo, zoo".

FIX( number )

Truncate a number to a whole number by eliminating the decimal point and all
characters to the right of the decimal point.
For example 9.89 will return 9 and -2.11 will return -2.
The major difference between FIX() and INT() is that FIX() provides a true
integer function (i.e. does not return the next lower number for negative
numbers as INT() does). This behaviour is for Microsoft compatibility.
See also CINT() .

FORMAT$( nbr [, fmt$] )

Will return a string representing ‘nbr’ formatted according to the specifications
in the string ‘fmt$’.
The format specification starts with a % character and ends with a letter.
Anything outside of this construct is copied to the output as is.
The structure of a format specification is:
% [flags] [width] [.precision] type
Where ‘flags’ can be:
Left justify the value within a given field width
0
Use 0 for the pad character instead of space
+
Forces the + sign to be shown for positive numbers
space Causes a positive value to display a space for the sign. Negative
values still show the – sign
‘width’ is the minimum number of characters to output, less than this the
number will be padded, more than this the width will be expanded.
‘precision’ specifies the number of fraction digits to generate with an e, or f
type or the maximum number of significant digits to generate with a g type and
defaults to 4 digits. If specified, the precision must be preceded by a dot (.).
‘type’ can be one of:
g
Automatically format the number for the best presentation.
f
Format the number with the decimal point and following digits
e
Format the number in exponential format
If uppercase G or F is used the exponential output will use an uppercase E. If
the format specification is not specified “%g” is assumed.
Examples:
format$(45) will return 45
format$(45, “%g”) will return 45



GPS()

The GPS functions are used to return data from a serial communications
channel opened as GPS.
The function GPS(VALID) should be checked before any of these functions are
used to ensure that the returned value is valid.

GPS(ALTITUDE)

Returns current altitude (if sentence GGA is enabled).

GPS(DATE)

Returns the normal date string corrected for local time e.g. “12-01-2020”.

GPS(DOP)

Returns DOP (dilution of precision) value (if sentence GGA is enabled).

GPS(FIX)

Returns non zero (true) if the GPS has a fix on sufficient satellites and is
producing valid data.

GPS(GEOID)

Returns the geoid-ellipsoid separation (if sentence GGA is enabled).

GPS(LATITUDE)

Returns the latitude in degrees as a floating point number, values are negative
for South of equator

GPS(LONGITUDE)

Returns the longitude in degrees as a floating point number, values are
negative for West of the meridian.

GPS(SATELLITES)

Returns number of satellites in view (if sentence GGA is enabled).

GPS(SPEED)

Returns the ground speed in knots as a floating point number.

GPS(TIME)

Returns the normal time string corrected for local time e.g. “12:09:33”.

GPS(TRACK)

Returns the track over the ground (degrees true) as a floating point number.

GPS(VALID)

Returns: 0=invalid data, 1=valid data

HEX$( number [, chars])

Returns a string giving the hexadecimal (base 16) value for the 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

INKEY$

Checks the console input buffer and, if there is one or more characters waiting
in the queue, will remove the first character and return it as a single character in
a string.
If the input buffer is empty this function will immediately return with an empty
string (i.e. "").

INPUT$(nbr, [#]fnbr)

Will return a string composed of ‘nbr’ characters read from a serial
communications port opened as 'fnbr'. This function will return as many
characters as are waiting in the receive buffer up to ‘nbr’. If there are no
characters waiting it will immediately return with an empty string.
#0 can be used which refers to the console's input buffer.
The # is optional. Also see the OPEN command.



INSTR( [start-position,]
string-searched$, stringpattern$ [,size] )

Returns the position at which 'string-pattern$' occurs in 'string-searched$',
beginning at 'start-position'. If 'start-position' is not provided it will default to
1.
Both the position returned and 'start-position' use 1 for the first character, 2 for
the second, etc.
The function returns zero if 'string-pattern$' is not found.
If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.

INT( number )

Truncate an expression to the next whole number less than or equal to the
argument. For example 9.89 will return 9 and -2.11 will return -3.
This behaviour is for Microsoft compatibility, the FIX() function provides a
true integer function. See also CINT() .

LCASE$( string$ )

Returns ‘string$’ converted to lowercase characters.

LCOMPARE(array1%(),
array2%())

Compare the contents of two long string variables array1%() and array2%().
The returned is an integer and will be -1 if array1%() is less than array2%(). It
will be zero if they are equal in length and content and +1 if array1%() is
greater than array2%(). The comparison uses the ASCII character set and is
case sensitive.

LEFT$( string$, nbr )

Returns a substring of ‘string$’ with ‘nbr' of characters from the left
(beginning) of the string.

LEN( string$ )

Returns the number of characters in 'string$'.

LGETBYTE(array%(), n)

Returns the numerical value of the 'n'th byte in the LONGSTRING held in
'array%()'. This function respects the setting of OPTION BASE in determining
which byte to return.

LGETSTR$(array%(), start,
length)

Returns part of a long string stored in array%() as a normal MMBasic string.
The parameters start and length define the part of the string to be returned.

LINSTR(array%(), search$
[,start] [,size]))

Returns the position of a search string in a long string. The returned value is an
integer and will be zero if the substring cannot be found. array%() is the string
to be searched and must be a long string variable. Search$ is the substring to
look for and it must be a normal MMBasic string or expression (not a long
string). The search is case sensitive.
Normally the search will start at the first character in 'str' but the optional third
parameter allows the start position of the search to be specified.
If the optional parameter “size” is specified the “string-pattern” is treated as a
regular expression. See Appendix E for the details.

LLEN(array%())

Returns the length of a long string stored in array%()

LOC( [#]fnbr )

For a serial communications port opened as 'fnbr' this function will return the
number of bytes received and waiting in the receive buffer to be read.
#0 can be used which refers to the console's input buffer.
The # is optional.



LOF( [#]fnbr )

For a serial communications port opened as 'fnbr' this function will return the
space (in characters) remaining in the transmit buffer.
Note that when the buffer is full MMBasic will pause when adding a new
character and wait for some space to become available.
The # is optional.

LOG( number )

Returns the natural logarithm of the argument 'number'.

MATH

The math function performs many simple mathematical calculations that can be
programmed in Basic but there are speed advantages to coding looping
structures in C and there is the advantage that once debugged they are there for
everyone without re-inventing the wheel.

Simple functions
MATH(ATAN3 x,y)

Returns ATAN3 of x and y

MATH(COSH a)

Returns the hyperbolic cosine of a

MATH(LOG10 a)

Returns the base 10 logarithm of a

MATH(SINH a)

Returns the hyperbolic sine of a

MATH(TANH a)

Returns the hyperbolic tan of a

MATH(CRCn data [,length]
[,polynome] [,startmask]
[,endmask] [,reverseIn]
[,reverseOut]

Calculates the CRC to n bits (8, 12, 16, 32) of “data”. “data” can be an integer
or floating point array or a string variable. “Length” is optional and if not
specified the size of the array or string length is used. The defaults for
startmask, endmask reverseIn, and reversOut are all zero. reverseIn, and
reversOut are both Booleans and take the value 1 or 0. The defaults for
polynomes are CRC8=&H07, CRC12=&H80D, CRC16=&H1021,
crc32=&H04C11DB7
e.g. for crc16_CCITT use MATH(CRC16 array(), n,, &HFFFF)

MATH(RAND)

Returns a random number 0.0 <= n < 1.0 using the "Mersenne Twister
algorithm. If not seeded with MATH RANDOMIZE the first usage seeds with
the time in microseconds since boot

Simple Statistics
Returns the Pearson's chi-squared value of the two dimensional array a())
MATH(CHI a())
MATH(CHI_p a())

MATH(CROSSING array()
[,level] [,direction]

MATH(CORREL a(), a())
MATH(MAX a() [,index%])


Returns the associated probability in % of the Pearson's chi-squared value of
the two dimensional array a())

This returns the array index at which the values in the array pass the "level" in
the direction specified. level defaults to 0. Direction defaults to 1 ( valid values
are -1 or 1)
Returns the Pearson’s correlation coefficient between arrays a() and b()
Returns the maximum of all values in the a() array, a() can have any number of


dimensions. If the integer variable is specified then it will be updated with the
index of the maximum value in the array. This is only available on onedimensional arrays
MATH(MEAN a())

Returns the average of all values in the a() array, a() can have any number of
dimensions

MATH(MEDIAN a())

Returns the median of all values in the a() array, a() can have any number of
dimensions

MATH(MIN a(), [index%])

Returns the minimum of all values in the a() array, a() can have any number of
dimensions. If the integer variable is specified then it will be updated with the
index of the maximum value in the array. This is only available on onedimensional arrays.

MATH(SD a())

Returns the standard deviation of all values in the a() array, a() can have any
number of dimensions

MATH(SUM a())

Returns the sum of all values in the a() array, a() can have any number of
dimensions

Vector Arithmetic
MATH(MAGNITUDE v())

Returns the magnitude of the vector v(). The vector can have any number of
elements

MATH(DOTPRODUCT
v1(), v2())

Returns the dot product of two vectors v1() and v2(). The vectors can have any
number of elements but must have the same cardinality

Matrix Arithmetic
MATH(M_DETERMINANT
array!())

Returns the determinant of the array. The array must be square.

Creation
complex% = MATH(C_CPLX r!, i!)
complex% = MATH(C_POLAR radius!, angle!)
Floating returns
real! = MATH(C_REAL complex%)
imag! = MATH(C_IMAG complex%)
arg! = MATH(C_ARG complex%)
mod! = MATH(C_MOD complex%)
phase! = MATH(C_PHASE complex%)
Unary functions
complex1% = MATH(C_CONJ complex2%)
complex1% = MATH(C_SIN complex2%)
complex1% = MATH(C_COS complex2%)
complex1% = MATH(C_TAN complex2%)


MMBasic supports a full range of functions to
allow the manipulation of complex numbers. In
this implementation complex numbers have a 32bit real and 32-bit imaginary part and to make
this work in MMBasic, it uses integers (64-bit) to
hold these.


complex1% = MATH(C_ASIN complex2%)
complex1% = MATH(C_ACOS complex2%)
complex1% = MATH(C_ATAN complex2%)
complex1% = MATH(C_SINH complex2%)
complex1% = MATH(C_COSH complex2%)
complex1% = MATH(C_TANH complex2%)
complex1% = MATH(C_ASINH complex2%)
complex1% = MATH(C_ACOSH complex2%)
complex1% = MATH(C_ATANH complex2%)
complex1% = MATH(C_PROJ complex2%)
Basic Arithmetic
complex1% = MATH(C_ADD complex2%,complex3%)
complex1% = MATH(C_SUB complex2%,complex3%)
complex1% = MATH(C_MUL complex2%,complex3%)
complex1% = MATH(C_DIV complex2%,complex3%)
complex1% = MATH(C_POW complex2%,complex3%)
complex1% = MATH(C_AND complex2%,complex3%)
complex1% = MATH(C_OR complex2%,complex3%)
complex1% = MATH(C_XOR complex2%,complex3%)
MAX( arg1 [, arg2 [, …]] )
or
MIN( arg1 [, arg2 [, …]] )

Returns the maximum or minimum number in the argument list.
Note that the comparison is a floating point comparison (integer arguments are
converted to floats) and a float is returned.

MID$( string$, start )
or
MID$( string$, start, nbr )

Returns a substring of ‘string$’ beginning at ‘start’ and continuing for ‘nbr’
characters. The first character in the string is number 1.
If ‘nbr’ is omitted the returned string will extend to the end of ‘string$’

MSGBOX (msg$, b1$ [,b2$
… b4$])

This function will display a message box on the screen with one to four touch
sensitive buttons. All other controls will be disabled until the user touches one
of the buttons. The message box will then be erased, the previous controls will
be restored and the function will return the number of the button touched (the
first button is number one)
'msg$' is the message to display. This can contain one or more tilde characters
(~) which indicate a line break. Up to 10 lines can be displayed inside the box.
'b1$' is the caption for the first button, 'b2$' is the caption for the second button,
etc. At least one button must be specified and four is the maximum. Any
buttons not included in the argument list will not be displayed.

OCT$( number [, chars])

Returns a string giving the octal (base 8) representation of 'number'.
'chars' is optional and specifies the number of characters in the string with zero
as the leading padding character(s).

PEEK(BYTE addr%)
or
PEEK(SHORT addr%)
or
PEEK(WORD addr%)
or
PEEK(INTEGER addr%)
or
PEEK(FLOAT addr%)

Will return a byte or a word within the PIC32 virtual memory space.
BYTE will return the byte (8-bits) located at 'addr%'
SHORT will return the short integer (16-bits) located at 'addr%'


WORD will return the word (32-bits) located at 'addr%'
INTEGER will return the integer (64-bits) located at 'addr%'
FLOAT will return the floating point number (32-bits) located at 'addr%'


or
PEEK(VARADDR var)
or
PEEK(CFUNADDR cfun)
or
PEEK(VAR var, ±offset)
or
PEEK( VARTBL, ±offset)
or
PEEK( PROGMEM, ±offset)

VARADDR will return the address (32-bits) of the variable 'var' in memory.
An array is specified as var().
CFUNADDR will return the address (32-bits) of the CFunction 'cfun' in
memory. This address can be passed to another CFunction which can then call
it to perform some common process.
VAR, will return a byte in the memory allocated to 'var'. An array is specified
as var().
VARTBL, will return a byte in the memory allocated to the variable table
maintained by MMBasic. Note that there is a comma after the keyword
VARTBL.
PROGMEM, will return a byte in the memory allocated to the program. Note
that there is a comma after the keyword PROGMEM.
Note that 'addr%' should be an integer.

PEEK(WP,n%)

peek(bp n%) ' returns the byte at address n% and increments n% to point to the
next byte
peek(sp n%) ' returns the short at address n% and increments n% to point to the
next short
peek(wp n%) ' returns the word at address n% and increments n% to point to
the next word

PI

Returns the value of pi.

PIN( pin )

Returns the value on the external I/O ‘pin’. Zero means digital low, 1 means
digital high and for analogue inputs it will return the measured voltage as a
floating point number.
Frequency inputs will return the frequency in Hz. A period input will return
the period in milliseconds while a count input will return the count since reset
(counting is done on the positive rising edge). The count input can be reset to
zero by resetting the pin to counting input (even if it is already so configured).
This function will also return the state of a pin configured as an output or a PIO
pin.
Also see the SETPIN and PIN() = commands. Refer to the section Using the
I/O pins for a general description of the PicoMite's input/output capabilities.

PIN( TEMP )

Returns the temperature of the RP2040 chip (see the RP2040 data sheet for the
details)

PIO(DMA RX POINTER)
PIO(DMA TX POINTER)

Returns the current data item being written or read by the PIO

PIO (SHIFTCTRL
push_threshold
[,pull_threshold] [,autopush]
[,autopull] [,in_shiftdir]
[,out_shiftdir] [,fjoin_rx]
[,fjoin_tx])

helper function to calculate the value of shiftctrl for the INIT MACHINE
command

PEEK(BP, n%)
PEEK(SP,n%)



PIO (PINCTRL
no_side_set_pins
[,no_set_pins] [,no_out_pins]
[,IN base]
[,side_set_base] [,set_base][,
out_base])

helper function to calculate the value of pinctrl for the INIT MACHINE
command. Note: The pin parameters must be formatted as GPn.

PIO (EXECCTRL jmp_pin
,wrap_target, wrap
[,side_pindir] [,side_en])

helper function to calculate the value of execctrl for the INIT MACHINE
command

PIO (FDEBUG pio)

returns the value of the FSDEBUG register for the pio specified

PIO (FSTAT pio)

returns the value of the FSTAT register for the pio specified

PIO (FLEVEL pio)

returns the value of the FLEVEL register for the pio specified
PIO(FLEVEL pio)

PIO(FLEVEL pio ,sm, DIR)

dir can be RX or TX. Returns the level of the specific fifo

PIO(.WRAP)
PIO(.WRAP TARGET)

returns the location of the .wrap directive in PIO ASSEMBLE
returns the location of the .wrap target directive in PIO ASSEMBLE.
These can be used in the PIO(EXECCTRL function as follows:
PIO (EXECCTRL jmp_pin PIO(.WRAP TARGET), PIO(.WRAP)
[,side_pindir] [,side_en])

PORT(start, nbr [,start,
nbr]…)

Returns the value of a number of I/O pins in one operation.
'start' is an I/O pin number and its value will be returned as bit 0. 'start'+1 will be
returned as bit 1, 'start'+2 will be returned as bit 2, and so on for 'nbr' number of
bits. I/O pins used must be numbered consecutively and any I/O pin that is
invalid or not configured as an input will cause an error. The start/nbr pair can be
repeated up to 25 times if additional groups of input pins need to be added.
This function will also return the state of a pin configured as an output. It can
be used to conveniently communicate with parallel devices like memory chips.
Any number of I/O pins (and therefore bits) can be used from 1 to the number
of I/O pins on the chip.
See the PORT command to simultaneously output to a number of pins.

PIXEL( x, y)

Returns the colour of a pixel on an LCD display. 'x' is the horizontal
coordinate and 'y' is the vertical coordinate of the pixel. The display must use
one of the SSD1963, ILI9341, ILI9488, or ST7789_320 controllers.

PULSIN( pin, polarity )
or
PULSIN( pin, polarity, t1 )
or
PULSIN( pin, polarity, t1, t2
)

Measures the width of an input pulse from 1µs to 1 second with 0.1µs
resolution.
'pin' is the I/O pin to use for the measurement, it must be previously configured
as a digital input. 'polarity' is the type of pulse to measure, if zero the function
will return the width of the next negative pulse, if non zero it will measure the
next positive pulse.
't1' is the timeout applied while waiting for the pulse to arrive, 't2' is the timeout
used while measuring the pulse. Both are in microseconds (µs) and are
optional. If 't2' is omitted the value of 't1' will be used for both timeouts. If
both 't1' and 't2' are omitted then the timeouts will be set at 100000 (i.e.



100ms).
This function returns the width of the pulse in microseconds (µs) or -1 if a
timeout has occurred. The measurement is accurate to ±0.5% and ±0.5µsNote
that this function will cause the running program to pause while the
measurement is made and interrupts will be ignored during this period.
RAD( degrees )

Converts 'degrees' to radians.

RGB(red, green, blue)
or
RGB(shortcut)

Generates an RGB true colour value.
'red', 'blue' and 'green' represent the intensity of each colour. A value of zero
represents black and 255 represents full intensity.
'shortcut' allows common colours to be specified by naming them. The colours
that can be named are white, black, blue, green, cyan, red, magenta, yellow,
brown, white, orange, pink, gold, salmon, beige, lightgrey and grey (or USA
spelling gray/lightgray). For example, RGB(red) or RGB(cyan).
Note that the value returned is an integer and, if it is to be saved, the variable
should be declared as an integer to retain the accuracy of the number.

RIGHT$( string$, number-ofchars )

Returns a substring of ‘string$’ with ‘number-of-chars’ from the right (end) of
the string.

RND( number )
or
RND

Returns a pseudo-random number in the range of 0 to 0.999999. The 'number'
value is ignored if supplied. The RANDOMIZE command reseeds the random
number generator.

SGN( number )

Returns the sign of the argument 'number', +1 for positive numbers, 0 for 0, and
-1 for negative numbers.

SIN( number )

Returns the sine of the argument 'number' in radians.

SPACE$( number )

Returns a string of blank spaces 'number' characters long.

SPI ( data )
or
SPI2 ( data )

Send and receive data using an SPI channel.
A single SPI transaction will send data while simultaneously receiving data
from the slave. ‘data’ is the data to send and the function will return the data
received during the transaction. ‘data’ can be an integer or a floating point
variable or a constant.

SQR( number )

Returns the square root of the argument 'number'.

STR$( number )
or
STR$( number, m )
or
STR$( number, m, n )
or
STR$( number, m, n, c$ )

Returns a string in the decimal (base 10) representation of 'number'.
If 'm' is specified sufficient spaces will be added to the start of the number to
ensure that the number of characters before the decimal point (including the
negative or positive sign) will be at least 'm' characters. If 'm' is zero or the
number has more than 'm' significant digits no padding spaces will be added.
If 'm' is negative, positive numbers will be prefixed with the plus symbol and
negative numbers with the negative symbol. If 'm' is positive then only the
negative symbol will be used.
'n' is the number of digits required to follow the decimal place. If it is zero the
string will be returned without the decimal point. If it is negative the output
will always use the exponential format with 'n' digits resolution. If 'n' is not
specified the number of decimal places and output format will vary



automatically according to the number.
'c$' is a string and if specified the first character of this string will be used as
the padding character instead of a space (see the 'm' argument).
Examples:
STR$(123.456)
will return "123.456"
STR$(-123.456)
will return "-123.456"
STR$(123.456, 1)
will return "123.456"
STR$(123.456, -1)
will return "+123.456"
STR$(123.456, 6)
will return "
123.456"
STR$(123.456, -6)
will return " +123.456"
STR$(-123.456, 6)
will return " -123.456"
STR$(-123.456, 6, 5) will return " -123.45600"
STR$(-123.456, 6, -5) will return "
-1.23456e+02"
STR$(53, 6)
will return "
53"
STR$(53, 6, 2)
will return "
53.00"
STR$(53, 6, 2, "*")
will return "****53.00"
STR2BIN(type, string$
[,BIG])

Returns a number equal to the binary representation in ‘string$’.
‘type’ can be:
INT64 converts 8 byte string representing a signed 64-bit integer to an integer
UINT64 converts 8 byte string representing an unsigned 64-bit integer to an
integer
INT32 converts 4 byte string representing a signed 32-bit integer to an integer
UINT32 converts 4 byte string representing an unsigned 32-bit integer to an
integer
INT16 converts 2 byte string representing a signed 16-bit integer to an integer
UINT16 converts 2 byte string representing an unsigned 16-bit integer to an
integer
INT8 converts 1 byte string representing a signed 8-bit integer to an integer
UINT8 converts 1 byte string representing an unsigned 8-bit integer to an
integer
SINGLE converts 4 byte string representing single precision float to a float
DOUBLE converts 8 byte string representing single precision float to a float
By default the string must contain the number in little-endian format (i.e. the
least significant byte is the first one in the string). Setting the third parameter
to ‘BIG’ will interpret the string in big-endian format (i.e. the most
significant byte is the first one in the string).
This function makes it easy to read data from binary data files, interpret
numbers from sensors or efficiently read binary data from flash memory
chips.
An error will be generated if the string is the incorrect length for the
conversion requested
See also the function BIN2STR$

STRING$( nbr, ascii )
or
STRING$( nbr, string$ )

Returns a string 'nbr' bytes long consisting of either the first character of string$
or the character representing the ASCII value 'ascii' which is an integer or float
number in the range of 0 to 255.

TAB( number )

Outputs spaces until the column indicated by 'number' has been reached on the
console output.



TAN( number )

Returns the tangent of the argument 'number' in radians.

TEMPR( pin )

Return the temperature measured by a DS18B20 temperature sensor connected
to 'pin' (which does not have to be configured).
The returned value is degrees C with a default resolution of 0.25ºC. If there is
an error during the measurement the returned value will be 1000.
The time required for the overall measurement is 200ms and interrupts will be
ignored during this period. Alternatively the TEMPR START command can be
used to start the measurement and your program can do other things while the
conversion is progressing. When this function is called the value will then be
returned instantly assuming the conversion period has expired. If it has not,
this function will wait out the remainder of the conversion time before
returning the value.
The DS18B20 can be powered separately by a 3V to 5V supply or it can
operate on parasitic power from the PicoMite.
See the section Special Hardware Devices for more details.

TIME$

Returns the current time based on MMBasic's internal clock as a string in the
form "HH:MM:SS" in 24 hour notation. For example, "14:30:00".
To set the current time use the command TIME$ = .

TIMER

Returns the elapsed time in milliseconds (e.g. 1/1000 of a second) since reset.
The timer is reset to zero on power up or a CPU restart and you can also reset it
by using TIMER as a command. If not specifically reset it will continue to
count up forever (it is a 64 bit number and therefore will only roll over to zero
after 200 million years).

TOUCH(X)
or
TOUCH(Y)

Will return the X or Y coordinate of the location currently touched on an LCD
panel.
If the screen is not being touched the function will return -1.

UCASE$( string$ )

Returns ‘string$’ converted to uppercase characters.

VAL( string$ )

Returns the numerical value of the ‘string$’. If 'string$' is an invalid number
the function will return zero.
This function will recognise the &H prefix for a hexadecimal number, &O for
octal and &B for binary.



Obsolete Commands and Functions
Detailed Listing
These commands and functions are mostly included to assist in converting programs written for Microsoft
BASIC. For new programs the corresponding modern commands in MMBasic should be used.
Note that these commands may be removed in the future to recover memory for other features.
BITBANG

Replaced by the command DEVICE. For compatibility BITBANG can still be
used in programs and will be automatically converted to DEVICE

GOSUB target

Initiates a subroutine call to the target, which can be a line number or a label.
The subroutine must end with RETURN.
New programs should use defined subroutines (i.e. SUB…END SUB).

IF condition THEN linenbr

For Microsoft compatibility a GOTO is assumed if the THEN statement is
followed by a number. A label is invalid in this construct.
New programs should use: IF condition THEN GOTO linenbr | label

IRETURN

Returns from an interrupt when the interrupt destination was a line number or a
label.
New programs should use a user defined subroutine as an interrupt destination.
In that case END SUB or EXIT SUB will cause a return from the interrupt.

ON nbr GOTO | GOSUB
target[,target, target,..]

ON either branches (GOTO) or calls a subroutine (GOSUB) based on the
rounded value of 'nbr'; if it is 1, the first target is called, if 2, the second target
is called, etc. Target can be a line number or a label.
New programs should use SELECT CASE.

POS

For the console, returns the current cursor position in the line in characters.

PAGE

Replaced with “GUI PAGE”

RETURN

RETURN concludes a subroutine called by GOSUB and returns to the
statement after the GOSUB.



Appendix A – Serial Communications
Serial Communications
Two serial interfaces are available for asynchronous serial communications. They are labelled COM1: and
COM2:.

I/O Pins
Before a serial interface can be used the I/O pins must be defined using the following command for the first
channel (referred as COM1):
SETPIN rx, tx, COM1
Valid pins are
RX:
GP1, GP13 or GP17
TX:
GP0, GP12, GP16 or GP28
And the following command for the second channel (referred to as COM2):
SETPIN rx, tx, COM2
Valid pins are
RX:
GP5, GP9 or GP21
TX:
GP4, GP8 or GP20
TX is data from the PicoMite and RX is data to it.
The signal polarity is standard for devices running at TTL voltages. Idle is voltage high, the start bit is voltage
low, data uses a high voltage for logic 1 and the stop bit is voltage high. These signal levels allow you to
directly connect to devices like GPS modules (which generally use TTL voltage levels).

After being opened the serial port will have an associated file number and you can use any commands that operate
with a file number to read and write to/from it. A serial port can be closed using the CLOSE command.
The following is an example:
SETPIN GP13, GP16, COM1
' assign the I/O pins for the first serial port
OPEN "COM1:4800" AS #5
' open the first serial port with a speed of 4800 baud
PRINT #5, "Hello"
' send the string "Hello" out of the serial port
dat$ = INPUT$(20, #5)
' get up to 20 characters from the serial port
CLOSE #5
' close the serial port

The OPEN Command
A serial port is opened using the command:
OPEN comspec$ AS #fnbr
‘fnbr’ is the file number to be used. It must be in the range of 1 to 10. The # is optional.
‘comspec$’ is the communication specification and is a string (it can be a string variable) specifying the serial
port to be opened and optional parameters. The default is 9600 baud, 8 data bits, no parity and one stop bit.
It has the form "COMn: baud, buf, int, int-trigger, EVEN, ODD, S2, 7BIT"
where:
 ‘n’ is the serial port number for either COM1: or COM2:.
 ‘baud’ is the baud rate. This can be any number from 1200 to 921600. Default is 9600.
 ‘buf’ is the receive buffer size in bytes (default size is 256). The transmit buffer is fixed at 256 bytes.
 ‘int’ is interrupt subroutine to be called when the serial port has received some data.
 ‘int-trigger’ is the number of characters received which will trigger an interrupt.
All parameters except the serial port name (COMn:) are optional. If any one parameter is left out then all the
following parameters must also be left out and the defaults will be used.
Five options can be added to the end of 'comspec$'. These are:
 'S2' specifies that two stop bits will be sent following each character transmitted.
 EVEN specifies that an even parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set.
 ODD specifies that an odd parity bit will be applied, this will result in a 9-bit transfer unless 7BIT is set
 7BIT specifies that there a 7bits of data. This is normally used with EVEN or ODD
 INV specifies that the output signals will be inverted and input assumed to be inverted


Examples
Opening a serial port using all the defaults:
OPEN "COM1:" AS #2

Opening a serial port specifying only the baud rate (4800 bits per second):
OPEN "COM1:4800" AS #1

Opening a serial port specifying the baud rate (9600 bits per second) and receive buffer size (1KB):
OPEN "COM2:9600, 1024" AS #8

The same as above but with two stop bits enabled:
OPEN "COM2:9600, 1024, S2" AS #8

An example specifying everything including an interrupt, an interrupt level, and two stop bits:
OPEN "COM2:19200, 1024, ComIntLabel, 256, S2" AS #5

Reading and Writing
Once a serial port has been opened you can use any command or function that uses a file number to read from
and write to the port. Data received by the serial port will be automatically buffered in memory by MMBasic
until it is read by the program and the INPUT$() function is the most convenient way of doing that. When
using the INPUT$() function the number of characters specified will be the maximum number of characters
returned but it could be less if there are less characters in the receive buffer. In fact the INPUT$() function will
immediately return an empty string if there are no characters available in the receive buffer.
The LOC() function is also handy; it will return the number of characters waiting in the receive buffer (i.e. the
maximum number characters that can be retrieved by the INPUT$() function). Note that if the receive buffer
overflows with incoming data the serial port will automatically discard the oldest data to make room for the
new data.
The PRINT command is used for outputting to a serial port and any data to be sent will be held in a memory
buffer while the serial port is sending it. This means that MMBasic will continue with executing the commands
after the PRINT command while the data is being transmitted. The one exception is if the output buffer is full
and in that case MMBasic will pause and wait until there is sufficient space before continuing. The LOF()
function will return the amount of space left in the transmit buffer and you can use this to avoid stalling the
program while waiting for space in the buffer to become available.
If you want to be sure that all the data has been sent (perhaps because you want to read the response from the
remote device) you should wait until the LOF() function returns 256 (the transmit buffer size) indicating that
there is nothing left to be sent.
Serial ports can be closed with the CLOSE command. This will wait for the transmit buffer to be emptied then
free up the memory used by the buffers and cancel the interrupt (if set). A serial port is also automatically
closed when commands such as RUN and NEW are issued.

Interrupts
The interrupt subroutine (if specified) will operate the same as a general interrupt on an external I/O pin (see
the section Using the I/O pins for a description).
When using interrupts you need to be aware that it will take some time for MMBasic to respond to the interrupt
and more characters could have arrived in the meantime, especially at high baud rates. For example, if you
have specified the interrupt level as 200 characters and a buffer of 256 characters then quite easily the buffer
will have overflowed by the time the interrupt subroutine can read the data. In this case the buffer should be
increased to 512 characters or more.



Appendix B – I2C Communications
I2C Communications
There are two I2C channels. They can operate in master or slave mode.

I/O Pins
Before the I2C interface can be used the I/O pins must be defined using the following command for the first
channel (referred as I2C):
SETPIN sda, scl, I2C
Valid pins are
SDA: GP0, GP4, GP8, GP12, GP16, GP20 or GP28
SCL: GP1, GP5, GP9, GP13, GP17 or GP21
And the following command for the second channel (referred to as I2C2):
SETPIN sda, scl, I2C2
Valid pins are
SDA: GP2, GP6, GP10, GP14, GP18, GP22 or GP26
SCL: GP3, GP7, GP11, GP15, GP19 or GP27
2
When running the I C bus at above 100 kHz the cabling between the devices becomes important. Ideally the
cables should be as short as possible (to reduce capacitance) and the data and clock lines should not run next to
each other but have a ground wire between them (to reduce crosstalk).
If the data line is not stable when the clock is high, or the clock line is jittery, the I2C peripherals can get
"confused" and end up locking the bus (normally by holding the clock line low). If you do not need the higher
speeds then operating at 100 kHz is the safest choice.

I2C Master Commands
There are four commands that can be used for the first channel (I2C) in master mode as follows.
The commands for the second channel (I2C2) are identical except that the command is I2C2
I2C OPEN speed,
timeout

Enables the I2C module in master mode. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
‘speed’ is the clock speed (in KHz) to use and must be either 100 or 400.
‘timeout’ is a value in milliseconds after which the master send and receive
commands will be interrupted if they have not completed. The minimum value is
100. A value of zero will disable the timeout (though this is not recommended).

I2C WRITE addr,
option, sendlen,
senddata [,sendata ..]

Send data to the I2C slave device. The I2C command refers to channel 1 while the
command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘sendlen’ is the number of bytes to send.
‘senddata’ is the data to be sent - this can be specified in various ways (all data
sent will be sent as bytes with a value between 0 and 255):
 The data can be supplied as individual bytes on the command line.
Example: I2C WRITE &H6F, 0, 3, &H23, &H43, &H25
 The data can be in a one dimensional array specified with empty brackets (i.e.
no dimensions). ‘sendlen’ bytes of the array will be sent starting with the first
element. Example: I2C WRITE &H6F, 0, 3, ARRAY()
 The data can be a string variable (not a constant).
Example: I2C WRITE &H6F, 0, 3, STRING$



I2C READ addr,
option, rcvlen, rcvbuf

Get data from the I2C slave device. The I2C command refers to channel 1 while
the command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave’s I2C address.
‘option’ can be 0 for normal operation or 1 to keep control of the bus after the
command (a stop condition will not be sent at the completion of the command)
‘rcvlen’ is the number of bytes to receive.
‘rcvbuf’ is the variable or array used to save the received data - this can be:
 A string variable. Bytes will be stored as sequential characters in the string.
 A one dimensional array of numbers specified with empty brackets. Received
bytes will be stored in sequential elements of the array starting with the first.
Example: I2C READ &H6F, 0, 3, ARRAY()
 A normal numeric variable (in this case rcvlen must be 1).

I2C CLOSE

Disables the master I2C module and returns the I/O pins to a "not configured" state.
This command will also send a stop if the bus is still held.

I2C Slave Commands
I2C SLAVE OPEN
addr, send_int,
rcv_int

Enables the I2C module in slave mode. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
‘addr’ is the slave I2C address.
‘send_int’ is the subroutine to be invoked when the module has detected that the
master is expecting data.
‘rcv_int is the subroutine to be called when the module has received data from the
master. Note that this is triggered on the first byte received so your program might
need to wait until all the data is received.

I2C SLAVE WRITE
sendlen, senddata
[,sendata ..]

Send the data to the I2C master. The I2C command refers to channel 1 while the
command I2C2 refers to channel 2 using the same syntax.
This command should be used in the send interrupt (ie in the 'send_int' subroutine
when the master has requested data). Alternatively, a flag can be set in the
interrupt subroutine and the command invoked from the main program loop when
the flag is set.
‘sendlen is the number of bytes to send.
‘senddata’ is the data to be sent. This can be specified in various ways, see the I2C
WRITE commands for details.

I2C SLAVE READ
rcvlen, rcvbuf, rcvd

Receive data from the I2C master device. The I2C command refers to channel 1
while the command I2C2 refers to channel 2 using the same syntax.
This command should be used in the receive interrupt (ie in the 'rcv_int' subroutine
when the master has sent some data). Alternatively a flag can be set in the receive
interrupt subroutine and the command invoked from the main program loop when
the flag is set.
‘rcvlen’ is the maximum number of bytes to receive.
‘rcvbuf’ is the variable to receive the data. This can be specified in various ways,
see the I2C READ commands for details.
‘rcvd’ is a variable that, at the completion of the command, will contain the actual
number of bytes received (which might differ from ‘rcvlen’).

I2C SLAVE CLOSE

Disables the slave I2C module and returns the external I/O pins to a "not
configured" state. They can then be configured using SETPIN.



Errors
Following an I2C write or read the automatic variable MM.I2C will be set to indicate the result as follows:
0 = The command completed without error.
1 = Received a NACK response
2 = Command timed out

7-Bit Addressing
The standard addresses used in these commands are 7-bit addresses (without the read/write bit). MMBasic will
add the read/write bit and manipulate it accordingly during transfers.
Some vendors provide 8-bit addresses which include the read/write bit. You can determine if this is the case
because they will provide one address for writing to the slave device and another for reading from the slave. In
these situations you should only use the top seven bits of the address. For example: If the read address is 9B
(hex) and the write address is 9A (hex) then using only the top seven bits will give you an address of 4D (hex).
Another indicator that a vendor is using 8-bit addresses instead of 7-bit addresses is to check the address range.
All 7-bit addresses should be in the range of 08 to 77 (hex). If your slave address is greater than this range then
probably your vendor has provided an 8-bit address.

Examples
As an example of a simple communications where the PicoMite is the master, the following program
will read and display the current time (hours and minutes) maintained by a PCF8563 real time clock
chip connected to the second I2C channel:
DIM AS INTEGER RData(2)
' this will hold received data
SETPIN GP6, GP5, I2C2
' assign the I/O pins for I2C2
I2C2 OPEN 100, 1000
' open the I2C channel
I2C2 WRITE &H51, 0, 1, 3
' set the first register to 3
I2C2 READ &H51, 0, 2, RData()
' read two registers
I2C2 CLOSE
' close the I2C channel
PRINT "Time is " RData(1) ":" RData(0)

This is an example of communications between two PicoMites where one is the master and the other
is the slave.
First the master:
SETPIN GP2, GP3, I2C2
I2C2 OPEN 100, 1000
i = 10
DO
i = i + 1
a$ = STR$(i)
I2C2 WRITE &H50, 0, LEN(a$), a$
PAUSE 200
I2C2 READ &H50, 0, 8, a$
PRINT a$
PAUSE 200
LOOP

Then the slave:
SETPIN GP2, GP3, I2C2
I2C2 SLAVE OPEN &H50, tint, rint
DO : LOOP
SUB rint
LOCAL count, a$
I2C2 SLAVE READ 10, a$, count
PRINT LEFT$(a$, count)
END SUB
SUB tint
LOCAL a$ = Time$
I2C2 SLAVE WRITE LEN(a$), a$
END SUB



Appendix C – 1-Wire Communications
1-Wire Communications
The 1-Wire protocol was developed by Dallas Semiconductor to communicate with chips using a single
signalling line. This implementation was written for MMBasic by Gerard Sexton.
There are three commands that you can use:
ONEWIRE RESET pin
ONEWIRE WRITE pin, flag, length, data [, data…]
ONEWIRE READ pin, flag, length, data [, data…]

Reset the 1-Wire bus
Send a number of bytes
Get a number of bytes

Where:
pin - The PicoMite I/O pin to use. It can be any pin capable of digital I/O.
flag - A combination of the following options:
1 - Send reset before command
2 - Send reset after command
4 - Only send/recv a bit instead of a byte of data
8 - Invoke a strong pullup after the command (the pin will be set high and open drain disabled)
length - Length of data to send or receive
data - Data to send or variable to receive.
The number of data items must agree with the length parameter.
The automatic variable MM.ONEWIRE returns true if a device was found
After the command is executed, the I/O pin will be set to the not configured state unless flag option 8 is used.
When a reset is requested the automatic variable MM.ONEWIRE will return true if a device was found. This
will occur with the ONEWIRE RESET command and the ONEWIRE READ and ONEWIRE WRITE
commands if a reset was requested (flag = 1 or 2).
The 1-Wire protocol is often used in communicating with the DS18B20 temperature measuring sensor and to
help in that regard MMBasic includes the TEMPR() function which provides a convenient method of directly
reading the temperature of a DS18B20 without using these functions.



Appendix D – SPI Communications
SPI Communications
The Serial Peripheral Interface (SPI) communications protocol is used to send and receive data between
integrated circuits. The PicoMite acts as the master (i.e. it generates the clock).

I/O Pins
Before an SPI interface can be used the I/O pins for the channel must be allocated using the following
commands. For the first channel (referred as SPI) it is:
SETPIN rx, tx, clk, SPI
Valid pins are
RX:
GP0, GP4, GP16 or GP20
TX:
GP3, GP7 or GP19
CLK: GP2, GP6 or GP18
And the following command for the second channel (referred to as SPI2) is:
SETPIN rx, tx, clk, SPI2
Valid pins are
RX:
GP8, GP12 or GP28
TX:
GP11, GP15 or GP27
CLK: GP10, GP14 or GP26
TX is data from the PicoMite and RX is data to it.

SPI Open
To use the SPI function the SPI channel must be first opened.
The syntax for opening the first SPI channel is (use SPI2 for the second channel):
SPI OPEN speed, mode, bits
Where:
 ‘speed’ is the speed of the clock. It is a number representing the clock speed in Hz.
 'mode' is a single numeric digit representing the transmission mode – see Transmission Format below.
 'bits' is the number of bits to send/receive. This can be any number in the range of 4 to 16 bits.
 It is the responsibility of the program to separately manipulate the CS (chip select) pin if required.

Transmission Format
The most significant bit is sent and received first. The format of the transmission can be specified by the 'mode'
as shown below. Mode 0 is the most common format.
Mode

Description

CPOL

CPHA

0

Clock is active high, data is captured on the rising edge and output on the falling edge

0

0

1

Clock is active high, data is captured on the falling edge and output on the rising edge

0

1

2

Clock is active low, data is captured on the falling edge and output on the rising edge

1

0

3

Clock is active low, data is captured on the rising edge and output on the falling edge

1

1

For a more complete explanation see: http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus

Standard Send/Receive
When the first SPI channel is open data can be sent and received using the SPI function (use SPI2 for the
second channel). The syntax is:
received_data = SPI(data_to_send)
Note that a single SPI transaction will send data while simultaneously receiving data from the slave.
‘data_to_send’ is the data to send and the function will return the data received during the transaction.
‘data_to_send’ can be an integer or a floating point variable or a constant.
If you do not want to send any data (i.e. you wish to receive only) any number (e.g. zero) can be used for the
data to send. Similarly if you do not want to use the data received it can be assigned to a variable and ignored.



Bulk Send/Receive
Data can also be sent in bulk (use SPI2 for the second channel):
SPI WRITE nbr, data1, data2, data3, … etc
or
SPI WRITE nbr, string$
or
SPI WRITE nbr, array()
In the first method 'nbr' is the number of data items to send and the data is the expressions in the argument list
(i.e. 'data1', data2' etc). The data can be an integer or a floating point variable or a constant.
In the second or third method listed above the data to be sent is contained in the 'string$' or the contents of
'array()' (which must be a single dimension array of integer or floating point numbers). The string length, or the
size of the array must be the same or greater than nbr. Any data returned from the slave is discarded.
Data can also be received in bulk (use SPI2 for the second channel):
SPI READ nbr, array()
Where 'nbr' is the number of data items to be received and array() is a single dimension integer array where the
received data items will be saved. This command sends zeros while reading the data from the slave.

SPI Close
If required the first SPI channel can be closed as follows (the I/O pins will be set to inactive):
SPI CLOSE
Use SPI2 for the second channel.

Examples
The following example shows how to use the SPI port for general I/O. It will send a command 80 (hex) and
receive two bytes from the slave SPI device using the standard send/receive function:
PIN(10) = 1 : SETPIN 10, DOUT
SETPIN GP20, GP3, GP2, SPI
SPI OPEN 5000000, 3, 8
PIN(10) = 0
junk = SPI(&H80)
byte1 = SPI(0)
byte2 = SPI(0)
PIN(10) = 1
SPI CLOSE

' pin 10 will be used as the enable signal

' assign the I/O pins
' speed is 5 MHz and the data size is 8 bits
' assert the enable line (active low)
' send the command and ignore the return
' get the first byte from the slave
' get the second byte from the slave
' deselect the slave
' and close the channel

The following is similar to the example given above but this time the transfer is made using the bulk
send/receive commands:
OPTION BASE 1
DIM data%(2)
SETPIN GP20, GP3, GP2, SPI
PIN(10) = 1 : SETPIN 10, DOUT
SPI OPEN 5000000, 3, 8
PIN(10) = 0
SPI WRITE 1, &H80
SPI READ 2, data%()
PIN(10) = 1
SPI CLOSE


' our array will start with the index 1
' define the array for receiving the data

' assign the I/O pins
' pin 10 will be used as the enable signal
' speed is 5 MHz, 8 bits data
' assert the enable line (active low)
' send the command
' get two bytes from the slave
' deselect the slave
' and close the channel


Appendix E – Regex Syntax
Regex Syntax
The alternate forms of the INSTR() and LINSTR() functions can take a regular expression as the search pattern.
The alternate form of the commands are:
INSTR([start],text$, search$ [,size])
LINSTR(text%(),search$ [,start] [,size]
In both cases specifying the size parameter causes the firmware to interpret the search string as a regular
expression. The size parameter is a floating point variable that is used by the firmware to return the size of a
matching string. If the variable doesn't exist it is created. As implemented in MMBasic you need to apply the
returned start and size values to the MID$ function to extract the matched string. e.g.
IF start THEN match$=MID$(text$,start,size) ELSE match$=”” ENDIF
The library used for the regular expressions “implements POSIX draft P1003.2/D11.2, except for some of the
internationalization features”. See http://mirror.math.princeton.edu/pub/oldlinux/Linux.old/Refdocs/POSIX/all.pdf section 2.8 for details of constructing Regular Expressions or other online tutorials if you
are not familiar with them.
The syntax of regular expressions can vary slightly with the various implementations. This document is a
summary of the syntax and supported operations used in the MMBasic implementation.
Anchors
^ Start of string
$ End of string
\b Word Boundary
\B Not a word boundary
\< Start of word
\> End of word
Qualifiers
*
0 or more (not escaped)
\+
1 or more
\?
0 or 1
\{3\} Exactly 3
\{3,\} 3 or more
\{3,5\} 3,4 or 5
Groups and Ranges
(a\|b)
a or b
\(…\) group
[abc]
Range (a or b or c)
[^abc] Not (a or b or c]
[a-q]
lower case letters a to q
[A-Q] upper case letters A to Q
[0-7]
Digits from 0 to 7
Escapes Required to Match Normal Characters
\^ to match ^ (caret)
\.
to match . (dot)
\* to match * (asterix)
\$ to match $ (dollar)
\[ to match [ (left bracket)
\\
to match \ (backslash)



Escapes with Special Functions
\+ See Quantifiers
\? See Quantifiers
\{ See Quantifiers
\} See Quantifiers
\| See Groups and Ranges
\( See Groups and Ranges
\) See Groups and Ranges
\w See Character Classes
Character Classes
\w
digits,letters and _
[:word:] digits,letters and _
[:upper:] Upper case letters_
[:lower:] Lower case letters_
[:alpha:] All letters
[:alnum:] Digits and letters
[:digit:] Digits
[:xdigit:] Hexidecimal digits
[:punct:] Puntuation
[:blank:] Space and tab
[:space:] Blank charaters
[:cntrl:] Control charaters
[:graph:] Printed characters
[:print:] Printed chars and spaces
Example expression to match an IP Address which is contained within a word boundary.
"\<[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\>"



Appendix F – The PIO Programming Package
The PIO Programming Package
Introduction to the PIO
The RP2040 has many built in peripherals like PWM, UART, ADC, SPI. In addition the RP2040 chip contains
two PIO blocks, rather like cut-down, highly specialised CPU cores. MMBasic refers to them as PIO0 and
PIO1 in line with the Raspberry Pi documentation. They are capable of running completely independently of
the main system and of each other. They can be used to create such things as very high accuracy serial data
interfaces and bit streams, although they are by no means restricted to this sort of thing. They can be made to
run extremely fast, with a throughput of up to 32 bits during every clock cycle.
Before a state machine can execute it's program, the program needs to be written to PIO memory, and the state
machine needs to be configured.
This appendix describes the support MMBasic can give in using PIO. It does not contain an explanation how to
write PIO state machine programs. For better understanding how the PIO state machines work look at
following thread "PIO explained PICOMITE" on the thebackshed.com forum:
https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=15385

Overview of PIO
A single PIO block has four independent state machines. All four state machines share a single 32 instruction
program area of flash memory. This memory has write-only access from the main system, but has four read
ports, one for each state machine, so that each can access it independently at its own speed. Each state machine
has its own program counter.
Each state machine also has two 32-bit "scratchpad" registers, X and Y, which can be used as temporary data
stores.
I/O pins are accessed via an input/output mapping module that can access 32 pins (but limited to 30 for the
RP2040). All state machines can access all the pins independently and simultaneously.
The system can write data into the input end of a 4-word 32-bit wide TX FIFO buffer. The state machine can
then use pull to move the output word of the FIFO into the OSR (Output Shift Register). It can also use out to
shift 1-32 bits at a time from the OSR into the output mapping module or other destinations. AUTOPULL can
be used to automatically pull data until the TX FIFO is empty or reaches a preset level.
The system can read data from the output end of a 4-word 32-bit wide RX FIFO buffer. The state machine can
then use in to shift 1-32 bits of data at a time from the input mapping module into the ISR (Input Shift
Register). It can also use push to move the contents of the ISR into the FIFO. AUTOPUSH can be used to
automatically push data until the RX FIFO is full or reaches a preset level.
The FIFO buffers can be reconfigured to form a single direction 8-word 32-bit FIFO in a single direction. The
buffers allow data to be passed to and from the state machines without either the system or the state machine
having to wait for the other.
Each of the four state machines in the PIO has four registers associated with it:
• CLKDIV is the clock divider, which has a 16-bit integer divider and an 8-bit fractional divider. This
sets how fast the state machine runs. It divides down from the main system clock.
• EXECCTRL holds information controlling the translation and execution of the program memory
• SHIFTCTRL controls the arrangement and usage of the shift registers
• PINCTRL controls which and how the GPIO pins are used.
The four state machines of a PIO have shared access to its block of 8 interrupt flags. Any state machine can use
any flag. They can set, reset or wait for them to change. In this way they can be made to run synchronously if
required. The lower four flags are also accessible to and from the main system, so the PIO can be controlled or
pass interrupts back.
DMA can be used to pass information to and from the PIO block via its FIFO from the RP2040's memory
A PIO has nine possible programming instructions, but there can be many variations on each one. For example,
Mov can have up to 8 sources, 8 destinations, 3 process operations during the copy, with optional delay and/or
side set operations!
• Jmp Jump to an absolute address in program memory if a condition is true (or instantly).
• Wait Stall operation of the state machine until a condition is true.
• In
Shift a number of bits from a source into the ISR.


• Out
Shift a number of bits out of the OSR to a destination.
• Push Push the contents of the ISR into the RX FIFO as a single 32-bit word.
• Pull
Load a 32-bit word from the TX FIFO into the OSR.
• Mov Copy date from a source to a destination.
• Irq
Set or clear an interrupt flag.
• Set
Immediately write data to a destination.
Instructions are all 16-bit and contain both the instruction and all data associated with it. All instructions
operate in 1 clock cycle, but it is possible to introduce a delay of several idle clock cycles between an
instruction and the next.
Additionally, there is a facility called "side-set" which allows a value to be written to some pre-defined output
pins while an instruction is being read from memory. This is transparent to the program.

Programming PIO
PicoMite programs the PIO statemachine memory using one of the following commands. Each option will be
explained with an example of the exact same program that toggles one of the GPIO lines of the PicoMite.
Which GPIO line is toggled, is determined in the configuration.

PIO ASSEMBLE
This command is used to use the build in assembler to generate the program from mnemonics, then write it
directly into PIO memory.
PIO ASSEMBLE 1,".program test"
PIO ASSEMBLE 1,".line 0"
PIO ASSEMBLE 1,"SET PINDIRS 1"
PIO ASSEMBLE 1,"label:"
PIO ASSEMBLE 1,"SET PIN 1"
PIO ASSEMBLE 1,"SET PIN 0"
PIO ASSEMBLE 1,"JMP label"
PIO ASSEMBLE 1,".end program list"

'a program has to have a name
'start the program at line 0
'SET the GPIO line to output
'define a label called "label"
'SET the GPIO pin high
'SET the GPIO pin low
'JuMP to "label" in an endless loop
'end program, list=show result

PIO PROGRAM LINE
This command can be used to program 16bit values to indidual lines in the PIO memory.
pio program line 1,0,&hE081
pio program line 1,1,&hE001
pio program line 1,2,&hE000
pio program line 1,3,&h0001

'SET pin output
'SET pin high
'SET pin low
'JMP to line 1

PIO PROGRAM
This command writes all 32 lines in one PIO from an array. This is useful once a PIO program is debugged. It
is extremely compact.
Dim a%(7)=(&h0001E0000E001E081,0,0,0,0,0,0,0)
PIO program 1,a%()

Configuring PIO
The PicoMite can configure each state machine individually. Configuration allows 2 state machines to run the
exact same program lines (e.g. an SPI interface) but operate with different GPIO pins and at different speeds.
There are several configuration fields.

FREQUENCY
PicoMite contains a default configuration for each configuration field, except for the frequency. The frequency
is set by a 16 bit divider from the ARM clock. Example: when OPTION CPUSPEED 126000 is set the PIO can
run at speeds between 126MHz and 1.922kHz (126000000 / 65536). Be aware that higher CPU speeds
(overclocking) directly impact the state machine frequency.

PIN CONTROL
PicoMite defaults the GPIO pins for use by MMBasic. For the PIO to take ownership of a GPIO pin MMBasic
needs to assign it to PIO as below.
SETPIN GPxx,PIOx
(e.g. SETPIN gp0,pio1)


A state machine can SET the state of a pin (SET is a state machine instruction), but can also output serial data
to one or more GPIO pins using the OUT instruction. Or read serial data using the IN instruction. And GPIO
pins can be set as a side effect of any state machine instruction (SIDE SET). For each method of interfacing,
different pins can be mapped to the state machine.
It is important to understand is that these instructions work on consecutive pins. This means that there is a range
of pins that can be controlled, starting at the lowest GPx pin number (e.g. GP0), and pins next to it can be
included (up to 5 pins in total). So GP0,GP1,GP2 is a valid set of IO pins. GP0,GP1,GP6 is not. Consider this
when designing a PIO application.
Assigning GPIO pins to a state machine uses the PIO helper function:
PIO(PINCTRL a,b,c,d,e,f,g)
a/ the number of SIDE SET pins (0...5), SIDE SET can write 5 pins at once
b/ the number of SET pins
(0...5), SET can write 5 pins at once
c/ the number of OUT pins
(0...31), OUT can write 32 pins at once
d/ the lowest pin for IN pins (GP0.....GP31) IN can read up to 32 pins at once
e/ the lowest pin for SIDE SET (GP0.....GP31)
f/ the lowest pin for SET
(GP0.....GP31)
g/ the lowest pin for OUT
(GP0.....GP31)

Ranges for the different functions can overlap, be identical, or adjacent.

EXECUTE CONTROL
The execute control register EXECCTRL configures the program flow. There is a field that connects a GPIO
pin to a conditional jump (JMP instruction), and fields that hold the line address of the main program loop
begin (.WRAP TARGET) and end (.WRAP).
If we want the program flow to change in response of a GPIO pin state, a JMP PIN is used. The JMP pin is
assigned in the execute control configuration (there can only be 1 pin per state machine) and the JMP happens
only when the pin is high).
The state machine program starts at the beginning and runs until it reaches the end. In above demo program, the
program loops from the end to beginning using a (unconditional) JMP instruction. An alternative way to using
the JMP instruction is defining the beginning of the loop (WRAP TARGET = line 1) and end of the loop
(WRAP = line 2) and configure the state machine to only execute these instructions in between. The JMP
instruction in line 3 is obsolete when WRAP/WRAP TARGET is used.
PIO(EXECCTRL a,b,c)
a/ the GPIO pin for conditional JMP (e.g. GP0)
b/ the WRAP TARGET line number
(e.g. 1)
c/ the WRAP line number
(e.g. 2)

SHIFT CONTROL
The IN and OUT instructions shift data from the FIFO register to the GPIO pins. In between MMBasic and the
PIO, 32bit words can be communicated. Since both the ARM cores and the PIO processors operate
independently, the data is exchanged through FIFO's. The ARM (MMBasic) puts data in the FIFO, PIO reads
it. This uses the TX FIFO. The other way around uses the RX FIFO. The FIFO's are normally 4 words deep but
can be configured to a single 8 word deep RX or TX FIFO.
The PIO can "shift" data IN the RX FIFO from the MSB side, or from the LSB side. That is set with the IN
SHIFTDIR bit. Similar the OUT SHIFTDIR bit for OUT data. The autopull and autopush flags in combination
with the pull and push thresholds determine when FIFO is replenished.
PIO(SHIFTCTRL a,b,c,d,e,f,g,h)
a/ push threshold
b/ pull threshold
c/ autopush
d/ autopull
e/ IN-shiftdir
f/ OUT-shiftdir
g/ fjoin_rx
h/ fjoin_tx


(leave 0 for now)
(leave 0 for now)
(leave 0 for now)
(leave 0 for now)
(1 = shift MSB, 0 = shift LSB)
(1 = shift MSB, 0 = shift LSB)
(join TX and RX fifo to 1 RX fifo)
(join TX and RX fifo to 1 TX fifo)


WRITING THE STATE MACHINE CONFIGURATION
A state machine configuration is written using the command:
PIO INIT MACHINE a,b,c,d,e,f,g
a/ the PIO
(0 or 1)
b/ the state machine number
(0...3)
c/ frequency
(CPUSPEED/65536...CPUSPEED in Hz)
d/ pincontrol value
(PIO(PINCTRL ......))
e/ execture control value
(PIO(EXECCTRL......))
f/ shiftcontrol value
(PIO(SHIFCTRL......))
g/ start address
(0....31, the line at which the state machine starts executing)

STARTING AND STOPPING A STATE MACHINES
Once the PIO is configured, you can start and stop the state machine using:
PIO START a,b
PIO STOP a,b
a/ the PIO number
b/ the state machine

(0 or 1)
(0...3)

Note that when stopping a state machine, it stops right where it is. To restart the state machine it is advisable to
PIO INIT MACHINE first.

EXAMPLE PROGRAM 1
A complete PIO implementation that toggles a GPIO pins can be implemented in MMBasic as shown below.
Connect a buzzer to GP0, and hear the audio tone generated by the PIO.
'disconnect ARM from GP0
setpin gp0,pio1

'use GP0 as output pin for PIO 1

'pio program used
'0 E081
'SET pin output
'1 E001
'SET pin high
'2 E000
'SET pin low
'3 0001
'jmp 1
'program pio 1 using an array to write the program in PIO memory, and start
Dim a%(7)=(&h0001E000E001E081,0,0,0,0,0,0,0)
PIO program 1,a%()
'configure pio 1 statemachine 0
p=Pio(pinctrl 0,1,,,,gp0,)
f=2029
133000
PIO init machine 1,0,f,p
address(=0)

'define SET uses 1 pin, and that is GP0
'2029 Hz is lowest frequency for CPUSPEED
'use default for execctrl, shiftctrl, start

'start the PIO 1 state machine 0
PIO start 1,0

Note that the MMBasic program ends, but the sound on the buzzer continues. PIO is independent of the ARM
processor, and continues until it is stopped. Entering the MMBasic editor stops the PIO.

FIFO's
MMBasic and the PIO exchange information using FIFO's. The PIO's PUSH data into the RX FIFO (MMBasic
is the receiver), or PULL data from the TX FIFO (MMBasic is the transmitter).
When PIO is fetching data from the FIFO the data is transferred to the OSR (Output Shift Register), from there
is can be processed. The PIO can push the data from the ISR (Input shift register) into the FIFO. Additionally,
the PIO has 2 registers X and Y that can be used for storage, or counting. PIO cannot add or subtract or
compare.
Data flow:
MMBasic -> FIFO -> OSR -> PIO (or pins)
PIO (or pins) -> ISR -> FIFO -> MMBasic
MMBasic can write data into the TX FIFO and read data from the RX FIFO using:


PIO READ a,b,c,d
PIO WRITE a,b,c,d
a/ PIO number
(0 or 1)
b/ state machine number
(0...3)
c/ number of 32 bit words
(1...4)
d/ integer variable name (i.e. variable% or array%())

PIO CLEAR clears all the PIO FIFO's, as does PIO START and PIO INIT MACHINE.
The MMBAsic program doesn't need to wait for data in the FIFO to appear since the RX FIFO can be assigned
an interrupt. The MMBasic interrupt routine can fetch the data from the FIFO.
Similar for TX interrupt in which case MMBasic gets an interrupt when data is needed for the TX FIFO.
PIO INTERRUPT a,b,c,d
a/ PIO
(0 or 1)
b/ state machine
(0...3)
c/ Name of RX interrupt handler (i.e. "myRX_Interrupt" or 0 to disable)
d/ Name of TX interrupt handler (i.e. "myTX_Interrupt" or 0 to disable)

EXAMPLE PROGRAM 2
Below program explains many of the above presented MMbasic functions and commands. The program reads a
NES controller (SPI) connected to the PicoMite. The NES controller consists of a HEF4021 shift register
connected to 8 push button switches.
Program uses: wrap and wrap target, IN, side set and delay, PUSH, PIO READ. GP0 and GP1 are in SET for
pin direction, and in side set for compact code.
The wiring is as defined in the code:
'disconnect ARM from GP0/1/2
setpin gp0,pio1
setpin gp1,pio1
setpin gp2,pio1

'clock out
'load out
'data in

'PIO program
PIO assemble 1,".program NES"
PIO assemble 1,".side_set 2"
PIO assemble 1,".line 0"
PIO assemble 1,"SET pindirs,&b11"
PIO assemble 1,".wrap target"
PIO assemble 1,"IN null,32 side 2"
PIO assemble 1,"SET X,7 side 0"
PIO assemble 1,"loop:"
PIO assemble 1,"IN pins,1 side 0"
PIO assemble 1,"JMP X-- loop side 1"
PIO assemble 1,"PUSH side 0 [7]"
PIO assemble 1,".wrap"
PIO assemble 1,".end program list"

'a program needs a name
'use 2 bits for side set, 3 for delay
'start code at line 0
'set GP0,GP1 output, side GP0,GP1 low
'wrap target = top of the loop
'set ISR to 0, GP1 high (load), GP0 low
'set X counter to 7, GP0,GP1 low
'inner loop label
'shift 1 databit in, keep GP0,GP1 low
'jmp to loop, dec. X, GP0 high(clock)
'now X=0, PUSH result into FIFO, delay 7
'end outer loop, repeat
'end of program, list result

'configure pio1
p=Pio(pinctrl 2,2,,gp2,gp0,gp0,)
'GP0,GP1 out (SET and SIDE SET), GP2
IN
f=1e5
'100kHz
s=PIO(shiftctrl 0,0,0,0,0,0)
'shift in from LSB for IN (and OUT)
e=PIO(execctrl gp0,PIO(.wrap target),PIO(.wrap)
'wrap and wrap target
'write the configuration
PIO init machine 1,0,f,p,e,s,0
'start the pio1 code
PIO start 1,0

'Check the the read data in MMBasic and print
dim d%
do
pio read 1,0,1,d%
print bin$(d%)



pause 200
loop
END

DMA To and From the FIFOS
The way that DMA works is as follows:
When reading from the FIFO the DMA controller waits on data being in the FIFO and when it appears transfers
that data into processor memory. Each time it reads it increments the pointer into the processor memory so that
it can, for example, incrementally fill an array as each and every data item is made available.
When writing to the FIFO the DMA controller writes data from processor memory to the FIFO automatically
waiting whenever the FIFO is full. Thus, data can be prepared in an array and the DMA controller will stream
that data to the PIO FIFO as fast as the PIO program requires it.
DMA can transfer a 32-bit word, a 16-bit short, or an 8-bit byte and when setting up DMA you need to tell it
the size of the tranfer and how many transfers to make. Because each transfer will increment the memory
pointer by 1,2, or 4 bytes MMBasic must deal with the data packed into memory rather than the 64-bits used for
MMbasic integers and floats. Luckily MMBasic implements two commands MEMORY PACK and MEMORY
UNPACK to do this very efficiently but it could equally be done using standard BASIC arithmetic.
The DMA can be configured to repeatedly loop data into or out of a section of memory (a ring buffer)
The commands are:
PIO DMA_IN a,b,c,d,e,f,g
PIO DMA_OUT a,b,c,d,e,f,g
a/ pio
b/ state machine
c/ nbr
d/ data%()
e/ completioninterrupt
f/ transfersize
g/ loopbackcount

(0 or 1)
(0...3)
(number of words to be transferred)
(interger array name)
(where to go when done, optional)
(8/16/32, optional)
(used data%() as a ring buffer, optional, loopbackcount = 2^n)

The DMA will start the state machine automatically and there is no need for a PIO START command. But,
before starting the transfer make sure a fresh PIO INIT MACHINE is done, so the state machine starts at the
required start address.
When a ring buffer is used, it requires special preparation:
PIO MAKE RING BUFFER a,b
a/ name of integer buffer
b/ size of the array in bytes

Example :
DIM packed%
PIO MAKE RING BUFFER packed%,4096

packed% will then be an integer array holding 4096/8=512 integers
This can then be used by the DMA for a loopbackcounter with DMA of 1024 32-bit words, 2048 16-bit shorts
or 4096 8-bit bytes

EXAMPLE PROGRAM 3
This program brings everything together and uses DMA to read 128 samples from the PIO RX FIFO. For the
demonstration, GP0 to GP5 are outputs of 3 PWMS, and are ,at the same time, sampled by the PIO as a 6
channel logic analyser or oscilloscope. The 128 samples are sent to the serial port as waveforms.
This program also demonstrates PIO DMA RX, MEMORY UNPACK, the use of buffers.
'generate a 50Hz 3 phase test signal to demonstrate the DMA on 6 GPIO pins.
SetPin gp0,pwm 'CH 0a
SetPin gp1,pwm 'CH 0b
SetPin gp2,pwm 'CH 1a
SetPin gp3,pwm 'CH 1b
SetPin gp4,pwm 'CH 2a
SetPin gp5,pwm 'CH 2b
Fpwm = 50: PW = 100 / 3
PWM 0, Fpwm, PW, PW - 100, 1, 1
PWM 1, Fpwm, PW, PW - 100, 1, 1



PWM 2, Fpwm, PW, PW - 100, 1, 1
PWM sync 0, 100/3, 200/3
'----------------------------------- LA code PIO -------------------------'PIO code to sample GP0..GP6 as elementary logic analyser
PIO clear 1
'in this program the PIO reads GP0..GP5 brute force
'and pushes data into FIFO. The clock speed determines the
'sampling rate. There are 2 instructions per cycle
'taking 10000/2 / 50 = 100 samples per 50Hz cycle.
PIO assemble 1,".program push"
PIO assemble 1,".line 0"
PIO assemble 1,".wrap target"
PIO assemble 1,"IN pins,6"
PIO assemble 1,"PUSH block"

‘'get 6 bits from GPIO pins (GP0..GP5)
'only push data when FIFO has room

PIO assemble 1,".wrap"
PIO assemble 1,".end program list"
'configuration
f=1e4
'PIO run at 10kHz
p=Pio(pinctrl 0,0,0,gp0,,,)
'IN base = GP0
e=Pio(execctrl gp0,PIO(.wrap target),PIO(.wrap)) 'wrap 1 to 0, gp0 is default
s=Pio(shiftctrl 0,0,0,0,0,0)
'shift in through LSB, out is not used
'write the configuration, running 10kHz (data in FIFO 10us after edge GP0)
PIO init machine 1,0,f,p,e,s,0
'start address = 0
'---------------------------- LA code MMBasic -------------------------------'define memory buffers
Dim a$(1)=("_","-")
'characters for the printout
length%=64
'size of the packed array
Dim data%(2*length%-1)
'array to put the 32 bit samples FIFO
format
Dim packed%(length%-1)
'DMA array to pack 32 bit samples in 64
bit integers
'let the DMA machine run, and repeat at will
Do
PIO DMA RX 1,0,2*length%,packed%(),ReadyInt
print "press any key to restart sampling"
do:loop while inkey$=""
Loop
End
'-----------------------------------SUBS MMBasic ----------------------------Sub ReadyInt
'stop the PIO and re-init for next run
PIO stop 1,0
PIO init machine 1,0,f,p,e,s,0
'start address = 0
'get the data from the packed DMA buffer and unpack to original 32 bit format
Memory unpack packed%(),data%(),2*length%,32
'Serial output as if logic analyzer traces
For j=0 To 5
mask%=2^j
For i=0 To 2*length%-1
If i<106 Then Print a$(((data%(i) And mask%)=mask%));
Next i
Print : Print
Next j
End Sub



Appendix G – Programming in BASIC - A Tutorial
Programming in BASIC - A Tutorial
The PicoMite is programmed using the BASIC programming language. The PicoMite version of
BASIC is called MMBasic which loosely emulates the Microsoft BASIC interpreter that was popular
years ago.
The BASIC language was introduced in 1964 by Dartmouth College in the USA as a computer
language for teaching programming and accordingly it is easy to use and learn. At the same time, it
has proved to be a competent and powerful programming language and as a result it became very
popular in the late 70s and early 80s. Even today some large commercial data systems are still written
in the BASIC language (primarily Pick Basic).
For the PicoMite the greatest advantage of BASIC is its ease of use. Some more modern languages
such as C and C++ can be truly mind bending but with BASIC you can start with a one line program
and get something sensible out of it. MMBasic is also powerful in that you can draw sophisticated
graphics, manipulate the external I/O pins to control other devices and communicate with other
devices using a range of built-in communications protocols.
Command Prompt
Interaction with MMBasic is done via the console at the command prompt (ie, the greater than symbol
(>) on the console). On startup MMBasic will issue the command prompt and wait for some
command to be entered. It will also return to the command prompt if your program ends or if it
generated an error message.
When the command prompt is displayed you have a wide range of commands that you can enter and
execute. Typically they would list the program held in memory (LIST) or edit it (EDIT) or perhaps
set some options (the OPTION command). Most times the command is just RUN which instructs
MMBasic to run the program held in program memory.
Almost any command can be entered at the command prompt and this is often used to test a command
to see how it works. A simple example is the PRINT command (more on this later), which you can
test by entering the following at the command prompt:
PRINT 2 + 2
and not surprisingly MMBasic will print out the number 4 before returning to the command prompt.
This ability to test a command at the command prompt is useful when you are learning to program in
BASIC, so it would be worthwhile having the PicoMite handy for the occasional test while you are
working through this tutorial.
Structure of a BASIC Program
A BASIC program starts at the first line and continues until it runs off the end or hits an END
command - at which point MMBasic will display the command prompt (>) on the console and wait for
something to be entered.
A program consists of a number of statements or commands, each of which will cause the BASIC
interpreter to do something (the words statement and command generally mean the same and are used
interchangeable in this tutorial).
Normally each statement is on its own line but you can have multiple statements in the one line
separated by the colon character (:).
For example;
A = 24.6 : PRINT A



Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters
however modern implementations (such as MMBasic) do not need them. You can still use them if
you wish but they have no benefit and generally just clutter up your programs.
This is an example of a program that uses line numbers:
50 A = 24.6
60 PRINT A
A line can also start with a label which can be used as the target for a program jump using the GOTO
command. This will be explained in more detail when we cover the GOTO command but this is an
example (the label name is JmpBack):
JmpBack: A = A + 1
PRINT A
GOTO JmpBack
Comments
A comment is any text that follows the single quote character ('). A comment can be placed anywhere
and extends to the end of the line. If MMBasic runs into a comment it will just skip to the end of it
(ie, it does not take any action regarding a comment).
Comments should be used to explain non obvious parts of the program and generally inform someone
who is not familiar with the program how it works and what it is trying to do. Remember that after
only a few months a program that you have written will have faded from your mind and will look
strange when you pick it up again. For this reason you will thank yourself later if you use plenty of
comments.
The following are some examples of comments:
' calculate the hypotenuse
PRINT SQR(a * a + b * b)
or
INPUT var

' get the temperature

Older BASIC programs used the command REM to start a comment and you can also use that if you
wish but the single quote character is easier to use and more convenient.
The PRINT Command
There are a number of common commands that are fundamental and we will cover them in this
tutorial but arguably the most useful is the PRINT command. Its job is simple; to print something on
the console. This is mostly used to output data for you to see (like the result of calculations) or
provide informative messages.
PRINT is also useful when you are tracing a fault in your program; you can use it to print out the
values of variables and display messages at key stages in the execution of the program.
In its simplest form the command will just print whatever is on its command line. So, for example:
PRINT 54
will display on the console the number 54 followed by a new line.
The data to be printed can be something simple like this or an expression, which means something to
be calculated. We will cover expressions in more detail later but as an example the following:
> PRINT 3/21
0.1428571429
>
would calculate the result of three divided by twenty one and display it. Note that the greater than
symbol (>) is the command prompt produced by MMBasic – you do not type that in.


Other examples of the PRINT command include:
> PRINT "Wonderful World"
Wonderful World
> PRINT (999 + 1) / 5
200
>
You can try these out at the command prompt.
The PRINT command will also work with multiple values at the same time, for example:
> PRINT "The amount is" 345 " and the second amount is" 456
The amount is 345 and the second amount is 456
>
Normally each value is separated by a space character as shown in the previous example but you can
also separate values with a comma (,). The comma will cause a tab to be inserted between the two
values. In MMBasic tabs in the PRINT command are eight characters apart.
To illustrate tabbing, the following command prints a tabbed list of numbers:
> PRINT 12, 34, 9.4, 1000
12
34
9.4
1000
>
Note that there is a space printed before each number. This space is a place holder for the minus
symbol (-) in case the value is negative. You can see the difference with the number 12 in this
example:
> PRINT -12, 34, -9.4, 1000
-12
34
-9.4
1000
>
The print statement can be terminated with a semicolon (;). This will prevent the PRINT command
from moving to a new line when it has printed all the text. For example:
PRINT "This will be";
PRINT " printed on a single line."
Will result in this output:
This will be printed on a single line.
The message would be look like this without the semicolon at the end of the first line:
This will be
printed on a single line.
Variables
Before we go much further we need to define what a "variable" is as they are fundamental to the
operation of the BASIC language (in fact, most programming languages). A variable is simply a
place to store an item of data (ie, its "value"). This value can be changed as the program runs which
why it is called a "variable".
Variables in MMBasic can be one of three types. The most common is floating point and this is
automatically assumed if the type of the variable is not specified. The other two types are integer and
string and we will cover them later. A floating point number is an ordinary number which can contain
a decimal point. For example 3.45 or -0.023 or 100.00 are all floating point numbers.
A variable can be used to store a number and it can then be used in the same manner as the number
itself, in which case it will represent the value of the last number assigned to it.



As a simple example:
A = 3
B = 4
PRINT A + B
will display the number 7. In this case both A and B are variables and MMBasic used their current
values in the PRINT statement. MMBasic will automatically create a variable when it first encounters
it so the statement A = 3 both created a floating point variable (the default type) with the name of A
and then it assigned the value of 3 to it.
The name of a variable must start with a letter while the remainder of the name can use letters,
numbers, the underscore or the full stop (or period) characters. The name can be up to 31 characters
long and the case (ie, capitals or not) is not important. Here are some examples:
Total_Count
ForeColour
temp3
count
x
ThisIsALongVariableName
increment.value
You can change the value of a variable anywhere in your program by using the assignment command,
ie:
variable = expression
For example:
temp3 = 24.6
count = 5
CTemp = (FTemp – 32) * 0.5556
In the last example both CTemp and FTemp are variables and this line converts the value of FTemp
(in degrees Fahrenheit) to degrees Celsius and stores the result in the variable CTemp.
Expressions
We have met the term ‘expression’ before in this tutorial and in programming it has a specific
meaning. It is a formula which can be resolved by the BASIC interpreter to a single number or value.
MMBasic will evaluate numeric expressions using the same rules that we learnt at school. For
example, multiplication and division are performed first followed by addition and subtraction. These
are called the rules of precedence and are fully spelt out in this manual.
This means that MMBasic will resolve 2 + 3 * 6 by first multiplying 3 by 6 giving 18 then adding 2
resulting in a final value of 20. Similarly, both 5 * 4 and 10 + 4 * 3 – 2 will also resolve to 20.
If you want to force the interpreter to evaluate parts of the expression first you can surround that part
of the expression with brackets. For example, (10 + 4) * (3 – 2) will resolve to 14 not 20 as would
have been the case if the brackets were not used. Using brackets does not appreciably slow down the
program so you should use them liberally if there is a chance that MMBasic will misinterpret your
intention.
As pointed out earlier, you can use variables in an expression exactly the same as straight numbers.
For example, this will increment the value of the variable temp by one:
temp = temp + 1
You can also use functions in expressions. These are special operations provided by MMBasic, for
example to calculate trigonometric values.



As an example, the following will print the length of the hypotenuse of a right angled triangle using
the SQR() function which returns the square root of a number (a and b are variables holding the
lengths of the other sides):
PRINT SQR(a * a + b * b)
MMBasic will first evaluate this expression by multiplying a by a, then multiplying b by b, then
adding the results together. The resulting number is then passed to the SQR() function which will
calculate the square root of that number (ie, the hypotenuse) and return it for the PRINT command to
display.
Some other mathematical functions provided by MMBasic include:
SIN(r) – the sine of r
COS(r) – the cosine of r
TAN(r) – the tangent of r
There are many more functions available to you and they are all listed earlier in this manual.
Note that in the above trigonometric functions the value passed to the function (ie, 'r') is the angle in
radians. In MMBasic you can use the function RAD(d) to convert an angle from degrees to radians
('d' is the angle in degrees).
Another feature of most programming languages including BASIC is that you can nest function calls
within each other. For example, given the angle in degrees (ie, 'd') the sine of that angle can be found
with this expression:
PRINT SIN(RAD(d))
In this case MMBasic will first take the value of d and convert it to radians using the RAD() function.
The output of this function then becomes the input to the SIN() function.
The IF Statement
Making decisions is at the core of most computer programs and in BASIC this is usually done with
the IF statement. This is written almost like an English sentence:
IF condition THEN action
The condition is usually a comparison such as equals, less than, more than, etc.
For example:
IF Temp < 25 THEN PRINT "Cold"
Temp would be a variable holding the current temperature (in ºC) and PRINT "Cold" the action to
be done.
There are a range of tests that you can make:
=
<
>

equals
less than
greater than

<>
<=
>=

not equal
less than or equals
greater than or equals

You can also add an ELSE clause which will be executed if the initial condition tested false:
IF condition THEN true-action ELSE false-action
For example, this will execute different actions when the temperature is under 25 or 25 or more:
IF Temp < 25 THEN PRINT "Cold" ELSE PRINT "Hot"
The previous examples all used single line IF statements but you can also have multiline IF
statements.



They look like this:
IF condition THEN
true-action
true-action
ENDIF
or
IF condition THEN
true-action
true-action
ELSE
false-action
false-action
ENDIF
Unlike the single line IF statement you can have many true actions with each on their own line and
similarly many false actions. Generally the single line IF statement is handy if you have a simple
action that needs to be taken while the multiline version is much easier to understand if the actions are
numerous and more complicated.
An example of a multiline IF statement with more than one action is:
IF Amount < 100 THEN
PRINT "Too low"
PRINT “Minimum value is 100”
ELSE
PRINT "Input accepted"
SaveToSDCard
PRINT "Enter second amount"
ENDIF
Note that in the above example each action is indented to show what part of the IF structure it belongs
to. Indenting is not mandatory but it makes a program much easier to understand for someone who is
not familiar with it and therefore it is highly recommended.
In a multiline IF statement you can make additional tests using the ELSE IF command. This is best
explained by using an example (the temperatures are all in ºC):
IF Temp < 0 THEN
PRINT “Freezing”
ELSE IF Temp < 20 THEN
PRINT “Cold”
ELSE IF Temp < 35 THEN
PRINT “Warm”
ELSE
PRINT “Hot”
ENDIF
The ELSE IF can use the same tests as an ordinary IF (ie, <, <=, etc) but that test will only be made if
the preceding test was false. So, for example, you will only get the message Warm if Temp < 0
failed, and Temp < 20 failed but Temp < 35 was true. The final ELSE will catch the case where
all the tests were false.
An expression like Temp < 20 is evaluated by MMBasic as either true or false with true having a
value of one and false zero. You can see this if you entered the following at the console:
PRINT 30 > 20
MMBasic will print 1 meaning that the value of the expression is true.



Similarly the following will print 0 meaning that the expression evaluated to false.
PRINT 30 < 20
The IF statement does not really care about what the condition actually is, it just evaluates the
condition and if the result is zero it will take that as false and if non zero it will take it as true. This
allows for some handy shortcuts. For example, if BalanceCorrect is a variable that is true (non
zero) when some feature of the program is correct then the following can be used to make a decision
based on that value:
IF BalanceCorrect THEN …do something…
FOR Loops
Another common requirement in programming is repeating a set of actions. For instance, you might
want to step through all seven days in the week and perform the same function for each day. BASIC
provides the FOR loop construct for this type of job and it works like this:
FOR day = 1 TO 7
Do something based on the value of ‘day’
NEXT day
This starts by creating the variable day and assigning the value of 1 to it. The program will then
execute the following statements until it comes to the NEXT statement. This tells the BASIC
interpreter to increment the value of day, go back to the previous FOR statement and re-execute the
following statements a second time. This will continue looping around until the value of day exceeds
7 and the program will then exit the loop and continue with the statements following the NEXT
statement.
As a simple example, you can print the numbers from one to ten like this:
FOR nbr = 1 TO 10
PRINT nbr,;
NEXT nbr
The comma at the end of the PRINT statement tells the interpreter to tab to the next tab column after
printing the number and the semicolon will leave the cursor on this line rather than automatically
moving to the next line. As a result, the numbers will be printed in neat columns across the page.
This is what you would see:
1

2

3

4

5

6

7

8

9

10

The FOR loop also has a couple of extra tricks up it sleeves. You can change the amount that the
variable is incremented by using the STEP keyword. So, for example, the following will print just the
odd numbers:
FOR nbr = 1 TO 10 STEP 2
PRINT nbr,;
NEXT nbr
The value of the step (or increment value) defaults to one if the STEP keyword is not used but you can
set it to whatever number you want.
When MMBasic is incrementing the variable it will check to see if the variable has exceeded the TO
value and, if it has, it will exit from the loop. So, in the above example, the value of nbr will reach
nine and it will be printed but on the next loop nbr will be eleven and at that point execution will
leave the loop. This test is also applied at the start of the loop (ie, if in the beginning the value of the
variable exceeds the TO value (and STEP is positive) the loop will never be executed, not even once).
By setting the STEP value to a negative number you can use the FOR loop to step down from a high
number to low. In that case the starting number must be greater than the TO number.



For example, the following will print the numbers from 1 to 10 in reverse:
FOR nbr = 10 TO 1 STEP -1
PRINT nbr,;
NEXT nbr
Multiplication Table
To further illustrate how loops work and how useful they can be, the following short program will use
two FOR loops to print out the multiplication table that we all learnt at school. The program for this is
not complicated:
FOR nbr1 = 1 to 10
FOR nbr2 = 1 to 10
PRINT nbr1 * nbr2,;
NEXT nbr2
PRINT
NEXT nbr1

The output is shown in the following screen grab, which also shows a listing of the program.

You need to work through the logic of this example line by line to understand what it is doing.
Essentially it consists of one loop inside another. The inner loop, which increments the variable
nbr2 prints one horizontal line of the table. When this loop has finished it will execute the following
PRINT command which has nothing to print - so it will simply output a new line (ie, terminate the
line printed by the inner loop).
The program will then execute another iteration of the outer loop by incrementing nbr1 and
re-executing the inner loop again. Finally, when the outer loop is exhausted (when nbr1 exceeds 10)
the program will reach the end and terminate.
One last point, you can omit the variable name from the NEXT statement and MMBasic will guess
which variable you are referring to. However, it is good practice to include the name to make it easier
for someone else who is reading the program to understand it. You can also terminate multiple loops
using a comma separated list of variables in the NEXT statement. For example:
FOR var1 = 1 TO 5
FOR var2 = 10 to 13
PRINT var1 * var2
NEXT var1, var2



DO Loops
Another method of looping is the DO…LOOP structure which looks like this:
DO WHILE condition
statement
statement
LOOP
This will start by testing the condition and if it is true the statements will be executed until the LOOP
command is reached, at which point the condition will be tested again and if it is still true the loop will
execute again. The ‘condition’ is the same as in the IF command (ie, X < Y).
For example, the following will keep printing the word "Hello" on the console for 4 seconds then stop:
Timer = 0
DO WHILE Timer < 4000
PRINT "Hello"
LOOP
Note that Timer is a function within MMBasic which will return the time in milliseconds since the
timer was reset. A reset is done by assigning zero to Timer (as done above) or when powering up
the PicoMite .
A variation on the DO-LOOP structure is the following:
DO
statement
statement
LOOP UNTIL condition
In this arrangement the loop is first executed once, the condition is then tested and if the condition is
false, the loop will be repeatedly executed until the condition becomes true. Note that the test in
LOOP UNTIL is the inverse of DO WHILE.
For example, similar to the previous example, the following will also print "Hello" for four seconds:
Timer = 0
DO
PRINT "Hello"
LOOP UNTIL Timer >= 4000
Both forms of the DO-LOOP essentially do the same thing, so you can use whatever structure fits
with the logic that you wish to implement.
Finally, it is possible to have a DO Loop that has no conditions at all - ie,
DO
statement
statement
LOOP
This construct will continue looping forever and you, as the programmer, will need to provide a way
to explicitly exit the loop (the EXIT DO command will do this). For example:
Timer = 0
DO
PRINT "Hello"
IF Timer >= 4000 THEN EXIT DO
LOOP



Console Input
As well as printing data for the user to see your programs will also want to get input from the user.
For that to work you need to capture keystrokes from the console and this can be done with the
INPUT command. In its simplest form the command is:
INPUT var
This command will print a question mark on the console's screen and wait for a number to be entered
followed by the Enter key. That number will then be assigned to the variable var.
For example, the following program extends the expression for finding the hypotenuse of a triangle by
allowing the user to enter the lengths of the other sides from the console.
PRINT "Length of side 1"
INPUT a
PRINT "Length of side 2"
INPUT b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
This is a screen capture of a typical session:

The INPUT command can also print your prompt for you, so that you do not need a separate PRINT
command. For example, this will work the same as the above program:
INPUT "Length of side 1"; a
INPUT "Length of side 2"; b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
Finally, the INPUT command will allow you to input a series of numbers separated by commas with
each number being saved in different variables.
For example:
INPUT "Enter the length of the two sides: ", a, b
PRINT "Length of the hypotenuse is" SQR(a * a + b * b)
If the user entered 12,15 the number 12 would be saved in the variable a and 15 in b.
Another method of getting input from the console is the LINE INPUT command. This will get the
whole line as typed by the user and allocate it to a string variable. Like the INPUT command you can
also specify a prompt. This is a simple example:
LINE INPUT "What is your name? ", s$
PRINT "Hello " s$
We will cover string variables later in this tutorial but for the moment you can think of them as a
variable that holds a sequence of characters. If you ran the above program and typed in John when
prompted the program would respond with Hello John.


Sometimes you do not want to wait for the user to hit the enter key, you want to get each character as
it is typed in. This can be done with the INKEY$ function which will return the value of the character
as a string consisting of just one character or an empty string (ie, contains no characters) if nothing has
been entered.
GOTO and Labels
One method of controlling the flow of the program is the GOTO command. This essentially tells
MMBasic to jump to another part of the program and continue executing from there. The target of the
GOTO is a label and this needs to be explained first.
A label is an identifier that marks part of the program. It must be the first thing on the line and it must
be terminated with the colon (:) character. The name that you use can be up to 31 characters long and
must follow the same rules as for a variable's name. For example, in the following program line
LoopBack is a label:
LoopBack:

a = a + 1

When you use the GOTO command to jump to that particular part of the program you would use the
command like this:
GOTO LoopBack
To put all this into context the following program will print out all the numbers from 1 to 10:
z = 0
LoopBack: z = z + 1
PRINT z
IF z < 10 THEN GOTO LoopBack
The program starts by setting the variable z to zero then incrementing it to 1 in the next line. The
value of z is printed and then tested to see if it is less than 10. If it is less than 10 the program
execution will jump back to the label LoopBack where the process will repeat. Eventually the value
of z will be more than 10 and the program will run off the end and terminate.
Note that a FOR loop can do the same thing (and is simpler) so this example is purely designed to
illustrate what the GOTO command can do.
In the past the GOTO command gained a bad reputation. This is because using GOTOs it is possible
to create a program that continuously jumps from one point to another (often referred to as "spaghetti
code") and that type of program is almost impossible for another programmer to understand. With
constructs like the multiline IF statements the need for the GOTO statement has been reduced and it
should be used only when there is no other way of changing the program's flow.
Testing for Prime Numbers
The following is a simple program which brings together many of the programming features
previously discussed.
DO
InpErr:
PRINT
INPUT "Enter a number: "; a
IF a < 2 THEN
PRINT "Number must be equal or greater than 2"
GOTO InpErr
ENDIF
Divs = 0
FOR x = 2 TO SQR(a)
r = a/x


IF r = FIX(r) THEN Divs = Divs + 1
NEXT x
PRINT a " is ";
IF Divs > 0 THEN PRINT "not ";
PRINT "a prime number."
LOOP

This will first prompt (on the console) for a number and, when it has been entered, it will test if that
number is a prime number or not and display a suitable message.
It starts with a DO Loop that does not have a condition – so it will continue looping forever. This is
what we want. It means that when the user has entered a number, it will report if it is a prime number
or not and then loop around and ask for another number. The way that the user can exit the program
(if they wanted to) is by typing the break character (normally CTRL-C).
The program then prints a prompt for the user which is terminated with a semicolon character. This
means that the cursor is left at the end of the prompt for the INPUT command which will get the
number and store it in the variable a.
Following this the number is tested. If it is less than 2 an error message will be printed and the
program will jump backwards and ask for the number again.
We are now ready to test if the number is a prime number. The program uses a FOR loop to step
through the possible divisors testing if each one can divide evenly into the entered number. Each time
it does the program will increment the variable Divs.
Note that the test is done with the function FIX(r) which simply strips off any digits after the decimal
point. So, the condition r = FIX(r) will be true if r is an integer (ie, has no digits after the
decimal point).
Finally, the program will construct the message for the user. The key part is that if the variable Divs
is greater than zero it means that one or more numbers were found that could divide evenly into the
test number. In that case the IF statement inserts the word "not" into the output message.
For example, if the entered number was 21 the user will see this response:
21 is not a prime number.
This is the result of running the program and some of the output:

You can test this program by using the editor (the EDIT command) to enter it.


Using your newly learnt skills you could then have a shot at making it more efficient. For example,
because the program counts how many times a number can be divided into the test number it takes a
lot longer than it should to detect a non prime number. The program would run much more efficiently
if it jumped out of the FOR loop at the first number that divided evenly. You could use the GOTO
command to do this or you could use the command EXIT FOR – that would cause the FOR loop to
terminate immediately.
Other efficiencies include only testing the division with odd numbers (by using an initial test for an
even number then starting the FOR loop at 3 and using STEP 2) or by only using prime numbers for
the test (that would be much more complicated).
Arrays
Arrays are something which you will probably not think of as
useful at first glance but when you do need to use them you will
find them very handy indeed.
An array is best thought of as a row of letterboxes for a block of
units or condos as shown on the right. The letterboxes are all
located at the same address and each box represents a unit or
condo at that address. You can place a letter in the box for unit
one, or unit two, etc.
Similarly an array in BASIC is a single variable with multiple
sub units (called elements in BASIC) which are numbered. You
can place data in element one, or element two, etc. In BASIC an
array is created by the DIM command, for example:
DIM numarr(300)
This creates an array with the name of numarr containing 301 elements (think of them as
letterboxes) ranging from 0 to 300. By default an array will start from zero so this is why there is an
extra element making the total 301. To specify a specific element in the array (ie, a specific letterbox)
you use an index which is simply the number of the array element that you wish to access. For
example, if you want to set element number 100 in this array to (say) the number 876, you would do it
this way:
numarr(100) = 876
Normally the index to an array is not a constant number as in this example (ie, 100) but a variable
which can be changed to access different array elements.
As an example of how you might use an array, consider the case where you would like to record the
maximum temperature for each day of the year and, at the end of the year, calculate the overall
average. You could use ordinary variables to record the temperature for each day but you would need
365 of them and that would make your program unwieldy indeed. Instead, you could define an array
to hold the values like this:
DIM days(365)
Every day you would need to save the temperature in the correct location in the array. If the number of
the day in the year was held in the variable doy and the maximum temperature was held in the
variable maxtemp you would save the reading like this:
days(doy) = maxtemp
At the end of the year it would be simple to calculate the average for the year:
total = 0
FOR i = 1 to 365
total = total + days(i)
NEXT i
PRINT "Average is:" total / 365


This is much easier than adding up and averaging 365 individual variables.
The above array was single dimensioned but you can have multiple
dimensions. Reverting to our analogy of letterboxes, an array with
two dimensions could be thought of as a block of flats with multiple
floors. A block could have a row of four letter boxes for level one,
another row of four boxes for level two, and so on. To place a letter
in a letterbox you need to specify the floor number and the unit
number on that floor.
In BASIC such an array is specified using two indices separated by a
comma. For example:
LetterBox(floor, unit)
As a practical example, assume that you needed to record the maximum temperature for each day over
five years. To do this you could dimension the array as follows:
DIM days(365, 5)
The first index is the day in the year and the second is a number representing the year. If you wanted
to set day 100 in year 3 to 24 degrees you would do it like this:
days(100, 3) = 24
In MMBasic for the PicoMite you can have up to five dimensions (this is different from some other
versions of MMBasic which support eight dimensions). The maximum size of an array is only limited
by the amount of free RAM that is available.
Integers
So far all the numbers and variables that we have been using have been floating point. As explained
before, floating point is handy because it will track digits after the decimal point and when you use
division it will return a sensible result. So, if you just want to get things done and are not concerned
with the details you should stick to floating point.
However, the limitation of floating point is that it stores numbers as an approximation with an
accuracy of 14 digits on the PicoMite . Most times this characteristic of floating point numbers is not
a problem but there are some cases where you need to accurately store larger numbers.
As an example, let us say that you want to manipulate time accurately down to the microsecond so
that you can compare two different date/times to work out which one is earlier. The easy way to do
this is to convert the date/time to the number of microseconds since some date (say 1st Jan in year
zero) - then finding the earliest of the two is just a matter of using an arithmetic compare in an IF
statement.
The problem is that the number of microseconds since that date will exceed the accuracy range of
floating point variables and this is where integer variables come in. An integer variable can accurately
hold very large numbers up to nine million million million (or ±9223372036854775807 to be precise).
The downside of using an integer is that it cannot store fractions (ie, numbers after the decimal point).
Any calculation that produces a fractional result will be rounded up or down to the nearest whole
number when assigned to an integer. However this characteristic can be handy when dealing with
money – for example, you don’t want to send someone a bill for $100.13333333333.
It is easy to create an integer variable, just add the percent symbol (%) as a suffix to a variable name.
For example, sec% is an integer variable. Within a program you can mix integers and floating point
and MMBasic will make the necessary conversions but if you want to maintain the full accuracy of
integers you should avoid mixing the two.
Just like floating point you can have arrays of integers with up to five dimensions, all you need to do
is add the percent character as a suffix to the array name. For example: days%(365, 5).



Beginners often get confused as to when they should use floating point or integers and the answer is
simple… always use floating point unless you need an extremely high level of accuracy in the
resulting number. This does not happen often but when you need them you will find that integers are
a lifesaver.
Strings
Strings are another variable type (like floating point and integers). Strings are used to hold a sequence
of characters. For example, in the command:
PRINT "Hello"
The string "Hello" is a string constant. Note that a constant is something that does not change (as
against a variable, which can) and that string constants are always surrounded by double quotes.
String variables names use the dollar symbol ($) as a suffix to identify them as a string instead of a
normal floating point variable and you can use ordinary assignment to set their value. The following
are examples (note that the second example uses an array of strings):
Car$ = "Holden"
Country$(12) = "India"
Name$ = "Fred"
You can also join strings using the plus operator:
Word1$ = "Hello"
Word2$ = "World"
Greeting$ = Word1$ + " " + Word2$
In which case the value of Greeting$ will be "Hello World".
Strings can also be compared using operators such as = (equals), <> (not equals), < (less than), etc.
For example:
IF Car$ = "Holden" THEN PRINT "Was an Aussie made car"
The comparison is made using the full ASCII character set so a space will come before a printable
character. Also the comparison is case sensitive so 'holden' will not equal "Holden". Using the
function UCASE() to convert the string to upper case you can then have a case insensitive
comparison. For example:
IF UCASE$(Car$) = "HOLDEN" THEN PRINT "Was an Aussie made car"
You can have arrays of strings but you need to be careful when you declare them as you can rapidly
run out of RAM (general memory used for storing variables, etc). This is because MMBasic will by
default allocate 255 bytes of RAM for each element of the array. For example, a string array with 100
elements will by default use 25K of RAM. To alleviate this you can use the LENGTH qualifier to
limit the maximum size of each element. For instance, if you know that the maximum length of any
string that will be stored in the array will be less than 20 characters you can use the following
declaration to allocate just 20 bytes for each element:
DIM MyArray$(100) LENGTH 20
The resultant array will only use 2K of RAM.
Manipulating Strings
String handling is one of MMBasic's strengths and using a few simple functions you can pull apart
and generally manipulate strings. The basic string functions are:
LEFT$(string$, nbr )

Returns a substring of string$ with nbr of characters from the left
(beginning) of the string.

RIGHT$(string$, nbr )

Same as the above but return nbr of characters from the right (end) of
the string.



MID$(string$, pos, nbr )

Returns a substring of string$ with nbr of characters starting from the
character pos in the string (ie, the middle of the string).

For example if S$ = "This is a string"
then:
R$ = LEFT$(S$, 7)
would result in the value of R$ being set to: "This is"
and:
R$ = RIGHT$(S$, 8) would result in the value of R$ being set to: "a string"
finally: R$ = MID$(S$, 6, 2) would result in the value of R$ being set to: "is"
Note that in MID$() the first character position in a string is number 1, the second is number 2 and so
on. So, counting the first character as one, the sixth position is the start of the word "is".
Another useful function is:
INSTR(string$, pattern$ )

Returns a number representing the position at which pattern$ occurs in
string$.

This can be used to search for a string inside another string. The number returned is the position of
the substring inside the main string. Like with MID$() the start of the string is position 1.
For example if S$ = "This is a string"
Then: pos = INSTR(S$, " ")
would result in pos being set to the position of the first space in S$ (ie, 5).
INSTR() can be combined with other functions so this would return the first word in S$:
R$ = LEFT$(S$, INSTR(S$, " ") - 1)
There is also an extended version of INSTR():
INSTR(pos, string$, pattern$ )

Returns a number representing the position at which pattern$
occurs in string$ when starting the search at the character position
pos.

So we can find the second word in S$ using the following:
pos = INSTR(S$, " ")
R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
This last example is rather complicated so it might be worth working through it in detail so that you
can understand how it works.
Note that INSTR() will return the number zero if the sub string is not found and that any string
function will throw an error (and halt the program) if that is used as a character position. So, in a
practical program you would first check for zero being returned by INSTR() before using that value.
For example:
pos = INSTR(S$, " ")
if pos > 0 THEN R$ = LEFT$(S$, INSTR(pos + 1, S$, " ") - 1)
Scientific Notation
Before we finish discussing data types we need to cover off the subject of floating point numbers and
scientific notation.
Most numbers can be written normally, for example 11 or 24.5, but very large or small numbers are
more difficult. For example, it has been estimated that the number of grains of sand on planet Earth is
7500000000000000000. The problem with this number is that you can easily lose track of how many
zeros there are in the number and consequently it is difficult to compare this with a similar sized
number.
A scientist would write this number as 7.5 x 1018 which is called scientific notation and is much easier
to comprehend.
MMBasic will automatically shift to scientific notation when dealing with very large or small floating
point numbers. For example, if the above number was stored in a floating point variable the PRINT



command would display it as 7.5E+18 (this is BASIC’s way of representing 7.5 x 1018). As another
example, the number 0.0000000456 would display as 4.56E-8 which is the same as 4.56 x 10-8.
You can also use scientific notation when entering constant numbers in MMBasic. For example:
SandGrains = 7.5E+18
MMBasic only uses scientific notation for displaying floating point numbers (not integers). For
instance, if you assigned the number of grains of sand to an integer variable it would print out as a
normal number (with lots of zeros).
DIM Command
We have used the DIM command before for defining arrays but it can also be used to create ordinary
variables. For example, you can simultaneously create four string variables like this:
DIM STRING Car, Name, Street, City
Note that because these variables have been defined as strings using the DIM command we do not
need the $ suffix, the definition alone is enough for MMBasic to identify their type. Similarly, when
you use these variables in an expression you do not need the type suffix: For example:
City = "Sydney"
You can also use the keyword INTEGER to define a number of integer variables and FLOAT to do
the same for floating point variables. This type of notation can similarly be used to define arrays.
For example:
DIM INTEGER seconds(200)
Another method of defining the variables type is to use the keyword AS. For example:
DIM Car AS STRING, Name AS STRING, Street AS STRING
This is the method used by Microsoft (MMBasic tries to maintain Microsoft compatibility) and it is
useful if the variables have different types. For example:
DIM Car AS STRING, Age AS INTEGER, Value AS FLOAT
You can use any of these methods of defining a variable's type, they all act the same.
The advantage of defining variables using the DIM command is that they are clearly defined
(preferably at the start of the program) and their type (float, integer or string) is not subject to
misinterpretation.
You can strengthen this by using the following commands at the very top of your program:
OPTION EXPLICIT
OPTION DEFAULT NONE
The first specifies to MMBasic that all variables must be explicitly defined using DIM before they can
be used. The second specifies that the type of all variables must be specified when they are created.
Why are these two commands important?
The first can help avoid a common programming error which is where you accidently misspell a
variable's name. For example, your program might have the current temperature saved in a variable
called Temp but at one point you accidently misspell it as Tmp. This will cause MMBasic to
automatically create a variable called Tmp and set its value to zero.
This is obviously not what you want and it will introduce a subtle error which could be hard to find,
even if you were aware that something was not right. On the other hand, if you used the OPTION
EXPLICIT command at the start of your program MMBasic would refuse to automatically create the
variable and instead would display an error thereby saving you from a probable headache.
The command OPTION DEFAULT NONE further helps because it tells MMBasic that the
programmer must specifically specify the type of every variable when they are declared. It is easy to


forget to specify the type and allowing MMBasic to automatically assume the type can lead to
unexpected consequences.
For small, quick and dirty programs, it is fine to allow MMBasic to automatically create variables but
in larger programs you should always disable this feature with OPTION EXPLICIT and strengthen it
with OPTION DEFAULT NONE.
When a variable is created it is set to zero for float and integers and an empty string (ie, contains no
characters) for a string variable. You can set its initial value to something else when it is created using
DIM. For example:
DIM FLOAT nbr = 12.56
DIM STRING Car = "Ford", City = "Perth"
You can also initialise arrays by placing the initialising values inside brackets like this:
DIM s$(2) = ("zero", "one", "two")
Note that because arrays start from zero by default this array actually has three elements with the
index numbers of 0, 1 and 2. This is why we needed three string constants to initialise it.
Constants
A common requirement in programming is to define an identifier that represents a value without the
risk of the value being accidently changed - which can happen if variables were used for this purpose.
These are called constants and they can represent I/O pin numbers, signal limits, mathematical
constants and so on.
You can create a constant using the CONST command. This defines an identifier that acts like a
variable but is set to a value that cannot be changed.
For example, if you wanted to check the voltage of a battery connected to pin 31 you could define the
relevant values thus:
CONST BatteryVoltagePin = 31
CONST BatteryMinimum = 1.5
These constants can then be used in the program where they make more sense to the casual reader
than simple numbers.
For example:
SETPIN BatteryVoltagePin, AIN
IF PIN(BatteryVoltagePin) < BatteryMinimum THEN SoundAlarm
It is good programming practice to use constants for any fixed number that represents an important
value. Normally they are defined at the start of a program where they are easy to see and conveniently
located for another programmer to adjust (if necessary).
Subroutines
A subroutine is a block of programming code which is self contained (like a module) and can be
called from anywhere within your program. To your program it looks like a built in MMBasic
command and can be used the same. For example, assume that you need a command that would
signal an error by printing a message on the console. You could define the subroutine like this:
SUB ErrMsg
PRINT "Error detected"
END SUB
With this subroutine embedded in your program all you have to do is use the command ErrMsg
whenever you want to display the message. For example:
IF A < B THEN ErrMsg



The definition of a subroutine can be anywhere in the program but typically it is at the end. If
MMBasic runs into the definition while running your program it will simply skip over it.
The above example is fine enough but it would be better if a more useful message could be displayed,
one that could be customised every time the subroutine was called. This can be done by passing a
string to the subroutine as an argument (sometimes called a parameter).
In this case the definition of the subroutine would look like this:
SUB ErrMsg Msg$
PRINT "Error: " + Msg$
END SUB
Then, when you call the subroutine, you can supply the string to be printed on the command line of
the subroutine.
For example:
IF A < B THEN ErrMsg "Number too small"
When the subroutine is called like this the message "Error: Number too small" will be
printed on the console. Inside the subroutine Msg$ will have the value of "Number too small" when
called like this and it will be concatenated in the PRINT statement to make the full error message.
A subroutine can have any number of arguments which can be float, integer or string with each
argument separated by a comma.
Within the subroutine the arguments act like ordinary variables but they exist only within the
subroutine and will vanish when the subroutine ends. You can have variables with the same name in
the main program and they will be hidden within the subroutine and be different from arguments
defined for the subroutine.
The type of the argument to be supplied can be specified with a type suffix (ie, $, % or ! for string,
integer and float). For example, in the following the first argument must be a string and the second an
integer:
SUB MySub Msg$, Nbr%
…
END SUB
MMBasic will convert the supplied values if it can, so if your program supplied a floating point value
as the second argument MMBasic will convert it to an integer. If MMBasic cannot convert the value
it will display an error and return to the command prompt. For example, if you supplied a string for
the second argument your program will stop with an error.
You do not have to use the type suffixes, you can instead define the type of the arguments using the
AS keyword similar to the way it is used in the DIM command.
For example, the following is identical to the above example:
SUB MySub Msg AS STRING, Nbr AS INTEGER
…
END SUB
Of course, if you used only one variable type throughout the program and used OPTION DEFAULT
to set that type you could ignore the question of variable types completely.
When a subroutine is called with an argument that is a variable (ie, not a constant or expression)
MMBasic will create a corresponding variable within the subroutine that points back to this variable.
Any changes to the variable representing the argument inside the subroutine will also change the
variable used in the call. This is called passing arguments by reference.



This is best explained by example:
DIM MyNumber = 5
CalcSquare MyNumber
PRINT MyNumber
END
SUB CalcSquare nbr
nbr = nbr * nbr
END SUB

‘ set the variable to 5
‘ the subroutine will square its value
‘ this will print the number 25

‘ square the argument and pass it back

The subroutine CalcSquare will take its argument, square it and write it back to the variable
representing the argument (nbr). Because the subroutine was called with a variable (MyNumber) the
variable nbr will point back to MyNumber and any change to nbr will also change MyNumber
accordingly. As a result the PRINT statement will output 25.
Passing arguments by reference is handy because it allows a subroutine to pass values back to the
code that called it. However it could lead to trouble if a subroutine used the variable representing an
argument as a general purpose variable and changed its value. Then, if it were called with a variable as
an argument, that variable would be inadvertently changed. For this reason you should avoid
manipulating variables representing arguments inside a subroutine, instead assign the value to a
local variable (see below) and manipulate that instead.
When you call a subroutine you can omit some (or all) of the parameters and they will take the value
of zero (for floats or integers) or an empty string. This is handy as your subroutine can tell if a
parameter is missing and act accordingly.
For example, here is our subroutine to generate an error message but this version can be used without
specifying an error message as a parameter:
SUB ErrMsg Msg$
IF Msg$ = "" THEN
PRINT "Error detected"
ELSE
PRINT "Error: " + Msg$
ENDIF
END SUB
Within a subroutine you can use most features of MMBasic including calling other subroutines,
IF…THEN commands, FOR…NEXT loops and so on. However, one thing that you cannot do is
jump out of a subroutine using GOTO (if you do the result will be undefined and may cause your hair
to turn grey).
Normally the subroutine will exit when the END SUB command is reached but you can also terminate
the subroutine early by using the EXIT SUB command.

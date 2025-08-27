# Options

This table lists the various option commands which can be used to configure MMBasic and change the way it
operates. Options that are marked as permanent will be saved in non-volatile memory and automatically
restored when the PicoMite firmware is restarted. Options that are not permanent will be reset on start-up, reset
and in many cases when a program is run and/or exited.

Many `OPTION` commands will force a restart of the PicoMite firmware and that will cause the USB console
interface to be reset. The program in memory will not be lost as it is held in non-volatile flash memory.


## OPTION LIST

This will list the settings of any options that have been changed from their default setting and are the permanent type. OPTION LIST also shows the version number and which firmware is loaded.

*This command must be run at the command prompt (not in a program).*


## OPTION PIN nbr

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

*This command must be run at the command prompt (not in a program).*


## OPTION DISK SAVE fname$<br>OPTION DISK LOAD fname$

These commands let the user save and restore the complete set of options defined to and from a disk file. The file could then be transferred to a host computer using `XMODEM` allowing additional devices to be easily configured or options recovered after a firmware upgrade.


## OPTION RESET

Reset all saved options to their default values.

*This command must be run at the command prompt (not in a program).*


## OPTION RESET cfg <br> OPTION RESET LIST

Reset all options to default values for the configuration `cfg`.

`OPTION RESET LIST` will list all available configurations.

*This command must be run at the command prompt (not in a program).*
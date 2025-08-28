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


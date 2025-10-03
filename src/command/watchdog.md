.wip


### WATCHDOG timeout or

Starts the watchdog timer which will automatically restart the processors when it has timed out. This can be used to recover from some event that disabled the running program (such as an endless loop or a programming or other error that

### WATCHDOG OFF or

halts a running program). This can be important in an unattended control situation.

### WATCHDOG HW timeout or

The timeout can either be processed in the system timer interrupt (WATCHDOG command) or as a true CPU/hardware watchdog

### WATCHDOG HW OFF

(WATCHDOG HW command). If the hardware watchdog is used the timer has a maximum of 8.3 seconds. No such limitation exists for the software watchdog. 'timeout' is the time in milliseconds (ms) before a restart is forced. This command should be placed in strategic locations in the running BASIC program to constantly reset the watchdog timer (to ‘timeout’) and therefore prevent it from counting down to zero. If the timer count does reach zero (perhaps because the BASIC program has stopped running) the PicoMite firmware will be automatically restarted and the automatic variable MM.WATCHDOG will be set to true (i.e. 1) indicating that an error occurred. On a normal startup MM.WATCHDOG will be set to false (i.e. 0). Note that OPTION AUTORUN must be specified for the program to restart. WATCHDOG OFF can be used to disable the watchdog timer (this is the default on a reset or power up). The timer is also turned off when the break character (CTRL-C) is used on the console to interrupt a running program.
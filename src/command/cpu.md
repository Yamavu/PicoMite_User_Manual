.wip


### CPU RESTART

Will force a restart of the processors. This will clear all variables and reset everything (eg, timers, COM ports, I²C, etc) similar to a power up situation but without the power up banner. If OPTION AUTORUN has been set the program in the specified flash location or program memory will restart.

### CPU SLEEP n

Will cause the processors to sleep for ‘n’ seconds. Note that the CPU does not have a true low power sleep so the power saving is limited.
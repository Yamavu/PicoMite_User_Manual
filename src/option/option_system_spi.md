## OPTION SYSTEM SPI CLKpin, MOSIpin, MISOpin <br> OPTION SYSTEM SPI DISABLE

Specify or disable the SPI port and pins for use by system devices (SD Card, LCD panel, etc).

The PicoMite firmware uses a specific hardware SPI port for system devices, leaving the other for the user. This command specifies which pins are to be used, and hence which of the SPI ports is to be used. The pins allocated to the `SYSTEM SPI` will not be available to other MMBasic commands.

*This command must be run at the command prompt (not in a program).*


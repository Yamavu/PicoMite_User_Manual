# OPTION SDCARD CSpin [,CLKpin, MOSIpin, MISOpin] <br> OPTION SDCARD DISABLE

Specify or disable the I/O pins to use for the SD Card interface.

If the optional pins are not specified the SD Card will use the pins specified by `OPTION SYSTEM SPI`.

Note: The pins specified by OPTION SYSTEM SPI must be a valid set of hardware SPI pins (SPI or SPI2), however, the pins specified by `OPTION SDCARD` can be any pins. The pins specified by `OPTION SYSTEM SPI` and `OPTION SDCARD` cannot be the same.

*This command must be run at the command prompt (not in a program).*


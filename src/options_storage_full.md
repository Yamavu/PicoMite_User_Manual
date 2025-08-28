# Storage

These Options relate to storage 


## OPTION SDCARD CSpin [,CLKpin, MOSIpin, MISOpin] <br> OPTION SDCARD DISABLE

Specify or disable the I/O pins to use for the SD Card interface.

If the optional pins are not specified the SD Card will use the pins specified by `OPTION SYSTEM SPI`.

Note: The pins specified by OPTION SYSTEM SPI must be a valid set of hardware SPI pins (SPI or SPI2), however, the pins specified by `OPTION SDCARD` can be any pins. The pins specified by `OPTION SYSTEM SPI` and `OPTION SDCARD` cannot be the same.

*This command must be run at the command prompt (not in a program).*


## OPTION SDCARD COMBINED CS

This specifies that the touch chip select pin is also used for the SDcard.

In this case external circuitry is needed to implement the SD chip select.

See “SD Cards” in the chapter “Program and Data Storage”.


## OPTION MODBUFF ENABLE/DISABLE [sizeinK]

Creates or removes an area of flash memory used for loading and playing .MOD files. If enabled then a mod buffer is created with a size of 128Kbytes. This can be overridden with `sizeinK`.

- This option reserves part of the Flash Filesystem (ie, it shrinks the Flash Filesystem). The default is disabled.
- This option is not required on an RP2350 with PSRAM enabled. In this case the MOD file will be loaded to space in the PSRAM.



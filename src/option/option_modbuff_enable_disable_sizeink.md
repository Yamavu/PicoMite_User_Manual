## OPTION MODBUFF ENABLE/DISABLE [sizeinK]

Creates or removes an area of flash memory used for loading and playing .MOD files. If enabled then a mod buffer is created with a size of 128Kbytes. This can be overridden with `sizeinK`.

- This option reserves part of the Flash Filesystem (ie, it shrinks the Flash Filesystem). The default is disabled.
- This option is not required on an RP2350 with PSRAM enabled. In this case the MOD file will be loaded to space in the PSRAM.



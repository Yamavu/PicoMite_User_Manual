## OPTION SYSTEM I2C sdapin, sclpin [,SLOW]<br>OPTION SYSTEM I2C sdapin, sclpin [,FAST]

Specify the I²C port and pins for use by system devices (LCD panel, and RTC).

The PicoMite firmware uses a specific I2C port for system devices, leaving the other for the programmer. This command specifies which pins are to be used, and hence which of the I²C ports is to be used.

The pins allocated to the SYSTEM I2C will not be available for other MMBasic SETPIN settings but can be used for additional I²C devices using the standard I2C command. Note: I2C(2) OPEN and I2C(2) CLOSE are not available in this case.

By default the I²C port is opened at a speed of 400KHz and with a 100mSec timeout. The I²C frequency can be set using the optional third parameter which can take the values FAST = 400KHz or SLOW = 100KHz.

*This command must be run at the command prompt (not in a program).*


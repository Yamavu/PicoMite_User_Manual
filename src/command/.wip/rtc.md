

### RTC GETTIME

 RTC GETTIME will get the current date/time from a PCF8563, DS1307 or DS3231 real time clock and set the internal MMBasic clock accordingly. The date/time can then be retrieved with the DATE$ and TIME$ functions.

### RTC SETTIME year, month, day, hour, minute, second

 RTC SETTIME will set the time in the clock chip. 'hour' must use 24 hour notation. ‘year’ can be two or four digits. The RTC SETTIME command will also accept a single string argument in the format of dd/mm/yy hh:mm. This means the date/time could be entered by the user using a GUI FORMATBOX with the DATETIME2 format (see Advanced Graphics Functions.pdf).

### RTC SETREG reg, value

 The RTC SETREG and GETREG commands can be used to set or read the

### RTC GETREG reg, var

 contents of registers within the real time clock chip. 'reg' is the register's number, 'value' is the number to store in the register and 'var' is a variable that will receive the number read from the register. These commands are not necessary for normal operation but they can be used to manipulate special features of the chip (alarms, output signals, etc). They are also useful for storing temporary information in the chip's battery backed RAM. These chips are I2C devices and must be connected to the two I2C pins as specified by OPTION SYSTEM I2C with appropriate pullup resistors. Also see the command OPTION RTC AUTO ENABLE.
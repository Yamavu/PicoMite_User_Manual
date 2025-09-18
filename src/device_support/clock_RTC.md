## Real Time Clock Interface

Using the RTC GETTIME command it is easy to get the current time from a PCF8563, DS1307, DS3231 or DS3232 real time clock as well as compatible devices such as the M41T11. These integrated circuits are popular and cheap, will keep accurate time even with the power removed and can be purchased for US$2 to $8 on eBay. Complete modules including the battery can also be purchased on eBay for a little more.

The PCF8563 and DS1307 will keep time to within a minute or two over a month while the DS3231 and DS3232 are particularly precise and will remain accurate to within a minute over a year.

These chips are I²C devices and should be connected to the I²C I/O pins of the Raspberry Pi Pico.

Internal pullup resistors (100KΩ) are applied to the I²C I/O pins so, in many cases external resistors are not needed.

In order to enable the RTC you first need to allocate the I²C pins to be used using the command `OPTION SYSTEM I2C SDApin, SCLpin`

The time used by the RTC must also be set. That is done with the RTC SETTIME command which uses the format `RTC SETTIME year, month, day, hour, minute, second` (Note that the hour must be in 24 hour format).

For example, the following will set the real time clock to 4PM on the 10th November 2025:

```basic
RTC SETTIME 2025, 11, 10, 16, 0, 0 
```

To get the time you use the RTC GETTIME command which will read the time from the real time clock chip and set the clock inside the Raspberry Pi Pico. Normally this command will be placed at the beginning of the program or in the subroutine MM.STARTUP so that the time is set on power up.

The command OPTION RTC AUTO ENABLE can also be used to set an automatic update of the TIME$ and DATE$ read only variables from the real time clock chip on boot and every hour.


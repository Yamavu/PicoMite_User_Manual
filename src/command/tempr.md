### TEMPR START pin [, precision] [,timeout]

This command can be used to start a conversion running on a DS18B20 temperature sensor connected to 'pin'. 

Normally the [TEMPR()](../function/tempr.md) function alone is sufficient to make a temperature measurement so usage of this command is optional.

For more detail see the section Measuring Temperature. This command will start the measurement on the temperature sensor. The program can then attend to other duties while the measurement is running and later use the `TEMPR()` function to get the reading. If the `TEMPR()` function is used before the conversion time has completed the function will wait for the remaining conversion time before returning the value.

Any number of these conversions (on different pins) can be started and be running simultaneously. 'precision' is the resolution of the measurement and is optional. It is a number between 0 and 3 meaning:

- 0 = 0.5ºC resolution, 100 ms conversion time.
- 1 = 0.25ºC resolution, 200 ms conversion time (this is the default).
- 2 = 0.125ºC resolution, 400 ms conversion time.
- 3 = 0.0625ºC resolution, 800 ms conversion time.

The optional timeout parameter overrides the conversion times above to allow for slow devices.

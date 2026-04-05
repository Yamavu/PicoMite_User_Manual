### TEMPR( pin [,timeout])

Return the temperature measured by a DS18B20 temperature sensor connected
to `pin` (which does not have to be configured).

The returned value is degrees C with a default resolution of 0.25ºC. If there is
an error during the measurement the returned value will be 1000.

The time required for the overall measurement is 200ms and interrupts will be
ignored during this period.

The optional parameter timeout can be used to override the default (200mSec)
to allow for slow devices.

Alternatively the TEMPR START command can be used to start the
measurement and your program can do other things while the conversion is
progressing. When this function is called the value will then be returned
instantly assuming the conversion period has expired. If it has not, this
function will wait out the remainder of the conversion time before returning the
value.

The DS18B20 can be powered separately by a 3V to 5V supply or it can
operate on parasitic power from the Raspberry Pi Pico.

See the chapter Special Hardware Devices for more details.


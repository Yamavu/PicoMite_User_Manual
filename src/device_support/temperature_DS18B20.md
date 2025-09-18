## Measuring Temperature

<div style="float: right; margin-left: 20px;">
  <img src="../img/12_temp_circuit.png" alt="DS18B20 circuit example" width="250"><br>
  <img src="../img/12_temp_parasitic_circuit.png" alt="DS18B20 circuit example" width="250">
</div>

The TEMPR() function will get the temperature from a DS18B20 3.3V temperature sensor. This device can be purchased on eBay for about 4.7K US$5 in a variety of packages including a waterproof probe version.

The DS18B20 can be powered separately by a 3.3V supply or it can Any PicoMite operate on parasitic power from the Raspberry Pi Pico as shown on the I/O Pin right. Multiple sensors can be used but a separate I/O pin and a 4.7K pullup resistor is required for each one.

Normal Power To get the current temperature you just use the TEMPR() function in an expression. For example, `PRINT "Temperature: " TEMPR(pin)`

Where `pin` is the I/O pin to which the sensor is connected. You do not have to configure the I/O pin, that is handled by MMBasic.

3.3V The returned value is in degrees C with a resolution of 0.25 ºC and is 4.7K accurate to ±0.5 ºC. If there is an error during the measurement the returned value will be 1000.

Any PicoMite The time required for the overall measurement is 200ms and the running I/O Pin program will halt for this period while the measurement is being made.

This also means that interrupts will be disabled for this period. If you do Parasitic Power not want this you can separately trigger the conversion using the TEMPR START command then later use the TEMPR() function to retrieve the temperature reading. The TEMPR() function will always wait if the sensor is still making the measurement.<br style="clear:both" />

For example:
```basic
TEMPR START GP15
< do other tasks >
PRINT "Temperature: " TEMPR(GP15)
```

The TEMPR START command can also be used to change the resolution of the measurement (from the default 0.25 ºC) and the associated conversion time.


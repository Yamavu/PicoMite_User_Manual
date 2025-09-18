## WS2812 multicolour LED

The PicoMite firmware has built in support for the WS2812 multicolour LED chip. This chip needs a very specific timing to work properly and with the DEVICE WS2812 command it is easy to control these devices with minimal effort.

This command will output the required signals needed to drive a chain of WS2812 LED chips connected to the pin specified and set the colours of each LED in the chain. The syntax of the command is:
`WS2812 type, pin, nbr%, colours%[()]`

Note that the pin must be set to a digital output before this command is used. The colours%() array should be sized to have at least the same number of elements as the number of LEDs to be driven (nbr%). Each element in the array should contain the colour in the normal RGB888 format (0 - HFFFFFF). Where a single LED is to be driven then colours% should be a simple variable.

Up to 256 WS2812 chips in a string are supported.

`type` is a single character specifying the type of chip being driven as follows:
- `O` = original WS2812
- `B` = WS2812B
- `S` = SK6812 
- `W` = SK6812W (RGBW)

As an example:

```basic
DIM b%(4)=(RGB(red), Rgb(green), RGB(blue), RGB(Yellow), rgb(cyan))
SETPIN GP5, DOUT
WS2812 O, GP5, 5, b%()
```

will output the specified colours to an array of five WS2812 LEDs daisy chained off pin GP5.

It is possible that a WS2812 will not work reliably with the 3.3V output from the Raspberry Pi Pico. In this case there are a number of solutions:

* Use the WS2812B which will work with a 3.3V supply and inputs.
* Use the Raspberry Pi Pico 2 which can tolerate 5V (while powered) so, in this case, level shifting is not required..
* Use a single WS2812 powered from 3.3V as a first stage to buffer the input of the first "real" LED in the string.<br>
The minimum supply for the WS2812 is 4V but in many cases it will work at 3.3V.

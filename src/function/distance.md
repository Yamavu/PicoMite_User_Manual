### DISTANCE( trigger, echo ) or DISTANCE( trig-echo )

Measure the distance to a target using the HC-SR04 ultrasonic distance sensor.

Four pin sensors have separate trigger and echo connections. `trigger` is the I/O
pin connected to the "trig" input of the sensor and `echo` is the pin connected to
the "echo" output of the sensor.

Three pin sensors have a combined trigger and echo connection and in that case
you only need to specify one I/O pin to interface to the sensor.

Note that the HC-SR04 is a 5V device so level shifting will be required on Pico
(RP2040) processors but not on Pico 2 (RP2350) processors.

The I/O pins are automatically configured by this function and multiple sensors
can be used on different I/O pins.

The value returned is the distance in centimetres to the target or -1 if no target
was detected or -2 if there was an error (i.e. sensor not connected).


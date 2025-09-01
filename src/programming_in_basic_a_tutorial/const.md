## Constants

A common requirement in programming is to define an identifier that represents a value without the
risk of the value being accidently changed - which can happen if variables were used for this purpose.

These are called constants and they can represent I/O pin numbers, signal limits, mathematical
constants and so on.

You can create a constant using the `CONST` command. This defines an identifier that acts like a
variable but is set to a value that cannot be changed.

For example, if you wanted to check the voltage of a battery connected to pin 31 you could define the
relevant values thus:

```basic
CONST BatteryVoltagePin = 31
CONST BatteryMinimum = 1.5
```

These constants can then be used in the program where they make more sense to the casual reader
than simple numbers. For example:

```basic
SETPIN BatteryVoltagePin, AIN
IF PIN(BatteryVoltagePin) < BatteryMinimum THEN SoundAlarm
```

It is good programming practice to use constants for any fixed number that represents an important
value. Normally they are defined at the start of a program where they are easy to see and conveniently
located for another programmer to adjust (if necessary).


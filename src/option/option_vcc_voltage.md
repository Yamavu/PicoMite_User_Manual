## OPTION VCC voltage

Specifies the voltage (Vcc) supplied to the Raspberry Pi Pico.

When using the ADC pins to measure voltage the PicoMite firmware uses the voltage on the pin marked VREF as its reference. This voltage can be accurately measured using a DMM and set using this command for more accurate measurement.

The parameter is not saved and should be initialised either on the command line or in a program. The default if not set is `3.3`.


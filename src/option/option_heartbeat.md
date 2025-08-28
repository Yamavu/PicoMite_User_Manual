## OPTION HEARTBEAT ON/OFF [HEARTBEATpin]

Enables or disables the output of the heartbeat LED.

In the case of the Pico-W the heartbeat is on a pin controlled by the CWY43 chip.

*NOT WEBMITE VERSION*

By default, for RP2350A chips the heartbeat is enabled on GP25. If it is disabled the program can control the LED via GP25.

For RP2350B chips the heartbeat is not enabled.

If the heartbeat is disabled then the command can be used both to enable it and optionally specify the pin to use (default GP25)


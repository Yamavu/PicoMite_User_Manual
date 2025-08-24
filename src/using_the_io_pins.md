# Using the I/O pins
Using the I/O pins
The Raspberry Pi Pico has 26 input/output pins which can be controlled from within the BASIC program with 3
of these supporting a high speed ADC (Analog to Digital Converter).
An I/O pin is referred to by its pin number and this can be the number (eg,, 2) or its GP number (eg,, GP1).

Digital Inputs
A digital input is the simplest type of input configuration. If the input voltage is higher than 2.5V the logic
level will be true (numeric value of 1) and anything below 0.65V will be false (numeric value of 0). The inputs
use a Schmitt trigger input so anything in between these levels will retain the previous logic level.
Note that the maximum voltage on the RP2040 (ie, the Raspberry Pi Pico) I/O pins is 3.3V. Level shifting will
be required if a device uses 5V levels for signalling. The Raspberry Pi Pico 2 using the RP2350 can tolerate 5V
(while powered) so, in this case, level shifting is not required for signals up to 5V.
In your BASIC program you would set the input as a digital input and use the PIN() function to get its level.
For example:
SETPIN GP4, DIN
IF PIN(GP4) = 1 THEN PRINT "High"
The SETPIN command configures pin GP4 as a digital input and the PIN() function will return the value of that
pin (the number 1 if the pin is high). The IF command will then execute the command after the THEN
statement if the input was high. If the input pin was low the program would just continue with the next line in
the program.
The SETPIN command also recognises a couple of options that will connect an internal resistor from the input
to either the supply or ground. This is called a "pullup" or "pulldown" resistor and is handy when connecting to
a switch as it saves having to install an external resistor to place a voltage across the contacts. Due to a
hardware issue with the RP2350 processor it is recommended that an external resistor of 8,2K or less be used if
a pulldown is required on that processor.

Analog Inputs
Pins marked as ADC can be configured to measure the voltage on the pin. The input range is from zero to 3.3V
and the PIN() function will return the voltage. For example:
> SETPIN 31, AIN
> PRINT PIN(31)
2.345
>
You will need a voltage divider if you want to measure voltages greater than 3.3V. For small voltages you may
need an amplifier to bring the input voltage into a reasonable range for measurement.
The measurement uses 3.3V power supply to the CPU as its reference and it is assumed that this is exactly
3.3V. This value can be changed with the OPTION VCC command. In order to get the best possible reading,
the analogue input is sampled 10 times. The values are then sorted and the top 2 and bottom 2 discarded and the
remaining 6 averaged.
If you want the direct reading from the ADC you can use the raw mode by using the ARAW option to the
SETPIN command:
SETPIN pinno,ARAW

In this case a value between 0 and 4095 will be returned based on a single sample.
The ADC commands provide an alternate method of recording analog inputs and are intended for high speed
recording of many readings into an array.

Counting Inputs
Any four pins can be used as counting inputs to measure frequency, period or just count pulses on the input.
The pins used for this function can be configured using the OPTION COUNT command but, if not changed,
will default to GP6, GP7, GP8 and GP9.

PicoMite User Manual

Page 45

As an example, the following will print the frequency of the signal on pin GP7:
> SETPIN GP7, FIN
> PRINT PIN(GP7)
110374
>
In this case the frequency is 110.374 kHz.
By default the gate time is one second which is the length of time that MMBasic will use to count the number
of cycles on the input and this means that the reading is updated once a second with a resolution of 1 Hz. By
specifying a third argument to the SETPIN command it is possible to specify an alternative gate time between
10 ms and 100000 ms. Shorter times will result in the readings being updated more frequently but the value
returned will have a lower resolution. The PIN() function will always scale the returned number as the
frequency in Hz regardless of the gate time used.
For example, the following will set the gate time to 10ms with a corresponding loss of resolution:
> SETPIN GP7, FIN, 10
> PRINT PIN(GP7)
110300
>
For accurate measurement of signals less than 10 Hz it is generally better to measure the period of the signal.
When set to this mode the PicoMite firmware will measure the number of milliseconds between sequential
rising edges of the input signal. The value is updated on the low to high transition so if your signal has a period
of (say) 100 seconds you should be prepared to wait that amount of time before the PIN() function will return
an updated value.
The count pins can also count the number of pulses on their input. When a pin is configured as a counter (for
example, SETPIN 7,CIN) the counter will be reset to zero and PicoMite firmware will then count every
transition from a low to high voltage. The counter can be reset to zero again by executing PIN(7) = 0.
Counting inputs are accurate up to about 200KHz at the default processors frequency. A minimum pulse width
of about 40nS is needed to trigger the counter. The RP2350 also has the option of configuring GP1 as an
extremely fast frequency counting pin (see the SETPIN GP1, FFIN command)..

Digital Outputs
All I/O pins can be configured as a digital output using the DOUT parameter to the SETPIN command. For
example:
SETPIN GP15, DOUT
This means that when an output pin is set to logic low it will pull its output to zero and when set high it will
pull its output to 3.3V. In MMBasic this is done with the PIN command. For example PIN(GP15) = 0
will set pin GP15 to low while PIN(GP15) = 1 will set it high.

Pulse Width Modulation
The PWM (Pulse Width Modulation) command allows the PicoMite firmware to generate square waves with a
program controlled duty cycle.
By varying the duty cycle you can generate a program controlled voltage output for use in controlling external
devices that require an analog input (power supplies, motor controllers, etc). The PWM outputs are also useful
for driving servos and for generating a sound output via a small transducer.
RP2040 The PWM outputs consists of up to 8 channels (numbered 0 to 7) with each channel having two
outputs (A and B). For each channel the frequency can be selected and for each output a different
duty cycle can be set. Up to 16 pins can be configured as PWM outputs using the SETPIN
command.
RP2350 The RP2350 supports up to 12 PWM channels numbered 0 to 11) and up to 24 pins can be
configured as PWM outputs using the SETPIN command.

Communications Interfaces (Serial, SPI and I2C)
These are described in the appendices at the rear of this manual. Before these interfaces can be used the pins
that are to be used for the relevant signals must be configured using the SETPIN command.

Page 46

PicoMite User Manual

Some devices such as an SD Card, LCD panels, touch, etc also use SPI or I2C interfaces and the pins used for
these must similarly be configured using the OPTION SYSTEM command before they can be used.

Interrupts
Interrupts are a handy way of dealing with an event that can occur at an unpredictable time. An example is
when the user presses a button. In your program you could insert code after each statement to check to see if
the button has been pressed but an interrupt makes for a cleaner and more readable program.
When an interrupt occurs MMBasic will execute a defined subroutine and when finished return to the main
program. The main program is completely unaware of the interrupt and will carry on as normal.
Any I/O pin that can be used as a digital input can be configured to generate an interrupt using the SETPIN
command with up to ten interrupts active at any one time. Interrupts can be set up to occur on a rising or falling
digital input signal (or both) and will cause an immediate branch to the specified user defined subroutine. The
target can be the same or different for each interrupt. Return from an interrupt is via the END SUB or EXIT
SUB commands. Note that no parameters can be passed to the subroutine however within the interrupt calls to
other subroutines and functions are allowed.
If two or more interrupts occur at the same time they will be processed in order of the interrupts as defined
below. During the processing of an interrupt all other interrupts are disabled until the interrupt subroutine
returns. During an interrupt (and at all times) the value of the interrupt pin can be accessed using the PIN()
function.
Interrupts can occur at any time but they are disabled during INPUT statements. Also interrupts are not
recognised during some long hardware related operations (eg, the TEMPR() function, LCD drawing
commands, and SD access commands) although they will be recognised if they are still present when the
operation has finished. When using interrupts the main program is completely unaffected by the interrupt
activity unless a variable used by the main program is changed during the interrupt.
Because interrupts run in the background they can cause difficult to diagnose bugs. Keep in mind the following
factors when using interrupts:
 Interrupts are only checked by MMBasic at the completion of each command, and they are not latched by
the hardware. This means that an interrupt that lasts for a short time can be missed, especially when the
program is executing commands that take some time to execute. Most commands will execute in under
15µs however some commands such as the TEMPR() function can take up to 200ms so it is possible for
an interrupt to occur and vanish within this window and thus not be recognised.


When inside an interrupt all other interrupts are blocked so your interrupts should be short and exit as
soon as possible. For example, never use PAUSE inside an interrupt. If you have some lengthy
processing to do you should simply set a flag and immediately exit the interrupt, then your main program
loop can detect the flag and do whatever is required.



The subroutine that the interrupt calls (and any other subroutines or functions called by it) should always
be exclusive to the interrupt. If you must call a subroutine that is also used by an interrupt you must
disable the interrupt first (you can reinstate it after you have finished with the subroutine).



Remember to disable an interrupt when you have finished needing it – background interrupts can cause
strange and non-intuitive bugs.

In addition to interrupts generated by the change in state of an I/O pin, an interrupt can also be generated by
other sections of MMBasic including timers and communications ports and the above notes also apply to them.
The list of all these interrupts (in high to low priority ranking) is:
1. PID control loops
2. ON KEY individual
3. ON KEY general
4. ON PS2
5. PIO RX FIFO
6. PIO TX FIFO
7. PIO RX DMA completion
8. PIO TX DMA completion
9. GUI Int Down
10. GUI Int Up
11. Sprite collision

PicoMite User Manual

Page 47

12. WebMite: TCP receive
13. WebMite: MQTT compete
14. WebMite: UDP receive
15. USB Game Controller/USB or PS2 Mouse/Wii controller
16. ADC completion
17. I2C Slave Rx
18. I2C Slave Tx
19. I2C2 Slave Rx
20. I2C2 Slave Tx
21. WAV Finished
22. COM1: Serial Port
23. COM2: Serial Port
24. IR Receive
25. Keypad
26. Interrupt command/CSub Interrupt
27. I/O Pin Interrupts in order of definition
28. Tick Interrupts (1 to 4 in that order)
As an example: If an ON KEY interrupt occurred at the same time as a COM1: interrupt the ON KEY interrupt
subroutine would be executed first and then, when the interrupt subroutine finished, the COM1: interrupt
subroutine would then be executed.

Page 48

PicoMite User Manual
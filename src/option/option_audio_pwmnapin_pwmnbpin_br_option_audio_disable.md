# OPTION AUDIO PWMnApin, PWMnBpin <br> OPTION AUDIO DISABLE

Configures one of the PWM channels as an audio output.

`PWMnApin` is the left audio channel, `PWMnBpin` is the right. Both pins must belong to the same audio channel.

Example, `OPTION AUDIO GP18, GP19` would use `PWM1A` and `PWM1B` on pins 24 and 25 respectively.

This option prevents use of these pins in the BASIC program. The audio output is generated using PWM so a low pass filter is
necessary on the output. The audio output from the Raspberry Pi Pico is very noisy. Using OPTION POWER and/or supplying power via a separate 3.3V linear regulator can reduce this.

*This command must be run at the command prompt (not in a program).*


# Audio

#Permanent


## OPTION AUDIO PWMnApin, PWMnBpin <br> OPTION AUDIO DISABLE

Configures one of the PWM channels as an audio output.

`PWMnApin` is the left audio channel, `PWMnBpin` is the right. Both pins must belong to the same audio channel.

Example, `OPTION AUDIO GP18, GP19` would use `PWM1A` and `PWM1B` on pins 24 and 25 respectively.

This option prevents use of these pins in the BASIC program. The audio output is generated using PWM so a low pass filter is
necessary on the output. The audio output from the Raspberry Pi Pico is very noisy. Using OPTION POWER and/or supplying power via a separate 3.3V linear regulator can reduce this.

*This command must be run at the command prompt (not in a program).*


## OPTION AUDIO SPI CSpin, CLKpin, MOSIpin <br> OPTION AUDIO DISABLE

Configures  the audio output to be directed to a MCP48n2 DAC connected to the specified pins. The LDAC pin on the DAC should be
connected to GND. 


## OPTION AUDIO VS1053 CLKpin, MOSIpin, MISOpin, XCSpin, XDCSpin, DREQpin, XRSTpin <br> OPTION AUDIO DISABLE

Configures the audio output to be directed to a VS1053 CODEC. This allows MP3 and MIDI playback in addition to the other formats
supported and also supports real-time MIDI output. See the `PLAY` command for more details


## OPTION AUDIO I2S BCLKpin, DINpin <br> OPTION AUDIO DISABLE

Configures the audio output to be directed to an I2S DAC connected to the specified pins. The LRCK pin on the DAC should be connected to the next consecutive GPIO pin to BCLKpin.

Configures the audio output to be directed to an I2S DAC connected to the specified pins. The LRCK pin on the DAC should be connected to


## OPTION FAST AUDIO ON|OFF

When using the `PLAY SOUND` command, changes to sounds, volumes, or frequencies can cause audible clicks in the output. The firmware attempts to mitigate this by ramping the volume down on the channel’s previous output before changing the output and ramping it back up again. This significantly improves the audio output but at the expense of a short delay in the `PLAY SOUND` command (worst case 3mSec). This delay can be avoided using OPTION FAST AUDIO ON in a program.

The audible clicks may then re-appear but this is at the programmer’s discretion.

This is a temporary option that is reset to `OFF` whenever a program is run.



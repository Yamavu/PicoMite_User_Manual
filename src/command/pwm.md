.wip


### PWM channel, frequency, [dutyA] [,dutyB][,phase][,defer]

There are 8 separate PWM frequencies available (channels 0 to 7) and up to 16 outputs with individually controlled duty cycle. You can output on either PWMnA or PWMnB or both for each channel - no restriction. Duty cycles are specified as a percentage and you can use a negative value to invert the output (-100.0 <= duty <=100.0). To use just channel B use the syntax: ‘PWM channel, frequency, , dutyB’ - note the double comma before the required duty cycle. Minimum frequency = (cpuspeed + 1) / (2^24) Hz. Maximum speed is OPTION CPUSPEED/4. At very fast speeds the duty cycles will be increasingly limited. Phase is a parameter that causes the waveforms to be centred such that a wave form with a shorter duty cycle starts and ends equal times from a longer one. Use 1 to enable this mode and 0 (or omit) to run as normal The parameter ‘deferredstart’ when set to 1 configures the PWM channels as but does not start the output running. They can the be started using the PWM SYNC command. This can be used to avoid any undesirable startup artefacts The PWM command is also capable of driving servos as follows: PWM 1,50,(position_as_a_percentage * 0.05 + 5)

### PWM SYNC s0 [,s1][,s2][,s3][,s4][,s5][,s6][,s7 ]

This initiates the PWM on channels where a deferred start was defined or just syncs existing running channels. However, the power comes in the ability to offset the channels one to another (defined as a percentage of the time period as per the duty cycle - can be a float) You can use an offset of -1 to omit a channel from the synch

### PWM channel, OFF

Stop output on ‘channel’.
### BACKLIGHT n [ ,DEFAULT | ,FreqInHz ]

*NON VGA OR HDMI VERSIONS*

Sets the display backlight, valid values are 0 to 100. If DEFAULT is specified then the firmware will automatically set the backlight to that level on power-up.

This is particularly useful for battery operation where reducing the backlight level can significantly increase battery life. 

Some circuits are too slow to use the default backlight PWM frequency which is chosen to avoid interference with audio. In which case a user frequency can be specified. 

*This is a temporary option and will need setting on reboot.*

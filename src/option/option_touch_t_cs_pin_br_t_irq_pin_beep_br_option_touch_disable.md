# OPTION TOUCH T_CS pin <br> T_IRQ pin [, Beep] <br> OPTION TOUCH DISABLE

*NOT VGA OR HDMI VERSIONS*

Configures MMBasic for the touch sensitive feature of an attached LCD
panel.

`T_CS pin` and `T_IRQ pin` are the I/O pins to be used for chip select and
touch interrupt respectively (any free pins can be used). The remaining
pins are connected to those specified using the OPTION SYSTEM SPI
command.

`Beep` is an optional pin which can be connected to a small
buzzer/beeper to generate a "click" or beep sound when an Advanced
Graphics control is touched (ie, radio button, switch, etc). This is
described in Advanced Graphics Functions.pdf.

*This command must be run at the command prompt (not in a program).*


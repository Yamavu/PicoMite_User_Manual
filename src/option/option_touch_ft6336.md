## OPTION TOUCH FT6336 IRQpin, RESETpin [,BEEPpin] [,sensitivity]

*NOT VGA OR HDMI VERSIONS*

Enables touch support for FT6336 capacitive touch chip. Sensitivity is a number between `0` and `255` - defaults to `50`, lower is more sensitive.

`SDA` and `SCK` should be connected to valid I2C pins and set up with `OPTION SYSTEM I2C`. See also the `TOUCH` function.


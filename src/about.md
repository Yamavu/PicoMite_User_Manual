PicoMite

User Manual





# PicoMite
**A Raspberry Pi Pico Running the MMBasic BASIC Interpreter**

MMBasic BASIC Interpreter

for the

* Raspberry Pi Pico
* Raspberry Pi Pico 2
* Raspberry Pi Pico W
* Raspberry Pi Pico 2 W
* modules using the RP2040 and RP2350 processors

Ver 6.00.03 
Revision 1
(18 July 2025)

For updates to this manual and more details on MMBasic go to
* [Geoff Graham's PicoMite](http://geoffg.net/picomite.html)
* [MMBasic](http://mmbasic.com)

## About

Peter Mather (matherp on the Back Shed Forum) led the project, ported MMBasic to the Raspberry Pi Pico and
wrote the drivers for its hardware features. The MMBasic interpreter and this manual was written by Geoff
Graham ( http://geoffg.net ). In addition, many others have supported the project with specialised code, testing
and suggestions.


### Support

Support questions should be raised on the Back Shed forum ( http://www.thebackshed.com/forum/Microcontrollers )
where there are many enthusiastic MMBasic users who would be only too happy to help. The developers of the
PicoMite firmware are also regulars on this forum.


### Copyright and Acknowledgments

The PicoMite firmware and MMBasic is copyright 2011-2024 by Geoff Graham and Peter Mather 2016-2024.

1-Wire Support is copyright 1999-2006 Dallas Semiconductor Corporation and 2012 Gerard Sexton.

FatFs (SD Card) driver is copyright 2014, ChaN.

WAV, MP3, and FLAC file support is copyright 2019 David Reid.

JPG support is thanks to Rich Geldreich

The pico-sdk is copyright 2021 Raspberry Pi (Trading) Ltd.

TinyUSB is copyright tinyusb.org

LittleFS is copyright Christopher Haster

Thomas Williams and Gerry Allardice for MMBasic enhancements

The VGA driver code was derived from work by Miroslav Nemecek

The CRC calculations are copyright Rob Tillaart

The compiled object code (the .uf2 file) for the PicoMite firmware is free software: you can use or redistribute it as you please. The source code is on GitHub ( https://github.com/UKTailwind/PicoMiteAllVersions ) and can be freely used subject to some conditions (see the header in the source files).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY, without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


### This Manual

Copyright 2025 Geoff Graham and Peter Mather
The author of this manual is Geoff Graham with input by Peter Mather, Harm de Leeuw, Mick Ames and many
others on The Back Shed forum. It is distributed under a Creative Commons Attribution-NonCommercialShareAlike 3.0 Australia license ([CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/au/))


### This Website

This website is made by Yamavu and distributed under a Creative Commons Attribution-NonCommercialShareAlike 3.0 Australia license ([CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/au/))

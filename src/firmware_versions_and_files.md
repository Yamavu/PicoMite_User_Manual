# Firmware Versions and Files

The PicoMite firmware can be used for two distinctly differing roles depending on the version of the firmware
loaded. These roles are; a self contained computer and an embedded controller:.

### Self Contained Computer

Versions with VGA or HDMI video output are intended for use as a self contained computer. These boot up
and display the output of the BASIC interpreter on the monitor connected to the video output. They are
coupled with a PS2 or USB keyboard and by using the keyboard and video output you can enter and edit a
program, run it, set options, etc.

Because the self contained computer starts by displaying the BASIC command prompt they are often called
“boot to BASIC” computers. They are simple and fun to use and were popular in the 70s and 80s, for example
the Apple II, Tandy TRS-80, Commodore 64 and others.

When a program is running all of its output (text and graphics) is displayed on the video output. The text
output is also sent to the serial console. This is a secondary communications channel using the Raspberry Pi
Pico’s USB connector and is another way of communicating with the MMBasic interpreter using a desktop or
laptop computer. For the details of using this see the next chapter: Serial Console.

## Embedded Controller

Versions of the firmware without a video output are primarily intended for use as an embedded controller. This
is where the Raspberry Pi Pico or Pico 2 is used as the brains inside some device. For example, a burglar
alarm, a heating controller, weather station, etc. Quite often they have an attached touch sensitive LCD panel
for the user to control the device and observe the output.

There is also a version of the firmware that supports the wireless interface on the Raspberry Pi Pico W (and
2 W) and using this you can create an embedded controller which has a miniature web server running on the
Pico and can access the Internet to get the time, send emails, etc.

To enter programs, set options and generally manage the Raspberry Pi Pico as an embedded controller you
use the serial console to connect to a desktop or laptop computer. Unlike the self contained computer
described above, this is the only way to communicate with the BASIC interpreter so it is important that you
can connect to it. For a description of the serial console see the heading Serial Console below.

## Processor Support

The PicoMite firmware supports the original RP2040 processors used in the Raspberry Pi Pico and the newer
RP2350 used in the Raspberry Pi Pico 2. The firmware is also designed to work with modules produced by
other vendors that use the same chips.

The RP2350 comes in four sub versions designated the RP2350A, RP2350B, RP2354A and the RP2354B. The
RP2354A and the RP2354B are not currently supported (although they may be in the future).

The RP2350B is the same as the RP2350A except that it has 18 additional I/O pins (pins GP30 to GP47) which
are automatically made available in MMBasic. Both of these chips are supported by the same PicoMite
firmware and work the same. So, within this manual, all references to the RP2350 apply equally to both the A
and B varients and the same firmware can be used.

Throughout this manual any references to the Raspberry Pi Pico also includes the Raspberry Pi Pico 2 unless it
specifically excluded. If there are differences then the part number of the processor (RP2040 or RP2350) will
be used to make the difference obvious.

## File Names

There are a twelve firmware files contained in the firmware distribution zip file.

A typical filename for a firmware image looks like this:
```
PicoMiteRP2350VGAUSBV6.00.02.uf2
```

Where (in this example):

- RP2350 is the processor that the firmware is compiled for.
- VGAUSB is the feature set supported (VGA and USB).
- V6.00.01 is the version number. This will be incremented in future releases.
- .uf2 is the extension indicating a loadable Raspberry Pi Pico firmware image.

The following table lists the prefix for each firmware file and its associated capabilities.

|  **Firmware File Name** <br>For example:<br><pre>PicoMiteRP2040V60.0.01.uf2</pre> | CPU | Touch<br>LCD<br>Panel | Keyboard/Mouse | Video Output | WiFi<br>Internet |
| - | :-: | :-: | :-: | :-: | :-: | 
| PicoMiteRP2040 | RP2040 | &check; | PS2 |  |  |
| PicoMiteRP2350 | RP2350 | &check; | PS2 |  |  |
| PicoMiteRP2040USB | RP2040 | &check; | USB |  |  |
| PicoMiteRP2350USB | RP2350 | &check; | USB |  |  |
| PicoMiteRP2040VGA | RP2040 | | PS2 | VGA | |
| PicoMiteRP2350VGA | RP2350 | | PS2 | VGA | |
| PicoMiteRP2040VGAUSB | RP2040 | | USB | VGA | |
| PicoMiteRP2350VGAUSB | RP2350 | | USB | VGA | |
| PicoMiteHDMI | RP2350 | | PS2 | HDMI | |
| PicoMiteHDMI | RP2350 | | USB | HDMI | |
| WebMiteRP2040 | RP2040 | &check; | PS2 | | &check; |
| WebMiteRP2350 | RP2350A | &check; | PS2 | | &check; |

## Loading the Firmware

The Raspberry Pi Pico and Pico 2 comes with its own built in firmware loader that is easy to use.

To load the PicoMite firmware follow these steps:

- Download the PicoMite firmware from http://geoffg.net/picomite.html, unzip the file and identify the
firmware which suits your usage (see the previous headings).
- Using a USB cable plug the Raspberry Pi Pico into your computer (Windows, Linux or Mac) **while
holding down the white BOOTSEL** button on the top of the module.
- The Raspberry Pi Pico should connect to your computer and create a virtual drive (the same as if you had
plugged in a USB memory stick). You can ignore any files that may be on this “drive”
- Copy the firmware file (with the extension .uf2) to this virtual drive.
- When the copy has completed the Raspberry Pi Pico will restart and create a virtual serial port over USB
on your computer. See the chapter Serial Console below for the details of using this.
- The LED on the Raspberry Pi Pico will blink slowly indicating that the PicoMite firmware with
MMBasic is now running.

While the virtual drive created by the Raspberry Pi Pico looks like a USB memory stick it is not, the firmware
file will vanish once copied and if you try copying any other type of file it will be ignored.

Loading the PicoMite firmware may erase all the flash memory including the current program, any files in
drive A: and all saved variables. So make sure that you backup this data before you upgrade the firmware.

It is possible for the flash memory to be corrupted resulting in unusual and unpredictable behaviour. In that
case you should download the appropriate firmware file listed below and load it onto the Pico as described
above. This will reset the Raspberry Pi Pico to its factory fresh state, then you can reload the PicoMite
firmware:

- Raspberry Pi Pico (RP2040) https://geoffg.net/Downloads/picomite/Clear_Flash.uf2
- Raspberry Pi Pico 2 (RP2350) https://geoffg.net/Downloads/picomite/Clear_Flash_RP2350.uf2

# OPTION HDMI PINS clockpositivepin, d0positivepin, d1positivepin, d2positivepin

*HDMI VERSION ONLY*

Set the I/O pins used for the HDMI video output. This is only required to suit nonstandard PCB layouts.

The positive HDMI signal pins are set according to `nbr` below. Valid values are 0-7 and the pins must not overlap for each channel. If `nbr` is an even number the negative output is on physical pin+1, if `nbr` is odd it will be on physical pin-1.

nbr | HSTX Nbr | Physical Pin
:-: | :-: | :-:
0 | HSTX0 | GP12
1 | HSTX1 | GP13
2 | HSTX2 | GP14
3 | HSTX3 | GP15
4 | HSTX4 | GP16
5 | HSTX5 | GP17
6 | HSTX6 | GP18
7 | HSTX7 | GP19

The default is: `OPTION HDMI PINS 2, 0, 6, 4`

Which means that:

- CK+ and CK- are allocated to GP14 and GP15
- D0+ and D0- are allocated to GP12 and GP13
- D1+ and D1- are allocated to GP18 and GP19
- D2+ and D2- are allocated to GP16 and GP17


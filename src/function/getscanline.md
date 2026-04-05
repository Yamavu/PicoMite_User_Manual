### GETSCANLINE

This will report on the line that is currently being drawn on the VGA monitor
in the range of 0 to 525. This is irrespective of the current MODE.

Using this to time updates to the screen can avoid timing effects caused by
updates while the screen is being updated.

The first visible line will return a value of 0. Any line number above 479 is in
the frame blanking period.

## GPS functions

The GPS functions are used to return data from a serial communications
channel opened as GPS.

The function GPS(VALID) should be checked before any of these functions are
used to ensure that the returned value is valid.


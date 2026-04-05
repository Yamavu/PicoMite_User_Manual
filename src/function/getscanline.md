### GETSCANLINE

This will report on the line that is currently being drawn on the VGA monitor
in the range of 0 to 525. This is irrespective of the current MODE.

Using this to time updates to the screen can avoid timing effects caused by
updates while the screen is being updated.

The first visible line will return a value of 0. Any line number above 479 is in
the frame blanking period.


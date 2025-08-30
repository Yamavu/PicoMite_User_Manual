

### TRIANGLE X1, Y1, X2, Y2, X3, Y3 [, C [, FILL]]

Draws a triangle on the attached video output or LCD display panel with the
corners at X1, Y1 and X2, Y2 and X3, Y3. 

`C` is the colour of the triangle and defaults to the current foreground colour.

`FILL` is the fill colour and defaults to no fill (it can also be set to `-1` for no fill).

All parameters can be expressed as arrays and the software will plot the number of triangles as determined by the dimensions of the smallest array unless X1 = Y1 = X2 = Y2 = X3 = Y3 = -1 in which case processing will stop at that point.

`x1`, `y1`, `x2`, `y2`, `x3`,and `y3` must all be arrays or all be single variables/constants otherwise an error will be generated `c` and `fill` can be either arrays or single variables/constants.

### TRIANGLE SAVE [#]n, x1,y1,x2,y2,x3,y3

Saves a triangular area of the screen to buffer #n.

### TRIANGLE RESTORE [#]n

Restores a saved triangular region of the screen and deletes the saved buffer.
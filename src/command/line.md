

### LINE x1, y1, x2, y2 [, LW [,C]]

On an attached LCD display this command will draw a line starting at the coordinates `x1` and `y1` and ending at `x2` and `y2`.

`LW` is the line’s width and is only valid for horizontal or vertical lines. It defaults to 1 if not specified. 

`C` is an integer representing the colour and defaults to the current foreground colour.

#### Array parameters

All parameters can be expressed as arrays and the software will plot the number of lines as determined by the dimensions of the smallest array. 

`x1`, `y1`, `x2`, and `y2` must **all be arrays** or **all be single variables/constants** otherwise an error will be generated. 

`lw` and `c` can be either arrays or single variables/constants. For horizontal and vertical lines that have a defined width and the x1 and y1 coordinate define the top-left pixel of the thick line. i.e. the line is to the right of the specified position or below it on the screen. For diagonal lines width a width > 1 the line is centered on the origin and destination pixels. If width is given as a -ve value then lines in all directions are centered on the given coordinates.


### LINE AA x1, y1, x2, y2 [

Draws a line with anti-aliasing . The parameters are as per the [LINE](./line.md) command


### LINE GRAPH x(), y(), colour

This command generates a line graph of the coordinate pairs specified in “x()” and “y()”. The graph will have n-1 segments where there are n elements in the x and y arrays.

```basic
DIM x(3)
DIM y(3)
DIM c = rgb(white)
FOR i = 1 TO 3 : x(i) = MATH(RAND)*80 : NEXT i
FOR i = 1 TO 3 : y(i) = MATH(RAND)*80 : NEXT i

' equivalent to
' LINE x(1), y(1), x(2), y(2), c
' LINE x(2), y(2), x(3), y(3), c
LINE GRAPH x(), y(), c
```


### LINE PLOT ydata() [,nbr] [,xstart] [,xinc] [,ystart] [,yinc] [,colour]

Plots a line graph from an array of y-axis data points. 

`ydata()` is an array of floats or integers to be plotted 

`nbr` is the number of line segments to be plotted - defaults to the lesser of the array size and MM.HRES-2 if omitted 

`xstart` is the x-coordinate to start plotting - defaults to 0 

`xinc` is the increment along the x-axis to plot each coordinate - defaults to 1

`ystart` is the location in ydata to start the plot - defaults to the array start. NB: respects [OPTION BASE](../option/base.md)

`yinc` is the increment to the index into ydata to add for each point to be plotted 

`colour` is the colour to draw the line
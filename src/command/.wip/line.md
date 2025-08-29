

### LINE x1, y1, x2, y2 [, LW [,

 On an attached LCD display this command will draw a line starting at the

### LINE AA x1, y1, x2, y2 [,

 Draws a line with anti-aliasing . The parameters are as per the LINE command

### LINE GRAPH x(), y(), colour

 This command generates a line graph of the coordinate pairs specified in “x()” and “y()”. The graph will have n-1 segments where there are n elements in the x and y arrays.

### LINE INPUT [prompt$,] string-variable$

 Reads an entire line from the console input into ‘string-variable$’. ‘prompt$’ is a string constant (not a variable or expression) and if specified it will be printed first. A question mark is not printed unless it is part of ‘prompt$’. Unlike INPUT, this command will read a whole line, not stopping for comma delimited data items.

### LINE INPUT #nbr, string-variable$

 Same as above except that the input is read from a serial communications port or a file previously opened for INPUT as ‘nbr’. See the OPEN command.

### LINE PLOT ydata() [,nbr] [,xstart] [,xinc] [,ystart] [,yinc] [,colour]

 Plots a line graph from an array of y-axis data points. ‘ydata()’ is an array of floats or integers to be plotted ‘nbr ‘is the number of line segments to be plotted - defaults to the lesser of the array size and MM.HRES-2 if omitted ‘xstart’ is the x-coordinate to start plotting - defaults to 0 ‘xinc’ is the increment along the x-axis to plot each coordinate - defaults to 1 ‘ystart’ is the location in ydata to start the plot - defaults to the array start. NB: respects OPTION BASE ‘yinc’ is the increment to the index into ydata to add for each point to be plotted ‘colour’ is the colour to draw the line
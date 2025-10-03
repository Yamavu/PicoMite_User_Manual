.wip


### POLYGON n, xarray%(), yarray%() [, bordercolour] [, fillcolour]

Draws a filled or outline polygon with ‘n’ xy-coordinate pairs in ‘xarray%()’ and ‘yarray%()’. If ‘fillcolour’ is omitted then just the polygon outline is drawn. If ‘bordercolour’ is omitted then it will default to the current default foreground colour.

### POLYGON n(), xarray%(), yarray%() [, bordercolour()] [, fillcolour()]

If the last xy-coordinate pair is not the same as the first the firmware will automatically create an additional xy-coordinate pair to complete the polygon. The size of the arrays should be at least as big as the number of x,y coordinate pairs. 'n' can be an array and the colours can also optionally be arrays as follows:

### POLYGON n(), xarray%(), yarray%() [, bordercolour] [, fillcolour]

POLYGON n(), xarray%(), yarray%() [, bordercolour()] [, fillcolour()] POLYGON n(), xarray%(), yarray%() [, bordercolour] [, fillcolour] The elements of ‘array n()’ define the number of xy-coordinate pairs in each of the polygons. eg, DIM n(1)=(3,3) would define that 2 polygons are to be drawn with three vertices each. The size of the n array determines the number of polygons that will be drawn unless an element is found with the value zero in which case the firmware only processes polygons up to that point. The x,y- coordinate pairs for all the polygons are stored in ‘xarray%()’ and ‘yarray%()’. The ‘xarray%()’ and ‘yarray%()’ parameters must have at least as many elements as the total of the values in the n array. Each polygon can be closed with the first and last elements the same. If the last element is not the same as the first the firmware will automatically create an additional x,y-coordinate pair to complete the polygon. If fill colour is omitted then just the polygon outlines are drawn. The colour parameters can be a single value in which case all polygons are drawn in the same colour or they can be arrays with the same cardinality as ‘n’. In this case each polygon drawn can have a different colour of both border and/or fill. For example, this will draw 3 triangles in yellow, green and red: DIM c%(2)=(3,3,3) DIM x%(8)=(100,50,150,100,50,150,100,50,150) DIM y%(8)=(50,100,100,150,200,200,250,300,300) DIM fc%(2)=(rgb(yellow),rgb(green),rgb(red)) POLYGON c%(),x%(),y%(),fc%(),fc%()
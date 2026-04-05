### BOUND(array() [,dimension]

This returns the upper limit of the array for the dimension requested.

The dimension defaults to one if not specified. Specifying a dimension value of
0 will return the current value of OPTION BASE.

Unused dimensions will return a value of zero.

For example:
DIM myarray(44,45)
BOUND(myarray(),2) will return 45


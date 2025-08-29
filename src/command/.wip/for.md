

### For a simple variable one expression is used, for an array a list of comma separated expressions surrounded by brackets is used.

keyword (i.e. FLOAT, INTEGER or STRING) after each variable. If you use this method the type must be specified for each variable and can be changed from variable to variable. For example: DIM amount AS FLOAT, name AS STRING Floating point or integer variables will be set to zero when created and strings will be set to an empty string (i.e. ""). You can initialise the value of the

### FOR counter = start TO finish [STEP increment]

Initiates a FOR-NEXT loop with the 'counter' initially set to 'start' and incrementing in 'increment' steps (default is 1) until 'counter' is greater than 'finish'. The ‘increment’ can be an integer or a floating point number. Note that using a floating point fractional number for 'increment' can accumulate rounding errors in 'counter' which could cause the loop to terminate early or late.
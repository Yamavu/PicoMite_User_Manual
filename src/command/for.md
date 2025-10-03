### FOR counter = start TO finish [STEP increment]

Initiates a `FOR`-`NEXT` loop with the `counter` initially set to `start` and incrementing in `increment` steps (default is 1) until `counter` is greater than `finish`.

The `increment` can be an integer or a floating point number. 

*Note that using a floating point fractional number for `increment` can accumulate rounding errors in `counter` which could cause the loop to terminate early or late.*

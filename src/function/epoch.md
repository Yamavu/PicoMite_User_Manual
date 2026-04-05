### EPOCH(DATETIME$)

Returns the epoch number (number of seconds that have elapsed since midnight
GMT on January 1, 1970) for the supplied DATETIME$ string.

The format for DATETIME$ is “dd-mm-yyyy hh:mm:ss”, “dd-mm-yy
hh:mm:ss”, or “yyyy-mm-dd hh:mm:ss”,. Use NOW to get the epoch number
for the current date and time, i.e. PRINT EPOCH(NOW)


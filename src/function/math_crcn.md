### MATH(CRCn data [,length] [,polynome] [,startmask] [,endmask] [,reverseIn] [,reverseOut]

Calculates the CRC to n bits (8, 12, 16, 32) of "data". "data" can be an integer
or floating point array or a string variable. "Length" is optional and if not
specified the size of the array or string length is used. The defaults for

startmask, endmask reverseIn, and reversOut are all zero. reverseIn, and
reversOut are both Booleans and take the value 1 or 0. The defaults for
polynomes are CRC8=&H07, CRC12=&H80D, CRC16=&H1021,
crc32=&H04C11DB7
eg, for crc16_CCITT use MATH(CRC16 array(), n,, &HFFFF)
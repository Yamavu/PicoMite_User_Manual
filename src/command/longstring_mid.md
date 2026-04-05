### LONGSTRING MID dest%(), src%(), start, nbr

Will copy 'nbr' characters from 'src%()' to 'dest%()' starting at character position 'start' overwriting whatever was in 'dest%()'. i.e. copy from the middle of 'src%()'. 'nbr' is optional and if omitted the characters from 'start' to the end of the string will be copied. 'src%()' and 'dest%()' must be long string variables. 'start' and 'nbr' must be integer constants or expressions.

See also: [MID$()](../function/mid$.md) - regular string mid extraction function.
### SPRITE LOAD fname$ [,start_sprite_number] [,mode]

Loads the file `fname$` which must be formatted as an original Colour Maximite sprite file. See the original Colour Maximite MMBasic Language Manual for the [file format](../sprite_format.md).

Multiple sprite files can be loaded by specifying a different `start_sprite_number` for each file. The programmer is responsible for making sure that the sprites do not overlap. 

Mode defaults to `0` zero in which case the CMM1/CMM2 colour codes are used. If mode is specified as `1` then the RGB121 colour codes are used. See [Colors](../colors.md)

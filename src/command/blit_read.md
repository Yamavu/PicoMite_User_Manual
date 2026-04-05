### BLIT READ [#]b, x, y, w, h

`BLIT READ` will copy a portion of the display to the memory buffer `#b`.The source coordinate is `x` and `y` and the width of the display area to copy is `w` and the height is `h`.

When this command is used the memory buffer is automatically created and sufficient memory allocated. 

This buffer can be freed and the memory recovered with the `BLIT CLOSE` command.

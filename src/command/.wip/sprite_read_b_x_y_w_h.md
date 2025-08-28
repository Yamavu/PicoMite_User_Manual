## SPRITE READ [#]b, x, y, w, h

This will copy a portion of the display to the memory buffer '#b'. The sourcecoordinate is 'x' and 'y' and the width of the display area to copy is 'w' and theheight is 'h'. When this command is used the memory buffer is automaticallycreated and sufficient memory allocated. This buffer can be freed and thememory recovered with the SPRITE CLOSE command.
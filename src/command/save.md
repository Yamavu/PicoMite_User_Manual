.wip


### SAVE file$

Saves the program in the current working directory of the Flash Filesystem or SD Card as ‘file$’. Example: SAVE “TEST.BAS” If an extension is not specified “.BAS” will be added to the file name. See also FLASH SAVE n for saving to a Flash Slot.

### SAVE CONTEXT [CLEAR]

Saves the variable space and optionally clears it - command should be used in top level program and not from within a subroutine. This saves the entire variable space to the A: drive. The command will fail if there is not enough free space on the A: drive. In the case of and RP2350 with PSRAM the variable space will be saved to a reserved area in the PSRAM and the A: drive is not used. See also LOAD CONTEXT

### SAVE IMAGE file$ [,x, y, w, h] or

Save the current image on the video output or LCD panel as a BMP file. Any LCD panel must be capable of being read, for example, a ILI9341 based panel or a VIRTUAL_M or VIRTUAL_C panel.

### SAVE COMPRESSED

'file$' is the name of the file. If an extension is not specified “.BMP” will be

### SAVE PERSISTENT n%

Saves the value n% in a special memory location that will survive a watchdog reset or a physical reset but not a power cycle See also MM.PERSISTENT or MM.INFO(PERSISTENT)
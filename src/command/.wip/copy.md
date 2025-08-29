

### COPY fname1$ TO fname2$

Copy a file from ‘fname1$’ to ‘fname2$’. Both are strings. A directory path can be used in both 'fname$' and 'fname$'. If the paths differ the file specified in 'fname$' will be copied to the path specified in 'fname2$' with the file name as specified. The filenames can include the drive specification in the case that you are copying to and or from the non-active drive (see the DRIVE command)

### COPY fname$ TO dirname$

Wildcard copy. The bulk copy is triggered if fname$ contains a '*' or a '?' character. dirname$ must be a valid directory name and should NOT end in a slash character


### EDIT or

Invoke the full screen editor. If a filename is specified the editor will load the file from the current disk (A:

### EDIT fname$ or

or B:) to allow editing and on exit with F1 or F2 save it to the disk. If the file does not exist it is created on exit. The current program stored in flash memory is not affected. If editing an existing file a backup with .bak appended to the

### EDIT FILE fname$

filename is also created on exit. If fname$ includes an extension other than .bas then colour coding will be temporarily turned off during the edit. If no extension is specified the firmware will assume .bas Editing a file from disk allows non-Basic files such as html or sprite files to be edited without corruption during the tokenising process that happens when stored to flash. EDIT and EDIT fname$ can only be invoked at the command prompt. If you wish to edit a file in a program you can use the EDIT FILE fname$ command. The command must be used in the top level program and not from within a subroutine. EDIT FILE fname$ differs from EDIT fname$ in that it will automatically save the entire variable space to the A: drive and restores it on exit. The command will fail if there is not enough free space on the A: drive. In the case of an RP2350 with PSRAM the variable space will be saved to a reserved area in the PSRAM and the A: drive is not used. See the chapter Full Screen Editor for details of how to use the editor.


### AUTOSAVE or

 Enter automatic program entry mode. This command will take lines of text from the console serial input and save them to program memory.

### AUTOSAVE CRUNCH or

 This mode is terminated by entering Control-Z or F1 which will then cause the received data to be transferred into program memory overwriting the previous program. Use F2 to exit and immediately run the program.

### AUTOSAVE APPEND

 The CRUNCH option instructs MMBasic to remove all comments, blank lines and unnecessary spaces from the program before saving. This can be used on large programs to allow them to fit into limited memory. CRUNCH can be abbreviated to the single letter C. The APPEND option will leave the existing program intact and append the new data from the serial input to the end of it. At any time this command can be aborted by Control-C which will leave program memory untouched. This is one way of transferring a BASIC program into the Raspberry Pi Pico. The program to be transferred can be pasted into a terminal emulator and this command will capture the text stream and store it into program memory. It can also be used for entering a small program directly at the console input. NON VGA OR HDMI VERSIONS
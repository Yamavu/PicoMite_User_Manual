.wip


### LIBRARY SAVE or

The library is a special segment of program memory that can contain program code such as subroutines, functions and CFunctions. These routines are not visible to the programmer but are available to the running program and act the

### LIBRARY DELETE or

same as the built in commands and functions in MMBasic. Any code in the library that is not contained within a subroutine or function will be executed immediately before a program is run. This can be used to initialise constants, set options, etc. See the heading The Library in this manual

### LIBRARY LIST or

for a full explanation. The library is stored in program memory Flash Slot 3 which will then not be available for saving a program (slots 1 to 2 will still be available).

### LIBRARY LIST ALL or

LIBRARY SAVE will take whatever is in normal program memory, compress it (remove redundant data such as comments) and append it to the library area (main program memory is then empty). The code in the library will not show

### LIBRARY DISK SAVE fname$ or

in LIST or EDIT and will not be deleted when a new program is loaded or NEW is used. LIBRARY DELETE will remove the library and return Flash Slot 3 for normal use (OPTION RESET will do the same).

### LIBRARY DISK LOAD fname$

LIBRARY LIST will list the contents of the library. Use ALL to list without page confirmations. LIBRARY DISK SAVE fname$ will save the current library as a binary file allowing a subsequent call to LIBRARY DISK LOAD fname$ to restore the library. Together, these allow libraries specific for individual programs to be stored and restored easily and distributed. Other than using version specific functionality in the library (WEB, VGA, GUI) libraries can be shared between versions.
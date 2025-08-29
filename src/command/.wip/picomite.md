

### PicoMite User Manual

Page 99

### PicoMite User Manual

Page 101

### PicoMite User Manual

Page 103 The “usersubname$” can be any string or variable or function that resolves to the name of a normal user subroutine (not an in-built command). The “usersubparameters” are the same parameters that would be used to call the subroutine directly. A typical use could be writing any sort of emulator where one of a large number of subroutines should be called depending on some variable. It also allows a way of passing a subroutine name to another subroutine or function as a variable. NOT VGA OR HDMI

### PicoMite User Manual

Page 105

### PicoMite User Manual

Page 107

### PicoMite User Manual

Page 109 number of elements is 231 and because each floating point number requires 8 bytes a total of 1848 bytes of memory will be allocated. Strings will default to allocating 255 bytes (i.e. characters) of memory for each element and this can quickly use up memory when defining arrays of strings. In that case the LENGTH keyword can be used to specify the amount of memory to be allocated to each element and therefore the maximum length of the string that can be stored. This allocation ('n') can be from 1 to 255 characters. For example: DIM STRING s(5, 10) will declare a string array with 66 elements consuming 16,896 bytes of memory while: DIM STRING s(5, 10) LENGTH 20 Will only consume 1,386 bytes of memory. Note that the amount of memory allocated for each element is n + 1 as the extra byte is used to track the actual length of the string stored in each element. If a string longer than 'n' is assigned to an element of the array an error will be produced. Other than this, string arrays created with the LENGTH keyword act exactly the same as other string arrays. This keyword can also be used with non-array string variables but it will not save any memory. In the above example you can also use the Microsoft syntax of specifying the type after the length qualifier. For example: DIM s(5, 10) LENGTH 20 AS STRING Arrays can also be initialised when they are declared by adding an equals symbol (=) followed by a bracketed list of values at the end of the declaration. For example: DIM INTEGER nbr(4) = (22, 44, 55, 66, 88) or DIM s$(3) = ("foo", "boo", "doo", "zoo") Note that the number of initialising values must match the number of elements in the array including the base value set by OPTION BASE. If a multi dimensioned array is initialised then the first dimension will be initialised first followed by the second, etc. Also note that the initialising values must be after the LENGTH qualifier (if used) and after the type declaration (if used).

### PicoMite User Manual

Page 111

### PicoMite User Manual

Page 113 'increment' can be negative in which case 'finish' should be less than 'start' and the loop will count downwards. See also the NEXT command. NOT HDMI AND VGA VERSIONS

### PicoMite User Manual

Page 115

### PicoMite User Manual

Page 117 NOT VGA AND HDMI VERSIONS

### PicoMite User Manual

Page 119

### PicoMite User Manual

Page 121

### PicoMite User Manual

Page 123

### PicoMite User Manual

Page 125

### PicoMite User Manual

Page 127 DIM IN(2)=(1,2,3) DIM OUT(2) MATH WINDOW IN(),7,3,OUT(),LOW,HIGH Will return OUT(0)=7, OUT(1)=5,OUT(2)=3,LOW=1,HIGH=3 This command can massively simplify scaling data for plotting etc.

### PicoMite User Manual

Page 129 frequency at array position N = N * sample_frequency / number_of_samples

### PicoMite User Manual

Page 131

### PicoMite User Manual

Page 133 blue). A framebuffer (F) can be created. This have no impact on the display and does not use user memory but can be used for creating images and copying to the display screen (N). In addition a layer buffer can be created. This also does not use user memory. any pixels written to the layer buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through. Map functionality is available to override the default colours of the 16 available In the case of VGA, the hardware is limited to the 16 colours defined by the resistor network

### PicoMite User Manual

Page 135 allowing the main display buffer to show through. Map functionality is available to override the default colours.

### PicoMite User Manual

Page 137

### PicoMite User Manual

Page 139 ‘fnbr’ is the file number (1 to 10). The # is optional. Up to 10 files can be open simultaneously and can be on either or both the A: and C: drives. The INPUT, LINE INPUT, PRINT, WRITE and CLOSE commands as well as the EOF() and INPUT$() functions all use ‘fnbr’ to identify the file being operated on. See also ON ERROR and MM.ERRNO for error handling.

### PicoMite User Manual

Page 141

### PicoMite User Manual

Page 143 'y' must both be arrays or both be single variables /constants otherwise an error will be generated. 'c' can be either an array or a single variable or constant. See the chapter Graphics Commands and Functions for a definition of the colours and graphics coordinates.

### PicoMite User Manual

Page 145 'file$' is the MP3 file to play (the extension of .mp3 will be appended if missing). The sample rate should be 44100Hz stereo. The MP3 file is played in the background. 'interrupt' is optional and is the name of a subroutine which will be called when the file has finished playing. If file$ is a directory on the B: drive the Pico will play all of the files in that directory in turn.

### PicoMite User Manual

Page 147

### PicoMite User Manual

Page 149

### PicoMite User Manual

Page 151 • Both ‘file$’ and ‘cmdline$’ may be supplied as string expressions. • Use FLASH RUN n to run a program stored in a Flash Slot.

### PicoMite User Manual

Page 153 and if any pullup or pulldown is enabled 2 specifies a falling edge with pullup, 3 specifies that both a falling and rising edge will trigger a count with no pullup applied, 5 specifies both edges but with a pullup applied. If ‘option’ is omitted a rising edge will trigger the count. Due to a bug in the RP2350 chips pulldown is not recommended. The pins can be GP6, GP7, GP8 or GP9 (can be changed with OPTION COUNT). DOUT Digital output 'option' is not used in this mode. The functions PIN() and PORT() can also be used to return the value on one or more output pins. See the function PIN() for reading inputs and the statement PIN()= for setting an output. See the command below if an interrupt is configured.

### PicoMite User Manual

Page 155

### PicoMite User Manual

Page 157

### PicoMite User Manual

Page 159 variable and therefore may be accessed after the subroutine has ended. The argument can be prefixed with BYVAL which will prevent this mechanism and cause only the value to be used. Alternatively, the prefix BYREF instructs MMBasic that a reference is required and an error will be generated if that cannot be done. Arrays are passed by specifying the array name with empty brackets (eg, arg()) and are always passed by reference and must be the correct type. Every definition must have one END SUB statement. When this is reached the program will return to the next statement after the call to the subroutine. The command EXIT SUB can be used for an early exit. You use the subroutine by using its name and arguments in a program just as you would a normal command. For example: MySub a1, a2 When the subroutine is called each argument in the caller is matched to the argument in the subroutine definition. These arguments are available only inside the subroutine. Subroutines can be called with a variable number of arguments. Any omitted arguments in the subroutine's list will be set to zero or a null string. Arguments in the caller's list that are a variable and have the correct type will be passed by reference to the subroutine. This means that any changes to the corresponding argument in the subroutine will also be copied to the caller's variable and therefore may be accessed after the subroutine has ended. The argument can be prefixed with BYVAL which will prevent this mechanism and cause only the value to be used. Alternatively, the prefix BYREF instructs MMBasic that a reference must be used and an error will occur if that cannot be done. Arrays are passed by specifying the array name with empty brackets (eg, arg()) and are always passed by reference. Brackets around the argument list in both the caller and the definition are optional.

### PicoMite User Manual

Page 161

### PicoMite User Manual

Page 163 rate of 50Hz. If an optional user interrupt is specified this will be triggered if either of the buttons changes (both on and off) See the DEVICE function for how to read data from the Wii Nunchuck.

### PicoMite User Manual

Page 165
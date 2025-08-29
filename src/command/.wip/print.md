

### PRINT expression [[,; ]expression] … etc

Outputs text to the serial console followed by a carriage return/newline pair. Multiple expressions can be used and must be separated by either a:  Comma (,) which will output the tab character  Semicolon (;) which will not output anything (it is just used to separate expressions).  Nothing or a space which will act the same as a semicolon. A semicolon (;) or a comma (,) at the end of the expression list will suppress the output of the carriage return/newline pair at the end of a print statement. When printed, a number is preceded with a space if positive or a minus (-) if negative but is not followed by a space. Integers (whole numbers) are printed without a decimal point while fractions are printed with the decimal point and the significant decimal digits. Large or small floating point numbers are automatically printed in scientific number format. The function TAB() can be used to space to a certain column and the STR$() function can be used to justify or otherwise format strings.

### PRINT #nbr, expression [[,; ]expression] … etc

Same as above except that the output is directed to a serial communications port or a file opened for OUTPUT or APPEND with a file number of ‘nbr’. See the OPEN command.

### PRINT #GPS, expression [[,; ]expression] … etc

Outputs a NMEA string to an opened GPS device. The string must start with a $ character and end with a * character. The checksum is automatically calculated and appended to the string together with the CR/LF characters.

### PRINT @(x [, y]) expression or

Works on terminal console on an attached computer or VGA/HDMI video or the display if OPTION LCDPANEL CONSOLE is enabled.

### PRINT @(x, [y], m) expression

Same as the standard PRINT command except that the cursor is positioned at the coordinates x, y expressed in pixels. If y is omitted the cursor will be positioned at “x” on the current line. Example: PRINT @(150, 45) "Hello World" The @ function can be used anywhere in a print command. Example: PRINT @(150, 45) "Hello" @(150, 55) "World" The @(x,y) function can be used to position the cursor anywhere on or off the screen. For example, PRINT @(-10, 0) "Hello" will only show "llo" as the first two characters could not be shown because they were off the screen. The @(x,y) function will automatically suppress the automatic line wrap normally performed when the cursor goes beyond the right screen margin. If 'm' is specified the mode of the video operation will be as follows: m = 0 Normal text (white letters, black background) m = 1 The background will not be drawn (ie, transparent) m = 2 The video will be inverted (black letters, white background) m = 5 Current pixels will be inverted (transparent background)
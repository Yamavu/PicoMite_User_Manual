

### OPEN fname$ FOR mode AS [#]fnbr

Opens a file for reading or writing. ‘fname’ is the filename with an optional extension separated by a dot (.). Long file names with upper and lower case characters are supported. The file system on the SD Card is NOT case sensitive however the Flash Filesystem IS case sensitive. A directory path can be specified with the backslash as directory separators. The parent of the current directory can be specified by using a directory name of “..” (two dots) and the current directory with “.” (a single dot). For example: OPEN ".\dir1\dir2\filename.txt" FOR INPUT AS #1 ‘mode’ is INPUT, OUTPUT, APPEND or RANDOM. INPUT will open the file for reading and throw an error if the file does not exist. OUTPUT will open the file for writing and will automatically overwrite any existing file with the same name. APPEND will also open the file for writing but it will not overwrite an existing file; instead any writes will be appended to the end of the file. If there is no existing file the APPEND mode will act the same as the OUTPUT mode (i.e. the file is created then opened for writing). RANDOM will open the file for both read and write and will allow random access using the SEEK command. When opened the read/write pointer is positioned at the end of the file. If the file does not exist , it will be created.

### OPEN comspec$ AS [#]fnbr

Will open a serial communications port for reading and writing. Two ports are available (COM1: and COM2:) and both can be open simultaneously. For a full description with examples see Appendix A. Using ‘fnbr’ the port can be written to and read from using any command or function that uses a file number.

### OPEN comspec$ AS GPS [,timezone_offset] [,monitor]

Will open a serial communications port for reading from a GPS receiver. See the GPS function for details. The sentences interpreted are GPRMC, GNRMC, GPGGA and GNGGA. The timezone_offset parameter is used to convert UTC as received from the GPS to the local timezone. If omitted the timezone will default to UTC. The timezone_offset can be a any number between -12 and 14 allowing the time to be set correctly even for the Chatham Islands in New Zealand (UTC +12:45). If the monitor parameter is set to 1 then all GPS input is directed to the console. This can be stopped by closing the GPS channel.
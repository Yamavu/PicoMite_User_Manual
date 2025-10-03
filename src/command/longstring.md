.wip


### LONGSTRING

The LONGSTRING commands allow for the manipulation of strings longer than the normal MMBasic limit of 255 characters. Variables for holding long strings must be defined as single dimensioned integer arrays with the number of elements set to the number of characters required for the maximum string length divided by eight. The reason for dividing by eight is that each integer in an MMBasic array occupies eight bytes. Note that the long string routines do not check for overflow in the length of the strings. If an attempt is made to create a string longer than a long string variable's size the outcome will be undefined.

### LONGSTRING AES128 ENCRYPT/DECRYPT CBC/ECB/CTR key$/key[!/%](), in%(), out%() [,iv$/iv[!/%]()]

Encrypts or decrypts the longstring in `in%()` putting the answer in `out%()`

For CBC and CTR modes the encryption will generate a random initialisation vector and prepend out%() with the IV. If an explicit IV is specified this will be used instead of the random vector and this will be prepended to out%() 



For CBC and CTR decryption the firmware assumes that the first 16 bytes of in%() are the initialisation vector. In the case where you want to transmit a message without IV you can use LONGSTRING RIGHT to remove the IV before sending the message. In this case the recipient must know the IV as well as the key and create a complete longstring before using DECRYPT. This can be done by using LONGSTRING CONCAT to add the incoming message to a longstring containing the IV.

### CBC/ECB/CTR key$/key(), in$/in(), out$/out() [,iv$/iv()]

The parameters can each be either a string, integer array, or float array with any mix possible The key must be 16 elements long (16*8=128bits), in and out must be a multiple of 16 elements long. In the case of out being specified as a string (e.g. out$), the string variable must exist and should be set to empty (DIM out$="") The maximum number of elements in 'in' and 'out' is limited by memory when defined as arrays. Strings for encrypting are limited to 240bytes (EBR) and 224bytes (CTR and CBC). For CBC and CTR encryption you can optionally specify an initialisation vector 'iv'. 'iv' must be 16 elements long (16*8=128bits). If an initialisation vector is not specified encryption will generate a random initialisation vector. In both cases the output is prepended with the IV. For CBC and CTR, decryption requires that the first 16 elements of the input are the initialisation vector. In the case where you want to transmit a message without IV you should remove the IV before sending the message using standard MMBasic manipulations. In this case the recipient must know the IV as well as the key and create a complete message before using DECRYPT by prepending the IV to the incoming message.


Encrypts or decrypts the longstring in in%() putting the answer in out%()

### LONGSTRING APPEND array%(), string$

Append a normal MMBasic string to a long string variable. ‘array%()’ is a long string variable while ‘string$’ is a normal MMBasic string expression.

### LONGSTRING BASE64

This BASE64 encodes or decodes the longstring in in%() placing the answer in

### LONGSTRING CLEAR array%()

Will clear the long string variable ‘array%()’. i.e. it will be set to an empty string.

### LONGSTRING COPY dest%(), src%()

Copy one long string to another. ‘dest%()’ is the destination variable and ‘src%()’ is the source variable. Whatever was in ‘dest%()’ will be overwritten.

### LONGSTRING CONCAT dest%(), src%()

Concatenate one long string to another. ‘dest%()’ is the destination variable and ‘src%()’ is the source variable. ‘src%()’ will the added to the end of ‘dest%()’ (the destination will not be overwritten).

### LONGSTRING LCASE array%()

Will convert any uppercase characters in ‘array%()’ to lowercase. ‘array%()’ must be long string variable.

### LONGSTRING LEFT dest%(), src%(), nbr

Will copy the left hand 'nbr' characters from ‘src%()’ to ‘dest%()’ overwriting whatever was in ‘dest%()’. i.e. copy from the beginning of ‘src%()’. ‘src%()’ and ‘dest%()’ must be long string variables. 'nbr' must be an integer constant or expression.

### LONGSTRING LOAD array%(), nbr, string$

Will copy 'nbr' characters from ‘string$’ to the long string variable ‘array%()’ overwriting whatever was in ‘array%()’.

### LONGSTRING MID dest%(), src%(), start, nbr

Will copy 'nbr' characters from ‘src%()’ to ‘dest%()’ starting at character position 'start' overwriting whatever was in ‘dest%()’. i.e. copy from the middle of ‘src%()’. 'nbr' is optional and if omitted the characters from 'start' to the end of the string will be copied ‘src%()’ and ‘dest%()’ must be long string variables. 'start' and 'nbr' must be integer constants or expressions.

### LONGSTRING PRINT [#n,] src%() [;]

Prints the longstring stored in ‘src%()’ to the file or COM port opened as ‘#n’. If ‘#n’ is not specified the output will be sent to the console. Add a semi-colon to supress CR/LF.

### LONGSTRING REPLACE array%() , string$, start

Will substitute characters in the normal MMBasic string ‘string$’ into an existing long string ‘array%()’ starting at position ‘start’ in the long string.

### LONGSTRING RESIZE addr%(), nbr

Sets the size of the longstring to ‘nbr’. This overrides the size set by other longstring commands so should be used with caution. Typical use would be in using a longstring as a byte array.

### LONGSTRING RIGHT dest%(), src%(), nbr

Will copy the right hand 'nbr' characters from ‘src%()’ to ‘dest%()’ overwriting whatever was in ‘dest%()’. i.e. copy from the end of ‘src%()’. ‘src%()’ and ‘dest%()’ must be long string variables. 'nbr' must be an integer constant or expression.

### LONGSTRING SETBYTE addr%(), nbr, data

Sets byte ‘nbr’ to the value “data”, ‘nbr’ respects OPTION BASE

### LONGSTRING TRIM array%(), nbr

Will trim ‘nbr’ characters from the left of a long string. ‘array%()’ must be a long string variables. 'nbr' must be an integer constant or expression.

### LONGSTRING UCASE array%()

Will convert any lowercase characters in ‘array%()’ to uppercase. ‘array%()’ must be long string variable.
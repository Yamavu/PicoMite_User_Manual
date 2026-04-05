### LCD CMD d1 [, d2 [, etc]]

Send one or more bytes to an LCD display as commands. Each byte is a number between 0 and 255 and must be separated by commas.

The LCD must have been previously initialised using the LCD INIT command. This command can be used to drive a non-standard LCD in "raw mode" or to enable specialised features such as scrolling, cursors and custom character sets. You will need to refer to the data sheet for your LCD to find the necessary command values.
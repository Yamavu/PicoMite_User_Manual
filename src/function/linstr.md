### LINSTR(array%(), search$ [,start] [,size]))

Returns the position of a search string in a long string.

The returned value is an integer and will be zero if the substring cannot be
found. `array%()` is the string to be searched and must be a long string
variable. `search$` is the substring to look for and it must be a normal
MMBasic string or expression (not a long string). The search is case sensitive.

Normally the search will start at the first character in ' array%()' but the
optional third parameter allows the start position of the search to be specified.

If the optional parameter `size` is specified the `search$` is treated as a regular
expression. See Appendix E for the details.


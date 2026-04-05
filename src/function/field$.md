### FIELD$( string1, nbr, string2 [, string3] )

Returns a particular field in a string with the fields separated by delimiters.

Note that a space character cannot be used as a delimeter.

`nbr` is the field to return (the first is nbr 1). `string1` is the string to search and
`string2` is a string holding the delimiters (more than one can be used). The
space character may not be used as a delimiter.

`string3` is optional and if specified will include characters that are used to
quote text in `string1` (ie, quoted text will not be searched for a delimiter).

For example:
S$ = "foo, boo, zoo, doo"
r$ = FIELD$(s$, 2, ",")
will result in r$ = "boo". While:
s$ = "foo, 'boo, zoo', doo"
r$ = FIELD$(s$, 2, ",", "'")
will result in r$ = "boo, zoo".




### FILES [fspec$] [,sort]

 Lists files in any directories on the default Flash Filesystem or SD Card. 'fspec$' (if specified) can contain a path and search wildcards in the filename. Question marks (?) will match any character and an asterisk (*) will match any number of characters. If omitted, all files will be listed. For example: * Find all entries *.TXT Find all entries with an extension of TXT E*.* Find all entries starting with E X?X.* Find all three letter file names starting and ending with X mydir/* Find all entries in directory mydir NB: putting wildcards in the pathname will result in an error 'sort' specifies the sort order as follows: size by ascending size time by descending time/date name by file name (default if not specified) type by file extension
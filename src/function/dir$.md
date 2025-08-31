### DIR$( [fspec],[type] )

Searches the default Flash Filesystem or SD Card for files and return the first name matching the query. Subsequent calls with no arguments will return more entries found. When only `""` is found, no (more) entries matched.

Optional parameters:

`fspec` is a file specification using wildcards the same as used by the [FILES](command/files.md) command. Eg, `"*.*"` will return all entries, `"*.TXT"` will return text files. 

Note that the wildcard *.* does not find files or folders without an extension.

`type` is the type of entry to return and can be one of:
* `ALL` : Search for all files and directories
* `DIR` : Search for directories only
* `FILE` : Search for files only (the default if 'type' is not specified)

The function will return the first entry found. To retrieve subsequent entries use the function with no arguments. i.e. `DIR$()`. The return of an empty string indicates that there are no more entries to retrieve.

This example will print all the files in a directory:

```basic
f$ = DIR$("*.*", FILE)
DO WHILE f$ <> ""
PRINT f$
f$ = DIR$()
LOOP
```

You must change to the required directory before invoking this command.
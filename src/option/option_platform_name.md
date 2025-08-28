# OPTION PLATFORM name$

Allows a user to identify a particular hardware configuration that can
then be used in programs to control the program's operation.

`name$` can be up to 31 characters long. This is a permanent option.

`MM.INFO$(PLATFORM)` returns this string.

For example, this can be used on a particular hardware configuration:

```basic
OPTION PLATFORM "GameMite"
```

Then programs that might run on this or other platforms can use:

```basic
IF MM.INFO$(PLATFORM) = "GameMite" THEN …
```
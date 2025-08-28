# OPTION FNKey string$

Define the string that will be generated when a function key is pressed at
the command prompt. `FNKey` can be *F1*, and *F5* thru to *F9*.

Example:

```basic
OPTION F8 “RUN “+chr$(34)+”myprog” +chr$(34)+chr$(13)+chr$(10).
```

*This command must be run at the command prompt (not in a program).*


### CMM2 LOAD <br> CMM2 RUN

Loads and/or Runs a program from disk using the CMM2 (Colour Maximite 2) program loading mechanism. This can be used for compatibility with *Colour Maximite 2* programs or to allow structuring programs into separate modules.

This includes an aggressive crunching of the program and supports #INCLUDE files and #DEFINE text replacement. 

It is important to note that if used all editing of programs must be offline or direct to and from disk as the source files cannot be reconstructed from the version loaded by these commands.


#### #DEFINE
```basic
#DEFINE "FROMSTRING","print"
#DEFINE "endstring","end"
'
FROMSTRING "Hello" 'will be converted to PRINT "Hello"
'
#DEFINE "fromstring","TEXT 100,500,"
FROMSTRING "Hello" 'will be converted to TEXT 100,100,"Hello"
'
print @(0,mm.info(Fontheight))"fromstring" 'won't be converted
print ""
'
list
ENDSTRING
```

#### #INCLUDE file$

This will insert the file 'file$' into the program at that point. 


```basic
#INCLUDE "constant.inc"
print c%
```

constant.inc
```basic
CONST c% = 12345
```



# Appendix E – Regex Syntax

Regex Syntax
The alternate forms of the INSTR() and LINSTR() functions can take a regular expression as the search pattern.
The alternate form of the commands are:
INSTR([start],text$, search$ [,size])
LINSTR(text%(),search$ [,start] [,size]

In both cases specifying the size parameter causes the firmware to interpret the search string as a regular
expression. The size parameter is a floating point variable that is used by the firmware to return the size of a
matching string. If the variable doesn't exist it is created. As implemented in MMBasic you need to apply the
returned start and size values to the MID$ function to extract the matched string. eg,

IF start THEN match$=MID$(text$,start,size) ELSE match$=”” ENDIF
The library used for the regular expressions implements POSIX draft P1003.2/D11.2, except for some of the
internationalization features. See http://mirror.math.princeton.edu/pub/oldlinux/Linux.old/Refdocs/POSIX/all.pdf section 2.8 for details of constructing Regular Expressions or other online tutorials.
The syntax of regular expressions can vary slightly with the various implementations. This document is a
summary of the syntax and supported operations used in the MMBasic implementation.
Anchors
^ Start of string
$ End of string
\b Word Boundary
\B Not a word boundary
\< Start of word
\> End of word
Qualifiers
*
0 or more (not escaped)
\+
1 or more
\?
0 or 1
\{3\} Exactly 3
\{3,\} 3 or more
\{3,5\} 3,4 or 5
Groups and Ranges
(a\|b)
a or b
\(…\) group
[abc]
Range (a or b or c)
[^abc] Not (a or b or c]
[a-q]
lower case letters a to q
[A-Q] upper case letters A to Q
[0-7]
Digits from 0 to 7
Escapes Required to Match Normal Characters
\^ to match ^ (caret)
\.
to match . (dot)
\* to match * (asterix)
\$ to match $ (dollar)
\[ to match [ (left bracket)
\\
to match \ (backslash)

Page 194

PicoMite User Manual

Escapes with Special Functions
\+ See Quantifiers
\? See Quantifiers
\{ See Quantifiers
\} See Quantifiers
\| See Groups and Ranges
\( See Groups and Ranges
\) See Groups and Ranges
\w See Character Classes
Character Classes
\w
digits,letters and _
[:word:] digits,letters and _
[:upper:] Upper case letters_
[:lower:] Lower case letters_
[:alpha:] All letters
[:alnum:] Digits and letters
[:digit:] Digits
[:xdigit:] Hexidecimal digits
[:punct:] Puntuation
[:blank:] Space and tab
[:space:] Blank charaters
[:cntrl:] Control charaters
[:graph:] Printed characters
[:print:] Printed chars and spaces
Example expression to match an IP Address which is contained within a word boundary.
"\<[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\>"

PicoMite User Manual

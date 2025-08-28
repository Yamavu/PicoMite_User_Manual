## Single Character Commands

### ‘ (single quotation mark)

`'` starts a comment and any text following it will be ignored. Comments can be
placed anywhere on a line.

### * (star/asterisk)


The star/asterisk command is a shortcut for RUN that may only be used at the
MMBasic prompt. eg,
short | long
:- | :-
`*` | `RUN`
`*foo` | `RUN "foo"`
`*"foo bar"` | `RUN "foo bar"`
`*foo –wombat` | `RUN "foo", "--wombat"`
`*foo "wom"` | `RUN "foo", CHR$(34) + "wom" + CHR$(34)`
`*foo --wom="bat"` | `RUN "foo","--wom=" + CHR$(34) + "bat" + CHR$(34)`

String expressions are not supported/evaluated by this command; any arguments provided are passed as a literal string to the `RUN` command.

### ? (question mark)

Shortcut for the PRINT command.

### /*  */ (multiline comments)

Start and end of multiline comments. `/*` and `*/` must be the first non-space characters at the start of a line and have a space or end-of-line after them (i.e. they are MMBasic commands). Multi-line comments cannot be used inside subroutines and functions. Any characters after */ on a line are also treated as a comment.


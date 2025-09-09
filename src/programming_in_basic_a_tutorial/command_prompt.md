## Command Prompt

Interaction with MMBasic is done via the console at the command prompt (ie, the greater than symbol
 `>` on the console). On startup MMBasic will issue the command prompt and wait for some
command to be entered. It will also return to the command prompt if your program ends or if it
generated an error message.

When the command prompt is displayed you have a wide range of commands that you can enter and
execute. Typically they would list the program held in memory ( `LIST` ) or edit it ( `EDIT` ) or perhaps
set some options (the `OPTION` command). Most times the command is just `RUN` which instructs
MMBasic to run the program held in program memory.

Almost any command can be entered at the command prompt and this is often used to test a command
to see how it works. A simple example is the `PRINT` command (more on this later), which you can
test by entering the following at the command prompt:

```basic
PRINT 2 + 2
```

and not surprisingly MMBasic will print out the number 4 before returning to the command prompt.

This ability to test a command at the command prompt is useful when you are learning to program in
BASIC, so it would be worthwhile having a Raspberry Pi Pico loaded with the PicoMite firmware
handy for the occasional test while you are working through this tutorial.

Structure of a BASIC Program
A BASIC program starts at the first line and continues until it runs off the end or hits an `END` 
command - at which point MMBasic will display the command prompt `>` on the console and wait for
something to be entered.

A program consists of a number of statements or commands, each of which will cause the BASIC
interpreter to do something (the words statement and command generally mean the same and are used
interchangeable in this tutorial).

Normally each statement is on its own line but you can have multiple statements in the one line
separated by the colon character `:`.

For example:
```
A = 24.6 : PRINT A
```

Each line can start with a line number. Line numbers were mandatory in the early BASIC interpreters
however modern implementations (such as MMBasic) do not need them. You can still use them if
you wish but they have no benefit and generally just clutter up your programs.

This is an example of a program that uses line numbers:

```basic
50 A = 24.6
60 PRINT A
```

A line can also start with a label which can be used as the target for a program jump using the `GOTO`
command. This will be explained in more detail when we cover the `GOTO` command but this is an
example (the label name is `JmpBack`):

```basic
JmpBack: A = A + 1
PRINT A
GOTO JmpBack
```



### IF expr THEN stmt [: stmt] <br>IF expr THEN stmt ELSE stmt

Evaluates the expression `expr` and performs the statement following the `THEN` keyword if it is true or skips to the next line if false. If there are more statements on the line (separated by colons (:) they will also be executed if true or skipped if false.

The ELSE keyword is optional and if present the statement(s) following it will be executed if `expr` resolved to be false. 

The `THEN` statement construct can be also replaced with: `GOTO linenumber | label`. This type of `IF` statement is all on one line.

### IF expression THEN <br>&lt;statements><br> [ELSEIF expression THEN <br>&lt;statements>] <br>[ELSE <br>&lt;statements>]<br> ENDIF 

Multiline `IF` statement with optional `ELSE` and `ELSEIF` cases and ending with `ENDIF`. Each component is on a separate line. 

Evaluates `expression` and performs the statement(s) following `THEN` if the expression is true or optionally the statement(s) following the `ELSE` statement if false. 

The `ELSEIF` statement (if present) is executed if the previous condition is false and it starts a new `IF` chain with further `ELSE` and/or `ELSEIF`
statements as required. One `ENDIF` is used to terminate the multiline `IF`.

### ELSE

Introduces an optional default condition in a multiline `IF` statement. 

See the multiline `IF` statement for more details.

### ELSEIF expression THEN or <br> ELSE IF expression THEN

Introduces an optional secondary condition in a multiline `IF` statement. 

See the multiline `IF` statement for more details.

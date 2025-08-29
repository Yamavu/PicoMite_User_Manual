

### IF expr THEN stmt [: stmt] or

 Evaluates the expression ‘expr' and performs the statement following the THEN keyword if it is true or skips to the next line if false. If there are more statements on the line (separated by colons (:) they will also be executed if true

### IF expr THEN stmt ELSE stmt

 or skipped if false. The ELSE keyword is optional and if present the statement(s) following it will be executed if 'expr' resolved to be false. The ‘THEN statement’ construct can be also replaced with: GOTO linenumber | label’. This type of IF statement is all on one line.

### IF expression THEN <statements> [ELSEIF expression THEN <statements>] [ELSE <statements>]

 Multiline IF statement with optional ELSE and ELSEIF cases and ending with ENDIF. Each component is on a separate line. Evaluates 'expression' and performs the statement(s) following THEN if the expression is true or optionally the statement(s) following the ELSE statement if false. The ELSEIF statement (if present) is executed if the previous condition is false and it starts a new IF chain with further ELSE and/or ELSEIF
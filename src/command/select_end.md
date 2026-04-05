### END SELECT

Concludes the SELECT CASE statement. When a match is made the `<statements>` following the `CASE` statement will be executed until `END SELECT` or another `CASE` is encountered when the program will then continue with the code following the `END SELECT`.

Each `SELECT CASE` must have one and one only matching `END SELECT` statement. Any number of `SELECT … CASE` statements can be nested inside the `CASE` statements of other `SELECT … CASE` statements.
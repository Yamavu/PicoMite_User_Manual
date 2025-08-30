

### CASE

```basic
SELECT CASE value
    CASE testexp [[, testexp] …]
        <statements>
        <statements>
    CASE test-n [[, test-n] …]
        <statements>
        <statements>
    CASE ELSE
        <statements>
        <statements>
END SELECT
```

Executes one of several groups of statements, depending on the value of an expression. 

`value` is the expression to be tested. It can be a number or string
variable or a complex expression.

`testexp` (or test-n) is the value that is to be compared against. 
It can be:

* A single expression to which it may equal <br>
  For example: `34`, `"string"` or `PIN(4)*5`

* A range of values in the form of two single expressions separated by the keyword `TO` <br>
  For example: `5 TO 9` or `"aa" TO "cc"`

* A comparison starting with the keyword `IS` (which is optional). When a number of test expressions (separated by commas) are used the `CASE` statement will be true if **any** one of these tests evaluates to true.<br>
  For example: `IS > 5, IS <= 10`

When a number of test expressions (separated by commas) are used the `CASE`
statement will be true if any one of these tests evaluates to true.
If `value` cannot be matched with a `testexp` it will be automatically matched to
the `CASE ELSE`. If `CASE ELSE` is not present the program will not execute any
`<statements>` and continue with the code following the `END SELECT`. When a
match is made the `<statements>` following the `CASE` statement will be
executed until `END SELECT` or another `CASE` is encountered when the
program will then continue with the code following the `END SELECT`.

An unlimited number of `CASE` statements can be used but there must be only
one `CASE ELSE` and that should be the last before the `END SELECT`.
Example:

```basic
SELECT CASE nbr%
    CASE 4, 9, 22, 33 TO 88
        statements
    CASE IS < 4, IS > 88, 5 TO 8
        statements
    CASE ELSE
        statements
END SELECT
```

Each `SELECT CASE` must have one and one only matching `END SELECT`
statement. Any number of `SELECT…CASE` statements can be nested inside
the `CASE` statements of other `SELECT…CASE` statements.

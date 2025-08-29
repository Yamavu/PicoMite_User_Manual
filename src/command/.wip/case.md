

### CASE testexp [[, testexp] …] <statements> <statements>

expression. 'value' is the expression to be tested. It can be a number or string variable or a complex expression. 'testexp' (or test-n) is the value that is to be compared against. It can be:

### CASE test-n [[, test-n] …] <statements> <statements>

 A single expression (i.e. 34, "string" or PIN(4)*5) to which it may equal  A range of values in the form of two single expressions separated by the keyword "TO" (i.e. 5 TO 9 or "aa" TO "cc")

### CASE ELSE <statements> <statements>

 A comparison starting with the keyword "IS" (which is optional). For example: IS > 5, IS <= 10. When a number of test expressions (separated by commas) are used the CASE statement will be true if any one of these tests evaluates to true.

### CASE 4

, 9, 22, 33 TO 88 statements

### CASE I

S < 4, IS > 88, 5 TO 8 statements

### CASE E

LSE statements
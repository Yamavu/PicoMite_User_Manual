## Arrays

Arrays are something which you will probably not think of as useful at first glance but when you do need to use them you will find them very handy indeed.

An array is best thought of as a row of letterboxes for a block of units or condos as shown on the right. The letterboxes are all located at the same address and each box represents a unit or condo at that address. You can place a letter in the box for unit one, or unit two, etc.

Similarly an array in BASIC is a single variable with multiple sub units (called elements in BASIC) which are numbered. You
can place data in element one, or element two, etc. In BASIC an array is created by the `DIM` command, for example:

```basic
DIM numarr(300)
```

This creates an array with the name of numarr containing 301 elements (think of them as letterboxes) ranging from 0 to 300. By default an array will start from zero so this is why there is an extra element making the total 301. To specify a specific element in the array (ie, a specific letterbox) you use an index which is simply the number of the array element that you wish to access. 

For example, if you want to set element number 100 in this array to (say) the number 876, you would do it this way:

```basic
numarr(100) = 876
```

Normally the index to an array is not a constant number as in this example (ie, 100) but a variable
which can be changed to access different array elements.

As an example of how you might use an array, consider the case where you would like to record the
maximum temperature for each day of the year and, at the end of the year, calculate the overall
average. You could use ordinary variables to record the temperature for each day but you would need
365 of them and that would make your program quite unwieldy. Instead, you could define an array to
hold the values like this:

```basic
DIM days(365)
```

Every day you would need to save the temperature in the correct location in the array. If the number of
the day in the year was held in the variable doy and the maximum temperature was held in the
variable maxtemp you would save the reading like this:

```basic
days(doy) = maxtemp
```

At the end of the year it would be simple to calculate the average for the year.

For example:

```basic
total = 0
FOR i = 1 to 365
total = total + days(i)
NEXT i
PRINT "Average is:" total / 365
```

This is much easier than adding up and averaging 365 individual variables.

The above array was single dimensioned but you can have multiple dimensions. Reverting to our analogy of letterboxes, an array with two dimensions could be thought of as a block of flats with multiple floors. A block could have a row of four letter boxes for level one, another row of four boxes for level two, and so on. To place a letter in a letterbox you need to specify the floor number and the unit number on that floor.

In BASIC such an array is specified using two indices separated by a comma. For example:

```basic
LetterBox(floor, unit)
```

As a practical example, assume that you needed to record the maximum temperature for each day over
five years. To do this you could dimension the array as follows:

```basic
DIM days(365, 5)
```

The first index is the day in the year and the second is a number representing the year. If you wanted to set day 100 in year 3 to 24 degrees you would do it like this:

```basic
days(100, 3) = 24
```

In MMBasic for the PicoMite firmware, you can have up to six dimensions with the RP2040 processor or five dimensions with the RP2350 processor. The size of an array is limited only by the amount of free RAM that is available.



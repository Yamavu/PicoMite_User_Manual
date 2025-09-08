## ARRAY

Creation:

```basic
DIM sourcearray(4)=(1,2,3,4)
```

or

```basic
DIM sourcearray(4)
sourcearray(1)=1
sourcearray(2)=2
sourcearray(3)=3
sourcearray(4)=4
```


### ARRAY ADD in(), value ,out()

This adds (or appends for strings) the value ´value´ to every element of the array/matrix `in()` and puts the answer in the array/matrix `out()`. `in()` and `out()` can be the same array.

Works for arrays of any dimensionality of strings and both integer and float (can convert between integer and float). 

Setting `num` to `0` or `""` is optimised and is a fast way of copying an entire array. 


### ARRAY INSERT targetarray(), [d1] [,d2] [,d3] [,d4] [,d5] , sourcearray()

This is the opposite of [ARRAY SLICE](./array.md#slice), has a very similar syntax, and allows you, for example, to substitute a single vector into an array of vectors with a single instruction or a one dimensional array of strings into a two dimensional array of strings.

The arrays can be numerical or strings and `sourcearray()` and `destinationarray()` must be the same (NB: can convert between integers and floats for numerical arrays). eg, 

```basic
OPTION BASE 1
DIM targetarray(3,4,5)
DIM sourcearray(4)=(1,2,3,4)
ARRAY INSERT targetarray(), 2, , 3, sourcearray() 
```

Will set elements `2,1,3 = 1` and `2,2,3 = 2` and `2,3,3 = 3` and `2,4,3 = 4`


### ARRAY SET value, array()

Sets all elements in array() to the value `value`. Value can be a number or a string and `array` must be the same (NB: can convert between integers and floats). 

This is the fastest way of clearing an array by setting it to zero or an empty string.


### ARRAY SLICE sourcearray() [,d1] [,d2] [,d3] [,d4] [,d5] ,destinationarray()

This command copies a specified set of values from a multi-dimensional array into a single dimensional array. It is much faster than using a FOR loop.

The slice is specified by giving a value for all but one of the source array indices and there should be as many indices in the command, including the blank one, as there are dimensions in the source array.

The arrays can be numerical or strings and `sourcearray` and `destinationarray` must be the same (NB: can convert between integers and floats for numerical arrays). eg, 

```basic
OPTION BASE 1
DIM a(3,4,5)
DIM b(4)
ARRAY SLICE a(), 2, , 3, b()
```

Will copy the elements `2,1,3` and `2,2,3` and `2,3,3` and `2,4,3` into array `b()`
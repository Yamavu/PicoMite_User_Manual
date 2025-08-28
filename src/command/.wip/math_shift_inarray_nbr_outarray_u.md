## MATH SHIFT inarray%(), nbr, outarray%() [,U]

This command does a bit shift on all elements of inarray%() and places theresult in outarray%() (may be the same as inarray%()). nbr can be between -63and 63. Positive numbers are a left shift (multiply by power of 2). Negativenumber are a right shift. The optional parameter ,U will force an unsignedshift.
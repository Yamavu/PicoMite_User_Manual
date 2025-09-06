## Format of a Sprite File

from [the original Colour Maximite MMBasic Language Manual](https://geoffg.net/Downloads/Maximite/MMBasic%20Language%20Manual.pdf)

A sprite file is similar to a font file except that it contains the definition of sprites which are 16x16 bit graphical
objects. The sprite file is just a text file containing ordinary characters which are loaded line by line to build
the bitmap of each sprite. Currently the dimensions of each sprite are fixed at 16x16 bits although alternative
sizes may be allowed in the future.

The first non-comment line in the file must be the specifications for the sprite file as follows:

`dimension, number`

Where `dimension` is the height and width of the sprites in pixels. At this time it must be the number 16.

`number` is the number of sprites in the file and is limited only by the amount of free memory available. The
remainder of the lines specify the bitmap for each sprite.

Each line represents a horizontal row of pixels with each character in the line defining the colour of the pixel.

The character can be a single numeric digit in the range of 0 to 7 representing the colours black to white or it
can be a space which means that that particular pixel will be transparent (ie, the background will show
through). On the monochrome Maximite 0 represents a black pixel and any other number represents a white
pixel.

Each sprite must immediately follow the preceding sprite in the file and be defined by 16 lines each of 16
characters wide (although trailing spaces can be omitted and will be assumed to be transparent pixels).

A comment line has an apostrophe ` ' ` as the first character and can occur anywhere. A comment line is
completely ignored; all other lines are significant.

The following example is of a file that contains a single sprite consisting of a red ball with a white border and a
blue centre dot. On the monochrome Maximite this would display as a white ball.

```
' e x a m p l e s p r i t e
' T E S T . S P R
1 6 , 1
            7 7 7 7
        7 4 4 4 4 4 4 7
    7 4 4 4 4 4 4 4 4 4 4 7
  7 4 4 4 4 4 4 4 4 4 4 4 4 7
  7 4 4 4 4 4 4 4 4 4 4 4 4 7
7 4 4 4 4 4 4 4 4 4 4 4 4 4 4 7
7 4 4 4 4 4 4 1 1 4 4 4 4 4 4 7
7 4 4 4 4 4 1 1 1 1 4 4 4 4 4 7
7 4 4 4 4 4 1 1 1 1 4 4 4 4 4 7
7 4 4 4 4 4 4 1 1 4 4 4 4 4 4 7
7 4 4 4 4 4 4 4 4 4 4 4 4 4 4 7
  7 4 4 4 4 4 4 4 4 4 4 4 4 7
  7 4 4 4 4 4 4 4 4 4 4 4 4 7
    7 4 4 4 4 4 4 4 4 4 4 7
        7 4 4 4 4 4 4 7
            7 7 7 7
```


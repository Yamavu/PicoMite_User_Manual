

### MAP

 The MAP commands allow the programmer to set the colours used in 4 or 8-bit colour modes. Each value in the 4 or 8-bit colour pallet can be set to an independent 24-bit colour (ie, RGB555 format). See the MAP function for more information

### MAP( n ) = rgb%

 This will assign the 24-bit colour 'rgb% to all pixels with the 4 or 8-bit colour value of 'n'. The change is activated after the MAP SET command.

### MAP MAXIMITE

 This will set the colour map to the colours implemented in the original Colour Maximite.

### MAP GREYSCALE

 This will set the colour map to 16 or 32 levels of grey (depending on the MODE). MAP GRAYSCALE is also valid.

### MAP SET

 This will cause MMBasic to update the colour map (set using MAP(n)=rgb%) during the next frame blanking interval.

### MAP RESET

 This will reset the colour map to the default colours VGA VERSION ONLY

### MAP

 The MAP commands allow the programmer to select the colours used in 4-bit colour modes. Each value in the 4-bit colour pallet can be set to one of the 16 available colours . See the MAP function for more information.

### MAP( n ) = rgb%

 This will assign the 24-bit colour 'rgb% to all pixels with the 4-bit colour value of 'n'. The RGB value is converted to one of the available 16 VGA RGB121 colours as set by the resistor network. The change is activated after the MAP SET command.

### MAP MAXIMITE

 This will set the colour map to the colours implemented in the original Colour Maximite.

### MAP SET

 This will cause MMBasic to update the colour map (set using MAP(n)=rgb%) during the next frame blanking interval.

### MAP RESET

 This will reset the colour map to the default colours which in 4-bit mode are: ‘n’ Colour Value 15 WHITE RGB(255, 255, 255) 14 YELLOW RGB(255, 255, 0) 13 LILAC RGB(255, 128, 255) 12 BROWN RGB(255, 128, 0) 11 FUCHSIA RGB(255, 64, 255) 10 RUST RGB(255, 64, 0) 9 MAGENTA RGB(255, 0, 255) 8 RED RGB(255, 0, 0) 7 CYAN RGB(0, 255, 255) 6 GREEN RGB(0, 255, 0) 5 CERULEAN RGB(0, 128, 255) 4 MIDGREEN RGB(0, 128, 0) 3 COBALT RGB(0, 64, 255) 2 MYRTLE RGB(0, 64, 0) 1 BLUE RGB(0, 0, 255) 0 BLACK RGB(0, 0, 0)
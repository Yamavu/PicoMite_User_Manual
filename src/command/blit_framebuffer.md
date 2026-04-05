### BLIT FRAMEBUFFER from, to, xin, yin, xout, yout, width, height [,colour]

Copies an area of a specific `from` framebuffer N, F, or L to another different `to` framebuffer N, F, or L. 

`xin` and `yin` define the top left of the area of `width` and `height` on the source framebuffer to be copied. 

`xout` and `yout` define the top left of the area on the target framebuffer to receive the copy. 

The optional parameter `colour` defines a pixel colour on the source which will not be copied. If omitted all pixels are copied. The colour is specified as a number between `0` and `15` representing:

black, blue, myrtle, cobalt, midgreen, cerulean, green, cyan, red, magenta, rust, fuschia, brown, lilac, yellow and white

Requires both a framebuffer and a layer buffer to have been created to operate. 

Will automatically wait for frame blanking before starting the copy on ILI9341, ST7789_320 and ILI9488 displays.

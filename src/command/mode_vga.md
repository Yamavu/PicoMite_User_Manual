### MODE n

*VGA VERSIONS ONLY*


VGA video supports a number of resolutions (see `OPTION RESOLUTION`).

This command will select the mode `n` depending on the resolution:

#### OPTION RESOLUTION 640 x 480

* **`MODE 1` 640 x 480 x 2 colours (monochrome).**
  
  *Default at startup.*
  
  Tiles width is fixed at 8 pixels. Tile height defaults to 12 pixels
  but can be from 8 to MM.HRES. Tiles colours are specified using
  the standard RGB888 notation. This is converted to RGB121. 
  
  A framebuffer (F) and a layer buffer (L) can be created. These have
  no impact on the display and do not use user memory but both
  can be used for creating images and copying to the display screen
  (N)

* **`MODE 2` 320 x 240 x 16 colours**
  
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N).
  
  In addition a layer buffer can be created. This also does not use user
  memory. any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer.

  A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through. Map functionality is available to override the default colours of the 16 available. The hardware is limited to the 16 colours defined by the resistor network

* **`MODE 3` 640 x 480 x 16 colours**
  
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). 

  In addition a layer buffer can be created. This also does not use user
  memory. Any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. 
  
  A colour can be specified (0-15: defaults to
  0) which does not show allowing the main display buffer to show
  through. Map functionality is available to override the default
  colours of the 16 available. The hardware is limited to the 16
  colours defined by the resistor network


#### OPTION RESOLUTION 720 x 400

* **`MODE 1` 720 x 400 x 2 colours (monochrome)** 
  
  *Default at startup.*
  
  Tiles width is fixed at 8 pixels. Tile height defaults to 12 pixels
  but can be from 8 to MM.HRES. Tiles colours are specified using
  the standard RGB888 notation. This is converted to RGB121. A
  framebuffer (F) and a layer buffer (L) can be created. These have
  no impact on the display and do not use user memory but both
  can be used for creating images and copying to the display screen
  (N)

* **`MODE 2` 360 x 200 x 16 colours**
  
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for blue).
  
  A framebuffer (F) can be created. This have no impact on the display and does not use user memory but can be used for creating images and copying to the display screen (N). 
  
  In addition a layer buffer can be created. This also does not use user memory. any pixels written to the layer buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through. Map functionality is available to override the default colours of the 16 available In the case of VGA, the hardware is limited to the 16 colours defined by the resistor network

* **`MODE 3` 720 x 400 x 16 colours**

  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). 
  
  In addition a layer buffer can be created. This also does not use user memory. Any pixels written to the layer buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. 
  
  A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through. Map functionality is available to override the default colours of the 16 available. In the case of VGA, the hardware is limited to the 16 colours defined by the resistor network


#### OPTION RESOLUTION 800 x 600 (RP2350 only)

* **`MODE 1` 800 x 600 x 2 colours (monochrome). Default at startup**
  Tiles width is fixed at 8 pixels. Tile height defaults to 12 pixels
  but can be from 8 to MM.HRES. Tiles colours are specified using
  the standard RGB888 notation. This is converted to RGB121. A
  framebuffer (F) and a layer buffer (L) can be created. These have
  no impact on the display and do not use user memory but both
  can be used for creating images and copying to the display screen
  (N)
* **`MODE 2` 400 x 300 x 16 colours**
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). In
  addition a layer buffer can be created. This also does not use user
  memory. any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. A colour can be specified (0-15: defaults to
  0) which does not show allowing the main display buffer to show
  through. Map functionality is available to override the default
  colours of the 16 available The hardware is limited to the 16
  colours defined by the resistor network
* **`MODE 3` 800 x 600 x 16 colours**
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). In
  addition a layer buffer can be created. This also does not use user
  memory. any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. A colour can be specified (0-15: defaults to
  0) which does not show allowing the main display buffer to show
  through. Map functionality is available to override the default
  colours of the 16 available, The hardware is limited to the 16
  colours defined by the resistor network


#### OPTION RESOLUTION 848 x 480 (RP2350 only)

* **`MODE 1` 848 x 480 x 2 colours (monochrome). Default at startup**
  Tiles width is fixed at 8 pixels. Tile height defaults to 12 pixels
  but can be from 8 to MM.HRES. Tiles colours are specified using
  the standard RGB888 notation. This is converted to RGB121. A
  framebuffer (F) and a layer buffer (L) can be created. These have
  no impact on the display and do not use user memory but both
  can be used for creating images and copying to the display screen
  (N)
* **`MODE 2` 424 x 240 x 16 colours**
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). In
  addition a layer buffer can be created. This also does not use user
  memory. any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. A colour can be specified (0-15: defaults to
  0) which does not show allowing the main display buffer to show
  through. Map functionality is available to override the default
  colours of the 16 available The hardware is limited to the 16
  colours defined by the resistor network
* **`MODE 3` 848 x 48 x 16 colours**
  RGB121 format (i.e. 1 bit for red, 2 bits for green, and 1 bit for
  blue). A framebuffer (F) can be created. This have no impact on
  the display and does not use user memory but can be used for
  creating images and copying to the display screen (N). In
  addition a layer buffer can be created. This also does not use user
  memory. any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. A colour can be specified (0-15: defaults to
  0) which does not show allowing the main display buffer to show
  through. Map functionality is available to override the default
  colours of the 16 available, The hardware is limited to the 16
  colours defined by the resistor network




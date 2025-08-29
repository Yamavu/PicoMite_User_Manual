### MODE n

*HDMI VERSIONS ONLY*

HDMI video supports a number of resolutions (see [OPTION RESOLUTION](../option/resolution.md)). This command will select the mode `n` depending on the resolution:

#### OPTION RESOLUTION 640 x 480

* **MODE 1** <br>
  640 x 480 x 2-colours (monochrome) <br>
  Default at startup. <br>
  Use the `TILE` command as normal. Tiles width is fixed at 8 pixels. Tile height defaults to 12 pixels but can be from 8 to `MM.HRES`. Tiles colours are specified using the standard RGB888 notation.<br>
  This is converted to RGB555. <br>
  A framebuffer (F) and a layer buffer (L) can be created. These can be used for creating images and copying to the display screen (N).

* **MODE 2** <br> 320 x 240 x 16 colours<br>
  A framebuffer (F) can be created. This can be used for creating images and copying to the display screen (N). In addition a layer buffer can be created.<br>
	Any pixels written to the layer buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through. <br>
	Map functionality is available to override the default colours.

* **MODE 3**<br>
  640 x 480 x 16 colours<br>
  Colour mapping to RGB555 palette. A framebuffer (F) can be created. It can be used for creating images and copying to the display screen (N). In addition a layer buffer can be created.<br>
  Any pixels written to the layer buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. <br>
  A colour can be specified (0-15: defaults to 0) which does not show allowing the main display buffer to show through.

* **MODE 4**<br>320 x 240 x 32768 colours<br>
This is full RGB555 allowing good quality colour images to be displayed. A framebuffer (F) and a layer buffer (L) can be created. These have no impact on the display and can be used for creating images and copying to the display screen (N). <br>
Only one can be created

* **MODE 5**<br> 320 x 240 x 256 colours<br>
  A framebuffer (F) can be created. This has no impact on the display. It can be used for creating images and copying to the display screen (N). In addition a layer buffer can be created.<br>
  This does not use user memory. Any pixels written to the layer
  buffer will automatically appear on the display sitting on top of whatever may be in the main display buffer. <br>
  A colour can be specified (0-255: defaults to 0) which does not show allowing the main display buffer to show through. Map functionality is available to override the default colours of the 256 available.<br>
  Each of the 256 colours can be mapped to any RGB555 colour.


#### OPTION RESOLUTION 720 x 400

* **MODE 1**<br> 720 x 400 x 2-colours (monochrome).<br> 
  *Default at startup.*<br>
  Use the TILE command as normal. Tiles width is fixed at 8
  pixels. Tile height defaults to 12 pixels but can be from 8 to
  MM.HRES. Tiles colours are specified using the standard
  RGB888 notation. This is converted to RGB555. A
  framebuffer (F) and a layer buffer (L) can be created. These
  can be used for creating images and copying to the display
  screen (N)
* **MODE 2**<br> 360 x 200 x 16 colours.<br>
  A framebuffer (F) can be created. This can be used for creating
  images and copying to the display screen (N). In addition a
  layer buffer can be created. Any pixels written to the layer
  buffer will automatically appear on the display sitting on top
  of whatever may be in the main display buffer. A colour can
  be specified (0-15: defaults to 0) which does not show
  allowing the main display buffer to show through. Map
  functionality is available to override the default colours.
* **MODE 3**<br> 720 x 400 x 16 colours.<br>
  Colour mapping to RGB555 palette. A framebuffer (F) can be
  created. It can be used for creating images and copying to the
  display screen (N). In addition a layer buffer can be created.
  Any pixels written to the layer buffer will automatically
  appear on the display sitting on top of whatever may be in the
  main display buffer. A colour can be specified (0-15: defaults
  to 0) which does not show allowing the main display buffer to
  show through.
* **MODE 4**<br> 360 x 200 x 32768 colours.<br>
  This is full RGB555 allowing good quality colour images to be
  displayed. A framebuffer (F) and a layer buffer (L) can be
  created. These have no impact on the display and can be used
  for creating images and copying to the display screen (N).
  Only one can be created
* **MODE 5**<br> 360 x 200 x 256 colours.<br>
  A framebuffer (F) can be created. This has no impact on the
  display. It can be used for creating images and copying to the
  display screen (N). In addition a layer buffer can be created.
  This does not use user memory. Any pixels written to the layer
  buffer will automatically appear on the display sitting on top of
  whatever may be in the main display buffer. A colour can be
  specified (0-255: defaults to 0) which does not show allowing
  the main display buffer to show through. Map functionality is
  available to override the default colours of the 256 available.
  Each of the 256 colours can be mapped to any RGB555 colour.
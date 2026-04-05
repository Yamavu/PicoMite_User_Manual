### SAVE COMPRESSED IMAGE filename$ [, StartX, StartY, width, height]

Saves the current image on the LCD screen to a file as a compressed 24-bit true colour BMP file using RLE compression to reduce file size.

**Parameters:**
- `filename$`: The filename to save to (file extension is optional - .BMP will be added if not specified)
- `StartX`: (Optional) X-coordinate of the top left corner of the area to save (defaults to 0)
- `StartY`: (Optional) Y-coordinate of the top left corner of the area to save (defaults to 0)
- `width`: (Optional) Width of the area to save in pixels (defaults to full screen width)
- `height`: (Optional) Height of the area to save in pixels (defaults to full screen height)

**Notes:**
- The image is saved as a 24-bit true colour BMP file with RLE (Run-Length Encoding) compression
- RLE compression reduces file size for images with areas of solid colour
- If no area parameters are specified, the entire screen will be saved
- Note that 'width', if used, must be a multiple of 2

**Example:**
```basic
SAVE COMPRESSED IMAGE "compressed.bmp"
SAVE COMPRESSED IMAGE "partial_compressed.bmp", 0, 0, 320, 100
```

**Cross-reference:** See [SAVE IMAGE](image_save.md) for saving without compression.
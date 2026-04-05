### SAVE IMAGE filename$ [, StartX, StartY, width, height]

Saves the current image on the LCD screen to a file as a 24-bit true colour BMP file.

**Parameters:**
- `filename$`: The filename to save to (file extension is optional - .BMP will be added if not specified)
- `StartX`: (Optional) X-coordinate of the top left corner of the area to save (defaults to 0)
- `StartY`: (Optional) Y-coordinate of the top left corner of the area to save (defaults to 0)
- `width`: (Optional) Width of the area to save in pixels (defaults to full screen width)
- `height`: (Optional) Height of the area to save in pixels (defaults to full screen height)

**Notes:**
- The image is saved as a 24-bit true colour BMP file
- If no area parameters are specified, the entire screen will be saved
- Note that 'width', if used, must be a multiple of 2

**Example:**
```basic
SAVE IMAGE "screenshot.bmp"
SAVE IMAGE "partial.bmp", 10, 20, 100, 80
```

**Cross-reference:** See [SAVE COMPRESSED IMAGE](image_save_compressed.md) for saving with RLE compression.
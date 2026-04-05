### LOAD IMAGE filename$ [, StartX, StartY]

Loads an image from the Flash Filesystem or SD Card for display on an attached LCD display panel. This can be used to draw a logo or add a background on the display.

**Parameters:**
- `filename$`: The image file to load (file extension is optional - .BMP will be added if not specified)
- `StartX`: (Optional) X-coordinate of the top left corner where the image will be displayed (defaults to 0)
- `StartY`: (Optional) Y-coordinate of the top left corner where the image will be displayed (defaults to 0)

**Supported Formats:**
The image must be in BMP format. All types of BMP formats are supported including black and white and true colour 24-bit images.

**Example:**
```basic
LOAD IMAGE "logo.bmp", 10, 20
```

**Cross-reference:** See [LOAD JPG](image_load_jpg.md) for loading JPG format images.
### LOAD JPG filename$ [, StartX, StartY]

Loads a JPG image from the Flash Filesystem or SD Card for display on an attached LCD display panel. This can be used to display photographs or high-quality compressed images.

**Parameters:**
- `filename$`: The JPG image file to load (file extension is optional - .JPG will be added if not specified)
- `StartX`: (Optional) X-coordinate of the top left corner where the image will be displayed (defaults to 0)
- `StartY`: (Optional) Y-coordinate of the top left corner where the image will be displayed (defaults to 0)

**Supported Formats:**
All types of JPG formats are supported including black and white and true colour 24-bit images.

**Example:**
```basic
LOAD JPG "photo.jpg", 0, 0
```

**Cross-reference:** See [LOAD IMAGE](image_load.md) for loading BMP format images.
## OPTION RESOLUTION nn [,cpuspeedinKhz]

*HDMI and VGA VERSIONS ONLY*
For firmware with HDMI video set the video resolution to `nn`.

Where `nn` is:

- `640x480` or `640`
- `720x400` or `720`
- `800x600` or `800` (RP2350 only)
- `848x480` or `848` (RP2350 only)
- `1280x720` or `1280` (HDMI only)
- `1024x768` or `1024` (HDMI only)

For `640x480` the display frequency can be set to 60Hz (252Mhz or 378MHz) or 75Hz (315MHz) by appending cpuspeedinKHz to the command (ie, `252000`, `378000` or `315000`).

Each VGA and HDMI resolution can operate in a number of modes which are set using the MODE command.

Note that `800x600` and `848x480` resolutions reduce both the maximum program size and the variable space available to the Basic programs


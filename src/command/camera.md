

### CAMERA

*not VGA or HDMI*

Command supporting the OV7670 camera module.

### CAMERA OPEN XLKpin, PLKpin, HSpin, VSCpin, RETpin, D0pin

This initialises the camera, It outputs a 12MHz clock on XLK (PWM) and checks that it is correctly receiving signals on PLK, VS, and HS.

The camera is set to a resolution of 160x120 (QQVGA) which is the maximum achievable within the limits of the available memory.

### CAMERA CAPTURE [scale, [x , y]]

This captures a picture from the camera (RGB565) and displays it on an LCD screen.

An SPI LCD must be connected and enabled in order for the command to work. (ILI9341 and ST7789_320 recommended). 

Scale defaults to 1 and x,y each to 0 By default a 160x120 image is output on the LCD with the top left at `0,0` on the LCD. Setting scale to `2` will fill a 320x240 display with the image.

Setting the `x` and `y` parameters will offset the top left of the image on the LCD. Update rate in a continuous loop is 7FPS onto the display at 1:1 scale and 5FPS scaled to 320x240. 

Assuming the display has MISO wired it is then possible to save the image to disk using the `SAVE IMAGE` command.

### CAMERA CLOSE

 Closes the camera subsystem and frees up all the pins allocated in the `CAMERA OPEN` command.

### CAMERA CHANGE image%(),change! [,scale [,x ,y]]

 The camera firmware is also able to detect motion in the camera's field of view using the command. It does this by operating the camera in YUV mode rather than RGB. This has the advantage that the intensity information and colour information are separated and just one byte is needed for a 256-level greyscale image which is ideal fer detecting movement.
 
 `image%` is an array of size 160x120 bytes (`DIM image%(160,120/8-1)`
 
 On calling the command it holds a packed 8-bit greyscale image. The change! variable returns the percentage the image has changed from the previous time the command was called.
 
 Optionally if `scale` is set then the image delta is output to the screen i.e. the difference between the previous image and this one. 
 
 As in the `CAPTURE` command the delta image can be scaled and positioned as required. If the scale parameter is omitted then the LCD is not updated by this command.

### CAMERA TEST tnum

 Enables or disables a test signal from the camera. `tnum=2` generates colourbars and `tnum=0` sets back to the visual input.

### CAMERA REGISTER reg%, data%

 Sets the register `reg%` in the camera to the value `data%`.
 
 When used the command will report to the console the previous value and automatically confirms that the new value has been set as requested.
 
 The colour rendition of the camera as initialised is reasonable but could probably be improved further by tuning the various camera registers.
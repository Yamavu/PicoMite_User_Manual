

### WII [CLASSIC] OPEN [,interrupt]

Opens a WII Classic controller and implements background polling of the device. The Wii Classic must be wired to the pins specified by OPTION SYSTEM I2C which is a prerequisite. Open attempts to talk to the Wii Classic and will return an error if not found. If found the firmware will sample the Wii data in the background at a rate of 50Hz. If an optional user interrupt is specified this will be triggered if any of the buttons changes (both on and off) See the DEVICE function for how to read data from the Wii Classic.

### WII [CLASSIC] CLOSE

CLOSE will stop the background polling and disable any interrupt specified

### WII NUNCHUCK OPEN [,interrupt]

Opens a WII Nunchuck controller and implements background polling of the device. The Wii Nunchuck must be wired to the pins specified by OPTION SYSTEM I2C which is a prerequisite. Open attempts to talk to the Wii Nunchuck and will return an error if not found. If found the firmware will sample the Wii data in the background at a

### WII NUNCHUCK CLOSE

CLOSE will stop the background polling and disable any interrupt specified WEBMITE ONLY
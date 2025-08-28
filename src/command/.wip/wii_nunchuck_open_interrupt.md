## WII NUNCHUCK OPEN [,interrupt]

Opens a WII Nunchuck controller and implements background polling of thedevice. The Wii Nunchuck must be wired to the pins specified by OPTIONSYSTEM I2C which is a prerequisite.Open attempts to talk to the Wii Nunchuck and will return an error if notfound. If found the firmware will sample the Wii data in the background at a
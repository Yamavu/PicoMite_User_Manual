### SETPIN pin, cfg [, option] 

Will configure an external I/O pin. Refer to the chapter [Using the I/O pins](../using_the_io_pins.md) for a general description of the Pico's input/output capabilities.

`pin` is the I/O pin to configure, `cfg` is the mode that the pin is to be set to and
`option` is an optional parameter. 

`cfg` is a keyword and can be any one of the following:

- `OFF` : Not configured or inactive
- `AIN` : Analog input (i.e. measure the voltage on the input).
- `ARAW` : Fast analog input returning a value between 0 and 4095.
- `DIN` : Digital input

  If `option` is omitted the input will be high impedance

  If `option` is the keyword "PULLUP" or “PULLDOWN” a constant current of about 50µA will be used to pull the input pin up or down to `3`.3V. Due to a bug in the RP2350 chips it is recommended that a pulldown be implemented using a `8`.2K or less resistor.
- `FIN` : Frequency input

  `option` can be used to specify the gate time (the length of time used to count the input cycles). It can be any number between 10 ms and 100000 ms. The PIN() function will always return the frequency correctly scaled in Hz regardless of the gate time used.

  If `option` is omitted the gate time will be `1` second.
  
  The pins can be GP6, GP7, GP8 or GP9 (can be changed with [OPTION COUNT](../option/count.md)).
- `PIN` : Period input
  
  `option` can be used to specify the number of input cycles to average the period measurement over. It can be any number between `1` and 10000. The PIN() function will always return the average period of one cycle correctly scaled in ms regardless of the number of cycles used for the average. If `option` is omitted the period of just one cycle will be used.
  
  The pins can be GP6, GP7, GP8 or GP9 (can be changed with [OPTION COUNT](../option/count.md)).
- `CIN` : Counting input
  
  `option` can be used to specify which edge triggers the count and if any pullup or pulldown is enabled 
  
  `2` specifies a falling edge with pullup,
  
  `3` specifies that both a falling and rising edge will trigger a count with no pullup applied,

  `5` specifies both edges but with a pullup applied.

  If `option` is omitted a rising edge will trigger the count. Due to a bug in the RP2350 chips pulldown is not recommended. 
  
  The pins can be GP6, GP7, GP8 or GP9 (can be changed with [OPTION COUNT](../option/count.md)).
- `DOUT` : Digital output
  
  `option` is not used in this mode.

The functions [PIN()](../function/pin.md) and [PORT()](../function/port.md) can also be used to return the value on one or more output pins. 

See the function PIN() for reading inputs and the statement PIN()= for setting an output. 

See the command below if an interrupt is configured.


### SETPIN pin, cfg, target [, option]

Will configure `pin` to generate an interrupt according to `cfg`. 

Any I/O pin capable of digital input can be configured to generate an interrupt with a maximum of ten interrupts configured at any one time.

`cfg` is a keyword and can be any one of the following: 
- `OFF` : Not configured or inactive INTH Interrupt on low to high input 
- `INTL` Interrupt on high to low input 
- `INTB` Interrupt on both (i.e. any change to the input) 

`target` is a user defined subroutine which will be called when the event happens. Return from the interrupt is via the [END SUB](../command/end.md#end-sub) or [EXIT SUB](../command/exit.md#exit-sub) commands. 

`option` is the same as used in [SETPIN pin DIN](#setpin-pin-cfg--option) (above). This mode also configures the pin as a digital input so the value of the pin can always be retrieved using the function PIN().

Refer to the chapter [Using the I/O pins](../using_the_io_pins.md) for a general description.

### SETPIN GP25, DOUT | HEARTBEAT

*NOT ON WEBMITE VERSION*

This version of SETPIN controls the on-board LED.

If it is configured as DOUT then it can be switched on and off under program control.

If configured as HEARTBEAT then it will flash 1s on, 1s off continually while powered. This is the default state and will be restored to this when the user program stops running.

### SETPIN p1[, p2 [, p3]], device

These commands are used for the pin allocation for special devices. Pins must be chosen from the pin designation diagram and must be allocated before the devices can be used. Note that the pins (eg, rx, tx, etc) can be declared in any order and that the pins can be referred to by using their pin number (eg, `1`, `2`) or GP number (eg, GP0, GP1).

Note that on the WebMite version:
* SPI1 and SPI2 are not available on `GP20` to `GP28` 
* COM1 and COM2 are not available on `GP20` to `GP28`
* I2C is not available on pin 34 (`GP28`)
* The following are not available; `GP29`, `GP25`, `GP24` and `GP23`

### SETPIN rx, tx, COM1

Allocate the pins to be used for serial port COM1.

Valid pins are 
* RX: `GP1`, `GP13` or `GP17` 
* TX: `GP0`, `GP12`, `GP16` or `GP28`

### SETPIN rx, tx, COM2

Allocate the pins to be used for serial port COM2. 

Valid pins are 
* RX: `GP5`, `GP9` or `GP21`
* TX: `GP4`, `GP8` or `GP20`

### SETPIN rx, tx, clk, SPI

Allocate the pins to be used for SPI port SPI. 

Valid pins are 
- RX: `GP0`, `GP4`, `GP16` or `GP20`
- TX: `GP3`, `GP7` or `GP19` CLK: `GP2`, `GP6` or `GP18`

### SETPIN rx, tx, clk, SPI2

Allocate the pins to be used for SPI port SPI2.

Valid pins are 
- RX: `GP8`, `GP12` or `GP28`
- TX: `GP11`, `GP15` or `GP27`
- CLK: `GP10`, `GP14` or `GP26`

### SETPIN sda, scl, I2C

Allocate the pins to be used for the I²C port I2C. 

Valid pins are
- SDA: `GP0`, `GP4`, `GP8`, `GP12`, `GP16`, `GP20` or `GP28`
- SCL: `GP1`, `GP5`, `GP9`, `GP13`, `GP17` or `GP21`

### SETPIN sda, scl, I2C2

Allocate the pins to be used for the I2C port I2C2. 

Valid pins are
- SDA: `GP2`, `GP6`, `GP10`, `GP14`, `GP18`, `GP22` or `GP26`
- SCL: `GP3`, `GP7`, `GP11`, `GP15`, `GP19` or `GP27`

### SETPIN pin, PWM[nx]

Allocate pin to PWMnx `n` is the PWM number (`0` to `7`) and `x` and is the channel (A or B). `n` and `x` are optional. 

The setpin can be changed until the PWM command is issued. At that point the pin becomes locked to PWM until `PWMn,OFF` is issued.

### SETPIN pin, IR

Allocate pins for InfraRed (IR) communications (can be any pin).

### SETPIN pin, PIOn

Reserve pin for use by a PIO0, PIO1 or PIO2 (RP2350 only) (see [Appendix F](../F_the_pio_programming_package.md) for PIO details).

### SETPIN GP1, FFIN [,gate]

*RP2350 ONLY*

Sets GP1 as a fast frequency input. 

Inputs up to the CPU speed /2 can be recorded.

`gate` can be used to specify the gate time (the length of time used to count the input cycles). It can be any number between 10 ms and 100000 ms.

The [PIN() function](../function/pin.md) will always return the frequency correctly scaled in Hz regardless of the gate time used. 

If `option` is omitted the gate time will be 1 second. 

The function uses PWM channel `0` to do the counting so it is incompatible with any other use of that PWM channel.

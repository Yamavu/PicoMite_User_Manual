

### SETPIN pin, cfg [, option] Will configure a a general descri 'pin' is the I/O 'option' is an o following:

 n external I/O pin. Refer to the chapter Using the I/O pins for ption of the Pico's input/output capabilities. pin to configure, ‘cfg’ is the mode that the pin is to be set to and ptional parameter. 'cfg' is a keyword and can be any one of the

### SETPIN pin, cfg, target [, option]

 Will configure ‘pin’ to generate an interrupt according to ‘cfg’. Any I/O pin capable of digital input can be configured to generate an interrupt with a maximum of ten interrupts configured at any one time. 'cfg' is a keyword and can be any one of the following: OFF Not configured or inactive INTH Interrupt on low to high input INTL Interrupt on high to low input INTB Interrupt on both (i.e. any change to the input) ‘target' is a user defined subroutine which will be called when the event happens. Return from the interrupt is via the END SUB or EXIT SUB commands. 'option' is the same as used in SETPIN pin DIN (above). This mode also configures the pin as a digital input so the value of the pin can always be retrieved using the function PIN(). Refer to the chapter Using the I/O pins for a general description. NOT ON WEBMITE VERSION

### SETPIN GP25, DOUT |

 This version of SETPIN controls the on-board LED.

### SETPIN p1[, p2 [, p3]], device

 These commands are used for the pin allocation for special devices. Pins must be chosen from the pin designation diagram and must be allocated before the devices can be used. Note that the pins (eg, rx, tx, etc) can be declared in any order and that the pins can be referred to by using their pin number (eg, 1, 2) or GP number (eg, GP0, GP1). Note that on the WebMite version:  SPI1 and SPI2 are not available on GP20 to GP28  COM1 and COM2 are not available on P20 to GP28  I2C is not available on pin 34 (GP28)  The following are not available; GP29, GP25, GP24 and GP23

### SETPIN rx, tx, COM1

 Allocate the pins to be used for serial port COM1. Valid pins are RX: GP1, GP13 or GP17 TX: GP0, GP12, GP16 or GP28

### SETPIN rx, tx, COM2

 Allocate the pins to be used for serial port COM2. Valid pins are RX: GP5, GP9 or GP21 TX: GP4, GP8 or GP20

### SETPIN rx, tx, clk, SPI

 Allocate the pins to be used for SPI port SPI. Valid pins are RX: GP0, GP4, GP16 or GP20 TX: GP3, GP7 or GP19 CLK: GP2, GP6 or GP18

### SETPIN rx, tx, clk, SPI2

 Allocate the pins to be used for SPI port SPI2. Valid pins are RX: GP8, GP12 or GP28 TX: GP11, GP15 or GP27 CLK: GP10, GP14 or GP26

### SETPIN sda, scl, I2C

 Allocate the pins to be used for the I2C port I2C. Valid pins are SDA: GP0, GP4, GP8, GP12, GP16, GP20 or GP28 SCL: GP1, GP5, GP9, GP13, GP17 or GP21

### SETPIN sda, scl, I2C2

 Allocate the pins to be used for the I2C port I2C2. Valid pins are SDA: GP2, GP6, GP10, GP14, GP18, GP22 or GP26 SCL: GP3, GP7, GP11, GP15, GP19 or GP27

### SETPIN pin, PWM[nx]

 Allocate pin to PWMnx 'n' is the PWM number (0 to 7) and 'x' and is the channel (A or B). n and x are optional. The setpin can be changed until the PWM command is issued. At that point the pin becomes locked to PWM until PWMn,OFF is issued.

### SETPIN pin, IR

 Allocate pins for InfraRed (IR) communications (can be any pin).

### SETPIN pin, PIOn

 Reserve pin for use by a PIO0, PIO1 or PIO2 (RP2350 only) (see Appendix F for PIO details). RP2350 ONLY

### SETPIN GP1, FFIN [,gate]

 Sets GP1 as a fast frequency input. Inputs up to the CPU speed /2 can be recorded. ‘gate’ can be used to specify the gate time (the length of time used to count the input cycles). It can be any number between 10 ms and 100000 ms. The PIN() function will always return the frequency correctly scaled in Hz regardless of the gate time used. If 'option' is omitted the gate time will be 1 second. The function uses PWM channel 0 to do the counting so it is incompatible with any other use of that PWM channel.
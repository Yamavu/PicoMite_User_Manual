## Trigonometric Functions

These functions perform trigonometric calculations and angle conversions, essential for geometry, physics, and graphics programming.

- [ACOS(number)](function/acos.md)
- [SIN(number)](function/sin.md)
- [ASIN(number)](function/asin.md)
- [TAN(number)](function/tan.md)
- [ATN(number)](function/atn.md)
- [ATAN2(y, x)](function/atan2.md)
- [COS(number)](function/cos.md)
- [DEG(radians)](function/deg.md)
- [RAD(degrees)](function/rad.md)

## String Functions

String functions manipulate text data, allowing you to convert, extract, search, and format strings for display and data processing.

See [STR](function/str.md) for comprehensive string documentation.

### String Conversion

- [STR$](function/str$.md)
- [STRING$](function/string$.md)
- [VAL](function/val.md)

### String Case Conversion

- [UCASE$](function/ucase$.md)
- [LCASE$](function/lcase$.md)

### String Extraction

- [LEFT$](function/left$.md)
- [MID$](function/mid$.md)
- [RIGHT$](function/right$.md)

### String Formatting & Utilities

- [SPACE$](function/space$.md)
- [TAB](function/tab.md)

### String Search

- [INSTR](function/instr.md)
- [LINSTR](function/linstr.md)

### Binary String Conversion

- [BIN2STR$](function/bin2str$.md)
- [STR2BIN](function/str2bin.md)

### Long String Operations

- [LGETSTR$](function/lgetstr$.md)

### Additional String Functions

- [ASC](function/asc.md)
- [CHR$](function/chr$.md)
- [LEN](function/len.md)
- [JSON$](function/json$.md)

## Binary Functions

These functions handle binary, hexadecimal, and octal number conversions, as well as bit manipulation operations.

- [BIT](function/bit.md)
- [BIN$](function/bin$.md)
- [BYTE](function/byte.md)
- [HEX$](function/hex$.md)
- [OCT$](function/oct$.md)

## MMBasic Functions

Special functions that provide access to MMBasic's internal capabilities and evaluation features.

- [CALL](function/call.md)
- [CHOICE](function/choice.md)
- [EVAL](function/eval.md)

## Time and Date Functions

Functions for retrieving and manipulating time and date information from the system clock.

See [Date & Time](function/datetime_time.md) for comprehensive date and time documentation.

### Date Functions

- [DATE$](function/date.md)
- [DATETIME$](function/datetime$.md)
- [DAY$](function/day_date.md)

### Time Functions

- [TIMER](function/timer.md)

### Time System Functions

- [EPOCH](function/epoch.md)

## DEVICE functions

Functions for interfacing with external devices such as game controllers, mice, and Wii controllers.

- [DEVICE(GAMEPAD)](function/device_gamepad.md)
- [DEVICE(MOUSE)](function/device_mouse.md)
- [DEVICE(WII CLASSIC)](function/device_wii_classic.md)
- [DEVICE(WII NUNCHUCK)](function/device_wii_nunchuck.md)
- [FIELD$](function/field$.md)
- [FLAG](function/flag.md)
- [FORMAT$](function/format$.md)
- [GETSCANLINE](function/getscanline.md)

## GPS functions

The GPS functions are used to return data from a serial communications channel opened as GPS. The function GPS(VALID) should be checked before any of these functions are used to ensure that the returned value is valid.

See [GPS](function/gps.md) for comprehensive GPS documentation.

### Position Functions

- [GPS(LATITUDE)](function/gps_latitude.md)
- [GPS(LONGITUDE)](function/gps_longitude.md)
- [GPS(ALTITUDE)](function/gps_altitude.md)

### Time Functions

- [GPS(DATE)](function/gps_date.md)
- [GPS(TIME)](function/gps_time.md)

### Navigation Functions

- [GPS(SPEED)](function/gps_speed.md)
- [GPS(TRACK)](function/gps_track.md)

### Quality and Accuracy Functions

- [GPS(FIX)](function/gps_fix.md)
- [GPS(SATELLITES)](function/gps_satellites.md)
- [GPS(DOP)](function/gps_dop.md)
- [GPS(GEOID)](function/gps_geoid.md)

### Status Functions

- [GPS(VALID)](function/gps_valid.md)

## Input Event functions

Functions for handling keyboard and input device events, including key presses and input buffering.

- [INKEY$](function/inkey$.md)
- [INPUT$](function/input$.md)
- [KEYDOWN](function/keydown.md)

## Longstring functions

Specialized functions for working with [long strings](long_strings.md), providing comparison, extraction, and manipulation capabilities.

- [LCOMPARE](function/lcompare.md)
- [LGETBYTE](function/lgetbyte.md)
- [LGETSTR$](function/lgetstr$.md)
- [LINSTR](function/linstr.md)
- [LLEN](function/llen.md)

## File and Memory Functions

Functions for file operations, directory navigation, and memory access including peeking at memory locations.

- [CWD$](function/cwd$.md)
- [DIR$](function/dir$.md)
- [EOF](function/eof.md)
- [LOC](function/loc.md)
- [LOF](function/lof.md)
- [PEEK](function/peek.md)

## Numeric Functions

Basic mathematical and numeric manipulation functions including rounding, logarithms, and random numbers.

- [CINT](function/cint.md)
- [EXP](function/exp.md)
- [LOG](function/log.md)
- [INT](function/int.md)
- [MAX](function/max.md)
- [MIN](function/min.md)
- [PI](function/pi.md)
- [RND](function/rnd.md)
- [SGN](function/sgn.md)
- [SQR](function/sqr.md)

## MATH functions

The math function performs many simple mathematical calculations that can be
programmed in Basic but there are speed advantages to coding looping
structures in C and there is the advantage that once debugged they are there for
everyone without re-inventing the wheel.

See [MATH](function/math.md) for comprehensive documentation.

### Trigonometric & Logarithmic Functions

- [MATH(ATAN3)](function/math_atan3.md)
- [MATH(COSH)](function/math_cosh.md)
- [MATH(LOG10)](function/math_log10.md)
- [MATH(SINH)](function/math_sinh.md)
- [MATH(TANH)](function/math_tanh.md)

### Random & Encoding Functions

- [MATH(RAND)](function/math_rand.md)
- [MATH(BASE64)](function/math_base64.md)
- [MATH(CRCn)](function/math_crcn.md)

### Basic Statistical Functions

- [MATH(MEAN)](function/math_mean.md)
- [MATH(MEDIAN)](function/math_median.md)
- [MATH(SUM)](function/math_sum.md)
- [MATH(SD)](function/math_sd.md)
- [MATH(MIN)](function/math_min.md)
- [MATH(MAX)](function/math_max.md)

### Advanced Statistical Functions

- [MATH(CHI)](function/math_chi.md)
- [MATH(CHI_p)](function/math_chi_p.md)
- [MATH(CORREL)](function/math_correl.md)
- [MATH(CROSSING)](function/math_crossing.md)

### Vector & Matrix Operations

- [MATH(MAGNITUDE)](function/math_magnitude.md)
- [MATH(DOTPRODUCT)](function/math_dotproduct.md)
- [MATH(M_DETERMINANT)](function/math_m_determinant.md)

### Control Systems

- [MATH(PID)](function/math_pid.md)

## Array functions

Functions for array manipulation and statistical calculations, including bounds checking and mathematical operations on arrays.

- [BOUND](function/bound.md)

## Graphics functions

Functions for graphics operations including color manipulation and pixel/screen coordinate mapping.

- [MAP](function/map.md)
- [PIXEL](function/pixel.md)
- [RGB](function/rgb.md)

## I/O Functions

Functions for input/output operations including port access, pulse measurement, and SPI communication.

- [PORT](function/port.md)
- [PULSIN](function/pulsin.md)
- [SPI](function/spi.md)
- [PIN](function/pin.md)

## PIO Functions

The PIO (Programmable I/O) functions provide access to the Raspberry Pi Pico's PIO hardware for advanced I/O operations.

see also [Appendix F – The PIO Programming Package](../F_the_pio_programming_package.md)

See [PIO](function/pio.md) for comprehensive documentation.

### Register Reading Functions

- [PIO(FSTAT)](function/pio_fstat.md)
- [PIO(FDEBUG)](function/pio_fdebug.md)
- [PIO(FLEVEL)](function/pio_flevel.md)

### DMX Functions

- [PIO(DMX RX)](function/pio_dmx_rx.md)
- [PIO(DMX TX)](function/pio_dmx_tx.md)

### Helper Functions for INIT MACHINE

- [PIO(EXECCTRL)](function/pio_execctrl.md)
- [PIO(PINCTRL)](function/pio_pinctrl.md)
- [PIO(SHIFTCTRL)](function/pio_shiftctrl.md)

## SPRITE functions

*VGA AND HDMI VERSIONS ONLY*

The SPRITE functions return information regarding sprites which are small graphic images on the VGA/HDMI screen. These are useful when writing games. See also the [SPRITE commands](../command/sprite.md).

See [SPRITE](function/sprite.md) for comprehensive documentation.

### Position & Dimensions

- [SPRITE(X)](function/sprite_x.md)
- [SPRITE(Y)](function/sprite_y.md)
- [SPRITE(W)](function/sprite_w.md)
- [SPRITE(H)](function/sprite_h.md)

### Collision & Contact Detection

- [SPRITE(C)](function/sprite_c.md)
- [SPRITE(T)](function/sprite_t.md)
- [SPRITE(E)](function/sprite_e.md)

### Sprite Management

- [SPRITE(N)](function/sprite_n.md)
- [SPRITE(N,n)](function/sprite_n_layer.md)
- [SPRITE(L)](function/sprite_l.md)
- [SPRITE(S)](function/sprite_s.md)

### Distance & Vector Operations

- [SPRITE(D)](function/sprite_d.md)
- [SPRITE(V)](function/sprite_v.md)

## Misc functions

Miscellaneous utility functions for handling optional devices including distance sensors, temperature sensors, and touch screens.

- [DISTANCE](function/distance.md)
- [TEMPR](function/tempr.md)

### TOUCH Functions

See [TOUCH](function/touch.md) for comprehensive documentation.

#### Touch Coordinates

- [TOUCH(X)](function/touch_x.md)
- [TOUCH(Y)](function/touch_y.md)

#### Multi-touch Coordinates (FT6336)

- [TOUCH(X2)](function/touch_x2.md)
- [TOUCH(Y2)](function/touch_y2.md)





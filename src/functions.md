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

- [STR$](function/str$.md)
- [UCASE$](function/ucase$.md)
- [LCASE$](function/lcase$.md)
- [ASC](function/asc.md)
- [CHR$](function/chr$.md)
- [VAL](function/val.md)
- [STRING$](function/string$.md)
- [LEFT$](function/left$.md)
- [MID$](function/mid$.md)
- [RIGHT$](function/right$.md)
- [LEN](function/len.md)
- [SPACE$](function/space$.md)
- [TAB](function/tab.md)
- [JSON$](function/json$.md)

## Binary Functions

These functions handle binary, hexadecimal, and octal number conversions, as well as bit manipulation operations.

- [BIT](function/bit.md)
- [BIN$](function/bin$.md)
- [BIN2STR$](function/bin2str$.md)
- [STR2BIN](function/str2bin.md)
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

- [DATE$](function/date$.md)
- [DATETIME$](function/datetime$.md)
- [DAY$](function/day$.md)
- [EPOCH](function/epoch.md)
- [TIME$](function/time$.md)
- [TIMER](function/timer.md)

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

The GPS functions are used to return data from a serial communications
channel opened as GPS.

The function GPS(VALID) should be checked before any of these functions are
used to ensure that the returned value is valid.

- [GPS(ALTITUDE)](function/gps_altitude.md)
- [GPS(DATE)](function/gps_date.md)
- [GPS(DOP)](function/gps_dop.md)
- [GPS(FIX)](function/gps_fix.md)
- [GPS(GEOID)](function/gps_geoid.md)
- [GPS(LATITUDE)](function/gps_latitude.md)
- [GPS(LONGITUDE)](function/gps_longitude.md)
- [GPS(SATELLITES)](function/gps_satellites.md)
- [GPS(SPEED)](function/gps_speed.md)
- [GPS(TIME)](function/gps_time.md)
- [GPS(TRACK)](function/gps_track.md)
- [GPS(VALID)](function/gps_valid.md)

## Input Event functions

Functions for handling keyboard and input device events, including key presses and input buffering.

- [INKEY$](function/inkey$.md)
- [INPUT$](function/input$.md)
- [INSTR](function/instr.md)
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

- [MATH(ATAN3)](function/math_atan3.md)
- [MATH(COSH)](function/math_cosh.md)
- [MATH(LOG10)](function/math_log10.md)
- [MATH(SINH)](function/math_sinh.md)
- [MATH(TANH)](function/math_tanh.md)
- [MATH(CRCn)](function/math_crcn.md)
- [MATH(RAND)](function/math_rand.md)

## Array functions

Functions for array manipulation and statistical calculations, including bounds checking and mathematical operations on arrays.

- [BOUND](function/bound.md)
- [MATH(CHI)](function/math_chi.md)
- [MATH(CHI_p)](function/math_chi_p.md)
- [MATH(CROSSING)](function/math_crossing.md)
- [MATH(CORREL)](function/math_correl.md)
- [MATH(MAX)](function/math_max.md)
- [MATH(MEAN)](function/math_mean.md)
- [MATH(MEDIAN)](function/math_median.md)
- [MATH(MIN)](function/math_min.md)
- [MATH(SD)](function/math_sd.md)
- [MATH(SUM)](function/math_sum.md)
- [MATH(MAGNITUDE)](function/math_magnitude.md)
- [MATH(DOTPRODUCT)](function/math_dotproduct.md)
- [MATH(M_DETERMINANT)](function/math_m_determinant.md)
- [MATH(PID)](function/math_pid.md)
- [MATH(BASE64)](function/math_base64.md)

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

see also [Appendix F – The PIO Programming Package](../F_the_pio_programming_package.md)

- [PIO(DMX RX)](function/pio_dmx_rx.md)
- [PIO(DMX TX)](function/pio_dmx_tx.md)
- [PIO(EXECCTRL)](function/pio_execctrl.md)
- [PIO(FDEBUG)](function/pio_fdebug.md)
- [PIO(FLEVEL)](function/pio_flevel.md)
- [PIO(FSTAT)](function/pio_fstat.md)
- [PIO(PINCTRL)](function/pio_pinctrl.md)
- [PIO(SHIFTCTRL)](function/pio_shiftctrl.md)

## SPRITE functions

*VGA AND HDMI VERSIONS ONLY*

The SPRITE functions return information regarding sprites which are small
graphic images on the VGA/HDMI screen. These are useful when writing
games. See also the [SPRITE commands](../command/sprite.md).

- [SPRITE(C)](function/sprite_c.md)
- [SPRITE(D)](function/sprite_d.md)
- [SPRITE(E)](function/sprite_e.md)
- [SPRITE(H)](function/sprite_h.md)
- [SPRITE(L)](function/sprite_l.md)
- [SPRITE(N)](function/sprite_n.md)
- [SPRITE(N,n)](function/sprite_n_layer.md)
- [SPRITE(S)](function/sprite_s.md)
- [SPRITE(T)](function/sprite_t.md)
- [SPRITE(V)](function/sprite_v.md)
- [SPRITE(W)](function/sprite_w.md)
- [SPRITE(X)](function/sprite_x.md)
- [SPRITE(Y)](function/sprite_y.md)

## Misc functions

Miscellaneous utility functions for handling optional devices including distance sensors, temperature sensors, and touch screens.

- [DISTANCE](function/distance.md)
- [TEMPR](function/tempr.md)
- [TOUCH(X)](function/touch_x.md)
- [TOUCH(Y)](function/touch_y.md)
- [TOUCH(X2)](function/touch_x2.md)
- [TOUCH(Y2)](function/touch_y2.md)





# MATH

The math command performs many simple mathematical calculations that can be programmed in BASIC but there are speed advantages to coding looping structures in the firmware and there is the advantage that once debugged they are there for everyone without re-inventing the wheel. 

2-dimensional maths matrices are always specified `DIM matrix(n_columns, n_rows)` ( the dimensions respect [OPTION BASE](../option/base.md) ).

Quaternions are stored as a 5 element array w, x, y, z, magnitude.

### MATH RANDOMIZE [n]

Seeds the Mersenne Twister algorithm. If n is not specified the seed is the time in microseconds since boot The Mersenne Twister algorithm gives a much better random number than the C-library inbuilt function

## Simple array arithmetic

### MATH SET nbr, array()

See [ARRAY SET](array.md)

### MATH SCALE in(), scale ,out()

This scales the matrix in() by the scalar scale and puts the answer in out(). Works for arrays of any dimensionality of both integer and float and can convert between. Setting b to 1 is optimised and is the fastest way of copying an entire array.

### MATH ADD in(), num ,out()

See {ARRAY ADD}(array.md)

### MATH INTERPOLATE in1(), in2(), ratio, out()

This command implements the following equation on every array element: out = (in2 - in1) * ratio + in1 Arrays can have any number of dimensions and must be distinct and have the same number of total elements. The command works with both integer and floating point arrays in any mixture

### MATH WINDOW in(), T minout, maxout, out() [,minin!, “ maxin!] m ( N b e

his command takes the `in` array and scales it between `minout` and maxout” returning the answer in `out`. Optionally, it can also return the inimum and maximum floating point values found in the original data `minin!` and `maxin!`). ote: `minout` can be greater than `maxout` and in this case the data will be oth scaled and inverted. .g

### MATH SLICE sourcearray(), [d1] [,d2] [,d3] [,d4] [,d5] , destinationarray()

See [ARRAY SLICE](array.md)

### MATH INSERT targetarray(), [d1] [,d2] [,d3] [,d4] [,d5] , sourcearray()

See [ARRAY INSERT](array.md)

### MATH POWER inarray(), power, outarray()

Raises each element in `inarray()` to the `power` defined and puts the output in `outarray()`

### MATH SHIFT inarray%(), nbr, outarray%() [,U]

This command does a bit shift on all elements of inarray%() and places the result in outarray%() (may be the same as inarray%()). nbr can be between -63 and 63. Positive numbers are a left shift (multiply by power of 2). Negative number are a right shift. The optional parameter ,U will force an unsigned shift.

## Matrix arithmetic

### MATH M_INVERSE array!(), inversearray!()

This returns the inverse of `array!()` in `inversearray!()`. The array must be square and you will get an error if the array cannot be inverted (determinant=0). 

`array!()` and `inversearray!()` cannot be the same.

### MATH M_PRINT array()

Quick mechanism to print a 2D matrix one row per line.

### MATH M_TRANSPOSE in(), out()

Transpose matrix in() and put the answer in matrix out(), both arrays must be 2D but need not be square. 

If not square then the arrays must be dimensioned in(m,n) out(n,m) .

### MATH M_MULT in1(), in2(), out()

Multiply the arrays in1() and in2() and put the answer in out()c.

All arrays must be 2D but need not be square. If not square then the arrays must be dimensioned in1(m,n) in2(p,m) ,out(p,n)

### MATH V_PRINT array() [,hex]

Quick mechanism to print a small array on a single line. `hex` will print in hex.

### MATH V_NORMALISE inV(), outV()

Converts a vector `inV()` to unit scale and puts the answer in `outV()` 

Unit scale scales the elements of the vector so (sqr(x*x + y*y +...)=1 is true.

There is no limit on number of elements in the vector.

### MATH V_MULT matrix(), inV(), outV()

Multiplies `matrix()` and vector `inV()` returning vector `outV()`. The vectors and the 2D matrix can be any size but must have the same cardinality.

### MATH V_CROSS inV1(), inV2(), outV()

Calculates the cross product of two three element vectors `inV1()` and `inV2()` and puts the answer in `outV()`

### MATH V_ROTATE x, y, a, xin(), yin(), xout(), yout()

This command rotates the coordinate pairs in `xin()` and `yin()` around the centre point defined by `x` and `y` by the angle `a` and puts the results in `xout()` and `yout()`. 

The input and output arrays can be the same and the rotation angle is, by default, in radians but this can be changed using the [OPTION ANGLE](../option/angle.md) command.

## Quaternion arithmetic

### MATH Q_INVERT inQ(), outQ()

Invert the quaternion in `inQ()` and put the answer in `outQ()`

### MATH Q_VECTOR x, y, z, outVQ()

Converts a vector specified by x , y, and z to a normalised quaternion vector `outVQ()` with the original magnitude stored

### MATH Q_CREATE theta, x, y, z, outRQ()

Generates a normalised rotation quaternion `outRQ()` to rotate quaternion vectors around axis x,y,z by an angle of theta. Theta is specified in radians.

### MATH Q_EULER yaw, pitch, roll, outRQ()

Generates a normalised rotation quaternion `outRQ()` to rotate quaternion vectors as defined by the yaw, pitch and roll angles With the vector in front of the `viewer` yaw is looking from the top of the ector and rotates clockwise, pitch rotates the top away from the camera and roll rotates around the z-axis clockwise. The yaw, pitch and roll angles default to radians but respect the setting of [OPTION ANGLE](../option/angle.md)

### MATH Q_MULT inQ1(), inQ2(), outQ()

Multiplies two quaternions `inQ1()` and `inQ2()` and puts the answer in `outQ()`

### MATH Q_ROTATE , RQ(), inVQ(), outVQ()

Rotates the source quaternion vector `inVQ()` by the rotate quaternion `RQ()` and puts the answer in `outVQ()`

## Matric Cell Operations

These commands do cell by cell operations (hence C_) on
identically sized arrays. There are no restrictions on the
number of dimensions and no restrictions on using the
same array twice or even three times in the parameters.

The datatype must be the same for all the arrays.

`MATH C_MUL a%(),a%(),a%()` will square all the values in the array `a%()`

### MATH C_ADD array1%(), array2%(), array3%() 


### MATH C_SUB array1%(), array2%(), array3%() 


### MATH C_MUL array1%(), array2%(), array3%() 


### MATH C_DIV array1%(), array2%(), array3%() 


### MATH C_ADD array1!(), array2!(), array3!() 


### MATH C_SUB array1!(), array2!(), array3!()


### MATH C_MUL array1!(), array2!(), array3!()


### MATH C_DIV array1!(), array2!(), array3!()


## Fast Fourier Transform

### MATH FFT signalarray!(),

Performs a fast fourier transform of the data in `signalarray!`. "signalarray"

### MATH FFT INVERSE

Performs an inverse fast fourier transform of the data in `FFTarray!`.

### MATH FFT MAGNITUDE signalarray!(),magnitudearray! ()

Generates magnitudes for frequencies for the data in `signalarray!` "signalarray" must be floating point and the size must be a power of 2 (eg, s(1023) assuming [OPTION BASE](../option/base.md) is zero). "magnitudearray" must be floating point and the size must be the same as the signal array The command will return the magnitude of the signal at various frequencies according to the formula:

### MATH FFT PHASE signalarray!(), phasearray!()

Generates phases for frequencies for the data in `signalarray!`. "signalarray" must be floating point and the size must be a power of 2 (eg, s(1023) assuming [OPTION BASE](../option/base.md) is zero). "phasearray" must be floating point and the size must be the same as the signal array The command will return the phase angle of the signal at various frequencies according to the formula above.

### MATH SENSORFUSION type ax, ay, az, gx, gy, gz, mx, my, mz, pitch, roll, yaw [,p1] [,p2]

Type can be `MAHONY` or `MADGWICK`

`ax`, `ay`, and `az` are the accelerations in the three directions and should be specified in units of standard gravitational acceleration.

`gx`, `gy`, and `gz` are the instantaneous values of rotational speed which should be specified in radians per second. 

`mx`, `my`, and `mz` are the magnetic fields in the three directions and should be specified in nano-Tesla (nT).

Care must be taken to ensure that the x, y and z components are consistent between the three inputs. So, for example, using the MPU-9250 the correct input will be ax, ay, az, gx, gy, gz, my, mx, -mz based on the reading from the sensor. 

Pitch, roll and yaw should be floating point variables and will contain the outputs from the sensor fusion. The `SENSORFUSION` routine will automatically measure the time between consecutive calls and will use this in its internal calculations.

The Madwick algorithm takes an optional parameter `p1`. This is used as beta in the calculation. It defaults to 0.5 if not specified.

The Mahony algorithm takes two optional parameters `p1`, and `p2`. These are used as Kp and Ki in the calculation. If not specified these default to 10.0 and 0.0 respectively. 

A fully worked example of using the code is given on the BackShed forum at: https://www.thebackshed.com/forum/ViewTopic.php?TID=13459&PID=166962#166962


### MATH PID INIT channel, pid_params!(), callback

This command sets up a PID controller that can work automatically in the background. Up to 8 PID controllers can run simultaneously (channels 1 to 8)

`callback` is a MMbasic subroutine which is called at the rate defined by the sample time. 

See the `MATH(PID …)` function for details of what should be included in the subroutine. The `pid_params!()` array must be dimensioned for all the listed elements, including the controller memory parameters (`DIM pid_params!(13)`) and be initialised with the required settings.

PID configuration
- Element 0 = Kp
- Element 1 = Ki 
- Element 2 = Kd
-  Element 3 = tau ' Derivative low-pass filter time constant
- Element 4 = limMin 'Output limits
- Element 5 = limMax
- Element 6 = limMinInt 'Integrator limits
- Element 7 = limMaxInt
- Element 8 = T 'Sample time (in seconds) 

Controller "memory"

- Element 9 = integrator
- Element 10 = prevError
- Element 11 = differentiator
- Element 12 = prevMeasurement
- Element 13 = out

### MATH PID START channel

Starts a previously initialised PID controller on the channel specified

### MATH PID STOP channel

Stops a previously initialised PID controller on the channel specified and deletes the internal data structures 

See https://www.thebackshed.com/forum/ViewTopic.php?FID=16&TID=17263 for an example of setting up and running a PID controller.

### MATH AES128 ENCRYPT/DECRYPT CBC/ECB/CTR key$/key(), in$/in(), out$/out() [,iv$/iv()]

This command encrypts or decrypts the data in `in` and puts the answer in `out` using the AES128 encryption method specified.

The parameters can each be either a string, integer array, or float array with any mix possible.

The key must be 16 elements long (16*8=128bits), in and out must be a multiple of 16 elements long. In the case of out being specified as a string (e.g. `out$`), the string variable must exist and should be set to empty (`DIM out$=""`).

The maximum number of elements in `in` and `out` is limited by memory when
defined as arrays. Strings for encrypting are limited to 240bytes (EBR) and
224bytes (CTR and CBC).

For CBC and CTR encryption you can optionally specify an initialisation vector `iv`. `iv` must be 16 elements long (16*8=128bits). If an initialisation vector is not specified encryption will generate a random initialisation vector.

In both cases the output is prepended with the IV.

For CBC and CTR, decryption requires that the first 16 elements of the input are the initialisation vector.

In the case where you want to transmit a message without IV you should remove the IV before sending the message using standard MMBasic manipulations. In this case the recipient must know the IV as well as the key and create a complete message before using `DECRYPT` by prepending the IV to the incoming message.
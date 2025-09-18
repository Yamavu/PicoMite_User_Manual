## Infrared Remote Control Decoder

You can easily add a remote control to your project using the IR command. When enabled this function will run in the background and interrupt the running program whenever a key is pressed on the IR remote control.

It will work with any NEC or Sony compatible remote controls including ones that generate extended IR Receiver messages. Most cheap programmable remote controls will generate either protocol and using one of these you 3.3V can add a sophisticated flair to your Pico based project.

The NEC protocol is also used by many other PicoMite manufacturers including Apple, Pioneer, Sanyo, Akai and Toshiba so their branded remotes can be used.

To detect the IR signal you need an IR receiver. NEC remotes use a 38kHz modulation of the IR signal and suitable receivers tuned to this frequency include the Vishay TSOP4838, Jaycar ZD1952 and Altronics Z1611A. Note that the I/O pins on the Raspberry Pi Pico are only 3.3V tolerant and so the receiver must be powered by a maximum of 3.3V. The Raspberry Pi Pico 2 is different and can withstand 5V.

Sony remotes use a 40 kHz modulation but receivers for this frequency can be hard to find. Generally 38 kHz receivers will work but maximum sensitivity will be achieved with a 40 kHz receiver.

The IR receiver can be connected to any pin on the Raspberry Pi Pico. This pin must be configured by the program using the command `SETPIN n, IR` where `n` is the I/O pin to use for this function.

To setup the decoder you use the command `IR dev, key, interrupt`. Where `dev` is a variable that will be updated with the device code and `key` is the variable to be updated with the key code. `interrupt` is the interrupt subroutine to call when a new key press has been detected. The IR decoding is done in the background and the program will continue after this command without interruption.

This is an example of using the IR decoder connected to the GP6 pin:

```basic
SETPIN GP6, IR               ' define the pin to be used
DIM INTEGER DevCode, KeyCode ' variables used by the decoder 
IR DevCode, KeyCode, IRInt   ' start the IR decoder 
DO
  ' < body of the program >
LOOP

SUB IRInt                    ' a key press has been detected
  PRINT "Received device = " DevCode " key = " KeyCode
END SUB
```

IR remote controls can address many different devices (VCR, TV, etc) so the program would normally examine the device code first to determine if the signal was intended for the program and, if it was, then take action based on the key pressed. There are many different devices and key codes so the best method of determining what codes your remote generates is to use the above program to discover the codes.

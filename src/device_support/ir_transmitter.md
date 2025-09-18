## Infrared Remote Control Transmitter

<div style="float: right; margin-left: 20px;">
  <img src="../img/12_IR_circuit.png" alt="IR circuit example" width="250">
</div>

Using the IR SEND command you can transmit a 12 bit Sony infrared remote control signal. This is intended for Raspberry Pi Pico to Raspberry Pi Pico or Micromite communications but it will also work with Sony equipment that uses 12 bit codes. Note that all Sony products require that the message be sent three times with a 26 ms delay between each message.

The circuit on the right illustrates what is required. The transistor is used to drive the infrared LED because the output capability of the Raspberry Pi Pico is limited. This circuit provides about 50 mA to the LED.

To send a signal you use the command `IR SEND pin, dev, key`

Where pin is the I/O pin used, dev is the device code to send and key is the key code. Any I/O pin on the Raspberry Pi Pico can be used and you do not have to set it up beforehand (IR SEND will automatically do that).

The modulation frequency used is 38 kHz and this matches the common IR receivers (described in the previous page) for maximum sensitivity when communicating between two Raspberry Pi Picos or with a Micromite.<br style="clear:both" />


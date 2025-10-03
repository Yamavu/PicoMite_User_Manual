.wip


### DEVICE BITSTREAM pinno, n_transitions, array%()

This command is used to generate an extremely accurate bit sequence on the pin specified. The pin must have previously been set up as an output and set to the required starting level. Notes:  The array contains the length of each level in the bitstream in microseconds. The maximum period allowed is 65.5 mSec  The first transition will occur immediately on executing the command.  The last period in the array is ignored other than defining the time before control returns to the program or command line.  The pin is left in the starting state if the number of transitions is even and the opposite state if the number of transitions is odd.

### DEVICE CAMERA

See CAMERA command

### DEVICE GAMEPAD

See GAMEPAD command

### DEVICE HUMID

See HUMID command

### DEVICE KEYPAD

See KEYPAD command

### DEVICE MOUSE

See MOUSE command

### DEVICE LCD

See LCD command

### DEVICE SERIALTX pinno, baudrate, ostring$

Outputs 'ostring$' as a serial data stream on 'pinno'. 'baudrate' can be between 110 and 230400 (230400 may need CPU to be overclocked). Note that the program will halt and interrupts ignored during transmission.

### DEVICE SERIALRX pinno, baudrate, istring$, timeout_in_ms, status% [,nbr] [,terminators$]

Inputs serial data on ‘pinno’. ‘baudrate’ can be between 110 and 230400 (230400 may need CPU to be overclocked). ‘status%’ returns: -1 = timeout (Note: use LEN(istring$) to see number of chars received) 2 = number of characters requested satisfied 3 = terminating character satisfied ‘nbr’ specifies the number of characters to be received before the command returns. ‘terminators$’ specifies one or more signle characters that can be used to terminate reception. The program will halt and interrupts ignored while this command is executing.

### DEVICE WII

See WII command

### DEVICE WS2812

See WS2812 command
## PIO DMA RX pio, sm, nbr, data%() [,completioninterrupt] [,transfersize] [,loopbackcount]

Sets up DMA transfers from PIO to MMBasic memory.pio specifies which of the two pio instances to use (0 or 1).sm specifies which of the state machine to use (0-3).nbr specifies how many 32-bit words to transfer. See below for the special case
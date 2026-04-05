### PIO

The processors chip in the Raspberry Pi Pico with the RP2040 processors contains a programmable I/O system with two identical PIO devices (pio%=0 or pio%=1) acting like specialised CPU cores. The Raspberry Pi Pico 2 with the RP2350 processors has three PIO devices. See the Appendix F for a more detailed description of programming PIOs.

### PIO assemble pio,linedata$

This command will assemble and load text based PIO assembler code including labels for jumps. Use: PIO assemble pio,".program anything" to initialise the assembler. Use: PIO assemble pio,".side_set n [opt] [pindirs]" if using side set. This is mandatory in order to correctly construct the op-codes if one or more side set pins are used. It does not load the pinctrl register as this is specific to the state-machine. Also note the "opt" parameter changes the op-code on instructions that have a side parameter. Use: PIO assemble pio,".line n" to assemble starting from a line other than 1 - this is optional. Use: PIO assemble pio,".end program [list]" to terminate the assembly and program the pio. The optional parameter LIST causes a hex dump of the op- codes to the terminal. Use: PIO assemble pio,"label:" to define a label. This must appear as a separate command. Use: PIO assemble “’.wrap target” to specify where the program will wrap to. See PIO(.wrap target) for how to use this. Use: PIO assemble “.wrap” to specify where the program should wrap back to from “.wrap target” . See PIO(.wrap) for how to use this. Use: PIO assemble pio "instruction [parameters]" to define the actual PIO instructions that will be converted to machine code.

### PIO DMA RX pio, sm, nbr, data%() [,completioninterrupt] [,transfersize] [,loopbackcount]

Sets up DMA transfers from PIO to MMBasic memory. pio specifies which of the two pio instances to use (0 or 1). sm specifies which of the state machine to use (0-3). nbr specifies how many 32-bit words to transfer. See below for the special case

### PIO DMA TX pio, sm, nbr, data%() [,completioninterrupt] [,transfersize] [,loopbackcount]

of setting nbr to zero. data%() is the array that will either supply or receive the PIO data. The optional parameter completioninterrupt is the name of a MMBasic subroutine rthat will be called when the DMA completes and in the case of DMA_OUT the FIFO has been emptied. If the optional interrupt is not used then the status of the DMA can be checked using the functions: MM.INFO(PIO RX DMA) MM.INFO(PIO TX DMA) The optional parameter transfersize allows the user to override the normal 32- bit transfers and select 8, 16, or 32. The optional parameter loopbackcount specifies how many data items are to be read or written before the DMA starts again at the beginning of the buffer. The parameter must be a power of 2 between 2 and 32768. Due to a limitation in the RP2040/RP2350 if loopbackcount is used the MMBasic array must be aligned in memory to the number of bytes in the loop. Thus if the array is 64 integers long which is 512 bytes then the array must be aligned to a 512byte boundary in memory. All MMBasic arrays are aligned to a 256 byte boundary but to create an array which is guaranteed to be aligned to a 512 byte boundary or greater the PIO MAKE RING BUFFER command must be used. If loopbackcount is set then “nbr” can be set to 0. In this case the transfer will run continuously repeatedly filling the buffer until explicitly stopped.

### PIO DMA RX OFF

Aborts a running DMA.

### PIO DMA TX OFF



### PIO INTERRUPT pio, sm [,RXinterrupt] [,TXinterrupt]

Sets Basic interrupts for PIO activity. Use the value 0 for RXinterrupt or TXinterrupt to disable an interrupt. Omit values not needed. The RX interrupt triggers whenever a word has been "pushed" by the PIO code into the specified FIFO. The data MUST be read in the interrupt to clear it. The TX interrupt triggers whenever the specified FIFO has been FULL and the PIO code has now "pulled" it

### PIO INIT MACHINE pio%, statemachine%, clockspeed [,pinctrl] [,execctrl] [,shiftctrl] [,startinstruction] [,sideout [,setout] [,outout]

Initialises PIO 'pio%' with state machine 'statemachine%'. 'clockspeed' is the clock speed of the state machine in kHz. The first four optional arguments are variables holding initialising values of the state machine registers and the address of the first instruction to execute (defaults to zero). These decide how the PIO will operate. sideout, setout, and outout can be set to 0 (default) or 1 to specify if pins defined in pinctrl should be initialised as inputs (0) or outputs (1)

### PIO EXECUTE pio, state_machine, instruction%

Immediately executes the instruction on the pio and state machine specified.

### PIO WRITE pio, state_machine, count, data0 [,data1..]

Writes the data elements to the pio and state machine specified. The write is blocking so the state machine needs to be able to take the data supplied NB: this command will probably need additional capability in future releases

### PIO WRITEFIFO a,b,v,d

Writes to one of the 4 individual FIFO registers. ‘a’ is the pio (0 or 1), ‘b’ id the state machine (0...3), ‘c’ is the FIFO register *0…3), ‘d’ is the data% (32 bit integer value).

### PIO READ pio, state_machine, count, data%[()]

Reads the data elements from the pio and state machine specified. The read is non-blocking so the state machine needs to be able to supply the data requested. When count is one then an integer can be used to receive the data, otherwise and integer array should be specified. NB: this command will probably need additional capability in future releases.

### PIO START pio, statemachine

Start a given state machine on pio.

### PIO STOP pio, statemachine

Stop a given state machine on pio.

### PIO CLEAR pio

This stops the pio specified on all statemachines and clears the control registers for the statemachines PINCTRL, EXECTRL, and SHIFTCTRL to defaults.

### PIO PROGRAM pio,array%()

Programs the entire pio program memory with the data in array%(). See Appendix F.

### PIO PROGRAM LINE pio, line, instruction

Programs just the specified line in a PIO program.

### PIO SET BASE 0/16

PIO commands can only work with 32 GPIO ports. For the RP2350B this command tells the system to use GP0-GP31 (0) or GP16-GP47 (16)

### PIO CONFIGURE pio, sm, clock [,startaddress] [,sidesetbase] [,sidesetno] [,sidesetout] [,setbase] [,setno] [,setout] [,outbase] [,outno] [,outout] [,inbase] [,jmppin] [,wraptarget] [,wrap] [,sideenable] [,sidepindir] [,pushthreshold] [,pullthreshold] [,autopush] [,autopull] [,inshiftdir] [,outshiftdir] [,joinrxfifo] [,jointxfifo] [,joinrxfifoget] [,joinrxfifoput]

## PIO Assembler Instructions

PIO assembler instructions are used within PIO programs to control state machine operations. These instructions are specified using the `PIO ASSEMBLE` command.

### Data Transfer Instructions
- [IN](in.md): Shift bits from a source into the Input Shift Register (ISR)
- [OUT](out.md): Shift bits from the Output Shift Register (OSR) to a destination
- [PUSH](push.md): Push ISR contents into the RX FIFO
- [PULL](pull.md): Load data from TX FIFO into the OSR

### Program Control Instructions
- [JMP](jmp.md): Jump to an address if a condition is true
- [WAIT](wait.md): Stall operation until a condition is true

### Data Manipulation Instructions
- [MOV](mov.md): Copy data from a source to a destination
- [SET](set.md): Immediately write data to a destination

### Interrupt Instructions
- [IRQ](irq.md): Set, clear, or wait for interrupt flags

### Miscellaneous Instructions
- [NOP](nop.md): No operation (typically used for delays)

See [Appendix F - The PIO Programming Package](../../F_the_pio_programming_package.md) for detailed information about PIO programming.

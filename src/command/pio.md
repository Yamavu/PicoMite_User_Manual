.wip


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

The parameters in this command are essentially the same as you would use in the PIO INIT command plus the helper functions PINCTRL, SHIFTCTRL and EXECCTRL but combined into a single command. This is required because the Pico sdk does some very clever processing behind the scenes to handle the RP2350B ‘sidesetbase’, ‘sidebase outbase’, ‘inbase’ and ‘jmppin’ are pin definitions. You can specify these as either a GPno or a pin number (e.g. GP3 or 5). In all cases specify the actual pin. So if PIO SET BASE is set to 16 for that PIO then values GP16 to GP47 are valid. If PIO SET BASE is not set or is set to 0 then pins GP0 to GP31 are valid. They all default to the base set except ‘jmppin’ (defaults to -1) which needs to be explicitly set if you want to use a ‘jmppin’ as this triggers setting the required status bit ‘clock’ is the desired PIO clock speed in Hz ‘startaddress’ is the PIO statement that will start execution - defaults to 0 ‘sidesetno’, ‘setno’ and ‘outno’ specify the number of pins that can be used for those functions - default to 0 ‘sidesetout’, ‘setout’ and ‘outout’ specify if those pins should be configured as outputs (1=yes, 0=no) - default to 0 ‘wraptarget and ‘wrap’ are in the range 0-31 and default to 0 and 31 ‘inshiftdir’ and ‘outshiftdir’ default to 1 - shift out of output shift register to right and shift input shift register to right (data enters from left). All other parameters are booleans that can enable a specific function - 1 to enable 0 to disable - all default to 0. Simple example: 'PIO Configure pio, sm, clock, startaddress, 'sidesetbase, sidesetno, sidesetout, 'setbase, setno, setout, outbase, outno, outout, inbase, 'jmppin, wraptarget, wrap, sideenable, sidepindir, 'pushthreshold, pullthreshold, autopush, autopull, inshiftdir, outshiftdir, 'joinrxfifo, jointxfifo, joinrxfifoget, joinrxfifoput PIO assemble 1 .program test .line 0 .wrap target Set pins,1 Set pins,0 .wrap .end program SetPin gp45,pio1 PIO set base 1,16 PIO configure 1,0,1000000,,,,,gp45,1,1,,,,,,Pio(.wrap target),Pio(.wrap) PIO start 1,0 Do Loop Although the PIO CONFIGURE command has many parameters, it is very easy to use if you adopt this simple approach: Copy the comment lines in the example into your program. For each parameter substitute your required value or delete the parameter leaving the commas intact. Once all substitutions are done delete any trailing commas Then assuming the line will be too long for the editor delete the CRs one by one starting at the end of the second last line and moving upwards. In this way you will have a valid command that is easy to input and edit. NB: You can also use continuation lines to make the editing easier (see OPTION CONTINUATION LINES)
### IRQ SET params

Sets an interrupt flag in the PIO state machine. This is a PIO assembler instruction used within PIO programs to control interrupt signaling between state machines or to the main processor.

**Parameters:**
- `params`: Interrupt number and optional modifiers (0-7 for PIO interrupts)

**Context:** Used in PIO assembler programs to set interrupt flags. PIO interrupts can be used for synchronization between multiple state machines or to signal the main processor.

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for PIO programming details and [using_the_io_pins.md](using_the_io_pins.md) for general interrupt concepts.
### IRQ NOWAIT params

Clears the wait condition for an interrupt flag without blocking. This instruction allows the state machine to continue execution regardless of interrupt state.

**Parameters:**
- `params`: Interrupt number (0-7 for PIO interrupts)

**Context:** Used in PIO assembler programs to override interrupt wait conditions. Unlike IRQ WAIT, this instruction doesn't stall the state machine.

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for PIO programming details and [using_the_io_pins.md](using_the_io_pins.md) for general interrupt concepts.
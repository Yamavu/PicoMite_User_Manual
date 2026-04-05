### IRQ WAIT params

Waits for an interrupt flag to be set in the PIO state machine. This instruction stalls the state machine until the specified interrupt condition is met.

**Parameters:**
- `params`: Interrupt number to wait for (0-7 for PIO interrupts)

**Context:** Used in PIO assembler programs to synchronize state machine execution with interrupt events. The state machine will pause until the specified interrupt flag is set.

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for PIO programming details and [using_the_io_pins.md](using_the_io_pins.md) for general interrupt concepts.
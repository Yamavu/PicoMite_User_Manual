### IRQ CLEAR params

Clears (resets) an interrupt flag in the PIO state machine. This instruction resets the specified interrupt flag to its inactive state.

**Parameters:**
- `params`: Interrupt number to clear (0-7 for PIO interrupts)

**Context:** Used in PIO assembler programs to reset interrupt flags after they have been processed. This prevents the interrupt from remaining active indefinitely.

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for PIO programming details and [using_the_io_pins.md](using_the_io_pins.md) for general interrupt concepts.
### IRQ

IRQ (Interrupt Request) commands for PIO state machines. These are PIO assembler instructions used to control interrupt flags for synchronization between state machines or signaling the main processor.

#### IRQ Control Instructions
{{#include irq_set.md}}
{{#include irq_wait.md}}
{{#include irq_clear.md}}
{{#include irq_nowait.md}}

### IRQ params

General IRQ instruction for PIO state machines. This is a versatile instruction that can set, clear, or wait for interrupts depending on the parameters used.

**Parameters:**
- `params`: Interrupt operation and number (0-7 for PIO interrupts)

**Context:** Used in PIO assembler programs for interrupt control. The exact behavior depends on the specific parameters, but generally controls interrupt flags for synchronization between PIO state machines.

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for PIO programming details, [using_the_io_pins.md](using_the_io_pins.md) for general interrupt concepts, [interrupt.md](interrupt.md) and [interruptsub.md](interruptsub.md) for software interrupt commands.


### IN params

Shifts a number of bits from a source into the Input Shift Register (ISR) in a PIO state machine. This is a PIO assembler instruction used to read data from GPIO pins or other sources into the state machine.

**Parameters:**
- `params`: Number of bits to shift and source specification (0-31 bits)

**Function:**
The IN instruction shifts data from a source (typically GPIO pins) into the ISR (Input Shift Register). The data is shifted according to the configured shift direction (LSB or MSB first). When the ISR reaches its configured threshold, it can automatically push the data into the RX FIFO where it can be read by the main program.

**Common Usage:**
- Reading serial data from GPIO pins
- Capturing data from external devices
- Building up data for transfer to the main processor via the RX FIFO

**Related Instructions:**
- OUT: Shifts bits from the OSR to a destination
- PUSH: Pushes ISR contents into RX FIFO
- PULL: Loads data from TX FIFO into OSR

**Cross-reference:** See [F_the_pio_programming_package.md](F_the_pio_programming_package.md) for comprehensive PIO programming details including shift control configuration and FIFO operations.


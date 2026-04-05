

## SPI/SPI2 Commands

The SPI (Serial Peripheral Interface) commands provide access to the PicoMite's SPI hardware for communication with external devices. The PicoMite supports two SPI channels (SPI and SPI2) with identical functionality.

### SPI Commands

{{#include spi_open.md}}
{{#include spi_read.md}}
{{#include spi_write_data.md}}
{{#include spi_write_string.md}}
{{#include spi_write_array.md}}
{{#include spi_close.md}}

### SPI2 Commands

SPI2 commands work identically to SPI commands but operate on the second SPI channel. Simply replace "SPI" with "SPI2" in any command (e.g., `SPI2 OPEN` instead of `SPI OPEN`).
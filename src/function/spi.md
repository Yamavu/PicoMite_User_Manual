### SPI ( data ) or SPI2 ( data )

Send and receive data using an SPI channel.

A single SPI transaction will send data while simultaneously receiving data
from the slave. `data` is the data to send and the function will return the data
received during the transaction. `data` can be an integer or a floating point
variable or a constant.

See [SPI Communications](../D_spi_communications.md)

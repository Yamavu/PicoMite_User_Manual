

### SPI OPEN speed, mode, bits

Communications via an SPI channel. See [Appendix D](../D_spi_communications.md) for the details. 

`nbr` is the number of data items to send or receive

### SPI READ nbr, array()

`array` must be a single dimension float or integer array and `nbr` elements will be received.


### SPI WRITE nbr, data1, data2, data3, … etc

`data1`, `data2`, ... can be float or integer and in the case of WRITE can be a constant or expression.


### SPI WRITE nbr, string$

If `string$` is used `nbr` characters will be sent.


### SPI WRITE nbr, array()

`array` must be a single dimension float or integer array and `nbr` elements will be sent.


### SPI CLOSE

Close SPI connection

### SPI2 ...

The same set of commands as for SPI (above) but applying to the second SPI channel.
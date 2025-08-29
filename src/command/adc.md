

## ADC

 The ADC commands provide an alternate method of recording analog inputs and are intended for high speed recording of many readings into an array.


### ADC OPEN freq, n_channels [,interrupt]

 This allocates up to 4 ADC channels for use and sets them to be converted at the specified frequency. 
 
 The range of pins are GP26, GP27, GP28, and GP29 for the RP2940 and RP2350A. Additionally GP40, GP41, GP42, GP43 on the RP2350B.
 
 If the number of channels is one then it will always be GP26 used, if two then GP26 and GP27 are used, etc. Sampling of multiple channels is sequential (there is only one ADC). The pins are locked to the function when ADC OPEN is active.
 
 The maximum total frequency is CPUspeed/96 (eg, 520KHz if all four channels are to be sampled with the CPU set at 200MHz). 
 
 Note that a aggregate sampling frequency over 500Khz is overclocking the ADC. 
 
 The optional `interrupt` parameter specifies an interrupt to call when the conversion completes. If not specified then conversion will be blocking


### ADC FREQUENCY freq

 This changes the sampling frequency of the ADC conversion without having to close and re-open


### ADC CLOSE

 Releases the pins to normal usage

### ADC START array1!() [,array2!()] [,array3!()] [,array4!()] [,C1min] [,C1max] [,C2min] [,C2max] [,C3min] [,C3max] [,C4min] [,C4max]

 This starts conversion into the specified arrays.
 
 The arrays must be floating point and the same size. The size of the arrays defines the number of conversions. Start can be called repeatedly once the ADC is OPEN
 
 `Cxmin` and `Cxmax` will scale the readings. For example, C1min=`200` and C1max=`100` will create values ranging from 200 to 100 for equivalent voltages of 0 - 3.3.

 If the scaling is not used the results are returned as a voltage between 0 and OPTION VCC (defaults to 3.3V).


### ADC RUN array1%(),array2%)

 Runs the ADC continuously in double buffered mode. 
 
 The ADC first fills `array1%` and then `array2%` and then back to array1% etc. If more than one ADC channel is specified in the `ADC OPEN` command the data are interleaved. 
 
 The data is returned as packed 8-bit values (Use `MEMORY UNPACK` to convert to a normal array). `MM.INFO(ADC)` will return the number of the buffer currently available for reading (`1` or `2`).
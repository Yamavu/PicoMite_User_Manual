## INTERRUPT [myint]

This command triggers a software interrupt. The interrupt is set up usingINTERRUPT ‘myint’ where ‘myint’ is the name of a subroutine that will beexecuted when the interrupt is triggered.Use INTERRUPT 0 to disable the interruptUse INTERRUPT without parameters to trigger the interrupt.Note: the interrupt can also be triggered from within a CSUB
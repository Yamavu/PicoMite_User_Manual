## END cmd$

the program ends with the break character (ie, Ctrl-C).The optional parameter ‘noend’ can be used to block execution of theMM.END subroutine eg, “END noend”if 'cmd$' is specified then it will be executed as though at the command promptafter the program finishes. Note: if "END cmd$" is used but a subroutineMM.END exists it will be executed and cmd$ ignored.
## POKE DISPLAY command [,data1] [,data2] [,datan]

This command sends commands and associated data to the display controllerfor a connected display. This allows the programmer to change parameters ofhow the display is configured. eg, POKE DISPLAY &H28 will turn off anSSD1963 display and POKE DISPLAY &H29 will turn it back on again.Works for all displays except the ST7790.
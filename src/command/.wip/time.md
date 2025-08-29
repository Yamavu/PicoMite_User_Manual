

### TIME$ = "HH:MM:SS" or

 Sets the time of the internal clock. MM and SS are optional and will default to zero if not specified. For example TIME$ = "14:30" will set the clock to 14:30 with zero seconds.

### TIME$ = "HH:MM" or

 With OPTION RTC AUTO ENABLE the PicoMite firmware starts with the TIME$ programmed in RTC. Without OPTION RTC AUTO ENABLE the

### TIME$ = "HH"

 firmware starts with TIME$="00:00:00"
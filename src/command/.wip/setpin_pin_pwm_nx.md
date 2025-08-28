## SETPIN pin, PWM[nx]

Allocate pin to PWMnx'n' is the PWM number (0 to 7) and 'x' and is the channel (A or B). n and x areoptional.The setpin can be changed until the PWM command is issued. At that point thepin becomes locked to PWM until PWMn,OFF is issued.
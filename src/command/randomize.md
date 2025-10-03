.wip


### RANDOMIZE nbr

Seed the random number generator with ‘nbr’. On the RP2040 the random number generator is seeded with zero at power up and will generate the same sequence of random numbers each time. To generate a different random sequence each time you must use a different value for ‘nbr’ (the TIMER function is handy for that). This command does nothing on the RP2350 which has a hardware random generator that does not require seeding.
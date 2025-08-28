## PIO READ pio, state_machine, count, data%[()]

Reads the data elements from the pio and state machine specified. The read isnon-blocking so the state machine needs to be able to supply the datarequested. When count is one then an integer can be used to receive the data,otherwise and integer array should be specified.NB: this command will probably need additional capability in future releases.
.wip


### PLAY

This command will generate a variety of audio outputs. See the OPTION AUDIO command for setting the I/O pins to be used for the output. The audio is a pulse width modulated signal (PWM) so a low pass filter is required to remove the carrier frequency.

### PLAY TONE left, right [,dur] [,interrupt]

Generates two separate frequencies on the sound output left and right channels. 'left' and 'right' are the frequencies in Hz to use for the left and right channels. The tone plays in the background (the program will continue running after this command) and 'dur' specifies the number of milliseconds that the tone will sound for. If the duration is not specified the tone will continue until explicitly stopped or the program terminates. 'interrupt' is an optional subroutine which will be called when the play terminates. The frequency can be from 1Hz to 20KHz and is very accurate (it is based on a crystal oscillator). The frequency can be changed at any time by issuing a new PLAY TONE command.

### PLAY FLAC file$ [, interrupt]

Will play a FLAC file on the sound output. 'file$' is the FLAC file to play (the extension of .flac will be appended if missing). The sample rate can be up to 48kHz in stereo (96kHz if the Pico is overclocked) The FLAC file is played in the background. 'interrupt' is optional and is the name of a subroutine which will be called when the file has finished playing. If file$ is a directory on the B: drive the Pico will play all of the files in that directory in turn.

### PLAY WAV file$ [, interrupt]

Will play a WAV file on the sound output. 'file$' is the WAV file to play (the extension of .wav will be appended if missing). The WAV file must be PCM encoded in mono or stereo with 8 or 16-bit sampling. The sample rate can be up to 48kHz in stereo (96kHz if the Pico is overclocked). The WAV file is played in the background. 'interrupt' is optional and is the name of a subroutine which will be called when the file has finished playing.

### PLAY MP3 file$ [, interrupt]

Will play a MP3 file on the sound output (RP2350 ONLY). 'file$' is the MP3file to play (the extension of .mp3 will be appended if missing). The sample rate can be up to 48kHz. The MP3 file is played in the background. 'interrupt' is optional and is the name of a subroutine which will be called when the file has finished playing. If file$ is a directory on the B: drive the Pico will play all of the files in that directory in turn.

### PLAY MODFILE file$ [,interrupt]

Will play a MOD file on the sound output. 'file$' is the MOD file to play (the extension of .mod will be appended if missing). The MOD file is played in the background and will play continuously in a loop. If the optional 'interrupt' is specified This will be called when the file has played once through the sequence and playback will then be terminated. This command will preferentially use space in PSRAM if enabled for the file buffer (RP2350 only). In this case a modbuffer does not need to be enabled with the OPTION command Plays a specific sample in the mod file on the channel specified. The volume is

### PLAY MODSAMPLE

optional and can be between 0 and 64. This command can only be used when

### PLAY LOAD SOUND array%()

4095. This provides the data for any arbitrary waveform that can be played by the PLAY SOUND command. You can use the MEMORY PACK command to create the arrays from a normal 4096 element integer array. Play a series of sounds simultaneously on the audio output.

### PLAY SOUND soundno, channelno, type [,frequency] [,volume]

'soundno' is the sound number and can be from 1 to 4 allowing for four simultaneous sounds on each channel. 'channelno' specifies the output channel. It can be L (left speaker), R (right speaker), B (both speakers). type' specifies the wave form to be used. It can be S (Sine wave), Q (square wave) , T (triangular wave) , W (saw tooth) , O (Null output), P (periodic noise), N (random noise) or U (user defined using PLAY LOAD SOUND). 'frequency' is the frequency from 1 to 20000 (Hz) and it must be specified except when type is O. In Type U mode, this parameter can also accept decimal values. For example, all of the following will play back the waveform at its original pitch: Sample rate of 4000, frequency = 1 Sample rate of 8000, frequency = 2 Sample rate of 16000, frequency = 4 'volume' is optional and must be between 1 and 25. It defaults to 25 When PLAY SOUND is called all other audio usage will be blocked and will remain blocked until PLAY STOP is called. Output can be stopped temporarily using PLAY PAUSE and PLAY RESUME. Calling SOUND on an already running 'soundno' will immediately replace the previous output. Individual sounds are turned off using type “O” Running 4 sounds simultaneously on both channels of the audio output consumes about 23% of the CPU.

### PLAY PAUSE

PLAY PAUSE will temporarily halt the currently playing file or tone.

### PLAY RESUME

PLAY RESUME will resume playing a sound that was paused.

### PLAY STOP

PLAY STOP will terminate the playing of the file or tone. When the program terminates for whatever reason the sound output will also be automatically stopped.

### PLAY VOLUME left, right

Will adjust the volume of the audio output. 'left' and 'right' are the levels to use for the left and right channels and can be between 0 and 100 with 100 being the maximum volume. There is a linear relationship between the specified level and the output. The volume defaults to maximum when a program is run.

### PLAY NEXT

Stops playback of the current audio file and starts the next one in the directory

### PLAY PREVIOUS

Stops playback of the current audio file and starts the previous one in the directory VS1053 specific PLAY commands

### PLAY MP3 file$ [, interrupt]

Will play a MP3 file on the sound output.

### PLAY HALT

This command works when a MP3 file is playing. It stops playback and records the current file position to allow playback to be resumed from the same point. This command is specifically designed to support for mp3 audio books

### PLAY CONTINUE track$

Resumes playback of the MP3 track specified. "track$" will be the name of the file that was playing when halted with all file attributes removed eg, PLAY MP3 "B:/mp3/mymp3.mp3" sometime later PLAY HALT later again PLAY CONTINUE "mymp3"

### PLAY MIDIFILE file$ [, interrupt]

Will play a MIDI file on the sound output. 'file$' is the MIDI file to play (the extension of .mid will be appended if missing). The MIDI file is played in the background. 'interrupt' is optional and is the name of a subroutine which will be called when the file has finished playing. If file$ is a directory on the B: drive the Pico will play all of the files in that directory in turn.

### PLAY MIDI

Initiates the real-time midi mode. In this mode midi instructions can be sent to the VS1053 to select which instruments to play on which channels, turn notes on, and turn them off in real timer

### PLAY MIDI CMD cmd%, data1%, data2%

Sends a midi command when in real time midi mode. An example would be to allocate an instrument to a channel. Eg, PLAY MIDI CMD &B11000001,4 ‘set channel 1 to instrument 4

### PLAY MIDI TEST n

Plays a MIDI test sequence, n=0 to 3, 0 = normal realtime, the others play note and instrument samples

### PLAY NOTE ON channel%, note%, velocity%

Turns on the note on the channel specified when in real time MIDI mode

### PLAY NOTE OFF channel%, note% [,velocity%]

Turns off the note on the channel specified when in real time MIDI mode

### PLAY STREAM buffer%(), readpointer%, writepointer%

Sends data to the VS1053 CODEC from the circular buffer “buffer%”. This command initiates a background output stream where the VS1053 is sent anything in the buffer between the readpointer and the write pointer, updating the readpointer as it goes. Can be used for arbitrary waveform output. Will set a byte or a word within the virtual memory space. Where more than one byte is written the address must be exactly divisible by the number of bytes: 2, 4, or 8 otherwise an error will be reported.
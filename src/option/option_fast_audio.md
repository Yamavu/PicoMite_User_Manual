# OPTION FAST AUDIO ON|OFF

When using the `PLAY SOUND` command, changes to sounds, volumes, or frequencies can cause audible clicks in the output. The firmware attempts to mitigate this by ramping the volume down on the channel’s previous output before changing the output and ramping it back up again. This significantly improves the audio output but at the expense of a short delay in the `PLAY SOUND` command (worst case 3mSec). This delay can be avoided using OPTION FAST AUDIO ON in a program.

The audible clicks may then re-appear but this is at the programmer’s discretion.

This is a temporary option that is reset to `OFF` whenever a program is run.



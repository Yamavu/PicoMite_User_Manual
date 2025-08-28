# OPTION BREAK nn

Set the value of the break key to the ASCII value `nn`. This key is used to
interrupt a running program.

The value of the break key is set to **CTRL-C** key at power upand when a
program is run but it can be changed to any keyboard key using this
command in a program (for example, `OPTION BREAK 4` will set the break
key to the **CTRL-D** key). Setting this option to zero `0` will disable the break
function entirely.


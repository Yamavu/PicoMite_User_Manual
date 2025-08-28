# Options

- [Audio](options_audio.md)
- [Behavior](options_behavior.md)
- [Command Prompt](options_command_prompt.md)
- [Display](options_display.md)
- [Hardware](options_hardware.md)
- [Keyboard](options_keyboard.md)
- [Mouse](options_mouse.md)
- [Network](options_network.md)
- [Storage](options_storage.md)

This table lists the various option commands which can be used to configure MMBasic and change the way it operates. Options that are marked as permanent will be saved in non-volatile memory and automatically restored when the PicoMite firmware is restarted. Options that are not permanent will be reset on start-up, reset and in many cases when a program is run and/or exited.

Many `OPTION` commands will force a restart of the PicoMite firmware and that will cause the USB console interface to be reset. The program in memory will not be lost as it is held in non-volatile flash memory.


{{#include option/list.md}}

{{#include option/pin_nbr.md}}

{{#include option/disk_save_fname_br_option_disk_load_fname.md}}

{{#include option/reset.md}}

{{#include option/reset_cfg_br_option_reset_list.md}}


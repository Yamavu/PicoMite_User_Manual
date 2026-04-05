
## SPRITE

*VGA AND HDMI VERSIONS ONLY*

The SPRITE commands are used to manipulate small graphic images on the VGA or HDMI screen and are useful when writing games. 

Sprites operate in framebuffers in MODEs 2 and 3 only.

Sprites are always stored as RGB121 `nibbles` for efficiency The maximum size of a sprite is MM.HRES-1 and MM.VRES-1.

See also the [BLIT command](./blit.md) and [SPRITE() functions](../function/sprite.md).

{{#include sprite_close.md}}

{{#include sprite_copy.md}}

{{#include sprite_hide.md}}

{{#include sprite_restore.md}}

{{#include sprite_interrupt.md}}

{{#include sprite_read.md}}

{{#include sprite_write.md}}

{{#include sprite_load.md}}

{{#include sprite_loadarray.md}}

{{#include sprite_loadbmp.md}}

{{#include sprite_loadpng.md}}

{{#include sprite_move.md}}

{{#include sprite_next.md}}

{{#include sprite_scroll.md}}

{{#include sprite_set.md}}

{{#include sprite_show.md}}

{{#include sprite_swap.md}}
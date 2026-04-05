### SPRITE SHOW [#]n, x,y, layer [,options]

Displays sprite `n` on the screen with the top left at coordinates `x`, `y`. Sprites will only collide with other sprites on the same layer, layer zero, or with the screen edge. If a sprite is already displayed on the screen, then the SPRITE SHOW command acts to move the sprite to the new location. The display background is stored as part of the command and will be replaced when the sprite is hidden or moved further. The parameter `options` is optional and can be set as follows: bit 0 set - mirrored left to right bit 1 set - mirrored top to bottom bit 2 set - black pixels not treated as transparent default is 0

### SPRITE SHOW SAFE [#]n, x,y, layer [,orientation] [,ontop]

Shows a sprite and automatically compensates for any other sprites that overlap it. If the sprite is not already being displayed the command acts exactly the same as SPRITE SHOW. If the sprite is already shown it is moved and remains in its position relative to other sprites based on the original order of writing. i.e. if sprite 1 was written before sprite 2 and it is moved to overlap sprite 2 it will display under sprite 2. If the optional "ontop" parameter is set to 1 then the sprite moved will become the newest sprite and will sit on top of any other sprite it overlaps. Refer to SPRITE SHOW for details of the orientation parameter.

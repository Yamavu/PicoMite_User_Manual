### SPRITE(V,[#]s1, [#]s2)

Returns the vector from sprite `s1` to `s2` in radians.

The angle is based on the clock so if `s2` is above `s1` on the screen then the
answer will be zero. This can be used on any pair of sprites that are visible. If
either sprite is not visible the function will return -1.

This is particularly useful after a collision if the programmer wants to make
some differential decision based on where the collision occurred. The angle is
calculated between the centre of each of the sprites which may of course be
different sizes.
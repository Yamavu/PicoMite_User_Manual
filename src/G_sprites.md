# Sprites

## VGA, HDMI and LCD FRAMEBUFFERS

You can create a sprite in various ways but essentially you are just storing an image in a buffer. The difference comes when you SHOW the sprite. In this case, first time in, the firmware stores the area of memory (or display real-estate) that will be replaced by the sprite and then draws the sprite in its place

Subsequent SHOW commands replace the sprite with the stored background, store the background for the new location and finally draw the sprite. In this way you can move the sprite over the background without any extra code

Collision detection then sits on top of this and looks for the rectangular boundaries of sprites touching to create an interrupt or a sprite touching the edge of the frame

Sprites are ordered so the drawing order is held in a lifo. suppose you have sprite 1 overlapped by sprite 2 and then by sprite 3. If you simply moved sprite 1 then its background would overwrite bits of 2 and 3 – not what we want. SPRITE SHOW SAFE unwinds the LIFO by removing each sprite in reverse order, moves sprite 1 and then restores first 2 and then 3 on top of it. Finally there is the concept of layers (this is the 4th parameter in SPRITE SHOW).
The concept of the sprite implementation is as follows:

Sprites are full colour and of any size. The collision boundary is the enclosing rectangle.







Sprites are loaded to a specific number (1 to 64).
Sprites are displayed using the SPRITE SHOW command

For each SHOW command the user must select a "layer". This can be between 0 and 10

Sprites collide with sprites on the same layer, layer 0, or the screen edge

Layer 0 is a special case and sprites on all other layers will collide with it

The SCROLL commands leave sprites on all layers except layer 0 unmoved.








Layer 0 sprites scroll with the background and this can cause collisions

There is no practical limit on the number of collisions caused by SHOW or SCROLL commands

The SPRITE() function allows the user to fully interrogate the details of a collision

A SHOW command will overwrite the details of any previous collisions for that sprite

A SCROLL command will overwrite details of previous collisions for ALL sprites

To restore a screen to a previous state sprites should be removed in the opposite order to which they were written (ie, last in first out).
Because moving a sprite or, particularly, scrolling the background can cause multiple sprite collisions it is important to understand how they can be interrogated

The best way to deal with a sprite collision is using the interrupt facility. A collision interrupt routine is set up using the SPRITE INTERRUPT command. Eg:
SPRITE INTERRUPT collision The following is an example program for identifying all collisions that have resulted from either a SPRITE SHOW command or a SCROLL command
'
' This routine demonstrates a complete interrogation of collisions
'
SUB collision LOCAL INTEGER i
' First use the SPRITE(S) function to see what caused the interrupt IF SPRITE(S) <> 0 THEN 'collision of specific individual sprite
'SPRITE(S) returns the sprite that moved to cause the collision PRINT "Collision on sprite ", SPRITE(S)
process_collision(SPRITE(S))
PicoMite User Manual

Page 205

PRINT ELSE

'0 means collision of one or more sprites caused by background move
' SPRITE(C, 0) will tell us how many sprites had a collision PRINT "Scroll caused a total of ", SPRITE(C,0)," sprites to have collisions"
FOR I = 1 TO SPRITE(C, 0)
' SPRITE(C, 0, i) will tell us the sprite number of the “I”th sprite PRINT "Sprite ", SPRITE(C, 0, i)
process_collision(SPRITE(C, 0, i))
NEXT i PRINT ENDIF END SUB
' get details of the specific collisions for a given sprite SUB process_collision(S AS INTEGER)
LOCAL INTEGER i, j
' SPRITE(C, #n) returns the number of current collisions for sprite n PRINT "Total of " SPRITE(C, S) " collisions"
FOR I = 1 TO SPRITE(C, S)
' SPRITE(C, S, i) will tell us the sprite number of the “I”th sprite j = SPRITE(C, S, i)
IF j = &HF1 THEN PRINT "collision with left of screen"
ELSE IF j = &HF2 THEN PRINT "collision with top of screen"
ELSE IF j = &HF4 THEN PRINT "collision with right of screen"
ELSE IF j = &HF8 THEN PRINT "collision with bottom of screen"
ELSE
' SPRITE(C, #n, #m) returns details of the mth collision PRINT "Collision with sprite ", SPRITE(C, S, i)
ENDIF NEXT i END SUB


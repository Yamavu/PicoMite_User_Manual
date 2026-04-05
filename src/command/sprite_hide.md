### SPRITE HIDE [#]n

Removes sprite n from the display and replaces the stored background. To restore a screen to a previous state sprites should be hidden in the opposite order to which they were written "LIFO"

### SPRITE HIDE ALL

Hides all the sprites allowing the background to be manipulated. The following commands cannot be used when all sprites are hidden: 
- SPRITE SHOW (SAFE)
- SPRITE HIDE (SAFE, ALL) 
- SPRITE SWAP 
- SPRITE MOVE 
- SPRITE SCROLLR 
- SPRITE SCROLL

### SPRITE HIDE SAFE [#]n

Removes sprite n from the display and replaces the stored background. 

Automatically hides all more recent sprites as well as the requested one and then replaces them afterwards. This ensures that sprites that are covered by other sprites can be removed without the user tracking the write order. 

Of course this version is less performant than the simple version and should only be used it there is a risk of the sprite being partially covered.

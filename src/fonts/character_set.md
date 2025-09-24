

## Character Set

Picomite uses an ASCII compatible character encoding.


### Non-Printable ASCII characters (character code 0-31)

The first 32 characters in the ASCII-table are unprintable control codes and are used to control peripherals such as printers.



Int | HEX | Symbol | Unicode<br>Codepoint | Description
:-: | :-:  | :-:    | :-:                  | :-
00 | 00 | ␀  | U+00000 |  Null character
01 | 01	| ␁  | U+00001 |  Start of Heading
02 | 02	| ␂  | U+00002 |  Start of Text
03 | 03	| ␃  | U+00003 |  End of Text
04 | 04	| ␄  | U+00004 |  End of Transmission
05 | 05	| ␅  | U+00005 |  Enquiry
06 | 06	| ␆  | U+00006 |  Acknowledge
07 | 07	| ␇  | U+00007 |  Bell, Alert
08 | 08	| ␈  | U+00008 |  Backspace
09 | 09	| ␉  | U+00009 |  Horizontal Tab
10 | 0A	| ␊  | U+0000A |  Line Feed
11 | 0B	| ␋  | U+0000B |  Vertical Tabulation
12 | 0C	| ␌  | U+0000C |  Form Feed
13 | 0D	| ␍  | U+0000D |  Carriage Return
14 | 0E	| ␎  | U+0000E |  Shift Out
15 | 0F	| ␏  | U+0000F |  Shift In
16 | 10	| ␐  | U+00010 |  Data Link Escape
17 | 11	| ␑  | U+00011 |  Device Control One (XON)
18 | 12	| ␒  | U+00012 |  Device Control Two
19 | 13	| ␓  | U+00013 |  Device Control Three (XOFF)
20 | 14	| ␔  | U+00014 |  Device Control Four
21 | 15	| ␕  | U+00015 |  Negative Acknowledge
22 | 16	| ␖  | U+00016 |  Synchronous Idle
23 | 17	| ␗  | U+00017 |  End of Transmission Block
24 | 18	| ␘  | U+00018 |  Cancel
25 | 19	| ␙  | U+00019 |  End of medium
26 | 1A	| ␚  | U+0001A |  Substitute
27 | 1B	| ␛  | U+0001B |  Escape
28 | 1C	| ␜  | U+0001C |  File Separator
29 | 1D	| ␝  | U+0001D |  Group Separator
30 | 1E | ␞  | U+0001E |  Record Separator
31 | 1F	| ␟  | U+0001F |  Unit Separator



### Printable ASCII characters

Codes 32-127 are common for all the different variations of the ASCII table, they are called printable characters, represent letters, digits, punctuation marks, and a few miscellaneous symbols. You will find almost every character on your keyboard. 


Int | HEX | Symbol  | Unicode<br>Codepoint |  Description                    | Font1
:-: | :-: | :-: | :-| :-                                 | :-
32  | 20 | `SP` | U+00020   |  Space                                   |  ![ ](font1/20.png) 
33  | 21 |	!   | U+00021   |  Exclamation mark                        |  ![!](font1/21.png) 
34  | 22 |	"   | U+00022   |  Double quotes (or speech marks)         |  !["](font1/22.png) 
35  | 23 |	#   | U+00023   |  Number sign                             |  ![#](font1/23.png) 
36  | 24 |	$   | U+00024   |  Dollar                                  |  ![\$](font1/24.png) 
37  | 25 |	%   | U+00025   |  Per cent sign                           |  ![%](font1/25.png) 
38  | 26 |	&   | U+00026   |  Ampersand                               |  ![&](font1/26.png) 
39  | 27 |	'   | U+00027   |  Single quote                            |  !['](font1/27.png)
40  | 28 |	(   | U+00028   |  Open parenthesis (or open bracket)      |  ![(](font1/28.png) 
41  | 29 |	)   | U+00029   |  Close parenthesis (or close bracket)    |  ![)](font1/29.png) 
42  | 2A |	*   | U+0002A   |  Asterisk                                |  ![*](font1/2A.png) 
43  | 2B |	+   | U+0002B   |  Plus                                    |  ![+](font1/2B.png) 
44  | 2C |	,   | U+0002C   |  Comma                                   |  ![,](font1/2C.png) 
45  | 2D |	-   | U+0002D   |  Hyphen-minus                            |  ![-](font1/2D.png) 
46  | 2E |	.   | U+0002E   |  Period, dot or full stop                |  ![.](font1/2E.png) 
47  | 2F |	/   | U+0002F   |  Slash or divide                         |  ![/](font1/2F.png)
48  | 30 |	0   | U+00030   |  Zero                                    |  ![0](font1/30.png) 
49  | 31 |	1   | U+00031   |  One                                     |  ![1](font1/31.png) 
50  | 32 |	2   | U+00032   |  Two                                     |  ![2](font1/32.png) 
51  | 33 |	3   | U+00033   |  Three                                   |  ![3](font1/33.png) 
52  | 34 |	4   | U+00034   |  Four                                    |  ![4](font1/34.png) 
53  | 35 |	5   | U+00035   |  Five                                    |  ![5](font1/35.png) 
54  | 36 |	6   | U+00036   |  Six                                     |  ![6](font1/36.png) 
55  | 37 |	7   | U+00037   |  Seven                                   |  ![7](font1/37.png)
56  | 38 |	8   | U+00038   |  Eight                                   |  ![8](font1/38.png) 
57  | 39 |	9   | U+00039   |  Nine                                    |  ![9](font1/39.png) 
58  | 3A |	:   | U+0003A   |  Colon                                   |  ![:](font1/3A.png) 
59  | 3B |	;   | U+0003B   |  Semicolon                               |  ![;](font1/3B.png) 
60  | 3C |	<   | U+0003C   |  Less than (or open angled bracket)      |  ![<](font1/3C.png) 
61  | 3D |	=   | U+0003D   |  Equals                                  |  ![=](font1/3D.png) 
62  | 3E |	>   | U+0003E   |  Greater than (or close angled bracket)  |  ![>](font1/3E.png) 
63  | 3F |	?   | U+0003F   |  Question mark                           |  ![?](font1/3F.png)
64  | 40 |	@   | U+00040   |  At sign                                 |  ![@](font1/40.png) 
65  | 41 |	A   | U+00041   |  Uppercase A                             |  ![A](font1/41.png) 
66  | 42 |	B   | U+00042   |  Uppercase B                             |  ![B](font1/42.png) 
67  | 43 |	C   | U+00043   |  Uppercase C                             |  ![C](font1/43.png) 
68  | 44 |	D   | U+00044   |  Uppercase D                             |  ![D](font1/44.png) 
69  | 45 |	E   | U+00045   |  Uppercase E                             |  ![E](font1/45.png) 
70  | 46 |	F   | U+00046   |  Uppercase F                             |  ![F](font1/46.png) 
71  | 47 |	G   | U+00047   |  Uppercase G                             |  ![G](font1/47.png)
72  | 48 |	H   | U+00048   |  Uppercase H                             |  ![H](font1/48.png) 
73  | 49 |	I   | U+00049   |  Uppercase I                             |  ![I](font1/49.png) 
74  | 4A |	J   | U+0004A   |  Uppercase J                             |  ![J](font1/4A.png) 
75  | 4B |	K   | U+0004B   |  Uppercase K                             |  ![K](font1/4B.png) 
76  | 4C |	L   | U+0004C   |  Uppercase L                             |  ![L](font1/4C.png) 
77  | 4D |	M   | U+0004D   |  Uppercase M                             |  ![M](font1/4D.png) 
78  | 4E |	N   | U+0004E   |  Uppercase N                             |  ![N](font1/4E.png) 
79  | 4F |	O   | U+0004F   |  Uppercase O                             |  ![O](font1/4F.png)
80  | 50 |	P   | U+00050   |  Uppercase P                             |  ![P](font1/50.png) 
81  | 51 |	Q   | U+00051   |  Uppercase Q                             |  ![Q](font1/51.png) 
82  | 52 |	R   | U+00052   |  Uppercase R                             |  ![R](font1/52.png) 
83  | 53 |	S   | U+00053   |  Uppercase S                             |  ![S](font1/53.png) 
84  | 54 |	T   | U+00054   |  Uppercase T                             |  ![T](font1/54.png) 
85  | 55 |	U   | U+00055   |  Uppercase U                             |  ![U](font1/55.png) 
86  | 56 |	V   | U+00056   |  Uppercase V                             |  ![V](font1/56.png) 
87  | 57 |	W   | U+00057   |  Uppercase W                             |  ![W](font1/57.png)
88  | 58 |	X   | U+00058   |  Uppercase X                             |  ![X](font1/58.png) 
89  | 59 |	Y   | U+00059   |  Uppercase Y                             |  ![Y](font1/59.png) 
90  | 5A |	Z   | U+0005A   |  Uppercase Z                             |  ![Z](font1/5A.png) 
91  | 5B |	[   | U+0005B   |  Opening bracket                         |  ![\[](font1/5B.png) 
92  | 5C |	\   | U+0005C   |  Backslash                               |  ![\\](font1/5C.png) 
93  | 5D |	]   | U+0005D   |  Closing bracket                         |  ![\]](font1/5D.png) 
94  | 5E |	\^  | U+0005E   |  Caret - circumflex                      |  ![\^](font1/5E.png) 
95  | 5F |	_   | U+0005F   |  Underscore                              |  ![_](font1/5F.png)
96  | 60 |	`   | U+00060   |  Grave accent                            |  ![°](font1/60.png) 
97  | 61 |	a   | U+00061   |  Lowercase a                             |  ![a](font1/61.png) 
98  | 62 |	b   | U+00062   |  Lowercase b                             |  ![b](font1/62.png) 
99  | 63 |	c   | U+00063   |  Lowercase c                             |  ![c](font1/63.png) 
100  | 64 |	d   | U+00064   |  Lowercase d                             |  ![d](font1/64.png) 
101  | 65 |	e   | U+00065   |  Lowercase e                             |  ![e](font1/65.png) 
102  | 66 |	f   | U+00066   |  Lowercase f                             |  ![f](font1/66.png) 
103  | 67 |	g   | U+00067   |  Lowercase g                             |  ![g](font1/67.png)
104  | 68 |	h   | U+00068   |  Lowercase h                             |  ![h](font1/68.png) 
105  | 69 |	i   | U+00069   |  Lowercase i                             |  ![i](font1/69.png) 
106  | 6A |	j   | U+0006A   |  Lowercase j                             |  ![j](font1/6A.png) 
107  | 6B |	k   | U+0006B   |  Lowercase k                             |  ![k](font1/6B.png) 
108  | 6C |	l   | U+0006C   |  Lowercase l                             |  ![l](font1/6C.png) 
109  | 6D |	m   | U+0006D   |  Lowercase m                             |  ![m](font1/6D.png) 
110  | 6E |	n   | U+0006E   |  Lowercase n                             |  ![n](font1/6E.png) 
111  | 6F |	o   | U+0006F   |  Lowercase o                             |  ![o](font1/6F.png)
112  | 70 |	p   | U+00070   |  Lowercase p                             |  ![p](font1/70.png) 
113  | 71 |	q   | U+00071   |  Lowercase q                             |  ![q](font1/71.png) 
114  | 72 |	r   | U+00072   |  Lowercase r                             |  ![r](font1/72.png) 
115  | 73 |	s   | U+00073   |  Lowercase s                             |  ![s](font1/73.png) 
116  | 74 |	t   | U+00074   |  Lowercase t                             |  ![t](font1/74.png) 
117  | 75 |	u   | U+00075   |  Lowercase u                             |  ![u](font1/75.png) 
118  | 76 |	v   | U+00076   |  Lowercase v                             |  ![v](font1/76.png) 
119  | 77 |	w   | U+00077   |  Lowercase w                             |  ![w](font1/77.png)
120  | 78 |	x   | U+00078   |  Lowercase x                             |  ![x](font1/78.png) 
121  | 79 |	y   | U+00079   |  Lowercase y                             |  ![y](font1/79.png) 
122  | 7A |	z   | U+0007A   |  Lowercase z                             |  ![z](font1/7A.png) 
123  | 7B |	{   | U+0007B   |  Opening brace                           |  ![{](font1/7B.png) 
124  | 7C |	\|  | U+0007C   |  Vertical bar                            |  ![ \| ](font1/7C.png) 
125  | 7D |	}   | U+0007D   |  Closing brace                           |  ![}](font1/7D.png) 
126  | 7E |	~   | U+0007E   |  Equivalency sign - tilde                |  ![~](font1/7E.png) 
127  | 7F |	⌂   | U+2302    |  HOUSE [^127] [^approx]                  |  ![⌂](font1/7F.png)

[^127]Character 127 should represent the command `DEL`, but is replaced for all fonts on PicoMite.


### Symbols

Fonts 1 and 4 have an extended character set. The symbols are not from the ASCII standard, some are not even in Unicode (as of 2025)

Int | Char | Font 1 | Unicode<br>Codepoint | Description
:-: | :-:  | :-     | :-:                  | :-
128 | ☐ | ![☐](font1/80.png) | U+2610 | BALLOT BOX 
129 | ☑ | ![☑](font1/81.png) | U+2611 | BALLOT BOX WITH CHECK
130 | ☒ | ![☒](font1/82.png) | U+2612 | BALLOT BOX WITH X
131 | ⊡ | ![⊡](font1/83.png) | U+22A1 | SQUARED DOT OPERATOR
132 | ⊟ | ![⊟](font1/84.png) | U+229F | SQUARED MINUS[^approx]
133 | & | ![&nbsp;](font1/85.png) |  | BALLOT BOX WITH EXCLAMATION MARK [^no]
134 | & | ![&nbsp;](font1/86.png) |  | BALLOT BOX WITH QUESTION MARK [^no]
135 | ☻ | ![☻](font1/87.png) | U+263B | BLACK SMILING FACE
136 | ☺ | ![☺](font1/88.png) | U+263A | WHITE SMILING FACE
137 | ♦ | ![♦](font1/89.png) | U+2666 | BLACK DIAMOND SUIT
138 | ♣ | ![♣](font1/8A.png) | U+2663 | BLACK CLUB SUIT
139 | ♠ | ![♠](font1/8B.png) | U+2660 | BLACK SPADE SUIT
140 | ♥ | ![♥](font1/8C.png) | U+2665 | BLACK HEART SUIT
141 | ◙ | ![◙](font1/8D.png) | U+25D9 | INVERSE WHITE CIRCLE
142 | ● | ![●](font1/8E.png) | U+25CF | BLACK CIRCLE
143 | ♪ | ![♪](font1/8F.png) | U+266A | EIGHTH NOTE
144 | ↕ | ![↕](font1/90.png) | U+2195 | UP DOWN ARROW
145 | ↔ | ![↔](font1/91.png) | U+2194 | LEFT RIGHT ARROW
146 | ↑ | ![↑](font1/92.png) | U+2191 | UPWARDS ARROW
147 | ↓ | ![↓](font1/93.png) | U+2193 | DOWNWARDS ARROW
148 | → | ![→](font1/94.png) | U+2192 | RIGHTWARDS ARROW
149 | ← | ![←](font1/95.png) | U+2190 | LEFTWARDS ARROW
150 | ⏻ | ![⏻](font1/96.png) | U+23FB | POWER SYMBOL
151 | 💡 | ![💡](font1/97.png) | U+1F4A1 | ELECTRIC LIGHT BULB
152 | 🧍 | ![🧍](font1/98.png) | U+1F9CD | STANDING PERSON
153 |   | ![](font1/99.png) |  | SECURE DIGITAL STORAGE CARD [^no]
154 |   | ![](font1/9A.png) |  | LIGHT-EMITTING DIODE WHITE [^no]
155 |   | ![](font1/9B.png) |  | LIGHT-EMITTING DIODE BLACK [^no]
156 | 🔊 | ![🔊](font1/9C.png) | U+1F50A | SPEAKER WITH THREE SOUND WAVES[^approx]
157 | ¶ | ![¶](font1/9D.png) | U+00B6 | PILCROW SIGN
158 | 🗲 | ![🗲](font1/9E.png) | U+1F5F2 | LIGHTNING MOOD[^approx]
159 | ★ | ![★](font1/9F.png) | U+2605 | BLACK STAR
160 | ⏸ | ![⏸](font1/A0.png) | U+23F8 | DOUBLE VERTICAL BAR
161 | ⏵ | ![⏵](font1/A1.png) | U+23F5 | BLACK MEDIUM RIGHT-POINTING TRIANGLE
162 | ⏹ | ![⏹](font1/A2.png) | U+23F9 | BLACK SQUARE FOR STOP
163 | 🔍 | ![🔍](font1/A3.png) | U+1F50D | LEFT-POINTING MAGNIFYING GLASS
164 | € | ![€](font1/A4.png) | U+20AC | EURO SIGN
165 | 🏠 | ![🏠](font1/A5.png) | U+1F3E0 | HOUSE BUILDING
166 | 🗑 | ![🗑](font1/A6.png) | U+1F5D1 | WASTEBASKET
167 |    | ![](font1/A7.png) |  | CIRCLED HEAVY WHITE UPWARDS ARROW [^no]
168 | 🖵 | ![🖵](font1/A8.png) | U+1F5B5 | SCREEN
169 | ❗ | ![❗](font1/A9.png) | U+2757 | HEAVY EXCLAMATION MARK SYMBOL
170 | 🌩 | ![🌩](font1/AA.png) | U+1F329 | CLOUD WITH LIGHTNING
171 | ᴼᵢ  | ![ᴼᵢ](font1/AB.png) | U+1D3C<br>U+1D62 | MODIFIER LETTER CAPITAL O<br>LATIN SUBSCRIPT SMALL LETTER I[^approx]
172 | 🔑 | ![🔑](font1/AC.png) | U+1F511 | KEY

#### Borders and UI Elements
Int | Char | Font 1 | Unicode<br>Codepoint | Description
:-: | :-:  | :-     | :-:                  | :-
173 | 𜱅 | ![𜱅](font1/AD.png) | U+1CC45 | DENSE HORIZONTAL FILL
174 | 𜱄 | ![𜱄](font1/AE.png) | U+1CC44 | DENSE VERTICAL FILL
175 | 🮕 | ![🮕](font1/AF.png) | U+1FB95 | CHECKER BOARD FILL
176 | 🮘 | ![🮘](font1/B0.png) | U+1FB98 | UPPER LEFT TO LOWER RIGHT FILL
177 | ▒ | ![▒](font1/B1.png) | U+2592  | MEDIUM SHADE
178 | 🮙 | ![🮙](font1/B2.png) | U+1FB99 | UPPER RIGHT TO LOWER LEFT FILL
179 | │ | ![│](font1/B3.png) | U+2502 | BOX DRAWINGS LIGHT VERTICAL
180 | ┤ | ![┤](font1/B4.png) | U+2524 | BOX DRAWINGS LIGHT VERTICAL AND LEFT
181 | ╡ | ![╡](font1/B5.png) | U+2561 | BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
182 | ╢ | ![╢](font1/B6.png) | U+2562 | BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
183 | ╖ | ![╖](font1/B7.png) | U+2556 | BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
184 | ╕ | ![╕](font1/B8.png) | U+2555 | BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
185 | ╣ | ![╣](font1/B9.png) | U+2563 | BOX DRAWINGS DOUBLE VERTICAL AND LEFT
186 | ║ | ![║](font1/BA.png) | U+2551 | BOX DRAWINGS DOUBLE VERTICAL
187 | ╗ | ![╗](font1/BB.png) | U+2557 | BOX DRAWINGS DOUBLE DOWN AND LEFT
188 | ╝ | ![╝](font1/BC.png) | U+255D | BOX DRAWINGS DOUBLE UP AND LEFT
189 | ╜ | ![╜](font1/BD.png) | U+255C | BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
190 | ╛ | ![╛](font1/BE.png) | U+255B | BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
191 | ┐ | ![┐](font1/BF.png) | U+2510 | BOX DRAWINGS LIGHT DOWN AND LEFT
192 | └ | ![└](font1/C0.png) | U+2514 | BOX DRAWINGS LIGHT UP AND RIGHT
193 | ┴ | ![┴](font1/C1.png) | U+2534 | BOX DRAWINGS LIGHT UP AND HORIZONTAL
194 | ┬ | ![┬](font1/C2.png) | U+252C | BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
195 | ├ | ![├](font1/C3.png) | U+251C | BOX DRAWINGS LIGHT VERTICAL AND RIGHT
196 | ─ | ![─](font1/C4.png) | U+2500 | BOX DRAWINGS LIGHT HORIZONTAL
197 | ┼ | ![┼](font1/C5.png) | U+253C | BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
198 | ╞ | ![╞](font1/C6.png) | U+255E | BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
199 | ╟ | ![╟](font1/C7.png) | U+255F | BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
200 | ╚ | ![╚](font1/C8.png) | U+255A | BOX DRAWINGS DOUBLE UP AND RIGHT
201 | ╔ | ![╔](font1/C9.png) | U+2554 | BOX DRAWINGS DOUBLE DOWN AND RIGHT
202 | ╩ | ![╩](font1/CA.png) | U+2569 | BOX DRAWINGS DOUBLE UP AND HORIZONTAL
203 | ╦ | ![╦](font1/CB.png) | U+2566 | BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
204 | ╠ | ![╠](font1/CC.png) | U+2560 | BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
205 | ═ | ![═](font1/CD.png) | U+2550 | BOX DRAWINGS DOUBLE HORIZONTAL
206 | ╬ | ![╬](font1/CE.png) | U+256C | BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
207 | ╧ | ![╧](font1/CF.png) | U+2567 | BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
208 | ╨ | ![╨](font1/D0.png) | U+2568 | BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
209 | ╤ | ![╤](font1/D1.png) | U+2564 | BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
210 | ╥ | ![╥](font1/D2.png) | U+2565 | BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
211 | ╙ | ![╙](font1/D3.png) | U+2559 | BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
212 | ╘ | ![╘](font1/D4.png) | U+2558 | BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
213 | ╒ | ![╒](font1/D5.png) | U+2552 | BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
214 | ╓ | ![╓](font1/D6.png) | U+2553 | BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
215 | ╫ | ![╫](font1/D7.png) | U+256B | BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
216 | ╪ | ![╪](font1/D8.png) | U+256A | BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
217 | ┘ | ![┘](font1/D9.png) | U+2518 | BOX DRAWINGS LIGHT UP AND LEFT
218 | ┌ | ![┌](font1/DA.png) | U+250C | BOX DRAWINGS LIGHT DOWN AND RIGHT
219 | █ | ![█](font1/DB.png) | U+2588 | FULL BLOCK
220 | ▄ | ![▄](font1/DC.png) | U+2584 | LOWER HALF BLOCK
221 | ▌ | ![▌](font1/DD.png) | U+258C | LEFT HALF BLOCK
222 | ▐ | ![▐](font1/DE.png) | U+2590 | RIGHT HALF BLOCK
223 | ▀ | ![▀](font1/DF.png) | U+2580 | UPPER HALF BLOCK


#### Math Symbols

Int | Char | Font 1 | Unicode<br>Codepoint | Description
:-: | :-:  | :-     | :-:                  | :-
224 | α | ![α](font1/E0.png)  | U+03B1 | GREEK SMALL LETTER ALPHA
225 | β | ![β](font1/E1.png)  | U+3B2 | GREEK SMALL LETTER BETA
226 | Γ | ![Γ](font1/E2.png)  | U+393 | GREEK CAPITAL LETTER GAMMA
227 | π | ![π](font1/E3.png)  | U+3C0 | GREEK SMALL LETTER PI
228 | Σ | ![Σ](font1/E4.png)  | U+3A3 | GREEK CAPITAL LETTER SIGMA
229 | σ | ![σ](font1/E5.png)  | U+3C3 | GREEK SMALL LETTER SIGMA
230 | μ | ![μ](font1/E6.png)  | U+3BC | GREEK SMALL LETTER MU
231 | γ | ![γ](font1/E7.png)  | U+3B3 | GREEK SMALL LETTER GAMMA
232 | Φ | ![Φ](font1/E8.png)  | U+3A6 | GREEK CAPITAL LETTER PHI
233 | Θ | ![Θ](font1/E9.png)  | U+398 | GREEK CAPITAL LETTER THETA
234 | Ω | ![Ω](font1/EA.png)  | U+3A9 | GREEK CAPITAL LETTER OMEGA
235 | δ | ![δ](font1/EB.png)  | U+3B4 | GREEK SMALL LETTER DELTA
236 | ∞ | ![∞](font1/EC.png)  | U+221E | INFINITY
237 | ∞̷ | ![∞̷](font1/ED.png) | U+221E<br>U+0337 | INFINITY<br> COMBINING SHORT SOLIDUS OVERLAY[^approx]
238 | ∈ | ![∈](font1/EE.png)  |  U+2208  | ELEMENT OF
239 | ∩ | ![∩](font1/EF.png)  |   U+2229 | INTERSECTION
240 | ≡ | ![≡](font1/F0.png)  | U+2261 | IDENTICAL TO
241 | ± | ![±](font1/F1.png)  |  U+B1   | PLUS-MINUS SIGN
242 | ≥ | ![≥](font1/F2.png)  |  U+2265  | GREATER-THAN OR EQUAL TO
243 | ≤ | ![≤](font1/F3.png)  |  U+2264  | LESS-THAN OR EQUAL TO
244 | ½ | ![½](font1/F4.png)  |  U+BD  | VULGAR FRACTION ONE HALF
245 | ¼ | ![¼](font1/F5.png)  | U+BC   | VULGAR FRACTION ONE QUARTER
246 | ÷ | ![÷](font1/F6.png)  |  U+F7  | DIVISION SIGN
247 | ≈ | ![≈](font1/F7.png)  |   U+2248 | ALMOST EQUAL TO
248 | \` | ![\`](font1/F8.png)  |  U+60  | GRAVE ACCENT
249 | · | ![·](font1/F9.png)  | U+B7 | MIDDLE DOT
250 | ᐨ | ![ᐨ](font1/FA.png)  | U+1428 | CANADIAN SYLLABICS FINAL SHORT HORIZONTAL STROKE[^approx]
251 | √ | ![√](font1/FB.png)  | U+221A   | SQUARE ROOT
252 | ⁿ | ![ⁿ](font1/FC.png)  |  U+207F  | SUPERSCRIPT LATIN SMALL LETTER N
253 | ² | ![²](font1/FD.png)  | U+B2 | SUPERSCRIPT TWO
254 | ∎ | ![∎](font1/FE.png)  |  U+220E  | END OF PROOF
255 | ✵ | ![✵](font1/FF.png)  |  U+2735  | EIGHT POINTED PINWHEEL STAR[^approx]

[^approx]: visual approximation, using the closest match
[^no]: no unicode equivalent as of Unicode v16.0 (Sep. 2024)

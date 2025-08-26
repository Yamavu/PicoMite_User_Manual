# Style Guide

*Just some common sense suggestions that proved allright.*

* After a Chapter or chapter denoted by `#` (1 or many) use 2 blank lines. After a paragraph one blank line.
* Any code or letters that are meant to be device input should be written as markdown code using inline backticks `` ` ``. 
  * Commands
  * Example Parameters or values
* Example Code should be formatted using ` ```basic ` and ` ``` `. A single empty line should be before and after.
* Use unicode where applicable, markdown allows for full UTF-8. The document should be understandable, even when viewed in ASCII compatibility mode.
* Bullet lists use `* `, non-bullet lists use `- `. Numbered lists should only be used if the order is absolutely necessary.
* Emphasis (underlined and all caps in original) should be denoted by `*` and use normal case.

## Images

* Images should be Jpeg (with `.jpg` extension) or SVG. End embeded in a styled `<div>`

    ```
    <div style="clear: both; margin: .5em 5em;">
    <img src="07_editor.jpg" alt="Raspberry Pi Pico pinout" style="width:100%">
    </div>
    ```


## Writing

* Sentences should end with single punctuation.
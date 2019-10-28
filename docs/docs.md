# DigiFormatter
<p id="subtitle"><strong>Make your terminals look spicy.</strong></p>

Oh, terminals. Lost to time, replaced by the ever-prevalent GUI. Why, in this age of nostalgia, do we restrict its growing reach to only synthwave music, 16-bit video games, and <span class="macplus"> a e s t h e t i c </span> video filters? Terminals are going to come back, I can feel it. And why not add a little pizzazz while we're at it? Unlike what hacker movies from the 2000's would like you to believe, terminals weren't all black and green. Special characters, colors, and overwriting made terminals a powerful and beautiful user interaction tool. And much like everything else in Python, now you can `import` it.

Current version `0.3.1`.

_________________________

## How to install
**Windows:** Open a Command Prompt as Admin and run `pip install git+https://github.com/DigiDuncan/DigiFormatter`.

**Linux:** Open a ~~Command Prompt~~ Bash Terminal and run `sudo pip install git+https://github.com/DigiDuncan/DigiFormatter`

**Mac:** &#xAF;&#x5C;&#x5F;&#x28;&#x30C4;&#x29;&#x5F;&#x2F;&#xAF;

Requires Python 3+ and the `colored` module (which should install itself.)

## How to import

If you've installed it right, you should just be able to use `import digiformatter`. I prefer to use `import digiformatter as <name>` since `digiformatter` is kinda long.

_________________________
#### Constants
* [BLANK, TWENTYFIVE, FIFTY, SEVENTYFIVE, FULL](#blocks)
* [BELL](#bell)
* [ESC](esc)
* [CURSOR\_UP, CURSOR\_DOWN, CURSOR\_RIGHT, CURSOR\_LEFT](#cursormove)
* [CURSOR\_HOME](#cursorhome)
* [SAVE\_CURSOR, LOAD\_CURSOR](#cursorsavestates)
* [START\_CURSOR\_BLINKING, STOP\_CURSOR\_BLINKING](#cursorblink)
* [SHOW\_CURSOR, HIDE\_CURSOR](#cursorshowhide)
* [SCROLL\_UP, SCROLL\_DOWN](#viewportscrolls)
* [INSERT\_BLANK, DELETE\_CHAR, INSERT\_LINE, DELETE\_LINE](#insanddel)
* [CLEAR\_LINE\_FROM\_CURSOR\_RIGHT, CLEAR\_LINE\_FROM\_CURSOR\_LEFT](#cursorclearline)
* [CLEAR\_SCREEN\_FROM\_CURSOR\_DOWN, CLEAR\_SCREEN\_FROM\_CURSOR\_UP](#cursorclearscreen)
* [CLEAR\_SCREEN](#clearscreen)
* [END\_OF\_LINE, BEGIN\_OF\_LINE](#endandstart)
* [RESET_TERMINAL](#resetterminal)

#### Functions
- Cursor Movement Functions
    * [cursorUp()](#cursorUp)
    * [cursorDown()](#cursorDown)
    * [cursorRight()](#cursorRight)
    * [cursorLeft()](#cursorLeft)
- Scrolling Functions
    * [scrollUp()](#scrollUp)
    * [scrollDown()](#scrollDown)
- Window Functions
    * [setWindowTitle()](#setwindowtitle)
- Setter Functions
    * [timecolor()](#timecolor)
    * [msgcolor()](#msgcolor)
    * [testcolor()](#testcolor)
    * [linelength()](#linelength)
    * [timestring()](#timestring)
- Message Printing Functions
    * [time()](#time)
    * [msg()](#msg)
    * [load()](#load)
    * [warn()](#warn)
    * [crit()](#crit)
    * [test()](#test)
- Custom Color Preset Functions
    * [createCustom()](#createCustom)
    * [custom()](#custom)
- Misc Functions
    * [createLoadBar()](#createLoadBar)
    * [truncate()](#truncate)

_________________________

## Constants

### <a id ="blocks"></a>`digiformatter`.**BLANK**, .**TWENTYFIVE**, .**FIFTY**, .**SEVENTYFIVE**, .**FULL**
Aliases for Extended ASCII "block characters". In order, 32 ("&#32;"), 176 ("░"), 177 ("▒"), 178 ("▓"), and 219 ("█").

<p id="comment"><i>//Yes, I know ASCII code 32 is just a space.</i></p>

### <a id ="bell"></a>`digiformatter`.**BELL**
Aliases for the ASCII character `07`, which when printed, is invisible, and plays a "bell" or "alert" sound.
<p class="alias">Aliases: <code>BEL</code></p>

### <a id ="esc"></a>`digiformatter`.**ESC**
Not really designed to be used in a program. Equates to the character octal <code>033<sub>8</sub></code> ("&#27;"). This is the [VT-100 formatting](http://www.termsys.demon.co.uk/vtansi.htm) escape character.

<p id="comment"><i>//The character "&#27;" is invisible and will not be able to be displayed, or will show up as a replacement character (a box or a "�").</i></p>

### <a id ="cursormove"></a>`digiformatter`.**CURSOR\_UP**, .**CURSOR\_DOWN**, .**CURSOR\_RIGHT**, .**CURSOR\_LEFT**
Prints VT-100 codes that move the cursor in the direction indicated. By default, for reference, the cursor is placed at the end of the last printed text.
Equates to `digiformatter.ESC` + `A`, `B`, `C`, and `D` respectively.
<p class="alias">Aliases: <code>C_UP</code>, <code>C_DOWN</code>, <code>C_RIGHT</code>, <code>C_LEFT</code></p>

### <a id ="cursorhome"></a>`digiformatter`.**CURSOR\_HOME**
Prints VT-100 code that move the cursor to the top-left corner of the screen.
Equates to `digiformatter.ESC` + `H`
<p class="alias">Aliases: <code>C_HOME</code></p>

### <a id ="cursorsavestates"></a>`digiformatter`.**SAVE\_CURSOR**, .**LOAD\_CURSOR**
Prints VT-100 codes that save and load the cursor position.
Equates to `digiformatter.ESC` + `7` and `8` respectively.
<p class="alias">Aliases: <code>C_SAVE</code>, <code>C_LOAD</code></p>

### <a id ="cursorblink"></a>`digiformatter`.**START\_CURSOR\_BLINKING**, .**STOP\_CURSOR\_BLINKING**
Prints VT-100 codes that start and stop the cursor blinking, respectively.
Equates to `digiformatter.ESC` + `[?12h` and `[?12l` respectively.
<p class="alias">Aliases: <code>C_BLINK_ON</code>, <code>C_BLINK_OFF</code></p>

### <a id ="cursorshowhide"></a>`digiformatter`.**SHOW\_CURSOR**, .**HIDE\_CURSOR**
Prints VT-100 codes that show and hide the cursor position, respectively.
Equates to `digiformatter.ESC` + `[?25h` and `[?25l` respectively.
<p class="alias">Aliases: <code>C_SHOW</code>, <code>C_HIDE</code></p>

### <a id ="viewportscrolls"></a>`digiformatter`.**SCROLL\_UP**, .**SCROLL\_DOWN**
Prints VT-100 codes that scroll the viewport up or down, respectively.
Equates to `digiformatter.ESC` + `[1S` and `[1T` respectively.

### <a id ="insanddel"></a>`digiformatter`.**INSERT\_BLANK**, .**DELETE\_CHAR**, **ERASE\_CHAR**, .**INSERT\_LINE**, .**DELETE\_LINE**
Prints VT-100 codes that insert and delete characters and lines, as per their names.
Equates to `digiformatter.ESC` + `[1@`, `[1P`, `[1X`, `[1L`, and `[1M` respectively.
<p class="alias">Aliases: <code>INS_BLANK</code>, <code>DEL_CHAR</code>, <code>ERS_CHAR</code>, <code>INS_LINE</code>, <code>DEL_CHAR</code></p>

### <a id ="cursorclearline"></a>`digiformatter`.**CLEAR\_LINE\_FROM\_CURSOR\_RIGHT**, .**CLEAR\_LINE\_FROM\_CURSOR\_RIGHT**
Prints VT-100 codes that clear the line starting at the cursor position and moving either right or left, respectively.
Equates to `digiformatter.ESC` + `[0K` and `[1K` respectively.
<p class="alias">Aliases: <code>CLEAR_RIGHT</code>, <code>CLEAR_LEFT</code></p>

### <a id ="cursorclearscreen"></a>`digiformatter`.**CLEAR\_SCREEN\_FROM\_CURSOR\_DOWN**, .**CLEAR\_SCREEN\_FROM\_CURSOR\_UP**
Prints VT-100 codes that clear the screen starting at the cursor position and moving either down or up, respectively.
Equates to `digiformatter.ESC` + `[0J` and `[1J` respectively.
<p class="alias">Aliases: <code>CLEAR_DOWN</code>, <code>CLEAR_UP</code></p>

### <a id ="clearscreen"></a>`digiformatter`.**CLEAR\_SCREEN**
Prints VT-100 code that clears the screen.
Equates to `digiformatter.ESC` + `[2J`
<p class="alias">Aliases: <code>CLEAR</code> or <code>CLS</code></p>

### <a id ="endandstart"></a>`digiformatter`.**END\_OF\_LINE**, .**BEGIN\_OF\_LINE**
Prints `digiformatter.CURSOR_RIGHT` or `digiformatter.CURSOR_LEFT` `digiformatter.linelength` times. See [`digiformatter.linelength()`](#linelength).
<p class="alias">Aliases: <code>EOL</code>, <code>BOL</code></p>

### <a id ="resetterminal"></a>`digiformatter`.**RESET\_TERMINAL**
Prints VT-100 code that resets the terminal to its initial state.
Equates to `digiformatter.ESC` + `c`
<p class="alias">Aliases: <code>RESET</code></p>

## Cursor Movement Functions

### <a id ="cursorUp"></a>`digiformatter`.**cursorUp(** *int* amount **)**
### <a id ="cursorDown"></a>`digiformatter`.**cursorDown(** *int* amount **)**
### <a id ="cursorRight"></a>`digiformatter`.**cursorRight(** *int* amount **)**
### <a id ="cursorLeft"></a>`digiformatter`.**cursorLeft(** *int* amount **)**
Moves the cursor in the direction indicated `amount` lines (for `cursorUp` and `cursorDown`) or characters (for `cursorLeft` and `cursorRight`).

## Scrolling Functions

### <a id ="scrollUp"></a>`digiformatter`.**scrollUp(** *int* amount **)**
### <a id ="scrollDown"></a>`digiformatter`.**scrollDown(** *int* amount **)**
Scrolls the viewport `amount` lines up or down, respectively.

## Window Functions

### <a id ="cursorLeft"></a>`digiformatter`.**setWindowTitle(** *str* string **)**
Set the window title to `string`.

## Setter Functions

### <a id ="timecolor"></a>`digiformatter`.**timecolor(** *int* new **)**
Sets the variable `digiformatter.timecolor` defaults to `5`, or `colored.PURPLE`. See [`digiformatter.time()`](#time).

### <a id ="msgcolor"></a>`digiformatter`.**msgcolor(** *int* new **)**
Sets the variable `digiformatter.msgcolor` defaults to `51`, or `colored.CYAN_1`. See `digiformatter.msg()`

### <a id ="testcolor"></a>`digiformatter`.**testcolor(** *int* new **)**
Sets the variable `digiformatter.testcolor` defaults to `4`, or `colored.BLUE`. See [`digiformatter.test()`](#test).

### <a id ="linelength"></a>`digiformatter`.**linelength(** *int* new **)**
Sets the variable `digiformatter.linelength` defaults to `100`.

### <a id ="timestring"></a>`digiformatter`.**timestring(** *str* new **)**
Sets the variable `digiformatter.linelength` defaults to `"%d %b %H:%M:%S"`.
See [`digiformatter.time()`](#time)

## Message Printing Functions

### <a id ="time"></a>`digiformatter`.**time()**
Returns a string in the color `digiformatter.timecolor` and in the format `strftime(f"{digiformatter.timestring} | ", localtime())`. See [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime) and [`time.localtime()`](https://docs.python.org/3/library/time.html#time.localtime).

### <a id ="msg"></a>`digiformatter`.**msg(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `digiformatter.msgcolor`, prefixed with `digiformatter.time()` if `showtime` = True.

### <a id ="load"></a>`digiformatter`.**load(** *str* message, *bool* showtime = <u>False</u>)
Prints a message in color `colored.colors.GREY_27`, prefixed with `digiformatter.time()` if `showtime` = True.

### <a id ="warn"></a>`digiformatter`.**warn(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `colored.colors.YELLOW`, prefixed with `digiformatter.time()` if `showtime` = True.

### <a id ="crit"></a>`digiformatter`.**crit(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `colored.colors.WHITE`, with background `colored.colors.RED`, with style `colored.style.BOLD`, prefixed with `digiformatter.time()` if `showtime` = True.

### <a id ="test"></a>`digiformatter`.**test(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `digiformatter.testcolor`, prefixed with `digiformatter.time()` if `showtime` = True.

### <a id ="overwriteLines"></a>`digiformatter`.**overwriteLines(** *int* lines **)**
Overwrites (clears) *lines* lines counting up from and including the line occupied by the cursor currently.

## Custom Color Preset Functions

### <a id ="createCustom"></a>`digiformatter`.**createCustom(** *str* name, *int/str* fore = <u>256</u>, *int/str* back = <u>256</u>, *int/str* attr = <u>None</u> **)**
Creates a custom message color preset.

* fore, back: Can be set to any valid `colored` color. See [`colored.colors`](https://pypi.org/project/colored/). Defaults to 256, or `colored.colors.DEFAULT`.
* attr: Can be set to any valid `colored` attribute. See [`colored.style`](https://pypi.org/project/colored/). Defaults to None.

See [`digiformatter.custom()`](#custom).

### <a id ="custom"></a>`digiformatter`.**custom(** *str* name, *str* message, *bool* showtime = <u>True</u> **)**
Prints a message in colors defined by previously defined preset `name`, prefixed with `digiformatter.time()` if `showtime` = True.

## Misc Functions

### <a id ="createLoadBar"></a>`digiformatter`.**createLoadBar(** *int* current, *int* total, *int* barlength, *bool* showpercent = <u>False</u>
Creates a bar representing the percentage `current`/`total` * 100, in which the bar is length `barlength` when percentage is 100, suffixed by the percentage rounded to the nearest two decimal places if `showpercent` = True.

### <a id ="truncate"></a>`digiformatter`.**truncate(** *str* item, *int* trunclen = <u>80</u> **)**
Returns `item` is its length is less than or equal to `trunclen`, else returns the first `trunclen - 1` characters of `item`, suffixed by "…" (the ellipses character.)

_________________________

<footer> &copy;2019 DigiDuncan. Free for public use. </footer>

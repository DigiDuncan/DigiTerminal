# DigiFormatter
**Make your terminals look spicy.**

Oh, terminals. Lost to time, replaced by the ever-prevalent GUI. Why, in this age of nostalgia, do we restrict its growing reach to only synthwave music, 16-bit video games, and ａｅｓｔｈｅｔｉｃ video filters? Terminals are going to come back, I can feel it. And why not add a little pizzazz while we're at it? Unlike what hacker movies from the 2000's would like you to believe, terminals weren't all black and green. Special characters, colors, and overwriting made terminals a powerful and beautiful user interaction tool. And much like everything else in Python, now you can `import` it.

## How to install
**Windows:** Open a Command Prompt as Admin and run `pip install git+https://github.com/DigiDuncan/DigiFormatter`.

**Linux:** Probably the same thing as Windows?

**Mac:** ¯\\\_(ツ)\_/¯

Requires Python 3+ and the `colored` module (which should install itself.)

## How to import

If you've installed it right, you should just be able to use `import digiformatter`. I prefer to use `import digiformatter as <name>` since `digiformatter` is kinda long.

_________________________

## Constants

### `digiformatter`.**BLANK**, .**TWENTYFIVE**, .**FIFTY**, .**SEVENTYFIVE**, .**FULL**
Aliases for Extended ASCII "block characters". In order, 32 (" "), 176 ("░"), 177 ("▒"), 178 ("▓"), and 219 ("█").

*//Yes, I know ASCII code 32 is just a space.*

### `digiformatter`.**BELL**
Aliases for the ASCII character 07, which when printed, is invisible, and plays a "bell" or "alert" sound.

### `digiformatter`.**ESC**
Not really designed to be used in a program. Equates to the character octal 033<sub>8</sub> (""). This is the [VT-100 formatting](http://www.termsys.demon.co.uk/vtansi.htm) escape character.

### `digiformatter`.**CURSOR_UP**, .**CURSOR_DOWN**, .**CURSOR_RIGHT**, .**CURSOR_LEFT**
Prints VT-100 codes that move the cursor in the direction indicated. By default, for reference, the cursor is placed at the end of the last printed text.
Equates to `digiformatter.ESC` + `A`, `B`, `C`, and `D` respectively.

### `digiformatter`.**SAVE_CURSOR**, .**LOAD_CURSOR**
Prints VT-100 codes that save and load the cursor position.
Equates to `digiformatter.ESC` + `7` and `8` respectively.

### `digiformatter`.**INSERT_BLANK**, .**DELETE_CHAR**, .**INSERT_LINE**, .**DELETE_LINE**
Prints VT-100 codes that insert and delete characters and lines, as per their names.
Equates to `digiformatter.ESC` + `[1@`, `[1X`, `[1L`, and `[1M` respectively.

### `digiformatter`.**END_OF_LINE**, .**BEGIN_OF_LINE**
Prints `digiformatter.CURSOR_RIGHT` or `digiformatter.CURSOR_LEFT` `digiformatter.linelength` times. See `digiformatter.linelength()`.

## Setter Functions

### `digiformatter`.**timecolor(** *int* new **)**
Sets the variable `digiformatter.timecolor` defaults to `5`, or `colored.PURPLE`. See `digiformatter.time()`

### `digiformatter`.**msgcolor(** *int* new **)**
Sets the variable `digiformatter.msgcolor` defaults to `51`, or `colored.CYAN_1`. See `digiformatter.msg()`

### `digiformatter`.**testcolor(** *int* new **)**
Sets the variable `digiformatter.testcolor` defaults to `4`, or `colored.BLUE`. See `digiformatter.test()`

### `digiformatter`.**linelength(** *int* new **)**
Sets the variable `digiformatter.linelength` defaults to `100`.

### `digiformatter`.**timestring(** *str* new **)**
Sets the variable `digiformatter.linelength` defaults to `"%d %b %H:%M:%S"`.
See `digiformatter.time()`

## Message Printing Functions

### `digiformatter`.**time()**
Returns a string in the color `digiformatter.timecolor` and in the format `strftime(f"{digiformatter.timestring} | ", localtime())`. See `time.strftime()` and `time.localtime()`.

### `digiformatter`.**msg(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `digiformatter.msgcolor`, prefixed with `digiformatter.time()` if `showtime` = True.

### `digiformatter`.**load(** *str* message, *bool* showtime = <u>False</u>)
Prints a message in color `colored.colors.GREY_27`, prefixed with `digiformatter.time()` if `showtime` = True.

### `digiformatter`.**warn(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `colored.colors.YELLOW`, prefixed with `digiformatter.time()` if `showtime` = True.

### `digiformatter`.**crit(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `colored.colors.WHITE`, with background `colored.colors.RED`, with style `colored.style.BOLD`, prefixed with `digiformatter.time()` if `showtime` = True.

### `digiformatter`.**test(** *str* message, *bool* showtime = <u>True</u>)
Prints a message in color `digiformatter.testcolor`, prefixed with `digiformatter.time()` if `showtime` = True.

### `digiformatter`.**overwriteLines(** *int* lines **)**
Overwrites (clears) *lines* lines counting up from and including the line occupied by the cursor currently.

## Custom Color Preset Functions

### `digiformatter`.**createCustom(** *str* name, *int/str* fore = <u>256</u>, *int/str* back = <u>256</u>, *int/str* attr = <u>None</u> **)**
Creates a custom message color preset.

* fore, back: Can be set to any valid `colored` color. See `colored.colors`. Defaults to 256, or `colored.colors.DEFAULT`.
* attr: Can be set to any valid `colored` attribute. See `colored.style`. Defaults to None.

See `digiformatter.custom()`.

### `digiformatter`.**custom(** *str* name, *str* message, *bool* showtime = <u>True</u> **)**
Prints a message in colors defined by previously defined preset `name`, prefixed with `digiformatter.time()` if `showtime` = True.

## Misc Functions

### `digiformatter`.**createLoadBar(** *int* current, *int* total, *int* barlength, *bool* showpercent = <u>False</u>
Creates a bar representing the percentage `current`/`total` * 100, in which the bar is length `barlength` when percentage is 100, suffixed by the percentage rounded to the nearest two decimal places if `showpercent` = True.

### `digiformatter`.**truncate(** *str* item, *int* trunclen = <u>80</u> **)**
Returns `item` is its length is less than or equal to `trunclen`, else returns the first `trunclen - 1` characters of `item`, suffixed by "…" (the ellipses character.)

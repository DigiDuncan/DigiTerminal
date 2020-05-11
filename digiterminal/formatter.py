import os

__all__ = ["cursorUp", "cursorDown", "cursorRight", "cursorLeft", "scrollUp",
           "scrollDown", "setWindowTitle", "overwriteLines"]

# Activate VT-100 terminal formatting
os.system("")

linelength = 132

# ASCII/ANSI characters
BLANK = " "
BELL = BEL = "\x07"

# VT-100 escape sequences
ESC = "\033"

SET_NEW_LINE_MODE = ESC + "[20h"
SET_CURSOR_KEY_TO_APP = ESC + "?1h"
SET_COLUMN_NUM_132 = ESC + "?3h"
SET_SMOOTH_SCROLLING = ESC + "?4h"
SET_REVERSE_VIDEO = ESC + "?5h"
SET_RELATIVE_ORIGIN = ESC + "?6h"
SET_AUTO_WRAP = ESC + "?7h"
SET_AUTO_REPEAT = ESC + "?8h"
SET_INTERLACING = ESC + "?9h"

SET_LINE_FEED_MODE = ESC + "[20l"
SET_CURSOR_KEY_TO_CURSOR = ESC + "?1l"
TOGGLE_VT_ANSI = ESC + "?2l"
SET_COLUMN_NUM_80 = ESC + "?3l"
SET_JUMP_SCROLLING = ESC + "?4l"
SET_NORMAL_VIDEO = ESC + "?5l"
SET_ABSOLUTE_ORIGIN = ESC + "?6l"
RESET_AUTO_WRAP = ESC + "?7l"
RESET_AUTO_REPEAT = ESC + "?8l"
RESET_INTERLACING = ESC + "?9l"

SET_ALT_KEYPAD = ESC + "="
SET_NUM_KEYPAD = ESC + ">"

SET_SINGLE_SHIFT_2 = ESC + "N"
SET_SINGLE_SHIFT_3 = ESC + "O"

CHAR_ATTRIBUTES_OFF = ESC + "[0m"
BOLD = ESC + "[1m"
LOW_INTENSITY = ESC + "[2m"
UNDERLINE = ESC + "[4m"
BLINK = ESC + "[5m"
REVERSE = REV = ESC + "[7m"
INVISIBLE = ESC + "[8m"

CURSOR_UP = C_UP = ESC + "A"
CURSOR_DOWN = C_DOWN = ESC + "B"
CURSOR_RIGHT = C_RIGHT = ESC + "C"
CURSOR_LEFT = C_LEFT = ESC + "D"
CURSOR_NEXT_LINE = C_NEXT_LINE = NEXT_LINE = ESC + "E"
CURSOR_HOME = C_HOME = ESC + "[H"

SAVE_CURSOR = C_SAVE = ESC + "7"
LOAD_CURSOR = C_LOAD = ESC + "8"

GET_CURSOR_POS = GET_CURSOR = ESC + "[6n"

SET_TAB = ESC + "H"
CLEAR_TAB_AT_COLUMN = ESC + "[0g"
CLEAR_ALL_TABS = ESC + "[3g"

DOUBLE_HEIGHT_LETTERS_TOP = ESC + "#3"
DOUBLE_HEIGHT_LETTERS_BOTTOM = ESC + "#4"
SINGLE_WIDTH_LETTERS = ESC + "#5"
DOUBLE_WIDTH_LETTERS = ESC + "#6"

START_CURSOR_BLINKING = C_BLINK_ON = ESC + "[?12h"
STOP_CURSOR_BLINKING = C_BLINK_OFF = ESC + "[?12l"
SHOW_CURSOR = C_SHOW = ESC + "[?25h"
HIDE_CURSOR = C_HIDE = ESC + "[?25l"

SCROLL_UP = ESC + "[1M"
SCROLL_DOWN = ESC + "[1D"

INSERT_BLANK = INS_BLANK = ESC + "[1@"
DELETE_CHAR = DEL_CHAR = ESC + "[1P"
ERASE_CHAR = ERS_CHAR = ESC + "[1X"
INSERT_LINE = INS_LINE = ESC + "[1L"
DELETE_LINE = DEL_LINE = ESC + "[2K"

CLEAR_LINE_FROM_CURSOR_RIGHT = CLEAR_RIGHT = ESC + "[0K"
CLEAR_LINE_FROM_CURSOR_LEFT = CLEAR_LEFT = ESC + "[1K"

CLEAR_SCREEN_FROM_CURSOR_DOWN = CLEAR_DOWN = ESC + "[0J"
CLEAR_SCREEN_FROM_CURSOR_UP = CLEAR_UP = ESC + "[1J"

CLEAR_SCREEN = CLEAR = CLS = ESC + "[2J"

END_OF_LINE = EOL = CURSOR_RIGHT * linelength
BEGIN_OF_LINE = BOL = CURSOR_LEFT * linelength

RESET_TERMINAL = RESET = ESC + "c"

SCREEN_ALIGNMENT_DISPLAY = ESC + "#8"

LED_1 = ESC + "[1q"
LED_2 = ESC + "[2q"
LED_3 = ESC + "[3q"
LED_4 = ESC + "[4q"
LEDS_OFF = ESC + "[0q"


# Cursor movement functions
def cursorUp(amount):
    """Move the screen cursor to the up"""
    print(ESC + f"[{amount}A", end = "")


def cursorDown(amount):
    """Move the screen cursor to the down"""
    print(ESC + f"[{amount}B", end = "")


def cursorRight(amount):
    """Move the screen cursor to the right"""
    print(ESC + f"[{amount}C", end = "")


def cursorLeft(amount):
    """Move the screen cursor to the left"""
    print(ESC + f"[{amount}D", end = "")


def goto(x, y):
    "Go to an X,Y coordinate in the window"
    print(ESC + f"[{x};{y}H", end = "")


# Currently disabled because the getCursorPosition code I could
# find only works on Linux due to a termios dependency.
# def BOL():
#     "Go to the beginning of the line."
#     x, y = getCursorPosition()
#     goto(1, y)


def scrollUp(amount):
    """Scroll up"""
    print(ESC + f"[{amount}S", end = "")


def scrollDown(amount):
    """Scroll down"""
    print(ESC + f"[{amount}T", end = "")


def setWindowTitle(s):
    """Set window title"""
    print(ESC + f"2;{s}{BELL}", end = "")


def setWindowBounds(top, bottom):
    """Set the top and bottom line of a window."""
    print(ESC + f"[{top};{bottom}r", end = "")


def overwriteLines(lines, hack = False):
    """Delete an amount of lines"""
    if hack:
        linedel = DELETE_LINE + (" " * linelength)
    else:
        linedel = DELETE_LINE
    for li in range(lines):
        print(BOL + linedel, end = "")
        if li != lines - 1:
            print(CURSOR_UP, end = "")
    print(BOL, end = "")

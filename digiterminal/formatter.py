import os

__all__ = ["cursorUp", "cursorDown", "cursorRight", "cursorLeft", "scrollUp", "scrollDown", "setWindowTitle", "overwriteLines"]

# Activate VT-100 terminal formatting
os.system("")

linelength = 132

# ASCII/ANSI characters
BLANK = " "
BELL = BEL = "\x07"

# VT-100 escape sequences
ESC = "\033"

CURSOR_UP = C_UP = ESC + "A"
CURSOR_DOWN = C_DOWN = ESC + "B"
CURSOR_RIGHT = C_RIGHT = ESC + "C"
CURSOR_LEFT = C_LEFT = ESC + "D"
CURSOR_NEXT_LINE = C_NEXT_LINE = NEXT_LINE = ESC + "E"
CURSOR_HOME = C_HOME = ESC + "H"

SAVE_CURSOR = C_SAVE = ESC + "7"
LOAD_CURSOR = C_LOAD = ESC + "8"

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


# Cursor movement functions
def cursorUp(amount):
    """Move the screen cursor to the up"""
    print(ESC + f"[{amount}A")


def cursorDown(amount):
    """Move the screen cursor to the down"""
    print(ESC + f"[{amount}B")


def cursorRight(amount):
    """Move the screen cursor to the right"""
    print(ESC + f"[{amount}C")


def cursorLeft(amount):
    """Move the screen cursor to the left"""
    print(ESC + f"[{amount}D")


def goto(x, y):
    "Go to an X,Y coordinate in the window"
    print(ESC + f"[{x};{y}H")


def scrollUp(amount):
    """Scroll up"""
    print(ESC + f"[{amount}S")


def scrollDown(amount):
    """Scroll down"""
    print(ESC + f"[{amount}T")


def setWindowTitle(s):
    """Set window title"""
    print(ESC + f"2;{s}{BELL}")


def overwriteLines(lines, hack = False):
    """Delete an amount of lines"""
    if hack:
        linedel = DELETE_LINE + (" " * linelength)
    else:
        linedel = DELETE_LINE
    for li in range(lines):
        print(BEGIN_OF_LINE + linedel, end = "")
        if li != lines - 1:
            print(CURSOR_UP)
    print(BEGIN_OF_LINE)

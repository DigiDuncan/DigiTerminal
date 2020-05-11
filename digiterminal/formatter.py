import os
import re
import sys
import termios
import tty

__all__ = ["cursorUp", "cursorDown", "cursorRight", "cursorLeft", "getCursorPosition", "scrollUp",
           "scrollDown", "setWindowTitle", "overwriteLines"]

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

GET_CURSOR_POS = GET_CURSOR = ESC + "[6n"

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
# BEGIN_OF_LINE = BOL = CURSOR_LEFT * linelength

RESET_TERMINAL = RESET = ESC + "c"


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


# Stolen code: see https://github.com/pboardman/py100/blob/master/py100/py100.py
def getCursorPosition():
    """Get cursor position as a tuple (x, y)"""

    buf = ""
    stdin = sys.stdin.fileno()
    tattr = termios.tcgetattr(stdin)

    try:
        tty.setcbreak(stdin, termios.TCSANOW)
        sys.stdout.write(GET_CURSOR)
        sys.stdout.flush()

        while True:
            buf += sys.stdin.read(1)
            if buf[-1] == 'R':
                break

    finally:
        termios.tcsetattr(stdin, termios.TCSANOW, tattr)

    matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
    groups = matches.groups()

    return (int(groups[1]), int(groups[0]))


def goto(x, y):
    "Go to an X,Y coordinate in the window"
    print(ESC + f"[{x};{y}H", end = "")


def BOL():
    "Go to the beginning of the line."
    x, y = getCursorPosition()
    goto(1, y)


def scrollUp(amount):
    """Scroll up"""
    print(ESC + f"[{amount}S", end = "")


def scrollDown(amount):
    """Scroll down"""
    print(ESC + f"[{amount}T", end = "")


def setWindowTitle(s):
    """Set window title"""
    print(ESC + f"2;{s}{BELL}", end = "")


def overwriteLines(lines, hack = False):
    """Delete an amount of lines"""
    if hack:
        linedel = DELETE_LINE + (" " * linelength)
    else:
        linedel = DELETE_LINE
    for li in range(lines):
        BOL()
        print(linedel, end = "")
        if li != lines - 1:
            print(CURSOR_UP, end = "")
    BOL()

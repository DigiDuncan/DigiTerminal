import os
import math
from time import strftime, localtime

from colored import fore, back, style, fg, bg, attr

#Activate VT-100 terminal formatting.
os.system("")

#Customizables.
timecolor = 5
msgcolor = 51
testcolor = 4
linelength = 100

#ASCII/ANSI characters.
BLANK = ' '
TWENTYFIVE = '\u2591'
FIFTY = '\u2592'
SEVENTYFIVE = '\u2593'
FULL = '\u2588'
BELL = '\x07'

#VT-100 escape sequences.
ESC = '\033'

CURSOR_UP = ESC + 'A'
CURSOR_DOWN = ESC + 'B'
CURSOR_RIGHT = ESC + 'C'
CURSOR_LEFT = ESC + 'D'

SAVE_CURSOR_ = ESC + '7'
LOAD_CURSOR_ = ESC + '8'

INSERT_BLANK = ESC + "[1@"
DELETE_CHAR = ESC + "[1X"
INSERT_LINE = ESC + "[1L"
DELETE_LINE = ESC + "[1M"

END_OF_LINE = CURSOR_RIGHT * linelength
BEGIN_OF_LINE = CURSOR_LEFT * linelength

#Delete an amount of lines.
def OverwriteLines(x):
    return BeginOfLine + ((CursorUp + DeleteLine) * x)

#Set methods for customizables.
def timecolor(new):
    global timecolor
    timecolor = new
def msgcolor(new):
    global msgcolor
    msgcolor = new
def testcolor(new):
    global testcolor
    testcolor = new
def linelength(new):
    global linelength
    linelength = new

#Color styling for terminal messages.
def time():
    return (fg(timecolor) + strftime("%d %b %H:%M:%S | ", localtime()) + style.RESET)
def warn(message, t = True):
    if t: return (time() + fore.YELLOW + message + style.RESET)
    else: return (fore.YELLOW + message + style.RESET)
def crit(message, t = True):
    if t: return (time() + back.RED + style.BOLD + message + style.RESET)
    else: return (back.RED + style.BOLD + message + style.RESET)
def test(message, t = True):
    if t: return (time() + fg(testcolor) + message + style.RESET)
    else: return (fg(testcolor) + message + style.RESET)
def load(message, t = False):
    if t: return (time() + fg(238) + message + style.RESET)
    else: return (fg(238) + message + style.RESET)
def msg(message, t = True):
    if t: return (time() + fg(msgcolor) + message + style.RESET)
    else: return (fg(msgcolor) + message + style.RESET)

#Create a progress bar.
def createloadbar(current, total, barlength = 50):
	progress = ((current/total)*100)
	bar = ""
	percentage = progress
	progress *= (barlength * 4 / 100)
	progress = int(progress)
	bars = math.floor(progress/4)
	bar = FULL * bars
	shade = progress - (bars*4)
	if shade == 1: bar += TWENTYFIVE
	if shade == 2: bar += FIFTY
	if shade == 3: bar += SEVENTYFIVE
	printableperc = int((c/t)*10000) / 100
	return "{0} {1}%".format(bar, printableperc)

#Truncate a long string for terminal printing.
def truncate(item, trunclen = 80):
	if len(item) > trunclen:
		printitem = "..." + item[-trunclen:]
	else:
		printitem = item
	return printitem

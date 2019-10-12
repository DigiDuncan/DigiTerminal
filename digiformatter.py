import os
import math
from time import strftime, localtime

from colored import fore, back, style, fg, bg, attr

#Activate VT-100 terminal formatting.
os.system("")

#Constants.
FORE = 0
BACK = 1
ATTR = 2
version = "0.2.0"

#Customizables.
timecolor = 5
msgcolor = 51
testcolor = 4
linelength = 100
timestring = "%d %b %H:%M:%S"

#Customizable color presets.
customs = {}

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

SAVE_CURSOR = ESC + '7'
LOAD_CURSOR = ESC + '8'

INSERT_BLANK = ESC + "[1@"
DELETE_CHAR = ESC + "[1X"
INSERT_LINE = ESC + "[1L"
DELETE_LINE = ESC + "[1M"

END_OF_LINE = CURSOR_RIGHT * linelength
BEGIN_OF_LINE = CURSOR_LEFT * linelength

#Delete an amount of lines.
def overwriteLines(lines):
    return BeginOfLine + ((CursorUp + DeleteLine) * lines)

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
def timestring(new):
    global timestring
    timestring = new

#Color styling for terminal messages.
def time():
    return (fg(timecolor) + strftime(f"{timestring} | ", localtime()) + style.RESET)
def warn(message, showtime = True):
    if showtime: print (time() + fore.YELLOW + message + style.RESET)
    else: print (fore.YELLOW + message + style.RESET)
def crit(message, showtime = True):
    if showtime: print (time() + back.RED + style.BOLD + message + style.RESET)
    else: print (back.RED + style.BOLD + message + style.RESET)
def test(message, showtime = True):
    if showtime: print (time() + fg(testcolor) + message + style.RESET)
    else: print (fg(testcolor) + message + style.RESET)
def load(message, showtime = False):
    if showtime: print (time() + fg(238) + message + style.RESET)
    else: print (fg(238) + message + style.RESET)
def msg(message, showtime = True):
    if showtime: print (time() + fg(msgcolor) + message + style.RESET)
    else: print (fg(msgcolor) + message + style.RESET)

#Create a custom color preset.
def createCustom(name, fore = 256, back = 256, attr = None):
    global customs
    customs[name] = [fore, back, style]

#Use a custom color preset.
def custom(name, message, showtime = True):
    fgcolor = customs[name][FORE]
    bgcolor = customs[name][BACK]
    attr = customs[name][ATTR]
    if attr is not None:
        if showtime: print (time() + fg(fgcolor) + bg(bgcolor) + message + style.RESET)
        else: print (fg(fgcolor) + bg(bgcolor) + message + style.RESET)
    else:
        if showtime: print (time() + fg(fcolor) + bg(bgcolor) + attr(attr) + message + style.RESET)
        else: print (fg(fcolor) + bg(bgcolor) + attr(attr) + message + style.RESET)

#Create a progress bar.
def createLoadBar(current, total, barlength = 50, showpercent = False):
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
    returnstring = "bar"
    if showpercent: returnstring += " " + printableperc + "%"
	return returnstring

#Truncate a long string for terminal printing.
def truncate(item, trunclen = 80):
	if len(item) > trunclen:
		printitem = "…" + item[-(trunclen - 1):]
	else:
		printitem = item
	return printitem

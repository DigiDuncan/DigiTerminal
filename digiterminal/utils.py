import math


def createLoadBar(current, total, barlength = 50, showpercent = False):
    """Create a progress bar"""
    TWENTYFIVE = "\u2591"
    FIFTY = "\u2592"
    SEVENTYFIVE = "\u2593"
    FULL = "\u2588"
    shades = {
        0: " ",
        1: TWENTYFIVE,
        2: FIFTY,
        3: SEVENTYFIVE,
        4: FULL
    }

    complete = current / total          # fraction complete
    bartodraw = complete * barlength    # how long the bar should be

    fullbar = math.floor(bartodraw)     # how many full segments the bar should have
    fullbarstring = FULL * fullbar

    remainder = bartodraw - fullbar     # fraction remaining to draw
    shade = math.floor(remainder * 4)   # what shade the last segment should be
    remainderstring = shades[shade]

    barstring = fullbarstring + remainderstring
    if showpercent:
        percentage = round(complete * 100, 2)
        barstring = f"{barstring} {percentage}%"
    return barstring


def truncate(s, trunclen = 80, trailing = False):
    """Truncate a long string for terminal printing"""
    if len(s) > trunclen:
        if trailing:
            s = "…" + s[-(trunclen - 1):]
        else:
            s = s[(trunclen - 1):] + "…"
    return s

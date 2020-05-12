from time import strftime, localtime

import colored

__all__ = ["styles"]


class Styles():
    __slots__ = ["_styles", "timestring", "timestampCodes", "_defaultStyle"]

    def __init__(self):
        self._styles = {}
        self.timestring = "%d %b %H:%M:%S"
        self.timestampCodes = colored.fg("magenta")

    def create(self, *args, **kwargs):
        """Create a custom style"""
        style = StyleFormatter(*args, **kwargs)
        self._styles[style.name] = style

    def format(self, message, *, style="default", showtime=False, **kwargs):
        """Format a message in the requested style

        :param message: Message to format
        :type message: str
        :param style: Name of style formatter
        :type style: str, optional
        :param showtime: Whether or not to show a timestamp
        :type showtime: bool, optional
        :param prefix: Whether or not to show a style prefix
        :type prefix: bool, optional
        :return: Formatted message
        :rtype: str
        """
        style = style.lower()
        if style not in self._styles:
            raise ValueError(f"Unknown style: {style}")
        formatter = self._styles[style]
        timestamp = ""
        if showtime:
            timestamp = self._timestamp()
        formatted = formatter.format(message, timestamp=timestamp, **kwargs)
        return formatted

    def print(self, *args, **kwargs):
        """Print a message in the requested style"""
        print(self.format(*args, **kwargs))

    def _timestamp(self):
        """Color styling for terminal messages"""
        t = localtime()
        return self.timestampCodes + strftime(f"{self.timestring} | ", t) + colored.attr("reset")

    def __getattr__(self, name):
        name = name.lower()
        if name not in self._styles:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
        return lambda message: self.print(message, style=name)

    def __str__(self):
        return "styles: " + (" ".join(formatter.format(level, prefix=False) for level, formatter in self._styles))


class StyleFormatter():
    __slots__ = ["name", "codes", "prefix"]
    def __init__(self, name, *, fg=None, bg=None, attr=None, prefix=None):
        self.name = name.lower()
        self.codes = ""
        if fg is not None:
            self.codes += colored.fg(fg)
        if bg is not None:
            self.codes += colored.bg(bg)
        if attr is not None:
            self.codes += colored.attr(attr)
        self.prefix = self.formatPrefix(prefix)

    def formatPrefix(self, prefix):
        if not prefix:
            return ""
        return self.codes + colored.attr("reverse") + prefix + colored.attr("reset") + " "

    def format(self, message, *, timestamp="", prefix=True):
        formatted = ""
        if prefix:
            formatted += self.prefix
        formatted += timestamp
        formatted += self.codes + message + colored.attr("reset")
        return formatted



styles = Styles()

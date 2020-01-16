from digiformatter import createStyle, formatStyle

__all__ = ["trace", "debug", "info", "warn", "error", "log"]

createStyle("trace", fg="grey_27")
createStyle("debug", fg="blue")
createStyle("info", fg="cyan_1")
createStyle("warn", fg="yellow")
createStyle("error", fg="red", attr="bold")


def trace(message):
    log(message, level="trace")


def debug(message):
    log(message, level="debug")


def info(message):
    log(message, level="info")


def warn(message):
    log(message, level="warn")


def error(message):
    log(message, level="error")


def log(message, level="info"):
    print(formatStyle(level, message))

import logging

from digiterminal import styles

__all__ = ["debug", "info", "warn", "error", "critical", "log"]

styles.create("debug", prefix="DBG", fg="blue")                               # DEBUG
styles.create("info", prefix="INF")                                           # INFO
styles.create("warning", prefix="WRN", fg="yellow")                           # WARNING
styles.create("warn", prefix="WRN", fg="yellow")                              # WARN - DEPRECATED (use WARNING)
styles.create("error", prefix="ERR", fg="red", attr="bold")                   # ERROR
styles.create("critical", prefix="CRI", fg="yellow", bg="red", attr="bold")   # CRITICAL
styles.create("fatal", prefix="CRI", fg="yellow", bg="red", attr="bold")      # FATAL - DEPRECATED (use CRITICAL)


def debug(message, **kwargs):
    log(message, level="debug", **kwargs)


def info(message, **kwargs):
    log(message, level="info", **kwargs)


def warn(message, **kwargs):
    log(message, level="warning", **kwargs)


def error(message, **kwargs):
    log(message, level="error", **kwargs)


def critical(message, **kwargs):
    log(message, level="critical", **kwargs)


def log(message, *, level="info", showtime=True, **kwargs):
    styles.print(message, style=level, showtime=showtime, **kwargs)


class DigiTerminalHandler(logging.Handler):
    def emit(self, record):
        message = record.getMessage()
        log(message, level=record.levelname.lower())


# Get the next unassigned log level, higher than the base level specified (default to 20: INFO)
def getFreeLevel(base=None):
    baselevel = logging._nameToLevel.get(base, 20)
    level = baselevel
    while level in logging._levelToName:
        level += 1
    return level


def addLogLevel(name, *args, base=None, **kwargs):
    styles.create(name, *args, **kwargs)
    freelevel = getFreeLevel(base)
    logging.addLevelName(name, freelevel)
    return freelevel

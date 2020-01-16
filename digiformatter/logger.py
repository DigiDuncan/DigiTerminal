from digiformatter import styles

__all__ = ["trace", "debug", "info", "warn", "error", "log"]

styles.create("trace", fg="grey_27")
styles.create("debug", fg="blue")
styles.create("info", fg="cyan_1")
styles.create("warn", fg="yellow")
styles.create("error", fg="red", attr="bold")


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
    print(styles.print(message, style=level))

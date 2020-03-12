import logging
import sys


class _PrettyFormatter(logging.Formatter):
    def format(self, record):
        message = record.getMessage()
        if record.levelno < logging.WARNING:
            return message
        return f"{record.levelname}: {message}"


def configure_logging(level):
    h = logging.StreamHandler(sys.stderr)
    if level >= logging.INFO:
        f = _PrettyFormatter()
    else:
        f = logging.Formatter("%(levelname)s: %(message)s")
    h.setFormatter(f)

    logger = logging.getLogger(__name__.split(".", 1)[0])
    logger.addHandler(h)
    logger.setLevel(level)

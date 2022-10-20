import logging


def initialize_logging() -> None:
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(format=fmt, level=logging.NOTSET)


initialize_logging()

import logging


formatter_develop = ("%(asctime)s - [%(levelname)s] - %(name)s - "
                     "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
formatter = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
formatter_aircraft = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"


def get_develop_handler():
    file_handler = logging.FileHandler("log/develop.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(formatter_develop))
    return file_handler


def get_warning_handler():
    file_handler = logging.FileHandler("log/important_develop.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(formatter_develop))
    return file_handler


def get_info_handler():
    file_handler = logging.FileHandler("log/main.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(formatter))
    return file_handler


def get_aircraft_handler():
    file_handler = logging.FileHandler("log/aircrafts.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(formatter_aircraft))
    return file_handler


def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_warning_handler())
    logger.addHandler(get_develop_handler())
    logger.addHandler(get_info_handler())
    return logger


def get_aircraft_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_aircraft_handler())
    return logger

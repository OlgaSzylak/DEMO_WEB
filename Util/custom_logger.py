import inspect
import logging


def custom_logger(logLevel=logging.DEBUG):

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s [%(filename)s:%(lineno)s] [%(levelname)s] %(funcName)2s: %(message)s",
                                  datefmt='%d/%m/%Y %I:%M:%S %p')

    file_handler = logging.FileHandler('test_execution.log')
    file_handler.setLevel(logLevel)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

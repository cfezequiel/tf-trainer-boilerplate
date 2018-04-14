import logging


DEBUG = logging.DEBUG


def set_log_level(logger, level_str):
    level = logging.getLevelName(level_str)
    logger.setLevel(level)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger



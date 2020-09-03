import logging
import os
from logging import Logger, StreamHandler
from logging.handlers import TimedRotatingFileHandler
# Logger 日志记录器 Handler 日志处理器
from configuration import config_obj

log_level = config_obj.get('logging', 'level') if config_obj.get('logging', 'level') else 'info'


def init_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    screen_handler = StreamHandler()
    datefmt = "%Y-%m-%d %H:%M:%S"
    format_str = "[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s"
    formatter = logging.Formatter(format_str, datefmt)
    screen_handler.setFormatter(formatter)
    screen_handler.setLevel(logging.DEBUG)
    logger.addHandler(screen_handler)

    log = logging.getLogger(logger_name)

    return log


log_name = config_obj.get('logging', 'level') if config_obj.get('logging', 'level') else "default"
logger = init_logger(log_name)
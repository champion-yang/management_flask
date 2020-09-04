import logging
import os
from logging import Logger, StreamHandler
from logging.handlers import TimedRotatingFileHandler
# Logger 日志记录器 Handler 日志处理器
from configuration import config_obj

log_level = config_obj.get('logging', 'level') if config_obj.get('logging', 'level') else 'info'


def init_logger(logger_name):
    if not os.path.exists("logs"):
        os.mkdir("logs")
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # handler all
    screen_handler = StreamHandler()
    handler = TimedRotatingFileHandler('./logs/{}_all.logs'.format(logger_name), when='midnight', backupCount=7)
    datefmt = "%Y-%m-%d %H:%M:%S"
    format_str = "[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s"
    formatter = logging.Formatter(format_str, datefmt)
    screen_handler.setFormatter(formatter)
    screen_handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    handler.setLevel(eval("logging.{}".format(log_level.upper())))
    logger.addHandler(screen_handler)
    logger.addHandler(handler)

    # handler error
    handler = TimedRotatingFileHandler('./logs/{}_error.logs'.format(logger_name), when='midnight', backupCount=7)
    datefmt = "%Y-%m-%d %H:%M:%S"
    format_str = "[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s"
    formatter = logging.Formatter(format_str, datefmt)
    handler.setFormatter(formatter)
    handler.setLevel(logging.ERROR)
    logger.addHandler(handler)

    log = logging.getLogger(logger_name)

    return log


log_name = config_obj.get('logging', 'level') if config_obj.get('logging', 'level') else "default"
logger = init_logger(log_name)
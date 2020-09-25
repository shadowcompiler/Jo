# coding:utf-8
import logging


def log():
    """
    log generator : For know when and why things don't work
    """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

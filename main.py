# coding:utf-8

# import

from telegram.ext import (Updater, CommandHandler)
from utils.token import key
import logging

# import

updater = Updater(token=key, use_context=True)  # updater init
dispatcher = updater.dispatcher

"""
log generator : For know when and why things don't work
"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


"""
Jo functions
"""



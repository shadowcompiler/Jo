# coding:utf-8

# import

from telegram.ext import (Updater, CommandHandler)
from utils.token import key
from utils.start import message
import logging

# import

updater = Updater(token=key, use_context=True)  # updater init
dispatcher = updater.dispatcher

"""
log generator : For know when and why things don't work
"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
Jo functions
"""


def start(update, context):
    """
    start reply process
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=message.format(update.effective_user.first_name))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# END


def start(update, context):
    """
    start reply process
    """


# Bot start
updater.start_polling()

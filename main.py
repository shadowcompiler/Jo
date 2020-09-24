# coding:utf-8

# import
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler)
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from utils.start import message
from utils.story import story_text
from utils.telme import telme_text
from utils.sum import sum_text
import logging
from utils.token import key

# import

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Jo functions


def start(update, context):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [[InlineKeyboardButton('Résumé du jour', callback_data='1'),
                 InlineKeyboardButton('Histoire du jour', callback_data='2')],

                [InlineKeyboardButton('Bouquinez', url='https://bouquinez.com'),
                 InlineKeyboardButton('Dis moi Jo...', callback_data='3')],
                [InlineKeyboardButton('Raccourcis bouquinez', callback_data='4')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(message.format(update.effective_chat.first_name), reply_markup=reply_markup)


def menu(update, context):
    keyboard = [[InlineKeyboardButton('Résumé du jour', callback_data='1'),
                 InlineKeyboardButton('Histoire du jour', callback_data='2')],

                [InlineKeyboardButton('Bouquinez', url='https://bouquinez.com'),
                 InlineKeyboardButton('Dis moi Jo...', callback_data='3')],
                [InlineKeyboardButton('Raccourcis bouquinez', callback_data='4')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text="Utilisez la command /jo pour obtenir de l'aide", reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    query.answer()
    if query.data == '1':
        keyboard = [[InlineKeyboardButton('Commenter', url='fcd.com'), InlineKeyboardButton('Acheter', url='fhejdk.com')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=sum_text, reply_markup=reply_markup)

    elif query.data == '2':
        keyboard = [[InlineKeyboardButton('Commenter', url='fcd.com')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text=story_text, reply_markup=reply_markup)

    elif query.data == '3':
        query.edit_message_text(text=telme_text)

    else:
        keyboard = [
            [InlineKeyboardButton('Fournitures', url='https://bouquinez.com/connect'), InlineKeyboardButton('Livres', url='https://bouquinez.com/livre')],
            [InlineKeyboardButton('vendre mes livre', url='https://bouquinez.com/lecture/adminlecture'), InlineKeyboardButton('Prêt de livre', url='https://bouquinez.com/lecture/ABONNEMENT.pdf')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Bouquinez.com', reply_markup=reply_markup)
# query.edit_message_text(text="Selected option: {}".format(query.data))


def main():
    updater = Updater(token=key, use_context=True)  # updater init
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('menu', menu))
    dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()

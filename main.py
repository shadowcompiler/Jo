# coding:utf-8

# import
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler)
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from utils.start import message
from utils.log import log
from utils.token import key

# import

log()

# Jo functions


def start(update, context):
    keyboard = [[InlineKeyboardButton('Résumé du jour', callback_data='1'),
                 InlineKeyboardButton('Histoire du jour', callback_data='2')],

                [InlineKeyboardButton('Bouquinez', url='https://bouquinez.com'),
                 InlineKeyboardButton('Découvrir...', callback_data='3')],
                [InlineKeyboardButton('Aide', callback_data='4')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(message.format(update.effective_chat.first_name), reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    query.answer()
    if query.data == '1':

        query.edit_message_text(text="Selected option: {}".format(query.data))


def main():
    updater = Updater(token=key, use_context=True)  # updater init
    dispatcher = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()


main()

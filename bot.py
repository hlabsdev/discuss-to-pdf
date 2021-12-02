#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


PORT = int(os.environ.get('PORT', '8443'))
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    welcom_text = """
    Welcom to DiscussToPDF.

    The availables commands are :
    - /help pour obtenir l'adresse du site
    - /select_chat: For converting your chat into PDF
    - /select_group For converting your group discussion into PDF
    """
    update.message.reply_text(welcom_text)
    # update.message.reply_text('Hello to use this, you should choose the chat to convert into pdf!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    Here is the main commands:
    
    /select_chat: Select the chat which's discussion will be converted into PDF, by sending the username of the other interlocutor. Exemple : if you want to turn your discussion with your friend John Doe, just send his username @jonhdoe.
    
    /select_group: Select the group which's discussion will be converted into PDF, by sending the group's link. Exemple : t.me/my_awesome_group
    """)


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

# Gestion des messqge inatendus ou incorrect
def mishandle(update, context):
    message = 'Je n\'ai pas compris votre message "{0}"'.format(update.message.text)
    update.message.reply_text(message)


# Commande de selection de chat
def select_chat(update, context):
    # message = "Select the chat which's discussion will be converted into PDF, by sending the username of the other interlocutor. Exemple : if you want to turn your discussion with your friend John Doe, just send his username @jonhdoe."
    # update.message.reply_text(message)    
    text = "Select the chat which's discussion will be converted into PDF, by sending the username of the other interlocutor. Exemple : if you want to turn your discussion with your friend John Doe, just send his username @jonhdoe."
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    

# Commande de selection de chat
def select_group(update, context):
    # message = "Select the group which's discussion will be converted into PDF, by sending the group's link. Exemple : t.me/my_awesome_group"
    # update.message.reply_text(message)    
    text = "Select the group which's discussion will be converted into PDF, by sending the group's link. Exemple : t.me/my_awesome_group"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# Inline response to chats
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
    

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

discussToPDFToken="796973086:AAFjQ7RCcox0T7CTZzdJDiGRp60oQqvh9uk"
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # updater = Updater("TOKEN", use_context=True)
    updater = Updater(discussToPDFToken, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("select_chat", select_chat))
    dp.add_handler(CommandHandler("select_group", select_group))
    inline_caps_handler = InlineQueryHandler(inline_caps)
    dp.add_handler(inline_caps_handler)

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
        
    # ====== This is for using webhook ====== #

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=discussToPDFToken)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + discussToPDFToken)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


    # ====== This is for using polling ====== #
    # # Start the Bot
    # updater.start_polling()

    # # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # # SIGTERM or SIGABRT. This should be used most of the time, since
    # # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.idle()


if __name__ == '__main__':
    main()

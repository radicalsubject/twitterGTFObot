from telegram import (Update, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (CallbackContext, ConversationHandler)
import logging

# # Define a few command handlers. These usually take the two arguments update and
# # context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    user_info = update.message.from_user
    chat_id = update.message.chat.id
    logging.info("Test log! user data read successfully.")
    update.message.reply_text(
"""Привет, {}! 👩🏻‍💻 """.format(user_info.first_name))

    context.chat_data.clear()
    user_data = context.user_data
    user_data.clear()
    return -1

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
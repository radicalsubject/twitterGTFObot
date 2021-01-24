from telegram import (Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (CallbackContext, ConversationHandler)
import os, logging
from modules import pytesseractModule
from token_extractor import token

bot = Bot(token)

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

def test(update, context):
    text = pytesseractModule.read_image()
    update.message.reply_text(f'{text}')

def image_handler(update: Update, context: CallbackContext):
    file_id = update.message.photo[-1].file_id
    file = bot.getFile(file_id)
    path = os.getcwd() + "/tmp/" + file_id + ".jpg"
    file.download(path)
    text = pytesseractModule.read_image(path)
    blacklist = ["bitcoin"]
    ANY([(word in text.lower()) for word in blacklist])
    update.message.reply_text(f'{text}')

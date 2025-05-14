from telegram import Update
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام زلمی جان! من بات تو هستم. چطور می‌تونم کمک‌ات کنم؟")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("برای استفاده از این بات، فقط پیام بفرست تا جواب بدم!")

def echo_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f"تو گفتی: {text}")

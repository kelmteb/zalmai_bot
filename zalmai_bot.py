import logging
from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

# تنظیم لاگ‌گیری
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور /start
def start(update, context):
    update.message.reply_text("سلام! من زلمی‌بات هستم.")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
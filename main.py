from telegram.ext import Updater, CommandHandler

# این تابع زمانی اجرا می‌شود که کاربر /start را بفرستد
def start(update, context):
    update.message.reply_text("سلام! من یک بات ساده هستم. چطور می‌تونم کمکت کنم؟ 😊")

def main():
    # توکن بات خود را این‌جا جایگزین کن
    updater = Updater("7904721098:AAGa_sJDhDg7oC4kxeSMstlj1Am4B2bqOKE", use_context=True)

    # گرفتن dispatcher برای ثبت فرمان‌ها
    dp = updater.dispatcher

    # وقتی کاربر /start می‌فرستد، تابع start اجرا می‌شود
    dp.add_handler(CommandHandler("start", start))

    # اجرای بات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


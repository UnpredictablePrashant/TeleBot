from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hello!')


def help(bot, update):
    update.message.reply_text('Welcome to Help menu!\n Please type /download to download mp3')


def echo(bot, update):
    update.message.reply_text(update.message.text)

def download(bot, update):
    update.message.reply_text("First Tell me your name? \n")
    dp.add_handler(MessageHandler(Filters.text, echo))
    if name=='prashant':
        update.message.reply_text("Welcome Prashant!")
    else:
        update.message.reply_text("Sorry you are not allowed to enter here.")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("download", download))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

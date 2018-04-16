from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import MessageEntity
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
NAME, INTERMEDIATE, DOWNLOAD = range(3)

def start(bot, update):
    update.message.reply_text('Hello!')
    return NAME

def name(bot, update):
    update.message.reply_text('Can you tell me your name?', reply_markup=ReplyKeyboardRemove())
    return INTERMEDIATE

def intermediate(bot, update):
    user = update.message.from_user
    print '[Intermediate] ',user
    name_n = update.message.text
    print name_n
    update.message.reply_text("Okay "+ name_n+"! Now you can send me the name of the song which you want me to download")
    return DOWNLOAD


def download(bot, update):
    url_d = update.message.text
    user = update.message.from_user
    print '[Download] ',user
    print '\n [URL] ',url_d
    os.system('wget '+url_d)
    update.message.reply_text('Good you are in downloads')
    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    print '[Cancel] ',user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            NAME: [MessageHandler(Filters.text, name)],
	    INTERMEDIATE : [MessageHandler(Filters.text, intermediate)],
            DOWNLOAD: [MessageHandler(Filters.entity(MessageEntity.URL), download)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

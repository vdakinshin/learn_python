import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def show_error(bot, update, error):
    print(error)

def main():
    updater = Updater("394233160:AAEB72rYjqQPmd54FXrjlhO3rr_LxVsQVrU")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()
main()




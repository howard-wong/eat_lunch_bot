from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re




def start(bot, update):
    print("New comer")
    print(update)
    print(bot)    
    update.message.reply_text("Hello, I am Eat Lunch Bot, what can I help you?")
   
def hello(bot, update):
	
    '''
    
    url = get_url()
    chat_id = update.message.chat_id
    print(update)
    print(bot)
    bot.send_photo(chat_id=chat_id, photo=url)
    '''
	
    print("hihi")
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
    
    
def main():
    updater = Updater('key')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('hello', hello))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    print("Eat Lunch Bot Start")
    main()
    
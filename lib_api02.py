import time

import telebot

TOKEN = '5629751285:AAG5C2UGTV4-U85lu1n5aihkLOp8P0ieU2I'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.reply_to(message, f'{i+1}')



@bot.message_handler(content_types='text')
def reverse_text(message):
    text = message.text[::-1]
    bot.reply_to(message, text)



bot.infinity_polling()

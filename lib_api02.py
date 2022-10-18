import time
import os
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
        bot.send_message(message.chat.id, f'{i+1}')


@bot.message_handler(commands=['say'])
def say(message):
    print(message.text.split(' ')[1:])
    print(message.text.split(' '))
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message,  f'***{text.upper()}!***')


@bot.message_handler(commands=['admin'], func=lambda message: message.from_user.username == 'Ampilog')
def admin(message):
    print(message)
    info = os.name
    bot.reply_to(message, info)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAACAgIAAxkBAAMnY05r3P3lhZlLIdt3_OqYfRy6GAgAAjcBAAL3AsgP0V5S9kOQB0QqBA'
    bot.send_sticker(message.chat.id, FILE_ID)


@bot.message_handler(content_types='text')
def reverse_text(message):
    text = message.text[::-1]
    bot.reply_to(message, text)



bot.infinity_polling()

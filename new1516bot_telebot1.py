import telebot
from telebot_parser import parce

TOKEN = '5629751285:AAG5C2UGTV4-U85lu1n5aihkLOp8P0ieU2I'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['map'])
def map_site(message):
    chat_id = message.chat.id
    q = parce()
    for key in q:
        bot.send_message(chat_id, f'{key} - {q[key]}')

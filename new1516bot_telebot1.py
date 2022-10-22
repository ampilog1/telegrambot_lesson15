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


@bot.message_handler(commands=['say'])
def say(message):
    print(message.text.split(' ')[1:])
    print(message.text.split(' '))
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')


@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, f'{i + 1}')


bot.infinity_polling()

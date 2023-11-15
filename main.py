import telebot
from telebot import types
from datetime import date
today = date.today()
now = datetime.now()

tokenfile = open("token.txt", "r")
token = tokenfile.read()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data = dt_string.split(' ')[0]
    time = dt_string.split(' ')[1]
    if time.split(':')[0] < 11:
        var_time = "Доброе утро,"
    elif time.split(':')[1] >= 11 and time.split(':')[1] < 18:
        var_time = "Добрый день,"
    else:
        var_time = "Добрый вечер,"
    username = message.from_user.username
    varres = var_time + " " + username + "." + " Текущие дата и время -" + dt_string + ".\nВведите номер вашей группы, пожалуйста."
    bot.send_message(message.from_user.id, varres)
bot.infinity_polling()
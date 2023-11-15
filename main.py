import telebot
from telebot import types
from datetime import date
from datetime import datetime
import pickle
today = date.today()
now = datetime.now()

tokenfile = open("token.txt", "r")
token = tokenfile.read()

with open("users.txt", "rb") as file:
    groupsuperlist = pickle.load(file)
with open("groups.txt", "rb") as file:
    schedulesuperlist = pickle.load(file)


def check_if_registered(user_id): # Если пользователя нет, возвращает False, если есть - возвращает группу
    global groupsuperlist
    for i in groupsuperlist:
        if i[0] == user_id:
            return i[1]
        else:
            return False
        


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])


def get_text_messages(message):
    global schedulesuperlist
    if message.text == '/start':
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data = dt_string.split(' ')[0]
        time = dt_string.split(' ')[1]
        if int(time.split(':')[0]) < 11:
            var_time = "Доброе утро,"
        elif int(time.split(':')[1]) >= 11 and int(time.split(':')[1])< 18:
            var_time = "Добрый день,"
        else:
            var_time = "Добрый вечер,"
        username = message.from_user.username
        varres = var_time + " " + username + "." + " Текущие дата и время -" + dt_string + ".\n"
        start_var1 = check_if_registered()
        bot.send_message(message.from_user.id, varres)
    elif message.text == "abcd":
        bot.send_message(message.from_user.id, "ABCD ABCD")
    elif message.text == "test2":
        bot.send_message(message.from_user.id, schedulesuperlist[0][1])
    elif message.test == "chkid":
        bot.send_message(message.from_user.id,message.from_user.id)
bot.infinity_polling()

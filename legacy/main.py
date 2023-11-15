import telebot
import sys
from telebot import types
from datetime import date
from datetime import datetime
import pickle
import subprocess
today = date.today()
now = datetime.now()

a = 0

tokenfile = open("token.txt", "r")
token = tokenfile.read()

with open("users.txt", "rb") as file:
    groupsuperlist = pickle.load(file)
with open("groups.txt", "rb") as file:
    schedulesuperlist = pickle.load(file)


def check_if_registered(user_id): # Если пользователя нет, возвращает False, если есть - возвращает группу
    global groupsuperlist
    for i in groupsuperlist:
        if int(i[0]) == int(user_id):
            return i[1]
        else:
            pass
    return False


def print_schedule(group): # Печатает расписание для группы, если она существует
    global schedulesuperlist
    for i in schedulesuperlist:
        if group == i[0]:
            return i
            break
        else:
            pass
    return False


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])


def get_text_messages(message):
    global schedulesuperlist
    global groupsuperlist
    global a
    ps2 = False
    ps3 = False
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
        start_var1 = check_if_registered(message.from_user.id)
        if start_var1 is False:
            varres += "Вы не зарегистрированы в боте. Введите номер группы, расписание которой хотите узнать."
            bot.send_message(message.from_user.id, varres)
        else:
            if print_schedule(start_var1) is not False:
                varres += "Ваша группа - "
                varres += str(print_schedule(start_var1)[0])
                varres += ". Вывожу расписание."
                bot.send_message(message.from_user.id, varres)
                bot.send_message(message.from_user.id, print_schedule(start_var1)[1])
            else:
                varres += "Ваша группа - "
                varres += str(start_var1)
                varres += str(".")
                bot.send_message(message.from_user.id, varres)
                bot.send_message(message.from_user.id,"Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        a = 1
    elif message.text == "chkid":
        bot.send_message(message.from_user.id,message.from_user.id)
        a = 1
    elif "-" in message.text:
        rpd = print_schedule(message.text)
        if rpd is False:
            bot.send_message(message.from_user.id,"Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        else:
            bot.send_message(message.from_user.id, print_schedule(message.text)[1])
            start_var1 = check_if_registered(message.from_user.id)
            if start_var1 is not False:
                bot.send_message(message.from_user.id, 'Хотите изменить свою группу? Напишите "Да", если это нужно.')
                ps2 = True
                pv1 = message.text
            else:
                ps3 = True
                print('d')
                pv1 = message.text
                bot.send_message(message.from_user.id, 'Вы не зарегистрированы. Если вы хотите зарегистрироваться (и сделать эту группу своей основной), напишите "Да".')
        a = 1
    elif ps2 is True:
        if message.text == "Да":
            for i in groupsuperlist:
                if message.from_user.id == i[0]:
                    i[1] = pv1
                else:
                    pass
        else:
            pass
        ps2 = False
        a = 1
    elif ps3 is True:
        if message.text == "Да":
            newlst = []
            newlst.append(message.from_user.id)
            newlst.append(pv1)
            groupsuperlist.append(newlst)
            print(groupsuperlist)
            bot.send_message(message.from_user.id, pv1)
            with open("users.txt", "wb") as file1:
                pickle.dump(groupsuperlist, file1)
        else:
            print('abc')
            pass
        ps3 = False
        a = 1
    elif message.text == '/stop':
        bot.stop_polling()

bot.infinity_polling()

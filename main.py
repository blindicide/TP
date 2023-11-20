import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
import pickle
import subprocess
now = datetime.now()
ps2 = False
ps3 = False
pv1 = ''



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

# Объект бота
bot = Bot(token="6340336033:AAG-qE0lUnMKQRzYC_cOcrjsRK9arFhG2UI")
# Диспетчер
dp = Dispatcher()

@dp.message(F.text)
async def mainfunc(message: Message):
    global schedulesuperlist, groupsuperlist
    global ps2, ps3, pv1
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
            await message.answer(varres)
        else:
            if print_schedule(start_var1) is not False:
                varres += "Ваша группа - "
                varres += str(print_schedule(start_var1)[0])
                varres += ". Вывожу расписание."
                await message.answer(varres)
                await message.answer(print_schedule(start_var1)[1])
            else:
                varres += "Ваша группа - "
                varres += str(start_var1)
                varres += str(".")
                await message.answer(varres)
                await message.answer("Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        a = 1
    elif message.text == "chkid":
        await message.answer(str(message.from_user.id))
        a = 1
    elif "-" in message.text:
        rpd = print_schedule(message.text)
        if rpd is False:
            await message.answer("Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        else:
            await message.answer(print_schedule(message.text)[1])
            start_var1 = check_if_registered(message.from_user.id)
            if start_var1 is not False:
                await message.answer('Хотите изменить свою группу? Напишите "Да", если это нужно.')
                ps2 = True
                pv1 = message.text
            else:
                ps3 = True
                print('d')
                pv1 = message.text
                await message.answer('Вы не зарегистрированы. Если вы хотите зарегистрироваться (и сделать эту группу своей основной), напишите "Да".')
        a = 1
    elif ps2 is True:
        if message.text == "Да":
            for i in groupsuperlist:
                if message.from_user.id == i[0]:
                    i[1] = pv1
                    msgs = "Вы успешно зарегистрировались, введя группу " + pv1 + ". Если вы хотите её изменить, введите номер желаемой группы."
                    await message.answer(msgs)
                    with open("users.txt", "wb") as file1:
                        pickle.dump(groupsuperlist, file1)
                else:
                    pass
        else:
            await message.answer("Ошибка. Код А-4: неправильный формат ввода. Пожалуйста, проверьте, в каком режиме вы находитесь.")
            pass
        ps2 = False
    elif ps3 is True:
        if message.text == "Да":
            print('vb')
            newlst = []
            newlst.append(message.from_user.id)
            newlst.append(pv1)
            groupsuperlist.append(newlst)
            print(groupsuperlist)
            await message.answer(pv1)
            with open("users.txt", "wb") as file1:
                pickle.dump(groupsuperlist, file1)
            msgs = "Вы успешно зарегистрировались, введя группу " + pv1 + ". Если вы хотите её изменить, введите номер желаемой группы."
            await message.answer(msgs)
        else:
            pass
        ps3 = False
    else:
        pass




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
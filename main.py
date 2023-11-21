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

ps2 = False
ps3 = False
ps4 = False
ps5 = False
ps6 = False
pv1 = ''


def gettime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    time = dt_string.split(' ')[1]
    return dt_string

with open("users.txt", "rb") as file:
    groupsuperlist = pickle.load(file)
with open("groups.txt", "rb") as file:
    schedulesuperlist = pickle.load(file)
with open("notes.txt", "rb") as file:
    notesuperlist = pickle.load(file)

def check_if_registered(user_id): # Если пользователя нет, возвращает False, если есть - возвращает группу
    user_id = int(user_id)
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
        else:
            pass
    return False

def check_notes(user_id): # Если пользователь зарегистрирован, но у него нет заметок, создаёт пустой список. Если есть, возвращает True.
    global notesuperlist
    user_id = int(user_id)
    mp = 0
    if check_if_registered(user_id) is not False:
        epd = False
        for i in notesuperlist:
            if i[0] == user_id:
                print("abc")
                mp = 3
            else:
                pass
        if mp == 3:
            return True
        else:
            print("ABC")
            adsp = [user_id]
            notesuperlist.append(adsp)
            with open("notes.txt", "wb") as file:
                pickle.dump(notesuperlist, file)
            return 1
    else:
        return False
    
def print_notes(user_id): # Если записок нет, то выводит False, если есть - выдаёт список для печати.
    global notesuperlist
    user_id = int(user_id)
    outlist = []
    for i in notesuperlist:
        if i[0] == user_id:
            if len(i) < 2:
                return False
            else:
                for u in range(len(i)):
                    if u != 0:
                        outlist.append(i[u])
                    else:
                        pass
                return outlist
        else:
            pass

# Объект бота
bot = Bot(token="6340336033:AAG-qE0lUnMKQRzYC_cOcrjsRK9arFhG2UI")
# Диспетчер
dp = Dispatcher()

@dp.message(F.text)
async def mainfunc(message: Message):
    global schedulesuperlist, groupsuperlist, nptesuperlist
    global ps2, ps3, ps4, ps5, ps6, pv1
    if message.text == '/start':
        dt_string = gettime()
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
    elif message.text == "/notes":
        if check_if_registered(message.from_user.id) is not False:
            await message.answer(
"""Вы получили доступ к своим заметкам. Команды:
1 - Просмотреть заметки
2 - Добавить новую заметку
3 - Удалить все заметки"""
                                 )
            ps4 = True
        elif check_notes(message.from_user.id) is False:
            await message.answer("Зарегистрируйтесь, пожалуйста.")
    elif ps4 is True:
        if message.text == "1":
            if check_notes(message.from_user.id) == 1 and check_notes(message.from_user.id) is not True:
                await message.answer("У вас пока не было созданных заметок. Теперь вы можете их создавать!")
            elif check_notes(message.from_user.id) is True:
                if print_notes(message.from_user.id) is not False:
                    psv = print_notes(message.from_user.id)
                    print(psv)
                    outline = ""
                    for i in range(0, len(psv)):
                        if i % 2 == 0:
                            outline += psv[i]
                        else:
                            outline += '\nДата создания заметки: '
                            outline += psv[i]
                            await message.answer(outline)
                            outline = ''
            else:
                await message.answer("У вас нет заметок.")
            await message.answer("Вызовите команду /notes ещё раз для дополнительных действий с заметками.")
        elif message.text == "2":
            await message.answer("Пожалуйста, напечатайте свою заметку следующим сообщением.")
            ps5 = True
        elif message.text == "3":
            await message.answer("Вы уверены? Если да, напишите 'УДАЛИТЬ' (без кавычек) следующим сообщением.")
            ps6 = True
        else:
            await message.answer("Ошибка: команда не распознана. Вызовите /notes ещё раз.")
        ps4 = False
    elif ps5 is True:
        temp1 = gettime()
        evg = message.text
        for i in notesuperlist:
            if message.from_user.id == i[0]:
                i.append(evg)
                i.append(gettime())
            else:
                pass
        with open("notes.txt", "wb") as file1:
            pickle.dump(notesuperlist, file1)
        ps5 = False
        outtxt = "Заметка добавлена. Время:" + gettime()
        await message.answer(outtxt)
    elif ps6 is True and message.text == "УДАЛИТЬ":
        for i in notesuperlist:
            if message.from_user.id == i[0]:
                for u in range(len(i)):
                    if u != 0:
                        i.pop(u)
                    else:
                        pass
            else:
                pass
        ps6 = False
    else:
        pass




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
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

temp_changegroup = False
temp_register = False
temp_notecommand = False
temp_addnote = False
temp_deletenote = False
temp_groupnumber = ''
## Переменные для переключения между "режимами"


def gettime(): # Получает текущее время
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    time = dt_string.split(' ')[1]
    return dt_string

with open("users.b", "rb") as file:
    groupsuperlist = pickle.load(file)
with open("groups.b", "rb") as file:
    schedulesuperlist = pickle.load(file)
with open("notes.b", "rb") as file:
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
                mp = 3
            else:
                pass
        if mp == 3:
            return True
        else:
            adsp = [user_id]
            notesuperlist.append(adsp)
            with open("notes.b", "wb") as file:
                pickle.dump(notesuperlist, file)
            return 1
    else:
        return False
    
def print_notes(user_id): # Если заметок нет, то выводит False, если есть - выдаёт список для печати.
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
    global temp_changegroup, temp_register, temp_notecommand, temp_addnote, temp_deletenote, temp_groupnumber
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
        start_text = var_time + " " + username + "." + " Текущие дата и время -" + dt_string + ".\n"
        start_var1 = check_if_registered(message.from_user.id)
        if start_var1 is False:
            start_text += "Вы не зарегистрированы в боте. Введите номер группы, расписание которой хотите узнать."
            await message.answer(start_text)
        else:
            if print_schedule(start_var1) is not False:
                start_text += "Ваша группа - "
                start_text += str(print_schedule(start_var1)[0])
                start_text += ". Вывожу расписание."
                await message.answer(start_text)
                await message.answer(print_schedule(start_var1)[1])
            else:
                start_text += "Ваша группа - "
                start_text += str(start_var1)
                start_text += str(".")
                await message.answer(start_text)
                await message.answer("Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        a = 1
    elif message.text == "chkid":
        await message.answer(str(message.from_user.id))
        a = 1
    elif "-" in message.text:
        checkgroup1 = print_schedule(message.text)
        if checkgroup1 is False:
            await message.answer("Ошибка. Код А-1: несуществующая группа. Пожалуйста, повторите ввод или введите другую группу для регистрации. Для вашего удобства выводим список всех групп по курсам.")
        else:
            await message.answer(print_schedule(message.text)[1])
            start_var1 = check_if_registered(message.from_user.id)
            if start_var1 is not False:
                await message.answer('Хотите изменить свою группу? Напишите "Да", если это нужно. Если вы напишете другое сообщение, регистрация будет сброшена.')
                temp_changegroup = True
                temp_groupnumber = message.text
            else:
                temp_register = True
                temp_groupnumber = message.text
                await message.answer(
                    """Если вы зарегистрируетесь в боте, то ваша группа будет сохранена в нашей базе данных (вы можете поменять её в любой момент).
                    Вы также сможете создавать заметки прямо в боте. Нажмите кнопку или введите сообщение «Да», чтобы зарегистрироваться."""
                )
        a = 1
    elif temp_changegroup is True:
        if message.text == "Да":
            for i in groupsuperlist:
                if message.from_user.id == i[0]:
                    i[1] = temp_groupnumber
                    msgs = "Вы успешно зарегистрировались, введя группу " + temp_groupnumber + ". Если вы хотите её изменить, введите номер желаемой группы."
                    pass
        else:
            pass
        temp_changegroup = False
    elif temp_register is True:
        if message.text == "Да":
            newlist = []
            newlist.append(message.from_user.id)
            newlist.append(temp_groupnumber)
            groupsuperlist.append(newlist)
            print(groupsuperlist)
            await message.answer(temp_groupnumber)
            with open("users.b", "wb") as file1:
                pickle.dump(groupsuperlist, file1)
            msgs = "Вы успешно зарегистрировались, введя группу " + temp_groupnumber + ". Если вы хотите её изменить, введите номер желаемой группы."
            await message.answer(msgs)
        else:
            pass
        temp_register = False
    elif message.text == "/notes":
        if check_if_registered(message.from_user.id) is not False:
            await message.answer(
"""Вы получили доступ к своим заметкам. Команды:
1 - Просмотреть заметки
2 - Добавить новую заметку
3 - Удалить все заметки"""
                                 )
            temp_notecommand = True
        elif check_notes(message.from_user.id) is False:
            await message.answer("Зарегистрируйтесь, пожалуйста.")
    elif temp_notecommand is True:
        if message.text == "1":
            if check_notes(message.from_user.id) == 1 and check_notes(message.from_user.id) is not True:
                await message.answer("У вас пока не было созданных заметок. Теперь вы можете их создавать!")
            elif check_notes(message.from_user.id) is True:
                if print_notes(message.from_user.id) is not False:
                    notelist = print_notes(message.from_user.id)
                    outline = ""
                    for i in range(0, len(notelist)):
                        if i % 2 == 0:
                            outline += notelist[i]
                        else:
                            outline += '\nДата создания заметки: '
                            outline += notelist[i]
                            await message.answer(outline)
                            outline = ''
                else:
                    await message.answer("У вас нет заметок.")
            await message.answer("Вызовите команду /notes ещё раз для дополнительных действий с заметками.")
        elif message.text == "2":
            await message.answer("Пожалуйста, напечатайте свою заметку следующим сообщением.\nПримечание: заметки исключительно из чисел в настоящий момент не поддерживаются.")
            temp_addnote = True
        elif message.text == "3":
            await message.answer("Вы уверены? Если да, напишите 'УДАЛИТЬ' (без кавычек) следующим сообщением.")
            temp_deletenote = True
        else:
            await message.answer("Ошибка: команда не распознана. Вызовите /notes ещё раз.")
        temp_notecommand = False
    elif temp_addnote is True:
        newnote_text = message.text
        for i in notesuperlist:
            if message.from_user.id == i[0]:
                i.append(newnote_text)
                i.append(gettime())
            else:
                pass
        with open("notes.b", "wb") as file1:
            pickle.dump(notesuperlist, file1)
        temp_addnote = False
        outtxt = "Заметка добавлена. Время: " + gettime()
        await message.answer(outtxt)
    elif temp_deletenote is True and message.text == "УДАЛИТЬ":
        for i in notesuperlist:
            if message.from_user.id == i[0]:
                i.clear()
                i.append(message.from_user.id)
                await message.answer("Заметки успешно удалены.")
            else:
                pass
        with open("notes.b", "wb") as file1:
            pickle.dump(notesuperlist, file1)
        temp_deletenote = False
    elif message.text == "/help":
        help_message = """Информационное сообщение
            Команды:
            /start - вывести стартовое сообщение
            (номер группы) - вывести расписание группы
            /notes - вывести меню заметок (если вы зарегистрированы)
            /help - вывести это сообщение
            Текущее время: """
        help_message += gettime()
        help_message += """Бот разработан Якуниным Р. и Филатовым А. в 2023 г. в рамках проекта по предмету 'Технологии программирования'
        По всем вопросам обращайтесь на почту y1rs.yrs@gmail.com с пометкой 'БОТ'."""
        await message.answer(help_message)
    else:
        await message.answer("Ошибка. Код А-4: неправильный формат ввода. Пожалуйста, проверьте, в каком режиме вы находитесь. Вызовите /help или /start.")




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
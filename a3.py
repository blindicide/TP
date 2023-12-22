abcd = """Нечётная неделя:
-------------
Понедельник:
9:40-11:10 - Языки программирования, лекция
13:00-14:30 - Физкультура
Вторник:
11:20-12:50 - Мат. анализ, лекция
Среда:
8:00-9:30 - Физика, практика
9:40-11:10 - Физика, лекция
11:20-12:50 - Мат. анализ, практика
13:00-14:30 - Физика, лабораторная работа
Четверг:
13:00 - Физкультура
Пятница:
8:00-11:10 - Т.П., лабораторная работа
11:20-12:50 - Информатика, лекция
14:40-17:50 - Информатика, лабораторная работа
-------------
Чётная неделя:
-------------
Понедельник:
13:00-14:30 - Физкультура
Вторник:
8:00-9:30 - А. и Г., лекция
9:40-11:10 - А. и Г., практика
11:20-12:50 - Мат. анализ, лекция
13:00-14:30 - Англ. яз.
Среда:
8:00-9:30 - Физика, практика
9:40-11:10 - Физика, лекция
11:20-12:50 - Мат. анализ, практика
Четверг:
13:00 - Физкультура
Пятница:
11:20-12:50 - Т.П., лекция
14:40-17:50 - Я.П., лабораторная работа"""
abdv = """Нечётная неделя:
-------------
Понедельник:
9:40-11:10 - Языки программирования, лекция
13:00-14:30 - Физкультура
Вторник:
8:00-9:30 - А. и Г., лекция
9:40-11:10 - А. и Г., практика
11:20-12:50 - Мат. анализ, лекция
13:00-14:30 - Англ. яз.
Среда:
8:00-9:30 - Физика, практика
9:40-11:10 - Физика, лекция
11:20-12:50 - Мат. анализ, практика
13:00-14:30 - Физика, лабораторная работа
Четверг:
13:00 - Физкультура
Пятница:
11:20-12:50 - Т.П., лекция
14:40-17:50 - Я.П., лабораторная работа
-------------
Чётная неделя:
-------------
Понедельник:
13:00-14:30 - Физкультура
Вторник:
11:20-12:50 - Мат. анализ, лекция
13:00-14:30 - Англ. яз.
Среда:
8:00-9:30 - Физика, практика
9:40-11:10 - Физика, лекция
11:20-12:50 - Мат. анализ, практика
Четверг:
13:00 - Физкультура
Пятница:
8:00-11:10 - Т.П., лабораторная работа
11:20-12:50 - Информатика, лекция
14:40-17:50 - Информатика, лабораторная работа
"""
import pickle

with open("groups.b", "rb") as file:
    schedulesuperlist = pickle.load(file)
# schedulesuperlist.append(['131-22', abcd])
schedulesuperlist.append(['131-21', abdv])
with open("groups.b", "wb") as file1:
    pickle.dump(schedulesuperlist, file1)
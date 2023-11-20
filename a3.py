abcd = """Нечётная неделя:
-------------
Понедельник:
8:00-9:30 - Математический анализ, аудитория 0001
9:40-11:10 - Алгебра, аудитория 0002"""
import pickle

with open("groups.txt", "rb") as file:
    schedulesuperlist = pickle.load(file)
schedulesuperlist.append(['1111-11', abcd])
with open("groups.txt", "wb") as file1:
    pickle.dump(schedulesuperlist, file1)
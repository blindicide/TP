import pickle
with open("users.txt", "rb") as file:
    groupsuperlist = pickle.load(file)
groupsuperlist.append([932305466, '55-55'])
with open("users.txt", "wb") as file:
    pickle.dump(groupsuperlist, file)
abcd = """Нечётная неделя:
-------------
Понедельник:
8:00-9:30 - Математический анализ, аудитория 0001
9:40-11:10 - Алгебра, аудитория 0002"""

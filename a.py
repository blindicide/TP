import pickle
groupsuperlist = []
gsl1 = [11111, 2222]
groupsuperlist.append(gsl1)
with open("users.b", "wb") as file:
    pickle.dump(groupsuperlist, file)
schedulesuperlist = []
sc1 = ['55-55']
## Вот так будет выглядеть расписание
abcd = """Нечётная неделя:
-------------
Понедельник:
8:00-9:30 - Математический анализ, аудитория 0001
9:40-11:10 - Алгебра, аудитория 002"""
sc1.append(abcd)
schedulesuperlist.append(sc1)
with open("groups.b", "wb") as file1:
    pickle.dump(schedulesuperlist, file1)

import pickle
groupsuperlist = []
gsl1 = ["TEST_USER", "TEST_GROUP"]
groupsuperlist.append(gsl1)
with open("users.txt", "wb") as file:
    pickle.dump(groupsuperlist, file)
schedulesuperlist = []
sc1 = ["TEST_GROUP"]
## Вот так будет выглядеть расписание
abcd = """Нечётная неделя:
-------------
Понедельник:
8:00-9:30 - Математический анализ, аудитория 0001
9:40-11:10 - Алгебра, аудитория 0002"""
sc1.append(abcd)
schedulesuperlist.append(sc1)
with open("groups.txt", "wb") as file1:
    pickle.dump(schedulesuperlist, file1)
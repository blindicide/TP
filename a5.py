import pickle
with open("notes.txt", "rb") as file:
    noteslist = pickle.load(file)
print(noteslist)
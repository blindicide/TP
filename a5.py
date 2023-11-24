import pickle
with open("notes.b", "rb") as file:
    noteslist = pickle.load(file)
print(noteslist)
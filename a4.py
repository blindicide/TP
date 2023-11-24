import pickle
nt1 = [1, '']
notesuperlist = [nt1]
with open("notes.b", "wb") as file:
    pickle.dump(notesuperlist, file)
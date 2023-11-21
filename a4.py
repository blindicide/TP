import pickle
nt1 = [1, '']
notesuperlist = [nt1]
with open("notes.txt", "wb") as file:
    pickle.dump(notesuperlist, file)
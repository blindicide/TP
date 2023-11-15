import pickle
with open("users.txt", "rb") as file:
    groupsuperlist = pickle.load(file)
groupsuperlist.append(['932305466', '5555'])
with open("users.txt", "wb") as file:
    pickle.dump(groupsuperlist, file)
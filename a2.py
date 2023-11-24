import pickle
with open("users.b", "rb") as file:
    groupsuperlist = pickle.load(file)
groupsuperlist.append([932305466, '55-55'])
with open("users.b", "wb") as file:
    pickle.dump(groupsuperlist, file)
import pickle

shoplist_file = 'shoplist.data'
shoplist = ('apple', 'orange', 'shit')

f = open(shoplist_file, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplist_file, 'rb')
storedlist = pickle.load(f)
print(storedlist)
f.close()

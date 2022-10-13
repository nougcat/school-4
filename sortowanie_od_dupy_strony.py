
alfabet = 'abcdefghijklmnoprstuwz'
slowa_jakies_dziwne = ['dupa', 'pies', 'bastion', 'slowo', 'labalbal']

pop_var = 0

for x in range(len(slowa_jakies_dziwne)):
    print(slowa_jakies_dziwne[x])
    if x == 3:
        slowa_jakies_dziwne.pop()
        x -= 1
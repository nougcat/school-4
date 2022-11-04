tekst = ' 6 1 2' #input('')

tekst = tekst.split()

r = int(tekst[0])   # distance between
k = int(tekst[1])   # size of K feet
a = int(tekst[2])   # size of A feet
i = 0
while r > 0:
    if i % 2==0:   # jeśli liczba parzysta to kazik się rusza
        r = r - k    # ruch kazika
    else:
        r = r - a   # ruch antka
    i += 1

if i%2 == 0:
    print(1)    # K wins
else:
    print(0)  # A wins


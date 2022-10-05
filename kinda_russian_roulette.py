n = 7   # ilosc  elemntów
k = 3   # co ile razy usuwać element

tab = [x+1 for x in range(n)]

czy_usunac = 0

while len(tab) > 1:
    for x in range(len(tab)- int(len(tab)/3)):
        pop_var = 0     # kiedy usuwamy liczbę z listy to ta lista skraca się o jeden. Po to jest ta lista
        print(x, czy_usunac)
        if czy_usunac == 2 and len(tab) > 1:
            print(tab, x - pop_var +1)
            tab.pop(x - pop_var)

            pop_var +=1

            czy_usunac = 1
        else:
            czy_usunac += 1

print(tab)

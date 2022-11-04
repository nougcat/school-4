def quicksort(tablica):
    if len(tablica) <= 1:
        return tablica

    pivot = int(tablica[-1])
    tablica.pop()

    smaller_items = []
    greater_items = []
    for x in tablica:
        if x < pivot:
            smaller_items.append(x)
        else:
            greater_items.append(x)
    return quicksort(greater_items) + [pivot] + quicksort(smaller_items)

a = input() # whatever
b = input()

b = b.split() # muszkieterzy
tablica = []
for x in b:
    tablica.append(int(x))


poczatek = 0
koniec = len(tablica) -1

sorted_stuff = quicksort(tablica)

for x in range(10):
    if len(sorted_stuff) >= x+1:
        print(sorted_stuff[x], end=' ')
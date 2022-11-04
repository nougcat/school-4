a = input()
a = a.split()

odp = 0
for x in range(int(a[0]), int(a[1])+1):
    if x % int(a[2]) == 0:
        odp +=1

print(odp)
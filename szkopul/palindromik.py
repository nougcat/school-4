slowo = input()

slowo = slowo.upper()

print(slowo)

palindrom = True

for x in range(len(slowo)):
    if slowo[x] != slowo[-x-1]:
        palindrom = False

odp = slowo

if not palindrom:
    for x in range(1, len(slowo)+1):
        odp += slowo[-x]

print(odp)
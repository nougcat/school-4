a = input()

tekst = input()

tekst_tab = tekst.split()

odp = 0
for x in tekst_tab:

    if x.isdigit():
        odp += int(x)

print(odp)
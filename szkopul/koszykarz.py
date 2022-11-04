tekst = input('')
tekst = tekst.split()

k = int(tekst[0]) # wzrost Kazia
w = int(tekst[1]) # wymagany wzrost
m = int(tekst[2]) # zmiana w wzroście

wynik = (w-k)/m

if wynik == int(wynik):
    print(int(wynik))
else:
    print(int(wynik)+1)
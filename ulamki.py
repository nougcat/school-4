wynik = '0.'

licznik = 5
mianownik = 8

while licznik > 0:
    licznik = licznik * 2
    print(wynik, licznik)

    if licznik >= mianownik:
        wynik += '1'
    else:
        wynik += '0'

    licznik = licznik % mianownik

print(wynik)
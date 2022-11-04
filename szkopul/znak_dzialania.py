tekst = input()
tekst =  tekst.split()

a =  int(tekst[0])
b =  int(tekst[1])

max = -99999999999999
if a + b > max:
    max = a+b
if a - b > max:
    max = a-b
if a * b > max:
    max = a*b


if a + b == max:
    print(f'{a}+{b}={a + b}')
if a - b == max:
    new_b = f'({b})'
    print(f'{a}-{new_b}={a - b}')
if a * b == max:
    print(f'{a}*{b}={a * b}')

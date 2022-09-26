def print_labirynt(labirynt):
    for x in range(len(labirynt[0])):
        if x < 10:
            print(f'0{x}', end=' ')
        else:
            print(f'{x}', end=' ')

    print(' ')
    for line in labirynt:
        for x in line:
            if x == 'X':  # printing only X (WALLS)
                print(x, end='  ')
            else:
                print(' ', end='  ')
        print(' ')


labirynt: list = []

with open('labirynt.txt') as f:
    for i, line in enumerate(f):
        labirynt.append([])
        for char in line:
            if char != '\n':
                labirynt[i].append(char)

print_labirynt(labirynt)

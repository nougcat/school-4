def labirynt_print(labirynt):
    print('XX', end=' ')
    for x in range(len(labirynt[0])):   # making upper column with numbers
        if x < 10:
            print(f'0{x}', end=' ')
        else:
            print(f'{x}', end=' ')

    print(' ')
    for i, line in enumerate(labirynt):
        if i < 10:
            print(f'0{i}', end=' ')
        else:
            print(f'{i}', end=' ')

        for x in line:
            if x == -1:  # printing only WALLS
                print(x, end=' ')
            else:
                print(' ', end='  ')
        print(' ')


labirynt: list = []

with open('labirynt.txt') as f:
    for i, line in enumerate(f):
        labirynt.append([])
        for char in line:
            if char != '\n':
                if char == 'X':
                    labirynt[i].append(-1)
                else:
                    labirynt[i].append(00)

labirynt_print(labirynt)

wybrany_punkt = []
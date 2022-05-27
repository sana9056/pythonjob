N = 5
i = 1


def titables():
    for j in range(1, 11):
        num = i * j
        print(i, 'x', j, '=', num)


while i <= N:
    titables()
    i = i + 1
    print('_____________________')

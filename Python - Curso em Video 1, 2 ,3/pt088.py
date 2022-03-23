print(f'\033[1;33m{" DESAFIO 86 ":#^25}\033[m\n')
matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite o número que deseja colocar na posição {[c, i]}: '))
        if c == 0:
            matriz[0].append(num)
        if c == 1:
            matriz[1].append(num)
        if c == 2:
            matriz[2].append(num)
print('=-'*28)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]:^3} ]', end='')
    print()

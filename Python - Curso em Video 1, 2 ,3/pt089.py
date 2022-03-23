print(f'\033[1;33m{" DESAFIO 87 ":#^30}\033[m\n')
matriz = [[], [], []]
par = som = 0
for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite o número que deseja colocar na posição {[c, i]}: '))
        if num % 2 == 0:
            par += num
        if c == 0:
            matriz[0].append(num)
        if c == 1:
            matriz[1].append(num)
        if c == 2:
            matriz[2].append(num)
        if i == 2:
            som += num
print('=-'*28)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]:^3} ]', end='')
    print()
print('=-'*28)
print(f'A soma dos valores pares é: {par}')
print(f'A soma da terceira coluna: {som}')
print(f'O maior número da 2º fila é: {max(matriz[1])}')

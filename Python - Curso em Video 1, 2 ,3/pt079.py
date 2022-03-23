print('\033[1;33m##### DESAFIO 78 #####\033[m\n')
val = []
for c in range(0, 5):
    val.append(int(input(f'Digite um valor na posição {c}: ')))
print('=-'*35)
print(f'Os valores digitados foram: {val}')
print(f'O menor valor foi {min(val)} na(s) posição(ões) ', end='')
for pos, c in enumerate(val):
    if c == min(val):
        print(f'{pos}... ', end='')
print(f'\nO maior valor foi {max(val)} na(s) posição(ões) ', end='')
for pos, c in enumerate(val):
    if c == max(val):
        print(f'{pos}... ', end='')
print('\n\nSee u later\n')

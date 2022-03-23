print('\033[1;33m##### DESAFIO 52 #####\033[m\n')
print('Verificador de números primos.')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi dividido {tot} vezes')
if tot == 2:
    print(f'{num} é Primo')
else:
    print(f'{num} não é primo')

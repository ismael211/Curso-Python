print('\033[1;33m##### DESAFIO 75 #####\033[m\n')
#pá de coisa
num = (int(input('Digite um número: ')), 
    int(input('Digite outro número: ')), 
    int(input('Digite mais um número: ')), 
    int(input('Digite último número: ')))
print(f'\nVocê digitou: {num}')
print(f'\nO 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 aparece na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado')
print(f'Você digitou esses números pares: ', end='')
for c in num:
    if c%2 == 0:
        print(f'{c} ', end='')
print('\n')

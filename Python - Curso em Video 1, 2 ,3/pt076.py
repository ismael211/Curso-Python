print('\033[1;33m##### DESAFIO 76 #####\033[m\n')
print(f'{"Listagem de preço":^30}')
print('='*30)
list = ('Pão', 1, 'Oleo', 5, 'Carne', 98, 'leite', 3)
for pos in range (0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:>6.2f}')
print('='*30)
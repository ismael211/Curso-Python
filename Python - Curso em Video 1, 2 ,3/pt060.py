print('\033[1;33m##### DESAFIO 61 #####\033[m\n')
ter = int(input('Digite o termo: '))
raz = int(input('Digite a razão: '))
termo = ter
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += raz
    cont += 1
print('FIM')
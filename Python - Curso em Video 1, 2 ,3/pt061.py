print('\033[1;33m##### DESAFIO 62 #####\033[m\n')
cont = 0
ter = int(input('Digite o termo: '))
raz = int(input('Digite a razão: '))
termo = ter
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}-'.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSE')
    mais = int(input('Você deseja ver mais quantos termos? '))
print('fim prog')

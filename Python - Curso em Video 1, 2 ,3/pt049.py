print('\033[1;33m##### DESAFIO 51 #####\033[m\n')
#mostre os 10 primeiros da (PA)
cont = 0
ter = int(input('Digite o termo: '))
ter2 = int(input('Digite o termo: '))
raz = int(input('Digite a razão: '))
for c in range (ter, ter2, raz):
    cont += 1
    if cont <= 10:
        print(c)
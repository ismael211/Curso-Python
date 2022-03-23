from datetime import date
print('\033[1;33m##### DESAFIO 54 #####\033[m\n')
#Quantos já fizeram a maior idade
contma = 0
contme = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano você nasceu? '))
    idade = ano - nasc
    if idade >= 21:
        contma += 1
    else:
        contme += 1
print(f'{contma} dessas pessoas são maiores de idade')
print(f'{contme} dessas pessoas são menores de idade')
from datetime import date
print('\033[1;33m##### DESAFIO 41 #####\033[m\n')
ano = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idad = ano - nasc
if idad < 9:
    print('Você está na categoria MIRIM!')
elif idad >= 9 and idad < 14:
    print('Você esta na categoria INFANTIL!')
elif idad >= 14 and idad < 19:
    print('Você está na categoria JUNIOR!')
elif idad >= 19 and idad <= 20:
    print('Você está na categoria SENIOR')
else:
    print('Você está na categoria MASTER!')
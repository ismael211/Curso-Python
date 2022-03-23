print('\033[1;33m##### DESAFIO 40 #####\033[m\n')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1+n2)/2
if med < 6.0:
    print(f'Você está reprovado! Sua média foi {med}')
elif med > 6.0 and med < 8.0:
    print(f'Você está de AV3! Sua média foi {med}')
else:
    print(f'Você está aprovado! Sua média foi {med}')
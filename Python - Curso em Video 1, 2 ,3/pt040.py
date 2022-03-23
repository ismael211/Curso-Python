print('\033[1;33m##### DESAFIO 42 #####\033[m\n')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    if r1 == r2 and r1 == r3:
        print('Esse é um triangulo EQUILATERO.')
    elif r1 == r2 or r1 == r3:
        print('Esse é um triangulo ISÓSCELES.')
    else:
        print('Esse é um triangulo ESCALENO.')
else:
    print('Essas retas não formam um triangulo.')
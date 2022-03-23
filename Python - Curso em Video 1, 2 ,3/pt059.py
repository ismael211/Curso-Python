print('\033[1;33m##### DESAFIO 60 #####\033[m\n')
#fatorial
num = int(input('Digite um número: '))
c = num
fat = 1
print(f'Calculando {num}! = {num}', end='')
while c > 0:
    print(f' x {c}', end='')
    fat *= c
    c -= 1
print(f' = {fat}')

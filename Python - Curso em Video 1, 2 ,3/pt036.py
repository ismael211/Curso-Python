print('\033[1;33m##### DESAFIO 38 #####\033[m\n')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O {n1} é maior que o {n2}')
elif n2 > n1:
    print(f'O {n2} é maior que {n1}')
else:
    print('Os valores são iguais.')
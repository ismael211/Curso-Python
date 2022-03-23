print('\033[1;33m##### DESAFIO 49 #####\033[m\n')
#tabuada
cont = 0
num = int(input('Digite um numero: '))
print('A TABUADA DE {} é:'.format(num))
print('-'*20)
for t in range(1, 11):
    cont += 1
    s = num*cont
    print(f'{num} x {cont} = {s}')
print('-'*20)
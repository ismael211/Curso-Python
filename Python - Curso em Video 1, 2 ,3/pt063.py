print('\033[1;33m##### DESAFIO 64 #####\033[m\n')
som = 0
cont = 0
n = 1
print('~~'*15)
print('0 para terminar')
print('~~'*15)
while n != 0:
    n = int(input('Digite um número: '))
    print('--'*15)
    if n != 0:
        som += n
        cont += 1
print(f'A soma dos {cont} numeros digitados é: {som}')

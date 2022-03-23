print('\033[1;33m##### DESAFIO 50 #####\033[m\n')
#somar os pares
som = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        cont += 1
        som += num
print(' A soma dos {} numeros pares é: {}'.format(cont, som))
#AULA 14 MUNDO - 2
'''senha = ''
while not senha == 'REBANHO':
    senha = str(input('Senha: ')).upper()
    if senha == 'REBANHO':
        print('SENHA CORRETA')
    else:
        print('SENHA INCORRETA. TENTE NOVAMENTE.')
        print('-'*35)'''
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Foram digitados {} numeros pares'.format(par-1))
print('Foram digitados {} numeros impares'.format(impar))
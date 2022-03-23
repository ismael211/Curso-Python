print('\033[1;33m##### DESAFIO 37 #####\033[m\n')
num = int(input('Digite um numero para ser convertido: '))
print('''\n[ 1 ] Para conversão em BINARIO
[ 2 ] Para conversão em OCTAL
[ 3 ] Para conversão em HEXADECIMAL''')
opc = int(input('\nEscolha um numero: '))
if opc == 1:
    print('{} em BINÁRIO fica: {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} em OCTAL fica: {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} em HEXADECIMAL fica: {}'.format(num, hex(num)[2:]))
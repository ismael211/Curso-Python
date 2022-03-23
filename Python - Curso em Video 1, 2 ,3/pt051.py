print('\033[1;33m##### DESAFIO 53 #####\033[m\n')
#Verificador de palindromos
pal = str(input('Digite uma frase: ')).strip().upper()
sep = pal.split()
junto = ''.join(sep)
inver = ''
for palidromo in range(len(junto) -1, -1, -1):
    inver += junto[palidromo]
print(f'O inverso de {junto} é {inver}')
if inver == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo.')
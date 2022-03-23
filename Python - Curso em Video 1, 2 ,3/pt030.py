print("###### DESAFIO 33 ######\n")
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>2:
    maior = n3
menor = n3
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2

print('O maior numero é {}.'.format(maior))
print('O menor numero é {}.'.format(menor))
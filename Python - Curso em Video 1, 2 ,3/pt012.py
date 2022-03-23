from math import hypot
print('######### DESAFIO 17 #########\n')
co = float(input('Qual o valor do Cateto Oposto? '))
ca = float(input('Qual o valor do Cateto Adjacente? '))
h = hypot(co, ca)
print('O valor da Hipotenusa é {:.2f}'.format(h))
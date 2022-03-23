from random import choice
print('######### QUEM VAI PAGAR A PIZZA? #########\n')
a1 = str(input('Participante 1: '))
a2 = str(input('Participante 2: '))
a3 = str(input('Participante 3: '))
a4 = str(input('Participante 4: '))
l = [a1, a2, a3, a4]
e = choice(l)
print(f'PARABÉNS VOCÊ VAI PAGAR A PIZZA: {e}')
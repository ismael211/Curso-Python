from random import randint
#sorteio de números aleatorios, maior e menor.
print('\033[1;33m##### DESAFIO 74 #####\033[m\n')
list = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram: {list}')
print(f'O maior número é {max(list)}\n O menor número é {min(list)}')

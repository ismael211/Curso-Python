from random import randint
from time import sleep
from operator import itemgetter
print(f'\033[1;33m{" DESAFIO 91 ":#^30}\033[m\n')
dado = {'jogador1':0, 'jogador2':0, 'jogador3':0, 'jogador4':0}
ranking = {}
for k in dado:
    dado[k] = randint(1, 6)
print('Valores sorteados: \n')
for k, v in dado.items():
    print(f'O {k} tirou: {v} ')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('\nRANKING DOS JOGADORES\n')
for p, v in enumerate(ranking):
    print(f'{p+1}º lugar  foi {v[0]} que tirou {v[1]}')
    sleep(1)

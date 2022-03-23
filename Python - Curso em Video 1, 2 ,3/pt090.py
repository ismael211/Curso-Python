from random import randint
from time import sleep
print(f'\033[1;33m{" DESAFIO 88 ":#^30}\033[m\n')
sorteio = []
final = []
print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
per = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, per):
    for i in range(0, 6):
        n = randint(1, 60)
        if n not in sorteio:
            sorteio.append(n)
        else:
            i = -1
    sorteio.sort()
    final.append(sorteio[:])
    sorteio.clear()
print(f'\n-=-=-=-=-={f" SORTEANDO {per} JOGO(S)":^20}=-=-=-=-=-\n')
for pos, c in enumerate(final):
    print(f'Jogo {pos+1}: {c}')
    sleep(1)
print(f'\n{" BOA SORTE! ":#^40}\n')

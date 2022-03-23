print(f'\033[1;33m{" DESAFIO 93 ":#^30}\033[m\n')
dado = {}
gol = []
dado['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantos partidas {dado["nome"]} jogou? '))
for c in range(0, jogos):
    gol.append(int(input(f'Quantos gols na partida {c}: ')))
dado['gols'] = gol[:]
dado['total'] = sum(gol)
print('=-'*30)
print(dado)
print('=-'*30)
for k, v in dado.items():
    print(f'O campo {k} tem o valor: {v}')
print('=-'*30)
print(f'O jogador {dado["nome"]} jogou {jogos} partidas')
for c in range(0, jogos):
    print(f'=> Na partida {c}, fez {gol[c]} gols.')
print(f'Foi um total de {dado["total"]} gols.\n')

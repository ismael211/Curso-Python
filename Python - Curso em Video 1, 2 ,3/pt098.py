print(f'\033[1;33m{" DESAFIO 95 ":#^30}\033[m\n')
dado = {}
banco = []
gol = []
while True:
    print('--'*16)
    nome = str(input('Nome do jogador: '))
    dado['nome'] = nome
    jogos = int(input(f'Quantos partidas {nome} jogou? '))
    for c in range(0, jogos):
        gol.append(int(input(f'Quantos gols na partida {c}: ')))
    dado['jogos'] = jogos
    dado['total'] = sum(gol)
    dado['gols'] = gol
    banco.append(dado.copy())
    dado.clear()
    gol.clear()
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print('=-'*16)
print('Nº   Nome      Gols     Total')
print('-'*30)
for p, c in enumerate(banco):
    print(f'{p:<}{c["nome"]:>10}    {c["gols"]}     {c["total"]}')
while True:
    print('-'*30)
    n = int(input('Mostrar dados de qual jogador: '))
    if n == 999:
        break
    elif n >= len(banco):
        print('ERRO! Não existe esse jogador. Tente novamente.')
    else:
        for p, c in enumerate(banco):
            if n == p:
                print(f'--- LEVANTAMENTO DO JOGADOR {c["nome"]}:')
                for j in range(0, c['jogos']):
                    print(f'=> Na partida {j} fez {c["gols"][j]} gols.')
print('\n---- ENCERRADO ----\n')

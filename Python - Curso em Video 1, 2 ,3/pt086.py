print(f'\033[1;33m{" DESAFIO 84 ":#^25}\033[m\n')
dados = []
analise = []
mlev = []
mpe = []
esc = ''
pos = pes = lev = 0
while True:
    dados.append(str(input('Qual seu nome? ')))
    dados.append(int(input('Qual seu peso? ')))
    analise.append(dados[:])
    if pos == 0:
        pes = dados[1]
        lev = dados[1]
    else:
        if pes < dados[1]:
            pes = dados[1]
        if lev > dados[1]:
            lev = dados[1]
    dados.clear()
    pos += 1
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print(f'Foram cadastradas {len(analise)} pessoas')
print(f'O maior peso é: {pes}kg. Peso do(a) ', end='')
for c in analise:
    if pes == c[1]:
        print(f'[{c[0]}] ', end='')
print()
print(f'O menor peso é: {lev}kg. Peso do(a) ', end='')
for c in analise:
    if lev == c[1]:
        print(f'[{c[0]}] ', end='')
print()
